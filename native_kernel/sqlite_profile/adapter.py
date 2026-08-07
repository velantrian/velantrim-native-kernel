from __future__ import annotations

import json
import re
import sqlite3
import uuid
from collections.abc import Callable, Iterable
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Protocol

from native_kernel.semantic_core.canonical import canonical_json_bytes
from native_kernel.semantic_core.errors import ContractViolation
from native_kernel.semantic_core.models import Command, EventType

from .errors import (
    IdempotencyConflict,
    ImportConflict,
    MigrationDrift,
    StaleWriterEpoch,
    StoredEventCorrupt,
    UnknownKernelInstance,
    WriterLeaseBusy,
    WriterLeaseExpired,
)
from .hashing import build_event_envelope, event_hash, payload_hash
from .models import AppendResult, AppendStatus, StoredEvent, WriterToken

PROFILE_ID = "native-kernel/sqlite-embedded"
PROFILE_VERSION = "0.5-p5"
EVIDENCE_LINEAGE = "clean/sqlite-embedded/0.1"
_ID_RE = re.compile(r"^[a-z0-9][a-z0-9._:/-]{0,127}$")


class AuthorityPort(Protocol):
    def require(self, command: Command) -> Any: ...


FaultHook = Callable[[StoredEvent], None]
Clock = Callable[[], datetime]
EventIdFactory = Callable[[], str]


MIGRATIONS: tuple[tuple[str, str], ...] = (
    (
        "0001-p5-sqlite-core",
        """
        CREATE TABLE IF NOT EXISTS schema_migrations(
            version TEXT PRIMARY KEY,
            digest TEXT NOT NULL,
            applied_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS kernel_instances(
            instance_id TEXT PRIMARY KEY,
            profile_id TEXT NOT NULL,
            evidence_lineage TEXT NOT NULL,
            last_global_seq INTEGER NOT NULL DEFAULT 0 CHECK(last_global_seq >= 0),
            last_event_hash TEXT,
            writer_epoch INTEGER NOT NULL DEFAULT 0 CHECK(writer_epoch >= 0),
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS writer_leases(
            instance_id TEXT PRIMARY KEY REFERENCES kernel_instances(instance_id) ON DELETE CASCADE,
            owner_id TEXT NOT NULL,
            epoch INTEGER NOT NULL CHECK(epoch >= 1),
            expires_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS stream_counters(
            instance_id TEXT NOT NULL REFERENCES kernel_instances(instance_id) ON DELETE CASCADE,
            stream_id TEXT NOT NULL,
            last_stream_seq INTEGER NOT NULL DEFAULT 0 CHECK(last_stream_seq >= 0),
            PRIMARY KEY(instance_id, stream_id)
        );
        CREATE TABLE IF NOT EXISTS events(
            instance_id TEXT NOT NULL REFERENCES kernel_instances(instance_id) ON DELETE CASCADE,
            global_seq INTEGER NOT NULL CHECK(global_seq >= 1),
            event_id TEXT NOT NULL UNIQUE,
            command_id TEXT NOT NULL,
            command_contract TEXT NOT NULL,
            idempotency_key TEXT NOT NULL,
            command_digest TEXT NOT NULL,
            stream_id TEXT NOT NULL,
            stream_seq INTEGER NOT NULL CHECK(stream_seq >= 1),
            actor_ref TEXT NOT NULL,
            authority_ref TEXT NOT NULL,
            recorded_at TEXT NOT NULL,
            event_type TEXT NOT NULL,
            schema_version TEXT NOT NULL,
            payload_text TEXT NOT NULL,
            payload_canonical BLOB NOT NULL,
            prev_global_hash TEXT NOT NULL,
            payload_hash TEXT NOT NULL,
            event_hash TEXT NOT NULL,
            envelope_canonical BLOB NOT NULL,
            writer_epoch INTEGER NOT NULL CHECK(writer_epoch >= 1),
            PRIMARY KEY(instance_id, global_seq),
            UNIQUE(instance_id, stream_id, stream_seq)
        );
        CREATE TABLE IF NOT EXISTS idempotency_records(
            instance_id TEXT NOT NULL REFERENCES kernel_instances(instance_id) ON DELETE CASCADE,
            command_contract TEXT NOT NULL,
            idempotency_key TEXT NOT NULL,
            command_digest TEXT NOT NULL,
            global_seq INTEGER NOT NULL,
            event_hash TEXT NOT NULL,
            PRIMARY KEY(instance_id, command_contract, idempotency_key),
            FOREIGN KEY(instance_id, global_seq) REFERENCES events(instance_id, global_seq)
        );
        CREATE INDEX IF NOT EXISTS idx_events_instance_stream
            ON events(instance_id, stream_id, stream_seq);
        """,
    ),
    (
        "0002-p5-sqlite-replay",
        """
        CREATE TABLE IF NOT EXISTS operation_receipts(
            receipt_id TEXT PRIMARY KEY,
            operation_type TEXT NOT NULL,
            instance_id TEXT NOT NULL REFERENCES kernel_instances(instance_id) ON DELETE CASCADE,
            event_count INTEGER NOT NULL,
            first_global_seq INTEGER NOT NULL,
            last_global_seq INTEGER NOT NULL,
            last_event_hash TEXT,
            state_digest TEXT NOT NULL,
            known_limits_text TEXT NOT NULL,
            projection_name TEXT,
            projection_generation INTEGER,
            reducer_version TEXT NOT NULL,
            target_schema_version TEXT NOT NULL,
            created_at TEXT NOT NULL,
            canonical_bytes BLOB NOT NULL,
            receipt_hash TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_receipts_instance_operation
            ON operation_receipts(instance_id, operation_type, projection_name, projection_generation);
        CREATE TABLE IF NOT EXISTS projections(
            instance_id TEXT NOT NULL REFERENCES kernel_instances(instance_id) ON DELETE CASCADE,
            projection_name TEXT NOT NULL,
            reducer_version TEXT NOT NULL,
            target_schema_version TEXT NOT NULL,
            generation INTEGER NOT NULL CHECK(generation >= 1),
            last_global_seq INTEGER NOT NULL CHECK(last_global_seq >= 0),
            last_event_hash TEXT,
            state_text TEXT NOT NULL,
            state_canonical BLOB NOT NULL,
            state_digest TEXT NOT NULL,
            receipt_id TEXT NOT NULL REFERENCES operation_receipts(receipt_id),
            rebuilt_at TEXT NOT NULL,
            PRIMARY KEY(instance_id, projection_name)
        );
        """,
    ),
)


def _require_id(name: str, value: object) -> str:
    if not isinstance(value, str) or not _ID_RE.fullmatch(value):
        raise ContractViolation(f"{name} must match {_ID_RE.pattern}")
    return value


def _require_ttl(ttl_seconds: object) -> int:
    if isinstance(ttl_seconds, bool) or not isinstance(ttl_seconds, int) or not 1 <= ttl_seconds <= 3600:
        raise ContractViolation("ttl_seconds must be an integer in [1, 3600]")
    return ttl_seconds


def _utc_second(value: datetime) -> datetime:
    if not isinstance(value, datetime) or value.tzinfo is None:
        raise ContractViolation("clock must return a timezone-aware datetime")
    return value.astimezone(timezone.utc).replace(microsecond=0)


def _format_time(value: datetime) -> str:
    return _utc_second(value).strftime("%Y-%m-%dT%H:%M:%SZ")


def _parse_time(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def _default_clock() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def _migration_digest(sql: str) -> str:
    import hashlib

    return hashlib.sha256(sql.encode("utf-8")).hexdigest()


class SQLiteAppendStore:
    """Independent embedded P5 append/idempotency adapter.

    The implementation uses Python stdlib sqlite3 and BEGIN IMMEDIATE for the
    declared single-writer envelope. It does not emulate PostgreSQL SQL,
    locking or operational capabilities.
    """

    def __init__(
        self,
        database_path: str | Path,
        authority: AuthorityPort,
        *,
        fault_hook: FaultHook | None = None,
        clock: Clock | None = None,
        event_id_factory: EventIdFactory | None = None,
        timeout_seconds: float = 5.0,
    ) -> None:
        path = str(database_path)
        if not path:
            raise ContractViolation("database_path must be non-empty")
        if not hasattr(authority, "require"):
            raise ContractViolation("authority must expose require(command)")
        if fault_hook is not None and not callable(fault_hook):
            raise ContractViolation("fault_hook must be callable")
        if clock is not None and not callable(clock):
            raise ContractViolation("clock must be callable")
        if event_id_factory is not None and not callable(event_id_factory):
            raise ContractViolation("event_id_factory must be callable")
        if not isinstance(timeout_seconds, (int, float)) or timeout_seconds <= 0:
            raise ContractViolation("timeout_seconds must be positive")
        self.database_path = path
        self._authority = authority
        self._fault_hook = fault_hook
        self._clock = clock or _default_clock
        self._event_id_factory = event_id_factory or (lambda: "event:" + uuid.uuid4().hex)
        self._timeout = float(timeout_seconds)

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(
            self.database_path,
            timeout=self._timeout,
            isolation_level=None,
        )
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("PRAGMA busy_timeout = 5000")
        connection.execute("PRAGMA journal_mode = WAL")
        connection.execute("PRAGMA synchronous = FULL")
        return connection

    @contextmanager
    def _transaction(self, *, immediate: bool = True) -> Iterable[sqlite3.Connection]:
        connection = self._connect()
        try:
            connection.execute("BEGIN IMMEDIATE" if immediate else "BEGIN")
            yield connection
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def migrate(self) -> tuple[str, ...]:
        applied: list[str] = []
        with self._transaction() as connection:
            connection.execute(
                "CREATE TABLE IF NOT EXISTS schema_migrations("
                "version TEXT PRIMARY KEY, digest TEXT NOT NULL, applied_at TEXT NOT NULL)"
            )
            for version, sql in MIGRATIONS:
                digest = _migration_digest(sql)
                row = connection.execute(
                    "SELECT digest FROM schema_migrations WHERE version = ?",
                    (version,),
                ).fetchone()
                if row is not None:
                    if row["digest"] != digest:
                        raise MigrationDrift(version)
                    continue
                connection.executescript(sql)
                connection.execute(
                    "INSERT INTO schema_migrations(version, digest, applied_at) VALUES(?,?,?)",
                    (version, digest, _format_time(self._clock())),
                )
                applied.append(version)
        return tuple(applied)

    def register_instance(self, instance_id: str) -> None:
        instance = _require_id("instance_id", instance_id)
        now = _format_time(self._clock())
        with self._transaction() as connection:
            connection.execute(
                "INSERT OR IGNORE INTO kernel_instances("
                "instance_id, profile_id, evidence_lineage, created_at, updated_at"
                ") VALUES(?,?,?,?,?)",
                (instance, PROFILE_ID, EVIDENCE_LINEAGE, now, now),
            )
            row = connection.execute(
                "SELECT profile_id, evidence_lineage FROM kernel_instances WHERE instance_id = ?",
                (instance,),
            ).fetchone()
            if row is None:
                raise UnknownKernelInstance(instance)
            if (row["profile_id"], row["evidence_lineage"]) != (PROFILE_ID, EVIDENCE_LINEAGE):
                raise ContractViolation("instance exists under a different profile/evidence lineage")

    def acquire_writer_lease(
        self,
        instance_id: str,
        owner_id: str,
        *,
        ttl_seconds: int = 30,
    ) -> WriterToken:
        instance = _require_id("instance_id", instance_id)
        owner = _require_id("owner_id", owner_id)
        ttl = _require_ttl(ttl_seconds)
        now = _utc_second(self._clock())
        expires = now + timedelta(seconds=ttl)
        with self._transaction() as connection:
            instance_row = connection.execute(
                "SELECT writer_epoch FROM kernel_instances WHERE instance_id = ?",
                (instance,),
            ).fetchone()
            if instance_row is None:
                raise UnknownKernelInstance(instance)
            current_epoch = int(instance_row["writer_epoch"])
            lease = connection.execute(
                "SELECT owner_id, epoch, expires_at FROM writer_leases WHERE instance_id = ?",
                (instance,),
            ).fetchone()
            reuse = False
            if lease is not None:
                stored_expiry = _parse_time(lease["expires_at"])
                if int(lease["epoch"]) != current_epoch:
                    raise StoredEventCorrupt("writer lease epoch differs from instance epoch")
                if stored_expiry > now and lease["owner_id"] != owner:
                    raise WriterLeaseBusy(
                        f"instance {instance} is leased by {lease['owner_id']} until {lease['expires_at']}"
                    )
                reuse = stored_expiry > now and lease["owner_id"] == owner
            epoch = current_epoch if reuse else current_epoch + 1
            if not reuse:
                connection.execute(
                    "UPDATE kernel_instances SET writer_epoch = ?, updated_at = ? WHERE instance_id = ?",
                    (epoch, _format_time(now), instance),
                )
            connection.execute(
                "INSERT INTO writer_leases(instance_id, owner_id, epoch, expires_at, updated_at) "
                "VALUES(?,?,?,?,?) ON CONFLICT(instance_id) DO UPDATE SET "
                "owner_id=excluded.owner_id, epoch=excluded.epoch, "
                "expires_at=excluded.expires_at, updated_at=excluded.updated_at",
                (instance, owner, epoch, _format_time(expires), _format_time(now)),
            )
        return WriterToken(instance, owner, epoch, expires)

    def renew_writer_lease(self, token: WriterToken, *, ttl_seconds: int = 30) -> WriterToken:
        if not isinstance(token, WriterToken):
            raise ContractViolation("token must be WriterToken")
        ttl = _require_ttl(ttl_seconds)
        now = _utc_second(self._clock())
        expires = now + timedelta(seconds=ttl)
        with self._transaction() as connection:
            self._validate_lease(connection, token, now)
            cursor = connection.execute(
                "UPDATE writer_leases SET expires_at=?, updated_at=? "
                "WHERE instance_id=? AND owner_id=? AND epoch=?",
                (_format_time(expires), _format_time(now), token.instance_id, token.owner_id, token.epoch),
            )
            if cursor.rowcount != 1:
                raise StaleWriterEpoch("writer lease changed before renewal")
        return WriterToken(token.instance_id, token.owner_id, token.epoch, expires)

    def release_writer_lease(self, token: WriterToken) -> None:
        if not isinstance(token, WriterToken):
            raise ContractViolation("token must be WriterToken")
        now = _utc_second(self._clock())
        with self._transaction() as connection:
            self._validate_lease(connection, token, now)
            connection.execute(
                "UPDATE writer_leases SET expires_at=?, updated_at=? "
                "WHERE instance_id=? AND owner_id=? AND epoch=?",
                (_format_time(now), _format_time(now), token.instance_id, token.owner_id, token.epoch),
            )

    def append(self, command: Command, token: WriterToken) -> AppendResult:
        if not isinstance(command, Command):
            raise ContractViolation("command must be Command")
        if not isinstance(token, WriterToken):
            raise ContractViolation("token must be WriterToken")
        self._authority.require(command)
        now = _utc_second(self._clock())
        with self._transaction() as connection:
            instance_row = self._validate_lease(connection, token, now)
            existing = connection.execute(
                "SELECT command_digest, global_seq, event_hash FROM idempotency_records "
                "WHERE instance_id=? AND command_contract=? AND idempotency_key=?",
                (token.instance_id, command.contract, command.idempotency_key),
            ).fetchone()
            if existing is not None:
                if existing["command_digest"] != command.digest:
                    raise IdempotencyConflict(
                        f"{token.instance_id}/{command.contract}/{command.idempotency_key}"
                    )
                event = self._load_event(connection, token.instance_id, int(existing["global_seq"]))
                if event.command_digest != existing["command_digest"] or event.event_hash != existing["event_hash"]:
                    raise StoredEventCorrupt("idempotency record differs from referenced event")
                return AppendResult(AppendStatus.RETURN_ORIGINAL_APPEND_RESULT, event)

            global_seq = int(instance_row["last_global_seq"]) + 1
            stream_row = connection.execute(
                "SELECT last_stream_seq FROM stream_counters WHERE instance_id=? AND stream_id=?",
                (token.instance_id, command.stream_id),
            ).fetchone()
            stream_seq = (int(stream_row["last_stream_seq"]) if stream_row else 0) + 1
            event_id = self._event_id_factory()
            _require_id("event_id", event_id)
            prev_hash = instance_row["last_event_hash"] or "GENESIS"
            envelope, payload_bytes, envelope_bytes = build_event_envelope(
                command,
                event_id=event_id,
                global_seq=global_seq,
                stream_seq=stream_seq,
                recorded_at=now,
                prev_global_hash=prev_hash,
            )
            connection.execute(
                "INSERT INTO events(instance_id,global_seq,event_id,command_id,command_contract,"
                "idempotency_key,command_digest,stream_id,stream_seq,actor_ref,authority_ref,"
                "recorded_at,event_type,schema_version,payload_text,payload_canonical,"
                "prev_global_hash,payload_hash,event_hash,envelope_canonical,writer_epoch) "
                "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    token.instance_id, global_seq, event_id, command.command_id, command.contract,
                    command.idempotency_key, command.digest, command.stream_id, stream_seq,
                    command.actor_ref, command.authority_ref, _format_time(now),
                    command.event_type.value, command.schema_version,
                    payload_bytes.decode("utf-8"), payload_bytes, prev_hash,
                    envelope["payload_hash"], envelope["event_hash"], envelope_bytes, token.epoch,
                ),
            )
            connection.execute(
                "INSERT INTO stream_counters(instance_id,stream_id,last_stream_seq) VALUES(?,?,?) "
                "ON CONFLICT(instance_id,stream_id) DO UPDATE SET last_stream_seq=excluded.last_stream_seq",
                (token.instance_id, command.stream_id, stream_seq),
            )
            connection.execute(
                "UPDATE kernel_instances SET last_global_seq=?, last_event_hash=?, updated_at=? "
                "WHERE instance_id=?",
                (global_seq, envelope["event_hash"], _format_time(now), token.instance_id),
            )
            connection.execute(
                "INSERT INTO idempotency_records(instance_id,command_contract,idempotency_key,"
                "command_digest,global_seq,event_hash) VALUES(?,?,?,?,?,?)",
                (token.instance_id, command.contract, command.idempotency_key,
                 command.digest, global_seq, envelope["event_hash"]),
            )
            event = StoredEvent(
                instance_id=token.instance_id,
                event_id=event_id,
                command_id=command.command_id,
                idempotency_key=command.idempotency_key,
                command_contract=command.contract,
                command_digest=command.digest,
                stream_id=command.stream_id,
                global_seq=global_seq,
                stream_seq=stream_seq,
                actor_ref=command.actor_ref,
                authority_ref=command.authority_ref,
                recorded_at=now,
                event_type=command.event_type,
                schema_version=command.schema_version,
                payload=command.as_contract_object()["payload"],
                prev_global_hash=prev_hash,
                payload_hash=envelope["payload_hash"],
                event_hash=envelope["event_hash"],
                writer_epoch=token.epoch,
                payload_canonical=payload_bytes,
                envelope_canonical=envelope_bytes,
            )
            if self._fault_hook is not None:
                self._fault_hook(event)
            return AppendResult(AppendStatus.APPENDED, event)

    def import_history(self, instance_id: str, events: Iterable[Any]) -> int:
        """Import a complete exact Event history into an empty SQLite instance.

        The source objects may come from another profile but must expose the
        StoredEvent attribute set. Canonical bytes and hashes are preserved.
        """
        instance = _require_id("instance_id", instance_id)
        source = tuple(events)
        with self._transaction() as connection:
            head = connection.execute(
                "SELECT last_global_seq, last_event_hash, writer_epoch FROM kernel_instances WHERE instance_id=?",
                (instance,),
            ).fetchone()
            if head is None:
                raise UnknownKernelInstance(instance)
            if int(head["last_global_seq"]) != 0 or connection.execute(
                "SELECT count(*) AS n FROM events WHERE instance_id=?", (instance,)
            ).fetchone()["n"] != 0:
                raise ImportConflict("target instance must be empty")
            previous_hash = "GENESIS"
            stream_heads: dict[str, int] = {}
            for index, item in enumerate(source, start=1):
                event = self._coerce_imported_event(instance, item)
                if event.global_seq != index:
                    raise ImportConflict("imported global sequence must be contiguous from 1")
                expected_stream = stream_heads.get(event.stream_id, 0) + 1
                if event.stream_seq != expected_stream:
                    raise ImportConflict("imported stream sequence is not contiguous")
                if event.prev_global_hash != previous_hash:
                    raise ImportConflict("imported global hash chain is discontinuous")
                self._verify_event(event)
                connection.execute(
                    "INSERT INTO events(instance_id,global_seq,event_id,command_id,command_contract,"
                    "idempotency_key,command_digest,stream_id,stream_seq,actor_ref,authority_ref,"
                    "recorded_at,event_type,schema_version,payload_text,payload_canonical,"
                    "prev_global_hash,payload_hash,event_hash,envelope_canonical,writer_epoch) "
                    "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (
                        instance, event.global_seq, event.event_id, event.command_id,
                        event.command_contract, event.idempotency_key, event.command_digest,
                        event.stream_id, event.stream_seq, event.actor_ref, event.authority_ref,
                        _format_time(event.recorded_at), event.event_type.value,
                        event.schema_version, event.payload_canonical.decode("utf-8"),
                        event.payload_canonical, event.prev_global_hash, event.payload_hash,
                        event.event_hash, event.envelope_canonical, event.writer_epoch,
                    ),
                )
                connection.execute(
                    "INSERT INTO idempotency_records(instance_id,command_contract,idempotency_key,"
                    "command_digest,global_seq,event_hash) VALUES(?,?,?,?,?,?)",
                    (instance, event.command_contract, event.idempotency_key,
                     event.command_digest, event.global_seq, event.event_hash),
                )
                stream_heads[event.stream_id] = event.stream_seq
                previous_hash = event.event_hash
            for stream_id, sequence in stream_heads.items():
                connection.execute(
                    "INSERT INTO stream_counters(instance_id,stream_id,last_stream_seq) VALUES(?,?,?)",
                    (instance, stream_id, sequence),
                )
            if source:
                connection.execute(
                    "UPDATE kernel_instances SET last_global_seq=?, last_event_hash=?, "
                    "writer_epoch=?, updated_at=? WHERE instance_id=?",
                    (len(source), previous_hash, max(int(getattr(item, "writer_epoch")) for item in source),
                     _format_time(self._clock()), instance),
                )
        return len(source)

    def read_events(self, instance_id: str) -> tuple[StoredEvent, ...]:
        instance = _require_id("instance_id", instance_id)
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT global_seq FROM events WHERE instance_id=? ORDER BY global_seq",
                (instance,),
            ).fetchall()
            return tuple(self._load_event(connection, instance, int(row["global_seq"])) for row in rows)

    def count_events(self, instance_id: str) -> int:
        instance = _require_id("instance_id", instance_id)
        with self._connect() as connection:
            row = connection.execute(
                "SELECT count(*) AS n FROM events WHERE instance_id=?", (instance,)
            ).fetchone()
            return int(row["n"])

    def corrupt_payload_canonical_for_test(self, instance_id: str, global_seq: int, value: bytes) -> None:
        with self._transaction() as connection:
            connection.execute(
                "UPDATE events SET payload_canonical=? WHERE instance_id=? AND global_seq=?",
                (value, _require_id("instance_id", instance_id), global_seq),
            )

    def _validate_lease(
        self,
        connection: sqlite3.Connection,
        token: WriterToken,
        now: datetime,
    ) -> sqlite3.Row:
        instance = connection.execute(
            "SELECT last_global_seq,last_event_hash,writer_epoch FROM kernel_instances WHERE instance_id=?",
            (token.instance_id,),
        ).fetchone()
        if instance is None:
            raise UnknownKernelInstance(token.instance_id)
        lease = connection.execute(
            "SELECT owner_id,epoch,expires_at FROM writer_leases WHERE instance_id=?",
            (token.instance_id,),
        ).fetchone()
        if lease is None:
            raise WriterLeaseExpired(token.instance_id)
        if int(instance["writer_epoch"]) != token.epoch or int(lease["epoch"]) != token.epoch or lease["owner_id"] != token.owner_id:
            raise StaleWriterEpoch(token.instance_id)
        if _parse_time(lease["expires_at"]) <= now:
            raise WriterLeaseExpired(token.instance_id)
        return instance

    @staticmethod
    def _coerce_imported_event(instance_id: str, item: Any) -> StoredEvent:
        return StoredEvent(
            instance_id=instance_id,
            event_id=item.event_id,
            command_id=item.command_id,
            idempotency_key=item.idempotency_key,
            command_contract=item.command_contract,
            command_digest=item.command_digest,
            stream_id=item.stream_id,
            global_seq=int(item.global_seq),
            stream_seq=int(item.stream_seq),
            actor_ref=item.actor_ref,
            authority_ref=item.authority_ref,
            recorded_at=item.recorded_at,
            event_type=item.event_type,
            schema_version=item.schema_version,
            payload=item.payload,
            prev_global_hash=item.prev_global_hash,
            payload_hash=item.payload_hash,
            event_hash=item.event_hash,
            writer_epoch=int(item.writer_epoch),
            payload_canonical=bytes(item.payload_canonical),
            envelope_canonical=bytes(item.envelope_canonical),
        )

    @staticmethod
    def _verify_event(event: StoredEvent) -> None:
        payload_object = json.loads(event.payload_canonical.decode("utf-8"))
        if canonical_json_bytes(payload_object) != event.payload_canonical:
            raise StoredEventCorrupt("payload canonical bytes mismatch")
        if payload_hash(payload_object) != event.payload_hash:
            raise StoredEventCorrupt("payload hash mismatch")
        envelope = json.loads(event.envelope_canonical.decode("utf-8"))
        if canonical_json_bytes(envelope) != event.envelope_canonical:
            raise StoredEventCorrupt("envelope canonical bytes mismatch")
        declared_hash = envelope.pop("event_hash", None)
        if declared_hash != event.event_hash or event_hash(envelope) != event.event_hash:
            raise StoredEventCorrupt("event hash mismatch")
        if envelope.get("payload_hash") != event.payload_hash:
            raise StoredEventCorrupt("envelope payload hash mismatch")
        expected = {
            "event_id": event.event_id,
            "command_id": event.command_id,
            "idempotency_key": event.idempotency_key,
            "stream_id": event.stream_id,
            "global_seq": event.global_seq,
            "stream_seq": event.stream_seq,
            "actor_ref": event.actor_ref,
            "authority_ref": event.authority_ref,
            "event_type": event.event_type.value,
            "schema_version": event.schema_version,
            "prev_global_hash": event.prev_global_hash,
        }
        for key, value in expected.items():
            if envelope.get(key) != value:
                raise StoredEventCorrupt(f"envelope field {key} mismatch")

    @classmethod
    def _load_event(cls, connection: sqlite3.Connection, instance_id: str, global_seq: int) -> StoredEvent:
        row = connection.execute(
            "SELECT * FROM events WHERE instance_id=? AND global_seq=?",
            (instance_id, global_seq),
        ).fetchone()
        if row is None:
            raise StoredEventCorrupt(f"missing Event {instance_id}/{global_seq}")
        payload_bytes = bytes(row["payload_canonical"])
        envelope_bytes = bytes(row["envelope_canonical"])
        payload = json.loads(row["payload_text"])
        event = StoredEvent(
            instance_id=instance_id,
            event_id=row["event_id"],
            command_id=row["command_id"],
            idempotency_key=row["idempotency_key"],
            command_contract=row["command_contract"],
            command_digest=row["command_digest"],
            stream_id=row["stream_id"],
            global_seq=int(row["global_seq"]),
            stream_seq=int(row["stream_seq"]),
            actor_ref=row["actor_ref"],
            authority_ref=row["authority_ref"],
            recorded_at=_parse_time(row["recorded_at"]),
            event_type=EventType(row["event_type"]),
            schema_version=row["schema_version"],
            payload=payload,
            prev_global_hash=row["prev_global_hash"],
            payload_hash=row["payload_hash"],
            event_hash=row["event_hash"],
            writer_epoch=int(row["writer_epoch"]),
            payload_canonical=payload_bytes,
            envelope_canonical=envelope_bytes,
        )
        cls._verify_event(event)
        if canonical_json_bytes(payload) != payload_bytes:
            raise StoredEventCorrupt("payload_text differs from canonical payload bytes")
        return event
