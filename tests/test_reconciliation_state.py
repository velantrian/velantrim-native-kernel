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
            "README.md",
            "README.ru.md",
            "STATUS.md",
            "docs/ai/README.md",
            "docs/ai/CURRENT_STATE.md",
            "docs/ai/ISSUE_RECONCILIATION.md",
            "docs/ai/NOTION_HANDOFF.md",
            "docs/ai/KNOWN_RISKS.md",
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

    def test_checkpoint_roles_separate_publication_and_notion(self) -> None:
        checkpoints = self.state["checkpoints"]
        self.assertEqual(
            module.NOTION_SYNC_SHA,
            checkpoints["manifest_generated_from_sha"],
        )
        self.assertEqual(
            module.PUBLICATION_SHA,
            checkpoints["publication_checkpoint_sha"],
        )
        self.assertEqual(
            module.NOTION_SYNC_SHA,
            checkpoints["notion_synchronized_through_sha"],
        )
        self.assertNotEqual(
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

    def test_publication_and_notion_role_collapse_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            self._copy_fixture(repo)
            state_path = repo / "project-state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["checkpoints"]["manifest_generated_from_sha"] = module.PUBLICATION_SHA
            state["checkpoints"]["notion_synchronized_through_sha"] = module.PUBLICATION_SHA
            state_path.write_text(json.dumps(state), encoding="utf-8")
            with self.assertRaisesRegex(module.ReconciliationError, "source|roles collapsed"):
                module.validate(repo)

    def test_current_surface_missing_descendant_checkpoint_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            self._copy_fixture(repo)
            current = repo / "docs/ai/CURRENT_STATE.md"
            current.write_text(
                current.read_text(encoding="utf-8").replace(
                    module.NOTION_SYNC_SHA,
                    "removed-descendant-checkpoint",
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(
                module.ReconciliationError,
                "CURRENT_STATE.md: manifest source binding missing or ambiguous",
            ):
                module.validate(repo)

    def test_current_surface_role_collapse_is_rejected_when_sha_remains_in_prose(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            self._copy_fixture(repo)
            current = repo / "docs/ai/CURRENT_STATE.md"
            text = current.read_text(encoding="utf-8")
            text = text.replace(
                f"manifest_generated_from: {module.NOTION_SYNC_SHA}",
                f"manifest_generated_from: {module.PUBLICATION_SHA}",
                1,
            ).replace(
                f"notion_synchronized_through: {module.NOTION_SYNC_SHA}",
                f"notion_synchronized_through: {module.PUBLICATION_SHA}",
                1,
            )
            self.assertIn(module.NOTION_SYNC_SHA, text)
            current.write_text(text, encoding="utf-8")
            with self.assertRaisesRegex(
                module.ReconciliationError,
                "CURRENT_STATE.md: manifest source binding drift",
            ):
                module.validate(repo)

    def test_readme_role_row_collapse_is_rejected_when_sha_remains_in_prose(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            self._copy_fixture(repo)
            readme = repo / "README.md"
            text = readme.read_text(encoding="utf-8").replace(
                f"| Manifest source / Notion synchronized descendant | `{module.NOTION_SYNC_SHA}` |",
                f"| Manifest source / Notion synchronized descendant | `{module.PUBLICATION_SHA}` |",
                1,
            )
            self.assertIn(module.NOTION_SYNC_SHA, text)
            readme.write_text(text, encoding="utf-8")
            with self.assertRaisesRegex(
                module.ReconciliationError,
                "README.md: Notion synchronized descendant binding drift",
            ):
                module.validate(repo)

    def test_stale_active_risk_state_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            self._copy_fixture(repo)
            risks = repo / "docs/ai/KNOWN_RISKS.md"
            risks.write_text(
                risks.read_text(encoding="utf-8").replace(
                    module.CURRENT_RISK_STATE,
                    "**State:** `MITIGATED BY PR #80 / HUMAN AND NOTION RECONCILIATION IN PROGRESS`.",
                    1,
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(
                module.ReconciliationError,
                "active current-state drift risk state drift",
            ):
                module.validate(repo)

    def test_known_risks_checkpoint_role_collapse_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            self._copy_fixture(repo)
            risks = repo / "docs/ai/KNOWN_RISKS.md"
            text = risks.read_text(encoding="utf-8").replace(
                f"notion_synchronized_descendant: {module.NOTION_SYNC_SHA}",
                f"notion_synchronized_descendant: {module.PUBLICATION_SHA}",
                1,
            )
            self.assertIn(module.NOTION_SYNC_SHA, text)
            risks.write_text(text, encoding="utf-8")
            with self.assertRaisesRegex(
                module.ReconciliationError,
                "KNOWN_RISKS.md: Notion synchronized descendant binding drift",
            ):
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
