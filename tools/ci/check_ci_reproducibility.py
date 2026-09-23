#!/usr/bin/env python3
"""Fail-closed static guard for reproducible GitHub Actions inputs.

Bounded claim: this checks workflow text only. It does not prove runner image,
container image, package-index, or network reproducibility.
"""
from __future__ import annotations

import re
from pathlib import Path

WORKFLOWS = Path(".github/workflows")
FULL_SHA_USE = re.compile(r"^\s*uses:\s*[^#\s]+@[0-9a-f]{40}(?:\s+#.*)?$", re.MULTILINE)
USE_LINE = re.compile(r"^\s*uses:\s*([^#\s]+)@([^\s#]+)", re.MULTILINE)
FORBIDDEN = (
    "runs-on: ubuntu-latest",
    "python -m pip install --upgrade pip",
)


def validate(repo: Path) -> list[str]:
    gaps: list[str] = []
    root = repo / WORKFLOWS
    for path in sorted((*root.glob("*.yml"), *root.glob("*.yaml"))):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(repo).as_posix()
        for match in USE_LINE.finditer(text):
            line = match.group(0)
            if FULL_SHA_USE.fullmatch(line) is None:
                gaps.append(f"{rel}: mutable/non-SHA action reference: {line.strip()}")
        for token in FORBIDDEN:
            if token in text:
                gaps.append(f"{rel}: forbidden reproducibility token: {token}")
    return gaps


def main() -> int:
    gaps = validate(Path(".").resolve())
    if gaps:
        print("CI_REPRODUCIBILITY_INVALID")
        for gap in gaps:
            print(f"  {gap}")
        return 1
    print("CI_REPRODUCIBILITY_VALID (bounded static workflow check; environment identity not proven)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
