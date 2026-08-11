from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


evaluator = _load_module("bpv1_evaluate", ROOT / "tools" / "bpv1" / "evaluate.py")
admission_validator = _load_module("bpv1_validate_admission", ROOT / "tools" / "bpv1" / "validate_execution_admission.py")
digest_tool = _load_module("bpv1_plan_digest", ROOT / "tools" / "bpv1" / "plan_digest.py")

SPEC = json.loads((ROOT / "experiments" / "bpv1" / "BPV1-001" / "admission" / "fixtures.json").read_text(encoding="utf-8"))


def _passing_value(check: dict):
    op = check["op"]
    if op == "TRUE":
        return True
    if op == "FALSE":
        return False
    if op == "IN":
        return check["expected"][0]
    return check.get("expected")


def _put_path(target: dict, path: str, value) -> None:
    current = target
    parts = path.split(".")
    for part in parts[:-1]:
        current = current.setdefault(part, {})
    current[parts[-1]] = value


def passing_observations() -> dict:
    observations = {
        "protocol": "nk-bpv1-observations/1",
        "scenario_id": SPEC["scenario_id"],
        "plan_sha256": SPEC["plan_sha256"],
        "subject_id": "synthetic-oracle-selftest",
        "fixtures": {},
    }
    for fixture in SPEC["fixtures"]:
        row: dict = {}
        for check in fixture["checks"]:
            _put_path(row, check["path"], _passing_value(check))
        observations["fixtures"][fixture["fixture_id"]] = row
    for check in SPEC["global_checks"]:
        _put_path(observations, check["path"], _passing_value(check))
    return observations


class BPV1ExecutionAdmissionTests(unittest.TestCase):
    def test_repository_admission_package_remains_valid_regardless_of_subject_existence(self) -> None:
        admission_validator.validate(ROOT)
        subject_root = ROOT / "experiments" / "bpv1" / "BPV1-001" / "subject"
        if subject_root.exists():
            state = json.loads((ROOT / "project-state.json").read_text(encoding="utf-8"))
            validation = state["tracks"]["long_horizon_research"]["post_blueprint_validation"]
            self.assertEqual("ADMITTED_FOR_EXPERIMENT_ONLY", validation.get("bpv1_status"))

    def test_frozen_plan_sha256_is_exact(self) -> None:
        digest = digest_tool.digest_file(ROOT / "docs" / "research" / "BPV1_PREREGISTRATION.json")
        self.assertEqual("7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0", digest)

    def test_synthetic_complete_bundle_supports_scope(self) -> None:
        report = evaluator.evaluate(SPEC, passing_observations())
        self.assertEqual("SUPPORTED_FOR_SCOPE", report["outcome"])
        self.assertTrue(all(item["status"] == "PASS" for item in report["fixture_results"]))
        self.assertTrue(all(item["passed"] for item in report["global_checks"]))

    def test_unknown_coerced_to_false_refutes(self) -> None:
        observations = passing_observations()
        observations["fixtures"]["BPV1-FX01-UNKNOWN-NOT-FALSE"]["coerced_unknown_to_false"] = True
        report = evaluator.evaluate(SPEC, observations)
        self.assertEqual("REFUTED", report["outcome"])

    def test_missing_mandatory_observable_is_indeterminate(self) -> None:
        observations = passing_observations()
        del observations["fixtures"]["BPV1-FX08-FORGED-AUTHORITY"]["unsupported_or_failure_exposed"]
        report = evaluator.evaluate(SPEC, observations)
        self.assertEqual("INDETERMINATE", report["outcome"])

    def test_no_fixture_observations_is_not_tested(self) -> None:
        observations = passing_observations()
        observations["fixtures"] = {}
        report = evaluator.evaluate(SPEC, observations)
        self.assertEqual("NOT_TESTED", report["outcome"])

    def test_wrong_plan_digest_is_rejected_before_semantic_evaluation(self) -> None:
        observations = passing_observations()
        observations["plan_sha256"] = "0" * 64
        with self.assertRaisesRegex(evaluator.EvaluationError, "plan_sha256"):
            evaluator.evaluate(SPEC, observations)

    def test_bounded_state_cap_violation_refutes(self) -> None:
        observations = passing_observations()
        observations["workload"]["durable_bytes_at_512"] = 262145
        report = evaluator.evaluate(SPEC, observations)
        self.assertEqual("REFUTED", report["outcome"])

    def test_growth_rule_failure_refutes(self) -> None:
        observations = passing_observations()
        observations["workload"]["growth_rule_passed"] = False
        report = evaluator.evaluate(SPEC, observations)
        self.assertEqual("REFUTED", report["outcome"])

    def test_current_runtime_reuse_refutes_oracle_scope(self) -> None:
        observations = passing_observations()
        observations["subject"]["imports_current_native_kernel"] = True
        report = evaluator.evaluate(SPEC, observations)
        self.assertEqual("REFUTED", report["outcome"])

    def test_current_event_reducer_receipt_sql_reuse_each_refutes(self) -> None:
        for key in (
            "reuses_current_event_envelope",
            "reuses_current_reducer",
            "reuses_current_receipt_shape_as_oracle",
            "uses_current_sql_profile",
        ):
            with self.subTest(key=key):
                observations = passing_observations()
                observations["subject"][key] = True
                self.assertEqual("REFUTED", evaluator.evaluate(SPEC, observations)["outcome"])

    def test_admission_package_cannot_self_authorize(self) -> None:
        admission = json.loads((ROOT / "docs" / "research" / "BPV1_EXECUTION_ADMISSION.json").read_text(encoding="utf-8"))
        self.assertEqual("CANDIDATE_PACKAGE / EXECUTION_NOT_ADMITTED", admission["status"])
        self.assertFalse(admission["execution_authorized_by_this_package"])
        self.assertTrue(admission["separate_post_merge_state_checkpoint_required"])

    def test_result_vocabulary_remains_a10_exact(self) -> None:
        self.assertEqual(
            ["SUPPORTED_FOR_SCOPE", "WEAKENED", "REFUTED", "INDETERMINATE", "NOT_TESTED"],
            SPEC["result_vocabulary"],
        )


if __name__ == "__main__":
    unittest.main()
