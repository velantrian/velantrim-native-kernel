from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from native_kernel.shadow_evaluation import ShadowEvaluationError, render_report, report_from_files  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 2:
        print("usage: offline_shadow_evaluator.py <shadow-workload.json> <c3-report.json>", file=sys.stderr)
        return 2
    try:
        report = report_from_files(Path(args[0]), Path(args[1]))
    except (OSError, ValueError, ShadowEvaluationError) as exc:
        print(f"C4 offline shadow evaluation failed: {exc}", file=sys.stderr)
        return 1
    print(render_report(report), end="")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
