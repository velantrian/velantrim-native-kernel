#!/usr/bin/env python3
"""Validate the frozen A10-H11 laboratory/Canon preregistration."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Mapping

PLAN_PATH = Path("docs/research/H11_PREREGISTRATION.json")
EN_PATH = Path("docs/research/H11_PREREGISTRATION.md")
RU_PATH = Path("docs/research/H11_PREREGISTRATION.ru.md")
SELECTION_PATH = Path("docs/research/H11_FAMILY_SELECTION.json")
EVIDENCE_MANIFEST = Path("evidence/c5/2026-08-08-adr0023/manifest.json")
EVIDENCE_VERIFIER = Path("tools/evidence/verify_bundle.py")
A9_PATH = Path("docs/A9_REFERENCE_LABORATORY_BOUNDARY.md")

PROTOCOL = "nk-h11-preregistration/1"
PLAN_ID = "H11-001-c5-lab-canon-separation-v1"
SELECTION_ID = "RFS-001-a10-h11-preregistration-selection-v1"
SELECTION_MERGE = "bcd3b3f6c9d898315c93e5d24b5d0e02c95508cc"
RAVP_MERGE = "edc0501d71a827462aafd1ac4497920a719a4519"
BUNDLE_ID = "native-kernel/c5/2026-08-08-adr0023"
NEXT_GATE = "A10_H11_EXECUTION_ADMISSION"
ALLOWED_OUTCOMES = ["SUPPORTED_FOR_SCOPE", "WEAKENED", "REFUTED", "INDETERMINATE", "NOT_TESTED"]
OBLIGATIONS = {"H11-O01", "H11-O02", "H11-O03", "H11-O04"}
MANDATORY_MECHANISMS = {
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
}


class H11PreregistrationError(ValueError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise H11PreregistrationError(message)


def _load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise H11PreregistrationError(f"cannot load {path}: {exc}") from exc
    _require(isinstance(value, dict), f"{path} root must be an object")
    return value


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    _require(spec is not None and spec.loader is not None, f"cannot load module {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _reject_execution_authority(value: Any, path: str = "root") -> None:
    if isinstance(value, Mapping):
        for key, item in value.items():
            child = f"{path}.{key}"
            lowered = key.lower()
            if "implementation_authorized" in lowered or "execution_authorized" in lowered:
                _require(item is False, f"{child} must remain false in preregistration scope")
            _reject_execution_authority(item, child)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _reject_execution_authority(item, f"{path}[{index}]")


def validate(repo: Path, plan_override: Mapping[str, Any] | None = None, *, verify_bundle: bool = True) -> None:
    repo = repo.resolve()
    plan = dict(plan_override) if plan_override is not None else _load(repo / PLAN_PATH)
    selection = _load(repo / SELECTION_PATH)

    _require(plan.get("protocol") == PROTOCOL, "H11 preregistration protocol drift")
    _require(plan.get("plan_id") == PLAN_ID, "H11 preregistration identity drift")
    _require(plan.get("state") == "PREREGISTERED / EXECUTION_NOT_AUTHORIZED", "H11 plan must remain preregistered and non-executable")
    _require(plan.get("target_hypothesis") == "A10-H11", "H11 target drift")
    _require(plan.get("target_family_id") == "RAVP-H11-LAB-CANON-SEPARATION", "H11 family drift")
    _require(plan.get("hypothesis") == "Laboratory mechanisms can remain reproducible without becoming Architecture Canon.", "H11 exact hypothesis drift")
    _require(plan.get("architecture_position") == "STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL", "architecture position overclaim")
    _require(plan.get("architecture_snapshot_sha") == SELECTION_MERGE, "architecture snapshot must be frozen at H11 selection merge")
    _require(plan.get("experiment_identity") == "H11-001", "H11 experiment identity drift")

    selection_auth = plan.get("selection_authority")
    _require(isinstance(selection_auth, Mapping), "selection authority binding required")
    _require(selection_auth.get("selection_id") == SELECTION_ID, "selection identity binding drift")
    _require(selection_auth.get("selection_pr") == 126, "selection PR binding drift")
    _require(selection_auth.get("selection_merge_sha") == SELECTION_MERGE, "selection merge binding drift")
    _require(selection.get("selection_id") == SELECTION_ID and selection.get("selected_hypothesis") == "A10-H11", "repository H11 selection artifact drift")
    _require(selection.get("preregistration_authorized_by_this_package") is False, "selection package must remain non-self-authorizing")

    residual = plan.get("source_residual_plan")
    _require(isinstance(residual, Mapping) and residual.get("merge_sha") == RAVP_MERGE, "RAVP source binding drift")

    lab = plan.get("historical_laboratory_checkpoint_and_evidence_identity")
    _require(isinstance(lab, Mapping), "historical laboratory identity required")
    _require(lab.get("laboratory_role") == "BOUNDED_REFERENCE_LABORATORY", "laboratory role drift")
    _require(lab.get("architecture_boundary_model") == "nk-reference-laboratory-boundary/A9-draft-1", "A9 model binding drift")
    _require(lab.get("evidence_bundle_id") == BUNDLE_ID, "H11 evidence bundle identity drift")
    _require(lab.get("evidence_manifest_path") == str(EVIDENCE_MANIFEST), "H11 evidence manifest path drift")
    _require(lab.get("checkpoint_count") == 2 and lab.get("artifact_count") == 8, "H11 exact laboratory inventory drift")
    _require(lab.get("historical_bundle_preserved") is True and lab.get("historical_bundle_rewrite_allowed") is False, "historical evidence immutability drift")
    checkpoints = lab.get("checkpoint_roles")
    _require(isinstance(checkpoints, list) and len(checkpoints) == 2, "H11 requires exactly two frozen checkpoints")
    _require([item.get("role") for item in checkpoints if isinstance(item, Mapping)] == ["remediation_pr_head", "remediation_final_main"], "H11 checkpoint role drift")
    _require(checkpoints[0].get("head_sha") == "ab7a203ce7ed8ec46c341bc4da9063d56f023338", "remediation PR checkpoint drift")
    _require(checkpoints[1].get("head_sha") == "675aa4b398a2fc0181dc71d38904a2d33a09f5f8", "final main checkpoint drift")

    reproduction = plan.get("exact_laboratory_reproduction_manifest")
    _require(isinstance(reproduction, Mapping), "exact laboratory reproduction manifest required")
    _require(reproduction.get("required_bundle_id") == BUNDLE_ID, "exact reproduction bundle drift")
    _require(reproduction.get("required_checkpoint_count") == 2 and reproduction.get("required_artifact_count") == 8, "exact reproduction count drift")
    _require(reproduction.get("required_report_files_per_artifact") == 6 and reproduction.get("required_scenarios_per_c5_report") == 18, "C5 exact report inventory drift")
    _require(reproduction.get("required_sqlite_floor") == "3.51.3", "SQLite evidence floor drift")
    _require(reproduction.get("architecture_authority_from_exactness") is False, "exact lab bytes must not become Architecture authority")

    obligations = plan.get("architecture_obligation_inventory")
    _require(isinstance(obligations, list), "H11 obligation inventory required")
    _require({item.get("obligation_id") for item in obligations if isinstance(item, Mapping)} == OBLIGATIONS, "H11 obligation inventory drift")

    graph = plan.get("mechanism_dependency_graph_schema")
    _require(isinstance(graph, Mapping), "mechanism dependency graph schema required")
    _require(set(graph.get("mandatory_profile_mechanisms_to_audit", [])) == MANDATORY_MECHANISMS, "mandatory profile mechanism audit inventory drift")
    _require("ARCHITECTURE_REQUIRES" in str(graph.get("forbidden_unqualified_edge")), "forbidden Canon dependency edge must remain explicit")

    rubric = plan.get("frozen_mechanism_leakage_rubric")
    _require(isinstance(rubric, Mapping), "frozen mechanism leakage rubric required")
    _require(set(rubric) >= {"LAB_ONLY", "PROFILE_SPECIFIC", "MEANING_LEVEL_JUSTIFIED", "UNJUSTIFIED_CANON_DEPENDENCY", "support_threshold", "hard_failure_class"}, "H11 leakage rubric incomplete")
    _require(rubric.get("hard_failure_class") == "UNJUSTIFIED_CANON_DEPENDENCY", "H11 hard failure class drift")
    _require("mandatory_profile_leakage_count == 0" in str(rubric.get("support_threshold")), "H11 support threshold drift")

    failures = plan.get("failure_conditions")
    _require(isinstance(failures, list) and len(failures) >= 6, "H11 failure conditions incomplete")
    failure_text = json.dumps(failures, ensure_ascii=False).lower()
    for marker in ("historical evidence", "architecture obligation", "semantic oracle", "laboratory-only", "architecture history", "dependency graph"):
        _require(marker in failure_text, f"H11 failure boundary missing: {marker}")
    _require("profile-specific c5 laboratory mechanism" in str(plan.get("hard_refutation", "")).lower(), "H11 hard refutation drift")

    _require(plan.get("grounding_mode") == "FROZEN_REPOSITORY_EVIDENCE_AND_ARCHITECTURE_SNAPSHOT_PLUS_QUALIFYING_INDEPENDENT_BOUNDARY_REVIEW", "H11 grounding mode drift")
    oracle = plan.get("semantic_oracle_authority")
    _require(isinstance(oracle, Mapping), "H11 semantic oracle required")
    _require(oracle.get("required_class") == "INDEPENDENT_SEMANTIC_ORACLE", "H11 semantic oracle independence drift")
    _require(oracle.get("architecture_authors_may_self_certify_h11") is False, "Architecture authors cannot self-certify H11")

    independence = plan.get("reviewer_reproducer_independence_basis")
    _require(isinstance(independence, Mapping), "reviewer/reproducer independence basis required")
    _require(independence.get("required_before_execution") is True, "independence must be required before execution")
    _require(independence.get("current_status") == "NOT_ESTABLISHED / MUST_BE_VERIFIED_AT_EXECUTION_ADMISSION", "current independence status must remain unestablished")
    _require(independence.get("no_qualifying_reviewer_outcome") == "BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER", "no-reviewer blocker drift")

    _require(plan.get("allowed_a10_outcome_vocabulary") == ALLOWED_OUTCOMES, "H11 A10 outcome vocabulary drift")
    adjudication = plan.get("adjudication_rules")
    _require(isinstance(adjudication, Mapping) and set(adjudication) == set(ALLOWED_OUTCOMES), "H11 adjudication rule inventory drift")
    _require("qualifying independent" in str(adjudication.get("SUPPORTED_FOR_SCOPE", "")).lower(), "H11 support must require qualifying independence")
    _require("hard_refutation" in str(adjudication.get("REFUTED", "")), "H11 refutation must bind the frozen hard refutation")
    _require("no qualifying execution" in str(adjudication.get("NOT_TESTED", "")).lower(), "H11 NOT_TESTED boundary drift")

    admission = plan.get("execution_admission")
    _require(isinstance(admission, Mapping), "H11 execution-admission gate required")
    _require(admission.get("required") is True and admission.get("next_gate_if_preregistered") == NEXT_GATE, "H11 next gate drift")
    _require(admission.get("implementation_authorized_by_this_plan") is False, "H11 preregistration cannot authorize implementation")
    _require(admission.get("execution_authorized_by_this_plan") is False, "H11 preregistration cannot authorize execution")
    _require(admission.get("requires_frozen_plan_digest") is True, "H11 admission must freeze the plan digest")
    _require(admission.get("requires_qualifying_independent_reviewer_reproducer") is True, "H11 admission must require qualifying independence")
    _reject_execution_authority(plan)

    _require(plan.get("runtime_expansion") == "FROZEN" and plan.get("product_runtime_thaw") is False, "runtime must remain frozen")
    _require(plan.get("production_authorized") is False and "DEFERRED" in str(plan.get("final_canon")), "Final Canon/production boundary drift")

    non_targets = json.dumps(plan.get("explicit_non_targets", []), ensure_ascii=False).lower()
    for marker in ("composition/federation", "universal future-substrate", "final canon", "issue #18", "issue #74", "track h"):
        _require(marker in non_targets, f"H11 explicit non-target missing: {marker}")

    a9 = (repo / A9_PATH).read_text(encoding="utf-8")
    for marker in (
        "bounded reference laboratory",
        "LABORATORY_ONLY_CONSTRAINT",
        "PROFILE_SPECIFIC_REALIZATION",
        "C5 — Bounded operational rehearsal",
        "laboratory evidence",
        "not architecture authority",
    ):
        _require(marker.lower() in a9.lower(), f"A9 H11 source boundary missing: {marker}")

    for relative in (EN_PATH, RU_PATH):
        text = (repo / relative).read_text(encoding="utf-8")
        for marker in (PLAN_ID, "A10-H11", BUNDLE_ID, "INDEPENDENT_SEMANTIC_ORACLE", "BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER", NEXT_GATE, "implementation_authorized_by_this_plan: false", "execution_authorized_by_this_plan: false", "A10-H11 ≠ composition/federation"):
            _require(marker in text, f"{relative}: missing frozen H11 marker: {marker}")

    if verify_bundle:
        verifier = _load_module(repo / EVIDENCE_VERIFIER, "h11_evidence_verifier")
        manifest = _load(repo / EVIDENCE_MANIFEST)
        try:
            verifier.validate(manifest, repo=repo)
        except Exception as exc:  # fail closed while preserving verifier error context
            raise H11PreregistrationError(f"frozen H11 laboratory bundle verification failed: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    try:
        validate(args.repo)
    except H11PreregistrationError as exc:
        print(f"H11 preregistration validation failed: {exc}", file=sys.stderr)
        return 1
    print("H11 preregistration valid; evidence_bundle=2_checkpoints/8_artifacts; independence=NOT_ESTABLISHED; execution=NOT_AUTHORIZED; runtime=FROZEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
