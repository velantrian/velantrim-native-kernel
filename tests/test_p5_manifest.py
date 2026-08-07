from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from tools.profiles.validate_p5_manifest import ManifestError, validate_manifest

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "profiles" / "sqlite-embedded-v0" / "p5-manifest.json"


class P5ManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_committed_manifest_is_valid(self) -> None:
        validate_manifest(self.manifest)

    def test_rejects_all_assertions_supported(self) -> None:
        candidate = copy.deepcopy(self.manifest)
        candidate["c3_assertion_coverage"].update(
            supported=72, partial=0, unsupported=0
        )
        with self.assertRaises(ManifestError):
            validate_manifest(candidate)

    def test_rejects_false_c3_without_repository_evidence(self) -> None:
        candidate = copy.deepcopy(self.manifest)
        candidate["repository_evidence"].update(
            status="NOT_RECORDED",
            head_sha=None,
            workflow_run_id=None,
            artifact_count=0,
        )
        with self.assertRaises(ManifestError):
            validate_manifest(candidate)

    def test_rejects_nk_epi_promotion(self) -> None:
        candidate = copy.deepcopy(self.manifest)
        candidate["c3_assertion_coverage"]["proposed_nk_epi_unsupported"] = 0
        with self.assertRaises(ManifestError):
            validate_manifest(candidate)

    def test_rejects_historical_recovery_claim(self) -> None:
        candidate = copy.deepcopy(self.manifest)
        candidate["issue_1_boundary"]["may_claim_recovery"] = True
        with self.assertRaises(ManifestError):
            validate_manifest(candidate)


if __name__ == "__main__":
    unittest.main()
