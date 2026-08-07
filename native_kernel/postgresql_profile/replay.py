from __future__ import annotations

import json
import re
from collections.abc import Callable
from typing import Any

from native_kernel.semantic_core.canonical import canonical_json_bytes
from native_kernel.semantic_core.errors import ContractViolation
from native_kernel.semantic_core.reducer import REDUCER_VERSION
from native_kernel.semantic_core.state_codec import semantic_state_from_contract_object
from native_kernel.semantic_core.upcasting import UpcasterRegistry, identity_upcaster_registry

from .adapter import connection_factory_from_dsn
from .errors import ProjectionCorrupt, ProjectionNotFound
from .history import read_snapshot, require_current_head
from .migrations import apply_migrations
from .receipt_store import insert_receipt, load_receipt, make_receipt
from .replay_models import (
    OperationType,
    OperationalReceipt,
    ProjectionRebuildResult,
    ReplayResult,
    ReplaySnapshot,
    StoredProjection,
)

_ID_RE = re.compile(r"^[a-z0-9][a-z0-9._:/-]{0,127}$")
DEFAULT_PROJECTION = "semantic-state"
ConnectionFactory = Callable[[], Any]
SnapshotHook = Callable[[ReplaySnapshot], None]
ReceiptFaultHook = Callable[[OperationalReceipt], None]


def _require_id(name: str, value: object) -> str:
    if not isinstance(value, str) or not _ID_RE.fullmatch(value):
        raise ContractViolation(f"{name} must match {_ID_RE.pattern}")
    return value


class PostgreSQLReplayProjector:
    """Bounded P3 replay, disposable projection and Receipt profile."""

    def __init__(
        self,
        connection_factory: ConnectionFactory,
        *,
        upcasters: UpcasterRegistry | None = None,
        snapshot_hook: SnapshotHook | None = None,
        receipt_fault_hook: ReceiptFaultHook | None = None,
    ) -> None:
        if not callable(connection_factory):
            raise ContractViolation("connection_factory must be callable")
        if upcasters is not None and not isinstance(upcasters, UpcasterRegistry):
            raise ContractViolation("upcasters must be UpcasterRegistry")
        if snapshot_hook is not None and not callable(snapshot_hook):
            raise ContractViolation("snapshot_hook must be callable")
        if receipt_fault_hook is not None and not callable(receipt_fault_hook):
            raise ContractViolation("receipt_fault_hook must be callable")
        self._connect = connection_factory
        self._upcasters = upcasters or identity_upcaster_registry("1")
        self._snapshot_hook = snapshot_hook
        self._receipt_fault_hook = receipt_fault_hook

    @classmethod
    def from_dsn(
        cls,
        dsn: str,
        *,
        upcasters: UpcasterRegistry | None = None,
        snapshot_hook: SnapshotHook | None = None,
        receipt_fault_hook: ReceiptFaultHook | None = None,
    ) -> "PostgreSQLReplayProjector":
        return cls(
            connection_factory_from_dsn(dsn),
            upcasters=upcasters,
            snapshot_hook=snapshot_hook,
            receipt_fault_hook=receipt_fault_hook,
        )

    def migrate(self) -> tuple[str, ...]:
        with self._connect() as connection:
            return apply_migrations(connection)

    def replay(self, instance_id: str, *, persist_receipt: bool = True) -> ReplayResult:
        instance = _require_id("instance_id", instance_id)
        snapshot = read_snapshot(self._connect, instance, self._upcasters)
        receipt = make_receipt(OperationType.REPLAY, snapshot)
        if persist_receipt:
            with self._connect() as connection:
                with connection.transaction(), connection.cursor() as cursor:
                    require_current_head(cursor, snapshot)
                    insert_receipt(cursor, receipt)
        return ReplayResult(snapshot=snapshot, receipt=receipt)

    def rebuild_projection(
        self,
        instance_id: str,
        projection_name: str = DEFAULT_PROJECTION,
    ) -> ProjectionRebuildResult:
        instance = _require_id("instance_id", instance_id)
        projection_key = _require_id("projection_name", projection_name)
        snapshot = read_snapshot(self._connect, instance, self._upcasters)
        if self._snapshot_hook is not None:
            self._snapshot_hook(snapshot)
        state_canonical = canonical_json_bytes(snapshot.state.as_contract_object())

        with self._connect() as connection:
            with connection.transaction(), connection.cursor() as cursor:
                require_current_head(cursor, snapshot)
                cursor.execute(
                    """
                    SELECT COALESCE(max(projection_generation), 0)
                    FROM native_kernel.operation_receipts
                    WHERE instance_id = %s
                      AND operation_type = 'PROJECTION_REBUILD'
                      AND projection_name = %s
                    """,
                    (instance, projection_key),
                )
                generation = int(cursor.fetchone()[0]) + 1
                receipt = make_receipt(
                    OperationType.PROJECTION_REBUILD,
                    snapshot,
                    projection_name=projection_key,
                    projection_generation=generation,
                )
                insert_receipt(cursor, receipt)
                if self._receipt_fault_hook is not None:
                    self._receipt_fault_hook(receipt)
                cursor.execute(
                    """
                    INSERT INTO native_kernel.projections(
                        instance_id, projection_name, reducer_version,
                        target_schema_version, generation, last_global_seq,
                        last_event_hash, state, state_canonical, state_digest,
                        receipt_id, rebuilt_at
                    ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s::jsonb,%s,%s,%s,%s)
                    ON CONFLICT (instance_id, projection_name) DO UPDATE SET
                        reducer_version = EXCLUDED.reducer_version,
                        target_schema_version = EXCLUDED.target_schema_version,
                        generation = EXCLUDED.generation,
                        last_global_seq = EXCLUDED.last_global_seq,
                        last_event_hash = EXCLUDED.last_event_hash,
                        state = EXCLUDED.state,
                        state_canonical = EXCLUDED.state_canonical,
                        state_digest = EXCLUDED.state_digest,
                        receipt_id = EXCLUDED.receipt_id,
                        rebuilt_at = EXCLUDED.rebuilt_at
                    RETURNING rebuilt_at
                    """,
                    (
                        instance,
                        projection_key,
                        snapshot.reducer_version,
                        snapshot.target_schema_version,
                        generation,
                        snapshot.last_global_seq,
                        snapshot.last_event_hash,
                        state_canonical.decode("utf-8"),
                        state_canonical,
                        snapshot.state.digest,
                        receipt.receipt_id,
                        receipt.created_at,
                    ),
                )
                rebuilt_at = cursor.fetchone()[0]

        projection = StoredProjection(
            instance_id=instance,
            projection_name=projection_key,
            generation=generation,
            state=snapshot.state,
            state_digest=snapshot.state.digest,
            last_global_seq=snapshot.last_global_seq,
            last_event_hash=snapshot.last_event_hash,
            receipt_id=receipt.receipt_id,
            rebuilt_at=rebuilt_at,
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
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT reducer_version, target_schema_version, generation,
                       last_global_seq, last_event_hash, state, state_canonical,
                       state_digest, receipt_id, rebuilt_at
                FROM native_kernel.projections
                WHERE instance_id = %s AND projection_name = %s
                """,
                (instance, projection_key),
            )
            row = cursor.fetchone()
        if row is None:
            raise ProjectionNotFound(f"{instance}/{projection_key}")
        state_object = json.loads(row[5]) if isinstance(row[5], str) else row[5]
        state_canonical = bytes(row[6])
        if canonical_json_bytes(state_object) != state_canonical:
            raise ProjectionCorrupt("stored projection canonical bytes mismatch")
        state = semantic_state_from_contract_object(state_object)
        if state.digest != row[7]:
            raise ProjectionCorrupt("stored projection state digest mismatch")
        projection = StoredProjection(
            instance_id=instance,
            projection_name=projection_key,
            generation=int(row[2]),
            state=state,
            state_digest=row[7],
            last_global_seq=int(row[3]),
            last_event_hash=row[4],
            receipt_id=row[8],
            rebuilt_at=row[9],
            state_canonical=state_canonical,
            reducer_version=row[0],
            target_schema_version=row[1],
        )
        if projection.reducer_version != REDUCER_VERSION:
            raise ProjectionCorrupt("stored projection reducer version is unsupported")
        if projection.target_schema_version != self._upcasters.target_version:
            raise ProjectionCorrupt("stored projection target schema version differs from registry")

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
            raise ProjectionCorrupt(
                "linked Receipt does not describe the stored projection rebuild"
            )
        return projection

    def destroy_projection(
        self,
        instance_id: str,
        projection_name: str = DEFAULT_PROJECTION,
    ) -> bool:
        instance = _require_id("instance_id", instance_id)
        projection_key = _require_id("projection_name", projection_name)
        with self._connect() as connection:
            with connection.transaction(), connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM native_kernel.projections "
                    "WHERE instance_id = %s AND projection_name = %s",
                    (instance, projection_key),
                )
                return cursor.rowcount == 1

    def load_receipt(self, receipt_id: str) -> OperationalReceipt:
        return load_receipt(self._connect, _require_id("receipt_id", receipt_id))

    def count_receipts(self, instance_id: str) -> int:
        instance = _require_id("instance_id", instance_id)
        with self._connect() as connection, connection.cursor() as cursor:
            cursor.execute(
                "SELECT count(*) FROM native_kernel.operation_receipts WHERE instance_id = %s",
                (instance,),
            )
            return int(cursor.fetchone()[0])
