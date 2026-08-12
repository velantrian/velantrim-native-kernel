from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


validator = _load_module(
    "h11_validate_execution_admission",
    ROOT / "tools" / "ai_context" / "validate_h11_execution_admission.py",
)


def _load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class H11ExecutionAdmissionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.admission = _load("docs/research/H11_EXECUTION_ADMISSION.json")
        self.reviewer = _load("docs/research/H11_REVIEWER_REPRODUCER_QUALIFICATION.json")
        self.dependency_schema = _load("docs/research/H11_DEPENDENCY_GRAPH_SCHEMA.json")
        self.raw_schema = _load("docs/research/H11_RAW_OBSERVATION_SCHEMA.json")
        self.semantic_schema = _load("docs/research/H11_SEMANTIC_ADJUDICATION_SCHEMA.json")
        self.plan = _load("docs/research/H11_PREREGISTRATION.json")

    def assert_rejected(self, **overrides) -> None:
        with self.assertRaises(validator.H11AdmissionError):
            validator.validate(ROOT, verify_history=False, **overrides)

    def test_repository_blocked_admission_package_is_valid(self) -> None:
        validator.validate(ROOT)
        self.assertEqual("BLOCKED", self.admission["admission"]["result"])
        self.assertEqual(
            "BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER",
            self.admission["admission"]["blocker"],
        )
        self.assertEqual("NOT_TESTED", self.admission["h11_outcome"])
        self.assertFalse(self.admission["implementation_authorized"])
        self.assertFalse(self.admission["execution_authorized"])

    def test_frozen_plan_digest_is_exact_repository_bytes(self) -> None:
        digest = hashlib.sha256((ROOT / "docs/research/H11_PREREGISTRATION.json").read_bytes()).hexdigest()
        self.assertEqual("60da649e675b79b3e70bf8a61cf03cb4d57bb989f4934b65ab8d50c925b19914", digest)

    def test_wrong_plan_digest_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.admission)
        mutated["plan"]["sha256"] = "0" * 64
        self.assert_rejected(admission_override=mutated)

    def test_wrong_plan_id_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.admission)
        mutated["plan"]["plan_id"] = "H11-WRONG"
        self.assert_rejected(admission_override=mutated)

    def test_wrong_frozen_plan_identity_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.plan)
        mutated["plan_id"] = "H11-WRONG"
        self.assert_rejected(plan_override=mutated)

    def test_family_must_remain_a10_h11(self) -> None:
        mutated = copy.deepcopy(self.admission)
        mutated["selected_family"] = "A10-H10"
        self.assert_rejected(admission_override=mutated)

    def test_implementation_authorization_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.admission)
        mutated["implementation_authorized"] = True
        self.assert_rejected(admission_override=mutated)

    def test_execution_authorization_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.admission)
        mutated["execution_authorized"] = True
        self.assert_rejected(admission_override=mutated)

    def test_dependency_graph_execution_authorization_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.admission)
        mutated["dependency_graph_execution_authorized"] = True
        self.assert_rejected(admission_override=mutated)

    def test_semantic_adjudication_authorization_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.admission)
        mutated["semantic_adjudication_authorized"] = True
        self.assert_rejected(admission_override=mutated)

    def test_runtime_thaw_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.admission)
        mutated["runtime_expansion"] = "THAWED"
        mutated["product_runtime_thaw"] = True
        self.assert_rejected(admission_override=mutated)

    def test_final_canon_promotion_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.admission)
        mutated["final_canon"] = "PROMOTED"
        self.assert_rejected(admission_override=mutated)

    def test_production_authorization_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.admission)
        mutated["production_authorized"] = True
        self.assert_rejected(admission_override=mutated)

    def test_h11_outcome_must_remain_not_tested(self) -> None:
        for outcome in ("SUPPORTED_FOR_SCOPE", "WEAKENED", "REFUTED", "INDETERMINATE", "PASS"):
            with self.subTest(outcome=outcome):
                mutated = copy.deepcopy(self.admission)
                mutated["h11_outcome"] = outcome
                self.assert_rejected(admission_override=mutated)

    def test_self_author_cannot_be_declared_independent(self) -> None:
        mutated = copy.deepcopy(self.reviewer)
        mutated.update(
            {
                "reviewer_identity_status": "ESTABLISHED",
                "reviewer_identity": "same-preregistration-author",
                "reviewer_role": "REVIEWER",
                "authorship_relation": "AUTHOR_OF_PREREGISTRATION",
                "custody_relation": "SAME_CUSTODY",
                "repository_visibility": "EVIDENCE_VISIBLE",
                "independence_basis": ["SELF_ASSERTED"],
                "evidence_references": ["self-review"],
                "qualification_result": "QUALIFIED",
            }
        )
        self.assert_rejected(reviewer_override=mutated)

    def test_missing_independence_basis_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.reviewer)
        del mutated["independence_basis"]
        self.assert_rejected(reviewer_override=mutated)

    def test_codex_bot_notice_cannot_be_independent_semantic_oracle(self) -> None:
        mutated = copy.deepcopy(self.admission)
        mutated["reviewer_reproducer"]["qualification_result"] = "CODEX_BOT_NOTICE"
        mutated["reviewer_reproducer"]["required_oracle_class"] = "CODEX_BOT_NOTICE"
        self.assert_rejected(admission_override=mutated)

    def test_ci_success_cannot_be_independent_semantic_oracle(self) -> None:
        mutated = copy.deepcopy(self.admission)
        mutated["reviewer_reproducer"]["qualification_result"] = "CI_SUCCESS"
        mutated["reviewer_reproducer"]["required_oracle_class"] = "CI_SUCCESS"
        self.assert_rejected(admission_override=mutated)

    def test_raw_and_semantic_layers_cannot_be_collapsed(self) -> None:
        mutated = copy.deepcopy(self.admission)
        mutated["schemas"]["raw_observations"] = mutated["schemas"]["semantic_adjudication"]
        self.assert_rejected(admission_override=mutated)

    def test_raw_schema_cannot_contain_final_h11_outcome(self) -> None:
        mutated = copy.deepcopy(self.raw_schema)
        mutated["properties"]["outcome"] = {"enum": validator.A10_OUTCOMES}
        self.assert_rejected(raw_schema_override=mutated)

    def test_missing_mandatory_profile_mechanism_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.admission)
        mutated["mandatory_profile_mechanisms"] = mutated["mandatory_profile_mechanisms"][:-1]
        self.assert_rejected(admission_override=mutated)

    def test_dependency_schema_must_require_all_twelve_mechanisms(self) -> None:
        mutated = copy.deepcopy(self.dependency_schema)
        spec = mutated["properties"]["mandatory_profile_mechanisms_covered"]
        spec["minItems"] = 11
        self.assert_rejected(dependency_schema_override=mutated)

    def test_unjustified_canon_dependency_cannot_be_removed(self) -> None:
        mutated = copy.deepcopy(self.dependency_schema)
        enum = mutated["properties"]["edges"]["items"]["properties"]["leakage_class"]["enum"]
        enum.remove("UNJUSTIFIED_CANON_DEPENDENCY")
        self.assert_rejected(dependency_schema_override=mutated)

    def test_indeterminate_cannot_be_added_as_leakage_class(self) -> None:
        mutated = copy.deepcopy(self.dependency_schema)
        enum = mutated["properties"]["edges"]["items"]["properties"]["leakage_class"]["enum"]
        enum.append("INDETERMINATE")
        self.assert_rejected(dependency_schema_override=mutated)

    def test_hard_refutation_weakening_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.admission)
        mutated["frozen_controls"]["hard_refutation"] = "weaker post-hoc refutation"
        self.assert_rejected(admission_override=mutated)

    def test_post_hoc_rubric_mutation_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.admission)
        mutated["frozen_controls"]["post_hoc_rubric_mutation"] = "ALLOWED"
        self.assert_rejected(admission_override=mutated)

    def test_support_threshold_mutation_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.semantic_schema)
        mutated["properties"]["leakage_rubric"]["properties"]["support_threshold"]["const"] = "good enough"
        self.assert_rejected(semantic_schema_override=mutated)

    def test_private_implementation_state_cannot_be_required_oracle_input(self) -> None:
        mutated = copy.deepcopy(self.semantic_schema)
        mutated["properties"]["input_policy"]["const"] = "PRIVATE_IMPLEMENTATION_STATE_REQUIRED"
        mutated["properties"]["subject_private_state_used"]["const"] = True
        self.assert_rejected(semantic_schema_override=mutated)

    def test_separate_post_merge_truth_checkpoint_remains_required(self) -> None:
        mutated = copy.deepcopy(self.admission)
        mutated["separate_post_merge_state_checkpoint_required"] = False
        self.assert_rejected(admission_override=mutated)


if __name__ == "__main__":
    unittest.main()
