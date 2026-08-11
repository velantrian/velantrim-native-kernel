#!/usr/bin/env python3
"""Fail closed on BPV1-001 execution-admission scope violations.

Two distinct, permanent checks:

1. Historical: the merged execution-admission candidate package itself
   (BASE..ADMISSION_MERGE) touched only its declared admission-only paths.
   This range is immutable git history and this check always passes once
   satisfied - it does not re-run against every future commit.
2. Ongoing: no commit, ever, touches product/runtime/subject paths that
   remain forbidden regardless of admission or status-sync activity. This
   check runs against the live BASE..HEAD diff and applies to every commit
   this workflow evaluates, including later status-sync checkpoints that
   legitimately touch docs/tests/tools/project-state.json outside the
   admission-only allowlist.
"""
from __future__ import annotations

import argparse
import fnmatch
import subprocess
from pathlib import Path

BASE = "20484a151bc7011509579353c2cf78845e3c33f9"
ADMISSION_MERGE = "6027eec73f11c4626be5553de7e79f827be2c81d"
ADMISSION_ALLOWED = (
    ".github/workflows/ai-context.yml",
    ".github/workflows/bpv1-admission.yml",
    "docs/research/BPV1_EXECUTION_ADMISSION.md",
    "docs/research/BPV1_EXECUTION_ADMISSION.ru.md",
    "docs/research/BPV1_EXECUTION_ADMISSION.json",
    "experiments/bpv1/BPV1-001/rust-toolchain.toml",
    "experiments/bpv1/BPV1-001/admission/**",
    "tools/bpv1/**",
    "tools/docs/bpv1-admission-bilingual-pair-v1.json",
    "tests/test_bpv1_execution_admission.py",
)
FORBIDDEN_PREFIXES = (
    "native_kernel/",
    "contracts/",
    "profiles/",
    "migrations/",
    "evidence/c5/",
)
# The BPV1-001 subject path is intentionally not in FORBIDDEN_PREFIXES.
# Unlike the product/runtime roots above, its prohibition was scoped to
# "before the separate execution-admission checkpoint", not forever. That
# checkpoint (PR #113) legitimately admitted subject implementation/
# execution; whether the subject may exist now is governed by the live
# bpv1_status check in validate_execution_admission.py, not by this
# permanent live-diff guard.


def _git(repo: Path, *args: str) -> str:
    result = subprocess.run(["git", "-C", str(repo), *args], check=False, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result.stdout


def _changed_paths(repo: Path, base: str, head: str) -> list[str]:
    return [line.strip() for line in _git(repo, "diff", "--name-only", f"{base}...{head}").splitlines() if line.strip()]


def audit(repo: Path, head: str = "HEAD") -> list[str]:
    findings: list[str] = []

    historical_changed = _changed_paths(repo, BASE, ADMISSION_MERGE)
    if not historical_changed:
        findings.append("historical admission-package diff is empty")
    for path in historical_changed:
        if not any(fnmatch.fnmatch(path, pattern) for pattern in ADMISSION_ALLOWED):
            findings.append(f"historical admission package touched a path outside its allowlist: {path}")

    live_changed = _changed_paths(repo, BASE, head)
    if not live_changed:
        findings.append("live diff since pre-admission base is empty")
    for path in live_changed:
        if any(path.startswith(prefix) for prefix in FORBIDDEN_PREFIXES):
            findings.append(f"forbidden product/subject path changed: {path}")

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--head", default="HEAD")
    args = parser.parse_args()
    try:
        findings = audit(args.repo.resolve(), args.head)
    except RuntimeError as exc:
        print(f"BPV1 admission scope audit ERROR: {exc}")
        return 2
    if findings:
        for finding in findings:
            print(f"ERROR {finding}")
        print(f"BPV1 admission scope audit FAILED ({len(findings)} finding(s))")
        return 1
    subject_state = "present" if (args.repo.resolve() / "experiments/bpv1/BPV1-001/subject").exists() else "absent"
    print(f"BPV1 admission scope audit PASS; base={BASE}; admission_merge={ADMISSION_MERGE}; subject={subject_state}; product_roots=unchanged")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
