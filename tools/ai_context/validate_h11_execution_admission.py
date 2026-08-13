#!/usr/bin/env python3
"""Validate the blocked A10-H11 execution-admission package fail closed."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Mapping

PLAN_PATH = Path("docs/research/H11_PREREGISTRATION.json")
PLAN_ID = "H11-001-c5-lab-canon-separation-v1"
PLAN_PROTOCOL = "nk-h11-preregistration/1"
PLAN_MERGE = "4a75ff15542013c033030620bdff61997e365140"
PLAN_SHA256 = "60da649e675b79b3e70bf8a61cf03cb4d57bb989f4934b65ab8d50c925b19914"
FROZEN_REVIEW_SUBJECT = "e36b7f45410d74b8a65406bff6fdd6d070fa96b0"
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
FROZEN_OBLIGATION_IDS = ["H11-O01", "H11-O02", "H11-O03", "H11-O04"]
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
RAW_FACT_TOKENS = {
    "BUNDLE_VERIFICATION": "BUNDLE_VERIFICATION_OBSERVED",
    "MANIFEST_IDENTITY": "MANIFEST_IDENTITY_OBSERVED",
    "ARTIFACT_INVENTORY": "ARTIFACT_INVENTORY_OBSERVED",
    "DEPENDENCY_EDGE": "DEPENDENCY_EDGE_OBSERVED",
    "SOURCE_REFERENCE": "SOURCE_REFERENCE_OBSERVED",
    "MECHANISM_CLASSIFICATION_INPUT": "MECHANISM_CLASSIFICATION_INPUT_OBSERVED",
    "REVIEWER_IDENTITY_EVIDENCE": "REVIEWER_IDENTITY_EVIDENCE_OBSERVED",
    "INDEPENDENCE_EVIDENCE": "INDEPENDENCE_EVIDENCE_OBSERVED",
    "MISSING_DATA": "MISSING_DATA_OBSERVED",
}
INDEPENDENCE_BASIS_TYPES = {
    "ORGANIZATIONAL_SEPARATION",
    "INDEPENDENT_EVIDENCE_CUSTODY",
    "NON_AUTHORSHIP",
    "CONFLICT_SCREEN",
    "PRIVATE_STATE_EXCLUSION",
}
INDEPENDENCE_EVIDENCE_PROTOCOL = "nk-h11-reviewer-independence-evidence/1"
CORE_INDEPENDENCE_ISSUER_ROLES = {
    "ORGANIZATIONAL_SEPARATION": "ORGANIZATIONAL_AUTHORITY",
    "INDEPENDENT_EVIDENCE_CUSTODY": "INDEPENDENT_CUSTODIAN",
}
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


def _commit_author_email(repo: Path, commit: str) -> str:
    """Return the Git author email of a commit, used to authenticate issuer provenance.

    Free-text `evidence_issuer_identity` strings can be invented by whoever writes the
    JSON; the Git author email of the commit that actually introduced the evidence file
    is not. It still cannot prove a real-world organizational relationship, but it closes
    the reproduced bypass where a single process commits both attestations under invented
    issuer labels while remaining the sole author of record.
    """
    email = _git(repo, "log", "-1", "--format=%ae", f"{commit}^{{commit}}").strip()
    _require(bool(email), f"cannot resolve Git author email for commit {commit}")
    return email


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
    frozen_at: str | None = None,
) -> bytes:
    _require(isinstance(reference, Mapping), f"{label} must be a content-addressed object")
    _require(
        set(reference) == {"path", "sha256", "artifact_type", "git_commit"},
        f"{label} must contain only path, sha256, artifact_type, and git_commit",
    )
    raw_path = reference.get("path")
    digest = reference.get("sha256")
    git_commit = reference.get("git_commit")
    _require(isinstance(raw_path, str) and raw_path, f"{label}.path required")
    _require(
        not raw_path.startswith("/") and ".." not in Path(raw_path).parts,
        f"{label}.path must be repository-relative",
    )
    _require(
        isinstance(digest, str) and re.fullmatch(r"[0-9a-f]{64}", digest) is not None,
        f"{label}.sha256 must be lowercase SHA-256",
    )
    _require(
        isinstance(git_commit, str) and re.fullmatch(r"[0-9a-f]{40}", git_commit) is not None,
        f"{label}.git_commit must be a full lowercase Git commit SHA",
    )
    _require(reference.get("artifact_type") == expected_type, f"{label}.artifact_type drift")
    _git(repo, "cat-file", "-e", f"{git_commit}^{{commit}}")
    ancestry = subprocess.run(
        ["git", "-C", str(repo), "merge-base", "--is-ancestor", git_commit, "HEAD"],
        check=False,
        capture_output=True,
    )
    _require(ancestry.returncode == 0, f"{label}.git_commit is not anchored in the adjudicated HEAD")
    committed = _git(repo, "show", f"{git_commit}:{raw_path}", binary=True)
    _require(_sha256(committed) == digest, f"{label}.sha256 mismatch at declared Git commit: {raw_path}")
    if frozen_at is not None:
        _git(repo, "cat-file", "-e", f"{frozen_at}^{{commit}}")
        frozen_ancestry = subprocess.run(
            ["git", "-C", str(repo), "merge-base", "--is-ancestor", frozen_at, "HEAD"],
            check=False,
            capture_output=True,
        )
        _require(frozen_ancestry.returncode == 0, f"{label} frozen review subject is not anchored in HEAD")
        source_ancestry = subprocess.run(
            ["git", "-C", str(repo), "merge-base", "--is-ancestor", git_commit, frozen_at],
            check=False,
            capture_output=True,
        )
        _require(
            source_ancestry.returncode == 0,
            f"{label}.git_commit postdates the immutable H11 review subject",
        )
        frozen_bytes = _git(repo, "show", f"{frozen_at}:{raw_path}", binary=True)
        _require(
            frozen_bytes == committed,
            f"{label} was not present unchanged at the immutable H11 review subject: {raw_path}",
        )
    head_bytes = _git(repo, "show", f"HEAD:{raw_path}", binary=True)
    _require(head_bytes == committed, f"{label} is not preserved unchanged at adjudicated HEAD: {raw_path}")
    return committed


def _load_referenced_json(
    repo: Path,
    reference: Any,
    *,
    expected_type: str,
    label: str,
) -> dict[str, Any]:
    payload = _validate_repository_reference(
        repo,
        reference,
        expected_type=expected_type,
        label=label,
    )
    try:
        value = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise H11AdmissionError(f"cannot read {label}: {exc}") from exc
    _require(isinstance(value, dict), f"{label} root must be an object")
    return value


def _json_exact_equal(left: Any, right: Any) -> bool:
    """Compare JSON values without Python's bool/int equality coercion."""
    if isinstance(left, Mapping) or isinstance(right, Mapping):
        if not isinstance(left, Mapping) or not isinstance(right, Mapping):
            return False
        return set(left) == set(right) and all(
            _json_exact_equal(left[key], right[key]) for key in left
        )
    if isinstance(left, list) or isinstance(right, list):
        return (
            isinstance(left, list)
            and isinstance(right, list)
            and len(left) == len(right)
            and all(_json_exact_equal(a, b) for a, b in zip(left, right))
        )
    return type(left) is type(right) and left == right


def _authenticated_verifier_bytes(repo: Path, relative: str) -> bytes:
    """Resolve verifier bytes from the adjudicated Git HEAD, not the mutable worktree.

    A worktree copy can be replaced with a no-op after evidence is corrupted, so the
    bytes that are actually executed must be proven identical to the committed HEAD
    object rather than trusted from disk.
    """
    worktree_path = repo / relative
    _require(worktree_path.is_file(), f"frozen bundle verifier is missing: {relative}")
    committed = _git(repo, "show", f"HEAD:{relative}", binary=True)
    _require(
        worktree_path.read_bytes() == committed,
        f"frozen bundle verifier worktree bytes do not match the Git-committed HEAD object: {relative}",
    )
    return committed


def _verify_frozen_bundle(repo: Path) -> int:
    manifest_path = repo / BUNDLE_MANIFEST
    _require(manifest_path.is_file(), "frozen bundle manifest is missing")
    verifier_bytes = _authenticated_verifier_bytes(repo, "tools/evidence/verify_bundle.py")
    with tempfile.TemporaryDirectory() as anchored_dir:
        anchored_verifier = Path(anchored_dir) / "verify_bundle.py"
        anchored_verifier.write_bytes(verifier_bytes)
        result = subprocess.run(
            [sys.executable, str(anchored_verifier), BUNDLE_MANIFEST, "--repo", str(repo)],
            cwd=repo,
            check=False,
            capture_output=True,
            text=True,
        )
    _require(
        result.returncode == 0,
        "frozen bundle verifier failed: " + (result.stderr.strip() or result.stdout.strip()),
    )
    manifest = _load(manifest_path, "frozen C5 evidence manifest")
    _require(manifest.get("bundle_id") == BUNDLE_ID, "frozen bundle verifier subject drift")
    checkpoints = manifest.get("checkpoints")
    _require(isinstance(checkpoints, list), "frozen bundle checkpoints required")
    artifact_count = sum(
        len(checkpoint.get("artifacts", []))
        for checkpoint in checkpoints
        if isinstance(checkpoint, Mapping) and isinstance(checkpoint.get("artifacts"), list)
    )
    _require(artifact_count == 8, "frozen bundle verifier must cover exactly eight artifacts")
    return artifact_count


def _schema_accepts(schema: Any, instance: Any, *, root: Mapping[str, Any] | None = None) -> bool:
    """Evaluate the JSON-Schema subset used by the frozen H11 contracts.

    This deliberately small evaluator makes conditional invariants executable in the
    admission validator without adding a new runtime dependency. Unsupported schema
    shapes fail closed through the explicit checks below.
    """
    if isinstance(schema, bool):
        return schema
    if not isinstance(schema, Mapping):
        return False
    if root is None:
        root = schema
    reference = schema.get("$ref")
    if reference is not None:
        if not isinstance(reference, str) or not reference.startswith("#/"):
            return False
        target: Any = root
        for part in reference[2:].split("/"):
            if not isinstance(target, Mapping) or part not in target:
                return False
            target = target[part]
        if not _schema_accepts(target, instance, root=root):
            return False
    if "allOf" in schema and not all(
        _schema_accepts(rule, instance, root=root) for rule in schema["allOf"]
    ):
        return False
    if "anyOf" in schema and not any(
        _schema_accepts(rule, instance, root=root) for rule in schema["anyOf"]
    ):
        return False
    if "oneOf" in schema and sum(
        _schema_accepts(rule, instance, root=root) for rule in schema["oneOf"]
    ) != 1:
        return False
    if "not" in schema and _schema_accepts(schema["not"], instance, root=root):
        return False
    if "if" in schema:
        branch = "then" if _schema_accepts(schema["if"], instance, root=root) else "else"
        if branch in schema and not _schema_accepts(schema[branch], instance, root=root):
            return False

    expected_type = schema.get("type")
    if expected_type is not None:
        expected_types = [expected_type] if isinstance(expected_type, str) else expected_type

        def matches_type(name: str) -> bool:
            return {
                "object": isinstance(instance, Mapping),
                "array": isinstance(instance, list),
                "string": isinstance(instance, str),
                "integer": isinstance(instance, int) and not isinstance(instance, bool),
                "number": isinstance(instance, (int, float)) and not isinstance(instance, bool),
                "boolean": isinstance(instance, bool),
                "null": instance is None,
            }.get(name, False)

        if not isinstance(expected_types, list) or not any(matches_type(name) for name in expected_types):
            return False
    if "const" in schema and not _json_exact_equal(instance, schema["const"]):
        return False
    if "enum" in schema:
        enum_values = schema["enum"]
        if not isinstance(enum_values, list) or not any(
            _json_exact_equal(instance, candidate) for candidate in enum_values
        ):
            return False
    if isinstance(instance, str):
        if len(instance) < schema.get("minLength", 0):
            return False
        pattern = schema.get("pattern")
        if pattern is not None:
            if not isinstance(pattern, str):
                return False
            try:
                if re.search(pattern, instance) is None:
                    return False
            except re.error:
                return False
    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            return False
        if "maximum" in schema and instance > schema["maximum"]:
            return False
    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            return False
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            return False
        if schema.get("uniqueItems") and len({json.dumps(item, sort_keys=True) for item in instance}) != len(instance):
            return False
        if "items" in schema and not all(
            _schema_accepts(schema["items"], item, root=root) for item in instance
        ):
            return False
        if "contains" in schema:
            matches = sum(
                _schema_accepts(schema["contains"], item, root=root) for item in instance
            )
            if matches < schema.get("minContains", 1):
                return False
            if "maxContains" in schema and matches > schema["maxContains"]:
                return False
    if isinstance(instance, Mapping):
        required = schema.get("required", [])
        if not isinstance(required, list) or any(key not in instance for key in required):
            return False
        properties = schema.get("properties", {})
        if not isinstance(properties, Mapping):
            return False
        if schema.get("additionalProperties") is False and any(
            key not in properties for key in instance
        ):
            return False
        for key, subschema in properties.items():
            if key in instance and not _schema_accepts(subschema, instance[key], root=root):
                return False
    return True


def _schema_reference(artifact_type: str) -> dict[str, str]:
    return {
        "path": "evidence/example.json",
        "sha256": "0" * 64,
        "artifact_type": artifact_type,
        "git_commit": "0" * 40,
    }


def _validate_schema_behavior(
    *,
    dependency_schema: Mapping[str, Any],
    raw_schema: Mapping[str, Any],
    semantic_schema: Mapping[str, Any],
    reviewer_schema: Mapping[str, Any],
) -> None:
    """Exercise conditional H11 schema rules with valid and adversarial instances."""
    repository_source = _schema_reference("REPOSITORY_SOURCE")
    dependency_node_schema = _schema_property(
        dependency_schema, "properties", "nodes", "items"
    )
    invalid_profile_node = {
        "node_id": "profile-node",
        "node_class": "PROFILE_MECHANISM",
        "label": "profile mechanism",
        "source_reference": repository_source,
    }
    _require(
        not _schema_accepts(
            dependency_node_schema,
            invalid_profile_node,
            root=dependency_schema,
        ),
        "dependency schema condition does not semantically require PROFILE_MECHANISM identity",
    )

    raw_item_schema = _schema_property(raw_schema, "properties", "observations", "items")
    raw_edge = {
        "observation_id": "obs-1",
        "observation_kind": "DEPENDENCY_EDGE",
        "observation_type": "REPOSITORY_INSPECTION",
        "producer_identity": "schema-test",
        "producer_authority_class": "REPOSITORY_OBSERVER",
        "source_reference": repository_source,
        "repository_visible": True,
        "fact": "DEPENDENCY_EDGE_OBSERVED",
        "structured_value": {
            "edge_id": "edge-1",
            "from": "node-a",
            "to": "node-b",
        },
    }
    _require(
        not _schema_accepts(raw_item_schema, raw_edge, root=raw_schema),
        "raw schema condition does not semantically require exact dependency-edge binding",
    )
    raw_edge["structured_value"]["edge_class"] = "PROFILE_REALIZES"
    raw_edge["fact"] = "A dependency relation was seen during inspection"
    _require(
        not _schema_accepts(raw_item_schema, raw_edge, root=raw_schema),
        "raw schema accepts an unbounded semantic paraphrase",
    )

    reviewer_evidence = _schema_reference("REVIEWER_EVIDENCE")
    reviewer_evidence_two = {
        **_schema_reference("REVIEWER_EVIDENCE"),
        "path": "evidence/example-two.json",
    }
    qualified_reviewer: dict[str, Any] = {
        "protocol": "nk-h11-reviewer-reproducer-qualification/1",
        "experiment_id": EXPERIMENT_ID,
        "source_plan_id": PLAN_ID,
        "source_plan_sha256": PLAN_SHA256,
        "reviewer_identity_status": "ESTABLISHED",
        "reviewer_identity": "schema-test-reviewer",
        "reviewer_role": "REVIEWER",
        "authorship_relation": "NOT_AUTHOR_OF_PREREGISTRATION_OR_FROZEN_RUBRIC",
        "custody_relation": "INDEPENDENT_FOR_DECLARED_SCOPE",
        "conflicts": [],
        "repository_visibility": "EVIDENCE_VISIBLE",
        "private_implementation_state_used": False,
        "independence_basis": [
            {
                "basis_type": "ORGANIZATIONAL_SEPARATION",
                "evidence_reference": reviewer_evidence,
            },
            {
                "basis_type": "INDEPENDENT_EVIDENCE_CUSTODY",
                "evidence_reference": reviewer_evidence_two,
            },
        ],
        "evidence_references": [reviewer_evidence, reviewer_evidence_two],
        "qualification_result": "QUALIFIED",
    }
    _require(
        _schema_accepts(reviewer_schema, qualified_reviewer),
        "reviewer schema rejects its qualifying reference instance",
    )
    reviewer_self_review = dict(qualified_reviewer)
    reviewer_self_review["custody_relation"] = "SAME_CUSTODY"
    reviewer_self_review["conflicts"] = ["SELF_REVIEW"]
    _require(
        not _schema_accepts(reviewer_schema, reviewer_self_review),
        "reviewer schema condition accepts same-custody self-review",
    )
    reviewer_substitute = dict(qualified_reviewer)
    reviewer_substitute["independence_basis"] = ["CI_SUCCESS", "AUTOMATED_VALIDATOR"]
    _require(
        not _schema_accepts(reviewer_schema, reviewer_substitute),
        "reviewer schema condition accepts non-qualifying independence substitutes",
    )

    semantic_reference_types = (
        "RAW_OBSERVATIONS",
        "DEPENDENCY_GRAPH",
        "REVIEWER_QUALIFICATION",
    )
    semantic_instance: dict[str, Any] = {
        "protocol": "nk-h11-semantic-adjudication/1",
        "experiment_id": EXPERIMENT_ID,
        "source_plan_id": PLAN_ID,
        "source_plan_sha256": PLAN_SHA256,
        "input_policy": "REPOSITORY_VISIBLE_FROZEN_INPUTS_ONLY",
        "raw_observation_record": _schema_reference(semantic_reference_types[0]),
        "dependency_graph_record": {
            **_schema_reference(semantic_reference_types[1]),
            "path": "evidence/graph.json",
        },
        "reviewer_reproducer_qualification_record": {
            **_schema_reference(semantic_reference_types[2]),
            "path": "evidence/reviewer.json",
        },
        "adjudicator_identity": "schema-test-reviewer",
        "adjudicator_role": "REVIEWER",
        "adjudicator_authority_class": "QUALIFYING_INDEPENDENT_REVIEWER",
        "subject_private_state_used": False,
        "leakage_rubric": {
            "classes": LEAKAGE_CLASSES,
            "hard_failure_class": "UNJUSTIFIED_CANON_DEPENDENCY",
            "support_threshold": SUPPORT_THRESHOLD,
        },
        "hard_refutation": HARD_REFUTATION,
        "mandatory_profile_leakage_count": 0,
        "unjustified_canon_dependency_count": 0,
        "independence_qualified": True,
        "outcome": "SUPPORTED_FOR_SCOPE",
        "rationale": "schema behavior fixture",
        "declared_gaps": [],
    }
    _require(
        _schema_accepts(semantic_schema, semantic_instance),
        "semantic schema rejects its scoped-support reference instance",
    )
    for field, invalid_value in (
        ("independence_qualified", False),
        ("mandatory_profile_leakage_count", 1),
        ("unjustified_canon_dependency_count", 1),
        ("declared_gaps", ["missing evidence"]),
    ):
        invalid_semantic = dict(semantic_instance)
        invalid_semantic[field] = invalid_value
        _require(
            not _schema_accepts(semantic_schema, invalid_semantic),
            f"semantic schema condition accepts invalid scoped support: {field}",
        )
    hard_failure = dict(semantic_instance)
    hard_failure["outcome"] = "WEAKENED"
    hard_failure["unjustified_canon_dependency_count"] = 1
    _require(
        not _schema_accepts(semantic_schema, hard_failure),
        "semantic schema permits a hard-failure count without REFUTED",
    )
    false_refutation = dict(semantic_instance)
    false_refutation["outcome"] = "REFUTED"
    _require(
        not _schema_accepts(semantic_schema, false_refutation),
        "semantic schema permits REFUTED without a hard-failure count",
    )


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


def _require_exact_keys(value: Any, keys: set[str], label: str) -> Mapping[str, Any]:
    _require(isinstance(value, Mapping), f"{label} must be an object")
    _require(set(value) == keys, f"{label} fields must be exactly {sorted(keys)}")
    return value


def _validate_raw_structured_value(observation: Mapping[str, Any], label: str) -> None:
    kind = observation.get("observation_kind")
    value = observation.get("structured_value")
    _require(observation.get("fact") == RAW_FACT_TOKENS.get(str(kind)), f"{label} fact must be the neutral token for {kind}")
    if kind == "BUNDLE_VERIFICATION":
        value = _require_exact_keys(
            value,
            {"bundle_id", "manifest_path", "exact_bundle_verified", "verifier_exit_code", "verified_artifact_count"},
            f"{label} structured value",
        )
        _require(isinstance(value.get("bundle_id"), str) and value.get("bundle_id"), f"{label} bundle ID required")
        _require(isinstance(value.get("manifest_path"), str) and value.get("manifest_path"), f"{label} manifest path required")
        _require(isinstance(value.get("exact_bundle_verified"), bool), f"{label} exact verification flag required")
        _require(isinstance(value.get("verifier_exit_code"), int) and not isinstance(value.get("verifier_exit_code"), bool), f"{label} verifier exit code required")
        _require(isinstance(value.get("verified_artifact_count"), int) and not isinstance(value.get("verified_artifact_count"), bool) and value.get("verified_artifact_count", -1) >= 0, f"{label} verified artifact count required")
    elif kind == "MANIFEST_IDENTITY":
        value = _require_exact_keys(value, {"bundle_id", "manifest_path", "manifest_sha256"}, f"{label} structured value")
        _require(isinstance(value.get("bundle_id"), str) and value.get("bundle_id"), f"{label} bundle ID required")
        _require(isinstance(value.get("manifest_path"), str) and value.get("manifest_path"), f"{label} manifest path required")
        _require(isinstance(value.get("manifest_sha256"), str) and re.fullmatch(r"[0-9a-f]{64}", value["manifest_sha256"]) is not None, f"{label} manifest digest invalid")
    elif kind == "ARTIFACT_INVENTORY":
        value = _require_exact_keys(value, {"bundle_id", "artifact_count", "inventory_sha256"}, f"{label} structured value")
        _require(isinstance(value.get("bundle_id"), str) and value.get("bundle_id"), f"{label} bundle ID required")
        _require(isinstance(value.get("artifact_count"), int) and not isinstance(value.get("artifact_count"), bool) and value.get("artifact_count", -1) >= 0, f"{label} artifact count invalid")
        _require(isinstance(value.get("inventory_sha256"), str) and re.fullmatch(r"[0-9a-f]{64}", value["inventory_sha256"]) is not None, f"{label} inventory digest invalid")
    elif kind == "DEPENDENCY_EDGE":
        value = _require_exact_keys(value, {"edge_id", "from", "to", "edge_class"}, f"{label} structured value")
        for key in ("edge_id", "from", "to"):
            _require(isinstance(value.get(key), str) and value.get(key), f"{label} {key} required")
        _require(value.get("edge_class") in EDGE_CLASSES, f"{label} edge class invalid")
    elif kind == "SOURCE_REFERENCE":
        value = _require_exact_keys(value, {"path", "sha256"}, f"{label} structured value")
        _require(isinstance(value.get("path"), str) and value.get("path"), f"{label} source path required")
        _require(isinstance(value.get("sha256"), str) and re.fullmatch(r"[0-9a-f]{64}", value["sha256"]) is not None, f"{label} source digest invalid")
    elif kind == "MECHANISM_CLASSIFICATION_INPUT":
        value = _require_exact_keys(value, {"mechanism_name", "dependency_edge_id"}, f"{label} structured value")
        _require(value.get("mechanism_name") in MANDATORY_MECHANISMS, f"{label} mechanism identity invalid")
        _require(isinstance(value.get("dependency_edge_id"), str) and value.get("dependency_edge_id"), f"{label} dependency edge ID required")
    elif kind == "REVIEWER_IDENTITY_EVIDENCE":
        value = _require_exact_keys(value, {"identity", "role"}, f"{label} structured value")
        _require(isinstance(value.get("identity"), str) and value.get("identity"), f"{label} reviewer identity required")
        _require(value.get("role") in {"REVIEWER", "REPRODUCER", "REVIEWER_AND_REPRODUCER"}, f"{label} reviewer role invalid")
    elif kind == "INDEPENDENCE_EVIDENCE":
        value = _require_exact_keys(value, {"basis_type"}, f"{label} structured value")
        _require(value.get("basis_type") in INDEPENDENCE_BASIS_TYPES, f"{label} independence basis invalid")
    elif kind == "MISSING_DATA":
        value = _require_exact_keys(value, {"missing_id", "effect_on_visibility"}, f"{label} structured value")
        _require(isinstance(value.get("missing_id"), str) and value.get("missing_id"), f"{label} missing-data ID required")
        _require(value.get("effect_on_visibility") in {"MATERIAL", "NON_MATERIAL"}, f"{label} visibility effect invalid")
    else:
        raise H11AdmissionError(f"{label} unsupported observation kind")


def _require_externally_authenticated_independence() -> None:
    """The final, unconditional independence stop for QUALIFIED_FOR_H11_REVIEW_ROLE.

    Everything checked earlier in `_validate_reviewer_record`'s QUALIFIED branch
    is repository-local: distinct issuer labels, distinct commit-author
    identities, distinct evidence artifacts. None of it is proof of a distinct
    real-world actor. A single operator can set two different
    `git config user.email` values in the same clone (the prior fixture did
    exactly this) and satisfy every structural check while remaining the sole
    author of both attestations; a locally generated GPG/SSH signing key has
    the identical self-assertion problem. Genuine independence requires
    provenance the subject cannot self-assert — e.g. a GitHub-verified commit
    signature or a protected PR review tied to a distinct authenticated GitHub
    account — which this offline, Git-only validator does not check. Until
    that externally authenticated binding exists, QUALIFIED_FOR_H11_REVIEW_ROLE
    must remain unreachable through this evidence contract: the earlier checks
    are retained as repository-local provenance hygiene (and as the structure
    a future externally authenticated check would build on), not as proof of
    independence, so qualification fails closed unconditionally here.

    Kept as its own function and called unconditionally by production code so
    that tests can isolate it: patching only this stop (instead of all of
    `_validate_reviewer_record`) lets a test still exercise every structural
    reviewer check plus this final independence stop, while reaching
    downstream semantic/evidence guards for its own target assertion.
    """
    raise H11AdmissionError(
        "qualification_result=QUALIFIED cannot be established by this evidence "
        "contract: repository-local Git authorship (commit author identity or a "
        "locally generated signing key) is self-assertable by a single actor and "
        "is not proof of a distinct, externally authenticated independent "
        "reviewer/custodian. Qualification must remain NOT_ESTABLISHED until "
        "externally authenticated provenance is added."
    )


def _validate_reviewer_record(
    repo: Path,
    reviewer: Mapping[str, Any],
    reviewer_schema: Mapping[str, Any],
) -> None:
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
        _require(len(independence_basis) >= 2, "qualified reviewer requires multiple independent evidence bases")
        _require(len(evidence_references) >= 2, "qualified reviewer requires at least two evidence references")
        basis_types: set[str] = set()
        basis_reference_keys: set[str] = set()
        core_issuers: set[str] = set()
        core_issuer_commit_authors: set[str] = set()
        subject_authorship_email = _commit_author_email(repo, PLAN_MERGE)
        evidence_record_schema = _schema_property(
            reviewer_schema,
            "$defs",
            "independenceEvidenceRecord",
        )
        for index, basis in enumerate(independence_basis):
            basis = _require_exact_keys(
                basis,
                {"basis_type", "evidence_reference"},
                f"qualified reviewer independence basis {index}",
            )
            basis_type = basis.get("basis_type")
            _require(basis_type in INDEPENDENCE_BASIS_TYPES, f"qualified reviewer independence basis {index} type invalid")
            _require(basis_type not in basis_types, "qualified reviewer independence basis types must be unique")
            basis_types.add(str(basis_type))
            evidence_reference = basis.get("evidence_reference")
            evidence_record = _load_referenced_json(
                repo,
                evidence_reference,
                expected_type="REVIEWER_EVIDENCE",
                label=f"qualified reviewer independence basis {index} evidence",
            )
            _require(
                _schema_accepts(
                    evidence_record_schema,
                    evidence_record,
                    root=reviewer_schema,
                ),
                f"qualified reviewer independence basis {index} evidence is not a structured attestation",
            )
            _require(
                evidence_record.get("protocol") == INDEPENDENCE_EVIDENCE_PROTOCOL,
                f"qualified reviewer independence basis {index} evidence protocol drift",
            )
            _require(
                evidence_record.get("experiment_id") == EXPERIMENT_ID
                and evidence_record.get("source_plan_id") == PLAN_ID
                and evidence_record.get("source_plan_sha256") == PLAN_SHA256,
                f"qualified reviewer independence basis {index} evidence plan binding drift",
            )
            _require(
                evidence_record.get("reviewer_identity") == reviewer.get("reviewer_identity"),
                f"qualified reviewer independence basis {index} evidence identity mismatch",
            )
            _require(
                evidence_record.get("basis_type") == basis_type,
                f"qualified reviewer independence basis {index} evidence type mismatch",
            )
            _require(
                evidence_record.get("attested_authorship_relation") == reviewer.get("authorship_relation")
                and evidence_record.get("attested_custody_relation") == reviewer.get("custody_relation")
                and evidence_record.get("attested_conflicts") == conflicts
                and evidence_record.get("attested_private_implementation_state_used")
                == reviewer.get("private_implementation_state_used")
                and evidence_record.get("attested_repository_visibility")
                == reviewer.get("repository_visibility"),
                f"qualified reviewer independence basis {index} evidence contradicts the qualification record",
            )
            issuer = evidence_record.get("evidence_issuer_identity")
            _require(
                isinstance(issuer, str)
                and issuer
                and issuer != reviewer.get("reviewer_identity"),
                f"qualified reviewer independence basis {index} requires a non-self issuer",
            )
            required_issuer_role = CORE_INDEPENDENCE_ISSUER_ROLES.get(str(basis_type))
            if required_issuer_role is not None:
                _require(
                    evidence_record.get("evidence_issuer_role") == required_issuer_role,
                    f"qualified reviewer independence basis {index} issuer role mismatch",
                )
                core_issuers.add(issuer)
                commit_author_email = _commit_author_email(
                    repo, str(evidence_reference.get("git_commit"))
                )
                _require(
                    commit_author_email != subject_authorship_email,
                    f"qualified reviewer independence basis {index} evidence cannot be "
                    "authored by the same Git identity that authored the frozen H11 "
                    "preregistration",
                )
                core_issuer_commit_authors.add(commit_author_email)
            _require(
                not _contains_semantic_verdict(evidence_record),
                f"qualified reviewer independence basis {index} evidence cannot carry an H11 verdict",
            )
            reference_key = json.dumps(evidence_reference, sort_keys=True, separators=(",", ":"))
            _require(
                reference_key not in basis_reference_keys,
                "qualified reviewer independence evidence artifacts must be distinct",
            )
            basis_reference_keys.add(reference_key)
        _require(
            {"ORGANIZATIONAL_SEPARATION", "INDEPENDENT_EVIDENCE_CUSTODY"}.issubset(basis_types),
            "qualified reviewer must prove organizational separation and independent evidence custody",
        )
        _require(
            len(core_issuers) == 2,
            "organizational-separation and custody attestations require distinct issuers",
        )
        _require(
            len(core_issuer_commit_authors) == 2,
            "organizational-separation and custody attestations must be committed by two "
            "distinct Git author identities, not merely labeled with two distinct issuer strings",
        )
        declared_reference_keys = {
            json.dumps(reference, sort_keys=True, separators=(",", ":"))
            for reference in evidence_references
        }
        _require(
            declared_reference_keys == basis_reference_keys,
            "qualified reviewer evidence references must exactly enumerate the independence attestations",
        )
        _require(
            not _contains_semantic_verdict(independence_basis)
            and not any(substitute in json.dumps(independence_basis) for substitute in NON_QUALIFYING_SUBSTITUTES),
            "qualified reviewer cannot use non-qualifying independence substitutes",
        )
        _require_externally_authenticated_independence()


def validate_h11_evidence_bundle(
    repo: Path,
    *,
    dependency_graph: Mapping[str, Any],
    raw_observations: Mapping[str, Any],
    semantic_adjudication: Mapping[str, Any],
    reviewer_record: Mapping[str, Any],
    semantic_adjudication_path: str,
    dependency_schema: Mapping[str, Any] | None = None,
    raw_schema: Mapping[str, Any] | None = None,
    semantic_schema: Mapping[str, Any] | None = None,
    reviewer_schema: Mapping[str, Any] | None = None,
) -> None:
    """Validate a future H11 evidence chain without executing or adjudicating H11.

    This is fail-closed validation machinery only. Tests call it with synthetic fixtures;
    repository admission remains blocked and no real H11 evidence bundle exists yet.
    """
    repo = repo.resolve()
    dependency_schema = (
        dict(dependency_schema)
        if dependency_schema is not None
        else _load(repo / DEPENDENCY_SCHEMA_PATH, "H11 dependency graph schema")
    )
    raw_schema = (
        dict(raw_schema)
        if raw_schema is not None
        else _load(repo / RAW_SCHEMA_PATH, "H11 raw observation schema")
    )
    semantic_schema = (
        dict(semantic_schema)
        if semantic_schema is not None
        else _load(repo / SEMANTIC_SCHEMA_PATH, "H11 semantic adjudication schema")
    )
    reviewer_schema = (
        dict(reviewer_schema)
        if reviewer_schema is not None
        else _load(repo / REVIEWER_SCHEMA_PATH, "H11 reviewer qualification schema")
    )
    for label, schema, record in (
        ("dependency graph", dependency_schema, dependency_graph),
        ("raw observations", raw_schema, raw_observations),
        ("semantic adjudication", semantic_schema, semantic_adjudication),
        ("reviewer qualification", reviewer_schema, reviewer_record),
    ):
        _require(
            _schema_accepts(schema, record),
            f"{label} violates its declared JSON Schema",
        )
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
        _validate_raw_structured_value(observation, f"raw observation {observation_id}")
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
    obligation_nodes: dict[str, list[str]] = {
        obligation_id: [] for obligation_id in FROZEN_OBLIGATION_IDS
    }
    class_counts = {node_class: 0 for node_class in NODE_CLASSES}
    for index, node in enumerate(nodes):
        _require(isinstance(node, Mapping), f"dependency node {index} must be an object")
        node_id = node.get("node_id")
        _require(isinstance(node_id, str) and node_id, f"dependency node {index} ID required")
        _require(node_id not in node_by_id, f"duplicate dependency node ID: {node_id}")
        node_class = node.get("node_class")
        _require(node_class in NODE_CLASSES, f"dependency node {node_id} class invalid")
        class_counts[str(node_class)] += 1
        _validate_repository_reference(
            repo,
            node.get("source_reference"),
            expected_type="REPOSITORY_SOURCE",
            label=f"dependency node {node_id} source",
            frozen_at=(
                FROZEN_REVIEW_SUBJECT
                if node_class
                in {
                    "ARCHITECTURE_OBLIGATION",
                    "LABORATORY_EVIDENCE",
                    "PROFILE_MECHANISM",
                }
                else None
            ),
        )
        if node_class == "ARCHITECTURE_OBLIGATION":
            obligation_id = node.get("obligation_id")
            _require(
                obligation_id in obligation_nodes,
                f"dependency node {node_id} frozen obligation identity invalid",
            )
            obligation_nodes[str(obligation_id)].append(node_id)
        else:
            _require(
                "obligation_id" not in node,
                f"dependency node {node_id} cannot claim a frozen obligation identity",
            )
        if node_class == "PROFILE_MECHANISM":
            mechanism = node.get("mechanism_name")
            _require(mechanism in profile_nodes, f"dependency node {node_id} mechanism invalid")
            profile_nodes[str(mechanism)].append(node_id)
        else:
            _require(
                "mechanism_name" not in node,
                f"dependency node {node_id} cannot claim a profile mechanism identity",
            )
        node_by_id[node_id] = node

    for node_class in NODE_CLASSES:
        _require(class_counts[node_class] > 0, f"dependency graph missing required node class: {node_class}")
    for obligation_id, obligation_node_ids in obligation_nodes.items():
        _require(
            len(obligation_node_ids) == 1,
            f"dependency graph requires exactly one {obligation_id} Architecture obligation node",
        )

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
        _require(from_id != to_id, f"dependency edge {edge_id} cannot be a self-loop")
        connected_nodes.update((str(from_id), str(to_id)))
        edge_class = edge.get("edge_class")
        _require(edge_class in EDGE_CLASSES, f"dependency edge {edge_id} class invalid")
        leakage_class = edge.get("leakage_class")
        _require(leakage_class in LEAKAGE_CLASSES, f"dependency edge {edge_id} leakage class invalid")
        structurally_unjustified = (
            node_by_id[str(from_id)].get("node_class") == "ARCHITECTURE_OBLIGATION"
            and node_by_id[str(to_id)].get("node_class") == "PROFILE_MECHANISM"
            and edge_class == "ARCHITECTURE_REQUIRES"
        )
        _require(
            not structurally_unjustified or leakage_class == "UNJUSTIFIED_CANON_DEPENDENCY",
            f"dependency edge {edge_id} structurally requires a profile mechanism and must be classified as UNJUSTIFIED_CANON_DEPENDENCY",
        )
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
                and binding.get("to") == to_id
                and binding.get("edge_class") == edge_class,
                f"dependency edge {edge_id} raw reference {observation_id} is not bound to the exact edge",
            )

    for mechanism, mechanism_nodes in profile_nodes.items():
        _require(len(mechanism_nodes) == 1, f"covered mechanism {mechanism!r} must have exactly one PROFILE_MECHANISM node")
        _require(mechanism_nodes[0] in connected_nodes, f"covered mechanism {mechanism!r} has no dependency edge")
    _require(
        connected_nodes == set(node_by_id),
        "every dependency node must participate in at least one evidence-bearing edge",
    )

    _validate_reviewer_record(repo, reviewer_record, reviewer_schema)
    raw_ref = semantic_adjudication.get("raw_observation_record")
    graph_ref = semantic_adjudication.get("dependency_graph_record")
    reviewer_ref = semantic_adjudication.get("reviewer_reproducer_qualification_record")
    references = [raw_ref, graph_ref, reviewer_ref]
    reference_paths = [reference.get("path") if isinstance(reference, Mapping) else None for reference in references]
    _require(len(set(reference_paths)) == 3 and None not in reference_paths, "semantic input artifacts must be three distinct paths")
    _require(semantic_adjudication_path not in reference_paths, "semantic adjudication cannot reference itself as an input")
    loaded_raw = _load_referenced_json(
        repo, raw_ref, expected_type="RAW_OBSERVATIONS", label="semantic raw input"
    )
    loaded_graph = _load_referenced_json(
        repo, graph_ref, expected_type="DEPENDENCY_GRAPH", label="semantic dependency input"
    )
    loaded_reviewer = _load_referenced_json(
        repo,
        reviewer_ref,
        expected_type="REVIEWER_QUALIFICATION",
        label="semantic reviewer input",
    )
    for label, schema, loaded, supplied in (
        ("semantic raw input", raw_schema, loaded_raw, raw_observations),
        ("semantic dependency input", dependency_schema, loaded_graph, dependency_graph),
        ("semantic reviewer input", reviewer_schema, loaded_reviewer, reviewer_record),
    ):
        _require(_schema_accepts(schema, loaded), f"{label} violates its declared JSON Schema")
        _require(
            _json_exact_equal(loaded, supplied),
            f"{label} does not match the supplied in-memory record with exact JSON types",
        )
    _require(semantic_adjudication.get("input_policy") == "REPOSITORY_VISIBLE_FROZEN_INPUTS_ONLY", "semantic input policy drift")
    _require(semantic_adjudication.get("subject_private_state_used") is False, "semantic adjudication cannot use private subject state")
    _require(reviewer_record.get("qualification_result") == "QUALIFIED", "semantic adjudication requires a qualifying independent reviewer")
    _require(semantic_adjudication.get("independence_qualified") is True, "semantic adjudication independence must be qualified")
    _require(
        semantic_adjudication.get("adjudicator_identity")
        == reviewer_record.get("reviewer_identity"),
        "semantic adjudicator identity must match the qualified reviewer",
    )
    _require(
        reviewer_record.get("reviewer_role")
        in {"REVIEWER", "REVIEWER_AND_REPRODUCER"}
        and semantic_adjudication.get("adjudicator_role")
        == reviewer_record.get("reviewer_role"),
        "semantic adjudicator role must match a qualified reviewer role",
    )
    _require(
        semantic_adjudication.get("adjudicator_authority_class")
        == "QUALIFYING_INDEPENDENT_REVIEWER",
        "semantic adjudicator authority must be independently qualified",
    )
    _require(semantic_adjudication.get("unjustified_canon_dependency_count") == unjustified_count, "semantic unjustified dependency count does not match graph")
    _require(
        semantic_adjudication.get("mandatory_profile_leakage_count") == len(unjustified_profile_mechanisms),
        "semantic mandatory-profile leakage count does not match implicated mechanisms",
    )
    _require(
        (unjustified_count > 0)
        == (semantic_adjudication.get("outcome") == "REFUTED"),
        "UNJUSTIFIED_CANON_DEPENDENCY and REFUTED must imply each other",
    )
    _require(
        semantic_adjudication.get("outcome") != "NOT_TESTED",
        "a submitted evidence bundle with a schema-valid, qualified independent adjudicator "
        "cannot report NOT_TESTED; NOT_TESTED means no qualifying execution/adjudication occurred",
    )
    if semantic_adjudication.get("outcome") == "SUPPORTED_FOR_SCOPE":
        _require(unjustified_count == 0, "SUPPORTED_FOR_SCOPE cannot contain UNJUSTIFIED_CANON_DEPENDENCY")
        _require(semantic_adjudication.get("mandatory_profile_leakage_count") == 0, "SUPPORTED_FOR_SCOPE requires zero mandatory profile leakage")
        _require(raw_observations.get("missing_data") == [], "SUPPORTED_FOR_SCOPE requires complete raw evidence")
        _require(dependency_graph.get("declared_gaps") == [], "SUPPORTED_FOR_SCOPE requires a gap-free dependency graph")
        _require(semantic_adjudication.get("declared_gaps") == [], "SUPPORTED_FOR_SCOPE requires no adjudication gaps")
        _require(
            not any(observation.get("observation_kind") == "MISSING_DATA" for observation in observations),
            "SUPPORTED_FOR_SCOPE cannot consume a missing-data observation",
        )
        bundle_verifications = [
            observation
            for observation in observations
            if observation.get("observation_kind") == "BUNDLE_VERIFICATION"
        ]
        _require(len(bundle_verifications) == 1, "SUPPORTED_FOR_SCOPE requires exactly one bundle-verification observation")
        bundle_value = bundle_verifications[0].get("structured_value")
        bundle_observation = bundle_verifications[0]
        _require(isinstance(bundle_value, Mapping), "bundle-verification observation value required")
        _require(
            bundle_observation.get("observation_type") == "TOOL_OUTPUT"
            and bundle_observation.get("producer_authority_class") == "AUTOMATED_VALIDATOR",
            "bundle verification must come from the repository verifier tool",
        )
        bundle_source = bundle_observation.get("source_reference")
        _require(
            isinstance(bundle_source, Mapping)
            and bundle_source.get("path") == BUNDLE_MANIFEST,
            "bundle-verification observation must reference the frozen manifest",
        )
        _validate_repository_reference(
            repo,
            bundle_source,
            expected_type="REPOSITORY_SOURCE",
            label="bundle-verification manifest source",
            frozen_at=FROZEN_REVIEW_SUBJECT,
        )
        _require(bundle_value.get("bundle_id") == BUNDLE_ID, "bundle-verification subject ID drift")
        _require(bundle_value.get("manifest_path") == BUNDLE_MANIFEST, "bundle-verification manifest drift")
        _require(bundle_value.get("exact_bundle_verified") is True, "SUPPORTED_FOR_SCOPE requires exact bundle verification")
        _require(bundle_value.get("verifier_exit_code") == 0, "SUPPORTED_FOR_SCOPE requires a successful verifier exit")
        verified_artifact_count = _verify_frozen_bundle(repo)
        _require(
            bundle_value.get("verified_artifact_count") == verified_artifact_count,
            "bundle-verification observation does not match actual verifier output",
        )


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
    _require(node_props.get("obligation_id", {}).get("enum") == FROZEN_OBLIGATION_IDS, "frozen H11 obligation node inventory drift")
    node_rules = _schema_property(dep_props, "nodes", "items", "allOf")
    _require(isinstance(node_rules, list) and node_rules, "PROFILE_MECHANISM nodes must conditionally require mechanism_name")
    node_rule_text = json.dumps(node_rules, sort_keys=True)
    _require('"PROFILE_MECHANISM"' in node_rule_text, "PROFILE_MECHANISM condition drift")
    _require('"then": {"required": ["mechanism_name"]}' in node_rule_text, "PROFILE_MECHANISM must require mechanism_name")
    _require('"ARCHITECTURE_OBLIGATION"' in node_rule_text, "ARCHITECTURE_OBLIGATION condition drift")
    _require('"then": {"required": ["obligation_id"]}' in node_rule_text, "ARCHITECTURE_OBLIGATION must require obligation_id")
    dep_reference_required = _schema_property(dependency_schema, "$defs", "repositoryArtifactReference", "required")
    _require("git_commit" in dep_reference_required, "dependency source references must be Git-anchored")

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
        "fact",
        "structured_value",
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
        '"required": ["edge_id", "from", "to", "edge_class"]',
    ):
        _require(required_literal in raw_rule_text, f"dependency-edge raw binding invariant missing: {required_literal}")
    _require(
        not _contains_key(raw_schema, {"outcome", "h11_outcome", "semantic_judgment", "adjudication"}),
        "raw observation schema must not contain final H11 semantic judgment fields",
    )
    raw_text = json.dumps(raw_schema, sort_keys=True)
    for outcome in A10_OUTCOMES:
        _require(outcome not in raw_text, f"raw observation schema must not encode final A10 outcome: {outcome}")
    raw_reference_required = _schema_property(raw_schema, "$defs", "repositoryArtifactReference", "required")
    _require("git_commit" in raw_reference_required, "raw source references must be Git-anchored")

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
        "adjudicator_identity",
        "adjudicator_role",
        "adjudicator_authority_class",
        "subject_private_state_used",
        "mandatory_profile_leakage_count",
        "unjustified_canon_dependency_count",
        "independence_qualified",
        "outcome",
        "declared_gaps",
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
        '"declared_gaps": {"maxItems": 0}',
        '"outcome": {"const": "REFUTED"}',
        '"unjustified_canon_dependency_count": {"minimum": 1}',
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
    evidence_record_schema = _schema_property(reviewer_schema, "$defs", "independenceEvidenceRecord")
    _require(
        evidence_record_schema.get("additionalProperties") is False
        and evidence_record_schema.get("properties", {}).get("protocol", {}).get("const")
        == INDEPENDENCE_EVIDENCE_PROTOCOL,
        "reviewer independence evidence must be a closed structured attestation",
    )
    reviewer_rules = reviewer_schema.get("allOf")
    _require(isinstance(reviewer_rules, list) and reviewer_rules, "qualified reviewer conditional constraints required")
    reviewer_rule_text = json.dumps(reviewer_rules, sort_keys=True)
    for required_literal in (
        '"custody_relation": {"const": "INDEPENDENT_FOR_DECLARED_SCOPE"}',
        '"conflicts": {"maxItems": 0}',
        '"evidence_references": {"minItems": 2, "uniqueItems": true}',
    ):
        _require(required_literal in reviewer_rule_text, f"qualified reviewer invariant missing: {required_literal}")
    reviewer_reference_required = _schema_property(reviewer_schema, "$defs", "evidenceReference", "required")
    _require("git_commit" in reviewer_reference_required, "reviewer evidence references must be Git-anchored")
    semantic_reference_required = _schema_property(semantic_schema, "$defs", "artifactReference", "required")
    _require("git_commit" in semantic_reference_required, "semantic artifact references must be Git-anchored")
    _validate_schema_behavior(
        dependency_schema=dependency_schema,
        raw_schema=raw_schema,
        semantic_schema=semantic_schema,
        reviewer_schema=reviewer_schema,
    )

    reviewer = _choose(reviewer_override, repo / REVIEWER_RECORD_PATH, "H11 reviewer/reproducer qualification record")
    _validate_reviewer_record(repo, reviewer, reviewer_schema)
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
