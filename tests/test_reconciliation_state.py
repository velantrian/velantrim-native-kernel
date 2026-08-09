from __future__ import annotations

import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "ai_context" / "validate_reconciliation.py"
SPEC = importlib.util.spec_from_file_location("validate_reconciliation", MODULE_PATH)
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class ReconciliationStateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.state = json.loads(
            (ROOT / "project-state.json").read_text(encoding="utf-8")
        )

    def _copy_fixture(self, directory: Path) -> None:
        for rel in (
            "project-state.json",
            "STATUS.md",
            "docs/ai/CURRENT_STATE.md",
            "docs/ai/ISSUE_RECONCILIATION.md",
            "docs/ai/NOTION_HANDOFF.md",
        ):
            source = ROOT / rel
            target = directory / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)

    def test_repository_reconciliation_passes(self) -> None:
        module.validate(ROOT)

    def test_foundational_issues_are_present_and_open(self) -> None:
        for number in module.ISSUES:
            issue = self.state["issues"][number]
            self.assertEqual("OPEN", issue["state"])
            self.assertEqual("VERIFIED", issue["verification"]["status"])
            self.assertEqual("GITHUB_API", issue["verification"]["method"])

    def test_checkpoint_roles_match_notion_publication(self) -> None:
        checkpoints = self.state["checkpoints"]
        self.assertEqual(
            module.PUBLICATION_SHA,
            checkpoints["manifest_generated_from_sha"],
        )
        self.assertEqual(
            checkpoints["publication_checkpoint_sha"],
            checkpoints["notion_synchronized_through_sha"],
        )

    def test_closed_foundational_issue_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            self._copy_fixture(repo)
            state_path = repo / "project-state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["issues"]["14"]["state"] = "CLOSED"
            state_path.write_text(json.dumps(state), encoding="utf-8")
            with self.assertRaisesRegex(module.ReconciliationError, "Issue #14"):
                module.validate(repo)

    def test_notion_checkpoint_drift_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            self._copy_fixture(repo)
            state_path = repo / "project-state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["checkpoints"]["notion_synchronized_through_sha"] = "0" * 40
            state_path.write_text(json.dumps(state), encoding="utf-8")
            with self.assertRaisesRegex(module.ReconciliationError, "Notion"):
                module.validate(repo)

    def test_missing_comment_identity_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            self._copy_fixture(repo)
            record = repo / "docs/ai/ISSUE_RECONCILIATION.md"
            record.write_text(
                record.read_text(encoding="utf-8").replace("5231286665", "removed"),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(module.ReconciliationError, "comment identity"):
                module.validate(repo)

    def test_all_comment_and_page_identities_are_recorded(self) -> None:
        issue_record = (ROOT / "docs/ai/ISSUE_RECONCILIATION.md").read_text(
            encoding="utf-8"
        )
        notion_record = (ROOT / "docs/ai/NOTION_HANDOFF.md").read_text(
            encoding="utf-8"
        )
        for comment_id in module.ISSUE_COMMENTS.values():
            self.assertIn(comment_id, issue_record)
        for page_id in module.NOTION_PAGE_IDS:
            self.assertIn(page_id, notion_record)


if __name__ == "__main__":
    unittest.main()
