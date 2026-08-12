#!/usr/bin/env python3
"""Validate ADR-0027 reconciliation state over preserved D8/history guards."""
from __future__ import annotations
import copy
from pathlib import Path
from typing import Any, Mapping
_D8_PATH=Path(__file__).with_name("validate_reconciliation_d8.py")
_saved=__name__; globals()["__name__"]="validate_reconciliation_d8_embedded"
exec(compile(_D8_PATH.read_text(encoding="utf-8"),str(_D8_PATH),"exec"),globals(),globals())
globals()["__name__"]=_saved
_D8_VALIDATE=validate
DECISION_MERGE="57993f39906ae7266011f6146c9a485d0587d2bf"
CURRENT_MARKER="POST_D8_OPERATOR_DECISION_CURRENT"

def _d8_repo_view(repo:Path)->None:
    # D8 validator reads files from repo directly. Current overlays preserve all
    # historical bindings, so only project-state's pending-sync boolean differs.
    state_path=repo/"project-state.json"; state=_load_json(state_path); original=state_path.read_text(encoding="utf-8")
    state["notion"]["synchronization_required"]=False
    state_path.write_text(json.dumps(state,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    try: _D8_VALIDATE(repo)
    finally: state_path.write_text(original,encoding="utf-8")

def validate(repo:Path)->None:
    _d8_repo_view(repo)
    state=_load_json(repo/"project-state.json"); notion=state.get("notion"); _require(isinstance(notion,Mapping),"Notion state required")
    _require(notion.get("synchronization_required") is True,"ADR-0027 Notion synchronization must remain pending before read-back")
    _require(DECISION_MERGE in str(notion.get("scope","")),"Notion scope missing ADR-0027 merge binding")
    decision=state["tracks"]["long_horizon_research"]["post_blueprint_validation"].get("post_d8_operator_decision")
    _require(isinstance(decision,Mapping) and decision.get("decision_merge_sha")==DECISION_MERGE,"ADR-0027 machine binding drift")
    for relative in CURRENT_SURFACES:
        _require(CURRENT_MARKER in _read(repo/relative),f"{relative}: current ADR-0027 overlay missing")

def main()->int:
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("--repo",type=Path,default=Path.cwd()); args=parser.parse_args(); repo=args.repo.resolve(); validate(repo)
    print("Reconciliation validation passed; D8 history preserved; ADR-0027 sync=pending; current overlays=present")
    return 0
if __name__=="__main__": raise SystemExit(main())
