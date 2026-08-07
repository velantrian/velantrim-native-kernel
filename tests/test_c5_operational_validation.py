from __future__ import annotations

import copy
import json
import os
import unittest
from pathlib import Path

from c4_test_support import make_c3_report
from native_kernel.operational_validation import (
    OperationalValidationError,
    ScenarioResult,
    build_report,
    canary_leaks,
    load_json,
    validate_plan,
    validate_report,
)
from native_kernel.shadow_evaluation import evaluate

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "contracts" / "operational-plan-v1.json"
C4_DATASET = ROOT / "contracts" / "shadow-workload-v1.json"


def make_c4() -> dict:
    dataset_text = C4_DATASET.read_text(encoding="utf-8")
    dataset = load_json(C4_DATASET)
    return evaluate(dataset, make_c3_report(ROOT), dataset_text=dataset_text)


def fake_results(plan: dict) -> list[ScenarioResult]:
    canary = plan["privacy"]["canary_tokens"][0]
    values: list[ScenarioResult] = []
    for item in plan["scenarios"]:
        metrics = {}
        if item["id"].startswith("resilience."):
            metrics["p95_append_ms"] = 1.0
        detail = (
            f"redacted before output: {canary}"
            if item["id"] == "privacy.canary-redaction"
            else "bounded synthetic scenario passed"
        )
        values.append(
            ScenarioResult(
                scenario_id=item["id"],
                category=item["category"],
                profile=item["profile"],
                status="PASS",
                duration_ms=1.0,
                detail=detail,
                metrics=metrics,
            )
        )
    return values


class C5OperationalValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.plan = load_json(PLAN)
        self.plan_bytes = PLAN.read_bytes()
        self.c4 = make_c4()
        self.c4_bytes = (json.dumps(self.c4, sort_keys=True, indent=2) + "\n").encode()

    def test_approved_plan_validates(self) -> None:
        validate_plan(self.plan)
        self.assertEqual(len(self.plan["scenarios"]), 18)

    def test_bounded_report_passes_and_preserves_c4_map(self) -> None:
        report = build_report(
            self.plan,
            self.c4,
            fake_results(self.plan),
            plan_bytes=self.plan_bytes,
            c4_bytes=self.c4_bytes,
        )
        validate_report(report, plan=self.plan, plan_bytes=self.plan_bytes)
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["operational_validation"], "C5_BOUNDED_REHEARSAL")
        self.assertEqual(report["kernel_runtime_conformance"], "C4")
        self.assertEqual(
            report["metrics"]["assertion_counts"],
            {"SUPPORTED": 45, "PARTIAL": 10, "UNSUPPORTED": 17, "FAILED": 0},
        )
        self.assertEqual(report["metrics"]["scenario_count"], 18)
        self.assertEqual(report["metrics"]["receipt_count"], 18)

    def test_canary_is_redacted_from_report_and_receipts(self) -> None:
        report = build_report(
            self.plan,
            self.c4,
            fake_results(self.plan),
            plan_bytes=self.plan_bytes,
            c4_bytes=self.c4_bytes,
        )
        self.assertFalse(canary_leaks(report, self.plan["privacy"]["canary_tokens"]))
        row = next(
            item for item in report["scenario_results"]
            if item["scenario_id"] == "privacy.canary-redaction"
        )
        self.assertIn("[REDACTED]", row["detail"])

    def test_failed_scenario_fails_closed(self) -> None:
        results = fake_results(self.plan)
        results[0] = ScenarioResult(
            scenario_id=results[0].scenario_id,
            category=results[0].category,
            profile=results[0].profile,
            status="FAIL",
            duration_ms=1.0,
            detail="injected failure",
            metrics={},
        )
        report = build_report(
            self.plan,
            self.c4,
            results,
            plan_bytes=self.plan_bytes,
            c4_bytes=self.c4_bytes,
        )
        self.assertEqual(report["status"], "FAIL")
        with self.assertRaisesRegex(OperationalValidationError, "did not PASS"):
            validate_report(report, plan=self.plan, plan_bytes=self.plan_bytes)

    def test_unsafe_deployment_boundary_is_rejected(self) -> None:
        plan = copy.deepcopy(self.plan)
        plan["deployment_boundary"]["live_user_data"] = True
        with self.assertRaisesRegex(OperationalValidationError, "unsafe deployment boundary"):
            validate_plan(plan)

    def test_receipt_overclaim_is_rejected(self) -> None:
        report = build_report(
            self.plan,
            self.c4,
            fake_results(self.plan),
            plan_bytes=self.plan_bytes,
            c4_bytes=self.c4_bytes,
        )
        report["receipts"][0]["production_approved"] = True
        with self.assertRaisesRegex(OperationalValidationError, "Receipt overclaim"):
            validate_report(report, plan=self.plan, plan_bytes=self.plan_bytes)

    def test_repository_metadata_required_when_requested(self) -> None:
        old = dict(os.environ)
        try:
            for name in (
                "NK_EVIDENCE_LEVEL",
                "NK_EVIDENCE_COMMIT",
                "NK_EVIDENCE_RUN_ID",
                "NK_PYTHON_VERSION",
                "NK_POSTGRESQL_VERSION",
                "NK_SQLITE_VERSION",
                "NK_RUNNER_OS",
            ):
                os.environ.pop(name, None)
            report = build_report(
                self.plan,
                self.c4,
                fake_results(self.plan),
                plan_bytes=self.plan_bytes,
                c4_bytes=self.c4_bytes,
            )
            with self.assertRaisesRegex(OperationalValidationError, "wrong C5 repository evidence level"):
                validate_report(
                    report,
                    plan=self.plan,
                    plan_bytes=self.plan_bytes,
                    require_repository=True,
                )

            os.environ.update({
                "NK_EVIDENCE_LEVEL": "REPOSITORY_REPRODUCED_OPERATIONAL_REHEARSAL",
                "NK_EVIDENCE_COMMIT": "a" * 40,
                "NK_EVIDENCE_RUN_ID": "12345",
                "NK_PYTHON_VERSION": "3.11",
                "NK_POSTGRESQL_VERSION": "16",
                "NK_SQLITE_VERSION": "3.45.1",
                "NK_RUNNER_OS": "ubuntu-24.04",
            })
            report = build_report(
                self.plan,
                self.c4,
                fake_results(self.plan),
                plan_bytes=self.plan_bytes,
                c4_bytes=self.c4_bytes,
            )
            validate_report(
                report,
                plan=self.plan,
                plan_bytes=self.plan_bytes,
                require_repository=True,
            )
        finally:
            os.environ.clear()
            os.environ.update(old)


if __name__ == "__main__":
    unittest.main()
