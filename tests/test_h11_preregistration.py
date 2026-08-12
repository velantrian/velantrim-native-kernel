from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "ai_context" / "validate_h11_preregistration.py"
SPEC = importlib.util.spec_from_file_location("validate_h11_preregistration", MODULE_PATH)
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class H11PreregistrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.plan = json.loads((ROOT / "docs" / "research" / "H11_PREREGISTRATION.json").read_text(encoding="utf-8"))

    def validate(self, value: dict | None = None) -> None:
        module.validate(ROOT, copy.deepcopy(self.plan) if value is None else value, verify_bundle=False)

    def test_repository_preregistration_passes(self) -> None:
        self.validate()

    def test_full_validation_including_frozen_bundle_passes(self) -> None:
        module.validate(ROOT)

    def test_plan_cannot_authorize_implementation_or_execution(self) -> None:
        for field in ("implementation_authorized_by_this_plan", "execution_authorized_by_this_plan"):
            value = copy.deepcopy(self.plan)
            value["execution_admission"][field] = True
            with self.assertRaisesRegex(module.H11PreregistrationError, "implementation|execution"):
                self.validate(value)

    def test_exact_lab_bytes_cannot_become_architecture_authority(self) -> None:
        value = copy.deepcopy(self.plan)
        value["exact_laboratory_reproduction_manifest"]["architecture_authority_from_exactness"] = True
        with self.assertRaisesRegex(module.H11PreregistrationError, "Architecture authority"):
            self.validate(value)

    def test_h11_requires_independent_semantic_oracle(self) -> None:
        value = copy.deepcopy(self.plan)
        value["semantic_oracle_authority"]["required_class"] = "SELF_REVIEW"
        with self.assertRaisesRegex(module.H11PreregistrationError, "semantic oracle independence"):
            self.validate(value)

    def test_architecture_authors_cannot_self_certify_h11(self) -> None:
        value = copy.deepcopy(self.plan)
        value["semantic_oracle_authority"]["architecture_authors_may_self_certify_h11"] = True
        with self.assertRaisesRegex(module.H11PreregistrationError, "cannot self-certify"):
            self.validate(value)

    def test_no_reviewer_must_block_instead_of_fabricating_validation(self) -> None:
        value = copy.deepcopy(self.plan)
        value["reviewer_reproducer_independence_basis"]["no_qualifying_reviewer_outcome"] = "PASS"
        with self.assertRaisesRegex(module.H11PreregistrationError, "blocker"):
            self.validate(value)

    def test_mandatory_profile_mechanism_cannot_be_silently_removed(self) -> None:
        value = copy.deepcopy(self.plan)
        value["mechanism_dependency_graph_schema"]["mandatory_profile_mechanisms_to_audit"].remove("SHA-256 digest verification")
        with self.assertRaisesRegex(module.H11PreregistrationError, "mechanism audit inventory"):
            self.validate(value)

    def test_support_threshold_must_remain_zero_leakage(self) -> None:
        value = copy.deepcopy(self.plan)
        value["frozen_mechanism_leakage_rubric"]["support_threshold"] = "mandatory_profile_leakage_count <= 1"
        with self.assertRaisesRegex(module.H11PreregistrationError, "support threshold"):
            self.validate(value)

    def test_hard_failure_class_cannot_be_weakened(self) -> None:
        value = copy.deepcopy(self.plan)
        value["frozen_mechanism_leakage_rubric"]["hard_failure_class"] = "WARNING_ONLY"
        with self.assertRaisesRegex(module.H11PreregistrationError, "hard failure class"):
            self.validate(value)

    def test_not_tested_remains_legitimate_until_execution(self) -> None:
        value = copy.deepcopy(self.plan)
        value["allowed_a10_outcome_vocabulary"].remove("NOT_TESTED")
        with self.assertRaisesRegex(module.H11PreregistrationError, "outcome vocabulary"):
            self.validate(value)

    def test_next_gate_cannot_jump_past_execution_admission(self) -> None:
        value = copy.deepcopy(self.plan)
        value["execution_admission"]["next_gate_if_preregistered"] = "A10_H11_EXECUTION"
        with self.assertRaisesRegex(module.H11PreregistrationError, "next gate"):
            self.validate(value)


if __name__ == "__main__":
    unittest.main()
