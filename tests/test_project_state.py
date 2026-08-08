from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "ai_context" / "validate_project_state.py"
SPEC = importlib.util.spec_from_file_location("validate_project_state", MODULE_PATH)
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class ProjectStateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.state = json.loads((ROOT / "project-state.json").read_text(encoding="utf-8"))

    def test_repository_state_passes(self) -> None:
        module.validate(copy.deepcopy(self.state), repo=ROOT, check_git=False)

    def test_production_promotion_is_rejected(self) -> None:
        state = copy.deepcopy(self.state)
        state["status"]["production_authorized"] = True
        with self.assertRaisesRegex(module.ProjectStateError, "production"):
            module.validate(state, repo=ROOT, check_git=False)

    def test_historical_track_cannot_block_clean_lineage(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["historical_recovery"]["blocks_clean_implementation"] = True
        with self.assertRaisesRegex(module.ProjectStateError, "must not block"):
            module.validate(state, repo=ROOT, check_git=False)

    def test_issue_64_must_remain_completed(self) -> None:
        state = copy.deepcopy(self.state)
        state["issues"]["64"]["state"] = "OPEN"
        with self.assertRaisesRegex(module.ProjectStateError, "Issue #64"):
            module.validate(state, repo=ROOT, check_git=False)

    def test_nk_epi_cannot_be_promoted_by_documentation(self) -> None:
        state = copy.deepcopy(self.state)
        state["nk_epi"]["supported"] = 1
        state["nk_epi"]["unsupported"] = 7
        with self.assertRaisesRegex(module.ProjectStateError, "NK-EPI"):
            module.validate(state, repo=ROOT, check_git=False)

    def test_sqlite_floor_and_historical_bundle_fail_closed(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["clean_implementation"]["integrity_review"][
            "sqlite_wal_minimum"
        ] = "3.45.1"
        with self.assertRaisesRegex(module.ProjectStateError, "SQLite WAL floor"):
            module.validate(state, repo=ROOT, check_git=False)

        state = copy.deepcopy(self.state)
        state["evidence"]["sqlite_integrity_revalidation"][
            "may_rewrite_2026_08_07_bundle"
        ] = True
        with self.assertRaisesRegex(module.ProjectStateError, "immutable"):
            module.validate(state, repo=ROOT, check_git=False)

    def test_sqlite_revalidation_evidence_cannot_be_removed(self) -> None:
        state = copy.deepcopy(self.state)
        state["evidence"]["sqlite_integrity_revalidation"]["artifact_count"] = 0
        with self.assertRaisesRegex(module.ProjectStateError, "inventory"):
            module.validate(state, repo=ROOT, check_git=False)

        state = copy.deepcopy(self.state)
        state["tracks"]["clean_implementation"]["integrity_review"][
            "affected_assertions_re_adjudicated"
        ] = False
        with self.assertRaisesRegex(module.ProjectStateError, "re-adjudicated"):
            module.validate(state, repo=ROOT, check_git=False)


if __name__ == "__main__":
    unittest.main()
