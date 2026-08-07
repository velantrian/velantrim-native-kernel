from __future__ import annotations

import os
import unittest
import uuid

from native_kernel.postgresql_profile import (
    PostgreSQLAppendStore,
    PostgreSQLReplayProjector,
    ProjectionCorrupt,
)
from native_kernel.semantic_core.models import Command, EventType

DSN = os.environ.get("NK_TEST_POSTGRES_DSN")


class AllowAuthority:
    def require(self, command: Command) -> object:
        return {"allowed": True, "command_id": command.command_id}


def make_command(key: str) -> Command:
    return Command(
        command_id="command:" + uuid.uuid4().hex,
        idempotency_key=key,
        stream_id="stream:p3-link",
        actor_ref="operator:p3",
        authority_ref="authority:p3",
        event_type=EventType.ADMIT,
        schema_version="1",
        payload={"claim_id": "claim:receipt-link"},
    )


@unittest.skipUnless(DSN, "NK_TEST_POSTGRES_DSN is required for PostgreSQL integration tests")
class ProjectionReceiptLinkIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.store = PostgreSQLAppendStore.from_dsn(DSN, AllowAuthority())
        cls.projector = PostgreSQLReplayProjector.from_dsn(DSN)
        cls.store.migrate()

    def test_projection_rejects_valid_but_mismatched_receipt_link(self) -> None:
        instance = "instance:" + uuid.uuid4().hex
        self.store.register_instance(instance)
        token = self.store.acquire_writer_lease(instance, "writer:p3-link", ttl_seconds=120)
        self.store.append(make_command("idem:p3:receipt-link"), token)

        replay = self.projector.replay(instance)
        rebuilt = self.projector.rebuild_projection(instance)
        self.assertNotEqual(replay.receipt.receipt_id, rebuilt.receipt.receipt_id)

        import psycopg

        with psycopg.connect(DSN) as connection:
            with connection.transaction(), connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE native_kernel.projections SET receipt_id = %s "
                    "WHERE instance_id = %s AND projection_name = %s",
                    (replay.receipt.receipt_id, instance, rebuilt.projection.projection_name),
                )

        with self.assertRaisesRegex(ProjectionCorrupt, "linked rebuild Receipt"):
            self.projector.load_projection(instance)


if __name__ == "__main__":
    unittest.main()
