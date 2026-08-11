#!/usr/bin/env python3
"""Validate BPV1-001 execution-admission package without admitting execution."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tomllib
from pathlib import Path
from typing import Any, Mapping

PLAN_ID = "BPV1-001-cross-lineage-bounded-accountability-v1"
PLAN_PATH = "docs/research/BPV1_PREREGISTRATION.json"
PLAN_MERGE = "a538d7f1e28858a88b9ee777ac7d6e05b85943db"
PLAN_SHA256 = "15c830ed195762d571cf675900303dfbfb29bf01a5cde2aac814388319585a91"
ADMISSION_PATH = "docs/research/BPV1_EXECUTION_ADMISSION.json"
FIXTURES_PATH = "experiments/bpv1/BPV1-001/admission/fixtures.json"
BOUNDARY_PATH = "experiments/bpv1/BPV1-001/admission/source-boundary.json"
TOOLCHAIN_PATH = "experiments/bpv1/BPV1-001/rust-toolchain.toml"
SUBJECT_ROOT = "experiments/bpv1/BPV1-001/subject"
EXPECTED_RUST = "1.97.1"


class AdmissionError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AdmissionError(message)


def _load_json(path: Path, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AdmissionError(f"cannot read {label}: {exc}") from exc
    _require(isinstance(value, dict), f"{label} root must be an object")
    return value


def _git(repo: Path, *args: str, binary: bool = False):
    result = subprocess.run(["git", "-C", str(repo), *args], check=False, capture_output=True, text=not binary)
    if result.returncode != 0:
        detail = result.stderr.decode() if binary else result.stderr
        raise AdmissionError(detail.strip() or f"git {' '.join(args)} failed")
    return result.stdout


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _check_map(spec: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    checks = spec.get("global_checks")
    _require(isinstance(checks, list), "fixture global_checks must be a list")
    result: dict[str, Mapping[str, Any]] = {}
    for item in checks:
        _require(isinstance(item, Mapping), "global check must be an object")
        path = item.get("path")
        _require(isinstance(path, str) and path, "global check path required")
        _require(path not in result, f"duplicate global check path: {path}")
        result[path] = item
    return result


def validate(repo: Path) -> None:
    repo = repo.resolve()
    plan_path = repo / PLAN_PATH
    admission_path = repo / ADMISSION_PATH
    fixture_path = repo / FIXTURES_PATH
    boundary_path = repo / BOUNDARY_PATH
    toolchain_path = repo / TOOLCHAIN_PATH

    plan_bytes = plan_path.read_bytes()
    _require(_sha256(plan_bytes) == PLAN_SHA256, "current BPV-1 plan SHA-256 drift")
    plan = _load_json(plan_path, "BPV-1 preregistration")
    _require(plan.get("protocol") == "nk-bpv1-preregistration/1", "plan protocol drift")
    _require(plan.get("plan_id") == PLAN_ID, "plan identity drift")
    _require(plan.get("execution_authorized") is False, "preregistered plan must not authorize execution")
    _require(plan.get("next_gate_after_plan_merge") == "BPV1_EXECUTION_ADMISSION", "plan next gate drift")

    if (repo / ".git").exists():
        result = subprocess.run(["git", "-C", str(repo), "merge-base", "--is-ancestor", PLAN_MERGE, "HEAD"], check=False)
        _require(result.returncode == 0, "authoritative BPV-1 plan merge is not an ancestor of admission candidate")
        historical = _git(repo, "show", f"{PLAN_MERGE}:{PLAN_PATH}", binary=True)
        _require(_sha256(historical) == PLAN_SHA256, "authoritative plan-merge bytes do not match frozen SHA-256")
        _require(historical == plan_bytes, "current preregistration bytes differ from authoritative plan-merge bytes")

    admission = _load_json(admission_path, "execution admission record")
    _require(admission.get("protocol") == "nk-bpv1-execution-admission/1", "admission protocol drift")
    _require(admission.get("admission_id") == "BPV1-001-execution-admission-v1", "admission identity drift")
    _require(admission.get("scenario_id") == PLAN_ID, "admission scenario drift")
    _require(admission.get("status") == "CANDIDATE_PACKAGE / EXECUTION_NOT_ADMITTED", "candidate admission status drift")
    _require(admission.get("execution_authorized_by_this_package") is False, "admission package cannot self-authorize execution")
    _require(admission.get("separate_post_merge_state_checkpoint_required") is True, "separate state checkpoint must remain required")
    admission_plan = admission.get("plan")
    _require(isinstance(admission_plan, Mapping), "admission plan binding required")
    _require(admission_plan.get("authoritative_merge") == PLAN_MERGE, "admission plan merge binding drift")
    _require(admission_plan.get("sha256") == PLAN_SHA256, "admission plan digest binding drift")
    _require(admission_plan.get("path") == PLAN_PATH, "admission plan path drift")

    fixtures = _load_json(fixture_path, "fixture specification")
    _require(fixtures.get("protocol") == "nk-bpv1-fixtures/1", "fixture protocol drift")
    _require(fixtures.get("scenario_id") == PLAN_ID, "fixture scenario drift")
    _require(fixtures.get("plan_merge") == PLAN_MERGE, "fixture plan merge drift")
    _require(fixtures.get("plan_sha256") == PLAN_SHA256, "fixture plan digest drift")
    _require(fixtures.get("oracle_authority") == "BPV1-ORACLE-001", "fixture oracle authority drift")
    fixture_rows = fixtures.get("fixtures")
    _require(isinstance(fixture_rows, list), "fixture inventory must be a list")
    fixture_ids = [item.get("fixture_id") for item in fixture_rows if isinstance(item, Mapping)]
    expected_ids = [item.get("id") for item in plan.get("fixture_families", []) if isinstance(item, Mapping)]
    _require(len(fixture_rows) == len(fixture_ids) == 12, "fixture oracle must contain exactly 12 object fixtures")
    _require(fixture_ids == expected_ids, "fixture oracle ids/order must match preregistered fixture families exactly")
    _require(all(item.get("mandatory") is True for item in fixture_rows if isinstance(item, Mapping)), "all BPV1-001 fixtures must remain mandatory")
    _require(all(isinstance(item.get("checks"), list) and item.get("checks") for item in fixture_rows if isinstance(item, Mapping)), "each fixture requires at least one executable check")

    workload = plan.get("workload")
    _require(isinstance(workload, Mapping), "preregistered workload required")
    checks = _check_map(fixtures)
    expected_globals = {
        "workload.mutation_count": workload.get("scripted_mutations"),
        "workload.checkpoint_count": len(workload.get("checkpoints_after_mutations", [])),
        "workload.durable_bytes_at_512": workload.get("durable_state_byte_cap"),
        "workload.retained_detailed_predecessors": workload.get("retained_detailed_predecessor_cap"),
        "workload.loss_witness_count": workload.get("loss_witness_cap"),
    }
    for path, expected in expected_globals.items():
        _require(path in checks, f"missing frozen workload check: {path}")
        _require(checks[path].get("expected") == expected, f"workload threshold drift for {path}")
    for required_false in (
        "subject.authoritative_per_operation_append_log",
        "subject.exact_replay_required",
        "subject.imports_current_native_kernel",
        "subject.reuses_current_event_envelope",
        "subject.reuses_current_reducer",
        "subject.reuses_current_receipt_shape_as_oracle",
        "subject.uses_current_sql_profile",
    ):
        _require(checks.get(required_false, {}).get("op") == "FALSE", f"required anti-capture check missing: {required_false}")

    boundary = _load_json(boundary_path, "source boundary")
    _require(boundary.get("protocol") == "nk-bpv1-source-boundary/1", "source boundary protocol drift")
    _require(boundary.get("scenario_id") == PLAN_ID, "source boundary scenario drift")
    _require(boundary.get("plan_merge") == PLAN_MERGE and boundary.get("plan_sha256") == PLAN_SHA256, "source boundary plan binding drift")
    _require(boundary.get("subject_root") == SUBJECT_ROOT, "subject root drift")
    _require(boundary.get("subject_must_not_exist_before_admission_checkpoint") is True, "subject absence rule drift")
    _require(boundary.get("rust_channel") == EXPECTED_RUST, "source-boundary Rust toolchain drift")
    _require(boundary.get("language_role") == "EXPERIMENTAL_INSTRUMENT_NOT_CANON", "Rust language role drift")
    _require(boundary.get("workspace_integration") == "FORBIDDEN", "workspace integration must remain forbidden")
    _require(boundary.get("runtime_registration") == "FORBIDDEN", "runtime registration must remain forbidden")
    _require(boundary.get("product_profile_registration") == "FORBIDDEN", "product profile registration must remain forbidden")
    _require(not (repo / SUBJECT_ROOT).exists(), "BPV1 subject source must not exist in execution-admission package")

    with toolchain_path.open("rb") as handle:
        toolchain = tomllib.load(handle)
    toolchain_section = toolchain.get("toolchain")
    _require(isinstance(toolchain_section, Mapping), "rust-toolchain.toml must contain [toolchain]")
    _require(toolchain_section.get("channel") == EXPECTED_RUST, "rust-toolchain channel drift")
    _require(toolchain_section.get("profile") == "minimal", "rust-toolchain profile must remain minimal")

    oracle = admission.get("oracle")
    _require(isinstance(oracle, Mapping), "admission oracle binding required")
    _require(oracle.get("fixture_spec") == FIXTURES_PATH, "admission fixture path drift")
    _require(oracle.get("evaluator") == "tools/bpv1/evaluate.py", "admission evaluator path drift")
    _require(oracle.get("self_test") == "tests/test_bpv1_execution_admission.py", "admission self-test path drift")
    _require(oracle.get("subject_may_define_expected_outcomes") is False, "subject cannot define expected outcomes")
    _require(oracle.get("post_result_normative_edits_under_same_scenario") == "FORBIDDEN", "post-result normative edits must remain forbidden")
    for required_path in (
        "tools/bpv1/evaluate.py",
        "tools/bpv1/audit_scope.py",
        "tools/bpv1/plan_digest.py",
        "tests/test_bpv1_execution_admission.py",
        "docs/research/BPV1_EXECUTION_ADMISSION.md",
        "docs/research/BPV1_EXECUTION_ADMISSION.ru.md",
    ):
        _require((repo / required_path).is_file(), f"missing execution-admission artifact: {required_path}")

    state = _load_json(repo / "project-state.json", "project state")
    validation = state.get("tracks", {}).get("long_horizon_research", {}).get("post_blueprint_validation", {})
    _require(validation.get("bpv1_status") == "BLOCKED_PENDING_EXECUTION_ADMISSION", "current machine state must remain blocked during admission-package PR")
    _require(validation.get("product_runtime_thaw") is False, "product runtime must remain frozen")
    _require(state.get("status", {}).get("production_authorized") is False, "production must remain unauthorized")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    args = parser.parse_args()
    try:
        validate(args.repo)
    except (AdmissionError, OSError, json.JSONDecodeError, tomllib.TOMLDecodeError) as exc:
        print(f"BPV1 execution admission validation FAILED: {exc}", file=sys.stderr)
        return 1
    print("BPV1 execution admission package PASS; package=candidate; subject=absent; execution=not_admitted; runtime_expansion_frozen=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
