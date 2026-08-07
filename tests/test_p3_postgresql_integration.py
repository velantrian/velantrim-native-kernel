from __future__ import annotations

import os
import unittest
import uuid

from native_kernel.postgresql_profile import (
    HistoryAdvanced,
    PostgreSQLAppendStore,
    PostgreSQLReplayProjector,
    ProjectionCorrupt,
    ProjectionNotFound,
    ReceiptCorrupt,
    StoredEventCorrupt,
)
from native_kernel.semantic_core.errors import UnsupportedVersion
from native_kernel.semantic_core.models import Command, EventType, SemanticEvent
from native_kernel.semantic_core.reducer import reduce_events
from native_kernel.semantic_core.upcasting import UpcastStep, UpcasterRegistry

DSN = os.environ.get("NK_TEST_POSTGRES_DSN")


class AllowAuthority:
    def require(self, command: Command) -> object:
        return {"allowed": True, "command_id": command.command_id}


def make_command(
    key: str,
    *,
    event_type: EventType = EventType.ADMIT,
    payload: dict[str, object] | None = None,
    schema_version: str = "1",
    stream_id: str = "stream:p3",
) -> Command:
    return Command(
        command_id="command:" + uuid.uuid4().hex,
        idempotency_key=key,
        stream_id=stream_id,
        actor_ref="operator:p3",
        authority_ref="authority:p3",
        event_type=event_type,
        schema_version=schema_version,
        payload=payload or {"claim_id": "claim:a"},
    )


@unittest.skipUnless(DSN, "NK_TEST_POSTGRES_DSN is required for PostgreSQL integration tests")
class P3PostgreSQLIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.store = PostgreSQLAppendStore.from_dsn(DSN, AllowAuthority())
        cls.projector = PostgreSQLReplayProjector.from_dsn(DSN)
        cls.store.migrate()

    def setUp(self) -> None:
        self.instance = "instance:" + uuid.uuid4().hex
        self.store.register_instance(self.instance)
        self.token = self.store.acquire_writer_lease(
            self.instance, "writer:p3", ttl_seconds=120
        )

    def append(self, command: Command):
        return self.store.append(command, self.token).event

    def test_replay_from_empty_matches_direct_reducer_and_persists_receipt(self) -> None:
        stored = [
            self.append(make_command("idem:p3:admit")),
            self.append(
                make_command(
                    "idem:p3:link",
                    event_type=EventType.LINK,
                    payload={
                        "from_claim_id": "claim:a",
                        "relation": "supports",
                        "to_claim_id": "claim:b",
                    },
                )
            ),
            self.append(
                make_command(
                    "idem:p3:utilized",
                    event_type=EventType.UTILIZED,
                    payload={"claim_id": "claim:a"},
                )
            ),
        ]
        direct = reduce_events(
            SemanticEvent(
                event.global_seq,
                event.stream_id,
                event.stream_seq,
                event.event_type,
                event.schema_version,
                event.payload,
            )
            for event in stored
        )
        result = self.projector.replay(self.instance)
        self.assertEqual(result.snapshot.state.digest, direct.digest)
        self.assertEqual(result.snapshot.event_count, 3)
        loaded = self.projector.load_receipt(result.receipt.receipt_id)
        self.assertEqual(loaded.receipt_hash, result.receipt.receipt_hash)
        self.assertEqual(self.projector.count_receipts(self.instance), 1)

    def test_projection_destroy_rebuild_is_deterministic_and_generation_monotonic(self) -> None:
        self.append(make_command("idem:p3:one"))
        first = self.projector.rebuild_projection(self.instance)
        second = self.projector.rebuild_projection(self.instance)
        self.assertEqual(first.projection.generation, 1)
        self.assertEqual(second.projection.generation, 2)
        self.assertEqual(first.projection.state_digest, second.projection.state_digest)
        self.assertTrue(self.projector.destroy_projection(self.instance))
        with self.assertRaises(ProjectionNotFound):
            self.projector.load_projection(self.instance)
        third = self.projector.rebuild_projection(self.instance)
        self.assertEqual(third.projection.generation, 3)
        self.assertEqual(third.projection.state_digest, first.projection.state_digest)
        self.assertEqual(self.projector.load_projection(self.instance), third.projection)

    def test_transactional_fault_preserves_previous_projection_and_receipts(self) -> None:
        self.append(make_command("idem:p3:fault"))
        first = self.projector.rebuild_projection(self.instance)

        def fail_after_receipt(_: object) -> None:
            raise RuntimeError("fault injection before projection commit")

        failing = PostgreSQLReplayProjector.from_dsn(
            DSN, receipt_fault_hook=fail_after_receipt
        )
        with self.assertRaises(RuntimeError):
            failing.rebuild_projection(self.instance)
        loaded = self.projector.load_projection(self.instance)
        self.assertEqual(loaded.generation, first.projection.generation)
        self.assertEqual(loaded.state_digest, first.projection.state_digest)
        self.assertEqual(self.projector.count_receipts(self.instance), 1)

    def test_history_advance_rejects_stale_projection(self) -> None:
        self.append(make_command("idem:p3:before"))

        def advance(_: object) -> None:
            self.append(make_command("idem:p3:after"))

        stale = PostgreSQLReplayProjector.from_dsn(DSN, snapshot_hook=advance)
        with self.assertRaises(HistoryAdvanced):
            stale.rebuild_projection(self.instance)
        with self.assertRaises(ProjectionNotFound):
            self.projector.load_projection(self.instance)
        self.assertEqual(self.projector.count_receipts(self.instance), 0)
        rebuilt = self.projector.rebuild_projection(self.instance)
        self.assertEqual(rebuilt.snapshot.event_count, 2)

    def test_stored_event_and_projection_corruption_are_detected(self) -> None:
        event = self.append(make_command("idem:p3:corrupt"))
        import psycopg

        with psycopg.connect(DSN) as connection:
            with connection.transaction(), connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE native_kernel.events SET payload_canonical = %s "
                    "WHERE instance_id = %s AND global_seq = %s",
                    (b"{}", self.instance, event.global_seq),
                )
        with self.assertRaises(StoredEventCorrupt):
            self.projector.replay(self.instance, persist_receipt=False)

        other = "instance:" + uuid.uuid4().hex
        self.store.register_instance(other)
        token = self.store.acquire_writer_lease(other, "writer:p3", ttl_seconds=120)
        self.store.append(make_command("idem:p3:projection"), token)
        self.projector.rebuild_projection(other)
        with psycopg.connect(DSN) as connection:
            with connection.transaction(), connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE native_kernel.projections SET state_canonical = %s "
                    "WHERE instance_id = %s",
                    (b"{}", other),
                )
        with self.assertRaises(ProjectionCorrupt):
            self.projector.load_projection(other)

    def test_receipt_corruption_is_detected(self) -> None:
        self.append(make_command("idem:p3:receipt"))
        result = self.projector.replay(self.instance)
        import psycopg

        with psycopg.connect(DSN) as connection:
            with connection.transaction(), connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE native_kernel.operation_receipts SET receipt_canonical = %s "
                    "WHERE receipt_id = %s",
                    (b"{}", result.receipt.receipt_id),
                )
        with self.assertRaises(ReceiptCorrupt):
            self.projector.load_receipt(result.receipt.receipt_id)

    def test_explicit_upcaster_path_is_required(self) -> None:
        self.append(make_command("idem:p3:v0", schema_version="0"))
        with self.assertRaises(UnsupportedVersion):
            self.projector.replay(self.instance, persist_receipt=False)
        registry = UpcasterRegistry(
            target_version="1",
            steps=(UpcastStep("0", "1", lambda payload: dict(payload)),),
        )
        compatible = PostgreSQLReplayProjector.from_dsn(DSN, upcasters=registry)
        result = compatible.replay(self.instance, persist_receipt=False)
        self.assertEqual(result.snapshot.event_count, 1)
        self.assertIn("claim:a", result.snapshot.state.admitted_claim_ids)


if __name__ == "__main__":
    unittest.main()
