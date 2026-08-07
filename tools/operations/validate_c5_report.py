#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from native_kernel.operational_validation import (
    OperationalValidationError,
    canonical_json_bytes,
    load_json,
    sha256_digest,
    validate_report,
)


def validate_backup(backup: dict, *, canaries: tuple[str, ...]) -> None:
    if backup.get("protocol") != "nk-operational-backup/1":
        raise OperationalValidationError("unsupported operational backup protocol")
    if not isinstance(backup.get("events"), list) or not backup["events"]:
        raise OperationalValidationError("operational backup events required")
    if backup.get("event_count") != len(backup["events"]):
        raise OperationalValidationError("operational backup event count mismatch")
    digest = backup.get("backup_digest")
    body = dict(backup)
    body.pop("backup_digest", None)
    if digest != sha256_digest(canonical_json_bytes(body)):
        raise OperationalValidationError("operational backup digest mismatch")
    text = json.dumps(backup, sort_keys=True)
    if any(token in text for token in canaries):
        raise OperationalValidationError("operational backup contains privacy canary")
    limitations = " ".join(str(item).lower() for item in backup.get("limitations", []))
    if "not a physical postgresql backup" not in limitations:
        raise OperationalValidationError("operational backup limitation missing")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--c4-report", type=Path)
    parser.add_argument("--backup", type=Path)
    parser.add_argument("--require-repository", action="store_true")
    args = parser.parse_args()

    report = load_json(args.report)
    plan = load_json(args.plan)
    plan_bytes = args.plan.read_bytes()
    validate_report(
        report,
        plan=plan,
        plan_bytes=plan_bytes,
        require_repository=args.require_repository,
    )
    if args.c4_report:
        expected = sha256_digest(args.c4_report.read_bytes())
        actual = report.get("prerequisite", {}).get("sha256")
        if actual != expected:
            raise OperationalValidationError(
                f"C4 prerequisite digest mismatch: expected {expected}, got {actual}"
            )
    if args.backup:
        validate_backup(
            load_json(args.backup),
            canaries=tuple(plan["privacy"]["canary_tokens"]),
        )
    print(
        "C5 report validation passed; "
        f"plan={report['plan']['sha256']}; "
        f"scenarios={report['metrics']['scenario_count']}; "
        f"commit={report['environment']['commit']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
