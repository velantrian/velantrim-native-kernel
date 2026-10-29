"""Read-only comparison of two nk-p1 semantic-state exports; not an H11 oracle."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from native_kernel.semantic_core.errors import ContractViolation
from native_kernel.semantic_core.state_codec import semantic_state_from_contract_object

MAX_EXPORT_BYTES = 4 * 1024 * 1024
SCOPE = "nk-p1-semantic-state/1-export-comparison-only"


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ValueError("non-finite JSON constant")


def read_export(path: Path) -> Any:
    with path.open("rb") as stream:
        data = stream.read(MAX_EXPORT_BYTES + 1)
    if len(data) > MAX_EXPORT_BYTES:
        raise ValueError("export exceeds the local probe byte limit")
    return json.loads(data.decode("utf-8"), object_pairs_hook=_unique_object,
                      parse_constant=_reject_constant)


def compare_objects(source: Any, target: Any) -> dict[str, Any]:
    """Validate both with the existing v1 codec, then compare all represented fields."""
    states = []
    for side, value in (("source", source), ("target", target)):
        try:
            states.append(semantic_state_from_contract_object(value))
        except (ContractViolation, RecursionError):
            return {"status": "BLOCKED", "scope": SCOPE, "reason": f"invalid_{side}"}
    left, right = (state.as_contract_object() for state in states)
    changed = sorted(key for key in left if left[key] != right[key])
    return {"status": "FAIL" if changed else "PASS", "scope": SCOPE,
            "changed_fields": changed}


def compare_files(source: Path, target: Path) -> dict[str, Any]:
    values = []
    for side, path in (("source", source), ("target", target)):
        try:
            values.append(read_export(path))
        except (OSError, ValueError, RecursionError):
            # Do not echo rejected content, decoder details or private file paths.
            return {"status": "BLOCKED", "scope": SCOPE, "reason": f"unreadable_{side}"}
    return compare_objects(*values)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path)
    args = parser.parse_args(argv)
    result = compare_files(args.source, args.target)
    print(json.dumps(result, sort_keys=True))
    return {"PASS": 0, "FAIL": 1, "BLOCKED": 2}[result["status"]]


if __name__ == "__main__":
    raise SystemExit(main())
