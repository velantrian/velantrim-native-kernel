#!/usr/bin/env python3
"""Fail closed when BPV1 admission or subject work escapes its declared repository boundary."""
from __future__ import annotations

import argparse
import fnmatch
import subprocess
from pathlib import Path

ADMISSION_ALLOWED = (
    ".github/workflows/ai-context.yml",
    "docs/research/BPV1_EXECUTION_ADMISSION.md",
    "docs/research/BPV1_EXECUTION_ADMISSION.ru.md",
    "docs/research/BPV1_EXECUTION_ADMISSION.json",
    "experiments/bpv1/BPV1-001/rust-toolchain.toml",
    "experiments/bpv1/BPV1-001/admission/**",
    "tools/bpv1/**",
    "tools/docs/bpv1-admission-bilingual-pair-v1.json",
    "tests/test_bpv1_execution_admission.py",
)

SUBJECT_ALLOWED = (
    "experiments/bpv1/BPV1-001/subject/**",
    "experiments/bpv1/BPV1-001/results/**",
    "tests/test_bpv1_subject.py",
    ".github/workflows/bpv1.yml",
)

FORBIDDEN_PRODUCT_ROOTS = (
    "native_kernel/",
    "contracts/",
    "profiles/",
    "migrations/",
    "evidence/c5/",
)


class ScopeError(RuntimeError):
    pass


def _git(repo: Path, *args: str) -> str:
    result = subprocess.run(["git", "-C", str(repo), *args], check=False, capture_output=True, text=True)
    if result.returncode != 0:
        raise ScopeError(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result.stdout


def _matches(path: str, patterns: tuple[str, ...]) -> bool:
    return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)


def audit(repo: Path, *, mode: str, base: str, head: str) -> list[str]:
    allowed = ADMISSION_ALLOWED if mode == "admission" else SUBJECT_ALLOWED
    changed = [line.strip() for line in _git(repo, "diff", "--name-only", f"{base}...{head}").splitlines() if line.strip()]
    findings: list[str] = []
    if not changed:
        findings.append("no changed files found for declared BPV1 scope")
        return findings
    for path in changed:
        if any(path.startswith(root) for root in FORBIDDEN_PRODUCT_ROOTS):
            findings.append(f"forbidden product/reference-laboratory root changed: {path}")
        if not _matches(path, allowed):
            findings.append(f"path outside {mode} allowlist: {path}")
    if mode == "admission" and any(path.startswith("experiments/bpv1/BPV1-001/subject/") for path in changed):
        findings.append("subject implementation is forbidden in execution-admission package")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--mode", choices=("admission", "subject"), required=True)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", default="HEAD")
    args = parser.parse_args()
    try:
        findings = audit(args.repo.resolve(), mode=args.mode, base=args.base, head=args.head)
    except ScopeError as exc:
        print(f"BPV1 scope audit ERROR: {exc}")
        return 2
    if findings:
        for finding in findings:
            print(f"ERROR {finding}")
        print(f"BPV1 {args.mode} scope audit FAILED ({len(findings)} finding(s))")
        return 1
    print(f"BPV1 {args.mode} scope audit PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
