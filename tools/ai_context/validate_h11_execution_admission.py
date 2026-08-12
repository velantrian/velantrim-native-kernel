#!/usr/bin/env python3
"""Validate the blocked A10-H11 execution-admission package fail closed."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Mapping

PLAN_PATH = Path("docs/research/H11_PREREGISTRATION.json")
PLAN_ID = "H11-001-c5-lab-canon-separation-v1"
PLAN_PROTOCOL = "nk-h11-preregistration/1"
PLAN_MERGE = "4a75ff15542013c033030620bdff61997e365140"
PLAN_SHA256 = "60da649e675b79b3e70bf8a61cf03cb4d57bb989f4934b65ab8d50c925b19914"
CURRENT_GATE_SOURCE_SHA = "82f5965bca9c44919f8f0c22d5b0862e803ff696"
TARGET = "A10-H11"
EXPERIMENT_ID = "H11-001"
BUNDLE_ID = "native-kernel/c5/2026-08-08-adr0023"
BUNDLE_MANIFEST = "evidence/c5/2026-08-08-adr0023/manifest.json"
BLOCKER = "BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER"

ADMISSION_PATH = Path("docs/research/H11_EXECUTION_ADMISSION.json")
DEPENDENCY_SCHEMA_PATH = Path("docs/research/H11_DEPENDENCY_GRAPH_SCHEMA.json")
RAW_SCHEMA_PATH = Path("docs/research/H11_RAW_OBSERVATION_SCHEMA.json")
SEMANTIC_SCHEMA_PATH = Path("docs/research/H11_SEMANTIC_ADJUDICATION_SCHEMA.json")
REVIEWER_SCHEMA_PATH = Path("docs/research/H11_REVIEWER_REPRODUCER_QUALIFICATION_SCHEMA.json")
REVIEWER_RECORD_PATH = Path("docs/research/H11_REVIEWER_REPRODUCER_QUALIFICATION.json")

NODE_CLASSES = [
    "ARCHITECTURE_OBLIGATION",
    "LABORATORY_EVIDENCE",
    "PROFILE_MECHANISM",
    "VALIDATOR_OR_ORACLE",
]
EDGE_CLASSES = [
    "MEANING_LEVEL_JUSTIFICATION",
    "LAB_REPRODUCTION_REQUIRES",
    "PROFILE_REALIZES",
    "ARCHITECTURE_REQUIRES",
    "VALIDATOR_DEPENDS_ON",
]
LEAKAGE_CLASSES = [
    "LAB_ONLY",
    "PROFILE_SPECIFIC",
    "MEANING_LEVEL_JUSTIFIED",
    "UNJUSTIFIED_CANON_DEPENDENCY",
]
A10_OUTCOMES = [
    "SUPPORTED_FOR_SCOPE",
    "WEAKENED",
    "REFUTED",
    "INDETERMINATE",
    "NOT_TESTED",
]
RAW_OBSERVATION_KINDS = [
    "BUNDLE_VERIFICATION",
    "MANIFEST_IDENTITY",
    "ARTIFACT_INVENTORY",
    "DEPENDENCY_EDGE",
    "SOURCE_REFERENCE",
    "MECHANISM_CLASSIFICATION_INPUT",
    "REVIEWER_IDENTITY_EVIDENCE",
    "INDEPENDENCE_EVIDENCE",
    "MISSING_DATA",
]
MANDATORY_MECHANISMS = [
    "Python 3.11/3.12",
    "PostgreSQL 16/18",
    "SQLite 3.51.3",
    "SQL schema/transactions/locking",
    "JSON serialization",
    "ZIP archive representation",
    "SHA-256 digest verification",
    "current Event vocabulary/envelope",
    "reducer v1",
    "Receipt encoding",
    "integer sequence/order mechanisms",
    "current P4/P5/C3/C4/C5 report schemas",
]
NON_QUALIFYING_SUBSTITUTES = [
    "SELF_REVIEW",
    "REPOSITORY_OWNER_REVIEW",
    "CI_SUCCESS",
    "CODEX_BOT_NOTICE",
    "AUTOMATED_VALIDATOR",
    "LLM_SELF_CRITIQUE",
    "SAME_AGENT_RENAMED",
]
SUPPORT_THRESHOLD = (
    "mandatory_profile_leakage_count == 0 and all Architecture obligations remain "
    "testable/falsifiable without current profile bytes as mandatory semantic-oracle input."
)
HARD_REFUTATION = (
    "Within this preregistered scope, a necessary accepted Architecture obligation cannot remain "
    "reproducible/testable unless a profile-specific C5 laboratory mechanism is elevated into "
    "universal Architecture solely because historical C5 evidence reproduction depends on that mechanism."
)


class H11AdmissionError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise H11AdmissionError(message)


def _load(path: Path, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise H11AdmissionError(f"cannot read {label}: {exc}") from exc
    _require(isinstance(value, dict), f"{label} root must be an object")
    return value


def _choose(override: Mapping[str, Any] | None, path: Path, label: str) -> dict[str, Any]:
    return dict(override) if override is not None else _load(path, label)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _git(repo: Path, *args: str, binary: bool = False):
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=False,
        capture_output=True,
        text=not binary,
    )
    if result.returncode != 0:
        detail = result.stderr.decode() if binary else result.stderr
        raise H11AdmissionError(detail.strip() or f"git {' '.join(args)} failed")
    return result.stdout


def _reject_authority_true(value: Any, path: str = "root") -> None:
    if isinstance(value, Mapping):
        for key, item in value.items():
            child = f"{path}.{key}"
            lowered = key.lower()
            if "implementation_authorized" in lowered or "execution_authorized" in lowered:
                _require(item is False, f"{child} must remain false in blocked H11 admission scope")
            _reject_authority_true(item, child)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _reject_authority_true(item, f"{path}[{index}]")


def _contains_key(value: Any, forbidden: set[str]) -> bool:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if key.lower() in forbidden or _contains_key(item, forbidden):
                return True
    elif isinstance(value, list):
        return any(_contains_key(item, forbidden) for item in value)
    return False


def _schema_property(schema: Mapping[str, Any], *path: str) -> Any:
    current: Any = schema
    for part in path:
        _require(isinstance(current, Mapping) and part in current, f"schema path missing: {'/'.join(path)}")
        current = current[part]
    return current


def validate(
    repo: Path,
    *,
    admission_override: Mapping[str, Any] | None = None,
    reviewer_override: Mapping[str, Any] | None = None,
    dependency_schema_override: Mapping[str, Any] | None = None,
    raw_schema_override: Mapping[str, Any] | None = None,
    semantic_schema_override: Mapping[str, Any] | None = None,
    reviewer_schema_override: Mapping[str, Any] | None = None,
    plan_override: Mapping[str, Any] | None = None,
    verify_history: bool = True,
) -> None:
    repo = repo.resolve()
    plan_path = repo / PLAN_PATH
    plan_bytes = plan_path.read_bytes()
    _require(_sha256(plan_bytes) == PLAN_SHA256, "current H11 preregistration SHA-256 drift")

    if verify_history and (repo / ".git").exists():
        result = subprocess.run(
            ["git", "-C", str(repo), "merge-base", "--is-ancestor", PLAN_MERGE, "HEAD"],
            check=False,
            capture_output=True,
        )
        _require(result.returncode == 0, "authoritative H11 preregistration merge is not an ancestor of admission candidate")
        historical = _git(repo, "show", f"{PLAN_MERGE}:{PLAN_PATH.as_posix()}", binary=True)
        _require(_sha256(historical) == PLAN_SHA256, "authoritative H11 plan-merge bytes do not match frozen SHA-256")
        _require(historical == plan_bytes, "current H11 preregistration bytes differ from authoritative plan-merge bytes")

    plan = _choose(plan_override, plan_path, "H11 preregistration")
    _require(plan.get("protocol") == PLAN_PROTOCOL, "H11 preregistration protocol drift")
    _require(plan.get("plan_id") == PLAN_ID, "H11 preregistration plan identity drift")
    _require(plan.get("target_hypothesis") == TARGET, "H11 target family drift")
    _require(plan.get("experiment_identity") == EXPERIMENT_ID, "H11 experiment identity drift")
    _require(plan.get("state") == "PREREGISTERED / EXECUTION_NOT_AUTHORIZED", "H11 plan state drift")
    _require(plan.get("runtime_expansion") == "FROZEN", "H11 preregistration runtime boundary drift")
    _require(plan.get("product_runtime_thaw") is False, "H11 preregistration product runtime thaw drift")
    _require(plan.get("production_authorized") is False, "H11 preregistration production boundary drift")
    _require("DEFERRED" in str(plan.get("final_canon")), "H11 preregistration Final Canon boundary drift")

    plan_graph = plan.get("mechanism_dependency_graph_schema")
    _require(isinstance(plan_graph, Mapping), "frozen H11 mechanism dependency graph definition required")
    _require(
        list(plan_graph.get("mandatory_profile_mechanisms_to_audit", [])) == MANDATORY_MECHANISMS,
        "frozen H11 mandatory profile mechanism inventory drift",
    )
    rubric = plan.get("frozen_mechanism_leakage_rubric")
    _require(isinstance(rubric, Mapping), "frozen H11 leakage rubric required")
    for leakage_class in LEAKAGE_CLASSES:
        _require(leakage_class in rubric, f"frozen H11 leakage class missing: {leakage_class}")
    _require(rubric.get("hard_failure_class") == "UNJUSTIFIED_CANON_DEPENDENCY", "frozen H11 hard-failure class drift")
    _require(rubric.get("support_threshold") == SUPPORT_THRESHOLD, "frozen H11 support threshold drift")
    _require(plan.get("hard_refutation") == HARD_REFUTATION, "frozen H11 hard refutation drift")
    _require(plan.get("allowed_a10_outcome_vocabulary") == A10_OUTCOMES, "frozen H11 A10 vocabulary drift")

    independence = plan.get("reviewer_reproducer_independence_basis")
    _require(isinstance(independence, Mapping), "frozen H11 reviewer/reproducer independence gate required")
    _require(independence.get("required_before_execution") is True, "independence must remain required before H11 execution")
    _require(
        independence.get("current_status") == "NOT_ESTABLISHED / MUST_BE_VERIFIED_AT_EXECUTION_ADMISSION",
        "frozen H11 preregistration independence status drift",
    )
    _require(independence.get("no_qualifying_reviewer_outcome") == BLOCKER, "frozen H11 no-reviewer blocker drift")
    execution_admission = plan.get("execution_admission")
    _require(isinstance(execution_admission, Mapping), "frozen H11 execution-admission requirements required")
    _require(execution_admission.get("requires_frozen_plan_digest") is True, "H11 admission must require a frozen plan digest")
    _require(
        execution_admission.get("requires_qualifying_independent_reviewer_reproducer") is True,
        "H11 admission must require a qualifying independent reviewer/reproducer",
    )
    _reject_authority_true(plan)

    dependency_schema = _choose(
        dependency_schema_override,
        repo / DEPENDENCY_SCHEMA_PATH,
        "H11 dependency graph schema",
    )
    _require(dependency_schema.get("$id") == "nk-h11-dependency-graph/1", "dependency graph protocol drift")
    dep_props = dependency_schema.get("properties")
    _require(isinstance(dep_props, Mapping), "dependency graph properties required")
    _require(dep_props.get("source_plan_sha256", {}).get("const") == PLAN_SHA256, "dependency graph plan digest binding drift")
    node_enum = _schema_property(dep_props, "nodes", "items", "properties", "node_class", "enum")
    edge_enum = _schema_property(dep_props, "edges", "items", "properties", "edge_class", "enum")
    leakage_enum = _schema_property(dep_props, "edges", "items", "properties", "leakage_class", "enum")
    _require(node_enum == NODE_CLASSES, "dependency graph node classes drift")
    _require(edge_enum == EDGE_CLASSES, "dependency graph edge classes drift")
    _require(leakage_enum == LEAKAGE_CLASSES, "dependency graph leakage classes drift")
    _require("INDETERMINATE" not in leakage_enum, "INDETERMINATE is an A10 outcome, not an H11 leakage class")
    mechanism_spec = dep_props.get("mandatory_profile_mechanisms_covered")
    _require(isinstance(mechanism_spec, Mapping), "dependency graph mandatory mechanism coverage required")
    _require(mechanism_spec.get("minItems") == 12 and mechanism_spec.get("maxItems") == 12, "dependency graph must require all 12 profile mechanisms")
    _require(mechanism_spec.get("uniqueItems") is True, "dependency graph mechanism coverage must be unique")
    _require(mechanism_spec.get("items", {}).get("enum") == MANDATORY_MECHANISMS, "dependency graph mechanism inventory drift")

    raw_schema = _choose(raw_schema_override, repo / RAW_SCHEMA_PATH, "H11 raw observation schema")
    _require(raw_schema.get("$id") == "nk-h11-raw-observations/1", "raw observation protocol drift")
    raw_props = raw_schema.get("properties")
    _require(isinstance(raw_props, Mapping), "raw observation properties required")
    _require(raw_props.get("source_plan_sha256", {}).get("const") == PLAN_SHA256, "raw observation plan digest binding drift")
    _require(
        raw_props.get("observation_layer", {}).get("const") == "RAW_FACTS_ONLY_NO_H11_SEMANTIC_JUDGMENT",
        "raw observation/adjudication separation drift",
    )
    raw_kinds = _schema_property(raw_props, "observations", "items", "properties", "observation_kind", "enum")
    _require(raw_kinds == RAW_OBSERVATION_KINDS, "raw observation kind inventory drift")
    _require(
        not _contains_key(raw_schema, {"outcome", "h11_outcome", "semantic_judgment", "adjudication"}),
        "raw observation schema must not contain final H11 semantic judgment fields",
    )
    raw_text = json.dumps(raw_schema, sort_keys=True)
    for outcome in A10_OUTCOMES:
        _require(outcome not in raw_text, f"raw observation schema must not encode final A10 outcome: {outcome}")

    semantic_schema = _choose(
        semantic_schema_override,
        repo / SEMANTIC_SCHEMA_PATH,
        "H11 semantic adjudication schema",
    )
    _require(semantic_schema.get("$id") == "nk-h11-semantic-adjudication/1", "semantic adjudication protocol drift")
    sem_props = semantic_schema.get("properties")
    _require(isinstance(sem_props, Mapping), "semantic adjudication properties required")
    _require(sem_props.get("source_plan_sha256", {}).get("const") == PLAN_SHA256, "semantic adjudication plan digest binding drift")
    _require(sem_props.get("input_policy", {}).get("const") == "REPOSITORY_VISIBLE_FROZEN_INPUTS_ONLY", "semantic adjudication input policy drift")
    _require(sem_props.get("subject_private_state_used", {}).get("const") is False, "private implementation state cannot be semantic-oracle input")
    _require(sem_props.get("outcome", {}).get("enum") == A10_OUTCOMES, "semantic adjudication A10 outcome vocabulary drift")
    sem_rubric = sem_props.get("leakage_rubric", {}).get("properties", {})
    _require(sem_rubric.get("classes", {}).get("const") == LEAKAGE_CLASSES, "semantic adjudication leakage rubric drift")
    _require(sem_rubric.get("hard_failure_class", {}).get("const") == "UNJUSTIFIED_CANON_DEPENDENCY", "semantic adjudication hard-failure class drift")
    _require(sem_rubric.get("support_threshold", {}).get("const") == SUPPORT_THRESHOLD, "semantic adjudication support threshold drift")
    _require(sem_props.get("hard_refutation", {}).get("const") == HARD_REFUTATION, "semantic adjudication hard refutation drift")
    sem_required = semantic_schema.get("required", [])
    for required_field in (
        "raw_observation_record",
        "dependency_graph_record",
        "reviewer_reproducer_qualification_record",
        "subject_private_state_used",
        "outcome",
    ):
        _require(required_field in sem_required, f"semantic adjudication missing required field: {required_field}")

    reviewer_schema = _choose(
        reviewer_schema_override,
        repo / REVIEWER_SCHEMA_PATH,
        "H11 reviewer/reproducer qualification schema",
    )
    _require(reviewer_schema.get("$id") == "nk-h11-reviewer-reproducer-qualification/1", "reviewer qualification schema protocol drift")
    reviewer_schema_props = reviewer_schema.get("properties")
    _require(isinstance(reviewer_schema_props, Mapping), "reviewer qualification schema properties required")
    _require(reviewer_schema_props.get("source_plan_sha256", {}).get("const") == PLAN_SHA256, "reviewer qualification schema digest drift")
    _require(reviewer_schema_props.get("private_implementation_state_used", {}).get("const") is False, "reviewer schema must forbid private implementation state")
    _require(
        reviewer_schema_props.get("qualification_result", {}).get("enum") == ["QUALIFIED", "NOT_ESTABLISHED", "DISQUALIFIED"],
        "reviewer qualification result vocabulary drift",
    )

    reviewer = _choose(reviewer_override, repo / REVIEWER_RECORD_PATH, "H11 reviewer/reproducer qualification record")
    reviewer_required = [
        "protocol",
        "experiment_id",
        "source_plan_id",
        "source_plan_sha256",
        "reviewer_identity_status",
        "reviewer_identity",
        "reviewer_role",
        "authorship_relation",
        "custody_relation",
        "conflicts",
        "repository_visibility",
        "private_implementation_state_used",
        "independence_basis",
        "evidence_references",
        "qualification_result",
    ]
    for key in reviewer_required:
        _require(key in reviewer, f"reviewer/reproducer qualification record missing: {key}")
    _require(reviewer.get("protocol") == "nk-h11-reviewer-reproducer-qualification/1", "reviewer record protocol drift")
    _require(reviewer.get("source_plan_id") == PLAN_ID and reviewer.get("source_plan_sha256") == PLAN_SHA256, "reviewer record plan binding drift")
    _require(reviewer.get("reviewer_identity_status") == "NOT_ESTABLISHED", "blocked admission cannot fabricate an established reviewer identity")
    _require(reviewer.get("reviewer_identity") is None, "blocked admission must not invent reviewer identity")
    _require(reviewer.get("reviewer_role") == "NOT_ESTABLISHED", "blocked admission reviewer role must remain unestablished")
    _require(reviewer.get("authorship_relation") == "UNKNOWN", "authorship relation cannot be asserted without reviewer identity")
    _require(reviewer.get("custody_relation") == "UNKNOWN", "custody relation cannot be asserted without reviewer identity")
    _require(reviewer.get("repository_visibility") == "NO_QUALIFYING_EVIDENCE_VISIBLE", "blocked reviewer record repository visibility drift")
    _require(reviewer.get("private_implementation_state_used") is False, "reviewer qualification cannot use private implementation state")
    _require(reviewer.get("independence_basis") == [], "blocked admission must not fabricate an independence basis")
    _require(reviewer.get("qualification_result") == "NOT_ESTABLISHED", "blocked admission cannot self-declare reviewer qualification")

    admission = _choose(admission_override, repo / ADMISSION_PATH, "H11 execution admission record")
    _require(admission.get("protocol") == "nk-h11-execution-admission/1", "H11 execution admission protocol drift")
    _require(admission.get("admission_id") == "H11-001-execution-admission-v1", "H11 execution admission identity drift")
    _require(admission.get("status") == "BLOCKED", "H11 execution admission must remain BLOCKED in this package")
    _require(admission.get("selected_family") == TARGET, "H11 execution admission family drift")
    _require(admission.get("experiment_id") == EXPERIMENT_ID, "H11 execution admission experiment identity drift")
    _require(admission.get("current_gate_source_sha") == CURRENT_GATE_SOURCE_SHA, "H11 admission source machine-truth checkpoint drift")
    admission_plan = admission.get("plan")
    _require(isinstance(admission_plan, Mapping), "H11 execution admission plan binding required")
    _require(admission_plan.get("protocol") == PLAN_PROTOCOL, "H11 admission plan protocol drift")
    _require(admission_plan.get("plan_id") == PLAN_ID, "H11 admission plan ID drift")
    _require(admission_plan.get("path") == PLAN_PATH.as_posix(), "H11 admission plan path drift")
    _require(admission_plan.get("authoritative_merge") == PLAN_MERGE, "H11 admission plan merge binding drift")
    _require(admission_plan.get("sha256") == PLAN_SHA256, "H11 admission plan digest drift")

    subject = admission.get("subject")
    _require(isinstance(subject, Mapping), "H11 admission subject binding required")
    _require(subject.get("role") == "BOUNDED_REFERENCE_LABORATORY", "H11 subject laboratory role drift")
    _require(subject.get("bundle_id") == BUNDLE_ID and subject.get("manifest_path") == BUNDLE_MANIFEST, "H11 frozen laboratory subject drift")

    schemas = admission.get("schemas")
    _require(isinstance(schemas, Mapping), "H11 admission schema bindings required")
    expected_schemas = {
        "dependency_graph": DEPENDENCY_SCHEMA_PATH.as_posix(),
        "raw_observations": RAW_SCHEMA_PATH.as_posix(),
        "semantic_adjudication": SEMANTIC_SCHEMA_PATH.as_posix(),
        "reviewer_reproducer_qualification": REVIEWER_SCHEMA_PATH.as_posix(),
    }
    _require(dict(schemas) == expected_schemas, "H11 admission schema path bindings drift")
    _require(schemas["raw_observations"] != schemas["semantic_adjudication"], "raw observations and semantic adjudication must remain separate artifacts")

    reviewer_binding = admission.get("reviewer_reproducer")
    _require(isinstance(reviewer_binding, Mapping), "H11 admission reviewer/reproducer binding required")
    _require(reviewer_binding.get("qualification_record") == REVIEWER_RECORD_PATH.as_posix(), "H11 reviewer qualification record path drift")
    _require(reviewer_binding.get("required_before_execution") is True, "H11 reviewer/reproducer must be required before execution")
    _require(reviewer_binding.get("qualification_result") == "NOT_ESTABLISHED", "H11 admission cannot claim qualifying independent reviewer")
    _require(reviewer_binding.get("required_oracle_class") == "INDEPENDENT_SEMANTIC_ORACLE", "H11 required semantic oracle class drift")
    _require(reviewer_binding.get("non_qualifying_substitutes") == NON_QUALIFYING_SUBSTITUTES, "H11 non-qualifying reviewer substitute boundary drift")

    admission_result = admission.get("admission")
    _require(isinstance(admission_result, Mapping), "H11 admission result required")
    _require(admission_result.get("result") == "BLOCKED", "H11 execution admission result must be BLOCKED")
    _require(admission_result.get("blocker") == BLOCKER, "H11 execution admission blocker drift")

    controls = admission.get("frozen_controls")
    _require(isinstance(controls, Mapping), "H11 frozen admission controls required")
    _require(controls.get("raw_observation_semantic_adjudication_separation_required") is True, "H11 raw/adjudication separation must remain mandatory")
    _require(controls.get("leakage_classes") == LEAKAGE_CLASSES, "H11 frozen leakage classes drift")
    _require(controls.get("hard_failure_class") == "UNJUSTIFIED_CANON_DEPENDENCY", "H11 hard failure class drift")
    _require(controls.get("support_threshold") == SUPPORT_THRESHOLD, "H11 support threshold weakening or mutation")
    _require(controls.get("hard_refutation") == HARD_REFUTATION, "H11 hard refutation weakening or mutation")
    _require(controls.get("post_hoc_rubric_mutation") == "FORBIDDEN", "H11 post-hoc rubric mutation must remain forbidden")
    _require(controls.get("historical_evidence_rewrite") == "FORBIDDEN", "H11 historical evidence rewrite must remain forbidden")
    _require(
        controls.get("private_implementation_state_as_required_semantic_oracle_input") == "FORBIDDEN",
        "private implementation state cannot be required H11 semantic-oracle input",
    )

    _require(admission.get("mandatory_profile_mechanisms") == MANDATORY_MECHANISMS, "H11 admission mandatory profile mechanism inventory drift")
    _require(admission.get("allowed_a10_outcomes") == A10_OUTCOMES, "H11 admission A10 outcome vocabulary drift")
    _require(admission.get("implementation_authorized") is False, "H11 implementation remains unauthorized")
    _require(admission.get("execution_authorized") is False, "H11 execution remains unauthorized")
    _require(admission.get("dependency_graph_execution_authorized") is False, "H11 dependency graph execution remains unauthorized")
    _require(admission.get("semantic_adjudication_authorized") is False, "H11 semantic adjudication remains unauthorized")
    _require(admission.get("h11_outcome") == "NOT_TESTED", "H11 must remain NOT_TESTED before qualifying execution/adjudication")
    _require(admission.get("runtime_expansion") == "FROZEN", "H11 admission cannot thaw runtime")
    _require(admission.get("product_runtime_thaw") is False, "H11 admission cannot thaw product runtime")
    _require(admission.get("final_canon") == "DEFERRED / NOT_AUTHORIZED", "H11 admission cannot promote Final Canon")
    _require(admission.get("production_authorized") is False, "H11 admission cannot authorize production")
    _require(admission.get("separate_post_merge_state_checkpoint_required") is True, "H11 admission requires a separate post-merge machine-truth checkpoint")
    _reject_authority_true(admission)

    for path in (
        DEPENDENCY_SCHEMA_PATH,
        RAW_SCHEMA_PATH,
        SEMANTIC_SCHEMA_PATH,
        REVIEWER_SCHEMA_PATH,
        REVIEWER_RECORD_PATH,
        ADMISSION_PATH,
        Path(BUNDLE_MANIFEST),
    ):
        _require((repo / path).is_file(), f"missing H11 admission artifact: {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    args = parser.parse_args()
    try:
        validate(args.repo)
    except (H11AdmissionError, OSError, json.JSONDecodeError) as exc:
        print(f"H11 execution admission validation FAILED: {exc}", file=sys.stderr)
        return 1
    print(
        "H11 execution admission valid; "
        "admission=BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER; "
        "H11=NOT_TESTED; implementation=NOT_AUTHORIZED; execution=NOT_AUTHORIZED; runtime=FROZEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
