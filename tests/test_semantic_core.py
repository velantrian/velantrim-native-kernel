from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

from native_kernel.semantic_core import (
    AdmissionReceipt,
    AuthorityDenied,
    AuthorityGrant,
    ClaimIdentity,
    Command,
    ContractViolation,
    DeletionReceipt,
    DeletionState,
    EventType,
    InvalidTransition,
    ReceiptOverclaim,
    SemanticContent,
    SemanticEvent,
    SemanticRole,
    SequenceViolation,
    StaticAuthorityPolicy,
    UnsupportedVersion,
    claim_id,
    content_hash,
    lineage_id,
    reduce_events,
    run_transitions,
)

ROOT = Path(__file__).resolve().parents[1]

PACK = json.loads((ROOT / "contracts" / "fixture-pack.json").read_text(encoding="utf-8"))
GOLDEN = PACK["identity_golden"]["vectors"]


def command(payload: dict[str, object] | None = None, *, authority_ref: str = "authority:fixture") -> Command:
    return Command(
        command_id="command:1",
        idempotency_key="idem:1",
        stream_id="stream:research",
        actor_ref="operator:test",
        authority_ref=authority_ref,
        event_type=EventType.ADMIT,
        schema_version="1",
        payload=payload or {"claim_id": GOLDEN[0]["expected"]["claim_id"]},
    )


class CanonicalIdentityTests(unittest.TestCase):
    def test_golden_vectors_match(self) -> None:
        for vector in GOLDEN:
            self.assertEqual(content_hash(vector["content"]), vector["expected"]["content_hash"])
            self.assertEqual(claim_id(vector["claim_identity"]), vector["expected"]["claim_id"])
            self.assertEqual(lineage_id(vector["lineage_seed"]), vector["expected"]["lineage_id"])

    def test_invalid_values_are_rejected(self) -> None:
        for vector in PACK["identity_invalid"]["vectors"]:
            with self.subTest(vector=vector):
                with self.assertRaises(ContractViolation):
                    content_hash(vector["input"])

    def test_semantic_content_and_claim_identity_are_distinct(self) -> None:
        content = SemanticContent(
            role=SemanticRole.PROPOSITION,
            scope={"domain": "astronomy", "language": "en"},
            fields={"proposition": "The observed signal originated from source A."},
        )
        identity = ClaimIdentity(
            content_hash=content.content_hash,
            source_ref="source:observatory-7",
            source_record_id="obs-2026-0001",
            asserted_at="2026-08-06T18:00:00Z",
        )
        self.assertTrue(content.content_hash.startswith("nkh1:"))
        self.assertTrue(identity.claim_id.startswith("nkc1:"))
        self.assertNotEqual(content.content_hash.split(":", 1)[1], identity.claim_id.split(":", 1)[1])

    def test_scope_requires_domain(self) -> None:
        with self.assertRaises(ContractViolation):
            SemanticContent(
                role=SemanticRole.PROPOSITION,
                scope={"language": "en"},
                fields={"proposition": "x"},
            )


class CommandTests(unittest.TestCase):
    def test_digest_is_deterministic_across_key_order(self) -> None:
        left = command({"claim_id": "nkc1:" + "1" * 64, "policy_ref": "policy:test"})
        right = command({"policy_ref": "policy:test", "claim_id": "nkc1:" + "1" * 64})
        self.assertEqual(left.digest, right.digest)
        self.assertTrue(left.digest.startswith("nkd0:"))

    def test_digest_changes_with_payload(self) -> None:
        self.assertNotEqual(command({"claim_id": "a"}).digest, command({"claim_id": "b"}).digest)

    def test_command_rejects_float_and_null_payloads(self) -> None:
        with self.assertRaises(ContractViolation):
            command({"value": 1.25})
        with self.assertRaises(ContractViolation):
            command({"value": None})


class AuthorityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.policy = StaticAuthorityPolicy(
            [
                AuthorityGrant(
                    authority_ref="authority:fixture",
                    actor_ref="operator:test",
                    policy_ref="policy:admission-v1",
                    authority_kind="operator-delegation",
                    allowed_event_types=(EventType.ADMIT,),
                    stream_prefixes=("stream:",),
                )
            ]
        )

    def test_explicit_grant_allows(self) -> None:
        decision = self.policy.require(command())
        self.assertTrue(decision.allowed)
        self.assertEqual(decision.policy_ref, "policy:admission-v1")

    def test_unknown_authority_is_denied_by_default(self) -> None:
        with self.assertRaises(AuthorityDenied):
            self.policy.require(command(authority_ref="authority:missing"))

    def test_admission_receipt_rejects_truth_overclaim(self) -> None:
        decision = self.policy.require(command())
        with self.assertRaises(ReceiptOverclaim):
            AdmissionReceipt(
                command_id="command:1",
                decision=decision,
                known_limits=("decision-only",),
                claims_truth_established=True,
            )

    def test_admission_receipt_records_limit(self) -> None:
        decision = self.policy.require(command())
        receipt = AdmissionReceipt(
            command_id="command:1",
            decision=decision,
            known_limits=("authority decision is not truth evidence",),
        )
        self.assertFalse(receipt.as_contract_object()["claims_truth_established"])


class ReducerTests(unittest.TestCase):
    def events(self) -> list[SemanticEvent]:
        a = GOLDEN[0]["expected"]["claim_id"]
        b = GOLDEN[1]["expected"]["claim_id"]
        return [
            SemanticEvent(1, "stream:research", 1, EventType.ADMIT, "1", {"claim_id": a}),
            SemanticEvent(
                2,
                "stream:research",
                2,
                EventType.LINK,
                "1",
                {"from_claim_id": a, "relation": "SUPPORTS", "to_claim_id": b},
            ),
            SemanticEvent(3, "stream:research", 3, EventType.UTILIZED, "1", {"claim_id": a}),
            SemanticEvent(
                4,
                "stream:research",
                4,
                EventType.SUPERSEDED,
                "1",
                {"claim_id": a, "by_claim_id": b},
            ),
            SemanticEvent(5, "stream:research", 5, EventType.ERASED, "1", {"claim_id": a}),
        ]

    def test_reducer_is_deterministic(self) -> None:
        first = reduce_events(self.events())
        second = reduce_events(self.events())
        self.assertEqual(first, second)
        self.assertEqual(first.digest, second.digest)
        self.assertEqual(first.last_global_seq, 5)
        self.assertEqual(first.utilization_counts[0][1], 1)

    def test_non_contiguous_global_sequence_fails(self) -> None:
        events = self.events()
        events[1] = SemanticEvent(
            3, "stream:research", 2, EventType.UTILIZED, "1", {"claim_id": "claim:x"}
        )
        with self.assertRaises(SequenceViolation):
            reduce_events(events)

    def test_non_contiguous_stream_sequence_fails(self) -> None:
        events = self.events()
        events[1] = SemanticEvent(
            2, "stream:research", 3, EventType.UTILIZED, "1", {"claim_id": "claim:x"}
        )
        with self.assertRaises(SequenceViolation):
            reduce_events(events)

    def test_unsupported_schema_and_reducer_fail_explicitly(self) -> None:
        with self.assertRaises(UnsupportedVersion):
            reduce_events(
                [SemanticEvent(1, "stream:x", 1, EventType.ADMIT, "2", {"claim_id": "claim:x"})]
            )
        with self.assertRaises(UnsupportedVersion):
            reduce_events([], reducer_version="nk-p1-reducer/999")


class DeletionTests(unittest.TestCase):
    def test_fixture_paths_reach_expected_states(self) -> None:
        for scenario in PACK["deletion_scenarios"]["scenarios"]:
            final = run_transitions(
                DeletionState(scenario["initial_state"]),
                [DeletionState(item["to"]) for item in scenario["transitions"]],
            )
            self.assertEqual(final.value, scenario["expected_final_state"])

    def test_forbidden_transition_fails(self) -> None:
        with self.assertRaises(InvalidTransition):
            run_transitions(DeletionState.ACTIVE, [DeletionState.PHYSICALLY_ERASED])

    def test_deletion_receipt_rejects_global_overclaim(self) -> None:
        with self.assertRaises(ReceiptOverclaim):
            DeletionReceipt(
                request_id="request:1",
                authority_ref="authority:privacy",
                policy_ref="policy:erase-v1",
                final_state=DeletionState.PHYSICALLY_ERASED,
                verified_locations=("primary",),
                unverified_or_pending_locations=("backup",),
                known_limits=("backup retention window",),
                claims_complete_global_erasure=True,
            )

    def test_deletion_receipt_rejects_location_overlap(self) -> None:
        with self.assertRaises(ContractViolation):
            DeletionReceipt(
                request_id="request:1",
                authority_ref="authority:privacy",
                policy_ref="policy:erase-v1",
                final_state=DeletionState.PARTIALLY_ERASED,
                verified_locations=("primary",),
                unverified_or_pending_locations=("primary",),
                known_limits=("partial",),
            )


class StorageBoundaryTests(unittest.TestCase):
    def test_semantic_core_has_no_database_or_network_imports(self) -> None:
        forbidden = re.compile(
            r"^\s*(?:from|import)\s+(?:psycopg|asyncpg|sqlite3|sqlalchemy|requests|httpx)\b",
            re.MULTILINE,
        )
        for path in (ROOT / "native_kernel" / "semantic_core").glob("*.py"):
            self.assertIsNone(forbidden.search(path.read_text(encoding="utf-8")), path)


if __name__ == "__main__":
    unittest.main()
