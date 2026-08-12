#!/usr/bin/env python3
"""Validate post-D8 current truth without weakening historical freeze guards.

The byte-preserved history layer contains the D5-R1-era validator and all of
its adversarial IAR/reconciliation/preregistration checks. This module executes
that layer in the current module namespace, validates a normalized historical
view, then independently validates the authoritative D6/D7/D8 live state.
"""
from __future__ import annotations

import copy
import sys
from pathlib import Path
from typing import Any, Mapping

_HISTORY_PATH = Path(__file__).with_name("validate_architecture_freeze_history.py")
_saved_name = __name__
globals()["__name__"] = "validate_architecture_freeze_history_embedded"
exec(compile(_HISTORY_PATH.read_text(encoding="utf-8"), str(_HISTORY_PATH), "exec"), globals(), globals())
globals()["__name__"] = _saved_name

_HISTORICAL_VALIDATE = validate

CURRENT_NEXT_GATE = "OPERATOR_CANON_RUNTIME_DECISION_REQUIRED"
CURRENT_RESEARCH_STATUS = "ACTIVE / OPTION D VALIDATION COMPLETE / OPERATOR DECISION REQUIRED / NO AUTOMATIC PROMOTION"
CURRENT_REFOUNDATION_STATUS = "BLUEPRINT COMPLETE / PROVISIONAL / OPTION D VALIDATION COMPLETE"
CURRENT_VALIDATION_STATUS = "COMPLETE / OPTION_D_VALIDATION_AND_SYNC_COMPLETE / AWAITING_SEPARATE_OPERATOR_DECISION"
CURRENT_EXTRA_VALIDATION_FIELDS = {
    "d6_hypothesis_classification",
    "d7_integrated_rereview",
    "d8_consolidated_sync",
}
D6_SUPPORTED = ["A10-H01", "A10-H02", "A10-H04", "A10-H05", "A10-H07", "A10-H12"]
D6_NOT_TESTED = ["A10-H03", "A10-H06", "A10-H08", "A10-H09", "A10-H10", "A10-H11"]
D6_MERGE_SHA = "030d0a0585bd061b27329a38e29708c11304701a"
D7_MERGE_SHA = "491ff7b229606d228ca04985b19b146878390e08"
D8_MERGE_SHA = "9ecb2369edec17a0171b6e965bcb49f9526adf0b"
D8_NOTION_SHA = D7_MERGE_SHA

_HISTORICAL_NONCLAIMS = (
    "Architecture Re-foundation documentation is not runtime implementation evidence.",
    "A future-facing blueprint does not prove compatibility with arbitrary future substrates.",
    "Integrated A1-A10 review completion is not independent validation, operator acceptance, Canon promotion, runtime authorization, arbitrary-substrate proof, or production authorization.",
    "ADR-0026 operator approval authorizes a validation phase, not Final Canon, runtime thaw, arbitrary-substrate proof, or production authorization.",
    "IAR-1 qualifying review completion and IAR-1-R1 reconciliation do not prove the architecture universally correct.",
    "BPV-1 execution admission authorizes only BPV1-001 subject implementation and execution; it does not authorize product runtime integration, reducer v2, new Event verbs, NK-EPI runtime, Final Canon, production, Track H admission, or a license decision.",
    "BPV1-001 SUPPORTED_FOR_SCOPE is scoped falsification evidence only; it is not universal substrate-independence proof.",
    "D5-R1 external qualification removes the identified HR10 subject-self-report adjudication path but does not establish independent implementation team, custody, or computation-model evidence.",
    "D6 A10 hypothesis classification is not yet performed; SUPPORTED_FOR_SCOPE must not be silently generalized into classifications that have not been adjudicated.",
    "Product runtime thaw remains unauthorized.",
)


def _historical_view(state: Mapping[str, Any]) -> dict[str, Any]:
    historical = copy.deepcopy(dict(state))
    research = historical["tracks"]["long_horizon_research"]
    research["status"] = "ACTIVE / POST-BLUEPRINT VALIDATION / NO AUTOMATIC PROMOTION"
    refoundation = research["architecture_refoundation"]
    refoundation["status"] = "BLUEPRINT COMPLETE / PROVISIONAL / VALIDATION ACTIVE"
    refoundation["next_content_slice"] = "D6_A10_HYPOTHESIS_CLASSIFICATION"

    validation = research["post_blueprint_validation"]
    validation["status"] = (
        "AUTHORIZED / REVIEW_COMPLETE / RECONCILIATION_COMPLETE / "
        "BPV1_PLAN_PREREGISTERED / EXECUTION_ADMITTED_FOR_EXPERIMENT_ONLY / "
        "D5_COMPLETE / D5_R1_QUALIFIED"
    )
    for field in CURRENT_EXTRA_VALIDATION_FIELDS:
        validation.pop(field, None)
    result = validation["bpv1_execution_result"]
    result["next_gate"] = "D6_A10_HYPOTHESIS_CLASSIFICATION"
    result["d6_status"] = "NOT_STARTED"
    result.pop("d7_status", None)
    result.pop("d8_status", None)

    historical["issues"]["88"]["meaning"] = (
        "Architecture Re-foundation A1-A10 and integrated review remain provisional; "
        "ADR-0026 Option D is active; IAR-1 is QUALIFYING_REVIEW_COMPLETE and "
        "IAR-1-R1 reconciliation resolves all blocking/material findings; frozen plan "
        f"{EXPECTED_PLAN_ID} remains bound to plan merge {EXPECTED_PLAN_MERGE_SHA}; "
        f"D5 execution merged at {EXPECTED_D5_MERGE_SHA}; D5-R1 qualification merged "
        f"at {EXPECTED_D5_R1_MERGE_SHA} with outcome {EXPECTED_D5_R1_OUTCOME}; "
        "D6 A10 hypothesis classification is next and NOT_STARTED; runtime remains frozen."
    )
    historical["non_claims"] = list(historical.get("non_claims", [])) + list(_HISTORICAL_NONCLAIMS)
    return historical


def _validate_current_option_d_state(state: Mapping[str, Any]) -> None:
    tracks = state.get("tracks")
    _require(isinstance(tracks, Mapping), "tracks object required")
    research = tracks.get("long_horizon_research")
    _require(isinstance(research, Mapping), "long-horizon research track required")
    _require(research.get("status") == CURRENT_RESEARCH_STATUS, "post-D8 research status drift")
    _require(research.get("runtime_authorized") is False, "research track must not authorize runtime")

    refoundation = research.get("architecture_refoundation")
    _require(isinstance(refoundation, Mapping), "architecture_refoundation required")
    _require(refoundation.get("status") == CURRENT_REFOUNDATION_STATUS, "post-D8 architecture status drift")
    _require(refoundation.get("next_content_slice") == CURRENT_NEXT_GATE, "next architecture validation gate drift")
    _require(refoundation.get("runtime_expansion_frozen") is True, "runtime expansion freeze must remain enabled")
    _require(refoundation.get("completed_deliverables") == EXPECTED_COMPLETED_DELIVERABLES, "completed blueprint deliverable inventory drift")

    validation = research.get("post_blueprint_validation")
    _require(isinstance(validation, Mapping), "post_blueprint_validation required")
    _require(set(validation) == EXPECTED_POST_BLUEPRINT_FIELDS | CURRENT_EXTRA_VALIDATION_FIELDS, "post-blueprint validation field inventory drift")
    _require(validation.get("selected_option") == "D_INDEPENDENT_CHALLENGE_THEN_BOUNDED_CROSS_LINEAGE_FALSIFICATION", "post-blueprint Option D selection drift")
    _require(validation.get("status") == CURRENT_VALIDATION_STATUS, "post-blueprint validation phase drift")
    _require(validation.get("independent_review_status") == "QUALIFYING_REVIEW_COMPLETE", "independent review completion drift")
    _require(validation.get("bpv1_status") == EXPECTED_CURRENT_BPV1_STATUS, "BPV-1 execution authorization must remain experiment-only")
    _require(validation.get("product_runtime_thaw") is False, "Option D must not thaw product runtime")
    _require(validation.get("automatic_canon_promotion") is False, "automatic Canon promotion forbidden")
    _require(validation.get("automatic_runtime_promotion") is False, "automatic runtime promotion forbidden")

    result = validation.get("bpv1_execution_result")
    _require(isinstance(result, Mapping), "BPV-1 execution result record required")
    _require(result.get("status") == "COMPLETE", "BPV-1 D5 result must remain complete")
    _require(result.get("qualification_status") == "QUALIFIED", "BPV-1 D5-R1 must remain qualified")
    _require(result.get("oracle_outcome") == EXPECTED_D5_R1_OUTCOME, "BPV-1 qualified oracle outcome drift")
    _require(result.get("qualification_merge_sha") == EXPECTED_D5_R1_MERGE_SHA, "BPV-1 D5-R1 merge drift")
    _require(result.get("hr10_self_report_path") == "REMOVED_BY_EXTERNAL_QUALIFICATION", "BPV-1 HR10 qualification drift")
    _require(result.get("next_gate") == CURRENT_NEXT_GATE, "BPV-1 post-D8 next gate drift")
    _require(result.get("d6_status") == "COMPLETE", "D6 completion drift")
    _require(result.get("d7_status") == "COMPLETE", "D7 completion drift")
    _require(result.get("d8_status") == "COMPLETE / READ_BACK_VERIFIED", "D8 completion drift")

    d6 = validation.get("d6_hypothesis_classification")
    _require(isinstance(d6, Mapping), "D6 classification record required")
    _require(d6.get("protocol") == "nk-a10-hypothesis-classification/1", "D6 classification protocol drift")
    _require(d6.get("status") == "COMPLETE", "D6 classification completion drift")
    _require(d6.get("pr") == 117 and d6.get("merge_sha") == D6_MERGE_SHA, "D6 classification merge binding drift")
    _require(d6.get("supported_for_scope") == D6_SUPPORTED, "D6 supported-for-scope inventory drift")
    _require(d6.get("not_tested") == D6_NOT_TESTED, "D6 not-tested inventory drift")
    _require(d6.get("weakened") == [] and d6.get("refuted") == [] and d6.get("indeterminate") == [], "D6 non-primary outcome drift")
    _require(d6.get("next_gate") == "D7_INTEGRATED_RE_REVIEW", "D6 next-gate history drift")

    d7 = validation.get("d7_integrated_rereview")
    _require(isinstance(d7, Mapping), "D7 integrated re-review record required")
    _require(d7.get("protocol") == "nk-integrated-post-bpv1-rereview/1", "D7 protocol drift")
    _require(d7.get("status") == "COMPLETE", "D7 completion drift")
    _require(d7.get("pr") == 118 and d7.get("merge_sha") == D7_MERGE_SHA, "D7 merge binding drift")
    _require(d7.get("review_outcome") == "PROVISIONAL_VALIDATION_REVIEW_COMPLETE", "D7 review outcome drift")
    _require(d7.get("architecture_position") == "STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL", "D7 architecture position drift")
    _require(d7.get("next_gate") == "D8_CONSOLIDATED_AUTHORITATIVE_SYNC", "D7 next-gate history drift")

    d8 = validation.get("d8_consolidated_sync")
    _require(isinstance(d8, Mapping), "D8 synchronization record required")
    _require(d8.get("protocol") == "nk-option-d-consolidated-sync/1", "D8 protocol drift")
    _require(d8.get("status") == "COMPLETE / READ_BACK_VERIFIED", "D8 synchronization completion drift")
    _require(d8.get("pr") == 119 and d8.get("merge_sha") == D8_MERGE_SHA, "D8 merge binding drift")
    _require(d8.get("source_checkpoint_sha") == D8_NOTION_SHA, "D8 source checkpoint drift")
    _require(d8.get("notion_surface_count") == 7 and d8.get("notion_read_back_verified_count") == 7, "D8 Notion 7/7 read-back drift")
    _require(d8.get("new_notion_pages_created") == 0, "D8 must not create Notion pages")
    _require(d8.get("next_gate") == CURRENT_NEXT_GATE, "D8 next gate drift")
    _require(d8.get("next_gate_authorized_by_d8") is False, "D8 cannot authorize the operator gate outcome")
    _require(d8.get("operator_decision_required") is True, "D8 must require a separate operator decision")

    issue = state.get("issues", {}).get("88")
    _require(isinstance(issue, Mapping), "Issue #88 snapshot required")
    _require(issue.get("state") == "OPEN", "Issue #88 must remain open through validation")
    meaning = str(issue.get("meaning", ""))
    _require("ADR-0026 Option D" in meaning, "Issue #88 must record Option D selection")
    for marker in (
        "IAR-1 is QUALIFYING_REVIEW_COMPLETE",
        "IAR-1-R1 reconciliation is COMPLETE",
        EXPECTED_PLAN_ID,
        EXPECTED_PLAN_MERGE_SHA,
        "D5/D5-R1 are complete",
        "six hypotheses SUPPORTED_FOR_SCOPE and six NOT_TESTED",
        "STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL",
        "7/7 read-back verification",
        CURRENT_NEXT_GATE,
        "Runtime remains frozen",
    ):
        _require(marker in meaning, f"Issue #88 current truth missing marker: {marker}")
    verification = issue.get("verification")
    _require(isinstance(verification, Mapping), "Issue #88 verification required")
    _require(verification.get("status") == "VERIFIED" and verification.get("method") == "GITHUB_API" and verification.get("source") == "issue/88", "Issue #88 verification drift")

    checkpoints = state.get("checkpoints")
    _require(isinstance(checkpoints, Mapping), "checkpoint inventory required")
    _require(checkpoints.get("notion_synchronized_through_sha") == D8_NOTION_SHA, "D8 Notion synchronization checkpoint drift")
    notion = state.get("notion")
    _require(isinstance(notion, Mapping), "Notion state required")
    _require(notion.get("synchronization_required") is False, "D8 Notion synchronization must be complete")
    _require(notion.get("status") == "SYNCED_THROUGH_DESCENDANT_CHECKPOINT", "Notion status drift")

    current_nonclaims = " ".join(str(item).lower() for item in state.get("non_claims", []))
    for phrase in (
        "six a10 hypotheses remain not_tested",
        "do not establish universal substrate independence",
        "does not authorize product runtime integration",
        "does not authorize or decide the separate operator_canon_runtime_decision_required gate",
    ):
        _require(phrase in current_nonclaims, f"missing post-D8 architecture boundary: {phrase}")


def validate(state: Mapping[str, Any], *, repo: Path) -> None:
    _validate_snapshot_chronology(state)
    _HISTORICAL_VALIDATE(_historical_view(state), repo=repo)
    _validate_current_option_d_state(state)


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
    print(
        "Architecture validation boundary passed; historical=preserved; "
        "D6=COMPLETE; D7=COMPLETE/STILL_PROVISIONAL; "
        "D8=COMPLETE/READ_BACK_VERIFIED; next=OPERATOR_CANON_RUNTIME_DECISION_REQUIRED; "
        "runtime_expansion_frozen=true"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
