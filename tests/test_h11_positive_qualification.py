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
    "h11_evaluate_positive_qualification",
    ROOT / "tools" / "ai_context" / "evaluate_h11_positive_qualification.py",
)


def _load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


CANDIDATE_URL = (
    "https://api.github.com/repos/velantrian/velantrim-native-kernel/"
    "pulls/131/reviews/1001"
)
ORG_URL = "https://api.github.com/repos/org-one/h11-attestations/issues/comments/2001"
CUSTODY_URL = "https://api.github.com/repos/org-two/h11-custody/pulls/7/reviews/3001"
ORG_REPO_URL = "https://api.github.com/repos/org-one/h11-attestations"
CUSTODY_REPO_URL = "https://api.github.com/repos/org-two/h11-custody"
ORG_META_URL = "https://api.github.com/orgs/org-one"
CUSTODY_META_URL = "https://api.github.com/orgs/org-two"


def _declaration(**overrides) -> dict:
    value = {
        "protocol": evaluator.DECLARATION_PROTOCOL,
        "experiment_id": evaluator.EXPERIMENT_ID,
        "source_plan_id": evaluator.PLAN_ID,
        "source_plan_sha256": evaluator.PLAN_SHA256,
        "reviewer_login": "external-reviewer",
        "known_aliases": [],
        "reviewer_role": "REVIEWER",
        "authorship_relation": "NOT_AUTHOR_OF_PREREGISTRATION_OR_FROZEN_RUBRIC",
        "custody_relation": "INDEPENDENT_FOR_DECLARED_SCOPE",
        "conflicts": [],
        "material_dependence": [],
        "repository_visible_frozen_inputs_only": True,
        "private_implementation_state_used": False,
        "statement": "I declare my H11 review-role relationship for the frozen inputs.",
    }
    value.update(overrides)
    return value


def _attestation(basis_type: str, **overrides) -> dict:
    value = {
        "protocol": evaluator.ATTESTATION_PROTOCOL,
        "experiment_id": evaluator.EXPERIMENT_ID,
        "source_plan_id": evaluator.PLAN_ID,
        "source_plan_sha256": evaluator.PLAN_SHA256,
        "reviewer_login": "external-reviewer",
        "basis_type": basis_type,
        "issuer_role": evaluator.BASIS_ROLES[basis_type],
        "attested_known_aliases": [],
        "attested_authorship_relation": "NOT_AUTHOR_OF_PREREGISTRATION_OR_FROZEN_RUBRIC",
        "attested_custody_relation": "INDEPENDENT_FOR_DECLARED_SCOPE",
        "attested_conflicts": [],
        "attested_material_dependence": [],
        "attested_repository_visible_frozen_inputs_only": True,
        "attested_private_implementation_state_used": False,
        "statement": "Independent H11 role attestation for the frozen plan.",
    }
    value.update(overrides)
    return value


def _request(**overrides) -> dict:
    value = {
        "protocol": evaluator.REQUEST_PROTOCOL,
        "experiment_id": evaluator.EXPERIMENT_ID,
        "source_plan_id": evaluator.PLAN_ID,
        "source_plan_sha256": evaluator.PLAN_SHA256,
        "evaluated_at": "2026-08-23T00:00:00Z",
        "candidate_review_api_url": CANDIDATE_URL,
        "second_basis_api_urls": [ORG_URL, CUSTODY_URL],
    }
    value.update(overrides)
    return value


def _bundle() -> dict[str, dict]:
    return {
        CANDIDATE_URL: {
            "url": CANDIDATE_URL,
            "id": 1001,
            "pull_request_url": (
                "https://api.github.com/repos/velantrian/velantrim-native-kernel/pulls/131"
            ),
            "state": "COMMENTED",
            "submitted_at": "2026-08-22T23:00:00Z",
            "user": {"login": "external-reviewer", "id": 5001},
            "body": json.dumps(_declaration()),
        },
        ORG_REPO_URL: {
            "full_name": "org-one/h11-attestations",
            "private": False,
            "owner": {"login": "org-one", "id": 7001, "type": "Organization"},
        },
        CUSTODY_REPO_URL: {
            "full_name": "org-two/h11-custody",
            "private": False,
            "owner": {"login": "org-two", "id": 7002, "type": "Organization"},
        },
        ORG_META_URL: {"login": "org-one", "id": 7001, "is_verified": True},
        CUSTODY_META_URL: {"login": "org-two", "id": 7002, "is_verified": True},
        ORG_URL: {
            "url": ORG_URL,
            "id": 2001,
            "issue_url": "https://api.github.com/repos/org-one/h11-attestations/issues/1",
            "created_at": "2026-08-22T22:00:00Z",
            "author_association": "MEMBER",
            "user": {"login": "org-authority", "id": 6001},
            "body": json.dumps(_attestation("ORGANIZATIONAL_SEPARATION")),
        },
        CUSTODY_URL: {
            "url": CUSTODY_URL,
            "id": 3001,
            "pull_request_url": "https://api.github.com/repos/org-two/h11-custody/pulls/7",
            "submitted_at": "2026-08-22T21:00:00Z",
            "author_association": "MEMBER",
            "user": {"login": "custodian", "id": 6002},
            "body": json.dumps(_attestation("INDEPENDENT_EVIDENCE_CUSTODY")),
        },
    }


class H11PositiveQualificationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.policy = _load("docs/research/H11_POSITIVE_QUALIFICATION_POLICY.json")

    def evaluate(self, bundle=None, request=None, policy=None):
        values = bundle or _bundle()
        return evaluator.evaluate(
            request or _request(),
            policy=policy or self.policy,
            fetch_json=lambda url: values[url],
        )

    def test_two_live_external_bases_can_reach_qualified_but_no_authority(self) -> None:
        result = self.evaluate()
        self.assertEqual(result["qualification_result"], "QUALIFIED")
        self.assertTrue(result["basis_1_verified"])
        self.assertTrue(result["basis_2_verified"])
        self.assertIn("ALIASES_DISCLOSED", result["reasons"])
        self.assertIn("NO_MATERIAL_DEPENDENCE", result["reasons"])
        self.assertTrue(result["stop_required_if_qualified"])
        self.assertEqual(
            result["next_action"],
            "SEPARATE_A10_H11_EXECUTION_ADMISSION_REASSESSMENT",
        )
        for key in (
            "execution_admission_changed",
            "h11_execution_authorized",
            "dependency_graph_execution_authorized",
            "semantic_adjudication_authorized",
            "runtime_thaw_authorized",
            "final_canon_authorized",
            "production_authorized",
        ):
            self.assertFalse(result[key], key)

    def test_repository_owner_candidate_is_disqualified(self) -> None:
        bundle = _bundle()
        bundle[CANDIDATE_URL]["user"] = {
            "login": "velantrian",
            "id": evaluator.REPOSITORY_OWNER_ID,
        }
        bundle[CANDIDATE_URL]["body"] = json.dumps(_declaration(reviewer_login="velantrian"))
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "DISQUALIFIED")
        self.assertEqual(result["reasons"], ["OWNER_OR_SELF_REVIEW"])

    def test_repository_owner_alias_is_disqualified(self) -> None:
        bundle = _bundle()
        bundle[CANDIDATE_URL]["body"] = json.dumps(_declaration(known_aliases=["velantrian"]))
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "DISQUALIFIED")
        self.assertEqual(result["reasons"], ["OWNER_ALIAS_DISCLOSED"])

    def test_frozen_plan_author_is_disqualified(self) -> None:
        bundle = _bundle()
        bundle[CANDIDATE_URL]["body"] = json.dumps(_declaration(authorship_relation="AUTHOR_OF_PREREGISTRATION"))
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "DISQUALIFIED")
        self.assertEqual(result["reasons"], ["AUTHOR_OF_PREREGISTRATION_OR_FROZEN_RUBRIC"])

    def test_same_custody_is_disqualified(self) -> None:
        bundle = _bundle()
        bundle[CANDIDATE_URL]["body"] = json.dumps(_declaration(custody_relation="SAME_CUSTODY"))
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "DISQUALIFIED")
        self.assertEqual(result["reasons"], ["SAME_CUSTODY"])

    def test_private_implementation_state_is_disqualified(self) -> None:
        bundle = _bundle()
        bundle[CANDIDATE_URL]["body"] = json.dumps(_declaration(private_implementation_state_used=True))
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "DISQUALIFIED")
        self.assertEqual(result["reasons"], ["PRIVATE_IMPLEMENTATION_STATE_USED"])

    def test_frozen_input_violation_is_disqualified(self) -> None:
        bundle = _bundle()
        bundle[CANDIDATE_URL]["body"] = json.dumps(_declaration(repository_visible_frozen_inputs_only=False))
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "DISQUALIFIED")
        self.assertEqual(result["reasons"], ["FROZEN_INPUT_BOUNDARY_VIOLATED"])

    def test_unresolved_conflict_remains_not_established(self) -> None:
        bundle = _bundle()
        bundle[CANDIDATE_URL]["body"] = json.dumps(_declaration(conflicts=["DISCLOSED_CONFLICT"]))
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "NOT_ESTABLISHED")
        self.assertEqual(result["reasons"], ["UNRESOLVED_CONFLICTS"])

    def test_material_dependence_remains_not_established(self) -> None:
        bundle = _bundle()
        bundle[CANDIDATE_URL]["body"] = json.dumps(_declaration(material_dependence=["SHARED_EMPLOYER_DEPENDENCE"]))
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "NOT_ESTABLISHED")
        self.assertEqual(result["reasons"], ["MATERIAL_DEPENDENCE"])

    def test_stale_candidate_review_remains_not_established(self) -> None:
        bundle = _bundle()
        bundle[CANDIDATE_URL]["submitted_at"] = "2026-01-01T00:00:00Z"
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "NOT_ESTABLISHED")
        self.assertEqual(result["reasons"], ["STALE_EVIDENCE"])

    def test_api_event_id_must_match_url(self) -> None:
        bundle = _bundle()
        bundle[ORG_URL]["id"] = 9999
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "NOT_ESTABLISHED")
        self.assertEqual(result["reasons"], ["UNVERIFIABLE_EVIDENCE"])

    def test_second_basis_repository_must_be_public(self) -> None:
        bundle = _bundle()
        bundle[ORG_REPO_URL]["private"] = True
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "NOT_ESTABLISHED")
        self.assertEqual(result["reasons"], ["UNVERIFIABLE_EVIDENCE"])

    def test_second_basis_repository_must_be_organization_owned(self) -> None:
        bundle = _bundle()
        bundle[ORG_REPO_URL]["owner"]["type"] = "User"
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "NOT_ESTABLISHED")
        self.assertEqual(result["reasons"], ["UNVERIFIABLE_EVIDENCE"])

    def test_second_basis_organization_must_be_github_verified(self) -> None:
        bundle = _bundle()
        bundle[ORG_META_URL]["is_verified"] = False
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "NOT_ESTABLISHED")
        self.assertEqual(result["reasons"], ["UNVERIFIABLE_EVIDENCE"])

    def test_second_basis_issuer_must_have_repository_association(self) -> None:
        bundle = _bundle()
        bundle[ORG_URL]["author_association"] = "NONE"
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "NOT_ESTABLISHED")
        self.assertEqual(result["reasons"], ["UNVERIFIABLE_EVIDENCE"])

    def test_disclosed_alias_cannot_issue_second_basis(self) -> None:
        bundle = _bundle()
        aliases = ["org-authority"]
        bundle[CANDIDATE_URL]["body"] = json.dumps(_declaration(known_aliases=aliases))
        bundle[ORG_URL]["body"] = json.dumps(_attestation("ORGANIZATIONAL_SEPARATION", attested_known_aliases=aliases))
        bundle[CUSTODY_URL]["body"] = json.dumps(_attestation("INDEPENDENT_EVIDENCE_CUSTODY", attested_known_aliases=aliases))
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "NOT_ESTABLISHED")
        self.assertEqual(result["reasons"], ["UNVERIFIABLE_EVIDENCE"])

    def test_second_basis_issuers_must_be_distinct(self) -> None:
        bundle = _bundle()
        bundle[CUSTODY_URL]["user"] = {"login": "org-authority", "id": 6001}
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "NOT_ESTABLISHED")
        self.assertEqual(result["reasons"], ["NON_DISTINCT_ISSUERS"])

    def test_second_basis_repositories_must_be_distinct(self) -> None:
        second_url = "https://api.github.com/repos/org-one/h11-attestations/pulls/7/reviews/3001"
        bundle = _bundle()
        bundle[second_url] = copy.deepcopy(bundle[CUSTODY_URL])
        bundle[second_url]["url"] = second_url
        bundle[second_url]["pull_request_url"] = "https://api.github.com/repos/org-one/h11-attestations/pulls/7"
        request = _request(second_basis_api_urls=[ORG_URL, second_url])
        result = self.evaluate(bundle=bundle, request=request)
        self.assertEqual(result["qualification_result"], "NOT_ESTABLISHED")
        self.assertEqual(result["reasons"], ["NON_DISTINCT_EVIDENCE_REPOSITORIES"])

    def test_contradictory_attestation_remains_not_established(self) -> None:
        bundle = _bundle()
        bundle[ORG_URL]["body"] = json.dumps(_attestation("ORGANIZATIONAL_SEPARATION", attested_custody_relation="UNKNOWN"))
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "NOT_ESTABLISHED")
        self.assertEqual(result["reasons"], ["CONTRADICTORY_ATTESTATIONS"])

    def test_contradictory_alias_attestation_remains_not_established(self) -> None:
        bundle = _bundle()
        bundle[ORG_URL]["body"] = json.dumps(_attestation("ORGANIZATIONAL_SEPARATION", attested_known_aliases=["other-alias"]))
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "NOT_ESTABLISHED")
        self.assertEqual(result["reasons"], ["CONTRADICTORY_ATTESTATIONS"])

    def test_missing_second_basis_remains_not_established(self) -> None:
        request = _request(second_basis_api_urls=[ORG_URL])
        result = self.evaluate(request=request)
        self.assertEqual(result["qualification_result"], "NOT_ESTABLISHED")
        self.assertEqual(result["reasons"], ["MISSING_EVIDENCE"])

    def test_malformed_candidate_body_remains_not_established(self) -> None:
        bundle = _bundle()
        bundle[CANDIDATE_URL]["body"] = "not-json"
        result = self.evaluate(bundle=bundle)
        self.assertEqual(result["qualification_result"], "NOT_ESTABLISHED")
        self.assertEqual(result["reasons"], ["MALFORMED_EVIDENCE"])

    def test_policy_cannot_grant_h11_execution(self) -> None:
        policy = copy.deepcopy(self.policy)
        policy["authority_boundary"]["qualification_authorizes_h11_execution"] = True
        result = self.evaluate(policy=policy)
        self.assertEqual(result["qualification_result"], "NOT_ESTABLISHED")
        self.assertEqual(result["reasons"], ["MALFORMED_EVIDENCE"])


if __name__ == "__main__":
    unittest.main()
