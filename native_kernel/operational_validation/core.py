from __future__ import annotations

import hashlib
import json
import math
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping

PLAN_PROTOCOL = "nk-operational-plan/1"
REPORT_PROTOCOL = "nk-operational-report/1"
RECEIPT_PROTOCOL = "nk-operational-receipt/1"
OPERATIONAL_LEVEL = "C5_BOUNDED_REHEARSAL"
DEPLOYMENT_CLASS = "CI_EPHEMERAL_SYNTHETIC"
EXPECTED_ASSERTION_COUNTS = {
    "SUPPORTED": 45,
    "PARTIAL": 10,
    "UNSUPPORTED": 17,
    "FAILED": 0,
}
REQUIRED_LIMITATIONS = (
    "synthetic data",
    "not production",
    "not cloud iam",
    "not physical deletion",
    "not compliance certification",
)


class OperationalValidationError(RuntimeError):
    pass


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def sha256_digest(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def load_json(path: str | Path) -> dict[str, Any]:
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise OperationalValidationError(f"{path}: top-level JSON must be an object")
    return value


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise OperationalValidationError(message)


def validate_plan(plan: Mapping[str, Any]) -> None:
    _require(plan.get("protocol") == PLAN_PROTOCOL, "unsupported operational plan protocol")
    _require(
        plan.get("plan_id") == "native-kernel/c5-bounded-rehearsal-v1",
        "unexpected operational plan id",
    )
    approval = plan.get("approval")
    _require(isinstance(approval, Mapping), "plan approval object required")
    _require(approval.get("state") == "APPROVED", "operational plan must be approved")
    _require(approval.get("decision_record") == "ADR-0021", "ADR-0021 approval required")
    boundary = plan.get("deployment_boundary")
    _require(isinstance(boundary, Mapping), "deployment boundary required")
    expected_boundary = {
        "deployment_class": DEPLOYMENT_CLASS,
        "live_user_data": False,
        "synthetic_data_only": True,
        "production_traffic": False,
        "network_api_exposed": False,
        "authority_promotion": False,
        "authoritative_external_side_effects": False,
        "ecosystem_wiring": False,
        "physical_deletion_claimed": False,
        "compliance_certification_claimed": False,
    }
    for key, expected in expected_boundary.items():
        _require(boundary.get(key) == expected, f"unsafe deployment boundary: {key}")

    prerequisite = plan.get("prerequisite")
    _require(isinstance(prerequisite, Mapping), "C4 prerequisite declaration required")
    _require(prerequisite.get("protocol") == "nk-shadow-report/1", "C4 protocol required")
    _require(prerequisite.get("status") == "PASS", "C4 PASS prerequisite required")
    _require(prerequisite.get("support_state") == "PARTIAL", "C4 support must remain PARTIAL")
    _require(
        (
            prerequisite.get("supported_assertions"),
            prerequisite.get("partial_assertions"),
            prerequisite.get("unsupported_assertions"),
        )
        == (45, 10, 17),
        "C4 prerequisite assertion map drifted",
    )

    scenarios = plan.get("scenarios")
    _require(isinstance(scenarios, list) and scenarios, "operational scenarios required")
    ids = [item.get("id") for item in scenarios if isinstance(item, Mapping)]
    _require(len(ids) == len(scenarios), "every scenario must be an object with id")
    _require(len(set(ids)) == len(ids), "duplicate operational scenario id")
    thresholds = plan.get("thresholds")
    _require(isinstance(thresholds, Mapping), "operational thresholds required")
    _require(
        thresholds.get("required_scenarios") == len(scenarios),
        "required scenario count differs from plan",
    )
    categories = {item.get("category") for item in scenarios}
    _require(
        categories == {"SECURITY", "PRIVACY", "RECOVERY", "ROLLBACK", "INCIDENT", "RELIABILITY", "RESILIENCE"},
        "operational category coverage drifted",
    )
    privacy = plan.get("privacy")
    _require(isinstance(privacy, Mapping), "privacy policy required")
    canaries = privacy.get("canary_tokens")
    _require(isinstance(canaries, list) and len(canaries) >= 2, "at least two privacy canaries required")
    _require(len(set(canaries)) == len(canaries), "duplicate privacy canary")
    _require(all(isinstance(value, str) and value for value in canaries), "invalid privacy canary")
    limitations = plan.get("limitations")
    _require(isinstance(limitations, list) and limitations, "plan limitations required")


def validate_c4_prerequisite(report: Mapping[str, Any]) -> None:
    _require(report.get("report_version") == "nk-shadow-report/1", "C4 prerequisite protocol mismatch")
    _require(report.get("status") == "PASS", "C4 prerequisite must PASS")
    _require(report.get("support_state") == "PARTIAL", "C4 prerequisite support must remain PARTIAL")
    _require(report.get("kernel_runtime_conformance") == "C4", "C4 prerequisite level mismatch")
    results = report.get("assertion_results")
    _require(isinstance(results, list) and len(results) == 72, "C4 prerequisite must contain 72 assertions")
    counts = {
        status: sum(item.get("status") == status for item in results)
        for status in EXPECTED_ASSERTION_COUNTS
    }
    _require(counts == EXPECTED_ASSERTION_COUNTS, f"C4 prerequisite map drifted: {counts}")


def redact_text(value: str, canaries: Iterable[str], marker: str = "[REDACTED]") -> str:
    redacted = value
    for token in canaries:
        redacted = redacted.replace(token, marker)
    return redacted


def redact_value(value: Any, canaries: Iterable[str], marker: str = "[REDACTED]") -> Any:
    if isinstance(value, str):
        return redact_text(value, canaries, marker)
    if isinstance(value, list):
        return [redact_value(item, canaries, marker) for item in value]
    if isinstance(value, tuple):
        return [redact_value(item, canaries, marker) for item in value]
    if isinstance(value, Mapping):
        return {
            str(key): redact_value(item, canaries, marker)
            for key, item in value.items()
        }
    return value


def canary_leaks(value: Any, canaries: Iterable[str]) -> tuple[str, ...]:
    text = canonical_json_bytes(value).decode("utf-8")
    return tuple(token for token in canaries if token in text)


@dataclass(frozen=True, slots=True)
class ScenarioResult:
    scenario_id: str
    category: str
    profile: str
    status: str
    duration_ms: float
    detail: str
    metrics: Mapping[str, Any]
    incident_timeline: tuple[Mapping[str, Any], ...] = ()

    def as_report_object(self) -> dict[str, Any]:
        value: dict[str, Any] = {
            "scenario_id": self.scenario_id,
            "category": self.category,
            "profile": self.profile,
            "status": self.status,
            "duration_ms": round(float(self.duration_ms), 3),
            "detail": self.detail,
            "metrics": dict(self.metrics),
        }
        if self.incident_timeline:
            value["incident_timeline"] = [dict(item) for item in self.incident_timeline]
        return value


class OperationalRecorder:
    def __init__(self, scenario_definitions: Iterable[Mapping[str, Any]]) -> None:
        self._definitions = {
            str(item["id"]): {
                "category": str(item["category"]),
                "profile": str(item["profile"]),
            }
            for item in scenario_definitions
        }
        self.results: list[ScenarioResult] = []

    def run(
        self,
        scenario_id: str,
        fn: Callable[[], Mapping[str, Any] | None],
        *,
        incident_timeline: tuple[Mapping[str, Any], ...] = (),
    ) -> ScenarioResult:
        definition = self._definitions.get(scenario_id)
        if definition is None:
            raise OperationalValidationError(f"unknown scenario: {scenario_id}")
        started = time.perf_counter()
        try:
            metrics = dict(fn() or {})
            status = "PASS"
            detail = str(metrics.pop("detail", "bounded operational scenario passed"))
        except Exception as exc:
            metrics = {"error_type": type(exc).__name__}
            status = "FAIL"
            detail = f"{type(exc).__name__}: {exc}"
        duration_ms = (time.perf_counter() - started) * 1000.0
        result = ScenarioResult(
            scenario_id=scenario_id,
            category=definition["category"],
            profile=definition["profile"],
            status=status,
            duration_ms=duration_ms,
            detail=detail,
            metrics=metrics,
            incident_timeline=incident_timeline,
        )
        self.results.append(result)
        return result


def percentile(values: Iterable[float], percentile_value: float) -> float:
    data = sorted(float(value) for value in values)
    if not data:
        return 0.0
    if len(data) == 1:
        return data[0]
    rank = (len(data) - 1) * percentile_value
    lower = math.floor(rank)
    upper = math.ceil(rank)
    if lower == upper:
        return data[lower]
    weight = rank - lower
    return data[lower] * (1.0 - weight) + data[upper] * weight


def _receipt_for(
    result: Mapping[str, Any],
    *,
    plan_digest: str,
    prerequisite_digest: str,
) -> dict[str, Any]:
    evidence = {
        "scenario_id": result["scenario_id"],
        "category": result["category"],
        "profile": result["profile"],
        "status": result["status"],
        "detail": result["detail"],
        "metrics": result["metrics"],
        "plan_digest": plan_digest,
        "prerequisite_digest": prerequisite_digest,
    }
    evidence_digest = sha256_digest(canonical_json_bytes(evidence))
    receipt_id = "oprec:" + evidence_digest.split(":", 1)[1]
    return {
        "contract": RECEIPT_PROTOCOL,
        "receipt_id": receipt_id,
        "scenario_id": result["scenario_id"],
        "category": result["category"],
        "profile": result["profile"],
        "status": result["status"],
        "evidence_digest": evidence_digest,
        "duration_ms": result["duration_ms"],
        "decision": "REHEARSAL_OBSERVATION_ONLY",
        "live_user_data_used": False,
        "authority_promoted": False,
        "authoritative_external_side_effects": False,
        "production_approved": False,
        "physical_deletion_proved": False,
        "compliance_certified": False,
        "limitations": [
            "Receipt proves only the named synthetic ephemeral rehearsal scenario.",
            "Receipt does not establish production readiness, cloud IAM, compliance or physical deletion.",
        ],
    }


def build_report(
    plan: Mapping[str, Any],
    c4_report: Mapping[str, Any],
    scenario_results: Iterable[ScenarioResult | Mapping[str, Any]],
    *,
    plan_bytes: bytes,
    c4_bytes: bytes,
    environment: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    validate_plan(plan)
    validate_c4_prerequisite(c4_report)
    scenario_objects = [
        item.as_report_object() if isinstance(item, ScenarioResult) else dict(item)
        for item in scenario_results
    ]
    plan_ids = [str(item["id"]) for item in plan["scenarios"]]
    result_ids = [str(item.get("scenario_id")) for item in scenario_objects]
    _require(len(result_ids) == len(set(result_ids)), "duplicate scenario result")
    _require(set(result_ids) == set(plan_ids), "scenario results do not cover exact plan")

    canaries = tuple(plan["privacy"]["canary_tokens"])
    marker = str(plan["privacy"]["redaction_marker"])
    scenario_objects = [
        redact_value(item, canaries, marker)
        for item in scenario_objects
    ]
    plan_digest = sha256_digest(plan_bytes)
    prerequisite_digest = sha256_digest(c4_bytes)
    receipts = [
        _receipt_for(item, plan_digest=plan_digest, prerequisite_digest=prerequisite_digest)
        for item in scenario_objects
    ]

    failed = sum(item["status"] != "PASS" for item in scenario_objects)
    canary_count = len(canary_leaks({"scenario_results": scenario_objects, "receipts": receipts}, canaries))
    recovery_failures = sum(
        item["status"] != "PASS" and item["category"] in {"RECOVERY", "ROLLBACK"}
        for item in scenario_objects
    )
    incident_uncontained = sum(
        item["status"] != "PASS" and item["category"] == "INCIDENT"
        for item in scenario_objects
    )
    append_latencies = [
        float(value)
        for item in scenario_objects
        for key, value in item.get("metrics", {}).items()
        if key == "p95_append_ms" and isinstance(value, (int, float))
    ]
    p95_append_ms = max(append_latencies, default=0.0)
    total_duration_ms = sum(float(item["duration_ms"]) for item in scenario_objects)
    counts = {
        status: sum(item.get("status") == status for item in c4_report["assertion_results"])
        for status in EXPECTED_ASSERTION_COUNTS
    }
    thresholds = plan["thresholds"]
    status = "PASS"
    if (
        failed > thresholds["failed_scenarios_max"]
        or canary_count > thresholds["canary_leaks_max"]
        or recovery_failures > thresholds["recovery_failures_max"]
        or incident_uncontained > thresholds["incident_uncontained_max"]
        or p95_append_ms > thresholds["p95_append_ms_max"]
        or total_duration_ms > thresholds["total_rehearsal_seconds_max"] * 1000.0
    ):
        status = "FAIL"

    env = {
        "evidence_level": os.environ.get("NK_EVIDENCE_LEVEL", "LOCALLY_TESTED"),
        "commit": os.environ.get("NK_EVIDENCE_COMMIT", "LOCAL"),
        "run_id": os.environ.get("NK_EVIDENCE_RUN_ID", "LOCAL"),
        "python_version": os.environ.get("NK_PYTHON_VERSION", "LOCAL"),
        "postgresql_version": os.environ.get("NK_POSTGRESQL_VERSION", "LOCAL"),
        "sqlite_version": os.environ.get("NK_SQLITE_VERSION", "LOCAL"),
        "runner_os": os.environ.get("NK_RUNNER_OS", "LOCAL"),
    }
    if environment:
        env.update(dict(environment))

    report = {
        "protocol": REPORT_PROTOCOL,
        "status": status,
        "operational_validation": OPERATIONAL_LEVEL,
        "kernel_runtime_conformance": "C4",
        "support_state": "PARTIAL",
        "plan": {
            "id": plan["plan_id"],
            "protocol": plan["protocol"],
            "sha256": plan_digest,
        },
        "prerequisite": {
            "report_version": c4_report["report_version"],
            "sha256": prerequisite_digest,
            "status": c4_report["status"],
            "support_state": c4_report["support_state"],
        },
        "deployment_boundary": dict(plan["deployment_boundary"]),
        "thresholds": dict(thresholds),
        "environment": env,
        "metrics": {
            "scenario_count": len(scenario_objects),
            "passed_scenarios": len(scenario_objects) - failed,
            "failed_scenarios": failed,
            "canary_leaks": canary_count,
            "recovery_failures": recovery_failures,
            "incident_uncontained": incident_uncontained,
            "p95_append_ms": round(p95_append_ms, 3),
            "total_duration_ms": round(total_duration_ms, 3),
            "receipt_count": len(receipts),
            "assertion_counts": counts,
        },
        "scenario_results": scenario_objects,
        "receipts": receipts,
        "assertion_results": [dict(item) for item in c4_report["assertion_results"]],
        "limitations": [
            "C5 evidence is limited to synthetic data in a controlled ephemeral CI deployment.",
            "Application-level authority and fencing are not cloud IAM, network security or Byzantine validation.",
            "Quarantine restore is bounded application-level recovery, not managed-provider disaster recovery.",
            "The rehearsal is not production readiness, not live-traffic validation and not compliance certification.",
            "The rehearsal is not physical deletion proof and does not establish cryptographic erasure.",
            "The inherited assertion map remains 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED.",
        ],
    }
    return report


def validate_report(
    report: Mapping[str, Any],
    *,
    plan: Mapping[str, Any] | None = None,
    plan_bytes: bytes | None = None,
    require_repository: bool = False,
) -> None:
    _require(report.get("protocol") == REPORT_PROTOCOL, "unsupported C5 report protocol")
    _require(report.get("operational_validation") == OPERATIONAL_LEVEL, "wrong C5 operational level")
    _require(report.get("kernel_runtime_conformance") == "C4", "C5 rehearsal must not rewrite assertion conformance")
    _require(report.get("support_state") == "PARTIAL", "support state must remain PARTIAL")
    _require(report.get("status") == "PASS", "C5 rehearsal report did not PASS")
    boundary = report.get("deployment_boundary")
    _require(isinstance(boundary, Mapping), "deployment boundary missing")
    for key in (
        "live_user_data",
        "production_traffic",
        "network_api_exposed",
        "authority_promotion",
        "authoritative_external_side_effects",
        "ecosystem_wiring",
        "physical_deletion_claimed",
        "compliance_certification_claimed",
    ):
        _require(boundary.get(key) is False, f"unsafe C5 report boundary: {key}")
    _require(boundary.get("synthetic_data_only") is True, "synthetic-only boundary required")
    _require(boundary.get("deployment_class") == DEPLOYMENT_CLASS, "deployment class mismatch")

    results = report.get("scenario_results")
    receipts = report.get("receipts")
    _require(isinstance(results, list) and results, "scenario results required")
    _require(isinstance(receipts, list) and len(receipts) == len(results), "one Receipt per scenario required")
    result_ids = [item.get("scenario_id") for item in results]
    receipt_ids = [item.get("scenario_id") for item in receipts]
    _require(len(set(result_ids)) == len(result_ids), "duplicate scenario result")
    _require(set(result_ids) == set(receipt_ids), "Receipt scenario coverage mismatch")
    _require(all(item.get("status") == "PASS" for item in results), "all C5 scenarios must PASS")
    for receipt in receipts:
        _require(receipt.get("contract") == RECEIPT_PROTOCOL, "wrong operational Receipt protocol")
        _require(receipt.get("status") == "PASS", "failed scenario Receipt")
        for key in (
            "live_user_data_used",
            "authority_promoted",
            "authoritative_external_side_effects",
            "production_approved",
            "physical_deletion_proved",
            "compliance_certified",
        ):
            _require(receipt.get(key) is False, f"operational Receipt overclaim: {key}")
        _require(receipt.get("limitations"), "operational Receipt limitations required")

    assertion_results = report.get("assertion_results")
    _require(isinstance(assertion_results, list) and len(assertion_results) == 72, "72 assertion results required")
    _require(len({item.get("assertion_id") for item in assertion_results}) == 72, "assertion IDs must be unique")
    counts = {
        status: sum(item.get("status") == status for item in assertion_results)
        for status in EXPECTED_ASSERTION_COUNTS
    }
    _require(counts == EXPECTED_ASSERTION_COUNTS, f"C5 inherited assertion map drifted: {counts}")
    metrics = report.get("metrics")
    _require(isinstance(metrics, Mapping), "C5 metrics required")
    _require(metrics.get("scenario_count") == len(results), "scenario count mismatch")
    _require(metrics.get("passed_scenarios") == len(results), "passed scenario count mismatch")
    _require(metrics.get("failed_scenarios") == 0, "failed scenario metric must be zero")
    _require(metrics.get("canary_leaks") == 0, "privacy canary leak detected")
    _require(metrics.get("recovery_failures") == 0, "recovery failure detected")
    _require(metrics.get("incident_uncontained") == 0, "uncontained incident detected")
    _require(metrics.get("receipt_count") == len(receipts), "Receipt count mismatch")
    _require(metrics.get("assertion_counts") == EXPECTED_ASSERTION_COUNTS, "assertion count metric mismatch")

    limitations = report.get("limitations")
    _require(isinstance(limitations, list) and limitations, "report limitations required")
    limitation_text = " ".join(str(item).lower() for item in limitations)
    for phrase in REQUIRED_LIMITATIONS:
        _require(phrase in limitation_text, f"missing C5 limitation: {phrase}")

    if plan is not None:
        validate_plan(plan)
        expected_ids = {item["id"] for item in plan["scenarios"]}
        _require(set(result_ids) == expected_ids, "C5 result set differs from approved plan")
        if plan_bytes is not None:
            _require(
                report.get("plan", {}).get("sha256") == sha256_digest(plan_bytes),
                "C5 plan digest mismatch",
            )
        canaries = plan["privacy"]["canary_tokens"]
        _require(not canary_leaks(report, canaries), "C5 report contains privacy canary")

    if require_repository:
        env = report.get("environment")
        _require(isinstance(env, Mapping), "repository environment required")
        _require(
            env.get("evidence_level") == "REPOSITORY_REPRODUCED_OPERATIONAL_REHEARSAL",
            "wrong C5 repository evidence level",
        )
        commit = env.get("commit")
        _require(
            isinstance(commit, str) and len(commit) == 40 and all(ch in "0123456789abcdef" for ch in commit),
            "exact 40-character C5 commit required",
        )
        run_id = env.get("run_id")
        _require(isinstance(run_id, str) and run_id.isdigit(), "numeric C5 run id required")
        for key in ("python_version", "postgresql_version", "sqlite_version", "runner_os"):
            _require(env.get(key) not in {None, "", "LOCAL"}, f"repository metadata missing: {key}")
