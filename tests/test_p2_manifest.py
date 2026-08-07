from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "tools" / "profiles" / "validate_p2_manifest.py"
spec = importlib.util.spec_from_file_location("validate_p2_manifest", MODULE)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)
DATA = json.loads((ROOT / "profiles/postgresql-reference-v0/p2-manifest.json").read_text())


class P2ManifestTests(unittest.TestCase):
    def test_committed_manifest_is_valid(self) -> None:
        validator.validate(DATA)

    def test_conformance_promotion_is_rejected(self) -> None:
        changed = copy.deepcopy(DATA)
        changed["kernel_runtime_conformance"] = "SUPPORTED"
        with self.assertRaises(validator.ManifestError):
            validator.validate(changed)

    def test_dependency_and_postgres_matrix_drift_are_rejected(self) -> None:
        changed = copy.deepcopy(DATA)
        changed["language_profile"]["p1_dependency_policy"] = "PSYCOPG_REQUIRED"
        with self.assertRaises(validator.ManifestError):
            validator.validate(changed)
        changed = copy.deepcopy(DATA)
        changed["postgresql_profile"]["supported_major_versions"] = [18]
        with self.assertRaises(validator.ManifestError):
            validator.validate(changed)

    def test_false_repository_pass_is_rejected(self) -> None:
        changed = copy.deepcopy(DATA)
        changed["local_validation"]["repository_ci"] = "PASS"
        with self.assertRaises(validator.ManifestError):
            validator.validate(changed)

    def test_recovery_and_p3_scope_drift_are_rejected(self) -> None:
        changed = copy.deepcopy(DATA)
        changed["issue_1_boundary"]["may_claim_recovery"] = True
        with self.assertRaises(validator.ManifestError):
            validator.validate(changed)
        changed = copy.deepcopy(DATA)
        changed["forbidden_in_p2"] = []
        with self.assertRaises(validator.ManifestError):
            validator.validate(changed)


if __name__ == "__main__":
    unittest.main()
