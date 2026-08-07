from __future__ import annotations

import sys
from pathlib import Path

from native_kernel.postgresql_profile.conformance import (
    ConformanceExecutionError,
    render_report,
    report_from_environment,
)


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 1:
        print(
            "usage: postgresql_profile_adapter.py <fixture-pack.json>",
            file=sys.stderr,
        )
        return 2
    try:
        report = report_from_environment(Path(args[0]))
    except (ConformanceExecutionError, OSError, ValueError) as exc:
        print(f"P4 adapter failed: {exc}", file=sys.stderr)
        return 1
    print(render_report(report), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
