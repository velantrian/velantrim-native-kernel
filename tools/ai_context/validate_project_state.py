#!/usr/bin/env python3
"""Validate machine-readable Native Kernel project truth."""
from __future__ import annotations
import argparse, json, re, subprocess
from pathlib import Path
from typing import Any, Mapping

SHA = re.compile(r"^[0-9a-f]{40}$")
REL = {"EXACT", "DESCENDANT_OR_EQUAL", "UNRELATED", "UNKNOWN"}
COUNTS = {"supported":45,"partial":10,"unsupported":17,"failed":0,"total":72}

class ProjectStateError(RuntimeError): pass

def req(ok: bool, msg: str) -> None:
    if not ok: raise ProjectStateError(msg)

def load(path: Path, label: str) -> dict[str, Any]:
    try: value=json.loads(path.read_text(encoding="utf-8"))
    except (OSError,json.JSONDecodeError) as exc: raise ProjectStateError(f"cannot read {label}: {exc}") from exc
    req(isinstance(value,dict),f"{label} must be an object")
    return value

def git(repo: Path,*args: str):
    return subprocess.run(["git","-C",str(repo),*args],check=False,capture_output=True,text=True)

def validate_registry(reg: Mapping[str,Any], state: Mapping[str,Any]) -> None:
    req("runtime_status" not in reg,"legacy registry runtime_status is forbidden")
    req(reg.get("implementation_support")=="PARTIAL","registry support must remain PARTIAL")
    summary=reg.get("runtime_summary")
    req(isinstance(summary,Mapping),"registry runtime summary required")
    status=state["status"]
    for key in ("clean_runtime_support","kernel_runtime_conformance","operational_validation","production_authorized"):
        req(summary.get(key)==status.get(key),f"registry/state mismatch: {key}")
    req(reg.get("assertion_evidence_summary")==state["assertion_map"],"registry assertion summary drift")
    families=reg.get("families")
    req(isinstance(families,list),"registry families required")
    index={item.get("family_id"):item for item in families if isinstance(item,Mapping)}
    req(set(index)=={"NK-SEM","NK-ID","NK-EVT","NK-AUT","NK-CFL","NK-EQV","NK-EPI"},"registry family inventory drift")
    for family_id,family in index.items():
        if family_id=="NK-EPI":
            req(family.get("decision_status")=="PROPOSED","NK-EPI must remain proposed")
            req((family.get("implementation_support"),family.get("fixture_support"),family.get("evidence_level"))==("NOT_IMPLEMENTED","NOT_IMPLEMENTED","NONE"),"NK-EPI support overclaim")
        else:
            req(family.get("decision_status")=="ACCEPTED",f"{family_id}: decision drift")
            req((family.get("implementation_support"),family.get("fixture_support"),family.get("evidence_level"))==("PARTIAL","PARTIAL","C4_PARTIAL"),f"{family_id}: support drift")

def validate(state: Mapping[str,Any],*,repo: Path,registry: Mapping[str,Any]|None=None,check_git: bool=True)->None:
    req(state.get("protocol")=="nk-project-state/2","unsupported project-state protocol")
    repository=state.get("repository")
    req(isinstance(repository,Mapping),"repository object required")
    req((repository.get("full_name"),repository.get("visibility"),repository.get("default_branch"))==("velantrian/velantrim-native-kernel","PUBLIC","main"),"repository identity drift")

    cp=state.get("checkpoints")
    req(isinstance(cp,Mapping),"checkpoint inventory required")
    fields=("manifest_generated_from_sha","runtime_checkpoint_sha","runtime_integrity_checkpoint_sha","evidence_producing_sha","publication_checkpoint_sha","notion_synchronized_through_sha")
    for field in fields: req(isinstance(cp.get(field),str) and SHA.fullmatch(cp[field]) is not None,f"invalid checkpoint: {field}")
    req(cp.get("expected_head_relationship") in REL,"invalid expected head relationship")
    req(cp["publication_checkpoint_sha"]==cp["notion_synchronized_through_sha"],"Notion/publication checkpoint mismatch")

    status=state.get("status")
    req(isinstance(status,Mapping),"status object required")
    req(status.get("repository_status")=="RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY","repository status drift")
    req(status.get("support_state")==status.get("clean_runtime_support")=="PARTIAL","runtime support drift")
    req((status.get("kernel_runtime_conformance"),status.get("operational_validation"),status.get("production_authorized"))==("C4","C5_BOUNDED_REHEARSAL",False),"maturity or production drift")

    tracks=state.get("tracks")
    req(isinstance(tracks,Mapping) and set(tracks)=={"historical_recovery","clean_implementation","long_horizon_research"},"exact H/C/R tracks required")
    req(tracks["historical_recovery"].get("blocks_clean_implementation") is False,"historical recovery must not block clean lineage")
    req(tracks["historical_recovery"].get("may_claim_globally_lost") is False,"global-loss overclaim")
    req(tracks["clean_implementation"].get("status")=="ACTIVE / PARTIAL","clean track drift")
    req(tracks["long_horizon_research"].get("runtime_authorized") is False,"research cannot authorize runtime")

    req(state.get("assertion_map")==COUNTS,"assertion map drift")
    epi=state.get("nk_epi")
    req(isinstance(epi,Mapping),"NK-EPI object required")
    req((epi.get("supported"),epi.get("partial"),epi.get("unsupported"),epi.get("failed"))==(0,0,8,0),"NK-EPI map drift")
    req(epi.get("implementation_support")=="NOT_IMPLEMENTED" and epi.get("promotion_authorized") is False,"NK-EPI promotion overclaim")
    req(state.get("issues",{}).get("1",{}).get("state")=="OPEN","Issue #1 state drift")
    req((state.get("issues",{}).get("64",{}).get("state"),state.get("issues",{}).get("64",{}).get("state_reason"))==("CLOSED","COMPLETED"),"Issue #64 state drift")
    req(state.get("notion",{}).get("status") in {"HANDOFF_REQUIRED","SYNCED_THROUGH_PUBLICATION_CHECKPOINT"},"invalid Notion status")

    validate_registry(registry or load(repo/"contracts/registry.json","contract registry"),state)

    if check_git and (repo/".git").exists():
        head=git(repo,"rev-parse","HEAD").stdout.strip(); source=cp["manifest_generated_from_sha"]; relation=cp["expected_head_relationship"]
        for field in fields: req(git(repo,"cat-file","-e",f"{cp[field]}^{{commit}}").returncode==0,f"{field} commit missing")
        if relation=="EXACT": req(source==head,"manifest source must equal HEAD")
        elif relation=="DESCENDANT_OR_EQUAL": req(git(repo,"merge-base","--is-ancestor",source,head).returncode==0,"manifest source not ancestor of HEAD")
        elif relation=="UNRELATED": req(git(repo,"merge-base","--is-ancestor",source,head).returncode!=0,"manifest source unexpectedly related")
        for field in fields[1:]: req(git(repo,"merge-base","--is-ancestor",cp[field],head).returncode==0,f"{field} not ancestor of HEAD")

def main()->int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("state",nargs="?",type=Path,default=Path("project-state.json")); p.add_argument("--repo",type=Path,default=Path.cwd()); p.add_argument("--no-git",action="store_true"); a=p.parse_args()
    repo=a.repo.resolve(); path=a.state if a.state.is_absolute() else repo/a.state; state=load(path,"project state"); validate(state,repo=repo,check_git=not a.no_git)
    cp=state["checkpoints"]; m=state["assertion_map"]
    print(f"Project-state validation passed; source={cp['manifest_generated_from_sha']}; relationship={cp['expected_head_relationship']}; runtime={state['status']['kernel_runtime_conformance']}; operational={state['status']['operational_validation']}; assertions={m['supported']}/{m['partial']}/{m['unsupported']}/{m['failed']}")
    return 0
if __name__=="__main__": raise SystemExit(main())
