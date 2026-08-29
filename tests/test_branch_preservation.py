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
    def _manifest(self, state="PENDING_MAIN_REACHABLE_ANCHOR"):
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
                "cited_by": ["docs/evidence.md"],
                "reason": "historical evidence anchor",
                "migration_state": state,
            }],
        }

    def _run(self, data, actual=SHA, citation_text=None, create_citations=True):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            path = repo / "manifest.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            if create_citations:
                for item in data.get("protected_refs", []):
                    for raw in item.get("cited_by", []):
                        if not isinstance(raw, str) or raw.startswith("/") or ".." in Path(raw).parts:
                            continue
                        citation = repo / raw
                        citation.parent.mkdir(parents=True, exist_ok=True)
                        text = citation_text
                        if text is None:
                            text = item["tip_sha"][:12]
                        citation.write_text(text, encoding="utf-8")
            old_git = module._git
            module._git = lambda *_args: actual
            try:
                module.validate(repo, path)
            finally:
                module._git = old_git

    def test_valid_manifest_passes(self):
        self._run(self._manifest())

    def test_intentional_lineage_can_bind_by_ref_name(self):
        data = self._manifest("INTENTIONAL_LONG_LIVED_LINEAGE")
        self._run(data, citation_text="preserve agent/example")

    def test_authority_promotion_fails_closed(self):
        data = self._manifest()
        data["authority_boundary"]["runtime_authorized"] = True
        with self.assertRaisesRegex(module.BranchPreservationError, "runtime_authorized"):
            self._run(data)

    def test_ref_tip_drift_fails_closed(self):
        with self.assertRaisesRegex(module.BranchPreservationError, "tip drift"):
            self._run(self._manifest(), actual="b" * 40)

    def test_missing_cited_by_fails_closed(self):
        data = self._manifest()
        data["protected_refs"][0]["cited_by"] = []
        with self.assertRaisesRegex(module.BranchPreservationError, "cited_by must be non-empty"):
            self._run(data)

    def test_missing_citation_file_fails_closed(self):
        with self.assertRaisesRegex(module.BranchPreservationError, "citation file required"):
            self._run(self._manifest(), create_citations=False)

    def test_wrong_citation_content_fails_closed(self):
        with self.assertRaisesRegex(module.BranchPreservationError, "citation anchor missing"):
            self._run(self._manifest(), citation_text="unrelated text")

    def test_duplicate_citation_path_fails_closed(self):
        data = self._manifest()
        data["protected_refs"][0]["cited_by"].append("docs/evidence.md")
        with self.assertRaisesRegex(module.BranchPreservationError, "duplicate cited_by path"):
            self._run(data)

    def test_citation_path_escape_fails_closed(self):
        data = self._manifest()
        data["protected_refs"][0]["cited_by"] = ["../outside.md"]
        with self.assertRaisesRegex(module.BranchPreservationError, "escapes repository"):
            self._run(data)

    def test_manifest_cannot_self_satisfy_citation(self):
        data = self._manifest()
        data["protected_refs"][0]["cited_by"] = ["manifest.json"]
        with self.assertRaisesRegex(module.BranchPreservationError, "cannot self-satisfy"):
            self._run(data)

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
