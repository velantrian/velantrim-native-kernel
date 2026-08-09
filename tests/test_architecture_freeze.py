from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "ai_context" / "validate_architecture_freeze.py"
SPEC = importlib.util.spec_from_file_location("validate_architecture_freeze", MODULE_PATH)
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class ArchitectureFreezeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.state = json.loads((ROOT / "project-state.json").read_text(encoding="utf-8"))

    def validate(self, state: dict | None = None) -> None:
        module.validate(copy.deepcopy(self.state) if state is None else state, repo=ROOT)

    def test_repository_freeze_passes(self) -> None:
        self.validate()

    def test_refoundation_object_is_required(self) -> None:
        state = copy.deepcopy(self.state)
        del state["tracks"]["long_horizon_research"]["architecture_refoundation"]
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "architecture_refoundation object required"):
            self.validate(state)

    def test_runtime_freeze_cannot_be_disabled(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["architecture_refoundation"]["runtime_expansion_frozen"] = False
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "freeze must remain enabled"):
            self.validate(state)

    def test_semantic_runtime_expansion_cannot_be_authorized(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["clean_implementation"]["semantic_runtime_expansion_authorized"] = True
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "not authorized"):
            self.validate(state)

    def test_reference_laboratory_role_cannot_be_promoted(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["clean_implementation"]["architecture_role"] = "CANON"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "bounded reference laboratory"):
            self.validate(state)

    def test_blueprint_deliverables_are_exact(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["architecture_refoundation"]["deliverables"].pop()
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "deliverable inventory"):
            self.validate(state)

    def test_completion_retains_separate_operator_review(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["architecture_refoundation"]["completion_requires_operator_review"] = False
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "separate operator review"):
            self.validate(state)

    def test_completed_deliverable_inventory_is_exact(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["architecture_refoundation"]["completed_deliverables"] = [
            "A1_KERNEL_PURPOSE_AND_NON_GOALS"
        ]
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "completed blueprint deliverable inventory drift"):
            self.validate(state)

    def test_completed_deliverable_must_be_declared(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["architecture_refoundation"]["completed_deliverables"] = [
            "A1_KERNEL_PURPOSE_AND_NON_GOALS",
            "NOT_A_REAL_DELIVERABLE",
        ]
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "completed blueprint deliverable inventory drift"):
            self.validate(state)

    def test_next_content_slice_must_be_a3(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["architecture_refoundation"]["next_content_slice"] = (
            "A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY"
        )
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "next blueprint content slice drift"):
            self.validate(state)

    def test_next_content_slice_cannot_be_completed(self) -> None:
        state = copy.deepcopy(self.state)
        refoundation = state["tracks"]["long_horizon_research"]["architecture_refoundation"]
        refoundation["completed_deliverables"] = [
            "A1_KERNEL_PURPOSE_AND_NON_GOALS",
            "A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY",
            "A3_ABSTRACT_NATIVE_KERNEL_MACHINE",
        ]
        module.EXPECTED_COMPLETED_DELIVERABLES.append("A3_ABSTRACT_NATIVE_KERNEL_MACHINE")
        try:
            with self.assertRaisesRegex(module.ArchitectureFreezeError, "must not already be marked completed"):
                self.validate(state)
        finally:
            module.EXPECTED_COMPLETED_DELIVERABLES.pop()

    def test_each_completed_deliverable_document_must_exist(self) -> None:
        original = module.COMPLETED_DELIVERABLE_DOCS["A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY"]
        module.COMPLETED_DELIVERABLE_DOCS["A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY"] = (
            "docs/DOES_NOT_EXIST.md",
        )
        try:
            with self.assertRaisesRegex(module.ArchitectureFreezeError, "missing completed deliverable document"):
                self.validate()
        finally:
            module.COMPLETED_DELIVERABLE_DOCS["A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY"] = original

    def test_completed_deliverable_requires_document_mapping(self) -> None:
        original = module.COMPLETED_DELIVERABLE_DOCS.pop("A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY")
        try:
            with self.assertRaisesRegex(module.ArchitectureFreezeError, "missing completed deliverable document mapping"):
                self.validate()
        finally:
            module.COMPLETED_DELIVERABLE_DOCS["A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY"] = original

    def test_issue_88_must_remain_open_and_verified(self) -> None:
        state = copy.deepcopy(self.state)
        state["issues"]["88"]["state"] = "CLOSED"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "must remain open"):
            self.validate(state)

        state = copy.deepcopy(self.state)
        state["issues"]["88"]["verification"]["method"] = "SUMMARY"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "verification drift"):
            self.validate(state)


if __name__ == "__main__":
    unittest.main()
