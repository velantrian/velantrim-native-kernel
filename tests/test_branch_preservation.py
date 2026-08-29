import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "tools" / "ai_context" / "validate_branch_preservation.py"
spec = importlib.util.spec_from_file_location("validate_branch_preservation", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)

SHA = "a" * 40


class BranchPreservationTests(unittest.TestCase):
    def _manifest(self):
        return {
            "protocol": "nk-branch-preservation/1",
            "authority_boundary": {
                "h11_outcome_changed": False,
                "runtime_authorized": False,
                "canon_authorized": False,
                "production_authorized": False,
                "branch_deletion_authorized": False,
                "auto_delete_authorized": False,
            },
            "protected_refs": [{
                "ref": "agent/example",
                "tip_sha": SHA,
                "reason": "historical evidence anchor",
                "migration_state": "PENDING_MAIN_REACHABLE_ANCHOR",
            }],
        }

    def _run(self, data, actual=SHA, cited=True):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            path = repo / "manifest.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            old_git, old_cited = module._git, module._sha_is_cited
            module._git = lambda *_args: actual
            module._sha_is_cited = lambda *_args: cited
            try:
                module.validate(repo, path)
            finally:
                module._git, module._sha_is_cited = old_git, old_cited

    def test_valid_manifest_passes(self):
        self._run(self._manifest())

    def test_authority_promotion_fails_closed(self):
        data = self._manifest()
        data["authority_boundary"]["runtime_authorized"] = True
        with self.assertRaisesRegex(module.BranchPreservationError, "runtime_authorized"):
            self._run(data)

    def test_ref_tip_drift_fails_closed(self):
        with self.assertRaisesRegex(module.BranchPreservationError, "tip drift"):
            self._run(self._manifest(), actual="b" * 40)

    def test_missing_external_citation_fails_closed(self):
        with self.assertRaisesRegex(module.BranchPreservationError, "no longer cited"):
            self._run(self._manifest(), cited=False)

    def test_duplicate_ref_fails_closed(self):
        data = self._manifest()
        data["protected_refs"].append(dict(data["protected_refs"][0]))
        with self.assertRaisesRegex(module.BranchPreservationError, "duplicate/invalid ref"):
            self._run(data)

    def test_short_sha_rejected(self):
        data = self._manifest()
        data["protected_refs"][0]["tip_sha"] = "a" * 12
        with self.assertRaisesRegex(module.BranchPreservationError, "full 40-char SHA"):
            self._run(data)


if __name__ == "__main__":
    unittest.main()
