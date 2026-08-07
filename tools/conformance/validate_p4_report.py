from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / "tools" / "conformance"
sys.path.insert(0, str(TOOLS))

import runner  # noqa: E402

PROFILE_ID = "native-kernel/postgresql-reference"
EXPECTED_COUNTS = {
    "SUPPORTED": 41,
    "PARTIAL": 13,
    "UNSUPPORTED": 18,
    "FAILED": 0,
}
REQUIRED_CHECKS = {
    "p4.registry.contracts",
    "p4.identity.golden",
    "p4.identity.invalid",
    "p4.semantic.roles",
    "p4.authority.policy",
    "p4.receipts.boundaries",
    "p4.reducer.determinism",
    "p4.reducer.failures",
    "p4.deletion.semantic",
    "p4.postgresql.migrations",
    "p4.postgresql.writer-fencing",
    "p4.postgresql.append-idempotency",
    "p4.postgresql.rollback-ordering",
    "p4.postgresql.replay-projection",
    "p4.postgresql.stale-head",
    "p4.postgresql.corruption",
    "p4.environment.metadata",
    "p4.report.traceability",
}


class P4ReportError(ValueError):
    pass


def _object(name: str, value: object) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise P4ReportError(f"{name} must be an object")
    return value


def validate(report: Mapping[str, Any], *, require_c2: bool) -> None:
    try:
        runner.validate_evidence_report(dict(report))
    except runner.ContractError as exc:
        raise P4ReportError(str(exc)) from exc

    if report.get("profile_id") != PROFILE_ID:
        raise P4ReportError(f"profile_id must remain {PROFILE_ID}")
    if report.get("support_state") != "PARTIAL":
        raise P4ReportError("P4 profile support_state must remain PARTIAL")
    if report.get("kernel_runtime_conformance") not in {"C1", "C2"}:
        raise P4ReportError("P4 report may declare only C1 or C2")
    if report.get("evidence_level") not in {
        "LOCALLY_TESTED",
        "REPOSITORY_REPRODUCED",
    }:
        raise P4ReportError("invalid P4 evidence level")
    if require_c2:
        if report.get("kernel_runtime_conformance") != "C2":
            raise P4ReportError("repository validation requires C2")
        if report.get("evidence_level") != "REPOSITORY_REPRODUCED":
            raise P4ReportError(
                "repository validation requires REPOSITORY_REPRODUCED"
            )

    checks_value = report.get("checks")
    if not isinstance(checks_value, list):
        raise P4ReportError("checks must be a list")
    check_map: dict[str, Mapping[str, Any]] = {}
    for raw in checks_value:
        check = _object("check", raw)
        check_id = check.get("check_id")
        if not isinstance(check_id, str) or not check_id:
            raise P4ReportError("check_id must be non-empty")
        if check_id in check_map:
            raise P4ReportError(f"duplicate check {check_id}")
        if check.get("status") != "PASS":
            raise P4ReportError(f"{check_id} did not PASS")
        detail = check.get("detail")
        if not isinstance(detail, str) or not detail:
            raise P4ReportError(f"{check_id} must include detail")
        check_map[check_id] = check
    if set(check_map) != REQUIRED_CHECKS:
        raise P4ReportError(
            "check coverage mismatch: "
            f"missing={sorted(REQUIRED_CHECKS - set(check_map))} "
            f"extra={sorted(set(check_map) - REQUIRED_CHECKS)}"
        )

    metadata = str(check_map["p4.environment.metadata"]["detail"])
    required_metadata = ("profile=", "commit=", "run=", "python=", "postgresql=")
    if any(marker not in metadata for marker in required_metadata):
        raise P4ReportError("environment metadata is incomplete")
    if require_c2 and any(
        token in metadata
        for token in (
            "commit=LOCAL",
            "run=LOCAL",
            "python=LOCAL",
            "postgresql=LOCAL",
        )
    ):
        raise P4ReportError("C2 metadata cannot contain LOCAL placeholders")

    results = report.get("assertion_results")
    if not isinstance(results, list):
        raise P4ReportError("assertion_results must be a list")
    counts = {status: 0 for status in EXPECTED_COUNTS}
    result_map: dict[str, Mapping[str, Any]] = {}
    for raw in results:
        result = _object("assertion result", raw)
        assertion_id = result.get("assertion_id")
        status = result.get("status")
        if not isinstance(assertion_id, str):
            raise P4ReportError("assertion_id must be a string")
        if assertion_id in result_map:
            raise P4ReportError(f"duplicate assertion result {assertion_id}")
        if status not in counts:
            raise P4ReportError(f"{assertion_id}: invalid status")
        counts[str(status)] += 1
        limitations = result.get("limitations")
        if not isinstance(limitations, list) or not limitations or any(
            not isinstance(item, str) or not item for item in limitations
        ):
            raise P4ReportError(f"{assertion_id}: limitations are required")
        evidence = result.get("evidence", [])
        if not isinstance(evidence, list):
            raise P4ReportError(f"{assertion_id}: evidence must be a list")
        if status in {"SUPPORTED", "PARTIAL"} and not evidence:
            raise P4ReportError(f"{assertion_id}: {status} requires evidence")
        for check_id in evidence:
            if check_id not in check_map:
                raise P4ReportError(
                    f"{assertion_id}: unknown evidence check {check_id}"
                )
        result_map[assertion_id] = result
    if counts != EXPECTED_COUNTS:
        raise P4ReportError(f"unexpected support counts {counts}")

    for index in range(1, 9):
        assertion_id = f"NK-EPI-{index:03d}"
        result = result_map.get(assertion_id)
        if result is None or result.get("status") != "UNSUPPORTED":
            raise P4ReportError(f"{assertion_id} must remain UNSUPPORTED")
        joined = "\n".join(str(item) for item in result.get("limitations", []))
        if "PROPOSED" not in joined:
            raise P4ReportError(
                f"{assertion_id} must retain proposed-family limitation"
            )

    limitations = report.get("limitations")
    if not isinstance(limitations, list):
        raise P4ReportError("report limitations must be a list")
    joined = "\n".join(str(item) for item in limitations)
    for phrase in (
        "C3",
        "physical deletion",
        "truth",
        "clean/postgresql-reference/0.1",
    ):
        if phrase not in joined:
            raise P4ReportError(f"missing report limitation: {phrase}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a P4 evidence report")
    parser.add_argument("--require-c2", action="store_true")
    parser.add_argument("report", type=Path)
    args = parser.parse_args(argv)
    try:
        value = json.loads(args.report.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise P4ReportError("report root must be an object")
        validate(value, require_c2=args.require_c2)
    except (OSError, json.JSONDecodeError, P4ReportError) as exc:
        print(f"P4 report invalid: {exc}", file=sys.stderr)
        return 1
    counts = {
        status: sum(
            1
            for item in value["assertion_results"]
            if item["status"] == status
        )
        for status in EXPECTED_COUNTS
    }
    print(
        "P4 report valid; "
        f"level={value['kernel_runtime_conformance']}; "
        f"evidence={value['evidence_level']}; counts={counts}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
