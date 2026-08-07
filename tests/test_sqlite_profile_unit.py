from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from native_kernel.semantic_core import AuthorityGrant, Command, EventType, StaticAuthorityPolicy
from native_kernel.sqlite_profile import (
    AppendStatus,
    IdempotencyConflict,
    SQLiteAppendStore,
    SQLiteReplayProjector,
    StaleWriterEpoch,
    WriterLeaseBusy,
)


def policy() -> StaticAuthorityPolicy:
    return StaticAuthorityPolicy((AuthorityGrant(
        authority_ref="authority:test",
        actor_ref="operator:test",
        policy_ref="policy:test",
        authority_kind="operator-delegation",
        allowed_event_types=tuple(EventType),
        stream_prefixes=("stream:",),
    ),))


def command(key: str, payload: dict[str, str] | None = None) -> Command:
    return Command(
        command_id="command:" + key.replace(":", "-"),
        idempotency_key=key,
        stream_id="stream:test",
        actor_ref="operator:test",
        authority_ref="authority:test",
        event_type=EventType.ADMIT,
        schema_version="1",
        payload=payload or {"claim_id": "claim:a"},
    )


class SQLiteProfileUnitTests(unittest.TestCase):
    def test_append_retry_fencing_and_replay(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = str(Path(directory) / "kernel.db")
            store = SQLiteAppendStore(path, policy())
            projector = SQLiteReplayProjector(path)
            self.assertEqual(len(store.migrate()), 2)
            self.assertEqual(store.migrate(), ())
            instance = "instance:test"
            store.register_instance(instance)
            token = store.acquire_writer_lease(instance, "writer:one", ttl_seconds=120)
            first = store.append(command("idem:test"), token)
            retry = store.append(command("idem:test"), token)
            self.assertIs(first.status, AppendStatus.APPENDED)
            self.assertIs(retry.status, AppendStatus.RETURN_ORIGINAL_APPEND_RESULT)
            self.assertEqual(first.event.event_hash, retry.event.event_hash)
            with self.assertRaises(IdempotencyConflict):
                store.append(command("idem:test", {"claim_id": "claim:b"}), token)
            with self.assertRaises(WriterLeaseBusy):
                store.acquire_writer_lease(instance, "writer:two", ttl_seconds=120)
            replay = projector.replay(instance)
            self.assertEqual(replay.snapshot.event_count, 1)
            rebuilt = projector.rebuild_projection(instance)
            self.assertEqual(projector.load_projection(instance), rebuilt.projection)
            store.release_writer_lease(token)
            replacement = store.acquire_writer_lease(instance, "writer:two", ttl_seconds=120)
            self.assertGreater(replacement.epoch, token.epoch)
            with self.assertRaises(StaleWriterEpoch):
                store.append(command("idem:stale"), token)

    def test_fault_rolls_back_without_sequence_gap(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = str(Path(directory) / "kernel.db")
            baseline = SQLiteAppendStore(path, policy())
            baseline.migrate()
            baseline.register_instance("instance:rollback")
            token = baseline.acquire_writer_lease("instance:rollback", "writer:test", ttl_seconds=120)
            def fail(_: object) -> None:
                raise RuntimeError("fault")
            failing = SQLiteAppendStore(path, policy(), fault_hook=fail)
            with self.assertRaises(RuntimeError):
                failing.append(command("idem:fault"), token)
            result = baseline.append(command("idem:fault"), token)
            self.assertEqual((result.event.global_seq, result.event.stream_seq), (1, 1))


if __name__ == "__main__":
    unittest.main()
