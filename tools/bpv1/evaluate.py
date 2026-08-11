#!/usr/bin/env python3
"""Evaluate BPV1-001 implementation-neutral observations against the frozen oracle."""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

FIXTURE_PROTOCOL = "nk-bpv1-fixtures/1"
OBSERVATION_PROTOCOL = "nk-bpv1-observations/1"
EVALUATION_PROTOCOL = "nk-bpv1-evaluation/1"


class EvaluationError(ValueError):
    pass


@dataclass(frozen=True)
class CheckResult:
    path: str
    passed: bool
    missing: bool
    expected: Any
    actual: Any
    op: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "op": self.op,
            "passed": self.passed,
            "missing": self.missing,
            "expected": self.expected,
            "actual": self.actual,
        }


def _load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise EvaluationError(f"cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise EvaluationError(f"JSON root must be an object: {path}")
    return value


def _get_path(value: Mapping[str, Any], path: str) -> tuple[bool, Any]:
    current: Any = value
    for part in path.split("."):
        if not isinstance(current, Mapping) or part not in current:
            return False, None
        current = current[part]
    return True, current


def _evaluate_check(container: Mapping[str, Any], check: Mapping[str, Any]) -> CheckResult:
    path = str(check.get("path", ""))
    op = str(check.get("op", ""))
    if not path or not op:
        raise EvaluationError("each check requires non-empty path and op")
    present, actual = _get_path(container, path)
    expected = check.get("expected")
    if not present:
        return CheckResult(path, False, True, expected, None, op)

    if op == "TRUE":
        passed = actual is True
        expected = True
    elif op == "FALSE":
        passed = actual is False
        expected = False
    elif op == "EQ":
        passed = actual == expected
    elif op == "IN":
        if not isinstance(expected, list) or not expected:
            raise EvaluationError(f"IN check requires non-empty expected list: {path}")
        passed = actual in expected
    elif op == "LE":
        passed = isinstance(actual, (int, float)) and not isinstance(actual, bool) and isinstance(expected, (int, float)) and not isinstance(expected, bool) and actual <= expected
    elif op == "GE":
        passed = isinstance(actual, (int, float)) and not isinstance(actual, bool) and isinstance(expected, (int, float)) and not isinstance(expected, bool) and actual >= expected
    else:
        raise EvaluationError(f"unsupported check operator {op!r} at {path}")
    return CheckResult(path, passed, False, expected, actual, op)


def evaluate(spec: Mapping[str, Any], observations: Mapping[str, Any]) -> dict[str, Any]:
    if spec.get("protocol") != FIXTURE_PROTOCOL:
        raise EvaluationError("fixture protocol mismatch")
    if observations.get("protocol") != OBSERVATION_PROTOCOL:
        raise EvaluationError("observation protocol mismatch")
    for field in ("scenario_id", "plan_sha256"):
        if observations.get(field) != spec.get(field):
            raise EvaluationError(f"observation {field} does not match frozen oracle")

    fixture_specs = spec.get("fixtures")
    if not isinstance(fixture_specs, list) or not fixture_specs:
        raise EvaluationError("frozen oracle must contain fixtures")
    observed_fixtures = observations.get("fixtures")
    if not isinstance(observed_fixtures, Mapping):
        raise EvaluationError("observations.fixtures must be an object")

    fixture_results: list[dict[str, Any]] = []
    any_failure = False
    any_missing = False
    present_fixture_count = 0

    for fixture in fixture_specs:
        if not isinstance(fixture, Mapping):
            raise EvaluationError("fixture entry must be an object")
        fixture_id = str(fixture.get("fixture_id", ""))
        mandatory = fixture.get("mandatory") is True
        fixture_observation = observed_fixtures.get(fixture_id)
        if fixture_observation is None:
            if mandatory:
                any_missing = True
            fixture_results.append({
                "fixture_id": fixture_id,
                "mandatory": mandatory,
                "status": "NOT_OBSERVED",
                "checks": [],
            })
            continue
        if not isinstance(fixture_observation, Mapping):
            raise EvaluationError(f"fixture observation must be an object: {fixture_id}")
        present_fixture_count += 1
        checks = fixture.get("checks")
        if not isinstance(checks, list) or not checks:
            raise EvaluationError(f"fixture has no checks: {fixture_id}")
        results = [_evaluate_check(fixture_observation, check) for check in checks if isinstance(check, Mapping)]
        if len(results) != len(checks):
            raise EvaluationError(f"fixture contains non-object check: {fixture_id}")
        missing = any(result.missing for result in results)
        failed = any(not result.passed and not result.missing for result in results)
        any_missing = any_missing or (mandatory and missing)
        any_failure = any_failure or (mandatory and failed)
        status = "PASS" if not missing and not failed else ("INDETERMINATE" if missing and not failed else "FAIL")
        fixture_results.append({
            "fixture_id": fixture_id,
            "mandatory": mandatory,
            "status": status,
            "checks": [result.as_dict() for result in results],
        })

    global_checks = spec.get("global_checks")
    if not isinstance(global_checks, list) or not global_checks:
        raise EvaluationError("frozen oracle must contain global checks")
    global_results = [_evaluate_check(observations, check) for check in global_checks if isinstance(check, Mapping)]
    if len(global_results) != len(global_checks):
        raise EvaluationError("global check list contains non-object entry")
    global_missing = any(result.missing for result in global_results)
    global_failed = any(not result.passed and not result.missing for result in global_results)
    any_missing = any_missing or global_missing
    any_failure = any_failure or global_failed

    if present_fixture_count == 0:
        outcome = "NOT_TESTED"
    elif any_failure:
        outcome = "REFUTED"
    elif any_missing:
        outcome = "INDETERMINATE"
    else:
        outcome = "SUPPORTED_FOR_SCOPE"

    return {
        "protocol": EVALUATION_PROTOCOL,
        "scenario_id": spec["scenario_id"],
        "plan_sha256": spec["plan_sha256"],
        "oracle_authority": spec.get("oracle_authority"),
        "outcome": outcome,
        "fixture_results": fixture_results,
        "global_checks": [result.as_dict() for result in global_results],
        "non_claims": [
            "This evaluator result is scoped to BPV1-001 only.",
            "SUPPORTED_FOR_SCOPE is not Final Canon, production readiness, or universal substrate portability.",
            "The evaluator does not establish independent team, custody, or computation-model evidence.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("observations", type=Path)
    parser.add_argument("--spec", type=Path, default=Path("experiments/bpv1/BPV1-001/admission/fixtures.json"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        report = evaluate(_load_json(args.spec), _load_json(args.observations))
    except EvaluationError as exc:
        print(f"BPV1 evaluator rejected input: {exc}")
        return 2
    rendered = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
