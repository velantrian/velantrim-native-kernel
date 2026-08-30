import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "tools" / "ai_context" / "validate_evidence_anchor_migration.py"
spec = importlib.util.spec_from_file_location("validate_evidence_anchor_migration", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)

HIST = "a" * 40
DURABLE = "b" * 40


class EvidenceAnchorMigrationTests(unittest.TestCase):
    def _entry(self):
        return {
            "ref": "agent/example",
            "historical_head_sha": HIST,
            "pull_request": 42,
            "durable_main_sha": DURABLE,
            "cited_by": ["docs/evidence.md"],
            "migration_state": "DURABLE_MAIN_CHECKPOINT_RECORDED",
        }

    def _manifest(self):
        return {
            "protocol": "nk-evidence-anchor-migration/1",
            "status": "BOUNDED_PROVENANCE_MIGRATION",
            "authority_boundary": {
                "branch_deletion_authorized": False,
                "auto_delete_authorized": False,
                "h11_outcome_changed": False,
                "runtime_authorized": False,
                "canon_authorized": False,
                "production_authorized": False,
            },
            "policy": {
                "historical_identity_retained": True,
                "durable_checkpoint_requirement": "MERGED_PR_MAIN_REACHABLE_CHECKPOINT",
                "deletion_requires_separate_owner_action": True,
            },
            "migrations": [self._entry()],
        }

    def _frozen(self):
        return {
            "agent/example": {
                "historical_head_sha": HIST,
                "pull_request": 42,
                "durable_main_sha": DURABLE,
                "cited_by": ("docs/evidence.md",),
            }
        }

    def _run(self, data, ancestor=True, citation_text=None, frozen=None):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            manifest = repo / "migration.json"
            manifest.write_text(json.dumps(data), encoding="utf-8")
            for item in data.get("migrations", []):
                for raw in item.get("cited_by", []):
                    if not isinstance(raw, str) or raw.startswith("/") or ".." in Path(raw).parts:
                        continue
                    path = repo / raw
                    if path.resolve() == manifest.resolve():
                        continue
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(citation_text if citation_text is not None else item["historical_head_sha"][:12], encoding="utf-8")
            old_ancestor = module._is_ancestor
            old_frozen = module.FROZEN_MIGRATIONS
            module._is_ancestor = lambda *_args: ancestor
            module.FROZEN_MIGRATIONS = frozen or self._frozen()
            try:
                module.validate(repo, manifest)
            finally:
                module._is_ancestor = old_ancestor
                module.FROZEN_MIGRATIONS = old_frozen

    def test_valid_migration_passes(self):
        self._run(self._manifest())

    def test_deletion_authority_fails_closed(self):
        data = self._manifest()
        data["authority_boundary"]["branch_deletion_authorized"] = True
        with self.assertRaisesRegex(module.EvidenceAnchorMigrationError, "branch_deletion_authorized"):
            self._run(data)

    def test_unknown_authority_key_fails_closed(self):
        data = self._manifest()
        data["authority_boundary"]["cleanup_authorized"] = True
        with self.assertRaisesRegex(module.EvidenceAnchorMigrationError, "authority_boundary keys drift"):
            self._run(data)

    def test_policy_drift_fails_closed(self):
        data = self._manifest()
        data["policy"]["deletion_requires_separate_owner_action"] = False
        with self.assertRaisesRegex(module.EvidenceAnchorMigrationError, "migration policy drift"):
            self._run(data)

    def test_historical_identity_drift_fails_closed(self):
        data = self._manifest()
        data["migrations"][0]["historical_head_sha"] = "c" * 40
        with self.assertRaisesRegex(module.EvidenceAnchorMigrationError, "historical identity drift"):
            self._run(data)

    def test_pr_identity_drift_fails_closed(self):
        data = self._manifest()
        data["migrations"][0]["pull_request"] = 43
        with self.assertRaisesRegex(module.EvidenceAnchorMigrationError, "pull request identity drift"):
            self._run(data)

    def test_durable_checkpoint_drift_fails_closed(self):
        data = self._manifest()
        data["migrations"][0]["durable_main_sha"] = "c" * 40
        with self.assertRaisesRegex(module.EvidenceAnchorMigrationError, "durable main checkpoint drift"):
            self._run(data)

    def test_durable_checkpoint_must_be_ancestor(self):
        with self.assertRaisesRegex(module.EvidenceAnchorMigrationError, "not main-reachable"):
            self._run(self._manifest(), ancestor=False)

    def test_historical_identity_must_remain_cited(self):
        with self.assertRaisesRegex(module.EvidenceAnchorMigrationError, "historical identity missing"):
            self._run(self._manifest(), citation_text="unrelated")

    def test_manifest_cannot_self_satisfy(self):
        data = self._manifest()
        data["migrations"][0]["cited_by"] = ["migration.json"]
        frozen = self._frozen()
        frozen["agent/example"]["cited_by"] = ("migration.json",)
        with self.assertRaisesRegex(module.EvidenceAnchorMigrationError, "cannot self-satisfy"):
            self._run(data, frozen=frozen)

    def test_duplicate_normalized_citation_fails(self):
        data = self._manifest()
        data["migrations"][0]["cited_by"] = ["docs/evidence.md", "docs/./evidence.md"]
        frozen = self._frozen()
        frozen["agent/example"]["cited_by"] = ("docs/evidence.md", "docs/./evidence.md")
        with self.assertRaisesRegex(module.EvidenceAnchorMigrationError, "duplicate normalized cited_by path"):
            self._run(data, frozen=frozen)

    def test_missing_frozen_migration_fails(self):
        frozen = self._frozen()
        frozen["agent/missing"] = {
            "historical_head_sha": "c" * 40,
            "pull_request": 43,
            "durable_main_sha": "d" * 40,
            "cited_by": ("docs/missing.md",),
        }
        with self.assertRaisesRegex(module.EvidenceAnchorMigrationError, "migration inventory incomplete"):
            self._run(self._manifest(), frozen=frozen)


if __name__ == "__main__":
    unittest.main()
