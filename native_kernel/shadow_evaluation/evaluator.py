from __future__ import annotations

import hashlib
import json
import os
import platform
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping

DATASET_VERSION = "nk-shadow-workload/1"
REPORT_VERSION = "nk-shadow-report/1"
RECEIPT_VERSION = "nk-shadow-receipt/1"
EXPECTED_C3_COUNTS = {"SUPPORTED": 45, "PARTIAL": 10, "UNSUPPORTED": 17, "FAILED": 0}
REQUIRED_LIMITATION_FRAGMENTS = (
    "not captured production traffic",
    "does not authorize authority promotion",
    "not live production shadowing",
    "not c5",
    "not production readiness",
)


class ShadowEvaluationError(RuntimeError):
    """Raised when the offline shadow contract cannot be evaluated safely."""


@dataclass(frozen=True)
class CaseComparison:
    case_id: str
    assertion_ids: tuple[str, ...]
    critical: bool
    matched: bool
    divergences: tuple[dict[str, Any], ...]
    allowed_differences: tuple[dict[str, Any], ...]
    latency_ratio: float
    comparison_digest: str


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_json(value: Any) -> str:
    return sha256_text(canonical_json(value))


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ShadowEvaluationError(f"cannot load JSON from {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ShadowEvaluationError(f"{path} must contain a JSON object")
    return value


def _path_value(value: Mapping[str, Any], dotted_path: str) -> Any:
    current: Any = value
    for part in dotted_path.split("."):
        if not isinstance(current, Mapping) or part not in current:
            raise ShadowEvaluationError(f"missing comparison field {dotted_path!r}")
        current = current[part]
    return current


def _validate_unique_strings(values: Any, label: str, *, allow_empty: bool = False) -> list[str]:
    if not isinstance(values, list) or (not values and not allow_empty):
        raise ShadowEvaluationError(f"{label} must be a non-empty list")
    if not all(isinstance(item, str) and item for item in values):
        raise ShadowEvaluationError(f"{label} must contain non-empty strings")
    if len(values) != len(set(values)):
        raise ShadowEvaluationError(f"{label} contains duplicates")
    return list(values)


def validate_c3_prerequisite(report: Mapping[str, Any]) -> dict[str, str]:
    if report.get("report_version") != "nk-equivalence-report/1":
        raise ShadowEvaluationError("C4 requires nk-equivalence-report/1 prerequisite evidence")
    if report.get("kernel_runtime_conformance") != "C3":
        raise ShadowEvaluationError("C4 prerequisite must be C3")
    if report.get("support_state") != "PARTIAL":
        raise ShadowEvaluationError("C4 prerequisite support_state must remain PARTIAL")
    rows = report.get("assertion_results")
    if not isinstance(rows, list) or len(rows) != 72:
        raise ShadowEvaluationError("C4 prerequisite must expose all 72 assertion results")
    statuses: dict[str, str] = {}
    counts = {key: 0 for key in EXPECTED_C3_COUNTS}
    for row in rows:
        if not isinstance(row, Mapping):
            raise ShadowEvaluationError("invalid C3 assertion row")
        assertion_id = row.get("assertion_id")
        status = row.get("status")
        if not isinstance(assertion_id, str) or not assertion_id:
            raise ShadowEvaluationError("C3 assertion result is missing assertion_id")
        if assertion_id in statuses:
            raise ShadowEvaluationError(f"duplicate C3 assertion result {assertion_id}")
        if status not in counts:
            raise ShadowEvaluationError(f"invalid C3 status for {assertion_id}: {status}")
        if assertion_id.startswith("NK-EPI-") and status != "UNSUPPORTED":
            raise ShadowEvaluationError("proposed NK-EPI assertions cannot be promoted by C4")
        statuses[assertion_id] = status
        counts[status] += 1
    if counts != EXPECTED_C3_COUNTS:
        raise ShadowEvaluationError(f"unexpected C3 assertion map: {counts}")
    return statuses


def validate_dataset(dataset: Mapping[str, Any], c3_statuses: Mapping[str, str]) -> None:
    if dataset.get("dataset_version") != DATASET_VERSION:
        raise ShadowEvaluationError(f"dataset_version must be {DATASET_VERSION}")
    approval = dataset.get("approval")
    if not isinstance(approval, Mapping) or approval.get("state") != "APPROVED":
        raise ShadowEvaluationError("shadow dataset must be explicitly approved")
    if approval.get("decision_record") != "ADR-0020" or approval.get("issue") != 61:
        raise ShadowEvaluationError("shadow dataset approval lineage is invalid")
    policy = dataset.get("authority_policy")
    expected_policy = {
        "mode": "SHADOW_ONLY",
        "authority_promotion": "FORBIDDEN",
        "authoritative_writes": "FORBIDDEN",
        "side_effects": "FORBIDDEN",
        "promotion_decision": "NOT_AUTHORIZED",
    }
    if policy != expected_policy:
        raise ShadowEvaluationError("C4 dataset must forbid authority promotion, writes and side effects")
    if dataset.get("prerequisite_conformance") != "C3":
        raise ShadowEvaluationError("C4 dataset prerequisite must be C3")
    thresholds = dataset.get("thresholds")
    if not isinstance(thresholds, Mapping):
        raise ShadowEvaluationError("C4 dataset thresholds are missing")
    expected_thresholds = {
        "critical_divergences_max": 0,
        "semantic_divergence_rate_max": 0.0,
        "missing_receipts_max": 0,
        "c3_supported_coverage_min": 1.0,
    }
    for key, expected in expected_thresholds.items():
        if thresholds.get(key) != expected:
            raise ShadowEvaluationError(f"unsafe C4 threshold {key}")
    if not isinstance(thresholds.get("latency_ratio_max"), (int, float)) or thresholds["latency_ratio_max"] < 1:
        raise ShadowEvaluationError("latency_ratio_max must be numeric and >= 1")
    limitations = dataset.get("limitations")
    if not isinstance(limitations, list) or len(limitations) < 3:
        raise ShadowEvaluationError("C4 dataset must state explicit limitations")
    joined = " ".join(str(item).lower() for item in limitations)
    if "not captured production traffic" not in joined or "does not authorize authority promotion" not in joined:
        raise ShadowEvaluationError("C4 dataset limitations are incomplete")
    cases = dataset.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ShadowEvaluationError("C4 dataset must contain cases")
    case_ids: set[str] = set()
    covered: set[str] = set()
    supported = {assertion_id for assertion_id, status in c3_statuses.items() if status == "SUPPORTED"}
    for case in cases:
        if not isinstance(case, Mapping):
            raise ShadowEvaluationError("invalid C4 case")
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id:
            raise ShadowEvaluationError("C4 case is missing case_id")
        if case_id in case_ids:
            raise ShadowEvaluationError(f"duplicate C4 case_id {case_id}")
        case_ids.add(case_id)
        assertion_ids = _validate_unique_strings(case.get("assertion_ids"), f"{case_id}.assertion_ids")
        unknown = set(assertion_ids) - set(c3_statuses)
        if unknown:
            raise ShadowEvaluationError(f"{case_id} references unknown assertions: {sorted(unknown)}")
        non_supported = {item for item in assertion_ids if c3_statuses[item] != "SUPPORTED"}
        if non_supported:
            raise ShadowEvaluationError(f"{case_id} attempts C4 evaluation of non-C3-supported assertions: {sorted(non_supported)}")
        overlap = covered.intersection(assertion_ids)
        if overlap:
            raise ShadowEvaluationError(f"C4 assertion coverage is duplicated: {sorted(overlap)}")
        covered.update(assertion_ids)
        _validate_unique_strings(case.get("comparison_fields"), f"{case_id}.comparison_fields")
        _validate_unique_strings(case.get("allowed_difference_fields"), f"{case_id}.allowed_difference_fields", allow_empty=True)
        if case.get("equivalence_class") not in {"BYTE", "STRUCTURAL", "SEMANTIC", "BEHAVIOURAL"}:
            raise ShadowEvaluationError(f"invalid equivalence class in {case_id}")
        if not isinstance(case.get("critical"), bool):
            raise ShadowEvaluationError(f"{case_id}.critical must be boolean")
        for side in ("reference_observation", "candidate_observation"):
            if not isinstance(case.get(side), Mapping):
                raise ShadowEvaluationError(f"{case_id}.{side} must be an object")
            boundary = case[side].get("proof_boundary")
            if not isinstance(boundary, Mapping) or boundary.get("authority_promoted") is not False or boundary.get("side_effects_executed") is not False:
                raise ShadowEvaluationError(f"{case_id}.{side} violates shadow-only proof boundary")
    if covered != supported:
        missing = sorted(supported - covered)
        extra = sorted(covered - supported)
        raise ShadowEvaluationError(f"C4 dataset must cover every C3-supported assertion exactly once; missing={missing}, extra={extra}")


def compare_case(case: Mapping[str, Any]) -> CaseComparison:
    reference = case["reference_observation"]
    candidate = case["candidate_observation"]
    divergences: list[dict[str, Any]] = []
    allowed: list[dict[str, Any]] = []
    for field in case["comparison_fields"]:
        left = _path_value(reference, field)
        right = _path_value(candidate, field)
        if left != right:
            divergences.append({"field": field, "reference": left, "candidate": right})
    for field in case["allowed_difference_fields"]:
        left = _path_value(reference, field)
        right = _path_value(candidate, field)
        if left != right:
            allowed.append({"field": field, "reference": left, "candidate": right})
    reference_latency = reference.get("latency_ms")
    candidate_latency = candidate.get("latency_ms")
    if not isinstance(reference_latency, (int, float)) or reference_latency <= 0:
        raise ShadowEvaluationError(f"{case['case_id']} reference latency must be positive")
    if not isinstance(candidate_latency, (int, float)) or candidate_latency < 0:
        raise ShadowEvaluationError(f"{case['case_id']} candidate latency must be non-negative")
    ratio = float(candidate_latency) / float(reference_latency)
    normalized = {
        "case_id": case["case_id"],
        "assertion_ids": case["assertion_ids"],
        "comparison_fields": case["comparison_fields"],
        "reference": {field: _path_value(reference, field) for field in case["comparison_fields"]},
        "candidate": {field: _path_value(candidate, field) for field in case["comparison_fields"]},
    }
    return CaseComparison(
        case_id=str(case["case_id"]),
        assertion_ids=tuple(case["assertion_ids"]),
        critical=bool(case["critical"]),
        matched=not divergences,
        divergences=tuple(divergences),
        allowed_differences=tuple(allowed),
        latency_ratio=ratio,
        comparison_digest=sha256_json(normalized),
    )


def _receipt(dataset_digest: str, case: Mapping[str, Any], result: CaseComparison) -> dict[str, Any]:
    receipt_material = {
        "dataset_digest": dataset_digest,
        "case_id": result.case_id,
        "comparison_digest": result.comparison_digest,
        "matched": result.matched,
    }
    return {
        "receipt_version": RECEIPT_VERSION,
        "receipt_id": "sha256:" + sha256_json(receipt_material),
        "dataset_digest": "sha256:" + dataset_digest,
        "case_id": result.case_id,
        "comparison_digest": "sha256:" + result.comparison_digest,
        "decision": "OBSERVE_ONLY",
        "authority_promoted": False,
        "authoritative_write_performed": False,
        "side_effects_executed": False,
        "matched": result.matched,
        "critical": result.critical,
        "proofs": {
            "recorded_observations_compared": True,
            "assertion_scope_recorded": True,
            "truth_proven": False,
            "external_authenticity_proven": False,
            "physical_deletion_proven": False,
            "production_safety_proven": False,
        },
        "limitations": [
            "This Receipt proves only that the recorded case was compared by the offline evaluator.",
            "It does not authorize authority promotion, writes, side effects, live traffic or production use.",
        ],
    }


def evaluate(dataset: Mapping[str, Any], c3_report: Mapping[str, Any], *, dataset_text: str | None = None) -> dict[str, Any]:
    c3_statuses = validate_c3_prerequisite(c3_report)
    validate_dataset(dataset, c3_statuses)
    canonical_dataset = dataset_text if dataset_text is not None else json.dumps(dataset, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    dataset_digest = sha256_text(canonical_dataset)
    c3_digest = sha256_json(c3_report)
    case_results: list[dict[str, Any]] = []
    receipts: list[dict[str, Any]] = []
    critical_divergences = 0
    semantic_divergences = 0
    allowed_difference_count = 0
    latency_violations = 0
    thresholds = dataset["thresholds"]
    assertion_to_cases: dict[str, list[str]] = {}
    for case in dataset["cases"]:
        result = compare_case(case)
        if not result.matched:
            semantic_divergences += 1
            if result.critical:
                critical_divergences += 1
        if result.latency_ratio > float(thresholds["latency_ratio_max"]):
            latency_violations += 1
        allowed_difference_count += len(result.allowed_differences)
        for assertion_id in result.assertion_ids:
            assertion_to_cases.setdefault(assertion_id, []).append(result.case_id)
        case_results.append({
            "case_id": result.case_id,
            "category": case["category"],
            "equivalence_class": case["equivalence_class"],
            "critical": result.critical,
            "assertion_ids": list(result.assertion_ids),
            "matched": result.matched,
            "comparison_digest": "sha256:" + result.comparison_digest,
            "divergences": list(result.divergences),
            "allowed_differences": list(result.allowed_differences),
            "latency_ratio": round(result.latency_ratio, 6),
            "latency_threshold_passed": result.latency_ratio <= float(thresholds["latency_ratio_max"]),
        })
        receipts.append(_receipt(dataset_digest, case, result))
    total_cases = len(case_results)
    divergence_rate = semantic_divergences / total_cases if total_cases else 1.0
    supported_ids = {key for key, value in c3_statuses.items() if value == "SUPPORTED"}
    coverage = len(assertion_to_cases) / len(supported_ids) if supported_ids else 0.0
    missing_receipts = total_cases - len(receipts)
    gates = {
        "critical_divergences": critical_divergences <= thresholds["critical_divergences_max"],
        "semantic_divergence_rate": divergence_rate <= thresholds["semantic_divergence_rate_max"],
        "missing_receipts": missing_receipts <= thresholds["missing_receipts_max"],
        "c3_supported_coverage": coverage >= thresholds["c3_supported_coverage_min"],
        "latency_ratio": latency_violations == 0,
        "authority_boundary": True,
    }
    overall_pass = all(gates.values())
    assertion_results: list[dict[str, Any]] = []
    for row in c3_report["assertion_results"]:
        assertion_id = row["assertion_id"]
        status = row["status"]
        evaluated = status == "SUPPORTED" and assertion_id in assertion_to_cases
        assertion_results.append({
            "assertion_id": assertion_id,
            "status": status,
            "shadow_level": "C4" if evaluated and overall_pass else ("C4_FAILED" if evaluated else "NOT_EVALUATED_C4"),
            "case_ids": assertion_to_cases.get(assertion_id, []),
            "limitations": (
                ["C4 is limited to approved offline recorded workloads and does not authorize production or authority promotion."]
                if evaluated
                else list(row.get("limitations", [])) or ["This assertion is outside the C4-supported shadow set."]
            ),
        })
    counts = {key: sum(1 for value in c3_statuses.values() if value == key) for key in EXPECTED_C3_COUNTS}
    environment = {
        "commit_sha": os.environ.get("NK_EVIDENCE_COMMIT", "LOCAL"),
        "workflow_run_id": os.environ.get("NK_EVIDENCE_RUN_ID", "LOCAL"),
        "python_version": os.environ.get("NK_PYTHON_VERSION", platform.python_version()),
        "postgresql_version": os.environ.get("NK_POSTGRESQL_VERSION", "RECORDED"),
        "sqlite_version": os.environ.get("NK_SQLITE_VERSION", "RECORDED"),
        "platform": platform.platform(),
    }
    report = {
        "report_version": REPORT_VERSION,
        "receipt_version": RECEIPT_VERSION,
        "evaluation_id": "native-kernel/c4-offline-shadow-v1",
        "dataset": {
            "dataset_id": dataset["dataset_id"],
            "dataset_version": dataset["dataset_version"],
            "sha256": "sha256:" + dataset_digest,
            "approval": dataset["approval"],
            "case_count": total_cases,
        },
        "prerequisite": {
            "report_version": c3_report["report_version"],
            "comparison_id": c3_report.get("comparison_id"),
            "sha256": "sha256:" + c3_digest,
            "kernel_runtime_conformance": "C3",
            "support_state": "PARTIAL",
        },
        "reference_profile": dataset["reference_profile"],
        "candidate_profile": dataset["candidate_profile"],
        "kernel_runtime_conformance": "C4" if overall_pass else "C4_FAILED",
        "support_state": "PARTIAL",
        "evidence_level": "REPOSITORY_REPRODUCED_OFFLINE_SHADOW" if environment["commit_sha"] != "LOCAL" else "LOCALLY_TESTED_OFFLINE_SHADOW",
        "shadow_mode": "OFFLINE_RECORDED_WORKLOAD",
        "authority_policy": dataset["authority_policy"],
        "promotion_decision": "NOT_AUTHORIZED",
        "environment": environment,
        "thresholds": thresholds,
        "metrics": {
            "total_cases": total_cases,
            "matched_cases": total_cases - semantic_divergences,
            "semantic_divergences": semantic_divergences,
            "critical_divergences": critical_divergences,
            "semantic_divergence_rate": round(divergence_rate, 8),
            "allowed_operational_differences": allowed_difference_count,
            "latency_threshold_violations": latency_violations,
            "receipts": len(receipts),
            "missing_receipts": missing_receipts,
            "c3_supported_assertions": len(supported_ids),
            "c4_shadow_evaluated_assertions": len(assertion_to_cases),
            "c3_supported_coverage": round(coverage, 8),
            "assertion_counts": counts,
        },
        "gates": gates,
        "case_results": case_results,
        "receipts": receipts,
        "assertion_results": assertion_results,
        "status": "PASS" if overall_pass else "FAIL",
        "limitations": [
            "The approved dataset contains recorded synthetic repository workloads, not captured production traffic.",
            "C4 does not authorize authority promotion, authoritative writes, side effects or automatic actions; it is not live production shadowing.",
            "C4 applies only to the existing 45 C3-supported assertions; 10 PARTIAL and 17 UNSUPPORTED assertions are not promoted.",
            "This report is not C5 and is not production readiness, operational equivalence, truth/authenticity or physical deletion evidence.",
        ],
    }
    return report


def report_from_files(dataset_path: Path, c3_report_path: Path) -> dict[str, Any]:
    dataset_text = dataset_path.read_text(encoding="utf-8")
    dataset = load_json(dataset_path)
    c3_report = load_json(c3_report_path)
    return evaluate(dataset, c3_report, dataset_text=dataset_text)


def render_report(report: Mapping[str, Any]) -> str:
    return json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def validate_report(report: Mapping[str, Any], *, require_repository: bool = False) -> None:
    if report.get("report_version") != REPORT_VERSION or report.get("receipt_version") != RECEIPT_VERSION:
        raise ShadowEvaluationError("invalid C4 report or Receipt protocol")
    if report.get("evaluation_id") != "native-kernel/c4-offline-shadow-v1":
        raise ShadowEvaluationError("invalid C4 evaluation_id")
    if report.get("kernel_runtime_conformance") != "C4" or report.get("status") != "PASS":
        raise ShadowEvaluationError("C4 report must fail closed unless every gate passes")
    if report.get("support_state") != "PARTIAL":
        raise ShadowEvaluationError("C4 support_state must remain PARTIAL")
    if report.get("shadow_mode") != "OFFLINE_RECORDED_WORKLOAD":
        raise ShadowEvaluationError("C4 report is not offline shadow evidence")
    policy = report.get("authority_policy")
    if not isinstance(policy, Mapping) or policy.get("authority_promotion") != "FORBIDDEN" or policy.get("authoritative_writes") != "FORBIDDEN" or policy.get("side_effects") != "FORBIDDEN":
        raise ShadowEvaluationError("C4 report violates the authority-free boundary")
    if report.get("promotion_decision") != "NOT_AUTHORIZED":
        raise ShadowEvaluationError("C4 cannot authorize promotion")
    prerequisite = report.get("prerequisite")
    if not isinstance(prerequisite, Mapping) or prerequisite.get("kernel_runtime_conformance") != "C3" or prerequisite.get("report_version") != "nk-equivalence-report/1":
        raise ShadowEvaluationError("C4 report is missing exact C3 prerequisite evidence")
    if not str(prerequisite.get("sha256", "")).startswith("sha256:"):
        raise ShadowEvaluationError("C4 prerequisite digest is missing")
    dataset = report.get("dataset")
    if not isinstance(dataset, Mapping) or dataset.get("dataset_version") != DATASET_VERSION or dataset.get("approval", {}).get("state") != "APPROVED":
        raise ShadowEvaluationError("C4 report dataset approval is invalid")
    if not str(dataset.get("sha256", "")).startswith("sha256:"):
        raise ShadowEvaluationError("C4 dataset digest is missing")
    metrics = report.get("metrics")
    expected_metrics = {
        "total_cases": 15,
        "matched_cases": 15,
        "semantic_divergences": 0,
        "critical_divergences": 0,
        "semantic_divergence_rate": 0.0,
        "latency_threshold_violations": 0,
        "receipts": 15,
        "missing_receipts": 0,
        "c3_supported_assertions": 45,
        "c4_shadow_evaluated_assertions": 45,
        "c3_supported_coverage": 1.0,
    }
    if not isinstance(metrics, Mapping):
        raise ShadowEvaluationError("C4 metrics are missing")
    for key, expected in expected_metrics.items():
        if metrics.get(key) != expected:
            raise ShadowEvaluationError(f"unexpected C4 metric {key}: {metrics.get(key)!r}")
    if metrics.get("assertion_counts") != EXPECTED_C3_COUNTS:
        raise ShadowEvaluationError("C4 changed the inherited assertion map")
    gates = report.get("gates")
    if not isinstance(gates, Mapping) or set(gates.values()) != {True}:
        raise ShadowEvaluationError("all C4 gates must pass")
    cases = report.get("case_results")
    receipts = report.get("receipts")
    if not isinstance(cases, list) or len(cases) != 15 or any(case.get("matched") is not True for case in cases):
        raise ShadowEvaluationError("C4 case results are incomplete or divergent")
    if not isinstance(receipts, list) or len(receipts) != 15:
        raise ShadowEvaluationError("C4 Receipts are incomplete")
    receipt_ids: set[str] = set()
    for receipt in receipts:
        if receipt.get("receipt_version") != RECEIPT_VERSION:
            raise ShadowEvaluationError("invalid Shadow Receipt version")
        receipt_id = receipt.get("receipt_id")
        if not isinstance(receipt_id, str) or not receipt_id.startswith("sha256:") or receipt_id in receipt_ids:
            raise ShadowEvaluationError("invalid or duplicate Shadow Receipt ID")
        receipt_ids.add(receipt_id)
        if receipt.get("decision") != "OBSERVE_ONLY" or receipt.get("authority_promoted") is not False or receipt.get("authoritative_write_performed") is not False or receipt.get("side_effects_executed") is not False:
            raise ShadowEvaluationError("Shadow Receipt violates the no-authority boundary")
        proofs = receipt.get("proofs")
        if not isinstance(proofs, Mapping) or proofs.get("truth_proven") is not False or proofs.get("production_safety_proven") is not False:
            raise ShadowEvaluationError("Shadow Receipt overclaims proof")
    assertions = report.get("assertion_results")
    if not isinstance(assertions, list) or len(assertions) != 72:
        raise ShadowEvaluationError("C4 report must expose all 72 assertion results")
    seen: set[str] = set()
    counts = {key: 0 for key in EXPECTED_C3_COUNTS}
    c4_count = 0
    for row in assertions:
        assertion_id = row.get("assertion_id")
        status = row.get("status")
        if not isinstance(assertion_id, str) or assertion_id in seen or status not in counts:
            raise ShadowEvaluationError("invalid C4 assertion result")
        seen.add(assertion_id)
        counts[status] += 1
        if row.get("shadow_level") == "C4":
            c4_count += 1
            if status != "SUPPORTED" or not row.get("case_ids"):
                raise ShadowEvaluationError("only supported and covered assertions may receive C4")
        elif status == "SUPPORTED":
            raise ShadowEvaluationError("every C3-supported assertion must be C4-evaluated")
        if assertion_id.startswith("NK-EPI-") and (status != "UNSUPPORTED" or row.get("shadow_level") == "C4"):
            raise ShadowEvaluationError("C4 cannot promote NK-EPI")
    if counts != EXPECTED_C3_COUNTS or c4_count != 45:
        raise ShadowEvaluationError("C4 assertion map or coverage is invalid")
    limitations = report.get("limitations")
    if not isinstance(limitations, list) or len(limitations) < 4:
        raise ShadowEvaluationError("C4 limitations are missing")
    joined = " ".join(str(item).lower() for item in limitations)
    for fragment in REQUIRED_LIMITATION_FRAGMENTS:
        if fragment not in joined:
            raise ShadowEvaluationError(f"C4 limitation missing fragment: {fragment}")
    environment = report.get("environment")
    if not isinstance(environment, Mapping):
        raise ShadowEvaluationError("C4 environment is missing")
    if require_repository:
        if report.get("evidence_level") != "REPOSITORY_REPRODUCED_OFFLINE_SHADOW":
            raise ShadowEvaluationError("repository C4 report has wrong evidence level")
        if environment.get("commit_sha") in {None, "", "LOCAL"} or environment.get("workflow_run_id") in {None, "", "LOCAL"}:
            raise ShadowEvaluationError("repository C4 report has placeholder metadata")


def validate_report_file(path: Path, *, require_repository: bool = False) -> None:
    validate_report(load_json(path), require_repository=require_repository)
