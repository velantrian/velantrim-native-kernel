from __future__ import annotations

import json
import re
import sqlite3
import uuid
from collections.abc import Callable
from datetime import datetime, timezone
from typing import Any

from native_kernel.semantic_core.canonical import canonical_json_bytes
from native_kernel.semantic_core.errors import ContractViolation
from native_kernel.semantic_core.models import SemanticEvent
from native_kernel.semantic_core.reducer import REDUCER_VERSION, SemanticState, reduce_event
from native_kernel.semantic_core.state_codec import semantic_state_from_contract_object
from native_kernel.semantic_core.upcasting import UpcasterRegistry, identity_upcaster_registry

from .adapter import SQLiteAppendStore, _format_time, _parse_time, _require_id, _utc_second
from .errors import (
    HistoryAdvanced,
    ProjectionCorrupt,
    ProjectionNotFound,
    ReceiptCorrupt,
    ReplayIntegrityError,
    UnknownKernelInstance,
)
from .replay_models import (
    OperationType,
    OperationalReceipt,
    ProjectionRebuildResult,
    ReplayResult,
    ReplaySnapshot,
    StoredProjection,
)

DEFAULT_PROJECTION = "semantic-state"
SnapshotHook = Callable[[ReplaySnapshot], None]
ReceiptFaultHook = Callable[[OperationalReceipt], None]
Clock = Callable[[], datetime]


def _default_clock() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def _known_limits(operation_type: OperationType) -> tuple[str, ...]:
    base = (
        "Receipt proves only the named bounded operation on one SQLite file and exact history head.",
        "Receipt does not establish truth or external authenticity.",
        "Receipt does not establish complete integrity under every threat model.",
        "Receipt does not establish physical or cryptographic deletion.",
    )
    if operation_type is OperationType.PROJECTION_REBUILD:
        return base + ("Projection is disposable and not authoritative history.",)
    return base


def _make_receipt(
    operation_type: OperationType,
    snapshot: ReplaySnapshot,
    *,
    created_at: datetime,
    projection_name: str | None = None,
    projection_generation: int | None = None,
) -> OperationalReceipt:
    return OperationalReceipt(
        receipt_id="receipt:" + uuid.uuid4().hex,
        operation_type=operation_type,
        instance_id=snapshot.instance_id,
        event_count=snapshot.event_count,
        first_global_seq=snapshot.first_global_seq,
        last_global_seq=snapshot.last_global_seq,
        last_event_hash=snapshot.last_event_hash,
        state_digest=snapshot.state.digest,
        known_limits=_known_limits(operation_type),
        created_at=_utc_second(created_at),
        projection_name=projection_name,
        projection_generation=projection_generation,
        reducer_version=snapshot.reducer_version,
        target_schema_version=snapshot.target_schema_version,
    )


class SQLiteReplayProjector:
    """Independent SQLite replay, disposable projection and Receipt profile."""

    def __init__(
        self,
        database_path: str,
        *,
        upcasters: UpcasterRegistry | None = None,
        snapshot_hook: SnapshotHook | None = None,
        receipt_fault_hook: ReceiptFaultHook | None = None,
        clock: Clock | None = None,
    ) -> None:
        if not isinstance(database_path, str) or not database_path:
            raise ContractViolation("database_path must be non-empty")
        if upcasters is not None and not isinstance(upcasters, UpcasterRegistry):
            raise ContractViolation("upcasters must be UpcasterRegistry")
        if snapshot_hook is not None and not callable(snapshot_hook):
            raise ContractViolation("snapshot_hook must be callable")
        if receipt_fault_hook is not None and not callable(receipt_fault_hook):
            raise ContractViolation("receipt_fault_hook must be callable")
        if clock is not None and not callable(clock):
            raise ContractViolation("clock must be callable")
        self.database_path = database_path
        self._upcasters = upcasters or identity_upcaster_registry("1")
        self._snapshot_hook = snapshot_hook
        self._receipt_fault_hook = receipt_fault_hook
        self._clock = clock or _default_clock

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.database_path, isolation_level=None, timeout=5)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("PRAGMA busy_timeout = 5000")
        return connection

    def replay(self, instance_id: str, *, persist_receipt: bool = True) -> ReplayResult:
        snapshot = self._read_snapshot(_require_id("instance_id", instance_id))
        receipt = _make_receipt(OperationType.REPLAY, snapshot, created_at=self._clock())
        if persist_receipt:
            connection = self._connect()
            try:
                connection.execute("BEGIN IMMEDIATE")
                self._require_current_head(connection, snapshot)
                self._insert_receipt(connection, receipt)
                connection.commit()
            except Exception:
                connection.rollback()
                raise
            finally:
                connection.close()
        return ReplayResult(snapshot=snapshot, receipt=receipt)

    def rebuild_projection(
        self,
        instance_id: str,
        projection_name: str = DEFAULT_PROJECTION,
    ) -> ProjectionRebuildResult:
        instance = _require_id("instance_id", instance_id)
        projection_key = _require_id("projection_name", projection_name)
        snapshot = self._read_snapshot(instance)
        if self._snapshot_hook is not None:
            self._snapshot_hook(snapshot)
        state_canonical = canonical_json_bytes(snapshot.state.as_contract_object())
        connection = self._connect()
        try:
            connection.execute("BEGIN IMMEDIATE")
            self._require_current_head(connection, snapshot)
            row = connection.execute(
                "SELECT COALESCE(max(projection_generation),0) AS n FROM operation_receipts "
                "WHERE instance_id=? AND operation_type='PROJECTION_REBUILD' AND projection_name=?",
                (instance, projection_key),
            ).fetchone()
            generation = int(row["n"]) + 1
            receipt = _make_receipt(
                OperationType.PROJECTION_REBUILD,
                snapshot,
                created_at=self._clock(),
                projection_name=projection_key,
                projection_generation=generation,
            )
            self._insert_receipt(connection, receipt)
            if self._receipt_fault_hook is not None:
                self._receipt_fault_hook(receipt)
            connection.execute(
                "INSERT INTO projections(instance_id,projection_name,reducer_version,"
                "target_schema_version,generation,last_global_seq,last_event_hash,state_text,"
                "state_canonical,state_digest,receipt_id,rebuilt_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?) "
                "ON CONFLICT(instance_id,projection_name) DO UPDATE SET "
                "reducer_version=excluded.reducer_version,target_schema_version=excluded.target_schema_version,"
                "generation=excluded.generation,last_global_seq=excluded.last_global_seq,"
                "last_event_hash=excluded.last_event_hash,state_text=excluded.state_text,"
                "state_canonical=excluded.state_canonical,state_digest=excluded.state_digest,"
                "receipt_id=excluded.receipt_id,rebuilt_at=excluded.rebuilt_at",
                (
                    instance, projection_key, snapshot.reducer_version,
                    snapshot.target_schema_version, generation, snapshot.last_global_seq,
                    snapshot.last_event_hash, state_canonical.decode("utf-8"), state_canonical,
                    snapshot.state.digest, receipt.receipt_id, _format_time(receipt.created_at),
                ),
            )
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()
        projection = StoredProjection(
            instance_id=instance,
            projection_name=projection_key,
            generation=generation,
            state=snapshot.state,
            state_digest=snapshot.state.digest,
            last_global_seq=snapshot.last_global_seq,
            last_event_hash=snapshot.last_event_hash,
            receipt_id=receipt.receipt_id,
            rebuilt_at=receipt.created_at,
            state_canonical=state_canonical,
            reducer_version=snapshot.reducer_version,
            target_schema_version=snapshot.target_schema_version,
        )
        return ProjectionRebuildResult(snapshot=snapshot, projection=projection, receipt=receipt)

    def load_projection(
        self,
        instance_id: str,
        projection_name: str = DEFAULT_PROJECTION,
    ) -> StoredProjection:
        instance = _require_id("instance_id", instance_id)
        projection_key = _require_id("projection_name", projection_name)
        with self._connect() as connection:
            row = connection.execute(
                "SELECT * FROM projections WHERE instance_id=? AND projection_name=?",
                (instance, projection_key),
            ).fetchone()
        if row is None:
            raise ProjectionNotFound(f"{instance}/{projection_key}")
        state_object = json.loads(row["state_text"])
        state_canonical = bytes(row["state_canonical"])
        if canonical_json_bytes(state_object) != state_canonical:
            raise ProjectionCorrupt("stored projection canonical bytes mismatch")
        state = semantic_state_from_contract_object(state_object)
        if state.digest != row["state_digest"]:
            raise ProjectionCorrupt("stored projection state digest mismatch")
        projection = StoredProjection(
            instance_id=instance,
            projection_name=projection_key,
            generation=int(row["generation"]),
            state=state,
            state_digest=row["state_digest"],
            last_global_seq=int(row["last_global_seq"]),
            last_event_hash=row["last_event_hash"],
            receipt_id=row["receipt_id"],
            rebuilt_at=_parse_time(row["rebuilt_at"]),
            state_canonical=state_canonical,
            reducer_version=row["reducer_version"],
            target_schema_version=row["target_schema_version"],
        )
        if projection.reducer_version != REDUCER_VERSION:
            raise ProjectionCorrupt("stored projection reducer version is unsupported")
        if projection.target_schema_version != self._upcasters.target_version:
            raise ProjectionCorrupt("stored projection target version differs from registry")
        receipt = self.load_receipt(projection.receipt_id)
        expected = (
            receipt.operation_type is OperationType.PROJECTION_REBUILD
            and receipt.instance_id == projection.instance_id
            and receipt.projection_name == projection.projection_name
            and receipt.projection_generation == projection.generation
            and receipt.last_global_seq == projection.last_global_seq
            and receipt.last_event_hash == projection.last_event_hash
            and receipt.reducer_version == projection.reducer_version
            and receipt.target_schema_version == projection.target_schema_version
            and receipt.state_digest == projection.state_digest
        )
        if not expected:
            raise ProjectionCorrupt("linked Receipt does not describe projection")
        return projection

    def destroy_projection(
        self,
        instance_id: str,
        projection_name: str = DEFAULT_PROJECTION,
    ) -> bool:
        connection = self._connect()
        try:
            connection.execute("BEGIN IMMEDIATE")
            cursor = connection.execute(
                "DELETE FROM projections WHERE instance_id=? AND projection_name=?",
                (_require_id("instance_id", instance_id), _require_id("projection_name", projection_name)),
            )
            connection.commit()
            return cursor.rowcount == 1
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def load_receipt(self, receipt_id: str) -> OperationalReceipt:
        key = _require_id("receipt_id", receipt_id)
        with self._connect() as connection:
            row = connection.execute(
                "SELECT * FROM operation_receipts WHERE receipt_id=?", (key,)
            ).fetchone()
        if row is None:
            raise ReceiptCorrupt(f"missing Receipt {key}")
        limits = tuple(json.loads(row["known_limits_text"]))
        receipt = OperationalReceipt(
            receipt_id=row["receipt_id"],
            operation_type=OperationType(row["operation_type"]),
            instance_id=row["instance_id"],
            event_count=int(row["event_count"]),
            first_global_seq=int(row["first_global_seq"]),
            last_global_seq=int(row["last_global_seq"]),
            last_event_hash=row["last_event_hash"],
            state_digest=row["state_digest"],
            known_limits=limits,
            created_at=_parse_time(row["created_at"]),
            projection_name=row["projection_name"],
            projection_generation=(
                int(row["projection_generation"])
                if row["projection_generation"] is not None else None
            ),
            reducer_version=row["reducer_version"],
            target_schema_version=row["target_schema_version"],
        )
        if receipt.canonical_bytes != bytes(row["canonical_bytes"]):
            raise ReceiptCorrupt("Receipt canonical bytes mismatch")
        if receipt.receipt_hash != row["receipt_hash"]:
            raise ReceiptCorrupt("Receipt hash mismatch")
        return receipt

    def count_receipts(self, instance_id: str) -> int:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT count(*) AS n FROM operation_receipts WHERE instance_id=?",
                (_require_id("instance_id", instance_id),),
            ).fetchone()
            return int(row["n"])

    def corrupt_projection_state_for_test(self, instance_id: str, value: bytes) -> None:
        connection = self._connect()
        try:
            connection.execute("BEGIN IMMEDIATE")
            connection.execute(
                "UPDATE projections SET state_canonical=? WHERE instance_id=?",
                (value, _require_id("instance_id", instance_id)),
            )
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def _read_snapshot(self, instance_id: str) -> ReplaySnapshot:
        connection = self._connect()
        try:
            connection.execute("BEGIN")
            head = connection.execute(
                "SELECT last_global_seq,last_event_hash FROM kernel_instances WHERE instance_id=?",
                (instance_id,),
            ).fetchone()
            if head is None:
                raise UnknownKernelInstance(instance_id)
            last_global_seq = int(head["last_global_seq"])
            last_event_hash = head["last_event_hash"]
            count_row = connection.execute(
                "SELECT count(*) AS n, COALESCE(max(global_seq),0) AS maximum "
                "FROM events WHERE instance_id=?",
                (instance_id,),
            ).fetchone()
            if int(count_row["n"]) != last_global_seq or int(count_row["maximum"]) != last_global_seq:
                raise ReplayIntegrityError("history head differs from Event count/max")
            state = SemanticState()
            previous_hash = "GENESIS"
            for sequence in range(1, last_global_seq + 1):
                event = SQLiteAppendStore._load_event(connection, instance_id, sequence)
                if event.prev_global_hash != previous_hash:
                    raise ReplayIntegrityError(f"hash chain mismatch at sequence {sequence}")
                upcasted = self._upcasters.upcast(event.schema_version, event.payload)
                state = reduce_event(
                    state,
                    SemanticEvent(
                        global_seq=event.global_seq,
                        stream_id=event.stream_id,
                        stream_seq=event.stream_seq,
                        event_type=event.event_type,
                        schema_version=upcasted.target_version,
                        payload=upcasted.payload,
                    ),
                )
                previous_hash = event.event_hash
            if last_global_seq == 0:
                if last_event_hash is not None:
                    raise ReplayIntegrityError("empty history must not declare head hash")
                snapshot_hash = None
            else:
                if last_event_hash != previous_hash:
                    raise ReplayIntegrityError("instance head differs from replayed chain")
                snapshot_hash = previous_hash
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()
        return ReplaySnapshot(
            instance_id=instance_id,
            state=state,
            event_count=last_global_seq,
            first_global_seq=1 if last_global_seq else 0,
            last_global_seq=last_global_seq,
            last_event_hash=snapshot_hash,
            reducer_version=REDUCER_VERSION,
            target_schema_version=self._upcasters.target_version,
        )

    @staticmethod
    def _require_current_head(connection: sqlite3.Connection, snapshot: ReplaySnapshot) -> None:
        row = connection.execute(
            "SELECT last_global_seq,last_event_hash FROM kernel_instances WHERE instance_id=?",
            (snapshot.instance_id,),
        ).fetchone()
        if row is None:
            raise UnknownKernelInstance(snapshot.instance_id)
        if int(row["last_global_seq"]) != snapshot.last_global_seq or row["last_event_hash"] != snapshot.last_event_hash:
            raise HistoryAdvanced(
                f"history advanced after replay for {snapshot.instance_id}"
            )

    @staticmethod
    def _insert_receipt(connection: sqlite3.Connection, receipt: OperationalReceipt) -> None:
        connection.execute(
            "INSERT INTO operation_receipts(receipt_id,operation_type,instance_id,event_count,"
            "first_global_seq,last_global_seq,last_event_hash,state_digest,known_limits_text,"
            "projection_name,projection_generation,reducer_version,target_schema_version,"
            "created_at,canonical_bytes,receipt_hash) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                receipt.receipt_id, receipt.operation_type.value, receipt.instance_id,
                receipt.event_count, receipt.first_global_seq, receipt.last_global_seq,
                receipt.last_event_hash, receipt.state_digest,
                json.dumps(list(receipt.known_limits), ensure_ascii=False, separators=(",", ":")),
                receipt.projection_name, receipt.projection_generation,
                receipt.reducer_version, receipt.target_schema_version,
                _format_time(receipt.created_at), receipt.canonical_bytes, receipt.receipt_hash,
            ),
        )
