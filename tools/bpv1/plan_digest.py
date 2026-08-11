#!/usr/bin/env python3
"""Print the SHA-256 digest of the authoritative BPV-1 preregistration bytes."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

DEFAULT_PLAN = Path("docs/research/BPV1_PREREGISTRATION.json")


def digest_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--plan", type=Path, default=DEFAULT_PLAN)
    args = parser.parse_args()
    repo = args.repo.resolve()
    plan = args.plan if args.plan.is_absolute() else repo / args.plan
    print(digest_file(plan))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
