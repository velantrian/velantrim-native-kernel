from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "tools" / "profiles" / "validate_p3_manifest.py"
spec = importlib.util.spec_from_file_location("validate_p3_manifest", MODULE)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)
DATA = json.loads((ROOT / "profiles/postgresql-reference-v0/p3-manifest.json").read_text())


class P3ManifestTests(unittest.TestCase):
    def test_committed_manifest_is_valid(self) -> None:
        validator.validate(DATA)

    def test_conformance_and_c_level_promotion_are_rejected(self) -> None:
        changed = copy.deepcopy(DATA)
        changed["kernel_runtime_conformance"] = "SUPPORTED"
        with self.assertRaises(validator.ManifestError):
            validator.validate(changed)
        changed = copy.deepcopy(DATA)
        changed["c1"] = "ESTABLISHED"
        with self.assertRaises(validator.ManifestError):
            validator.validate(changed)

    def test_false_repository_pass_is_rejected(self) -> None:
        changed = copy.deepcopy(DATA)
        changed["local_validation"]["repository_ci"] = "PASS"
        with self.assertRaises(validator.ManifestError):
            validator.validate(changed)

    def test_receipt_limits_and_stale_head_guard_are_required(self) -> None:
        changed = copy.deepcopy(DATA)
        changed["receipt_limits"] = []
        with self.assertRaises(validator.ManifestError):
            validator.validate(changed)
        changed = copy.deepcopy(DATA)
        changed["postgresql_profile"]["projection_publish_guard"] = "NONE"
        with self.assertRaises(validator.ManifestError):
            validator.validate(changed)

    def test_recovery_and_p4_scope_drift_are_rejected(self) -> None:
        changed = copy.deepcopy(DATA)
        changed["issue_1_boundary"]["may_claim_recovery"] = True
        with self.assertRaises(validator.ManifestError):
            validator.validate(changed)
        changed = copy.deepcopy(DATA)
        changed["forbidden_in_p3"] = []
        with self.assertRaises(validator.ManifestError):
            validator.validate(changed)


if __name__ == "__main__":
    unittest.main()
