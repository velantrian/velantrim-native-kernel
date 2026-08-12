#!/usr/bin/env python3
"""Validate ADR-0027 current truth before completed Notion read-back."""
from __future__ import annotations
import copy
import sys
from pathlib import Path
from typing import Any, Mapping

_D8_PATH = Path(__file__).with_name("validate_architecture_freeze_d8.py")
_saved_name = __name__
globals()["__name__"] = "validate_architecture_freeze_d8_embedded"
exec(compile(_D8_PATH.read_text(encoding="utf-8"), str(_D8_PATH), "exec"), globals(), globals())
globals()["__name__"] = _saved_name
_D8_VALIDATE = validate

POST_DECISION_GATE = "RESIDUAL_A10_VALIDATION_PLAN"
POST_DECISION_MERGE = "57993f39906ae7266011f6146c9a485d0587d2bf"
POST_DECISION_STATUS = "COMPLETE / OPTION_D_OPERATOR_DECISION_ACCEPTED / RESIDUAL_VALIDATION_PLANNING_AUTHORIZED"
POST_RESEARCH_STATUS = "ACTIVE / POST-D8 RESIDUAL VALIDATION PLANNING / NO AUTOMATIC PROMOTION"
POST_REFOUNDATION_STATUS = "BLUEPRINT COMPLETE / PROVISIONAL / RESIDUAL VALIDATION PLANNING AUTHORIZED"
RESIDUAL = ["A10-H03", "A10-H06", "A10-H08", "A10-H09", "A10-H10", "A10-H11"]
D8_NONCLAIMS = [
    "Six A10 hypotheses remain NOT_TESTED.",
    "D6/D7/D8 do not establish universal substrate independence.",
    "D6/D7/D8 do not authorize product runtime integration.",
    "D8 does not authorize or decide the separate OPERATOR_CANON_RUNTIME_DECISION_REQUIRED gate.",
]


def _d8_view(state: Mapping[str, Any]) -> dict[str, Any]:
    value = copy.deepcopy(dict(state))
    value["checkpoints"]["notion_synchronized_through_sha"] = D8_NOTION_SHA
    research = value["tracks"]["long_horizon_research"]
    research["status"] = CURRENT_RESEARCH_STATUS
    ref = research["architecture_refoundation"]
    ref["status"] = CURRENT_REFOUNDATION_STATUS
    ref["next_content_slice"] = CURRENT_NEXT_GATE
    validation = research["post_blueprint_validation"]
    validation["status"] = CURRENT_VALIDATION_STATUS
    validation.pop("post_d8_operator_decision", None)
    validation["bpv1_execution_result"]["next_gate"] = CURRENT_NEXT_GATE
    value["notion"]["synchronization_required"] = False
    value["issues"]["88"]["meaning"] = (
        "Architecture Re-foundation A1-A10 and integrated review remain provisional; ADR-0026 Option D is active; "
        "IAR-1 is QUALIFYING_REVIEW_COMPLETE and IAR-1-R1 reconciliation is COMPLETE; "
        f"{EXPECTED_PLAN_ID} remains bound to {EXPECTED_PLAN_MERGE_SHA}; D5/D5-R1 are complete at "
        f"{EXPECTED_D5_MERGE_SHA} / {EXPECTED_D5_R1_MERGE_SHA}; six hypotheses SUPPORTED_FOR_SCOPE and six NOT_TESTED; "
        "D7 is STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL; D8 completed with 7/7 read-back verification; "
        "OPERATOR_CANON_RUNTIME_DECISION_REQUIRED is next. Runtime remains frozen."
    )
    nonclaims = list(value.get("non_claims", []))
    for item in D8_NONCLAIMS:
        if item not in nonclaims:
            nonclaims.append(item)
    value["non_claims"] = nonclaims
    return value


def _validate_post_decision(state: Mapping[str, Any]) -> None:
    research = state["tracks"]["long_horizon_research"]
    _require(research.get("status") == POST_RESEARCH_STATUS, "post-ADR-0027 research status drift")
    ref = research["architecture_refoundation"]
    _require(ref.get("status") == POST_REFOUNDATION_STATUS, "post-ADR-0027 architecture status drift")
    _require(
        ref.get("next_content_slice") == POST_DECISION_GATE,
        "next architecture validation gate drift; post-ADR-0027 next gate drift",
    )
    _require(ref.get("runtime_expansion_frozen") is True, "ADR-0027 must preserve runtime freeze")
    validation = research["post_blueprint_validation"]
    _require(validation.get("status") == POST_DECISION_STATUS, "post-ADR-0027 validation status drift")
    _require(validation.get("product_runtime_thaw") is False, "ADR-0027 cannot thaw product runtime")
    _require(validation.get("automatic_canon_promotion") is False, "ADR-0027 cannot auto-promote Canon")
    _require(validation.get("automatic_runtime_promotion") is False, "ADR-0027 cannot auto-promote runtime")
    result = validation["bpv1_execution_result"]
    _require(result.get("next_gate") == POST_DECISION_GATE, "BPV1 result post-decision gate drift")
    decision = validation.get("post_d8_operator_decision")
    _require(isinstance(decision, Mapping), "post-D8 operator decision record required")
    _require(decision.get("protocol") == "nk-post-d8-operator-decision/1", "post-D8 decision protocol drift")
    _require(decision.get("decision_id") == "OD-POST-D8-001", "post-D8 decision identity drift")
    _require(decision.get("decision_status") == "ACCEPTED" and decision.get("operator_approval") == "APPROVED", "post-D8 decision approval drift")
    _require(decision.get("decision_merge_sha") == POST_DECISION_MERGE, "post-D8 decision merge binding drift")
    _require(decision.get("final_canon") == "DEFERRED / NOT_AUTHORIZED_AT_THIS_CHECKPOINT", "Final Canon overclaim")
    _require(decision.get("architecture_position") == "STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL", "architecture position drift")
    _require(decision.get("runtime_expansion") == "FROZEN" and decision.get("product_runtime_thaw") is False, "runtime-thaw overclaim")
    _require(decision.get("production_authorized") is False, "production overclaim")
    _require(decision.get("next_gate") == POST_DECISION_GATE and decision.get("next_gate_scope") == "RESEARCH_PLANNING_ONLY", "residual planning gate drift")
    _require(decision.get("experiment_execution_authorized") is False, "residual experiment execution must remain unauthorized")
    _require(decision.get("residual_validation_targets") == RESIDUAL, "residual A10 target inventory drift")
    _require(state["status"]["production_authorized"] is False, "production must remain unauthorized")
    _require(state["notion"]["synchronization_required"] is True, "operator-decision Notion sync must remain pending before read-back")

    issue = state.get("issues", {}).get("88")
    _require(isinstance(issue, Mapping), "Issue #88 snapshot required")
    _require(issue.get("state") == "OPEN", "Issue #88 must remain open through validation")
    meaning = str(issue.get("meaning", ""))
    _require(
        "ADR-0027 / OD-POST-D8-001" in meaning and POST_DECISION_MERGE in meaning,
        "Option D selection / post-D8 operator decision binding drift",
    )
    _require(POST_DECISION_GATE in meaning, "Issue #88 current gate drift")
    _require("Final Canon is deferred" in meaning, "Issue #88 Final Canon boundary drift")
    _require("runtime remains frozen" in meaning.lower(), "Issue #88 runtime freeze drift")
    _require("experiment execution is not authorized" in meaning, "Issue #88 experiment-execution boundary drift")
    verification = issue.get("verification")
    _require(isinstance(verification, Mapping), "Issue #88 verification required")
    _require(
        verification.get("status") == "VERIFIED"
        and verification.get("method") == "GITHUB_API"
        and verification.get("source") == "issue/88",
        "Issue #88 verification drift",
    )


def validate(state: Mapping[str, Any], *, repo: Path) -> None:
    _D8_VALIDATE(_d8_view(state), repo=repo)
    _validate_post_decision(state)


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
    print("Architecture validation passed; history=D8 preserved; ADR-0027=ACCEPTED; notion_sync=pending; next=RESIDUAL_A10_VALIDATION_PLAN; execution_authorized=false; runtime_expansion_frozen=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
