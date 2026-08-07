from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from typing import Any

from .errors import ReceiptCorrupt
from .replay_models import OperationType, OperationalReceipt, ReplaySnapshot

DEFAULT_LIMITS = (
    "verifies only the selected PostgreSQL instance snapshot and declared checks",
    "does not establish truth of recorded Claims",
    "does not establish external authenticity or signatures",
    "does not prove absence of privileged rewrites before the verified snapshot",
    "does not prove physical deletion of primary bytes backups exports logs or keys",
    "does not establish complete Event Integrity C1 C2 C3 or production readiness",
)


def make_receipt(
    operation_type: OperationType,
    snapshot: ReplaySnapshot,
    *,
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
        reducer_version=snapshot.reducer_version,
        target_schema_version=snapshot.target_schema_version,
        state_digest=snapshot.state.digest,
        projection_name=projection_name,
        projection_generation=projection_generation,
        known_limits=DEFAULT_LIMITS,
        created_at=datetime.now(timezone.utc).replace(microsecond=0),
    )


def insert_receipt(cursor: Any, receipt: OperationalReceipt) -> None:
    cursor.execute(
        """
        INSERT INTO native_kernel.operation_receipts(
            receipt_id, operation_type, instance_id, projection_name,
            projection_generation, event_count, first_global_seq,
            last_global_seq, last_event_hash, reducer_version,
            target_schema_version, state_digest, known_limits,
            created_at, claims_truth_established,
            claims_external_authenticity, claims_complete_integrity,
            claims_complete_erasure, receipt_hash, receipt_canonical
        ) VALUES (
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s::jsonb,%s,
            %s,%s,%s,%s,%s,%s
        )
        """,
        (
            receipt.receipt_id,
            receipt.operation_type.value,
            receipt.instance_id,
            receipt.projection_name,
            receipt.projection_generation,
            receipt.event_count,
            receipt.first_global_seq,
            receipt.last_global_seq,
            receipt.last_event_hash,
            receipt.reducer_version,
            receipt.target_schema_version,
            receipt.state_digest,
            json.dumps(list(receipt.known_limits), ensure_ascii=False, separators=(",", ":")),
            receipt.created_at,
            False,
            False,
            False,
            False,
            receipt.receipt_hash,
            receipt.canonical_bytes,
        ),
    )


def load_receipt(connection_factory: Any, receipt_id: str) -> OperationalReceipt:
    with connection_factory() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT operation_type, instance_id, projection_name,
                   projection_generation, event_count, first_global_seq,
                   last_global_seq, last_event_hash, reducer_version,
                   target_schema_version, state_digest, known_limits,
                   created_at, claims_truth_established,
                   claims_external_authenticity, claims_complete_integrity,
                   claims_complete_erasure, receipt_hash, receipt_canonical
            FROM native_kernel.operation_receipts
            WHERE receipt_id = %s
            """,
            (receipt_id,),
        )
        row = cursor.fetchone()
    if row is None:
        raise ReceiptCorrupt(f"missing Receipt {receipt_id}")
    limits = json.loads(row[11]) if isinstance(row[11], str) else row[11]
    receipt = OperationalReceipt(
        receipt_id=receipt_id,
        operation_type=OperationType(row[0]),
        instance_id=row[1],
        projection_name=row[2],
        projection_generation=row[3],
        event_count=int(row[4]),
        first_global_seq=int(row[5]),
        last_global_seq=int(row[6]),
        last_event_hash=row[7],
        reducer_version=row[8],
        target_schema_version=row[9],
        state_digest=row[10],
        known_limits=tuple(limits),
        created_at=row[12],
        claims_truth_established=row[13],
        claims_external_authenticity=row[14],
        claims_complete_integrity=row[15],
        claims_complete_erasure=row[16],
    )
    if receipt.receipt_hash != row[17] or receipt.canonical_bytes != bytes(row[18]):
        raise ReceiptCorrupt("stored Receipt commitments mismatch")
    return receipt
