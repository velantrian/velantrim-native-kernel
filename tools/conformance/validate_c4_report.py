from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from native_kernel.shadow_evaluation import ShadowEvaluationError, validate_report_file  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate an nk-shadow-report/1 C4 report")
    parser.add_argument("report", type=Path)
    parser.add_argument("--require-repository", action="store_true")
    args = parser.parse_args(argv)
    try:
        validate_report_file(args.report, require_repository=args.require_repository)
    except (OSError, ValueError, ShadowEvaluationError) as exc:
        print(f"C4 report validation failed: {exc}", file=sys.stderr)
        return 1
    print("C4 report validation PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
