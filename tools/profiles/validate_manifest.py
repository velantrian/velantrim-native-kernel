from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "contracts" / "registry.json"
DEFAULT_MANIFEST = ROOT / "profiles" / "postgresql-reference-v0" / "profile-manifest.json"


class ManifestError(ValueError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ManifestError(f"{path}: root must be an object")
    return value


def registry_ids(registry: dict[str, Any]) -> tuple[list[str], set[str]]:
    ids: list[str] = []
    epi: set[str] = set()
    for family in registry.get("families", []):
        family_id = family.get("family_id")
        for assertion in family.get("assertions", []):
            assertion_id = assertion.get("assertion_id")
            if not isinstance(assertion_id, str):
                raise ManifestError("registry assertion_id must be a string")
            ids.append(assertion_id)
            if family_id == "NK-EPI":
                epi.add(assertion_id)
    if len(ids) != len(set(ids)):
        raise ManifestError("registry contains duplicate assertion IDs")
    return ids, epi


def validate_manifest(manifest: dict[str, Any], registry: dict[str, Any]) -> dict[str, Any]:
    if manifest.get("profile_manifest_version") != "nk-profile-manifest/0.1":
        raise ManifestError("unexpected profile_manifest_version")
    if manifest.get("profile_id") != "native-kernel/postgresql-reference":
        raise ManifestError("unexpected profile_id")
    if manifest.get("decision_status") != "PROPOSED":
        raise ManifestError("planning manifest must remain PROPOSED")
    if manifest.get("operator_approval") != "PENDING":
        raise ManifestError("operator approval must remain PENDING")
    if manifest.get("implementation_status") != "NOT_STARTED":
        raise ManifestError("implementation_status must remain NOT_STARTED")
    if manifest.get("kernel_runtime_conformance") != "UNSUPPORTED":
        raise ManifestError("planning manifest cannot claim Kernel runtime conformance")
    if manifest.get("historical_lineage") is not None:
        raise ManifestError("clean profile must not claim historical lineage")

    issue_boundary = manifest.get("issue_1_boundary", {})
    if issue_boundary.get("relationship") != "INDEPENDENT":
        raise ManifestError("Issue #1 relationship must remain INDEPENDENT")
    if issue_boundary.get("may_claim_recovery") is not False:
        raise ManifestError("planning profile cannot claim recovery")
    if issue_boundary.get("may_use_v0_1_2_1_name") is not False:
        raise ManifestError("planning profile cannot use the v0.1.2.1 identity")

    expected_ids, epi_ids = registry_ids(registry)
    rows = manifest.get("assertion_plan")
    if not isinstance(rows, list):
        raise ManifestError("assertion_plan must be a list")

    seen: set[str] = set()
    for row in rows:
        if not isinstance(row, dict):
            raise ManifestError("assertion_plan entries must be objects")
        assertion_id = row.get("assertion_id")
        if assertion_id in seen:
            raise ManifestError(f"duplicate assertion plan: {assertion_id}")
        seen.add(assertion_id)
        if row.get("runtime_support") != "UNSUPPORTED":
            raise ManifestError(f"{assertion_id}: planning manifest cannot claim runtime support")
        if row.get("evidence_state") != "NONE":
            raise ManifestError(f"{assertion_id}: planning evidence must remain NONE")
        if assertion_id in epi_ids:
            if row.get("planning_state") != "DEFERRED_PROPOSED_FAMILY":
                raise ManifestError(f"{assertion_id}: NK-EPI must remain deferred/proposed")
            if row.get("implementation_phase") != "NONE":
                raise ManifestError(f"{assertion_id}: NK-EPI must not receive an implementation phase")
        else:
            if row.get("planning_state") != "PLANNED":
                raise ManifestError(f"{assertion_id}: accepted-family assertion must be PLANNED")
            if row.get("implementation_phase") not in {"P1", "P2", "P3", "P4", "P5"}:
                raise ManifestError(f"{assertion_id}: invalid implementation phase")

    expected = set(expected_ids)
    if seen != expected:
        missing = sorted(expected - seen)
        extra = sorted(seen - expected)
        raise ManifestError(f"assertion coverage mismatch; missing={missing}, extra={extra}")

    return {
        "profile_id": manifest["profile_id"],
        "profile_version": manifest["profile_version"],
        "assertions": len(seen),
        "planned": len(seen - epi_ids),
        "deferred_epi": len(epi_ids),
        "runtime_support": "UNSUPPORTED",
        "status": "PASS",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Native Kernel planning profile manifest")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        report = validate_manifest(load_json(args.manifest), load_json(REGISTRY))
    except (ManifestError, OSError, json.JSONDecodeError, KeyError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False, indent=2))
        return 1

    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
