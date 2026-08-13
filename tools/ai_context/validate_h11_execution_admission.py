#!/usr/bin/env python3
"""Validate the blocked A10-H11 execution-admission package fail closed."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
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
RAW_OBSERVATION_TYPES = [
    "DIRECT_MEASUREMENT",
    "REPOSITORY_INSPECTION",
    "TOOL_OUTPUT",
    "DECLARED_MISSING_DATA",
]
RAW_PRODUCER_AUTHORITY_CLASSES = [
    "SUBJECT_IMPLEMENTATION",
    "CI_RUNNER",
    "AUTOMATED_VALIDATOR",
    "REPOSITORY_OBSERVER",
    "QUALIFYING_INDEPENDENT_REVIEWER",
    "NON_QUALIFYING_REVIEW_BOT",
]
SEMANTIC_VERDICT_TOKENS = frozenset(
    A10_OUTCOMES + ["PASS", "QUALIFIED", "SUPPORTED"]
)
SEMANTIC_VERDICT_KEYS = frozenset(
    {
        "adjudication",
        "h11_outcome",
        "outcome",
        "qualification_result",
        "semantic_judgment",
        "verdict",
    }
)
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


def _validate_repository_reference(
    repo: Path,
    reference: Any,
    *,
    expected_type: str,
    label: str,
) -> Path:
    _require(isinstance(reference, Mapping), f"{label} must be a content-addressed object")
    _require(
        set(reference) == {"path", "sha256", "artifact_type"},
        f"{label} must contain only path, sha256, and artifact_type",
    )
    raw_path = reference.get("path")
    digest = reference.get("sha256")
    _require(isinstance(raw_path, str) and raw_path, f"{label}.path required")
    _require(
        not raw_path.startswith("/") and ".." not in Path(raw_path).parts,
        f"{label}.path must be repository-relative",
    )
    _require(
        isinstance(digest, str) and re.fullmatch(r"[0-9a-f]{64}", digest) is not None,
        f"{label}.sha256 must be lowercase SHA-256",
    )
    _require(reference.get("artifact_type") == expected_type, f"{label}.artifact_type drift")
    candidate = (repo / raw_path).resolve()
    _require(candidate.is_relative_to(repo), f"{label}.path escapes repository")
    _require(candidate.is_file(), f"{label}.path does not exist: {raw_path}")
    _require(_sha256(candidate.read_bytes()) == digest, f"{label}.sha256 mismatch: {raw_path}")
    return candidate


def _load_referenced_json(
    repo: Path,
    reference: Any,
    *,
    expected_type: str,
    label: str,
) -> dict[str, Any]:
    path = _validate_repository_reference(
        repo,
        reference,
        expected_type=expected_type,
        label=label,
    )
    return _load(path, label)


def _contains_semantic_verdict(value: Any) -> bool:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key).strip().lower() in SEMANTIC_VERDICT_KEYS:
                return True
            if _contains_semantic_verdict(item):
                return True
        return False
    if isinstance(value, list):
        return any(_contains_semantic_verdict(item) for item in value)
    if isinstance(value, str):
        upper = value.upper()
        return any(
            re.search(rf"(?<![A-Z0-9_]){re.escape(token)}(?![A-Z0-9_])", upper)
            for token in SEMANTIC_VERDICT_TOKENS
        )
    return False


def _validate_reviewer_record(repo: Path, reviewer: Mapping[str, Any]) -> None:
    required = [
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
    for key in required:
        _require(key in reviewer, f"reviewer/reproducer qualification record missing: {key}")
    _require(reviewer.get("protocol") == "nk-h11-reviewer-reproducer-qualification/1", "reviewer record protocol drift")
    _require(reviewer.get("experiment_id") == EXPERIMENT_ID, "reviewer record experiment drift")
    _require(
        reviewer.get("source_plan_id") == PLAN_ID
        and reviewer.get("source_plan_sha256") == PLAN_SHA256,
        "reviewer record plan binding drift",
    )
    _require(reviewer.get("private_implementation_state_used") is False, "reviewer qualification cannot use private implementation state")
    conflicts = reviewer.get("conflicts")
    independence_basis = reviewer.get("independence_basis")
    evidence_references = reviewer.get("evidence_references")
    _require(isinstance(conflicts, list), "reviewer conflicts must be an array")
    _require(isinstance(independence_basis, list), "reviewer independence basis must be an array")
    _require(isinstance(evidence_references, list), "reviewer evidence references must be an array")
    for index, reference in enumerate(evidence_references):
        _validate_repository_reference(
            repo,
            reference,
            expected_type="REVIEWER_EVIDENCE",
            label=f"reviewer evidence reference {index}",
        )

    result = reviewer.get("qualification_result")
    _require(result in {"QUALIFIED", "NOT_ESTABLISHED", "DISQUALIFIED"}, "reviewer qualification result invalid")
    if result == "QUALIFIED":
        _require(reviewer.get("reviewer_identity_status") == "ESTABLISHED", "qualified reviewer identity must be established")
        _require(isinstance(reviewer.get("reviewer_identity"), str) and reviewer.get("reviewer_identity"), "qualified reviewer identity required")
        _require(reviewer.get("reviewer_role") in {"REVIEWER", "REPRODUCER", "REVIEWER_AND_REPRODUCER"}, "qualified reviewer role invalid")
        _require(
            reviewer.get("authorship_relation")
            == "NOT_AUTHOR_OF_PREREGISTRATION_OR_FROZEN_RUBRIC",
            "qualified reviewer cannot author the frozen H11 plan or rubric",
        )
        _require(
            reviewer.get("custody_relation") == "INDEPENDENT_FOR_DECLARED_SCOPE",
            "qualified reviewer custody must be independent for the declared scope",
        )
        _require(conflicts == [], "qualified reviewer cannot carry unresolved conflicts")
        _require(reviewer.get("repository_visibility") == "EVIDENCE_VISIBLE", "qualified reviewer evidence must be repository-visible")
        _require(bool(independence_basis), "qualified reviewer independence basis required")
        _require(bool(evidence_references), "qualified reviewer evidence references required")


def validate_h11_evidence_bundle(
    repo: Path,
    *,
    dependency_graph: Mapping[str, Any],
    raw_observations: Mapping[str, Any],
    semantic_adjudication: Mapping[str, Any],
    reviewer_record: Mapping[str, Any],
    semantic_adjudication_path: str,
) -> None:
    """Validate a future H11 evidence chain without executing or adjudicating H11.

    This is fail-closed validation machinery only. Tests call it with synthetic fixtures;
    repository admission remains blocked and no real H11 evidence bundle exists yet.
    """
    repo = repo.resolve()
    _require(dependency_graph.get("protocol") == "nk-h11-dependency-graph/1", "dependency graph protocol drift")
    _require(raw_observations.get("protocol") == "nk-h11-raw-observations/1", "raw observation protocol drift")
    _require(semantic_adjudication.get("protocol") == "nk-h11-semantic-adjudication/1", "semantic adjudication protocol drift")
    for label, record in (
        ("dependency graph", dependency_graph),
        ("raw observations", raw_observations),
        ("semantic adjudication", semantic_adjudication),
        ("reviewer qualification", reviewer_record),
    ):
        _require(record.get("experiment_id") == EXPERIMENT_ID, f"{label} experiment drift")
        _require(record.get("source_plan_id") == PLAN_ID, f"{label} plan ID drift")
        _require(record.get("source_plan_sha256") == PLAN_SHA256, f"{label} plan digest drift")

    observations = raw_observations.get("observations")
    _require(isinstance(observations, list) and observations, "raw observations required")
    observation_by_id: dict[str, Mapping[str, Any]] = {}
    for index, observation in enumerate(observations):
        _require(isinstance(observation, Mapping), f"raw observation {index} must be an object")
        observation_id = observation.get("observation_id")
        _require(isinstance(observation_id, str) and observation_id, f"raw observation {index} ID required")
        _require(observation_id not in observation_by_id, f"duplicate raw observation ID: {observation_id}")
        _require(observation.get("observation_kind") in RAW_OBSERVATION_KINDS, f"raw observation {observation_id} kind invalid")
        _require(observation.get("observation_type") in RAW_OBSERVATION_TYPES, f"raw observation {observation_id} type invalid")
        _require(isinstance(observation.get("producer_identity"), str) and observation.get("producer_identity"), f"raw observation {observation_id} producer identity required")
        _require(observation.get("producer_authority_class") in RAW_PRODUCER_AUTHORITY_CLASSES, f"raw observation {observation_id} producer authority invalid")
        _validate_repository_reference(
            repo,
            observation.get("source_reference"),
            expected_type="REPOSITORY_SOURCE",
            label=f"raw observation {observation_id} source",
        )
        _require(observation.get("repository_visible") is True, f"raw observation {observation_id} is not repository-visible")
        _require(not _contains_semantic_verdict(observation.get("fact")), f"raw observation {observation_id} contains a semantic verdict")
        _require(not _contains_semantic_verdict(observation.get("structured_value")), f"raw observation {observation_id} structured value contains a semantic verdict")
        observation_by_id[observation_id] = observation

    nodes = dependency_graph.get("nodes")
    edges = dependency_graph.get("edges")
    covered = dependency_graph.get("mandatory_profile_mechanisms_covered")
    _require(isinstance(nodes, list) and nodes, "dependency graph nodes required")
    _require(isinstance(edges, list) and edges, "dependency graph edges required")
    _require(isinstance(covered, list), "dependency graph coverage inventory required")
    _require(len(covered) == len(MANDATORY_MECHANISMS) and set(covered) == set(MANDATORY_MECHANISMS), "dependency graph must cover exactly all mandatory mechanisms")

    node_by_id: dict[str, Mapping[str, Any]] = {}
    profile_nodes: dict[str, list[str]] = {mechanism: [] for mechanism in MANDATORY_MECHANISMS}
    for index, node in enumerate(nodes):
        _require(isinstance(node, Mapping), f"dependency node {index} must be an object")
        node_id = node.get("node_id")
        _require(isinstance(node_id, str) and node_id, f"dependency node {index} ID required")
        _require(node_id not in node_by_id, f"duplicate dependency node ID: {node_id}")
        _require(node.get("node_class") in NODE_CLASSES, f"dependency node {node_id} class invalid")
        _validate_repository_reference(
            repo,
            node.get("source_reference"),
            expected_type="REPOSITORY_SOURCE",
            label=f"dependency node {node_id} source",
        )
        if node.get("node_class") == "PROFILE_MECHANISM":
            mechanism = node.get("mechanism_name")
            _require(mechanism in profile_nodes, f"dependency node {node_id} mechanism invalid")
            profile_nodes[str(mechanism)].append(node_id)
        node_by_id[node_id] = node

    connected_nodes: set[str] = set()
    edge_ids: set[str] = set()
    unjustified_count = 0
    unjustified_profile_mechanisms: set[str] = set()
    for index, edge in enumerate(edges):
        _require(isinstance(edge, Mapping), f"dependency edge {index} must be an object")
        edge_id = edge.get("edge_id")
        _require(isinstance(edge_id, str) and edge_id, f"dependency edge {index} ID required")
        _require(edge_id not in edge_ids, f"duplicate dependency edge ID: {edge_id}")
        edge_ids.add(edge_id)
        from_id = edge.get("from")
        to_id = edge.get("to")
        _require(from_id in node_by_id and to_id in node_by_id, f"dependency edge {edge_id} endpoint missing")
        connected_nodes.update((str(from_id), str(to_id)))
        _require(edge.get("edge_class") in EDGE_CLASSES, f"dependency edge {edge_id} class invalid")
        leakage_class = edge.get("leakage_class")
        _require(leakage_class in LEAKAGE_CLASSES, f"dependency edge {edge_id} leakage class invalid")
        if leakage_class == "UNJUSTIFIED_CANON_DEPENDENCY":
            unjustified_count += 1
            implicated_mechanisms = {
                str(node_by_id[node_id]["mechanism_name"])
                for node_id in (from_id, to_id)
                if node_by_id[node_id].get("node_class") == "PROFILE_MECHANISM"
            }
            _require(
                implicated_mechanisms,
                f"unjustified dependency edge {edge_id} must implicate a PROFILE_MECHANISM",
            )
            unjustified_profile_mechanisms.update(implicated_mechanisms)
        raw_refs = edge.get("raw_observation_refs")
        _require(isinstance(raw_refs, list) and raw_refs, f"dependency edge {edge_id} raw evidence required")
        _require(len(raw_refs) == len(set(raw_refs)), f"dependency edge {edge_id} raw refs must be unique")
        for observation_id in raw_refs:
            _require(observation_id in observation_by_id, f"dependency edge {edge_id} references missing raw observation: {observation_id}")
            observation = observation_by_id[str(observation_id)]
            _require(
                observation.get("observation_kind") == "DEPENDENCY_EDGE",
                f"dependency edge {edge_id} raw reference {observation_id} is not DEPENDENCY_EDGE evidence",
            )
            binding = observation.get("structured_value")
            _require(
                isinstance(binding, Mapping)
                and binding.get("edge_id") == edge_id
                and binding.get("from") == from_id
                and binding.get("to") == to_id,
                f"dependency edge {edge_id} raw reference {observation_id} is not bound to the exact edge",
            )

    for mechanism, mechanism_nodes in profile_nodes.items():
        _require(len(mechanism_nodes) == 1, f"covered mechanism {mechanism!r} must have exactly one PROFILE_MECHANISM node")
        _require(mechanism_nodes[0] in connected_nodes, f"covered mechanism {mechanism!r} has no dependency edge")

    _validate_reviewer_record(repo, reviewer_record)
    raw_ref = semantic_adjudication.get("raw_observation_record")
    graph_ref = semantic_adjudication.get("dependency_graph_record")
    reviewer_ref = semantic_adjudication.get("reviewer_reproducer_qualification_record")
    references = [raw_ref, graph_ref, reviewer_ref]
    reference_paths = [reference.get("path") if isinstance(reference, Mapping) else None for reference in references]
    _require(len(set(reference_paths)) == 3 and None not in reference_paths, "semantic input artifacts must be three distinct paths")
    _require(semantic_adjudication_path not in reference_paths, "semantic adjudication cannot reference itself as an input")
    _require(
        _load_referenced_json(repo, raw_ref, expected_type="RAW_OBSERVATIONS", label="semantic raw input") == dict(raw_observations),
        "semantic raw input does not match supplied raw observations",
    )
    _require(
        _load_referenced_json(repo, graph_ref, expected_type="DEPENDENCY_GRAPH", label="semantic dependency input") == dict(dependency_graph),
        "semantic dependency input does not match supplied graph",
    )
    _require(
        _load_referenced_json(repo, reviewer_ref, expected_type="REVIEWER_QUALIFICATION", label="semantic reviewer input") == dict(reviewer_record),
        "semantic reviewer input does not match supplied qualification",
    )
    _require(semantic_adjudication.get("input_policy") == "REPOSITORY_VISIBLE_FROZEN_INPUTS_ONLY", "semantic input policy drift")
    _require(semantic_adjudication.get("subject_private_state_used") is False, "semantic adjudication cannot use private subject state")
    _require(reviewer_record.get("qualification_result") == "QUALIFIED", "semantic adjudication requires a qualifying independent reviewer")
    _require(semantic_adjudication.get("independence_qualified") is True, "semantic adjudication independence must be qualified")
    _require(semantic_adjudication.get("unjustified_canon_dependency_count") == unjustified_count, "semantic unjustified dependency count does not match graph")
    _require(
        semantic_adjudication.get("mandatory_profile_leakage_count") == len(unjustified_profile_mechanisms),
        "semantic mandatory-profile leakage count does not match implicated mechanisms",
    )
    if semantic_adjudication.get("outcome") == "SUPPORTED_FOR_SCOPE":
        _require(unjustified_count == 0, "SUPPORTED_FOR_SCOPE cannot contain UNJUSTIFIED_CANON_DEPENDENCY")
        _require(semantic_adjudication.get("mandatory_profile_leakage_count") == 0, "SUPPORTED_FOR_SCOPE requires zero mandatory profile leakage")


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
    _require(dep_props.get("edges", {}).get("minItems") == 1, "dependency graph must require at least one evidence-bearing edge")
    node_props = _schema_property(dep_props, "nodes", "items", "properties")
    _require(node_props.get("source_reference", {}).get("$ref") == "#/$defs/repositoryArtifactReference", "dependency nodes require content-addressed repository sources")
    _require(node_props.get("mechanism_name", {}).get("enum") == MANDATORY_MECHANISMS, "profile mechanism node inventory drift")
    node_rules = _schema_property(dep_props, "nodes", "items", "allOf")
    _require(isinstance(node_rules, list) and node_rules, "PROFILE_MECHANISM nodes must conditionally require mechanism_name")
    node_rule_text = json.dumps(node_rules, sort_keys=True)
    _require('"PROFILE_MECHANISM"' in node_rule_text, "PROFILE_MECHANISM condition drift")
    _require('"then": {"required": ["mechanism_name"]}' in node_rule_text, "PROFILE_MECHANISM must require mechanism_name")

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
    raw_item = _schema_property(raw_props, "observations", "items")
    raw_required = raw_item.get("required", [])
    for required_field in (
        "observation_type",
        "producer_identity",
        "producer_authority_class",
        "source_reference",
        "repository_visible",
    ):
        _require(required_field in raw_required, f"raw observation missing required provenance field: {required_field}")
    raw_item_props = raw_item.get("properties", {})
    _require(raw_item_props.get("observation_type", {}).get("enum") == RAW_OBSERVATION_TYPES, "raw observation type inventory drift")
    _require(raw_item_props.get("producer_authority_class", {}).get("enum") == RAW_PRODUCER_AUTHORITY_CLASSES, "raw producer authority inventory drift")
    _require(raw_item_props.get("source_reference", {}).get("$ref") == "#/$defs/repositoryArtifactReference", "raw observations require content-addressed sources")
    raw_item_rules = raw_item.get("allOf")
    _require(isinstance(raw_item_rules, list) and raw_item_rules, "dependency-edge observations require structured edge binding")
    raw_rule_text = json.dumps(raw_item_rules, sort_keys=True)
    for required_literal in (
        '"DEPENDENCY_EDGE"',
        '"required": ["structured_value"]',
        '"required": ["edge_id", "from", "to"]',
    ):
        _require(required_literal in raw_rule_text, f"dependency-edge raw binding invariant missing: {required_literal}")
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
        "mandatory_profile_leakage_count",
        "unjustified_canon_dependency_count",
        "independence_qualified",
        "outcome",
    ):
        _require(required_field in sem_required, f"semantic adjudication missing required field: {required_field}")
    semantic_types = {
        "raw_observation_record": "RAW_OBSERVATIONS",
        "dependency_graph_record": "DEPENDENCY_GRAPH",
        "reviewer_reproducer_qualification_record": "REVIEWER_QUALIFICATION",
    }
    for field, artifact_type in semantic_types.items():
        spec = sem_props.get(field, {})
        _require(isinstance(spec.get("allOf"), list), f"semantic {field} must be a structured artifact reference")
        _require(
            any(
                isinstance(rule, Mapping)
                and rule.get("properties", {}).get("artifact_type", {}).get("const") == artifact_type
                for rule in spec["allOf"]
            ),
            f"semantic {field} artifact type drift",
        )
    support_rules = semantic_schema.get("allOf")
    _require(isinstance(support_rules, list) and support_rules, "semantic support outcome must have conditional invariants")
    support_rule_text = json.dumps(support_rules, sort_keys=True)
    for required_literal in (
        '"SUPPORTED_FOR_SCOPE"',
        '"independence_qualified": {"const": true}',
        '"mandatory_profile_leakage_count": {"const": 0}',
        '"unjustified_canon_dependency_count": {"const": 0}',
    ):
        _require(required_literal in support_rule_text, f"semantic support invariant missing: {required_literal}")

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
    evidence_items = reviewer_schema_props.get("evidence_references", {}).get("items", {})
    _require(evidence_items.get("$ref") == "#/$defs/evidenceReference", "reviewer evidence must be content-addressed")
    reviewer_rules = reviewer_schema.get("allOf")
    _require(isinstance(reviewer_rules, list) and reviewer_rules, "qualified reviewer conditional constraints required")
    reviewer_rule_text = json.dumps(reviewer_rules, sort_keys=True)
    for required_literal in (
        '"custody_relation": {"const": "INDEPENDENT_FOR_DECLARED_SCOPE"}',
        '"conflicts": {"maxItems": 0}',
        '"evidence_references": {"minItems": 1}',
    ):
        _require(required_literal in reviewer_rule_text, f"qualified reviewer invariant missing: {required_literal}")

    reviewer = _choose(reviewer_override, repo / REVIEWER_RECORD_PATH, "H11 reviewer/reproducer qualification record")
    _validate_reviewer_record(repo, reviewer)
    _require(reviewer.get("reviewer_identity_status") == "ESTABLISHED", "substantive Codex reviewer identity reconciliation drift")
    _require(reviewer.get("reviewer_identity") == "OpenAI GPT-5.6 Sol / Codex review agent", "Codex reviewer identity drift")
    _require(reviewer.get("reviewer_role") == "REVIEWER", "Codex reviewer role drift")
    _require(reviewer.get("authorship_relation") == "NOT_AUTHOR_OF_PREREGISTRATION_OR_FROZEN_RUBRIC", "Codex reviewer authorship disclosure drift")
    _require(reviewer.get("custody_relation") == "SHARED_CUSTODY_DISCLOSED", "Codex review shared-custody disclosure drift")
    _require(reviewer.get("repository_visibility") == "EVIDENCE_VISIBLE", "Codex review evidence visibility drift")
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
