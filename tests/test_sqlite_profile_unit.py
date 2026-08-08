from __future__ import annotations

import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from native_kernel.semantic_core.canonical import canonical_json_bytes
from native_kernel.semantic_core import AuthorityGrant, Command, EventType, StaticAuthorityPolicy
from native_kernel.sqlite_profile import (
    AppendStatus,
    IdempotencyConflict,
    SQLiteAppendStore,
    SQLiteReplayProjector,
    StaleWriterEpoch,
    StoredEventCorrupt,
    UnsafeSQLiteVersion,
    WriterLeaseBusy,
)
from native_kernel.sqlite_profile.hashing import event_hash
from native_kernel.sqlite_profile.runtime import (
    MINIMUM_WAL_SAFE_SQLITE,
    require_safe_sqlite_for_wal,
    sqlite_wal_version_is_safe,
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


def command(key: str, payload: dict[str, object] | None = None) -> Command:
    return Command(
        command_id="command:" + key.replace(":", "-"),
        idempotency_key=key,
        stream_id="stream:test",
        actor_ref="operator:test",
        authority_ref="authority:test",
        event_type=EventType.ADMIT,
        schema_version="1",
        payload={"claim_id": "claim:a"} if payload is None else payload,
    )


class SQLiteProfileUnitTests(unittest.TestCase):
    def _store_with_event(
        self,
        directory: str,
        label: str,
        payload: dict[str, object] | None = None,
    ) -> tuple[SQLiteAppendStore, Path]:
        path = Path(directory) / f"{label}.db"
        store = SQLiteAppendStore(path, policy())
        store.migrate()
        store.register_instance("instance:test")
        token = store.acquire_writer_lease("instance:test", "writer:test", ttl_seconds=120)
        store.append(command(f"idem:{label}", payload), token)
        return store, path

    @staticmethod
    def _rewrite_envelope(path: Path, mutate: object) -> None:
        with sqlite3.connect(path) as connection:
            row = connection.execute(
                "SELECT envelope_canonical FROM events WHERE instance_id=? AND global_seq=1",
                ("instance:test",),
            ).fetchone()
            assert row is not None
            envelope = json.loads(bytes(row[0]).decode("utf-8"))
            assert callable(mutate)
            mutate(envelope)
            committed = dict(envelope)
            committed.pop("event_hash", None)
            envelope["event_hash"] = event_hash(committed)
            envelope_bytes = canonical_json_bytes(envelope)
            connection.execute(
                "UPDATE events SET envelope_canonical=?, event_hash=? "
                "WHERE instance_id=? AND global_seq=1",
                (envelope_bytes, envelope["event_hash"], "instance:test"),
            )

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

    def test_event_envelope_commits_exact_contract_time_payload_and_fields(self) -> None:
        mutations = {
            "contract": lambda envelope: envelope.__setitem__("contract", "nk-event-envelope/999"),
            "recorded_at": lambda envelope: envelope.__setitem__(
                "recorded_at", "2099-01-01T00:00:00Z"
            ),
            "payload": lambda envelope: envelope.__setitem__(
                "payload", {"claim_id": "claim:forged"}
            ),
            "unexpected": lambda envelope: envelope.__setitem__("uncommitted_field", "forged"),
            "missing": lambda envelope: envelope.pop("contract"),
        }
        for label, mutate in mutations.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as directory:
                store, path = self._store_with_event(directory, label)
                self._rewrite_envelope(path, mutate)
                with self.assertRaisesRegex(StoredEventCorrupt, "envelope"):
                    store.read_events("instance:test")

    def test_event_envelope_payload_comparison_preserves_json_types(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store, path = self._store_with_event(
                directory,
                "typed-payload",
                {"claim_id": "claim:a", "ordinal": 1},
            )
            self._rewrite_envelope(
                path,
                lambda envelope: envelope["payload"].__setitem__("ordinal", True),
            )
            with self.assertRaisesRegex(StoredEventCorrupt, "payload mismatch"):
                store.read_events("instance:test")

    def test_invalid_stored_json_is_reported_as_corruption(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store, path = self._store_with_event(directory, "invalid-envelope-json")
            with sqlite3.connect(path) as connection:
                connection.execute(
                    "UPDATE events SET envelope_canonical=? WHERE instance_id=? AND global_seq=1",
                    (b"{", "instance:test"),
                )
            with self.assertRaisesRegex(StoredEventCorrupt, "envelope canonical bytes are not JSON"):
                store.read_events("instance:test")

        with tempfile.TemporaryDirectory() as directory:
            store, _ = self._store_with_event(directory, "invalid-payload-json")
            store.corrupt_payload_canonical_for_test("instance:test", 1, b"{")
            with self.assertRaisesRegex(StoredEventCorrupt, "payload canonical bytes are not JSON"):
                store.read_events("instance:test")

    def test_timeout_parameter_controls_busy_timeout(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteAppendStore(
                Path(directory) / "timeout.db", policy(), timeout_seconds=0.2
            )
            connection = store._connect()
            try:
                row = connection.execute("PRAGMA busy_timeout").fetchone()
                self.assertIsNotNone(row)
                self.assertEqual(int(row[0]), 200)
            finally:
                connection.close()

    def test_migration_failure_rolls_back_the_complete_migration(self) -> None:
        migration = (
            (
                "broken-migration",
                "CREATE TABLE should_not_survive(value TEXT); THIS IS NOT VALID SQL;",
            ),
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "migration.db"
            store = SQLiteAppendStore(path, policy())
            with patch("native_kernel.sqlite_profile.adapter.MIGRATIONS", migration):
                with self.assertRaises(sqlite3.DatabaseError):
                    store.migrate()
            with sqlite3.connect(path) as connection:
                rows = connection.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
                ).fetchall()
            self.assertEqual(rows, [])


class SQLiteRuntimeGuardTests(unittest.TestCase):
    def test_wal_guard_has_a_conservative_fixed_floor(self) -> None:
        self.assertEqual(MINIMUM_WAL_SAFE_SQLITE, "3.51.3")
        for version in ("3.7.0", "3.45.1", "3.50.4", "3.51.2", "invalid"):
            with self.subTest(version=version):
                self.assertFalse(sqlite_wal_version_is_safe(version))
                with self.assertRaises(UnsafeSQLiteVersion):
                    require_safe_sqlite_for_wal(version)
        for version in ("3.51.3", "3.51.4", "3.52.0", "4.0.0"):
            with self.subTest(version=version):
                self.assertTrue(sqlite_wal_version_is_safe(version))
                self.assertEqual(require_safe_sqlite_for_wal(version), version)


if __name__ == "__main__":
    unittest.main()
