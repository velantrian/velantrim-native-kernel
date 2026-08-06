from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.profiles.validate_manifest import ManifestError, load_json, validate_manifest

REGISTRY = load_json(ROOT / "contracts" / "registry.json")
MANIFEST = load_json(ROOT / "profiles" / "postgresql-reference-v0" / "profile-manifest.json")


class ProfileManifestTests(unittest.TestCase):
    def test_current_manifest_passes(self) -> None:
        report = validate_manifest(copy.deepcopy(MANIFEST), REGISTRY)
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["assertions"], 72)
        self.assertEqual(report["deferred_epi"], 8)
        self.assertEqual(report["runtime_support"], "UNSUPPORTED")

    def test_missing_assertion_is_rejected(self) -> None:
        manifest = copy.deepcopy(MANIFEST)
        manifest["assertion_plan"].pop()
        with self.assertRaises(ManifestError):
            validate_manifest(manifest, REGISTRY)

    def test_duplicate_assertion_is_rejected(self) -> None:
        manifest = copy.deepcopy(MANIFEST)
        manifest["assertion_plan"].append(copy.deepcopy(manifest["assertion_plan"][0]))
        with self.assertRaises(ManifestError):
            validate_manifest(manifest, REGISTRY)

    def test_runtime_support_claim_is_rejected(self) -> None:
        manifest = copy.deepcopy(MANIFEST)
        manifest["assertion_plan"][0]["runtime_support"] = "SUPPORTED"
        with self.assertRaises(ManifestError):
            validate_manifest(manifest, REGISTRY)

    def test_historical_lineage_claim_is_rejected(self) -> None:
        manifest = copy.deepcopy(MANIFEST)
        manifest["historical_lineage"] = "v0.1.2.1"
        with self.assertRaises(ManifestError):
            validate_manifest(manifest, REGISTRY)


if __name__ == "__main__":
    unittest.main()
