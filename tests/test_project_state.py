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
        self.state = json.loads(
            (ROOT / "project-state.json").read_text(encoding="utf-8")
        )
        self.registry = json.loads(
            (ROOT / "contracts" / "registry.json").read_text(encoding="utf-8")
        )

    def validate(
        self,
        state: dict | None = None,
        registry: dict | None = None,
    ) -> None:
        module.validate(
            copy.deepcopy(self.state) if state is None else state,
            repo=ROOT,
            registry=copy.deepcopy(self.registry) if registry is None else registry,
            check_git=False,
        )

    def test_repository_state_passes(self) -> None:
        self.validate()

    def test_production_promotion_is_rejected(self) -> None:
        state = copy.deepcopy(self.state)
        state["status"]["production_authorized"] = True
        with self.assertRaisesRegex(module.ProjectStateError, "maturity|production"):
            self.validate(state=state)

    def test_checkpoint_relation_is_declared(self) -> None:
        state = copy.deepcopy(self.state)
        state["checkpoints"]["expected_head_relationship"] = "MAYBE"
        with self.assertRaisesRegex(module.ProjectStateError, "relationship"):
            self.validate(state=state)

    def test_notion_checkpoint_must_match_publication(self) -> None:
        state = copy.deepcopy(self.state)
        state["checkpoints"]["notion_synchronized_through_sha"] = "0" * 40
        with self.assertRaisesRegex(module.ProjectStateError, "Notion/publication"):
            self.validate(state=state)

    def test_historical_recovery_cannot_block_clean_lineage(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["historical_recovery"]["blocks_clean_implementation"] = True
        with self.assertRaisesRegex(module.ProjectStateError, "must not block"):
            self.validate(state=state)

    def test_sqlite_floor_and_historical_bundle_fail_closed(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["clean_implementation"]["integrity_review"][
            "sqlite_wal_minimum"
        ] = "3.45.1"
        with self.assertRaisesRegex(module.ProjectStateError, "SQLite WAL floor"):
            self.validate(state=state)

        state = copy.deepcopy(self.state)
        state["evidence"]["sqlite_integrity_revalidation"][
            "may_rewrite_2026_08_07_bundle"
        ] = True
        with self.assertRaisesRegex(module.ProjectStateError, "immutable"):
            self.validate(state=state)

    def test_sqlite_revalidation_evidence_cannot_be_removed(self) -> None:
        state = copy.deepcopy(self.state)
        state["evidence"]["sqlite_integrity_revalidation"]["artifact_count"] = 0
        with self.assertRaisesRegex(module.ProjectStateError, "inventory"):
            self.validate(state=state)

        state = copy.deepcopy(self.state)
        state["tracks"]["clean_implementation"]["integrity_review"][
            "affected_assertions_re_adjudicated"
        ] = False
        with self.assertRaisesRegex(module.ProjectStateError, "re-adjudicated"):
            self.validate(state=state)

    def test_nk_epi_cannot_be_promoted_by_metadata(self) -> None:
        state = copy.deepcopy(self.state)
        state["nk_epi"]["supported"] = 1
        state["nk_epi"]["unsupported"] = 7
        with self.assertRaisesRegex(module.ProjectStateError, "NK-EPI"):
            self.validate(state=state)

    def test_legacy_registry_runtime_status_is_rejected(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["runtime_status"] = "NOT_IMPLEMENTED"
        with self.assertRaisesRegex(module.ProjectStateError, "legacy registry"):
            self.validate(registry=registry)

    def test_registry_runtime_summary_must_match_state(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["runtime_summary"]["kernel_runtime_conformance"] = "C3"
        with self.assertRaisesRegex(module.ProjectStateError, "registry/project-state"):
            self.validate(registry=registry)

    def test_registry_assertion_arithmetic_must_match(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["assertion_evidence_summary"]["supported"] = 44
        with self.assertRaisesRegex(module.ProjectStateError, "assertion evidence"):
            self.validate(registry=registry)

    def test_accepted_family_cannot_claim_full_support(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["families"][0]["implementation_support"] = "FULL"
        with self.assertRaisesRegex(module.ProjectStateError, "support drift"):
            self.validate(registry=registry)

    def test_nk_epi_registry_cannot_claim_runtime(self) -> None:
        registry = copy.deepcopy(self.registry)
        epi = next(
            family
            for family in registry["families"]
            if family["family_id"] == "NK-EPI"
        )
        epi["implementation_support"] = "PARTIAL"
        with self.assertRaisesRegex(module.ProjectStateError, "NK-EPI support"):
            self.validate(registry=registry)

    def test_duplicate_assertion_is_rejected(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["families"][1]["assertions"][0]["assertion_id"] = registry[
            "families"
        ][0]["assertions"][0]["assertion_id"]
        with self.assertRaisesRegex(module.ProjectStateError, "duplicate assertion"):
            self.validate(registry=registry)

    def test_issue_64_must_remain_completed(self) -> None:
        state = copy.deepcopy(self.state)
        state["issues"]["64"]["state"] = "OPEN"
        with self.assertRaisesRegex(module.ProjectStateError, "Issue #64"):
            self.validate(state=state)

    def test_issue_verification_must_remain_direct(self) -> None:
        state = copy.deepcopy(self.state)
        state["issues"]["1"]["verification"]["method"] = "SUMMARY"
        with self.assertRaisesRegex(module.ProjectStateError, "verification method"):
            self.validate(state=state)

    def test_notion_synchronization_remains_required(self) -> None:
        state = copy.deepcopy(self.state)
        state["notion"]["synchronization_required"] = False
        with self.assertRaisesRegex(module.ProjectStateError, "must remain required"):
            self.validate(state=state)


if __name__ == "__main__":
    unittest.main()
