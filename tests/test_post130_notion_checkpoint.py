from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "ai_context" / "validate_project_state.py"
SPEC = importlib.util.spec_from_file_location("validate_project_state_post130_test", MODULE_PATH)
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)

H11_ADMISSION_MERGE = "f7d13fce0104a4c2ce67589e954b09365a82f36f"
H11_STATE_BINDING_MERGE = "e36b7f45410d74b8a65406bff6fdd6d070fa96b0"
ADR0028_DECISION_MERGE = "4a13d2b4ee8001a43f7e3e701dbe9025dbcfd0df"
ADR0028_RECONCILIATION_MERGE = "5ebb33f5a74a81a7a49dae36ed29247d9b71db87"


class Post130NotionCheckpointTests(unittest.TestCase):
    def setUp(self) -> None:
        self.state = json.loads((ROOT / "project-state.json").read_text(encoding="utf-8"))
        self.registry = json.loads((ROOT / "contracts" / "registry.json").read_text(encoding="utf-8"))

    def validate(self, state: dict) -> None:
        module.validate(
            state,
            repo=ROOT,
            registry=copy.deepcopy(self.registry),
            check_git=False,
        )

    def test_current_notion_checkpoint_preserves_h11_binding_and_records_adr0028_sync(self) -> None:
        self.assertEqual(
            self.state["checkpoints"]["notion_synchronized_through_sha"],
            H11_STATE_BINDING_MERGE,
        )
        self.assertFalse(self.state["notion"]["synchronization_required"])
        self.assertEqual(
            self.state["notion"]["status"],
            "SYNCED_THROUGH_DESCENDANT_CHECKPOINT",
        )
        self.assertEqual(
            self.state["notion"]["decision_sync_status"],
            "COMPLETE / READ_BACK_VERIFIED",
        )
        self.assertEqual(self.state["notion"]["surface_count"], 8)
        self.assertEqual(self.state["notion"]["read_back_verified_count"], 8)
        self.assertEqual(self.state["notion"]["new_pages_created"], 0)
        self.assertIn(ADR0028_DECISION_MERGE, self.state["notion"]["scope"])
        self.assertIn(ADR0028_RECONCILIATION_MERGE, self.state["notion"]["scope"])
        self.assertIn("updated and read back", self.state["notion"]["scope"])
        self.validate(copy.deepcopy(self.state))

    def test_old_pr129_checkpoint_is_rejected_as_current_notion_truth(self) -> None:
        state = copy.deepcopy(self.state)
        state["checkpoints"]["notion_synchronized_through_sha"] = H11_ADMISSION_MERGE
        with self.assertRaisesRegex(module.ProjectStateError, "checkpoint drift"):
            self.validate(state)


if __name__ == "__main__":
    unittest.main()
