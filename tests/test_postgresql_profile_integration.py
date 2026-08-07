from __future__ import annotations

import os
import threading
import unittest
import uuid
from concurrent.futures import ThreadPoolExecutor

from native_kernel.postgresql_profile import (
    AppendStatus,
    IdempotencyConflict,
    PostgreSQLAppendStore,
    StaleWriterEpoch,
    WriterLeaseBusy,
)
from native_kernel.semantic_core.models import Command, EventType

DSN = os.environ.get("NK_TEST_POSTGRES_DSN")


class AllowAuthority:
    def require(self, command: Command) -> object:
        return {"allowed": True, "command_id": command.command_id}


def make_command(key: str, *, claim: str = "claim:a") -> Command:
    return Command(
        command_id="command:" + uuid.uuid4().hex,
        idempotency_key=key,
        stream_id="stream:integration",
        actor_ref="operator:integration",
        authority_ref="authority:integration",
        event_type=EventType.ADMIT,
        schema_version="1",
        payload={"claim_id": claim},
    )


@unittest.skipUnless(DSN, "NK_TEST_POSTGRES_DSN is required for PostgreSQL integration tests")
class PostgreSQLIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.store = PostgreSQLAppendStore.from_dsn(DSN, AllowAuthority())
        cls.store.migrate()

    def setUp(self) -> None:
        self.instance = "instance:" + uuid.uuid4().hex
        self.store.register_instance(self.instance)
        self.token = self.store.acquire_writer_lease(
            self.instance, "writer:primary", ttl_seconds=60
        )

    def test_migration_and_instance_registration_are_idempotent(self) -> None:
        self.assertEqual(self.store.migrate(), ())
        self.store.register_instance(self.instance)

    def test_lease_busy_release_and_epoch_fencing(self) -> None:
        with self.assertRaises(WriterLeaseBusy):
            self.store.acquire_writer_lease(self.instance, "writer:other", ttl_seconds=60)
        old = self.token
        self.store.release_writer_lease(old)
        new = self.store.acquire_writer_lease(self.instance, "writer:other", ttl_seconds=60)
        self.assertGreater(new.epoch, old.epoch)
        with self.assertRaises(StaleWriterEpoch):
            self.store.append(make_command("idem:stale"), old)

    def test_append_retry_and_conflict_are_atomic(self) -> None:
        command = make_command("idem:one")
        first = self.store.append(command, self.token)
        retry = self.store.append(command, self.token)
        self.assertEqual(first.status, AppendStatus.APPENDED)
        self.assertEqual(retry.status, AppendStatus.RETURN_ORIGINAL_APPEND_RESULT)
        self.assertEqual(first.event.event_hash, retry.event.event_hash)
        self.assertEqual(self.store.count_events(self.instance), 1)
        with self.assertRaises(IdempotencyConflict):
            self.store.append(make_command("idem:one", claim="claim:different"), self.token)
        self.assertEqual(self.store.count_events(self.instance), 1)

    def test_transaction_rollback_preserves_contiguous_sequence(self) -> None:
        triggered = threading.Event()

        def fail_after_insert(event: object) -> None:
            triggered.set()
            raise RuntimeError("fault injection before commit")

        failing = PostgreSQLAppendStore.from_dsn(
            DSN, AllowAuthority(), fault_hook=fail_after_insert
        )
        command = make_command("idem:rollback")
        with self.assertRaises(RuntimeError):
            failing.append(command, self.token)
        self.assertTrue(triggered.is_set())
        self.assertEqual(self.store.count_events(self.instance), 0)
        result = self.store.append(command, self.token)
        self.assertEqual(result.event.global_seq, 1)
        self.assertEqual(result.event.stream_seq, 1)

    def test_concurrent_same_digest_appends_once(self) -> None:
        command = make_command("idem:concurrent")
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(lambda _: self.store.append(command, self.token), range(2)))
        self.assertEqual(
            {item.status for item in results},
            {AppendStatus.APPENDED, AppendStatus.RETURN_ORIGINAL_APPEND_RESULT},
        )
        self.assertEqual(len({item.event.event_hash for item in results}), 1)
        self.assertEqual(self.store.count_events(self.instance), 1)


if __name__ == "__main__":
    unittest.main()
