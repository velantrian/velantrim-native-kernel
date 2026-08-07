from __future__ import annotations

import copy
import tempfile
import unittest
from pathlib import Path

from native_kernel.sqlite_profile.conformance import build_report
from tools.conformance.validate_p5_report import ValidationError, validate_sqlite

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "contracts" / "fixtures" / "fixture-pack.json"


class P5ReportValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp = tempfile.TemporaryDirectory()
        cls.report = build_report(
            FIXTURES,
            database_path=str(Path(cls.temp.name) / "validator.db"),
            conformance_level="C1",
            evidence_level="LOCALLY_TESTED",
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temp.cleanup()

    def test_valid_report(self) -> None:
        validate_sqlite(self.report, require_c2=False)

    def test_rejects_missing_assertion(self) -> None:
        candidate = copy.deepcopy(self.report)
        candidate["assertion_results"].pop()
        with self.assertRaises(ValidationError):
            validate_sqlite(candidate, require_c2=False)

    def test_rejects_supported_without_evidence(self) -> None:
        candidate = copy.deepcopy(self.report)
        item = next(value for value in candidate["assertion_results"] if value["status"] == "SUPPORTED")
        item.pop("evidence", None)
        with self.assertRaises(ValidationError):
            validate_sqlite(candidate, require_c2=False)

    def test_rejects_nk_epi_promotion(self) -> None:
        candidate = copy.deepcopy(self.report)
        item = next(value for value in candidate["assertion_results"] if value["assertion_id"] == "NK-EPI-001")
        item["status"] = "SUPPORTED"
        item["evidence"] = ["p4.registry.contracts"]
        with self.assertRaises(ValidationError):
            validate_sqlite(candidate, require_c2=False)

    def test_rejects_fake_c2_metadata(self) -> None:
        candidate = copy.deepcopy(self.report)
        candidate["kernel_runtime_conformance"] = "C2"
        candidate["evidence_level"] = "REPOSITORY_REPRODUCED"
        with self.assertRaises(ValidationError):
            validate_sqlite(candidate, require_c2=True)


if __name__ == "__main__":
    unittest.main()
