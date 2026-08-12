#!/usr/bin/env python3
"""Fail closed when Native Kernel post-blueprint validation truth drifts.

Historical IAR-1/IAR-1-R1 and BPV1 preregistration/admission records retain
publication-time semantics. Current project truth records Option D validation
through D8 as complete while Final Canon/runtime authority remains a separate
operator decision.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator, Mapping

EXPECTED_DELIVERABLES = [
    "A1_KERNEL_PURPOSE_AND_NON_GOALS",
    "A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY",
    "A3_ABSTRACT_NATIVE_KERNEL_MACHINE",
    "A4_SEMANTIC_LAWS_AND_INVARIANTS",
    "A5_IDENTITY_TIME_AND_CHANGE",
    "A6_KNOWLEDGE_LIFECYCLE",
    "A7_CONFLICT_UNCERTAINTY_AND_REVISION",
    "A8_SUBSTRATE_INDEPENDENCE_CONTRACT",
    "A9_REFERENCE_LABORATORY_BOUNDARY",
    "A10_OPEN_QUESTIONS_AND_FALSIFICATION",
]
EXPECTED_FREEZE_EXCEPTIONS = [
    "integrity and security fixes",
    "reproducibility and provenance corrections",
    "evidence preservation",
    "validator and current-truth repairs",
    "historical recovery",
    "isolated blueprint falsification experiments without runtime promotion",
]
EXPECTED_PROMOTION_REQUIREMENTS = [
    "explicit ontology or semantic law",
    "abstract machine or contract",
    "failure and falsification cases",
    "separate decision record",
    "operator approval",
]
EXPECTED_REFOUNDATION_FIELDS = {
    "decision", "issue", "operator_approval", "status", "runtime_expansion_frozen",
    "existing_reference_runtime_role", "plan_en", "plan_ru", "deliverables",
    "completion_requires_operator_review", "completed_deliverables", "next_content_slice",
}
EXPECTED_POST_BLUEPRINT_FIELDS = {
    "decision", "issue", "operator_approval", "selected_option", "status",
    "independent_review_protocol", "independent_review_document_en",
    "independent_review_document_ru", "independent_review_status", "bpv1_status",
    "bpv1_role", "bpv1_plan", "bpv1_execution_admission", "bpv1_execution_result",
    "d6_hypothesis_classification", "d7_integrated_rereview", "d8_consolidated_sync",
    "product_runtime_thaw", "automatic_canon_promotion", "automatic_runtime_promotion",
}
EXPECTED_CURRENT_RESEARCH_STATUS = "ACTIVE / OPTION D VALIDATION COMPLETE / OPERATOR DECISION REQUIRED / NO AUTOMATIC PROMOTION"
EXPECTED_REFOUNDATION_STATUS = "BLUEPRINT COMPLETE / PROVISIONAL / OPTION D VALIDATION COMPLETE"
EXPECTED_CURRENT_VALIDATION_STATUS = "COMPLETE / OPTION_D_VALIDATION_AND_SYNC_COMPLETE / AWAITING_SEPARATE_OPERATOR_DECISION"
EXPECTED_CURRENT_NEXT_CONTENT_SLICE = "OPERATOR_CANON_RUNTIME_DECISION_REQUIRED"
EXPECTED_CURRENT_BPV1_STATUS = "ADMITTED_FOR_EXPERIMENT_ONLY"
EXPECTED_HISTORICAL_RECONCILIATION_NEXT_GATE = "BPV1_PLAN_AND_PREREGISTRATION"
EXPECTED_PLAN_NEXT_GATE = "BPV1_EXECUTION_ADMISSION"
EXPECTED_PLAN_POST_MERGE_STATUS = "BLOCKED_PENDING_EXECUTION_ADMISSION"
EXPECTED_PLAN_ID = "BPV1-001-cross-lineage-bounded-accountability-v1"
EXPECTED_PLAN_PROTOCOL = "nk-bpv1-preregistration/1"
EXPECTED_PLAN_PATH = "docs/research/BPV1_PREREGISTRATION.json"
EXPECTED_PLAN_MERGE_SHA = "a538d7f1e28858a88b9ee777ac7d6e05b85943db"
EXPECTED_PLAN_SHA256 = "7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0"
EXPECTED_ADMISSION_PACKAGE_MERGE_SHA = "6027eec73f11c4626be5553de7e79f827be2c81d"
EXPECTED_ADMISSION_STATUS_MERGE_SHA = "e2deac859c2a56f29b88c54f1da440f3f04734dc"
EXPECTED_D5_MERGE_SHA = "a191e9c868c14af34a269dcdfae44406f1013bda"
EXPECTED_D5_R1_MERGE_SHA = "3856740570620fb2243e2f0da76359281ec4068f"
EXPECTED_D6_MERGE_SHA = "030d0a0585bd061b27329a38e29708c11304701a"
EXPECTED_D7_MERGE_SHA = "491ff7b229606d228ca04985b19b146878390e08"
EXPECTED_D8_MERGE_SHA = "9ecb2369edec17a0171b6e965bcb49f9526adf0b"
EXPECTED_D5_R1_OUTCOME = "SUPPORTED_FOR_SCOPE"
SUPPORTED_HYPOTHESES = ["A10-H01", "A10-H02", "A10-H04", "A10-H05", "A10-H07", "A10-H12"]
NOT_TESTED_HYPOTHESES = ["A10-H03", "A10-H06", "A10-H08", "A10-H09", "A10-H10", "A10-H11"]
IAR_RESULT_PATH = "docs/reviews/IAR-1_RESULT.json"
IAR_RECON_PATH = "docs/reviews/IAR-1_RECONCILIATION.json"
D6_PATH = "docs/research/BPV1_D6_A10_CLASSIFICATION.json"
D7_PATH = "docs/research/BPV1_D7_INTEGRATED_REREVIEW.json"
D8_PATH = "docs/research/BPV1_D8_CONSOLIDATED_SYNC.json"

EXPECTED_IAR_BLOCKERS = ["IAR-F01", "IAR-F02", "IAR-F03", "IAR-F05", "IAR-F07", "IAR-F08", "IAR-F09"]
EXPECTED_IAR_MATERIAL = ["IAR-F04", "IAR-F06", "IAR-F10"]
EXPECTED_IAR_SEVERITY = {
    **{item: "BLOCKING" for item in EXPECTED_IAR_BLOCKERS},
    **{item: "MATERIAL" for item in EXPECTED_IAR_MATERIAL},
}
EXPECTED_RECON_DEPENDENCY = {
    **{item: "RESOLVED_BEFORE_PLAN" for item in EXPECTED_IAR_BLOCKERS},
    "IAR-F04": "INFORMS_PLAN",
    "IAR-F06": "INFORMS_PLAN",
    "IAR-F10": "INFORMS_FUTURE_COMPOSITION_SCOPE",
}
EXPECTED_PREREG_FIELDS = [
    "scenario_id", "purpose_scope", "mandatory_obligations", "applicability_rules",
    "mandatory_observables", "equivalence_predicates", "allowed_declared_losses",
    "failure_thresholds", "hard_refutation_observations", "grounding_mode",
    "threat_model", "oracle_authority",
]


class ArchitectureFreezeError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ArchitectureFreezeError(message)


def _load_json(path: Path, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ArchitectureFreezeError(f"cannot read {label}: {exc}") from exc
    _require(isinstance(value, dict), f"{label} must contain an object")
    return value


def _load(path: Path) -> dict[str, Any]:
    return _load_json(path, "project state")


def _parse_timestamp(value: Any, label: str) -> datetime:
    _require(isinstance(value, str) and value.strip(), f"{label} timestamp required")
    try:
        parsed = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError as exc:
        raise ArchitectureFreezeError(f"invalid {label} timestamp: {value}") from exc
    _require(parsed.tzinfo is not None, f"{label} timestamp must include timezone")
    return parsed.astimezone(timezone.utc)


def _verification_observations(value: Any, path: str = "$") -> Iterator[tuple[str, Any]]:
    if isinstance(value, Mapping):
        verification = value.get("verification")
        if isinstance(verification, Mapping) and "observed_at" in verification:
            yield f"{path}.verification.observed_at", verification.get("observed_at")
        for key, child in value.items():
            if key != "verification":
                yield from _verification_observations(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _verification_observations(child, f"{path}[{index}]")


def _validate_snapshot_chronology(state: Mapping[str, Any]) -> None:
    snapshot = _parse_timestamp(state.get("observed_at"), "project-state observed_at")
    for path, raw in _verification_observations(state):
        _require(snapshot >= _parse_timestamp(raw, path), f"project-state observed_at predates constituent verification: {path}")


def _validate_iar_history(repo: Path) -> None:
    result = _load_json(repo / IAR_RESULT_PATH, "IAR-1 result")
    _require(result.get("protocol") == "nk-independent-architecture-review-result/1", "IAR-1 result protocol drift")
    _require(result.get("review_id") == "IAR-1", "IAR-1 identity drift")
    _require(result.get("process_outcome") == "QUALIFYING_REVIEW_COMPLETE", "IAR-1 must be a qualifying completed review")
    _require(result.get("reviewed_commit") == "2dd51723e30d5f3c5e86268365bf4cf7639b5e9a", "IAR-1 reviewed commit drift")
    _require(result.get("q1_q12_complete") is True, "IAR-1 Q1-Q12 coverage must be complete")
    _require(result.get("finding_count") == 10, "IAR-1 finding count drift")
    _require(result.get("blocking_findings") == EXPECTED_IAR_BLOCKERS, "IAR-1 blocking finding inventory drift")
    _require(result.get("material_findings") == EXPECTED_IAR_MATERIAL, "IAR-1 material finding inventory drift")
    _require(result.get("bpv1_status_recommendation") == "BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION", "IAR-1 must not itself admit BPV-1")
    _require(result.get("product_runtime_status") == "FROZEN", "IAR-1 must preserve runtime freeze")
    reviewer = result.get("reviewer")
    _require(isinstance(reviewer, Mapping), "IAR-1 reviewer record required")
    basis = reviewer.get("independence_basis")
    _require(isinstance(basis, str) and len(basis.strip()) >= 80, "IAR-1 substantive independence basis required")
    for marker in ("Separate GitHub review agent", "contributor/collaborator", "did not author"):
        _require(marker in basis, f"IAR-1 independence basis missing evidence marker: {marker}")
    _require(reviewer.get("prior_authorship_of_A1_A10") is False, "IAR-1 reviewer cannot be A1-A10 author")
    _require(reviewer.get("prior_authorship_of_integrated_review") is False, "IAR-1 reviewer cannot be integrated-review author")
    findings = result.get("findings")
    _require(isinstance(findings, list) and len(findings) == 10, "IAR-1 findings register must contain ten entries")
    by_id = {item.get("finding_id"): item for item in findings if isinstance(item, Mapping)}
    _require(set(by_id) == set(EXPECTED_IAR_SEVERITY), "IAR-1 finding ids drift")
    for finding_id, item in by_id.items():
        _require(item.get("severity") == EXPECTED_IAR_SEVERITY[finding_id], f"{finding_id} severity drift")
        _require(item.get("status") == "OPEN", f"{finding_id} source review status must remain OPEN")
        for field in ("claim_or_obligation", "finding", "counterexample_or_reasoning", "implementation_capture_risk", "falsifiability_impact", "recommended_disposition", "source_review_comment_id"):
            _require(item.get(field) not in (None, "", []), f"{finding_id} source finding field required: {field}")

    recon = _load_json(repo / IAR_RECON_PATH, "IAR-1 reconciliation")
    _require(recon.get("protocol") == "nk-independent-architecture-review-reconciliation/1", "IAR-1 reconciliation protocol drift")
    _require(recon.get("reconciliation_id") == "IAR-1-R1", "IAR-1 reconciliation identity drift")
    _require(recon.get("status") == "COMPLETE", "IAR-1 reconciliation must be complete")
    _require(recon.get("architecture_status") == "PROVISIONAL_RECONCILED", "IAR-1 architecture status drift")
    _require(recon.get("runtime_expansion") == "FROZEN", "IAR-1 reconciliation must preserve runtime freeze")
    _require(recon.get("bpv1_status_after_reconciliation") == "BLOCKED_PENDING_PREREGISTERED_PLAN", "IAR-1 reconciliation must preserve its historical post-review BPV-1 status")
    _require(recon.get("next_gate") == EXPECTED_HISTORICAL_RECONCILIATION_NEXT_GATE, "IAR-1 reconciliation next gate drift")
    _require(recon.get("open_blocking_findings") == [], "IAR-1 reconciliation cannot leave blocking findings open")
    _require(recon.get("open_material_findings") == [], "IAR-1 reconciliation cannot leave material findings untracked")
    _require(recon.get("automatic_canon_promotion") is False, "IAR-1 reconciliation cannot auto-promote Canon")
    _require(recon.get("automatic_runtime_promotion") is False, "IAR-1 reconciliation cannot auto-promote runtime")
    rows = recon.get("findings")
    _require(isinstance(rows, list) and len(rows) == 10, "IAR-1 reconciliation must cover all findings")
    reconciled = {item.get("finding_id"): item for item in rows if isinstance(item, Mapping)}
    _require(set(reconciled) == set(EXPECTED_IAR_SEVERITY), "IAR-1 reconciliation finding inventory drift")
    for finding_id, item in reconciled.items():
        _require(item.get("severity") == EXPECTED_IAR_SEVERITY[finding_id], f"{finding_id} reconciliation severity drift")
        _require(item.get("status") == "RESOLVED", f"{finding_id} must be reconciled")
        _require(bool(str(item.get("reconciliation_record", "")).strip()), f"{finding_id} reconciliation record required")
        _require(item.get("bpv1_dependency") == EXPECTED_RECON_DEPENDENCY[finding_id], f"{finding_id} reconciliation BPV-1 dependency drift")
    prereg = recon.get("conformance_preregistration")
    _require(isinstance(prereg, Mapping), "IAR-1 preregistration boundary required")
    fields = prereg.get("fields")
    _require(fields == EXPECTED_PREREG_FIELDS, "preregistration field inventory drift")
    _require(len(fields) == len(set(fields)), "preregistration field inventory contains duplicates")
    _require(prereg.get("post_hoc_rescoping") == "INVALIDATES_RUN_FOR_CLAIMED_SCOPE", "post-hoc BPV-1 rescoping must fail closed")
    principles = recon.get("principles")
    _require(isinstance(principles, Mapping), "IAR-1 refined principle boundary required")
    _require(principles.get("event_sourcing_universal") is False, "Event sourcing cannot become universal")
    _require(principles.get("exact_reconstruction_universal") is False, "exact reconstruction cannot remain universal")
    _require(principles.get("global_total_order_universal") is False, "global total order cannot become universal")
    _require(principles.get("composition_conformance_implied_by_local_conformance") is False, "local conformance cannot imply composition conformance")


def _validate_plan_admission_and_d5(validation: Mapping[str, Any], repo: Path) -> None:
    plan = validation.get("bpv1_plan")
    _require(isinstance(plan, Mapping), "BPV-1 plan binding required")
    _require(plan.get("protocol") == EXPECTED_PLAN_PROTOCOL, "BPV-1 plan protocol drift")
    _require(plan.get("plan_id") == EXPECTED_PLAN_ID, "BPV-1 plan identity drift")
    _require(plan.get("path") == EXPECTED_PLAN_PATH, "BPV-1 plan path drift")
    _require(plan.get("authoritative_plan_merge_sha") == EXPECTED_PLAN_MERGE_SHA, "BPV-1 authoritative plan merge drift")
    _require(plan.get("status") == "PREREGISTERED / EXECUTION_NOT_AUTHORIZED", "BPV-1 plan status drift")
    _require(plan.get("execution_authorized") is False, "BPV-1 execution must remain blocked at the plan level")
    _require(plan.get("execution_admission_required") is True, "BPV-1 execution admission must remain required")
    _require(plan.get("next_gate") == EXPECTED_PLAN_NEXT_GATE, "BPV-1 plan historical next gate drift")
    frozen = _load_json(repo / EXPECTED_PLAN_PATH, "BPV-1 preregistration")
    _require(frozen.get("plan_id") == EXPECTED_PLAN_ID, "BPV-1 preregistration identity drift")
    _require(frozen.get("execution_authorized") is False, "merged BPV-1 preregistration cannot itself authorize execution")
    boundary = frozen.get("execution_boundary")
    _require(isinstance(boundary, Mapping), "BPV-1 execution boundary required")
    _require(boundary.get("plan_merge_authorizes_execution") is False, "plan merge alone cannot authorize BPV-1 execution")
    _require(boundary.get("execution_status_after_plan_merge") == EXPECTED_PLAN_POST_MERGE_STATUS, "BPV-1 post-plan-merge execution status drift")

    admission = validation.get("bpv1_execution_admission")
    _require(isinstance(admission, Mapping), "BPV-1 execution-admission status record required")
    _require(admission.get("status") == "COMPLETE", "BPV-1 execution-admission status drift")
    _require(admission.get("admission_package_merge_sha") == EXPECTED_ADMISSION_PACKAGE_MERGE_SHA, "BPV-1 execution-admission package merge drift")
    _require(admission.get("status_checkpoint_merge_sha") == EXPECTED_ADMISSION_STATUS_MERGE_SHA, "BPV-1 execution-admission checkpoint merge drift")
    _require(admission.get("plan_sha256") == EXPECTED_PLAN_SHA256, "BPV-1 execution-admission frozen plan digest drift")
    _require(admission.get("subject_implementation_authorization") == "AUTHORIZED_FOR_BPV1-001_ONLY", "BPV-1 subject implementation authorization drift")
    _require(admission.get("subject_execution_authorization") == "AUTHORIZED_FOR_BPV1-001_ONLY", "BPV-1 subject execution authorization drift")
    _require(admission.get("product_runtime_integration_authorized") is False, "BPV-1 execution admission cannot authorize product runtime integration")
    _require(admission.get("runtime_expansion") == "FROZEN", "BPV-1 execution admission must preserve runtime freeze")

    result = validation.get("bpv1_execution_result")
    _require(isinstance(result, Mapping), "BPV-1 execution result record required")
    _require(result.get("historical_d5_merge_sha") == EXPECTED_D5_MERGE_SHA, "BPV-1 historical D5 merge drift")
    _require(result.get("qualification_merge_sha") == EXPECTED_D5_R1_MERGE_SHA, "BPV-1 D5-R1 merge drift")
    _require(result.get("qualification_status") == "QUALIFIED", "BPV-1 D5-R1 must remain qualified")
    _require(result.get("oracle_outcome") == EXPECTED_D5_R1_OUTCOME, "BPV-1 qualified oracle outcome drift")
    _require(result.get("mandatory_fixtures") == 12 and result.get("mandatory_fixture_pass") == 12, "BPV-1 mandatory fixture PASS count drift")
    _require(result.get("mandatory_fixture_fail") == 0 and result.get("mandatory_fixture_indeterminate") == 0, "BPV-1 mandatory fixture failure drift")
    _require(result.get("workload_mutations") == 512, "BPV-1 mutation count drift")
    _require(result.get("checkpoint_mutations") == [128, 256, 512], "BPV-1 checkpoint inventory drift")
    _require(result.get("hr10_self_report_path") == "REMOVED_BY_EXTERNAL_QUALIFICATION", "BPV-1 HR10 qualification drift")
    _require(result.get("independent_team") == "NOT_ESTABLISHED", "BPV-1 independent-team overclaim")
    _require(result.get("independent_custody") == "NOT_ESTABLISHED", "BPV-1 independent-custody overclaim")
    _require(result.get("independent_computation_model") == "NOT_ESTABLISHED / CONVENTIONAL_DIGITAL", "BPV-1 computation-model overclaim")
    _require(result.get("d6_status") == "COMPLETE", "D6 completion drift")
    _require(result.get("d7_status") == "COMPLETE", "D7 completion drift")
    _require(result.get("d8_status") == "COMPLETE / READ_BACK_VERIFIED", "D8 completion drift")
    _require(result.get("next_gate") == EXPECTED_CURRENT_NEXT_CONTENT_SLICE, "post-D8 operator gate drift")


def _validate_d6_d7_d8(validation: Mapping[str, Any], repo: Path) -> None:
    d6 = validation.get("d6_hypothesis_classification")
    _require(isinstance(d6, Mapping), "D6 hypothesis classification required")
    _require(d6.get("protocol") == "nk-a10-hypothesis-classification/1", "D6 protocol drift")
    _require(d6.get("status") == "COMPLETE", "D6 status drift")
    _require(d6.get("merge_sha") == EXPECTED_D6_MERGE_SHA, "D6 merge drift")
    _require(d6.get("supported_for_scope") == SUPPORTED_HYPOTHESES, "D6 supported hypothesis inventory drift")
    _require(d6.get("not_tested") == NOT_TESTED_HYPOTHESES, "D6 not-tested hypothesis inventory drift")
    _require(d6.get("weakened") == [] and d6.get("refuted") == [] and d6.get("indeterminate") == [], "D6 outcome arithmetic drift")
    d6_file = _load_json(repo / D6_PATH, "D6 classification")
    _require(d6_file.get("summary") == {"SUPPORTED_FOR_SCOPE": 6, "WEAKENED": 0, "REFUTED": 0, "INDETERMINATE": 0, "NOT_TESTED": 6, "total": 12}, "D6 summary drift")

    d7 = validation.get("d7_integrated_rereview")
    _require(isinstance(d7, Mapping), "D7 integrated re-review required")
    _require(d7.get("status") == "COMPLETE", "D7 status drift")
    _require(d7.get("merge_sha") == EXPECTED_D7_MERGE_SHA, "D7 merge drift")
    _require(d7.get("review_outcome") == "PROVISIONAL_VALIDATION_REVIEW_COMPLETE", "D7 outcome drift")
    _require(d7.get("architecture_position") == "STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL", "D7 architecture position drift")
    d7_file = _load_json(repo / D7_PATH, "D7 integrated re-review")
    conclusions = d7_file.get("review_conclusions")
    _require(isinstance(conclusions, Mapping), "D7 review conclusions required")
    _require(conclusions.get("a1_a10_final_canon") is False, "D7 cannot promote Final Canon")
    _require(conclusions.get("universal_substrate_independence_proven") is False, "D7 cannot claim universal substrate independence")
    _require(conclusions.get("runtime_thaw_authorized") is False, "D7 cannot thaw runtime")

    d8 = validation.get("d8_consolidated_sync")
    _require(isinstance(d8, Mapping), "D8 consolidated sync required")
    _require(d8.get("status") == "COMPLETE / READ_BACK_VERIFIED", "D8 status drift")
    _require(d8.get("merge_sha") == EXPECTED_D8_MERGE_SHA, "D8 merge drift")
    _require(d8.get("source_checkpoint_sha") == EXPECTED_D7_MERGE_SHA, "D8 source checkpoint drift")
    _require(d8.get("notion_surface_count") == 7 and d8.get("notion_read_back_verified_count") == 7, "D8 Notion read-back drift")
    _require(d8.get("new_notion_pages_created") == 0, "D8 must not create new Notion pages")
    _require(d8.get("next_gate") == EXPECTED_CURRENT_NEXT_CONTENT_SLICE, "D8 next gate drift")
    _require(d8.get("next_gate_authorized_by_d8") is False, "D8 cannot authorize operator decision outcome")
    _require(d8.get("operator_decision_required") is True, "D8 must preserve separate operator decision")
    d8_file = _load_json(repo / D8_PATH, "D8 consolidated synchronization")
    sync = d8_file.get("notion_sync")
    _require(isinstance(sync, Mapping), "D8 Notion sync evidence required")
    _require(sync.get("surface_count") == 7 and sync.get("read_back_verified_count") == 7, "D8 repository sync evidence drift")
    _require(sync.get("new_pages_created") == 0 and sync.get("historical_content_preserved") is True, "D8 Notion scope drift")
    _require(d8_file.get("next_gate_authorized_by_d8") is False, "D8 evidence cannot authorize operator decision")


def validate(state: Mapping[str, Any], *, repo: Path) -> None:
    _require(state.get("protocol") == "nk-project-state/2", "unsupported project-state protocol")
    _validate_snapshot_chronology(state)
    status = state.get("status")
    _require(isinstance(status, Mapping), "status object required")
    _require(status.get("production_authorized") is False, "architecture validation cannot coexist with production authorization")

    tracks = state.get("tracks")
    _require(isinstance(tracks, Mapping), "tracks object required")
    clean = tracks.get("clean_implementation")
    _require(isinstance(clean, Mapping), "clean implementation track required")
    _require(clean.get("architecture_role") == "BOUNDED_REFERENCE_LABORATORY", "clean implementation must remain a bounded reference laboratory")
    _require(clean.get("semantic_runtime_expansion_authorized") is False, "semantic/runtime expansion is not authorized")
    _require(clean.get("maintenance_allowed") is True, "bounded maintenance allowance must remain explicit")

    research = tracks.get("long_horizon_research")
    _require(isinstance(research, Mapping), "long-horizon research track required")
    _require(research.get("status") == EXPECTED_CURRENT_RESEARCH_STATUS, "post-blueprint validation status drift")
    _require(research.get("runtime_authorized") is False, "research track must not authorize runtime")

    refoundation = research.get("architecture_refoundation")
    _require(isinstance(refoundation, Mapping), "ADR-0025 architecture_refoundation object required")
    _require(set(refoundation) == EXPECTED_REFOUNDATION_FIELDS, "architecture_refoundation field inventory drift")
    _require((refoundation.get("decision"), refoundation.get("issue"), refoundation.get("operator_approval")) == ("ADR-0025", 88, "APPROVED"), "ADR-0025 identity, issue or approval drift")
    _require(refoundation.get("status") == EXPECTED_REFOUNDATION_STATUS, "ADR-0025 phase drift")
    _require(refoundation.get("runtime_expansion_frozen") is True, "runtime expansion freeze must remain enabled")
    _require(refoundation.get("existing_reference_runtime_role") == "BOUNDED_REFERENCE_LABORATORY", "existing runtime role drift")
    _require(refoundation.get("deliverables") == EXPECTED_DELIVERABLES, "A1-A10 blueprint deliverable inventory drift")
    _require(refoundation.get("completed_deliverables") == EXPECTED_DELIVERABLES, "completed blueprint deliverable inventory drift")
    _require(refoundation.get("next_content_slice") == EXPECTED_CURRENT_NEXT_CONTENT_SLICE, "next architecture validation gate drift")

    validation = research.get("post_blueprint_validation")
    _require(isinstance(validation, Mapping), "ADR-0026 post_blueprint_validation object required")
    _require(set(validation) == EXPECTED_POST_BLUEPRINT_FIELDS, "post_blueprint_validation field inventory drift")
    _require((validation.get("decision"), validation.get("issue"), validation.get("operator_approval")) == ("ADR-0026", 88, "APPROVED"), "ADR-0026 identity, issue or approval drift")
    _require(validation.get("selected_option") == "D_INDEPENDENT_CHALLENGE_THEN_BOUNDED_CROSS_LINEAGE_FALSIFICATION", "post-blueprint Option D selection drift")
    _require(validation.get("status") == EXPECTED_CURRENT_VALIDATION_STATUS, "post-blueprint validation phase drift")
    _require(validation.get("independent_review_status") == "QUALIFYING_REVIEW_COMPLETE", "independent review completion drift")
    _require(validation.get("bpv1_status") == EXPECTED_CURRENT_BPV1_STATUS, "BPV-1 execution authorization must remain experiment-only")
    _require(validation.get("bpv1_role") == "FALSIFICATION_INSTRUMENT_ONLY", "BPV-1 role drift")
    _require(validation.get("product_runtime_thaw") is False, "Option D must not thaw product runtime")
    _require(validation.get("automatic_canon_promotion") is False, "automatic Canon promotion forbidden")
    _require(validation.get("automatic_runtime_promotion") is False, "automatic runtime promotion forbidden")

    _validate_iar_history(repo)
    _validate_plan_admission_and_d5(validation, repo)
    _validate_d6_d7_d8(validation, repo)

    _require(research.get("runtime_freeze_exceptions") == EXPECTED_FREEZE_EXCEPTIONS, "runtime freeze exception inventory drift")
    _require(research.get("canonical_promotion_requires") == EXPECTED_PROMOTION_REQUIREMENTS, "canonical promotion requirement inventory drift")

    issue = state.get("issues", {}).get("88")
    _require(isinstance(issue, Mapping), "Issue #88 snapshot required")
    _require(issue.get("state") == "OPEN", "Issue #88 must remain open for operator handoff")
    meaning = str(issue.get("meaning", ""))
    for marker in ("ADR-0026 Option D", "QUALIFYING_REVIEW_COMPLETE", EXPECTED_PLAN_ID, EXPECTED_D5_R1_MERGE_SHA, EXPECTED_D8_MERGE_SHA, "six hypotheses SUPPORTED_FOR_SCOPE", "six NOT_TESTED", "STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL", EXPECTED_CURRENT_NEXT_CONTENT_SLICE):
        _require(marker in meaning, f"Issue #88 current truth missing marker: {marker}")
    _require("does not authorize or decide" in meaning, "Issue #88 must preserve operator-decision boundary")
    _require("runtime remains frozen" in meaning.lower(), "Issue #88 must preserve runtime freeze")
    verification = issue.get("verification")
    _require(isinstance(verification, Mapping), "Issue #88 verification required")
    _require(verification.get("status") == "VERIFIED" and verification.get("method") == "GITHUB_API" and verification.get("source") == "issue/88", "Issue #88 verification drift")

    notion = state.get("notion")
    _require(isinstance(notion, Mapping), "Notion state required")
    _require(notion.get("synchronization_required") is False, "D8 Notion synchronization must be complete")
    _require(notion.get("status") == "SYNCED_THROUGH_DESCENDANT_CHECKPOINT", "Notion status drift")
    notion_scope = str(notion.get("scope", ""))
    for marker in ("10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c", "70acd0da61fee19131947aa56125833adb156ced", EXPECTED_D7_MERGE_SHA, "7/7 read-back verification", EXPECTED_D8_MERGE_SHA):
        _require(marker in notion_scope, f"Notion synchronization scope missing marker: {marker}")

    non_claims = " ".join(str(item).lower() for item in state.get("non_claims", []))
    for phrase in (
        "future-facing blueprint does not prove compatibility with arbitrary future substrates",
        "a1-a10 remain provisional after d7",
        "six a10 hypotheses remain not_tested",
        "does not establish independent implementation team, custody, or computation-model evidence",
        "do not authorize product runtime integration",
        "does not authorize or decide the separate operator_canon_runtime_decision_required gate",
    ):
        _require(phrase in non_claims, f"missing architecture boundary: {phrase}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("state", nargs="?", type=Path, default=Path("project-state.json"))
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    repo = args.repo.resolve()
    state_path = args.state if args.state.is_absolute() else repo / args.state
    try:
        validate(_load(state_path), repo=repo)
    except ArchitectureFreezeError as exc:
        print(f"Architecture validation boundary failed: {exc}", file=sys.stderr)
        return 1
    print("Architecture validation boundary passed; Option D D0-D8=COMPLETE; D6=6_SUPPORTED_FOR_SCOPE/6_NOT_TESTED; D7=STILL_PROVISIONAL; Notion=7/7_READ_BACK_VERIFIED; next=OPERATOR_CANON_RUNTIME_DECISION_REQUIRED; runtime_expansion_frozen=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
