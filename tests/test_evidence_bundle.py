from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify_bundle", ROOT / "tools" / "evidence" / "verify_bundle.py")
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(module)


class EvidenceBundleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = json.loads((ROOT / "evidence" / "c5" / "2026-08-07" / "manifest.json").read_text(encoding="utf-8"))

    def test_repository_bundle_passes(self) -> None:
        module.validate(copy.deepcopy(self.manifest), repo=ROOT)

    def test_digest_drift_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["checkpoints"][0]["artifacts"][0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(module.EvidenceBundleError, "artifact digest mismatch"):
            module.validate(manifest, repo=ROOT)

    def test_checkpoint_commit_drift_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["checkpoints"][1]["head_sha"] = "0" * 40
        with self.assertRaisesRegex(module.EvidenceBundleError, "report commit mismatch"):
            module.validate(manifest, repo=ROOT)

    def test_path_escape_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["checkpoints"][0]["artifacts"][0]["path"] = "../outside.zip"
        with self.assertRaisesRegex(module.EvidenceBundleError, "escapes repository"):
            module.validate(manifest, repo=ROOT)


if __name__ == "__main__":
    unittest.main()
