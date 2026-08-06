from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL_PATH = ROOT / "tools" / "profiles" / "validate_p1_manifest.py"
SPEC = importlib.util.spec_from_file_location("validate_p1_manifest", TOOL_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)

MANIFEST = json.loads(
    (ROOT / "profiles" / "postgresql-reference-v0" / "p1-manifest.json").read_text(
        encoding="utf-8"
    )
)


class P1ManifestTests(unittest.TestCase):
    def test_manifest_passes(self) -> None:
        report = module.validate_p1_manifest(copy.deepcopy(MANIFEST))
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["kernel_runtime_conformance"], "UNSUPPORTED")

    def test_runtime_conformance_overclaim_is_rejected(self) -> None:
        value = copy.deepcopy(MANIFEST)
        value["kernel_runtime_conformance"] = "C1"
        with self.assertRaises(module.P1ManifestError):
            module.validate_p1_manifest(value)

    def test_historical_lineage_is_rejected(self) -> None:
        value = copy.deepcopy(MANIFEST)
        value["issue_1_boundary"]["historical_lineage"] = "v0.1.2.1"
        with self.assertRaises(module.P1ManifestError):
            module.validate_p1_manifest(value)

    def test_external_dependency_policy_is_rejected(self) -> None:
        value = copy.deepcopy(MANIFEST)
        value["language_profile"]["dependencies"] = "psycopg"
        with self.assertRaises(module.P1ManifestError):
            module.validate_p1_manifest(value)


if __name__ == "__main__":
    unittest.main()
