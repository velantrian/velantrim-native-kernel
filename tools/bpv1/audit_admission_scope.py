#!/usr/bin/env python3
"""Fail closed if the BPV1-001 execution-admission package escapes its bounded paths."""
from __future__ import annotations

import argparse
import fnmatch
import subprocess
from pathlib import Path

BASE = "20484a151bc7011509579353c2cf78845e3c33f9"
ALLOWED = (
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
    "experiments/bpv1/BPV1-001/subject/",
)


def _git(repo: Path, *args: str) -> str:
    result = subprocess.run(["git", "-C", str(repo), *args], check=False, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result.stdout


def audit(repo: Path, head: str = "HEAD") -> list[str]:
    changed = [line.strip() for line in _git(repo, "diff", "--name-only", f"{BASE}...{head}").splitlines() if line.strip()]
    findings: list[str] = []
    if not changed:
        return ["admission diff is empty"]
    for path in changed:
        if any(path.startswith(prefix) for prefix in FORBIDDEN_PREFIXES):
            findings.append(f"forbidden product/subject path changed: {path}")
        if not any(fnmatch.fnmatch(path, pattern) for pattern in ALLOWED):
            findings.append(f"path outside execution-admission allowlist: {path}")
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
    print(f"BPV1 admission scope audit PASS; base={BASE}; subject=absent; product_roots=unchanged")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
