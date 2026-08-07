from __future__ import annotations

import unittest
from datetime import datetime, timezone

from native_kernel.postgresql_profile.replay_models import OperationType, OperationalReceipt, ReplaySnapshot
from native_kernel.semantic_core.errors import ContractViolation, ReceiptOverclaim, UnsupportedVersion
from native_kernel.semantic_core.models import EventType, SemanticEvent
from native_kernel.semantic_core.reducer import SemanticState, reduce_event
from native_kernel.semantic_core.state_codec import semantic_state_from_contract_object
from native_kernel.semantic_core.upcasting import UpcastStep, UpcasterRegistry, identity_upcaster_registry


class UpcasterTests(unittest.TestCase):
    def test_identity_and_multi_step_upcast(self) -> None:
        identity = identity_upcaster_registry("1")
        result = identity.upcast("1", {"claim_id": "claim:a"})
        self.assertEqual(result.applied_steps, ())
        self.assertEqual(dict(result.payload), {"claim_id": "claim:a"})

        registry = UpcasterRegistry(
            target_version="2",
            steps=(
                UpcastStep("0", "1", lambda payload: {**dict(payload), "claim_id": "claim:a"}),
                UpcastStep("1", "2", lambda payload: {**dict(payload), "migrated": True}),
            ),
        )
        result = registry.upcast("0", {})
        self.assertEqual(result.target_version, "2")
        self.assertEqual(result.applied_steps, (("0", "1"), ("1", "2")))
        self.assertEqual(dict(result.payload), {"claim_id": "claim:a", "migrated": True})

    def test_missing_duplicate_cycle_and_non_mapping_are_rejected(self) -> None:
        with self.assertRaises(UnsupportedVersion):
            identity_upcaster_registry("1").upcast("0", {})
        with self.assertRaises(ContractViolation):
            UpcasterRegistry(
                target_version="2",
                steps=(
                    UpcastStep("0", "1", lambda value: value),
                    UpcastStep("0", "2", lambda value: value),
                ),
            )
        with self.assertRaises(ContractViolation):
            UpcasterRegistry(
                target_version="3",
                steps=(
                    UpcastStep("0", "1", lambda value: value),
                    UpcastStep("1", "0", lambda value: value),
                ),
            )
        registry = UpcasterRegistry(
            target_version="1",
            steps=(UpcastStep("0", "1", lambda value: ["not", "mapping"]),),
        )
        with self.assertRaises(ContractViolation):
            registry.upcast("0", {})


class StateCodecTests(unittest.TestCase):
    def test_round_trip_and_noncanonical_state_rejection(self) -> None:
        state = reduce_event(
            SemanticState(),
            SemanticEvent(1, "stream:a", 1, EventType.ADMIT, "1", {"claim_id": "claim:a"}),
        )
        decoded = semantic_state_from_contract_object(state.as_contract_object())
        self.assertEqual(decoded, state)
        changed = state.as_contract_object()
        changed["admitted_claim_ids"] = ["claim:z", "claim:a"]
        with self.assertRaises(ContractViolation):
            semantic_state_from_contract_object(changed)


class ReceiptTests(unittest.TestCase):
    def test_receipt_is_canonical_and_bounded(self) -> None:
        snapshot = ReplaySnapshot(
            instance_id="instance:a",
            state=SemanticState(),
            event_count=0,
            first_global_seq=0,
            last_global_seq=0,
            last_event_hash=None,
        )
        receipt = OperationalReceipt(
            receipt_id="receipt:a",
            operation_type=OperationType.REPLAY,
            instance_id=snapshot.instance_id,
            event_count=0,
            first_global_seq=0,
            last_global_seq=0,
            last_event_hash=None,
            state_digest=snapshot.state.digest,
            known_limits=("bounded snapshot only",),
            created_at=datetime(2026, 8, 7, tzinfo=timezone.utc),
        )
        self.assertTrue(receipt.receipt_hash.startswith("nkr0:"))
        self.assertIn(b'"claims_truth_established":false', receipt.canonical_bytes)

    def test_receipt_overclaims_and_projection_shape_are_rejected(self) -> None:
        kwargs = dict(
            receipt_id="receipt:a",
            operation_type=OperationType.REPLAY,
            instance_id="instance:a",
            event_count=0,
            first_global_seq=0,
            last_global_seq=0,
            state_digest=SemanticState().digest,
            known_limits=("bounded",),
            created_at=datetime(2026, 8, 7, tzinfo=timezone.utc),
        )
        with self.assertRaises(ReceiptOverclaim):
            OperationalReceipt(**kwargs, claims_truth_established=True)
        with self.assertRaises(ContractViolation):
            OperationalReceipt(**kwargs, projection_name="semantic-state")


if __name__ == "__main__":
    unittest.main()
