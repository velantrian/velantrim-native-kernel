from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Mapping

ASSERTION_RE = re.compile(r"^NK-[A-Z]{2,3}-\d{3}$")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")


class ValidationError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValidationError("report must be a JSON object")
    return value


def _check_results(
    report: Mapping[str, Any],
    expected_counts: Mapping[str, int],
    *,
    required_promotions: set[str] | None = None,
) -> None:
    results = report.get("assertion_results")
    checks = report.get("checks")
    if not isinstance(results, list) or not isinstance(checks, list):
        raise ValidationError("assertion_results and checks must be lists")
    if len(results) != 72:
        raise ValidationError(f"expected 72 assertion results, found {len(results)}")
    ids = [item.get("assertion_id") for item in results if isinstance(item, dict)]
    if len(ids) != 72 or len(set(ids)) != 72 or not all(
        isinstance(item, str) and ASSERTION_RE.fullmatch(item) for item in ids
    ):
        raise ValidationError("assertion IDs must be 72 unique registry-shaped IDs")
    check_map: dict[str, Mapping[str, Any]] = {}
    for check in checks:
        if not isinstance(check, dict):
            raise ValidationError("check must be an object")
        check_id = check.get("check_id")
        if not isinstance(check_id, str) or not check_id:
            raise ValidationError("check_id must be non-empty")
        if check_id in check_map:
            raise ValidationError(f"duplicate check {check_id}")
        check_map[check_id] = check
    counts = {key: 0 for key in expected_counts}
    for item in results:
        status = item.get("status")
        assertion_id = item.get("assertion_id")
        if status not in counts:
            raise ValidationError(f"{assertion_id}: invalid status {status}")
        counts[status] += 1
        limitations = item.get("limitations")
        if not isinstance(limitations, list) or not limitations or not all(
            isinstance(value, str) and value for value in limitations
        ):
            raise ValidationError(f"{assertion_id}: limitations required")
        evidence = item.get("evidence", [])
        if status in {"SUPPORTED", "PARTIAL"} and not evidence:
            raise ValidationError(f"{assertion_id}: {status} requires evidence")
        if not isinstance(evidence, list):
            raise ValidationError(f"{assertion_id}: evidence must be a list")
        for check_id in evidence:
            check = check_map.get(check_id)
            if check is None or check.get("status") != "PASS":
                raise ValidationError(f"{assertion_id}: invalid evidence check {check_id}")
        if assertion_id.startswith("NK-EPI-") and status != "UNSUPPORTED":
            raise ValidationError(f"{assertion_id}: proposed NK-EPI cannot be promoted")
    if counts != dict(expected_counts):
        raise ValidationError(f"unexpected support counts {counts}")
    if required_promotions:
        status_map = {item["assertion_id"]: item["status"] for item in results}
        for assertion_id in required_promotions:
            if status_map.get(assertion_id) != "SUPPORTED":
                raise ValidationError(f"required C3 promotion missing: {assertion_id}")


def validate_sqlite(report: Mapping[str, Any], *, require_c2: bool) -> None:
    if report.get("report_version") != "nk-evidence-report/1":
        raise ValidationError("unexpected SQLite report_version")
    if report.get("profile_id") != "native-kernel/sqlite-embedded":
        raise ValidationError("unexpected SQLite profile_id")
    if report.get("profile_version") != "0.5-p5":
        raise ValidationError("unexpected SQLite profile_version")
    if report.get("support_state") != "PARTIAL":
        raise ValidationError("SQLite support_state must remain PARTIAL")
    expected_level = "C2" if require_c2 else report.get("kernel_runtime_conformance")
    if expected_level not in {"C1", "C2"} or report.get("kernel_runtime_conformance") != expected_level:
        raise ValidationError("SQLite conformance must be C1/C2 as requested")
    if require_c2 and report.get("evidence_level") != "REPOSITORY_REPRODUCED":
        raise ValidationError("SQLite C2 requires REPOSITORY_REPRODUCED")
    _check_results(
        report,
        {"SUPPORTED": 41, "PARTIAL": 13, "UNSUPPORTED": 18, "FAILED": 0},
    )
    limitations = "\n".join(report.get("limitations", []))
    for phrase in ("not C3", "No truth", "physical deletion", "operational envelope"):
        if phrase not in limitations:
            raise ValidationError(f"SQLite report missing boundary: {phrase}")
    if require_c2:
        metadata = next(
            (item for item in report["checks"] if item.get("check_id") == "p5.environment.metadata"),
            None,
        )
        if metadata is None:
            raise ValidationError("SQLite C2 environment metadata missing")
        detail = metadata.get("detail", "")
        if "commit=LOCAL" in detail or "run=LOCAL" in detail:
            raise ValidationError("SQLite C2 cannot use local placeholder metadata")
        match = re.search(r"commit=([0-9a-f]{40})", detail)
        if match is None or not SHA_RE.fullmatch(match.group(1)):
            raise ValidationError("SQLite C2 commit metadata invalid")


def validate_c3(report: Mapping[str, Any], *, require_repository: bool) -> None:
    if report.get("report_version") != "nk-equivalence-report/1":
        raise ValidationError("unexpected C3 report_version")
    if report.get("kernel_runtime_conformance") != "C3":
        raise ValidationError("comparison report must declare C3")
    if report.get("support_state") != "PARTIAL":
        raise ValidationError("C3 support_state must remain PARTIAL")
    if report.get("left_profile", {}).get("profile_id") != "native-kernel/postgresql-reference":
        raise ValidationError("C3 left profile must be PostgreSQL reference")
    if report.get("right_profile", {}).get("profile_id") != "native-kernel/sqlite-embedded":
        raise ValidationError("C3 right profile must be SQLite embedded")
    classes = report.get("equivalence_classes")
    if not isinstance(classes, dict) or set(classes) != {"BYTE", "STRUCTURAL", "SEMANTIC", "BEHAVIOURAL"}:
        raise ValidationError("C3 equivalence classes are incomplete")
    for key in ("allowed_differences", "forbidden_differences", "limitations"):
        values = report.get(key)
        if not isinstance(values, list) or not values:
            raise ValidationError(f"C3 {key} must be non-empty")
    _check_results(
        report,
        {"SUPPORTED": 45, "PARTIAL": 10, "UNSUPPORTED": 17, "FAILED": 0},
        required_promotions={"NK-SEM-008", "NK-ID-008", "NK-EQV-002", "NK-EQV-003"},
    )
    required_checks = {
        "c3.equivalence.classes",
        "c3.profile-reports.compatibility",
        "c3.identity.shared-vectors",
        "c3.behavioural.workload",
        "c3.failures.parity",
        "c3.replay-projection",
        "c3.translation.exact-import",
        "c3.report.traceability",
    }
    passed = {
        item.get("check_id")
        for item in report["checks"]
        if isinstance(item, dict) and item.get("status") == "PASS"
    }
    if not required_checks.issubset(passed):
        raise ValidationError(f"missing C3 checks: {sorted(required_checks - passed)}")
    if require_repository:
        if report.get("evidence_level") != "REPOSITORY_REPRODUCED":
            raise ValidationError("repository C3 requires REPOSITORY_REPRODUCED")
        environment = report.get("environment")
        if not isinstance(environment, dict):
            raise ValidationError("C3 environment missing")
        commit = environment.get("commit")
        run_id = environment.get("run_id")
        if not isinstance(commit, str) or not SHA_RE.fullmatch(commit):
            raise ValidationError("C3 repository commit invalid")
        if not isinstance(run_id, str) or not run_id or run_id == "LOCAL":
            raise ValidationError("C3 repository run_id invalid")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", choices=("sqlite", "c3"))
    parser.add_argument("report", type=Path)
    parser.add_argument("--require-repository", action="store_true")
    args = parser.parse_args(argv)
    try:
        report = _load(args.report)
        if args.kind == "sqlite":
            validate_sqlite(report, require_c2=args.require_repository)
        else:
            validate_c3(report, require_repository=args.require_repository)
    except (OSError, json.JSONDecodeError, ValidationError) as exc:
        print(f"P5 report validation failed: {exc}")
        return 1
    print(f"P5 {args.kind} report validation PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
