from __future__ import annotations

import unittest
from datetime import datetime, timezone

from native_kernel.profile_common import event_envelope as common
from native_kernel.postgresql_profile import hashing as postgresql
from native_kernel.semantic_core.errors import ContractViolation
from native_kernel.semantic_core.models import Command, EventType
from native_kernel.sqlite_profile import hashing as sqlite


def fixture_command() -> Command:
    return Command(
        command_id="command:shared-envelope",
        idempotency_key="idem:shared-envelope",
        stream_id="stream:shared-envelope",
        actor_ref="operator:fixture",
        authority_ref="authority:fixture-only",
        event_type=EventType.ADMIT,
        schema_version="1",
        payload={"claim_id": "claim:shared-envelope", "ordinal": 1},
    )


class SharedEventEnvelopeContractTests(unittest.TestCase):
    def test_profile_surfaces_delegate_to_the_shared_primitive(self) -> None:
        for name in (
            "payload_hash",
            "event_hash",
            "canonical_recorded_at",
            "build_event_envelope",
        ):
            with self.subTest(name=name):
                self.assertIs(getattr(postgresql, name), getattr(common, name))
                self.assertIs(getattr(sqlite, name), getattr(common, name))

    def test_valid_input_is_byte_identical_across_all_surfaces(self) -> None:
        kwargs = dict(
            command=fixture_command(),
            event_id="event:shared-envelope",
            global_seq=3,
            stream_seq=2,
            recorded_at=datetime(2026, 9, 9, 12, 0, tzinfo=timezone.utc),
            prev_global_hash="GENESIS",
        )
        common_result = common.build_event_envelope(**kwargs)
        self.assertEqual(postgresql.build_event_envelope(**kwargs), common_result)
        self.assertEqual(sqlite.build_event_envelope(**kwargs), common_result)
        envelope, payload_bytes, envelope_bytes = common_result
        self.assertEqual(postgresql.payload_hash(envelope["payload"]), envelope["payload_hash"])
        self.assertEqual(sqlite.payload_hash(envelope["payload"]), envelope["payload_hash"])
        without_hash = dict(envelope)
        without_hash.pop("event_hash")
        self.assertEqual(postgresql.event_hash(without_hash), envelope["event_hash"])
        self.assertEqual(sqlite.event_hash(without_hash), envelope["event_hash"])
        self.assertIsInstance(payload_bytes, bytes)
        self.assertIsInstance(envelope_bytes, bytes)

    def test_invalid_inputs_preserve_contract_violation_semantics(self) -> None:
        base = dict(
            command=fixture_command(),
            event_id="event:shared-envelope",
            global_seq=1,
            stream_seq=1,
            recorded_at=datetime(2026, 9, 9, 12, 0, tzinfo=timezone.utc),
            prev_global_hash="GENESIS",
        )
        cases = (
            ("empty_event_id", {"event_id": ""}, "event_id must be a non-empty string"),
            ("boolean_global_seq", {"global_seq": True}, "global_seq must be a positive integer"),
            ("zero_stream_seq", {"stream_seq": 0}, "stream_seq must be a positive integer"),
            ("bad_previous_hash", {"prev_global_hash": "bad"}, "prev_global_hash must be GENESIS or an nke1 hash"),
            (
                "subsecond_timestamp",
                {"recorded_at": datetime(2026, 9, 9, 12, 0, 0, 1, tzinfo=timezone.utc)},
                "recorded_at must be truncated to an exact UTC second",
            ),
        )
        for label, mutation, expected_message in cases:
            with self.subTest(label=label):
                kwargs = dict(base)
                kwargs.update(mutation)
                for surface in (common, postgresql, sqlite):
                    with self.assertRaisesRegex(ContractViolation, expected_message):
                        surface.build_event_envelope(**kwargs)

    def test_existing_profile_import_paths_remain_available(self) -> None:
        self.assertEqual(
            postgresql.build_event_envelope.__module__,
            "native_kernel.profile_common.event_envelope",
        )
        self.assertEqual(
            sqlite.build_event_envelope.__module__,
            "native_kernel.profile_common.event_envelope",
        )
        self.assertTrue(callable(postgresql.build_event_envelope))
        self.assertTrue(callable(sqlite.build_event_envelope))


if __name__ == "__main__":
    unittest.main()
