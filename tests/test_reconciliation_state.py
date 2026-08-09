from __future__ import annotations

import copy
import importlib.util
import json
import sys
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

    def test_rejects_closed_foundational_issue(self) -> None:
        state = copy.deepcopy(self.state)
        state["issues"]["14"]["state"] = "CLOSED"
        self.assertNotEqual("OPEN", state["issues"]["14"]["state"])

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
