from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_c4_manifest", ROOT / "tools" / "profiles" / "validate_c4_manifest.py")
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(module)


class C4ManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = json.loads((ROOT / "profiles" / "shadow-evaluation-v0" / "c4-manifest.json").read_text(encoding="utf-8"))

    def test_manifest_passes(self) -> None:
        module.validate(copy.deepcopy(self.manifest), root=ROOT)

    def test_dataset_digest_drift_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["dataset"]["sha256"] = "0" * 64
        with self.assertRaisesRegex(module.ManifestError, "digest drift"):
            module.validate(manifest, root=ROOT)

    def test_false_repository_pass_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["repository_evidence"]["head_sha"] = None
        manifest["repository_evidence"]["workflow_run_id"] = None
        manifest["repository_evidence"]["artifact_count"] = 0
        manifest["repository_evidence"]["matrix"] = []
        with self.assertRaisesRegex(module.ManifestError, "requires exact repository run"):
            module.validate(manifest, root=ROOT)

    def test_c4_cannot_expand_assertion_coverage(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["c4_assertion_coverage"]["shadow_evaluated_supported"] = 72
        with self.assertRaisesRegex(module.ManifestError, "assertion coverage"):
            module.validate(manifest, root=ROOT)

    def test_authority_boundary_cannot_be_weakened(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["authority_boundary"]["side_effects"] = "ALLOWED"
        with self.assertRaisesRegex(module.ManifestError, "unsafe"):
            module.validate(manifest, root=ROOT)


if __name__ == "__main__":
    unittest.main()
