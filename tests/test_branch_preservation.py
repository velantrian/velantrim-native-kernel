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
            "status": "BOUNDED_REPOSITORY_HYGIENE_SAFETY_CONTRACT",
            "authority_boundary": {
                "h11_outcome_changed": False,
                "runtime_authorized": False,
                "canon_authorized": False,
                "production_authorized": False,
                "branch_deletion_authorized": False,
                "auto_delete_authorized": False,
            },
            "policy": {
                "purpose": "Prevent deletion of refs that currently keep repository-cited historical evidence commits reachable until durable main-reachable anchors are recorded.",
                "default_action": "NO_DELETION_FROM_THIS_MANIFEST",
                "migration_rule": "Preserve the historical PR-head identity and add a durable main-reachable checkpoint before a protected ref may leave this manifest.",
            },
            "protected_refs": [{
                "ref": "agent/example",
                "tip_sha": SHA,
                "cited_by": ["docs/evidence.md"],
                "reason": "historical evidence anchor",
                "migration_state": state,
            }],
        }

    def _frozen(self, state="PENDING_MAIN_REACHABLE_ANCHOR", cited_by=("docs/evidence.md",)):
        return {
            "agent/example": {
                "tip_sha": SHA,
                "migration_state": state,
                "cited_by": cited_by,
            }
        }

    def _run(self, data, remote=SHA, citation_text=None, create_citations=True, required=None):
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
                        if citation.resolve() == path.resolve():
                            continue
                        citation.parent.mkdir(parents=True, exist_ok=True)
                        text = citation_text
                        if text is None:
                            text = item["tip_sha"][:12]
                        citation.write_text(text, encoding="utf-8")
            old_remote = module._remote_branch_sha
            old_required = module.FROZEN_CONTRACT
            if isinstance(remote, Exception):
                def fail_remote(*_args):
                    raise remote
                module._remote_branch_sha = fail_remote
            else:
                module._remote_branch_sha = lambda *_args: remote
            module.FROZEN_CONTRACT = required or self._frozen(state=data["protected_refs"][0]["migration_state"])
            try:
                module.validate(repo, path)
            finally:
                module._remote_branch_sha = old_remote
                module.FROZEN_CONTRACT = old_required

    def test_valid_manifest_passes(self):
        self._run(self._manifest())

    def test_intentional_lineage_can_bind_by_ref_name(self):
        data = self._manifest("INTENTIONAL_LONG_LIVED_LINEAGE")
        self._run(
            data,
            citation_text="preserve agent/example",
            required=self._frozen("INTENTIONAL_LONG_LIVED_LINEAGE"),
        )

    def test_authority_promotion_fails_closed(self):
        data = self._manifest()
        data["authority_boundary"]["runtime_authorized"] = True
        with self.assertRaisesRegex(module.BranchPreservationError, "runtime_authorized"):
            self._run(data)

    def test_unknown_authority_key_fails_closed(self):
        data = self._manifest()
        data["authority_boundary"]["branch_cleanup_authorized"] = True
        with self.assertRaisesRegex(module.BranchPreservationError, "authority_boundary keys drift"):
            self._run(data)

    def test_policy_default_action_drift_fails_closed(self):
        data = self._manifest()
        data["policy"]["default_action"] = "DELETE_PROTECTED_REFS"
        with self.assertRaisesRegex(module.BranchPreservationError, "no-deletion policy drift"):
            self._run(data)

    def test_unknown_ref_semantic_field_fails_closed(self):
        data = self._manifest()
        data["protected_refs"][0]["deletion_authorized"] = True
        with self.assertRaisesRegex(module.BranchPreservationError, "protected ref entry keys drift"):
            self._run(data)

    def test_remote_missing_fails_even_if_local_state_could_match(self):
        error = module.BranchPreservationError("remote branch missing")
        with self.assertRaisesRegex(module.BranchPreservationError, "remote branch missing"):
            self._run(self._manifest(), remote=error)

    def test_ref_tip_drift_fails_closed(self):
        with self.assertRaisesRegex(module.BranchPreservationError, "remote ref tip drift"):
            self._run(self._manifest(), remote="b" * 40)

    def test_frozen_tip_drift_fails_closed(self):
        data = self._manifest()
        data["protected_refs"][0]["tip_sha"] = "b" * 40
        with self.assertRaisesRegex(module.BranchPreservationError, "frozen protected tip drift"):
            self._run(data, remote="b" * 40)

    def test_migration_state_drift_fails_closed(self):
        data = self._manifest("INTENTIONAL_LONG_LIVED_LINEAGE")
        with self.assertRaisesRegex(module.BranchPreservationError, "frozen migration_state drift"):
            self._run(data, required=self._frozen("PENDING_MAIN_REACHABLE_ANCHOR"))

    def test_unexpected_ref_requires_validator_update(self):
        data = self._manifest()
        data["protected_refs"][0]["ref"] = "agent/unexpected"
        with self.assertRaisesRegex(module.BranchPreservationError, "explicit validator update"):
            self._run(data)

    def test_missing_frozen_ref_fails_closed(self):
        required = self._frozen()
        required["agent/missing"] = {
            "tip_sha": "b" * 40,
            "migration_state": "PENDING_MAIN_REACHABLE_ANCHOR",
            "cited_by": ("docs/missing.md",),
        }
        with self.assertRaisesRegex(module.BranchPreservationError, "inventory incomplete"):
            self._run(self._manifest(), required=required)

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

    def test_duplicate_normalized_citation_path_fails_closed(self):
        data = self._manifest()
        data["protected_refs"][0]["cited_by"] = ["docs/evidence.md", "docs/./evidence.md"]
        with self.assertRaisesRegex(module.BranchPreservationError, "duplicate normalized cited_by path"):
            self._run(
                data,
                required=self._frozen(cited_by=("docs/evidence.md", "docs/./evidence.md")),
            )

    def test_cited_by_inventory_drift_fails_closed(self):
        data = self._manifest()
        data["protected_refs"][0]["cited_by"] = ["docs/other.md"]
        with self.assertRaisesRegex(module.BranchPreservationError, "frozen cited_by drift"):
            self._run(data, required=self._frozen())

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
