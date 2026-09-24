#!/usr/bin/env python3
"""Fail closed on hidden Russian-document parity coverage drift."""
from __future__ import annotations
import json
from pathlib import Path

MANIFEST=Path("tools/docs/bilingual-coverage-v1.json")
PROTOCOL="nk-bilingual-coverage/1"

class CoverageError(RuntimeError): pass
def req(v,m):
    if not v: raise CoverageError(m)

def validate(repo:Path)->None:
    data=json.loads((repo/MANIFEST).read_text(encoding="utf-8"))
    req(data.get("protocol")==PROTOCOL,"protocol drift")
    boundary=data.get("authority_boundary") or {}
    for k in ("semantic_equivalence_certified","legal_equivalence_certified","canon_changed","runtime_changed"):
        req(boundary.get(k) is False,f"authority boundary must remain false: {k}")
    actual=sorted(p.relative_to(repo).as_posix() for p in repo.rglob("*.ru.md"))
    validated=data.get("validated") or []
    unvalidated=data.get("explicitly_unvalidated") or []
    vp=[x.get("path") for x in validated]
    up=[x.get("path") for x in unvalidated]
    req(len(vp)==len(set(vp)),"duplicate validated path")
    req(len(up)==len(set(up)),"duplicate unvalidated path")
    req(not(set(vp)&set(up)),"path appears in validated and unvalidated sets")
    req(sorted(vp+up)==actual,"Russian-document coverage inventory drift")
    counts=data.get("counts") or {}
    req(counts.get("russian_documents")==len(actual),"russian_documents count drift")
    req(counts.get("validated_by_config")==len(vp),"validated count drift")
    req(counts.get("explicitly_unvalidated")==len(up),"unvalidated count drift")
    for item in validated:
        cfg=repo/item["config"]
        req(cfg.is_file(),f"missing parity config: {item['config']}")
        cfgdata=json.loads(cfg.read_text(encoding="utf-8"))
        match=[p for p in cfgdata.get("pairs",[]) if p.get("pair_id")==item["pair_id"] and p.get("russian")==item["path"]]
        req(len(match)==1,f"configured coverage binding drift: {item['path']}")
    for item in unvalidated:
        req(isinstance(item.get("reason"),str) and item["reason"].strip(),f"reason required: {item.get('path')}")

if __name__=="__main__":
    try: validate(Path(".").resolve())
    except (CoverageError,json.JSONDecodeError) as exc: raise SystemExit(f"BILINGUAL_COVERAGE_INVALID: {exc}")
    print("BILINGUAL_COVERAGE_VALID (inventory only; translation equivalence not certified)")
