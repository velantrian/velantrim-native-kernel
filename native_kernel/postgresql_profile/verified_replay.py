from __future__ import annotations

from .errors import ProjectionCorrupt
from .replay import PostgreSQLReplayProjector as _BaseReplayProjector
from .replay_models import OperationType, StoredProjection


class PostgreSQLReplayProjector(_BaseReplayProjector):
    """P3 projector with projection-to-Receipt consistency verification.

    A projection row is disposable, but its declared rebuild evidence must still
    point to a valid bounded PROJECTION_REBUILD Receipt whose snapshot and
    version fields exactly match the stored projection.
    """

    def load_projection(
        self,
        instance_id: str,
        projection_name: str = "semantic-state",
    ) -> StoredProjection:
        projection = super().load_projection(instance_id, projection_name)
        receipt = self.load_receipt(projection.receipt_id)

        expected = {
            "operation_type": OperationType.PROJECTION_REBUILD,
            "instance_id": projection.instance_id,
            "projection_name": projection.projection_name,
            "projection_generation": projection.generation,
            "state_digest": projection.state_digest,
            "last_global_seq": projection.last_global_seq,
            "last_event_hash": projection.last_event_hash,
            "reducer_version": projection.reducer_version,
            "target_schema_version": projection.target_schema_version,
            "created_at": projection.rebuilt_at,
        }
        actual = {
            "operation_type": receipt.operation_type,
            "instance_id": receipt.instance_id,
            "projection_name": receipt.projection_name,
            "projection_generation": receipt.projection_generation,
            "state_digest": receipt.state_digest,
            "last_global_seq": receipt.last_global_seq,
            "last_event_hash": receipt.last_event_hash,
            "reducer_version": receipt.reducer_version,
            "target_schema_version": receipt.target_schema_version,
            "created_at": receipt.created_at,
        }
        for field, expected_value in expected.items():
            if actual[field] != expected_value:
                raise ProjectionCorrupt(
                    f"stored projection differs from linked rebuild Receipt: {field}"
                )
        return projection
