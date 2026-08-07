from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools" / "profiles"
sys.path.insert(0, str(TOOLS))

import validate_p4_manifest  # noqa: E402

MANIFEST = ROOT / "profiles" / "postgresql-reference-v0" / "p4-manifest.json"


class P4ManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.data = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_committed_manifest_is_valid(self) -> None:
        validate_p4_manifest.validate(self.data)

    def test_support_count_drift_is_rejected(self) -> None:
        changed = copy.deepcopy(self.data)
        changed["assertion_coverage"]["supported"] = 42
        with self.assertRaisesRegex(
            validate_p4_manifest.ManifestError,
            "support summary drifted",
        ):
            validate_p4_manifest.validate(changed)

    def test_false_repository_c2_is_rejected(self) -> None:
        changed = copy.deepcopy(self.data)
        changed["conformance_state"]["repository_c2"] = "REPOSITORY_REPRODUCED"
        with self.assertRaisesRegex(
            validate_p4_manifest.ManifestError,
            "without repository evidence",
        ):
            validate_p4_manifest.validate(changed)

    def test_c3_and_p5_promotion_are_rejected(self) -> None:
        changed = copy.deepcopy(self.data)
        changed["conformance_state"]["c3"] = "REPOSITORY_REPRODUCED"
        with self.assertRaisesRegex(validate_p4_manifest.ManifestError, "promote C3"):
            validate_p4_manifest.validate(changed)
        changed = copy.deepcopy(self.data)
        changed["forbidden_in_p4"] = [
            item
            for item in changed["forbidden_in_p4"]
            if "P5 SQLite" not in item
        ]
        with self.assertRaisesRegex(validate_p4_manifest.ManifestError, "P5 SQLite"):
            validate_p4_manifest.validate(changed)

    def test_recovery_and_nk_epi_promotion_are_rejected(self) -> None:
        changed = copy.deepcopy(self.data)
        changed["issue_1_boundary"]["may_claim_recovery"] = True
        with self.assertRaisesRegex(validate_p4_manifest.ManifestError, "recovery"):
            validate_p4_manifest.validate(changed)
        changed = copy.deepcopy(self.data)
        changed["assertion_coverage"]["proposed_nk_epi_unsupported"] = 0
        with self.assertRaisesRegex(
            validate_p4_manifest.ManifestError,
            "support summary drifted",
        ):
            validate_p4_manifest.validate(changed)


if __name__ == "__main__":
    unittest.main()
