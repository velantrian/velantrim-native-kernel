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

    def test_runtime_freeze_cannot_be_disabled(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["architecture_refoundation"]["runtime_expansion_frozen"] = False
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "freeze must remain enabled"):
            self.validate(state)

    def test_runtime_expansion_cannot_be_authorized(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["clean_implementation"]["semantic_runtime_expansion_authorized"] = True
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "not authorized"):
            self.validate(state)

    def test_reference_laboratory_cannot_be_promoted(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["clean_implementation"]["architecture_role"] = "CANON"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "bounded reference laboratory"):
            self.validate(state)

    def test_completed_deliverables_remain_exact_a1_a10(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["architecture_refoundation"]["completed_deliverables"].pop()
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "completed blueprint deliverable inventory drift"):
            self.validate(state)

    def test_next_gate_is_independent_architecture_review(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["architecture_refoundation"]["next_content_slice"] = "BPV1"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "next architecture validation gate drift"):
            self.validate(state)

    def test_operator_gate_is_not_a_deliverable(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["architecture_refoundation"]["completed_deliverables"].append("OPERATOR_POST_BLUEPRINT_DECISION")
        module.EXPECTED_COMPLETED_DELIVERABLES.append("OPERATOR_POST_BLUEPRINT_DECISION")
        try:
            with self.assertRaisesRegex(module.ArchitectureFreezeError, "operator gate must not be treated as an A1-A10 deliverable"):
                self.validate(state)
        finally:
            module.EXPECTED_COMPLETED_DELIVERABLES.pop()

    def test_independent_review_gate_is_not_a_deliverable(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["architecture_refoundation"]["completed_deliverables"].append("INDEPENDENT_ARCHITECTURE_REVIEW")
        module.EXPECTED_COMPLETED_DELIVERABLES.append("INDEPENDENT_ARCHITECTURE_REVIEW")
        try:
            with self.assertRaisesRegex(module.ArchitectureFreezeError, "independent review gate must not be treated as an A1-A10 deliverable"):
                self.validate(state)
        finally:
            module.EXPECTED_COMPLETED_DELIVERABLES.pop()

    def test_integrated_review_is_not_a_deliverable(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["architecture_refoundation"]["completed_deliverables"].append("INTEGRATED_A1_A10_REVIEW")
        module.EXPECTED_COMPLETED_DELIVERABLES.append("INTEGRATED_A1_A10_REVIEW")
        try:
            with self.assertRaisesRegex(module.ArchitectureFreezeError, "integrated review must not be treated as an A1-A10 deliverable"):
                self.validate(state)
        finally:
            module.EXPECTED_COMPLETED_DELIVERABLES.pop()

    def test_integrated_review_documents_are_required(self) -> None:
        original = module.INTEGRATED_REVIEW_DOCS
        module.INTEGRATED_REVIEW_DOCS = ("docs/DOES_NOT_EXIST.md",)
        try:
            with self.assertRaisesRegex(module.ArchitectureFreezeError, "missing integrated review document"):
                self.validate()
        finally:
            module.INTEGRATED_REVIEW_DOCS = original

    def test_independent_review_protocol_documents_are_required(self) -> None:
        original = module.INDEPENDENT_REVIEW_DOCS
        module.INDEPENDENT_REVIEW_DOCS = ("docs/DOES_NOT_EXIST.md", "docs/ALSO_MISSING.md")
        try:
            with self.assertRaisesRegex(module.ArchitectureFreezeError, "independent review English document drift"):
                self.validate()
        finally:
            module.INDEPENDENT_REVIEW_DOCS = original

    def test_option_d_selection_cannot_drift(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["post_blueprint_validation"]["selected_option"] = "C_RUNTIME_THAW"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "Option D selection drift"):
            self.validate(state)

    def test_independent_review_cannot_be_self_certified(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["post_blueprint_validation"]["independent_review_status"] = "QUALIFYING_REVIEW_COMPLETE"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "must not be self-certified"):
            self.validate(state)

    def test_bpv1_cannot_be_unblocked_before_review_and_reconciliation(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["post_blueprint_validation"]["bpv1_status"] = "AUTHORIZED"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "BPV-1 must remain blocked"):
            self.validate(state)

    def test_option_d_cannot_thaw_product_runtime(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["post_blueprint_validation"]["product_runtime_thaw"] = True
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "must not thaw product runtime"):
            self.validate(state)

    def test_issue_88_remains_open_verified_and_records_option_d(self) -> None:
        state = copy.deepcopy(self.state)
        state["issues"]["88"]["state"] = "CLOSED"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "must remain open"):
            self.validate(state)
        state = copy.deepcopy(self.state)
        state["issues"]["88"]["meaning"] = "Architecture Re-foundation is active."
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "Option D selection"):
            self.validate(state)
        state = copy.deepcopy(self.state)
        state["issues"]["88"]["verification"]["method"] = "SUMMARY"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "verification drift"):
            self.validate(state)


if __name__ == "__main__":
    unittest.main()