from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
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


def _evidence_schemas() -> dict[str, dict]:
    return {
        "dependency_schema": _load("docs/research/H11_DEPENDENCY_GRAPH_SCHEMA.json"),
        "raw_schema": _load("docs/research/H11_RAW_OBSERVATION_SCHEMA.json"),
        "semantic_schema": _load("docs/research/H11_SEMANTIC_ADJUDICATION_SCHEMA.json"),
        "reviewer_schema": _load("docs/research/H11_REVIEWER_REPRODUCER_QUALIFICATION_SCHEMA.json"),
    }


def _set_git_identity(root: Path, name: str, email: str) -> None:
    subprocess.run(["git", "-C", str(root), "config", "user.name", name], check=True)
    subprocess.run(["git", "-C", str(root), "config", "user.email", email], check=True)


def _write_json(root: Path, relative: str, value: dict, artifact_type: str) -> dict:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    path.write_text(payload, encoding="utf-8")
    subprocess.run(["git", "-C", str(root), "add", relative], check=True)
    subprocess.run(
        ["git", "-C", str(root), "commit", "-m", f"fixture: add {relative}"],
        check=True,
        capture_output=True,
    )
    git_commit = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    return {
        "path": relative,
        "sha256": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
        "artifact_type": artifact_type,
        "git_commit": git_commit,
    }


def _repository_reference(
    root: Path,
    relative: str,
    git_commit: str,
    artifact_type: str = "REPOSITORY_SOURCE",
) -> dict:
    payload = subprocess.run(
        ["git", "-C", str(root), "show", f"{git_commit}:{relative}"],
        check=True,
        capture_output=True,
    ).stdout
    return {
        "path": relative,
        "sha256": hashlib.sha256(payload).hexdigest(),
        "artifact_type": artifact_type,
        "git_commit": git_commit,
    }


def _synthetic_evidence_bundle(root: Path) -> tuple[dict, dict, dict, dict]:
    subprocess.run(
        ["git", "clone", "-q", "--shared", str(ROOT), str(root)],
        check=True,
    )
    _set_git_identity(root, "H11 Fixture", "h11-fixture@example.invalid")
    source_ref = _repository_reference(
        root,
        "docs/research/H11_PREREGISTRATION.json",
        validator.FROZEN_REVIEW_SUBJECT,
    )
    bundle_source_ref = _repository_reference(
        root,
        validator.BUNDLE_MANIFEST,
        validator.FROZEN_REVIEW_SUBJECT,
    )
    verifier_source_ref = _repository_reference(
        root,
        "tools/evidence/verify_bundle.py",
        validator.FROZEN_REVIEW_SUBJECT,
    )
    obligation_labels = {
        "H11-O01": "Laboratory evidence and profile mechanisms remain separate from Architecture authority",
        "H11-O02": "Semantic obligations can survive different realization mechanisms",
        "H11-O03": "Historical evidence identity remains reproducible without rewriting Architecture history",
        "H11-O04": "Architecture falsification remains expressible without current profile bytes",
    }
    architecture_nodes = [
        {
            "node_id": f"architecture-{obligation_id.lower()}",
            "node_class": "ARCHITECTURE_OBLIGATION",
            "obligation_id": obligation_id,
            "label": label,
            "source_reference": source_ref,
        }
        for obligation_id, label in obligation_labels.items()
    ]
    laboratory_node = {
        "node_id": "laboratory-c5-bundle",
        "node_class": "LABORATORY_EVIDENCE",
        "label": "Frozen C5 evidence bundle",
        "source_reference": bundle_source_ref,
    }
    validator_node = {
        "node_id": "validator-c5-bundle",
        "node_class": "VALIDATOR_OR_ORACLE",
        "label": "Repository C5 bundle verifier",
        "source_reference": verifier_source_ref,
    }
    profile_nodes = [
        {
            "node_id": f"mechanism-{index}",
            "node_class": "PROFILE_MECHANISM",
            "label": mechanism,
            "mechanism_name": mechanism,
            "source_reference": source_ref,
        }
        for index, mechanism in enumerate(validator.MANDATORY_MECHANISMS)
    ]
    profile_edges = [
        {
            "edge_id": f"edge-{index}",
            "from": node["node_id"],
            "to": laboratory_node["node_id"],
            "edge_class": "LAB_REPRODUCTION_REQUIRES",
            "leakage_class": "PROFILE_SPECIFIC",
            "justification": "Synthetic validator fixture edge.",
            "raw_observation_refs": [f"obs-{index}"],
        }
        for index, node in enumerate(profile_nodes)
    ]
    obligation_edges = [
        {
            "edge_id": f"edge-obligation-{index}",
            "from": laboratory_node["node_id"],
            "to": node["node_id"],
            "edge_class": "MEANING_LEVEL_JUSTIFICATION",
            "leakage_class": "MEANING_LEVEL_JUSTIFIED",
            "justification": "Synthetic frozen-obligation coverage edge.",
            "raw_observation_refs": [f"obs-obligation-{index}"],
        }
        for index, node in enumerate(architecture_nodes)
    ]
    validator_edge = {
        "edge_id": "edge-validator",
        "from": validator_node["node_id"],
        "to": laboratory_node["node_id"],
        "edge_class": "VALIDATOR_DEPENDS_ON",
        "leakage_class": "LAB_ONLY",
        "justification": "Synthetic validator-to-bundle coverage edge.",
        "raw_observation_refs": ["obs-validator"],
    }
    edges = [*profile_edges, *obligation_edges, validator_edge]

    def raw_edge_observation(edge: dict, observation_id: str) -> dict:
        return {
            "observation_id": observation_id,
            "observation_kind": "DEPENDENCY_EDGE",
            "observation_type": "REPOSITORY_INSPECTION",
            "producer_identity": "synthetic-repository-observer",
            "producer_authority_class": "REPOSITORY_OBSERVER",
            "source_reference": source_ref,
            "repository_visible": True,
            "fact": "DEPENDENCY_EDGE_OBSERVED",
            "structured_value": {
                "edge_id": edge["edge_id"],
                "from": edge["from"],
                "to": edge["to"],
                "edge_class": edge["edge_class"],
            },
        }

    raw = {
        "protocol": "nk-h11-raw-observations/1",
        "experiment_id": validator.EXPERIMENT_ID,
        "source_plan_id": validator.PLAN_ID,
        "source_plan_sha256": validator.PLAN_SHA256,
        "observation_layer": "RAW_FACTS_ONLY_NO_H11_SEMANTIC_JUDGMENT",
        "observations": [
            raw_edge_observation(edge, edge["raw_observation_refs"][0])
            for edge in edges
        ]
        + [
            {
                "observation_id": "obs-bundle-verification",
                "observation_kind": "BUNDLE_VERIFICATION",
                "observation_type": "TOOL_OUTPUT",
                "producer_identity": "synthetic-bundle-verifier",
                "producer_authority_class": "AUTOMATED_VALIDATOR",
                "source_reference": bundle_source_ref,
                "repository_visible": True,
                "fact": "BUNDLE_VERIFICATION_OBSERVED",
                "structured_value": {
                    "bundle_id": validator.BUNDLE_ID,
                    "manifest_path": validator.BUNDLE_MANIFEST,
                    "exact_bundle_verified": True,
                    "verifier_exit_code": 0,
                    "verified_artifact_count": 8,
                },
            }
        ],
        "missing_data": [],
    }
    graph = {
        "protocol": "nk-h11-dependency-graph/1",
        "experiment_id": validator.EXPERIMENT_ID,
        "source_plan_id": validator.PLAN_ID,
        "source_plan_sha256": validator.PLAN_SHA256,
        "nodes": [*architecture_nodes, laboratory_node, validator_node, *profile_nodes],
        "edges": edges,
        "mandatory_profile_mechanisms_covered": list(validator.MANDATORY_MECHANISMS),
        "declared_gaps": [],
    }
    attestation_common = {
        "protocol": validator.INDEPENDENCE_EVIDENCE_PROTOCOL,
        "experiment_id": validator.EXPERIMENT_ID,
        "source_plan_id": validator.PLAN_ID,
        "source_plan_sha256": validator.PLAN_SHA256,
        "reviewer_identity": "synthetic-independent-reviewer",
        "attested_authorship_relation": "NOT_AUTHOR_OF_PREREGISTRATION_OR_FROZEN_RUBRIC",
        "attested_custody_relation": "INDEPENDENT_FOR_DECLARED_SCOPE",
        "attested_conflicts": [],
        "attested_private_implementation_state_used": False,
        "attested_repository_visibility": "EVIDENCE_VISIBLE",
    }
    # The two core independence attestations must be committed by two distinct Git
    # author identities (both distinct from the fixture's default identity used for
    # everything else) so the validator's issuer-authentication check has genuine
    # per-basis provenance to compare, not two JSON string labels from one committer.
    _set_git_identity(root, "H11 Organizational Attester", "org-attester@example.invalid")
    organization_ref = _write_json(
        root,
        "evidence/reviewer-organization-attestation.json",
        {
            **attestation_common,
            "evidence_issuer_identity": "synthetic-organizational-attester",
            "evidence_issuer_role": "ORGANIZATIONAL_AUTHORITY",
            "basis_type": "ORGANIZATIONAL_SEPARATION",
            "statement": "The reviewer is organizationally separate for the declared H11 scope.",
        },
        "REVIEWER_EVIDENCE",
    )
    _set_git_identity(root, "H11 Independent Custodian", "independent-custodian@example.invalid")
    custody_ref = _write_json(
        root,
        "evidence/reviewer-custody-attestation.json",
        {
            **attestation_common,
            "evidence_issuer_identity": "synthetic-independent-custodian",
            "evidence_issuer_role": "INDEPENDENT_CUSTODIAN",
            "basis_type": "INDEPENDENT_EVIDENCE_CUSTODY",
            "statement": "The declared evidence custody is independent for the H11 review packet.",
        },
        "REVIEWER_EVIDENCE",
    )
    _set_git_identity(root, "H11 Fixture", "h11-fixture@example.invalid")
    reviewer = {
        "protocol": "nk-h11-reviewer-reproducer-qualification/1",
        "experiment_id": validator.EXPERIMENT_ID,
        "source_plan_id": validator.PLAN_ID,
        "source_plan_sha256": validator.PLAN_SHA256,
        "reviewer_identity_status": "ESTABLISHED",
        "reviewer_identity": "synthetic-independent-reviewer",
        "reviewer_role": "REVIEWER",
        "authorship_relation": "NOT_AUTHOR_OF_PREREGISTRATION_OR_FROZEN_RUBRIC",
        "custody_relation": "INDEPENDENT_FOR_DECLARED_SCOPE",
        "conflicts": [],
        "repository_visibility": "EVIDENCE_VISIBLE",
        "private_implementation_state_used": False,
        "independence_basis": [
            {
                "basis_type": "ORGANIZATIONAL_SEPARATION",
                "evidence_reference": organization_ref,
            },
            {
                "basis_type": "INDEPENDENT_EVIDENCE_CUSTODY",
                "evidence_reference": custody_ref,
            },
        ],
        "evidence_references": [organization_ref, custody_ref],
        "qualification_result": "QUALIFIED",
    }
    raw_ref = _write_json(root, "evidence/raw.json", raw, "RAW_OBSERVATIONS")
    graph_ref = _write_json(root, "evidence/graph.json", graph, "DEPENDENCY_GRAPH")
    reviewer_ref = _write_json(
        root,
        "evidence/reviewer.json",
        reviewer,
        "REVIEWER_QUALIFICATION",
    )
    semantic = {
        "protocol": "nk-h11-semantic-adjudication/1",
        "experiment_id": validator.EXPERIMENT_ID,
        "source_plan_id": validator.PLAN_ID,
        "source_plan_sha256": validator.PLAN_SHA256,
        "input_policy": "REPOSITORY_VISIBLE_FROZEN_INPUTS_ONLY",
        "raw_observation_record": raw_ref,
        "dependency_graph_record": graph_ref,
        "reviewer_reproducer_qualification_record": reviewer_ref,
        "adjudicator_identity": reviewer["reviewer_identity"],
        "adjudicator_role": reviewer["reviewer_role"],
        "adjudicator_authority_class": "QUALIFYING_INDEPENDENT_REVIEWER",
        "subject_private_state_used": False,
        "leakage_rubric": {
            "classes": validator.LEAKAGE_CLASSES,
            "hard_failure_class": "UNJUSTIFIED_CANON_DEPENDENCY",
            "support_threshold": validator.SUPPORT_THRESHOLD,
        },
        "hard_refutation": validator.HARD_REFUTATION,
        "mandatory_profile_leakage_count": 0,
        "unjustified_canon_dependency_count": 0,
        "independence_qualified": True,
        "outcome": "SUPPORTED_FOR_SCOPE",
        "rationale": "Synthetic validator acceptance fixture only.",
        "declared_gaps": [],
    }
    return graph, raw, reviewer, semantic


class H11ExecutionAdmissionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.admission = _load("docs/research/H11_EXECUTION_ADMISSION.json")
        self.reviewer = _load("docs/research/H11_REVIEWER_REPRODUCER_QUALIFICATION.json")
        self.dependency_schema = _load("docs/research/H11_DEPENDENCY_GRAPH_SCHEMA.json")
        self.raw_schema = _load("docs/research/H11_RAW_OBSERVATION_SCHEMA.json")
        self.semantic_schema = _load("docs/research/H11_SEMANTIC_ADJUDICATION_SCHEMA.json")
        self.reviewer_schema = _load("docs/research/H11_REVIEWER_REPRODUCER_QUALIFICATION_SCHEMA.json")
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
                "conflicts": ["SELF_REVIEW"],
                "repository_visibility": "EVIDENCE_VISIBLE",
                "independence_basis": ["SELF_ASSERTED"],
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

    def test_profile_mechanism_schema_must_require_mechanism_identity(self) -> None:
        mutated = copy.deepcopy(self.dependency_schema)
        mutated["properties"]["nodes"]["items"]["allOf"] = []
        self.assert_rejected(dependency_schema_override=mutated)

    def test_profile_mechanism_schema_condition_cannot_be_made_unreachable(self) -> None:
        mutated = copy.deepcopy(self.dependency_schema)
        mutated["properties"]["nodes"]["items"]["allOf"][0]["if"]["not"] = {}
        self.assert_rejected(dependency_schema_override=mutated)

    def test_dependency_raw_schema_must_require_exact_edge_binding(self) -> None:
        mutated = copy.deepcopy(self.raw_schema)
        mutated["properties"]["observations"]["items"]["allOf"] = []
        self.assert_rejected(raw_schema_override=mutated)

    def test_dependency_raw_schema_condition_cannot_be_made_unreachable(self) -> None:
        mutated = copy.deepcopy(self.raw_schema)
        mutated["properties"]["observations"]["items"]["allOf"][0]["if"]["not"] = {}
        self.assert_rejected(raw_schema_override=mutated)

    def test_reviewer_schema_condition_cannot_be_made_unreachable(self) -> None:
        mutated = copy.deepcopy(self.reviewer_schema)
        mutated["allOf"][0]["if"]["not"] = {}
        self.assert_rejected(reviewer_schema_override=mutated)

    def test_semantic_support_condition_cannot_be_made_unreachable(self) -> None:
        mutated = copy.deepcopy(self.semantic_schema)
        mutated["allOf"][0]["if"]["not"] = {}
        self.assert_rejected(semantic_schema_override=mutated)

    def test_schema_subset_enforces_string_patterns(self) -> None:
        commit_schema = {"type": "string", "pattern": "^[0-9a-f]{40}$"}
        self.assertTrue(validator._schema_accepts(commit_schema, "a" * 40))
        self.assertFalse(validator._schema_accepts(commit_schema, "not-a-commit"))
        self.assertFalse(
            validator._schema_accepts(
                {"type": "string", "pattern": "["},
                "invalid-regex-must-fail-closed",
            )
        )

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

    def test_qualification_cannot_be_established_via_repository_local_git_identity_switch(
        self,
    ) -> None:
        """A single process switching `git config user.email` mid-build is not independence.

        `_synthetic_evidence_bundle` builds its two core independence attestations by
        committing under two different Git identities from one process/clone (exactly
        the bypass: one actor, `user.email` flipped between commits). Distinct commit
        author identities are retained as repository-local provenance hygiene, but they
        are not proof of a distinct real-world actor, so this fully schema-valid,
        structurally self-consistent bundle must still be rejected.
        """
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            graph, raw, reviewer, semantic = _synthetic_evidence_bundle(repo)
            with self.assertRaises(validator.H11AdmissionError) as context:
                validator.validate_h11_evidence_bundle(
                    repo,
                    dependency_graph=graph,
                    raw_observations=raw,
                    semantic_adjudication=semantic,
                    reviewer_record=reviewer,
                    semantic_adjudication_path="evidence/semantic.json",
                    **_evidence_schemas(),
                )
            self.assertIn("externally authenticated", str(context.exception))

    def assert_bundle_rejected(self, mutate) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            graph, raw, reviewer, semantic = _synthetic_evidence_bundle(repo)
            mutate(repo, graph, raw, reviewer, semantic)
            with self.assertRaises(validator.H11AdmissionError):
                validator.validate_h11_evidence_bundle(
                    repo,
                    dependency_graph=graph,
                    raw_observations=raw,
                    semantic_adjudication=semantic,
                    reviewer_record=reviewer,
                    semantic_adjudication_path="evidence/semantic.json",
                    **_evidence_schemas(),
                )

    def test_supplied_records_are_validated_against_declared_schemas(self) -> None:
        def mutate(_repo, _graph, _raw, _reviewer, semantic) -> None:
            semantic["production_authorized"] = True

        self.assert_bundle_rejected(mutate)

    def test_claimed_mechanism_without_profile_node_is_rejected(self) -> None:
        def mutate(_repo, graph, _raw, _reviewer, _semantic) -> None:
            graph["nodes"] = [
                node
                for node in graph["nodes"]
                if node.get("mechanism_name") != validator.MANDATORY_MECHANISMS[0]
            ]

        self.assert_bundle_rejected(mutate)

    def test_graph_requires_each_frozen_architecture_obligation(self) -> None:
        def mutate(_repo, graph, _raw, _reviewer, _semantic) -> None:
            graph["nodes"] = [
                node for node in graph["nodes"] if node.get("obligation_id") != "H11-O04"
            ]

        self.assert_bundle_rejected(mutate)

    def test_graph_cannot_duplicate_one_obligation_to_cover_another(self) -> None:
        def mutate(_repo, graph, _raw, _reviewer, _semantic) -> None:
            node = next(
                item for item in graph["nodes"] if item.get("obligation_id") == "H11-O04"
            )
            node["obligation_id"] = "H11-O03"

        self.assert_bundle_rejected(mutate)

    def test_graph_requires_laboratory_and_validator_node_classes(self) -> None:
        def mutate(_repo, graph, _raw, _reviewer, _semantic) -> None:
            graph["nodes"] = [
                node
                for node in graph["nodes"]
                if node.get("node_class") != "VALIDATOR_OR_ORACLE"
            ]

        self.assert_bundle_rejected(mutate)

    def test_every_graph_node_must_be_connected(self) -> None:
        def mutate(_repo, graph, _raw, _reviewer, _semantic) -> None:
            graph["edges"] = [
                edge for edge in graph["edges"] if edge["edge_id"] != "edge-validator"
            ]

        self.assert_bundle_rejected(mutate)

    def test_profile_mechanism_without_dependency_edge_is_rejected(self) -> None:
        self.assert_bundle_rejected(
            lambda _repo, graph, _raw, _reviewer, _semantic: graph["edges"].pop(0)
        )

    def test_graph_reference_to_missing_raw_observation_is_rejected(self) -> None:
        def mutate(_repo, graph, _raw, _reviewer, _semantic) -> None:
            graph["edges"][0]["raw_observation_refs"] = ["obs-missing"]

        self.assert_bundle_rejected(mutate)

    def test_dependency_edge_requires_exact_raw_edge_binding(self) -> None:
        def mutate(repo, _graph, raw, _reviewer, semantic) -> None:
            raw["observations"][0]["structured_value"]["to"] = "different-node"
            semantic["raw_observation_record"] = _write_json(
                repo,
                "evidence/raw-mutated.json",
                raw,
                "RAW_OBSERVATIONS",
            )

        self.assert_bundle_rejected(mutate)

    def test_architecture_requires_profile_edge_cannot_hide_under_lab_only(self) -> None:
        def mutate(repo, graph, raw, _reviewer, semantic) -> None:
            edge = graph["edges"][0]
            edge["from"] = "architecture-h11-o01"
            edge["to"] = "mechanism-0"
            edge["edge_class"] = "ARCHITECTURE_REQUIRES"
            edge["leakage_class"] = "LAB_ONLY"
            binding = raw["observations"][0]["structured_value"]
            binding["from"] = edge["from"]
            binding["to"] = edge["to"]
            binding["edge_class"] = edge["edge_class"]
            semantic["raw_observation_record"] = _write_json(
                repo, "evidence/raw-structural-bypass.json", raw, "RAW_OBSERVATIONS"
            )
            semantic["dependency_graph_record"] = _write_json(
                repo, "evidence/graph-structural-bypass.json", graph, "DEPENDENCY_GRAPH"
            )

        self.assert_bundle_rejected(mutate)

    def test_dependency_edge_cannot_use_generic_raw_observation(self) -> None:
        def mutate(repo, _graph, raw, _reviewer, semantic) -> None:
            raw["observations"][0]["observation_kind"] = "SOURCE_REFERENCE"
            semantic["raw_observation_record"] = _write_json(
                repo,
                "evidence/raw-mutated.json",
                raw,
                "RAW_OBSERVATIONS",
            )

        self.assert_bundle_rejected(mutate)

    def test_qualified_same_custody_self_review_is_rejected(self) -> None:
        def mutate(repo, _graph, _raw, reviewer, semantic) -> None:
            reviewer["custody_relation"] = "SAME_CUSTODY"
            reviewer["conflicts"] = ["SELF_REVIEW"]
            semantic["reviewer_reproducer_qualification_record"] = _write_json(
                repo,
                "evidence/reviewer-mutated.json",
                reviewer,
                "REVIEWER_QUALIFICATION",
            )

        self.assert_bundle_rejected(mutate)

    def test_qualified_reviewer_cannot_use_ci_as_independence_basis(self) -> None:
        def mutate(repo, _graph, _raw, reviewer, semantic) -> None:
            reviewer["independence_basis"] = ["CI_SUCCESS", "AUTOMATED_VALIDATOR"]
            semantic["reviewer_reproducer_qualification_record"] = _write_json(
                repo,
                "evidence/reviewer-substitute.json",
                reviewer,
                "REVIEWER_QUALIFICATION",
            )

        self.assert_bundle_rejected(mutate)

    def test_generic_repository_json_cannot_pose_as_independence_evidence(self) -> None:
        def mutate(repo, _graph, _raw, reviewer, semantic) -> None:
            generic_ref = _repository_reference(
                repo,
                "docs/research/H11_PREREGISTRATION.json",
                validator.FROZEN_REVIEW_SUBJECT,
                "REVIEWER_EVIDENCE",
            )
            reviewer["independence_basis"][0]["evidence_reference"] = generic_ref
            reviewer["evidence_references"][0] = generic_ref
            semantic["reviewer_reproducer_qualification_record"] = _write_json(
                repo,
                "evidence/reviewer-generic-evidence.json",
                reviewer,
                "REVIEWER_QUALIFICATION",
            )

        self.assert_bundle_rejected(mutate)

    def test_independence_attestation_must_bind_reviewer_identity(self) -> None:
        def mutate(repo, _graph, _raw, reviewer, semantic) -> None:
            old_ref = reviewer["independence_basis"][0]["evidence_reference"]
            evidence = json.loads((repo / old_ref["path"]).read_text(encoding="utf-8"))
            evidence["reviewer_identity"] = "different-reviewer"
            new_ref = _write_json(
                repo,
                "evidence/reviewer-identity-mismatch.json",
                evidence,
                "REVIEWER_EVIDENCE",
            )
            reviewer["independence_basis"][0]["evidence_reference"] = new_ref
            reviewer["evidence_references"][0] = new_ref
            semantic["reviewer_reproducer_qualification_record"] = _write_json(
                repo,
                "evidence/reviewer-with-identity-mismatch.json",
                reviewer,
                "REVIEWER_QUALIFICATION",
            )

        self.assert_bundle_rejected(mutate)

    def test_core_independence_attestations_require_distinct_issuers(self) -> None:
        def mutate(repo, _graph, _raw, reviewer, semantic) -> None:
            first_ref = reviewer["independence_basis"][0]["evidence_reference"]
            second_ref = reviewer["independence_basis"][1]["evidence_reference"]
            first = json.loads((repo / first_ref["path"]).read_text(encoding="utf-8"))
            second = json.loads((repo / second_ref["path"]).read_text(encoding="utf-8"))
            second["evidence_issuer_identity"] = first["evidence_issuer_identity"]
            new_ref = _write_json(
                repo,
                "evidence/reviewer-duplicate-issuer.json",
                second,
                "REVIEWER_EVIDENCE",
            )
            reviewer["independence_basis"][1]["evidence_reference"] = new_ref
            reviewer["evidence_references"][1] = new_ref
            semantic["reviewer_reproducer_qualification_record"] = _write_json(
                repo,
                "evidence/reviewer-with-duplicate-issuer.json",
                reviewer,
                "REVIEWER_QUALIFICATION",
            )

        self.assert_bundle_rejected(mutate)

    def test_core_independence_attestations_committed_by_same_author_is_rejected(self) -> None:
        def mutate(repo, _graph, _raw, reviewer, semantic) -> None:
            _set_git_identity(repo, "Single Fixture Process", "single-process@example.invalid")
            first_ref = reviewer["independence_basis"][0]["evidence_reference"]
            second_ref = reviewer["independence_basis"][1]["evidence_reference"]
            first = json.loads((repo / first_ref["path"]).read_text(encoding="utf-8"))
            second = json.loads((repo / second_ref["path"]).read_text(encoding="utf-8"))
            new_first_ref = _write_json(
                repo, "evidence/reviewer-org-same-author.json", first, "REVIEWER_EVIDENCE"
            )
            new_second_ref = _write_json(
                repo, "evidence/reviewer-custody-same-author.json", second, "REVIEWER_EVIDENCE"
            )
            reviewer["independence_basis"][0]["evidence_reference"] = new_first_ref
            reviewer["independence_basis"][1]["evidence_reference"] = new_second_ref
            reviewer["evidence_references"] = [new_first_ref, new_second_ref]
            semantic["reviewer_reproducer_qualification_record"] = _write_json(
                repo,
                "evidence/reviewer-with-same-author-bases.json",
                reviewer,
                "REVIEWER_QUALIFICATION",
            )

        self.assert_bundle_rejected(mutate)

    def test_independence_evidence_authored_by_subject_is_rejected(self) -> None:
        def mutate(repo, _graph, _raw, reviewer, semantic) -> None:
            subject_email = subprocess.run(
                ["git", "-C", str(repo), "log", "-1", "--format=%ae", validator.PLAN_MERGE],
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
            _set_git_identity(repo, "Subject Self-Certifier", subject_email)
            first_ref = reviewer["independence_basis"][0]["evidence_reference"]
            first = json.loads((repo / first_ref["path"]).read_text(encoding="utf-8"))
            new_ref = _write_json(
                repo, "evidence/reviewer-org-subject-authored.json", first, "REVIEWER_EVIDENCE"
            )
            reviewer["independence_basis"][0]["evidence_reference"] = new_ref
            reviewer["evidence_references"][0] = new_ref
            semantic["reviewer_reproducer_qualification_record"] = _write_json(
                repo,
                "evidence/reviewer-with-subject-authored-basis.json",
                reviewer,
                "REVIEWER_QUALIFICATION",
            )

        self.assert_bundle_rejected(mutate)

    def test_evidence_bundle_cannot_report_not_tested_outcome(self) -> None:
        def mutate(repo, _graph, _raw, _reviewer, semantic) -> None:
            semantic["outcome"] = "NOT_TESTED"
            semantic["rationale"] = "Attempt to record a qualified adjudication as untested."

        self.assert_bundle_rejected(mutate)

    def test_supported_outcome_without_qualified_independence_is_rejected(self) -> None:
        def mutate(repo, _graph, _raw, reviewer, semantic) -> None:
            reviewer["qualification_result"] = "NOT_ESTABLISHED"
            reviewer["custody_relation"] = "SHARED_CUSTODY_DISCLOSED"
            reviewer["conflicts"] = ["SELF_REVIEW_RISK"]
            semantic["independence_qualified"] = False
            semantic["reviewer_reproducer_qualification_record"] = _write_json(
                repo,
                "evidence/reviewer-mutated.json",
                reviewer,
                "REVIEWER_QUALIFICATION",
            )

        self.assert_bundle_rejected(mutate)

    def test_supported_outcome_with_unjustified_dependency_is_rejected(self) -> None:
        def mutate(repo, graph, _raw, _reviewer, semantic) -> None:
            graph["edges"][0]["leakage_class"] = "UNJUSTIFIED_CANON_DEPENDENCY"
            semantic["mandatory_profile_leakage_count"] = 1
            semantic["unjustified_canon_dependency_count"] = 1
            semantic["dependency_graph_record"] = _write_json(
                repo,
                "evidence/graph-mutated.json",
                graph,
                "DEPENDENCY_GRAPH",
            )

        self.assert_bundle_rejected(mutate)

    def test_hard_failure_edge_forces_refuted_outcome(self) -> None:
        def mutate(repo, graph, _raw, _reviewer, semantic) -> None:
            graph["edges"][0]["leakage_class"] = "UNJUSTIFIED_CANON_DEPENDENCY"
            semantic["mandatory_profile_leakage_count"] = 1
            semantic["unjustified_canon_dependency_count"] = 1
            semantic["outcome"] = "WEAKENED"
            semantic["dependency_graph_record"] = _write_json(
                repo,
                "evidence/graph-hard-failure-weakened.json",
                graph,
                "DEPENDENCY_GRAPH",
            )

        self.assert_bundle_rejected(mutate)

    def test_refuted_outcome_requires_hard_failure_edge(self) -> None:
        self.assert_bundle_rejected(
            lambda _repo, _graph, _raw, _reviewer, semantic: semantic.__setitem__(
                "outcome", "REFUTED"
            )
        )

    def test_semantic_adjudicator_must_match_qualified_reviewer(self) -> None:
        self.assert_bundle_rejected(
            lambda _repo, _graph, _raw, _reviewer, semantic: semantic.__setitem__(
                "adjudicator_identity", "different-reviewer"
            )
        )

    def test_semantic_input_artifacts_must_be_distinct(self) -> None:
        def mutate(_repo, _graph, _raw, _reviewer, semantic) -> None:
            semantic["raw_observation_record"] = copy.deepcopy(
                semantic["dependency_graph_record"]
            )
            semantic["raw_observation_record"]["artifact_type"] = "RAW_OBSERVATIONS"

        self.assert_bundle_rejected(mutate)

    def test_semantic_input_digest_mismatch_is_rejected(self) -> None:
        def mutate(_repo, _graph, _raw, _reviewer, semantic) -> None:
            semantic["raw_observation_record"]["sha256"] = "0" * 64

        self.assert_bundle_rejected(mutate)

    def test_semantic_input_must_be_committed_and_head_anchored(self) -> None:
        def mutate(repo, _graph, raw, _reviewer, semantic) -> None:
            path = repo / "evidence/untracked-raw.json"
            payload = json.dumps(raw, sort_keys=True).encode("utf-8")
            path.write_bytes(payload)
            semantic["raw_observation_record"] = {
                "path": "evidence/untracked-raw.json",
                "sha256": hashlib.sha256(payload).hexdigest(),
                "artifact_type": "RAW_OBSERVATIONS",
                "git_commit": subprocess.run(
                    ["git", "-C", str(repo), "rev-parse", "HEAD"],
                    check=True,
                    capture_output=True,
                    text=True,
                ).stdout.strip(),
            }

        self.assert_bundle_rejected(mutate)

    def test_non_repository_visible_raw_observation_is_rejected(self) -> None:
        def mutate(repo, _graph, raw, _reviewer, semantic) -> None:
            raw["observations"][0]["repository_visible"] = False
            semantic["raw_observation_record"] = _write_json(
                repo,
                "evidence/raw-mutated.json",
                raw,
                "RAW_OBSERVATIONS",
            )

        self.assert_bundle_rejected(mutate)

    def test_raw_semantic_self_report_in_fact_is_rejected(self) -> None:
        def mutate(repo, _graph, raw, _reviewer, semantic) -> None:
            raw["observations"][0]["fact"] = "outcome SUPPORTED_FOR_SCOPE"
            semantic["raw_observation_record"] = _write_json(
                repo,
                "evidence/raw-mutated.json",
                raw,
                "RAW_OBSERVATIONS",
            )

        self.assert_bundle_rejected(mutate)

    def test_raw_semantic_paraphrase_in_fact_is_rejected(self) -> None:
        def mutate(repo, _graph, raw, _reviewer, semantic) -> None:
            raw["observations"][0]["fact"] = "This dependency appears acceptable for scoped support"
            semantic["raw_observation_record"] = _write_json(
                repo,
                "evidence/raw-paraphrase.json",
                raw,
                "RAW_OBSERVATIONS",
            )

        self.assert_bundle_rejected(mutate)

    def test_supported_outcome_requires_exact_bundle_verification(self) -> None:
        def mutate(repo, _graph, raw, _reviewer, semantic) -> None:
            raw["observations"] = [
                observation
                for observation in raw["observations"]
                if observation["observation_kind"] != "BUNDLE_VERIFICATION"
            ]
            semantic["raw_observation_record"] = _write_json(
                repo, "evidence/raw-no-bundle.json", raw, "RAW_OBSERVATIONS"
            )

        self.assert_bundle_rejected(mutate)

    def test_bundle_observation_count_must_match_actual_verifier(self) -> None:
        def mutate(repo, _graph, raw, _reviewer, semantic) -> None:
            bundle = next(
                observation
                for observation in raw["observations"]
                if observation["observation_kind"] == "BUNDLE_VERIFICATION"
            )
            bundle["structured_value"]["verified_artifact_count"] = 9
            semantic["raw_observation_record"] = _write_json(
                repo,
                "evidence/raw-false-bundle-count.json",
                raw,
                "RAW_OBSERVATIONS",
            )

        self.assert_bundle_rejected(mutate)

    def test_bundle_observation_cannot_hide_actual_artifact_corruption(self) -> None:
        def mutate(repo, _graph, _raw, _reviewer, _semantic) -> None:
            manifest = json.loads((repo / validator.BUNDLE_MANIFEST).read_text(encoding="utf-8"))
            artifact_path = manifest["checkpoints"][0]["artifacts"][0]["path"]
            (repo / artifact_path).write_bytes(b"corrupt fixture artifact")

        self.assert_bundle_rejected(mutate)

    def test_tampered_worktree_verifier_cannot_rescue_corrupted_bundle(self) -> None:
        def mutate(repo, _graph, _raw, _reviewer, _semantic) -> None:
            manifest = json.loads((repo / validator.BUNDLE_MANIFEST).read_text(encoding="utf-8"))
            artifact_path = manifest["checkpoints"][0]["artifacts"][0]["path"]
            (repo / artifact_path).write_bytes(b"corrupt fixture artifact")
            verifier_path = repo / "tools/evidence/verify_bundle.py"
            verifier_path.write_text("raise SystemExit(0)\n", encoding="utf-8")

        self.assert_bundle_rejected(mutate)

    def test_historical_graph_source_cannot_postdate_frozen_subject(self) -> None:
        def mutate(repo, graph, _raw, _reviewer, semantic) -> None:
            late_ref = semantic["raw_observation_record"].copy()
            late_ref["artifact_type"] = "REPOSITORY_SOURCE"
            graph["nodes"][0]["source_reference"] = late_ref
            semantic["dependency_graph_record"] = _write_json(
                repo,
                "evidence/graph-with-late-source.json",
                graph,
                "DEPENDENCY_GRAPH",
            )

        self.assert_bundle_rejected(mutate)

    def test_supported_outcome_rejects_any_declared_gap(self) -> None:
        def mutate(repo, graph, _raw, _reviewer, semantic) -> None:
            graph["declared_gaps"] = ["missing dependency evidence"]
            semantic["dependency_graph_record"] = _write_json(
                repo, "evidence/graph-with-gap.json", graph, "DEPENDENCY_GRAPH"
            )

        self.assert_bundle_rejected(mutate)

    def test_supported_outcome_rejects_raw_missing_data(self) -> None:
        def mutate(repo, _graph, raw, _reviewer, semantic) -> None:
            raw["missing_data"] = [
                {
                    "missing_id": "missing-1",
                    "description": "synthetic missing evidence",
                    "effect_on_visibility": "MATERIAL",
                }
            ]
            semantic["raw_observation_record"] = _write_json(
                repo, "evidence/raw-with-gap.json", raw, "RAW_OBSERVATIONS"
            )

        self.assert_bundle_rejected(mutate)

    def test_supported_outcome_rejects_adjudication_gap(self) -> None:
        self.assert_bundle_rejected(
            lambda _repo, _graph, _raw, _reviewer, semantic: semantic.__setitem__(
                "declared_gaps", ["unresolved semantic evidence"]
            )
        )

    def test_raw_semantic_self_report_in_structured_value_is_rejected(self) -> None:
        def mutate(repo, _graph, raw, _reviewer, semantic) -> None:
            raw["observations"][0]["structured_value"] = {
                "qualification_result": "QUALIFIED"
            }
            semantic["raw_observation_record"] = _write_json(
                repo,
                "evidence/raw-mutated.json",
                raw,
                "RAW_OBSERVATIONS",
            )

        self.assert_bundle_rejected(mutate)

    def test_raw_observation_without_producer_identity_is_rejected(self) -> None:
        def mutate(repo, _graph, raw, _reviewer, semantic) -> None:
            raw["observations"][0]["producer_identity"] = ""
            semantic["raw_observation_record"] = _write_json(
                repo,
                "evidence/raw-mutated.json",
                raw,
                "RAW_OBSERVATIONS",
            )

        self.assert_bundle_rejected(mutate)

    def test_exact_json_comparison_distinguishes_boolean_from_integer(self) -> None:
        self.assertFalse(validator._json_exact_equal({"value": True}, {"value": 1}))
        self.assertFalse(validator._json_exact_equal([0], [False]))
        self.assertFalse(validator._schema_accepts({"const": True}, 1))
        self.assertFalse(validator._schema_accepts({"enum": [False]}, 0))


if __name__ == "__main__":
    unittest.main()
