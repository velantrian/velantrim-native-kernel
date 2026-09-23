import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "tools" / "ai_context" / "validate_branch_hygiene_inventory.py"
spec = importlib.util.spec_from_file_location("validate_branch_hygiene_inventory", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class BranchHygieneInventoryTests(unittest.TestCase):
    def _data(self):
        return {
            "protocol": "nk-branch-hygiene-inventory/1",
            "status": "READ_ONLY_CLASSIFICATION_NO_DELETION_AUTHORITY",
            "observed_branch_count_including_main": 3,
            "observed_non_main_count": 2,
            "observed_pull_request_count": 1,
            "authority_boundary": {
                "h11_outcome_changed": False,
                "runtime_authorized": False,
                "canon_authorized": False,
                "production_authorized": False,
                "branch_deletion_authorized": False,
                "auto_delete_authorized": False,
            },
            "classification_counts": {"KEEP_PROTECTED": 2},
            "entries": [
                {"ref": "archive/bootstrap-v0.1.2.1-docs-lineage", "classification": "KEEP_PROTECTED"},
                {"ref": "bootstrap/research-kernel-v0.1.2.1", "classification": "KEEP_PROTECTED"},
            ],
            "method": {},
        }

    def _run(self, data):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "inventory.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            module.validate(Path(tmp), path)

    def test_valid_inventory(self):
        self._run(self._data())

    def test_deletion_authority_fails_closed(self):
        data = self._data()
        data["authority_boundary"]["branch_deletion_authorized"] = True
        with self.assertRaisesRegex(module.BranchHygieneInventoryError, "branch_deletion_authorized"):
            self._run(data)

    def test_safe_delete_class_fails_closed(self):
        data = self._data()
        data["entries"][0]["classification"] = "SAFE_DELETE"
        data["classification_counts"] = {"SAFE_DELETE": 1, "KEEP_PROTECTED": 1}
        with self.assertRaisesRegex(module.BranchHygieneInventoryError, "deletion-authorizing"):
            self._run(data)

    def test_counts_must_match(self):
        data = self._data()
        data["classification_counts"] = {"KEEP_PROTECTED": 1}
        with self.assertRaisesRegex(module.BranchHygieneInventoryError, "classification_counts mismatch"):
            self._run(data)

    def test_protected_ref_class_fails_closed(self):
        data = self._data()
        data["entries"][0]["classification"] = "UNKNOWN_NO_PR_ASSOCIATION"
        data["classification_counts"] = {"UNKNOWN_NO_PR_ASSOCIATION": 1, "KEEP_PROTECTED": 1}
        with self.assertRaisesRegex(module.BranchHygieneInventoryError, "protected ref class drift"):
            self._run(data)


if __name__ == "__main__":
    unittest.main()
