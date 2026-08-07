from __future__ import annotations

from typing import Any

from native_kernel.semantic_core.models import SemanticEvent
from native_kernel.semantic_core.reducer import REDUCER_VERSION, SemanticState, reduce_event
from native_kernel.semantic_core.upcasting import UpcasterRegistry

from .adapter import PostgreSQLAppendStore
from .errors import HistoryAdvanced, ReplayIntegrityError, UnknownKernelInstance
from .replay_models import ReplaySnapshot


def read_snapshot(connection_factory: Any, instance_id: str, upcasters: UpcasterRegistry) -> ReplaySnapshot:
    with connection_factory() as connection:
        with connection.transaction(), connection.cursor() as cursor:
            cursor.execute("SET TRANSACTION ISOLATION LEVEL REPEATABLE READ, READ ONLY")
            cursor.execute(
                """
                SELECT last_global_seq, last_event_hash
                FROM native_kernel.kernel_instances
                WHERE instance_id = %s
                """,
                (instance_id,),
            )
            head = cursor.fetchone()
            if head is None:
                raise UnknownKernelInstance(instance_id)
            last_global_seq = int(head[0])
            last_event_hash = head[1]
            cursor.execute(
                """
                SELECT count(*), COALESCE(max(global_seq), 0)
                FROM native_kernel.events
                WHERE instance_id = %s
                """,
                (instance_id,),
            )
            count, maximum = cursor.fetchone()
            if int(count) != last_global_seq or int(maximum) != last_global_seq:
                raise ReplayIntegrityError(
                    "instance history head differs from stored Event count/max sequence"
                )

            state = SemanticState()
            previous_hash = "GENESIS"
            for sequence in range(1, last_global_seq + 1):
                event = PostgreSQLAppendStore._load_event(cursor, instance_id, sequence)
                if event.prev_global_hash != previous_hash:
                    raise ReplayIntegrityError(
                        f"global hash chain mismatch at sequence {sequence}"
                    )
                upcasted = upcasters.upcast(event.schema_version, event.payload)
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
                    raise ReplayIntegrityError("empty history must not declare a head hash")
                snapshot_hash = None
            else:
                if last_event_hash != previous_hash:
                    raise ReplayIntegrityError(
                        "instance head hash differs from replayed Event chain"
                    )
                snapshot_hash = previous_hash

    return ReplaySnapshot(
        instance_id=instance_id,
        state=state,
        event_count=last_global_seq,
        first_global_seq=1 if last_global_seq else 0,
        last_global_seq=last_global_seq,
        last_event_hash=snapshot_hash,
        reducer_version=REDUCER_VERSION,
        target_schema_version=upcasters.target_version,
    )


def require_current_head(cursor: Any, snapshot: ReplaySnapshot) -> None:
    cursor.execute(
        """
        SELECT last_global_seq, last_event_hash
        FROM native_kernel.kernel_instances
        WHERE instance_id = %s
        FOR UPDATE
        """,
        (snapshot.instance_id,),
    )
    row = cursor.fetchone()
    if row is None:
        raise UnknownKernelInstance(snapshot.instance_id)
    if int(row[0]) != snapshot.last_global_seq or row[1] != snapshot.last_event_hash:
        raise HistoryAdvanced(
            f"history advanced after replay for {snapshot.instance_id}: "
            f"expected {snapshot.last_global_seq}/{snapshot.last_event_hash}, "
            f"got {row[0]}/{row[1]}"
        )
