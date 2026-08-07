from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from c4_test_support import make_c3_report
from native_kernel.operational_validation import ScenarioResult, build_report, load_json
from native_kernel.shadow_evaluation import evaluate
from tools.operations.validate_c5_report import validate_backup
from native_kernel.operational_validation import OperationalValidationError

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "contracts" / "operational-plan-v1.json"
C4_DATASET = ROOT / "contracts" / "shadow-workload-v1.json"


class C5ReportValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.plan = load_json(PLAN)
        dataset_text = C4_DATASET.read_text(encoding="utf-8")
        self.c4 = evaluate(
            load_json(C4_DATASET),
            make_c3_report(ROOT),
            dataset_text=dataset_text,
        )
        self.results = [
            ScenarioResult(
                scenario_id=item["id"],
                category=item["category"],
                profile=item["profile"],
                status="PASS",
                duration_ms=1.0,
                detail="scenario passed",
                metrics={"p95_append_ms": 1.0} if item["id"].startswith("resilience.") else {},
            )
            for item in self.plan["scenarios"]
        ]

    def test_backup_validator_accepts_exact_digest(self) -> None:
        from native_kernel.operational_validation import canonical_json_bytes, sha256_digest
        backup = {
            "protocol": "nk-operational-backup/1",
            "source_profile": "native-kernel/postgresql-reference",
            "source_instance": "instance:test",
            "event_count": 1,
            "last_event_hash": "nke1:" + "0" * 64,
            "events": [{"global_seq": 1, "event_hash": "nke1:" + "0" * 64}],
            "limitations": [
                "Application-level logical export only.",
                "Not a physical PostgreSQL backup or managed-provider disaster-recovery proof.",
            ],
        }
        backup["backup_digest"] = sha256_digest(canonical_json_bytes(backup))
        validate_backup(backup, canaries=tuple(self.plan["privacy"]["canary_tokens"]))

    def test_backup_digest_drift_is_rejected(self) -> None:
        backup = {
            "protocol": "nk-operational-backup/1",
            "event_count": 1,
            "events": [{"global_seq": 1}],
            "backup_digest": "sha256:" + "0" * 64,
            "limitations": ["Not a physical PostgreSQL backup."],
        }
        with self.assertRaisesRegex(OperationalValidationError, "backup digest mismatch"):
            validate_backup(backup, canaries=tuple(self.plan["privacy"]["canary_tokens"]))

    def test_report_prerequisite_digest_is_stable(self) -> None:
        c4_bytes = (json.dumps(self.c4, sort_keys=True, indent=2) + "\n").encode()
        report = build_report(
            self.plan,
            self.c4,
            self.results,
            plan_bytes=PLAN.read_bytes(),
            c4_bytes=c4_bytes,
        )
        self.assertTrue(report["prerequisite"]["sha256"].startswith("sha256:"))
        altered = copy.deepcopy(report)
        altered["prerequisite"]["sha256"] = "sha256:" + "0" * 64
        self.assertNotEqual(altered["prerequisite"]["sha256"], report["prerequisite"]["sha256"])


if __name__ == "__main__":
    unittest.main()
