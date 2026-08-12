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

    def test_snapshot_cannot_predate_constituent_verification(self) -> None:
        state = copy.deepcopy(self.state)
        state["observed_at"] = "2000-01-01T00:00:00Z"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "observed_at predates constituent verification"):
            self.validate(state)

    def test_snapshot_timestamp_requires_timezone(self) -> None:
        state = copy.deepcopy(self.state)
        state["observed_at"] = "2026-08-11T16:51:48"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "timestamp must include timezone"):
            self.validate(state)

    def test_constituent_verification_timestamp_is_validated(self) -> None:
        state = copy.deepcopy(self.state)
        state["issues"]["88"]["verification"]["observed_at"] = "not-a-time"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "invalid .*verification.observed_at timestamp"):
            self.validate(state)

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

    def test_current_next_content_slice_is_d6(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["architecture_refoundation"]["next_content_slice"] = "BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION"
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

    def test_independent_review_completion_cannot_be_downgraded(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["post_blueprint_validation"]["independent_review_status"] = "NOT_ESTABLISHED"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "independent review completion drift"):
            self.validate(state)

    def test_bpv1_execution_authorization_cannot_drift_beyond_admitted_scope(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["post_blueprint_validation"]["bpv1_status"] = "AUTHORIZED"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "must remain experiment-only"):
            self.validate(state)

    def test_d5_r1_result_cannot_be_promoted_to_universal(self) -> None:
        state = copy.deepcopy(self.state)
        result = state["tracks"]["long_horizon_research"]["post_blueprint_validation"]["bpv1_execution_result"]
        result["oracle_outcome"] = "UNIVERSALLY_SUPPORTED"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "qualified oracle outcome drift"):
            self.validate(state)

    def test_d6_cannot_be_marked_started_in_d5_r1_checkpoint(self) -> None:
        state = copy.deepcopy(self.state)
        result = state["tracks"]["long_horizon_research"]["post_blueprint_validation"]["bpv1_execution_result"]
        result["d6_status"] = "IN_PROGRESS"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "D6 must remain not started"):
            self.validate(state)

    def test_hr10_self_report_path_cannot_reappear(self) -> None:
        state = copy.deepcopy(self.state)
        result = state["tracks"]["long_horizon_research"]["post_blueprint_validation"]["bpv1_execution_result"]
        result["hr10_self_report_path"] = "SUBJECT_SELF_REPORT"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "HR10 qualification drift"):
            self.validate(state)

    def test_plan_binding_cannot_authorize_execution(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["post_blueprint_validation"]["bpv1_plan"]["execution_authorized"] = True
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "execution must remain blocked"):
            self.validate(state)

    def test_plan_merge_binding_is_exact(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["post_blueprint_validation"]["bpv1_plan"]["authoritative_plan_merge_sha"] = "0" * 40
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "authoritative plan merge drift"):
            self.validate(state)

    def test_plan_identity_is_exact(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["post_blueprint_validation"]["bpv1_plan"]["plan_id"] = "BPV1-OTHER"
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "plan identity drift"):
            self.validate(state)

    def test_option_d_cannot_thaw_product_runtime(self) -> None:
        state = copy.deepcopy(self.state)
        state["tracks"]["long_horizon_research"]["post_blueprint_validation"]["product_runtime_thaw"] = True
        with self.assertRaisesRegex(module.ArchitectureFreezeError, "must not thaw product runtime"):
            self.validate(state)

    def test_iar1_review_result_is_required(self) -> None:
        original = module.IAR1_RESULT_JSON
        module.IAR1_RESULT_JSON = "docs/reviews/DOES_NOT_EXIST.json"
        try:
            with self.assertRaisesRegex(module.ArchitectureFreezeError, "missing IAR-1 review/reconciliation record"):
                self.validate()
        finally:
            module.IAR1_RESULT_JSON = original

    def test_iar1_review_must_cover_q1_q12(self) -> None:
        original = module._load_json_record
        def fake_load(path: Path, label: str):
            value = original(path, label)
            if label == "IAR-1 result":
                value["q1_q12_complete"] = False
            return value
        module._load_json_record = fake_load
        try:
            with self.assertRaisesRegex(module.ArchitectureFreezeError, "Q1-Q12 coverage"):
                self.validate()
        finally:
            module._load_json_record = original

    def test_independence_basis_cannot_be_empty_or_generic(self) -> None:
        original = module._load_json_record
        def fake_load(path: Path, label: str):
            value = original(path, label)
            if label == "IAR-1 result":
                value["reviewer"]["independence_basis"] = "x" * 120
            return value
        module._load_json_record = fake_load
        try:
            with self.assertRaisesRegex(module.ArchitectureFreezeError, "independence basis missing evidence marker"):
                self.validate()
        finally:
            module._load_json_record = original

    def test_input_packet_read_cannot_be_empty_or_partial(self) -> None:
        original = module._load_json_record
        def fake_load(path: Path, label: str):
            value = original(path, label)
            if label == "IAR-1 result":
                value["input_packet_read"] = []
            return value
        module._load_json_record = fake_load
        try:
            with self.assertRaisesRegex(module.ArchitectureFreezeError, "input packet evidence drift"):
                self.validate()
        finally:
            module._load_json_record = original

    def test_source_blocker_cannot_be_rewritten_as_nonblocking(self) -> None:
        original = module._load_json_record
        def fake_load(path: Path, label: str):
            value = original(path, label)
            if label == "IAR-1 result":
                value["findings"][0]["bpv1_dependency"] = "SHOULD_INFORM"
            return value
        module._load_json_record = fake_load
        try:
            with self.assertRaisesRegex(module.ArchitectureFreezeError, "source BPV-1 dependency drift"):
                self.validate()
        finally:
            module._load_json_record = original

    def test_source_finding_requires_protocol_evidence_fields(self) -> None:
        original = module._load_json_record
        def fake_load(path: Path, label: str):
            value = original(path, label)
            if label == "IAR-1 result":
                value["findings"][0].pop("counterexample_or_reasoning")
            return value
        module._load_json_record = fake_load
        try:
            with self.assertRaisesRegex(module.ArchitectureFreezeError, "source finding field required"):
                self.validate()
        finally:
            module._load_json_record = original

    def test_material_source_severity_cannot_drift(self) -> None:
        original = module._load_json_record
        def fake_load(path: Path, label: str):
            value = original(path, label)
            if label == "IAR-1 result":
                next(item for item in value["findings"] if item["finding_id"] == "IAR-F04")["severity"] = "MINOR"
            return value
        module._load_json_record = fake_load
        try:
            with self.assertRaisesRegex(module.ArchitectureFreezeError, "IAR-F04 severity drift"):
                self.validate()
        finally:
            module._load_json_record = original

    def test_reconciliation_must_resolve_every_blocker(self) -> None:
        original = module._load_json_record
        def fake_load(path: Path, label: str):
            value = original(path, label)
            if label == "IAR-1 reconciliation":
                value["findings"][0]["status"] = "OPEN"
            return value
        module._load_json_record = fake_load
        try:
            with self.assertRaisesRegex(module.ArchitectureFreezeError, "must be reconciled"):
                self.validate()
        finally:
            module._load_json_record = original

    def test_material_reconciliation_cannot_reopen(self) -> None:
        original = module._load_json_record
        def fake_load(path: Path, label: str):
            value = original(path, label)
            if label == "IAR-1 reconciliation":
                next(item for item in value["findings"] if item["finding_id"] == "IAR-F06")["status"] = "OPEN"
            return value
        module._load_json_record = fake_load
        try:
            with self.assertRaisesRegex(module.ArchitectureFreezeError, "IAR-F06 must be reconciled"):
                self.validate()
        finally:
            module._load_json_record = original

    def test_preregistration_fields_must_match_exact_inventory(self) -> None:
        original = module._load_json_record
        def fake_load(path: Path, label: str):
            value = original(path, label)
            if label == "IAR-1 reconciliation":
                value["conformance_preregistration"]["fields"].remove("threat_model")
            return value
        module._load_json_record = fake_load
        try:
            with self.assertRaisesRegex(module.ArchitectureFreezeError, "preregistration field inventory drift"):
                self.validate()
        finally:
            module._load_json_record = original


if __name__ == "__main__":
    unittest.main()
