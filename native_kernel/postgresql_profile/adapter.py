from __future__ import annotations

import json
import re
import uuid
from collections.abc import Callable
from datetime import timezone
from typing import Any, Protocol

from native_kernel.semantic_core.canonical import canonical_json_bytes
from native_kernel.semantic_core.errors import ContractViolation
from native_kernel.semantic_core.models import Command, EventType

from .errors import (
    DriverUnavailable,
    IdempotencyConflict,
    StaleWriterEpoch,
    StoredEventCorrupt,
    UnknownKernelInstance,
    WriterLeaseBusy,
    WriterLeaseExpired,
)
from .hashing import build_event_envelope, event_hash, payload_hash
from .migrations import apply_migrations
from .models import AppendResult, AppendStatus, StoredEvent, WriterToken

PROFILE_ID = "native-kernel/postgresql-reference"
EVIDENCE_LINEAGE = "clean/postgresql-reference/0.1"
_ID_RE = re.compile(r"^[a-z0-9][a-z0-9._:/-]{0,127}$")


class AuthorityPort(Protocol):
    def require(self, command: Command) -> Any: ...


ConnectionFactory = Callable[[], Any]
FaultHook = Callable[[StoredEvent], None]


def _require_id(name: str, value: object) -> str:
    if not isinstance(value, str) or not _ID_RE.fullmatch(value):
        raise ContractViolation(f"{name} must match {_ID_RE.pattern}")
    return value


def _require_ttl(ttl_seconds: object) -> int:
    if isinstance(ttl_seconds, bool) or not isinstance(ttl_seconds, int) or not 1 <= ttl_seconds <= 3600:
        raise ContractViolation("ttl_seconds must be an integer in [1, 3600]")
    return ttl_seconds


def _load_psycopg() -> Any:
    try:
        import psycopg  # type: ignore[import-not-found]
    except ImportError as exc:
        raise DriverUnavailable(
            'P2 requires psycopg >=3.3,<3.4; install "psycopg[binary]>=3.3,<3.4" for local/CI use'
        ) from exc
    return psycopg


def connection_factory_from_dsn(dsn: str) -> ConnectionFactory:
    if not isinstance(dsn, str) or not dsn:
        raise ContractViolation("dsn must be a non-empty string")

    def factory() -> Any:
        return _load_psycopg().connect(dsn, autocommit=False)

    return factory


class PostgreSQLAppendStore:
    """Bounded P2 append/idempotency adapter.

    No projection, replay/upcasting, network API, deletion execution or
    assertion-scoped conformance is implemented here.
    """

    def __init__(
        self,
        connection_factory: ConnectionFactory,
        authority: AuthorityPort,
        *,
        fault_hook: FaultHook | None = None,
    ) -> None:
        if not callable(connection_factory):
            raise ContractViolation("connection_factory must be callable")
        if not hasattr(authority, "require"):
            raise ContractViolation("authority must expose require(command)")
        if fault_hook is not None and not callable(fault_hook):
            raise ContractViolation("fault_hook must be callable")
        self._connect = connection_factory
        self._authority = authority
        self._fault_hook = fault_hook

    @classmethod
    def from_dsn(
        cls,
        dsn: str,
        authority: AuthorityPort,
        *,
        fault_hook: FaultHook | None = None,
    ) -> "PostgreSQLAppendStore":
        return cls(connection_factory_from_dsn(dsn), authority, fault_hook=fault_hook)

    def migrate(self) -> tuple[str, ...]:
        with self._connect() as connection:
            return apply_migrations(connection)

    def register_instance(self, instance_id: str) -> None:
        _require_id("instance_id", instance_id)
        with self._connect() as connection:
            with connection.transaction(), connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO native_kernel.kernel_instances(
                        instance_id, profile_id, evidence_lineage
                    ) VALUES (%s, %s, %s)
                    ON CONFLICT (instance_id) DO NOTHING
                    """,
                    (instance_id, PROFILE_ID, EVIDENCE_LINEAGE),
                )
                cursor.execute(
                    "SELECT profile_id, evidence_lineage FROM native_kernel.kernel_instances WHERE instance_id = %s",
                    (instance_id,),
                )
                row = cursor.fetchone()
                if row is None:
                    raise UnknownKernelInstance(instance_id)
                if row != (PROFILE_ID, EVIDENCE_LINEAGE):
                    raise ContractViolation("instance exists under a different profile/evidence lineage")

    def acquire_writer_lease(
        self,
        instance_id: str,
        owner_id: str,
        *,
        ttl_seconds: int = 30,
    ) -> WriterToken:
        _require_id("instance_id", instance_id)
        _require_id("owner_id", owner_id)
        ttl = _require_ttl(ttl_seconds)
        with self._connect() as connection:
            with connection.transaction(), connection.cursor() as cursor:
                _, _, current_epoch = self._lock_instance(cursor, instance_id)
                cursor.execute(
                    """
                    SELECT owner_id, epoch, expires_at, transaction_timestamp()
                    FROM native_kernel.writer_leases
                    WHERE instance_id = %s
                    FOR UPDATE
                    """,
                    (instance_id,),
                )
                row = cursor.fetchone()
                reuse = False
                if row is not None:
                    stored_owner, stored_epoch, expires_at, now = row
                    if stored_epoch != current_epoch:
                        raise StoredEventCorrupt(
                            f"writer lease epoch {stored_epoch} differs from instance epoch {current_epoch}"
                        )
                    if expires_at > now and stored_owner != owner_id:
                        raise WriterLeaseBusy(
                            f"instance {instance_id} is leased by {stored_owner} until {expires_at.isoformat()}"
                        )
                    reuse = expires_at > now and stored_owner == owner_id
                epoch = current_epoch if reuse else current_epoch + 1
                if not reuse:
                    cursor.execute(
                        """
                        UPDATE native_kernel.kernel_instances
                        SET writer_epoch = %s, updated_at = transaction_timestamp()
                        WHERE instance_id = %s
                        """,
                        (epoch, instance_id),
                    )
                cursor.execute(
                    """
                    INSERT INTO native_kernel.writer_leases(
                        instance_id, owner_id, epoch, expires_at, updated_at
                    ) VALUES (
                        %s, %s, %s,
                        transaction_timestamp() + (%s * interval '1 second'),
                        transaction_timestamp()
                    )
                    ON CONFLICT (instance_id) DO UPDATE SET
                        owner_id = EXCLUDED.owner_id,
                        epoch = EXCLUDED.epoch,
                        expires_at = EXCLUDED.expires_at,
                        updated_at = transaction_timestamp()
                    RETURNING expires_at
                    """,
                    (instance_id, owner_id, epoch, ttl),
                )
                expires_at = cursor.fetchone()[0]
        return WriterToken(instance_id, owner_id, epoch, expires_at)

    def renew_writer_lease(self, token: WriterToken, *, ttl_seconds: int = 30) -> WriterToken:
        if not isinstance(token, WriterToken):
            raise ContractViolation("token must be WriterToken")
        ttl = _require_ttl(ttl_seconds)
        with self._connect() as connection:
            with connection.transaction(), connection.cursor() as cursor:
                self._lock_and_validate_lease(cursor, token)
                cursor.execute(
                    """
                    UPDATE native_kernel.writer_leases
                    SET expires_at = transaction_timestamp() + (%s * interval '1 second'),
                        updated_at = transaction_timestamp()
                    WHERE instance_id = %s AND owner_id = %s AND epoch = %s
                    RETURNING expires_at
                    """,
                    (ttl, token.instance_id, token.owner_id, token.epoch),
                )
                row = cursor.fetchone()
                if row is None:
                    raise StaleWriterEpoch("writer lease changed before renewal")
                expires_at = row[0]
        return WriterToken(token.instance_id, token.owner_id, token.epoch, expires_at)

    def release_writer_lease(self, token: WriterToken) -> None:
        if not isinstance(token, WriterToken):
            raise ContractViolation("token must be WriterToken")
        with self._connect() as connection:
            with connection.transaction(), connection.cursor() as cursor:
                self._lock_and_validate_lease(cursor, token)
                cursor.execute(
                    """
                    UPDATE native_kernel.writer_leases
                    SET expires_at = transaction_timestamp(), updated_at = transaction_timestamp()
                    WHERE instance_id = %s AND owner_id = %s AND epoch = %s
                    """,
                    (token.instance_id, token.owner_id, token.epoch),
                )

    def append(self, command: Command, token: WriterToken) -> AppendResult:
        if not isinstance(command, Command):
            raise ContractViolation("command must be Command")
        if not isinstance(token, WriterToken):
            raise ContractViolation("token must be WriterToken")
        self._authority.require(command)
        with self._connect() as connection:
            with connection.transaction(), connection.cursor() as cursor:
                last_global_seq, last_event_hash = self._lock_and_validate_lease(cursor, token)
                existing = self._find_idempotency(cursor, token.instance_id, command)
                if existing is not None:
                    stored_digest, global_seq, stored_event_hash = existing
                    if stored_digest != command.digest:
                        raise IdempotencyConflict(
                            f"{token.instance_id}/{command.contract}/{command.idempotency_key}"
                        )
                    event = self._load_event(cursor, token.instance_id, global_seq)
                    if event.command_digest != stored_digest or event.event_hash != stored_event_hash:
                        raise StoredEventCorrupt("idempotency record differs from referenced event")
                    return AppendResult(AppendStatus.RETURN_ORIGINAL_APPEND_RESULT, event)

                global_seq = last_global_seq + 1
                stream_seq = self._next_stream_seq(cursor, token.instance_id, command.stream_id)
                cursor.execute("SELECT date_trunc('second', transaction_timestamp())")
                recorded_at = cursor.fetchone()[0].astimezone(timezone.utc).replace(microsecond=0)
                event_id = "event:" + uuid.uuid4().hex
                prev_global_hash = last_event_hash or "GENESIS"
                envelope, payload_bytes, envelope_bytes = build_event_envelope(
                    command,
                    event_id=event_id,
                    global_seq=global_seq,
                    stream_seq=stream_seq,
                    recorded_at=recorded_at,
                    prev_global_hash=prev_global_hash,
                )
                cursor.execute(
                    """
                    INSERT INTO native_kernel.events(
                        instance_id, global_seq, event_id, command_id, command_contract,
                        idempotency_key, command_digest, stream_id, stream_seq,
                        actor_ref, authority_ref, recorded_at, event_type, schema_version,
                        payload, payload_canonical, prev_global_hash, payload_hash,
                        event_hash, envelope_canonical, writer_epoch
                    ) VALUES (
                        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                        %s::jsonb,%s,%s,%s,%s,%s,%s
                    )
                    """,
                    (
                        token.instance_id,
                        global_seq,
                        event_id,
                        command.command_id,
                        command.contract,
                        command.idempotency_key,
                        command.digest,
                        command.stream_id,
                        stream_seq,
                        command.actor_ref,
                        command.authority_ref,
                        recorded_at,
                        command.event_type.value,
                        command.schema_version,
                        payload_bytes.decode("utf-8"),
                        payload_bytes,
                        prev_global_hash,
                        envelope["payload_hash"],
                        envelope["event_hash"],
                        envelope_bytes,
                        token.epoch,
                    ),
                )
                cursor.execute(
                    """
                    UPDATE native_kernel.stream_counters
                    SET last_stream_seq = %s
                    WHERE instance_id = %s AND stream_id = %s
                    """,
                    (stream_seq, token.instance_id, command.stream_id),
                )
                cursor.execute(
                    """
                    UPDATE native_kernel.kernel_instances
                    SET last_global_seq = %s,
                        last_event_hash = %s,
                        updated_at = transaction_timestamp()
                    WHERE instance_id = %s
                    """,
                    (global_seq, envelope["event_hash"], token.instance_id),
                )
                cursor.execute(
                    """
                    INSERT INTO native_kernel.idempotency_records(
                        instance_id, command_contract, idempotency_key,
                        command_digest, global_seq, event_hash
                    ) VALUES (%s,%s,%s,%s,%s,%s)
                    """,
                    (
                        token.instance_id,
                        command.contract,
                        command.idempotency_key,
                        command.digest,
                        global_seq,
                        envelope["event_hash"],
                    ),
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
                    recorded_at=recorded_at,
                    event_type=command.event_type,
                    schema_version=command.schema_version,
                    payload=command.as_contract_object()["payload"],
                    prev_global_hash=prev_global_hash,
                    payload_hash=envelope["payload_hash"],
                    event_hash=envelope["event_hash"],
                    writer_epoch=token.epoch,
                    payload_canonical=payload_bytes,
                    envelope_canonical=envelope_bytes,
                )
                if self._fault_hook is not None:
                    self._fault_hook(event)
                return AppendResult(AppendStatus.APPENDED, event)

    def count_events(self, instance_id: str) -> int:
        _require_id("instance_id", instance_id)
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(
                "SELECT count(*) FROM native_kernel.events WHERE instance_id = %s",
                (instance_id,),
            )
            return int(cursor.fetchone()[0])

    @staticmethod
    def _find_idempotency(cursor: Any, instance_id: str, command: Command) -> Any:
        cursor.execute(
            """
            SELECT command_digest, global_seq, event_hash
            FROM native_kernel.idempotency_records
            WHERE instance_id = %s AND command_contract = %s AND idempotency_key = %s
            FOR UPDATE
            """,
            (instance_id, command.contract, command.idempotency_key),
        )
        return cursor.fetchone()

    @staticmethod
    def _next_stream_seq(cursor: Any, instance_id: str, stream_id: str) -> int:
        cursor.execute(
            """
            INSERT INTO native_kernel.stream_counters(instance_id, stream_id, last_stream_seq)
            VALUES (%s, %s, 0)
            ON CONFLICT (instance_id, stream_id) DO NOTHING
            """,
            (instance_id, stream_id),
        )
        cursor.execute(
            """
            SELECT last_stream_seq
            FROM native_kernel.stream_counters
            WHERE instance_id = %s AND stream_id = %s
            FOR UPDATE
            """,
            (instance_id, stream_id),
        )
        row = cursor.fetchone()
        if row is None:
            raise StoredEventCorrupt("stream counter disappeared")
        return int(row[0]) + 1

    @staticmethod
    def _lock_instance(cursor: Any, instance_id: str) -> tuple[int, str | None, int]:
        cursor.execute(
            """
            SELECT last_global_seq, last_event_hash, writer_epoch
            FROM native_kernel.kernel_instances
            WHERE instance_id = %s
            FOR UPDATE
            """,
            (instance_id,),
        )
        row = cursor.fetchone()
        if row is None:
            raise UnknownKernelInstance(instance_id)
        return int(row[0]), row[1], int(row[2])

    @staticmethod
    def _lock_and_validate_lease(cursor: Any, token: WriterToken) -> tuple[int, str | None]:
        last_global_seq, last_event_hash, current_epoch = PostgreSQLAppendStore._lock_instance(
            cursor, token.instance_id
        )
        cursor.execute(
            """
            SELECT owner_id, epoch, expires_at, transaction_timestamp()
            FROM native_kernel.writer_leases
            WHERE instance_id = %s
            FOR UPDATE
            """,
            (token.instance_id,),
        )
        row = cursor.fetchone()
        if row is None:
            raise WriterLeaseExpired(f"no lease for {token.instance_id}")
        owner_id, epoch, expires_at, now = row
        if epoch != current_epoch:
            raise StoredEventCorrupt(
                f"writer lease epoch {epoch} differs from instance epoch {current_epoch}"
            )
        if owner_id != token.owner_id or epoch != token.epoch:
            raise StaleWriterEpoch(
                f"stored writer {owner_id}/{epoch} differs from token {token.owner_id}/{token.epoch}"
            )
        if expires_at <= now:
            raise WriterLeaseExpired(
                f"lease {token.instance_id}/{token.owner_id}/{token.epoch} expired at {expires_at.isoformat()}"
            )
        return last_global_seq, last_event_hash

    @staticmethod
    def _load_event(cursor: Any, instance_id: str, global_seq: int) -> StoredEvent:
        cursor.execute(
            """
            SELECT event_id, command_id, idempotency_key, command_contract,
                   command_digest, stream_id, stream_seq, actor_ref, authority_ref,
                   recorded_at, event_type, schema_version, payload,
                   prev_global_hash, payload_hash, event_hash, writer_epoch,
                   payload_canonical, envelope_canonical
            FROM native_kernel.events
            WHERE instance_id = %s AND global_seq = %s
            """,
            (instance_id, global_seq),
        )
        row = cursor.fetchone()
        if row is None:
            raise StoredEventCorrupt(
                f"idempotency record references missing event {instance_id}/{global_seq}"
            )
        payload = json.loads(row[12]) if isinstance(row[12], str) else row[12]
        event = StoredEvent(
            instance_id=instance_id,
            event_id=row[0],
            command_id=row[1],
            idempotency_key=row[2],
            command_contract=row[3],
            command_digest=row[4],
            stream_id=row[5],
            global_seq=global_seq,
            stream_seq=row[6],
            actor_ref=row[7],
            authority_ref=row[8],
            recorded_at=row[9],
            event_type=EventType(row[10]),
            schema_version=row[11],
            payload=payload,
            prev_global_hash=row[13],
            payload_hash=row[14],
            event_hash=row[15],
            writer_epoch=row[16],
            payload_canonical=bytes(row[17]),
            envelope_canonical=bytes(row[18]),
        )
        PostgreSQLAppendStore._verify_stored_event(event)
        return event

    @staticmethod
    def _verify_stored_event(event: StoredEvent) -> None:
        if canonical_json_bytes(event.payload) != event.payload_canonical:
            raise StoredEventCorrupt("stored payload canonical bytes mismatch")
        if payload_hash(event.payload) != event.payload_hash:
            raise StoredEventCorrupt("stored payload hash mismatch")
        try:
            envelope = json.loads(event.envelope_canonical.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise StoredEventCorrupt("stored envelope bytes are not canonical JSON") from exc
        try:
            canonical_envelope = canonical_json_bytes(envelope)
        except ContractViolation as exc:
            raise StoredEventCorrupt("stored envelope is outside the canonical JSON subset") from exc
        if canonical_envelope != event.envelope_canonical:
            raise StoredEventCorrupt("stored envelope bytes are not canonical")
        expected_fields = {
            "contract": "nk-event-envelope/1",
            "event_id": event.event_id,
            "command_id": event.command_id,
            "idempotency_key": event.idempotency_key,
            "stream_id": event.stream_id,
            "global_seq": event.global_seq,
            "stream_seq": event.stream_seq,
            "actor_ref": event.actor_ref,
            "authority_ref": event.authority_ref,
            "recorded_at": event.recorded_at.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "event_type": event.event_type.value,
            "schema_version": event.schema_version,
            "payload": json.loads(event.payload_canonical.decode("utf-8")),
            "prev_global_hash": event.prev_global_hash,
            "payload_hash": event.payload_hash,
            "event_hash": event.event_hash,
        }
        if set(envelope) != set(expected_fields):
            missing = sorted(set(expected_fields) - set(envelope))
            unexpected = sorted(set(envelope) - set(expected_fields))
            raise StoredEventCorrupt(
                f"stored envelope field set mismatch; missing={missing}; unexpected={unexpected}"
            )
        for key, expected in expected_fields.items():
            try:
                exact_value_match = canonical_json_bytes(envelope[key]) == canonical_json_bytes(expected)
            except ContractViolation as exc:
                raise StoredEventCorrupt(f"stored envelope field is not canonical: {key}") from exc
            if not exact_value_match:
                raise StoredEventCorrupt(f"stored envelope field mismatch: {key}")
        committed = dict(envelope)
        declared = committed.pop("event_hash")
        if declared != event.event_hash or event_hash(committed) != event.event_hash:
            raise StoredEventCorrupt("stored event hash mismatch")
