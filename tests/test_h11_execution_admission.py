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


def _synthetic_evidence_bundle(root: Path) -> tuple[dict, dict, dict, dict]:
    subprocess.run(["git", "init", "-q", str(root)], check=True)
    subprocess.run(["git", "-C", str(root), "config", "user.name", "H11 Fixture"], check=True)
    subprocess.run(["git", "-C", str(root), "config", "user.email", "h11-fixture@example.invalid"], check=True)
    source = root / "evidence/source.txt"
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_text("repository-visible synthetic H11 validator fixture\n", encoding="utf-8")
    subprocess.run(["git", "-C", str(root), "add", "evidence/source.txt"], check=True)
    subprocess.run(
        ["git", "-C", str(root), "commit", "-m", "fixture: add repository source"],
        check=True,
        capture_output=True,
    )
    source_commit = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    source_ref = {
        "path": "evidence/source.txt",
        "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "artifact_type": "REPOSITORY_SOURCE",
        "git_commit": source_commit,
    }
    architecture_node = {
        "node_id": "architecture-boundary",
        "node_class": "ARCHITECTURE_OBLIGATION",
        "label": "Laboratory reproducibility remains separate from Architecture Canon",
        "source_reference": source_ref,
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
    edges = [
        {
            "edge_id": f"edge-{index}",
            "from": node["node_id"],
            "to": architecture_node["node_id"],
            "edge_class": "PROFILE_REALIZES",
            "leakage_class": "MEANING_LEVEL_JUSTIFIED",
            "justification": "Synthetic validator fixture edge.",
            "raw_observation_refs": [f"obs-{index}"],
        }
        for index, node in enumerate(profile_nodes)
    ]
    raw = {
        "protocol": "nk-h11-raw-observations/1",
        "experiment_id": validator.EXPERIMENT_ID,
        "source_plan_id": validator.PLAN_ID,
        "source_plan_sha256": validator.PLAN_SHA256,
        "observation_layer": "RAW_FACTS_ONLY_NO_H11_SEMANTIC_JUDGMENT",
        "observations": [
            {
                "observation_id": f"obs-{index}",
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
            for index, edge in enumerate(edges)
        ]
        + [
            {
                "observation_id": "obs-bundle-verification",
                "observation_kind": "BUNDLE_VERIFICATION",
                "observation_type": "TOOL_OUTPUT",
                "producer_identity": "synthetic-bundle-verifier",
                "producer_authority_class": "AUTOMATED_VALIDATOR",
                "source_reference": source_ref,
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
        "nodes": [architecture_node, *profile_nodes],
        "edges": edges,
        "mandatory_profile_mechanisms_covered": list(validator.MANDATORY_MECHANISMS),
        "declared_gaps": [],
    }
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
                "evidence_reference": {
                    **source_ref,
                    "artifact_type": "REVIEWER_EVIDENCE",
                },
            },
            {
                "basis_type": "INDEPENDENT_EVIDENCE_CUSTODY",
                "evidence_reference": {
                    **source_ref,
                    "artifact_type": "REVIEWER_EVIDENCE",
                },
            },
        ],
        "evidence_references": [
            {
                **source_ref,
                "artifact_type": "REVIEWER_EVIDENCE",
            }
        ],
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

    def test_synthetic_hardened_evidence_chain_is_accepted_by_validator_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            graph, raw, reviewer, semantic = _synthetic_evidence_bundle(repo)
            validator.validate_h11_evidence_bundle(
                repo,
                dependency_graph=graph,
                raw_observations=raw,
                semantic_adjudication=semantic,
                reviewer_record=reviewer,
                semantic_adjudication_path="evidence/semantic.json",
                **_evidence_schemas(),
            )

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
        self.assert_bundle_rejected(
            lambda _repo, graph, _raw, _reviewer, _semantic: graph["nodes"].pop(1)
        )

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
            edge["from"] = "architecture-boundary"
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


if __name__ == "__main__":
    unittest.main()
