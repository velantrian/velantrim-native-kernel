#!/usr/bin/env python3
"""Validate post-ADR-0027 project state before Notion read-back completion."""
from __future__ import annotations
import copy
from pathlib import Path
from typing import Any, Mapping
_D8_PATH=Path(__file__).with_name("validate_project_state_d8.py")
_saved=__name__; globals()["__name__"]="validate_project_state_d8_embedded"
exec(compile(_D8_PATH.read_text(encoding="utf-8"),str(_D8_PATH),"exec"),globals(),globals())
globals()["__name__"]=_saved
_D8_VALIDATE=validate
DECISION_MERGE="57993f39906ae7266011f6146c9a485d0587d2bf"

def _d8_view(state: Mapping[str,Any])->dict[str,Any]:
    value=copy.deepcopy(dict(state))
    notion=value["notion"]
    notion["synchronization_required"]=False
    notion["status"]="SYNCED_THROUGH_DESCENDANT_CHECKPOINT"
    notion["scope"]=(
        "Publication checkpoint " + PUBLICATION_SHA
        + ", manifest source " + MANIFEST_SOURCE_SHA
        + ", D8 Notion synchronization checkpoint " + D8_NOTION_SYNC_SHA
        + ", and D8 consolidated record merge " + D8_RECORD_MERGE_SHA
        + " remain distinct historical roles."
    )
    nonclaims=list(value.get("non_claims",[]))
    historical_boundary="D8 preserved the assertion arithmetic while synchronizing descendant truth surfaces."
    if historical_boundary not in nonclaims:
        nonclaims.append(historical_boundary)
    value["non_claims"]=nonclaims
    return value

def _validate_post_decision(state: Mapping[str,Any])->None:
    notion=state.get("notion"); _require(isinstance(notion,Mapping),"Notion synchronization state required")
    _require(notion.get("synchronization_required") is True,"operator-decision Notion synchronization must remain pending before read-back")
    _require(notion.get("status")=="SYNCED_THROUGH_DESCENDANT_CHECKPOINT","Notion status drift")
    _require(DECISION_MERGE in str(notion.get("scope","")),"Notion scope missing ADR-0027 pending-sync binding")
    research=state["tracks"]["long_horizon_research"]; validation=research["post_blueprint_validation"]
    decision=validation.get("post_d8_operator_decision"); _require(isinstance(decision,Mapping),"post-D8 operator decision required")
    _require(decision.get("decision_merge_sha")==DECISION_MERGE,"post-D8 decision merge drift")
    _require(decision.get("next_gate")=="RESIDUAL_A10_VALIDATION_PLAN","residual planning gate drift")
    _require(decision.get("next_gate_scope")=="RESEARCH_PLANNING_ONLY","residual planning scope drift")
    _require(decision.get("experiment_execution_authorized") is False,"residual experiment execution must remain unauthorized")
    _require(state["status"]["production_authorized"] is False,"production must remain unauthorized")

def validate(state: Mapping[str,Any],*,repo:Path,registry:Mapping[str,Any]|None=None,check_git:bool=True)->None:
    _D8_VALIDATE(_d8_view(state),repo=repo,registry=registry,check_git=check_git)
    _validate_post_decision(state)

def main()->int:
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("state",nargs="?",type=Path,default=Path("project-state.json")); parser.add_argument("--repo",type=Path,default=Path.cwd()); parser.add_argument("--no-git",action="store_true"); args=parser.parse_args()
    repo=args.repo.resolve(); state_path=args.state if args.state.is_absolute() else repo/args.state; state=_load(state_path,"project state"); validate(state,repo=repo,check_git=not args.no_git)
    print("Project-state validation passed; ADR-0027=ACCEPTED; notion_sync=pending; next=RESIDUAL_A10_VALIDATION_PLAN; runtime=FROZEN")
    return 0
if __name__=="__main__": raise SystemExit(main())
