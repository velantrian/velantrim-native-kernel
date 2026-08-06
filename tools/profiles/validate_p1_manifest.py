from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = ROOT / "profiles" / "postgresql-reference-v0" / "p1-manifest.json"


class P1ManifestError(ValueError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise P1ManifestError("manifest root must be an object")
    return value


def validate_p1_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
    expected = {
        "manifest_version": "nk-p1-implementation-manifest/1",
        "profile_id": "native-kernel/postgresql-reference",
        "profile_version": "0.1-p1",
        "evidence_lineage": "clean/postgresql-reference/0.1",
        "decision_status": "ACCEPTED",
        "operator_approval": "APPROVED",
        "phase": "P1",
        "implementation_status": "PARTIAL",
        "evidence_level": "LOCALLY_TESTED",
        "kernel_runtime_conformance": "UNSUPPORTED",
    }
    for key, expected_value in expected.items():
        if manifest.get(key) != expected_value:
            raise P1ManifestError(f"{key} must be {expected_value!r}")

    language = manifest.get("language_profile", {})
    if language.get("language") != "Python":
        raise P1ManifestError("P1 language must be Python")
    if language.get("dependencies") != "STANDARD_LIBRARY_ONLY":
        raise P1ManifestError("P1 must remain standard-library only")
    if language.get("package") != "native_kernel.semantic_core":
        raise P1ManifestError("unexpected P1 package")
    if language.get("permanent_architecture_choice") is not False:
        raise P1ManifestError("P1 language cannot be promoted to permanent architecture")

    support = manifest.get("assertion_support_policy", {})
    if support.get("reported_runtime_support") != "UNSUPPORTED":
        raise P1ManifestError("P1 cannot claim assertion runtime support before P4")
    if support.get("registry_version") != "nk-contract-registry/1.1.0":
        raise P1ManifestError("unexpected registry version")

    boundary = manifest.get("issue_1_boundary", {})
    if boundary.get("relationship") != "INDEPENDENT":
        raise P1ManifestError("Issue #1 must remain independent")
    if boundary.get("historical_lineage") is not None:
        raise P1ManifestError("clean P1 cannot claim historical lineage")
    if boundary.get("may_claim_recovery") is not False:
        raise P1ManifestError("clean P1 cannot claim source recovery")
    if boundary.get("may_use_v0_1_2_1_name") is not False:
        raise P1ManifestError("clean P1 cannot use the v0.1.2.1 identity")

    forbidden = set(manifest.get("forbidden_in_p1", []))
    if not any("PostgreSQL" in item for item in forbidden):
        raise P1ManifestError("P1 must explicitly forbid a PostgreSQL adapter")
    if not any("C1" in item or "C2" in item or "C3" in item for item in forbidden):
        raise P1ManifestError("P1 must explicitly forbid conformance promotion")

    validation = manifest.get("local_validation", {})
    if validation.get("semantic_core_tests") != 20:
        raise P1ManifestError("unexpected semantic-core test count")
    if validation.get("semantic_core_result") != "PASS":
        raise P1ManifestError("semantic-core local result must be PASS")
    if validation.get("repository_ci") != "NOT_RECORDED":
        raise P1ManifestError("repository CI must not be inferred")

    return {
        "profile_id": manifest["profile_id"],
        "phase": manifest["phase"],
        "implementation_status": manifest["implementation_status"],
        "kernel_runtime_conformance": manifest["kernel_runtime_conformance"],
        "status": "PASS",
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate the Native Kernel P1 implementation manifest"
    )
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        report = validate_p1_manifest(load_json(args.manifest))
    except (P1ManifestError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False, indent=2))
        return 1
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
