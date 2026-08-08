from __future__ import annotations

import hashlib
import importlib
import json
import sys
import tempfile
import unittest
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path

from native_kernel.postgresql_profile import (
    AppendStatus,
    MigrationDrift,
    PostgreSQLAppendStore,
    StoredEvent,
    StoredEventCorrupt,
    WriterToken,
    build_event_envelope,
    canonical_recorded_at,
    discover_migrations,
    event_hash,
    payload_hash,
)
from native_kernel.semantic_core.canonical import canonical_json_bytes
from native_kernel.postgresql_profile.migrations import Migration, apply_migrations
from native_kernel.semantic_core.errors import ContractViolation
from native_kernel.semantic_core.models import Command, EventType


def fixture_command() -> Command:
    return Command(
        command_id="command:0001",
        idempotency_key="idem:0001",
        stream_id="stream:research-demo",
        actor_ref="operator:fixture",
        authority_ref="authority:fixture-only",
        event_type=EventType.ADMIT,
        schema_version="1",
        payload={
            "claim_id": "nkc1:31ef0e9f661cc97f4921e73a3ea9dcff1051aa0e368d50da48cb5d945ecfe00f",
            "policy_ref": "policy:research-admission-v1",
        },
    )


class HashingTests(unittest.TestCase):
    def test_fixture_payload_and_event_hash_match(self) -> None:
        command = fixture_command()
        envelope, payload_bytes, envelope_bytes = build_event_envelope(
            command,
            event_id="event:0001",
            global_seq=1,
            stream_seq=1,
            recorded_at=datetime(2026, 8, 6, 18, 1, tzinfo=timezone.utc),
            prev_global_hash="GENESIS",
        )
        self.assertEqual(
            envelope["payload_hash"],
            "nkp1:8e7e54f646e1501c917eeb4df7f6821e2c213362c96530d9a055f83b565202ee",
        )
        self.assertEqual(
            envelope["event_hash"],
            "nke1:00816e0625c8318bb02497b9007e51a89ee94a6ee0bb3532909d2abb6c58087a",
        )
        self.assertEqual(payload_hash(command.as_contract_object()["payload"]), envelope["payload_hash"])
        without_hash = dict(envelope)
        without_hash.pop("event_hash")
        self.assertEqual(event_hash(without_hash), envelope["event_hash"])
        self.assertEqual(json.loads(payload_bytes), command.as_contract_object()["payload"])
        self.assertEqual(json.loads(envelope_bytes), envelope)

    def test_recorded_at_requires_exact_utc_second(self) -> None:
        self.assertEqual(
            canonical_recorded_at(datetime(2026, 8, 7, 5, 0, tzinfo=timezone.utc)),
            "2026-08-07T05:00:00Z",
        )
        with self.assertRaises(ContractViolation):
            canonical_recorded_at(datetime(2026, 8, 7, 5, 0, 0, 1, tzinfo=timezone.utc))
        with self.assertRaises(ContractViolation):
            canonical_recorded_at(datetime(2026, 8, 7, 5, 0))

    def test_envelope_rejects_bad_previous_hash_and_sequences(self) -> None:
        command = fixture_command()
        kwargs = dict(
            command=command,
            event_id="event:x",
            global_seq=1,
            stream_seq=1,
            recorded_at=datetime(2026, 8, 7, 5, 0, tzinfo=timezone.utc),
            prev_global_hash="bad",
        )
        with self.assertRaises(ContractViolation):
            build_event_envelope(**kwargs)
        kwargs["prev_global_hash"] = "GENESIS"
        kwargs["global_seq"] = True
        with self.assertRaises(ContractViolation):
            build_event_envelope(**kwargs)

    def test_stored_envelope_rejects_unexpected_committed_fields(self) -> None:
        command = fixture_command()
        recorded_at = datetime(2026, 8, 6, 18, 1, tzinfo=timezone.utc)
        envelope, payload_bytes, envelope_bytes = build_event_envelope(
            command,
            event_id="event:0001",
            global_seq=1,
            stream_seq=1,
            recorded_at=recorded_at,
            prev_global_hash="GENESIS",
        )
        event = StoredEvent(
            instance_id="instance:test",
            event_id="event:0001",
            command_id=command.command_id,
            idempotency_key=command.idempotency_key,
            command_contract=command.contract,
            command_digest=command.digest,
            stream_id=command.stream_id,
            global_seq=1,
            stream_seq=1,
            actor_ref=command.actor_ref,
            authority_ref=command.authority_ref,
            recorded_at=recorded_at,
            event_type=command.event_type,
            schema_version=command.schema_version,
            payload=command.as_contract_object()["payload"],
            prev_global_hash="GENESIS",
            payload_hash=envelope["payload_hash"],
            event_hash=envelope["event_hash"],
            writer_epoch=1,
            payload_canonical=payload_bytes,
            envelope_canonical=envelope_bytes,
        )
        PostgreSQLAppendStore._verify_stored_event(event)

        forged = dict(envelope)
        forged["unexpected"] = "field"
        forged_without_hash = dict(forged)
        forged_without_hash.pop("event_hash")
        forged["event_hash"] = event_hash(forged_without_hash)
        corrupted = replace(
            event,
            event_hash=forged["event_hash"],
            envelope_canonical=canonical_json_bytes(forged),
        )
        with self.assertRaisesRegex(StoredEventCorrupt, "field set mismatch"):
            PostgreSQLAppendStore._verify_stored_event(corrupted)


class MigrationTests(unittest.TestCase):
    def test_discovery_is_ordered_and_checksummed(self) -> None:
        migrations = discover_migrations()
        self.assertEqual([item.version for item in migrations], sorted(item.version for item in migrations))
        self.assertEqual(migrations[0].version, "0001")
        self.assertEqual(migrations[0].sha256, hashlib.sha256(migrations[0].path.read_bytes()).hexdigest())
        self.assertIn("native_kernel.idempotency_records", migrations[0].sql)
        self.assertIn("native_kernel.writer_leases", migrations[0].sql)
        self.assertIn("writer_epoch bigint", migrations[0].sql)

    def test_invalid_migration_filename_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "bad.sql").write_text("SELECT 1;", encoding="utf-8")
            with self.assertRaises(ValueError):
                discover_migrations(root)

    def test_migration_drift_is_rejected(self) -> None:
        migration = Migration("0001", "x", "SELECT 1", "a" * 64, Path("0001_x.sql"))

        class Cursor:
            def __enter__(self): return self
            def __exit__(self, *args): return False
            def execute(self, sql, params=None): pass
            def fetchone(self): return ("x", "b" * 64)

        class Tx:
            def __enter__(self): return self
            def __exit__(self, *args): return False

        class Connection:
            def transaction(self): return Tx()
            def cursor(self): return Cursor()

        with self.assertRaises(MigrationDrift):
            apply_migrations(Connection(), [migration])


class BoundaryTests(unittest.TestCase):
    def test_profile_import_does_not_require_psycopg(self) -> None:
        before = set(sys.modules)
        module = importlib.import_module("native_kernel.postgresql_profile")
        self.assertTrue(hasattr(module, "PostgreSQLAppendStore"))
        self.assertNotIn("psycopg", set(sys.modules) - before)

    def test_writer_token_validates_identity_epoch_and_timezone(self) -> None:
        token = WriterToken(
            "instance:test",
            "writer:test",
            1,
            datetime(2026, 8, 7, 5, 0, tzinfo=timezone.utc),
        )
        self.assertEqual(token.epoch, 1)
        with self.assertRaises(ContractViolation):
            WriterToken("", "writer:test", 1, token.expires_at)
        with self.assertRaises(ContractViolation):
            WriterToken("instance:test", "writer:test", True, token.expires_at)
        with self.assertRaises(ContractViolation):
            WriterToken("instance:test", "writer:test", 1, datetime(2026, 8, 7, 5, 0))

    def test_append_status_is_explicit(self) -> None:
        self.assertEqual(AppendStatus.APPENDED.value, "APPENDED")
        self.assertEqual(
            AppendStatus.RETURN_ORIGINAL_APPEND_RESULT.value,
            "RETURN_ORIGINAL_APPEND_RESULT",
        )


if __name__ == "__main__":
    unittest.main()
