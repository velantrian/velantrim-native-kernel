from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_c5_manifest",
    ROOT / "tools" / "profiles" / "validate_c5_manifest.py",
)
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(module)


class C5ManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = json.loads(
            (ROOT / "profiles" / "operational-validation-v0" / "c5-manifest.json").read_text(
                encoding="utf-8"
            )
        )

    def test_manifest_passes(self) -> None:
        module.validate(copy.deepcopy(self.manifest), root=ROOT)

    def test_plan_digest_drift_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["plan"]["sha256"] = "0" * 64
        with self.assertRaisesRegex(module.ManifestError, "plan digest drift"):
            module.validate(manifest, root=ROOT)

    def test_false_repository_pass_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["repository_evidence"]["status"] = "PASS"
        with self.assertRaisesRegex(module.ManifestError, "exact repository head"):
            module.validate(manifest, root=ROOT)

    def test_c5_cannot_rewrite_assertion_conformance(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["kernel_runtime_conformance"] = "C5"
        with self.assertRaisesRegex(module.ManifestError, "must not rewrite"):
            module.validate(manifest, root=ROOT)

    def test_production_boundary_cannot_be_enabled(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["deployment_boundary"]["production_traffic"] = True
        with self.assertRaisesRegex(module.ManifestError, "unsafe C5 boundary"):
            module.validate(manifest, root=ROOT)


if __name__ == "__main__":
    unittest.main()
