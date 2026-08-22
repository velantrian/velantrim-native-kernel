from __future__ import annotations

import copy
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


evaluator = _load_module(
    "h11_evaluate_positive_qualification_policy_guard",
    ROOT / "tools" / "ai_context" / "evaluate_h11_positive_qualification.py",
)


def _load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class H11PositiveQualificationPolicyGuardTests(unittest.TestCase):
    def setUp(self) -> None:
        self.policy = _load("docs/research/H11_POSITIVE_QUALIFICATION_POLICY.json")

    def assert_policy_rejected(self, mutate) -> None:
        policy = copy.deepcopy(self.policy)
        mutate(policy)
        with self.assertRaises(evaluator.EvidenceFailure) as context:
            evaluator._validate_policy(policy)
        self.assertEqual(context.exception.code, "MALFORMED_EVIDENCE")

    def test_candidate_owner_separation_cannot_be_disabled(self) -> None:
        self.assert_policy_rejected(
            lambda policy: policy["review_surface"].__setitem__(
                "candidate_must_not_equal_repository_owner", False
            )
        )

    def test_candidate_evidence_freshness_cannot_be_weakened(self) -> None:
        self.assert_policy_rejected(
            lambda policy: policy["basis_1"].__setitem__("max_age_days", 3650)
        )

    def test_second_basis_freshness_cannot_be_weakened(self) -> None:
        self.assert_policy_rejected(
            lambda policy: policy["basis_2"].__setitem__("max_age_days", 3650)
        )

    def test_distinct_issuer_floor_cannot_be_lowered(self) -> None:
        self.assert_policy_rejected(
            lambda policy: policy["basis_2"].__setitem__("minimum_distinct_issuers", 1)
        )

    def test_distinct_repository_floor_cannot_be_lowered(self) -> None:
        self.assert_policy_rejected(
            lambda policy: policy["basis_2"].__setitem__(
                "minimum_distinct_public_repositories", 1
            )
        )

    def test_org_owner_requirement_cannot_be_removed(self) -> None:
        self.assert_policy_rejected(
            lambda policy: policy["basis_2"].__setitem__("repository_owner_type", "User")
        )

    def test_issuer_membership_requirement_cannot_be_weakened(self) -> None:
        self.assert_policy_rejected(
            lambda policy: policy["basis_2"].__setitem__(
                "issuer_author_association", ["NONE", "CONTRIBUTOR", "MEMBER", "OWNER"]
            )
        )

    def test_result_vocabulary_cannot_drop_not_established(self) -> None:
        self.assert_policy_rejected(
            lambda policy: policy["qualification"].__setitem__(
                "result_vocabulary", ["QUALIFIED", "DISQUALIFIED"]
            )
        )

    def test_authority_boundary_cannot_be_promoted(self) -> None:
        self.assert_policy_rejected(
            lambda policy: policy["authority_boundary"].__setitem__(
                "qualification_changes_execution_admission", True
            )
        )


if __name__ == "__main__":
    unittest.main()
