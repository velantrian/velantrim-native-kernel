#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping


class ManifestError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ManifestError(message)


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ManifestError(f"{path}: top-level JSON must be an object")
    return value


def validate(manifest: Mapping[str, Any], *, root: Path) -> None:
    _require(
        manifest.get("manifest_version") == "nk-c5-operational-manifest/1",
        "unsupported C5 manifest version",
    )
    _require(manifest.get("phase") == "C5", "manifest phase must be C5")
    _require(manifest.get("decision_record") == "ADR-0021", "ADR-0021 required")
    _require(manifest.get("decision_status") == "ACCEPTED", "C5 decision must be accepted")
    _require(manifest.get("operator_approval") == "APPROVED", "C5 operator approval required")
    _require(manifest.get("implementation_status") == "PARTIAL", "C5 must remain partial")
    _require(
        manifest.get("operational_validation") == "C5_BOUNDED_REHEARSAL",
        "wrong C5 operational level",
    )
    _require(
        manifest.get("kernel_runtime_conformance") == "C4",
        "C5 rehearsal must not rewrite assertion conformance",
    )
    _require(manifest.get("support_state") == "PARTIAL", "support state must remain PARTIAL")

    plan = manifest.get("plan")
    _require(isinstance(plan, Mapping), "C5 plan manifest entry required")
    _require(plan.get("id") == "native-kernel/c5-bounded-rehearsal-v1", "unexpected C5 plan id")
    _require(plan.get("protocol") == "nk-operational-plan/1", "wrong C5 plan protocol")
    _require(plan.get("scenario_count") == 18, "C5 scenario count must be 18")
    plan_path = root / str(plan.get("path"))
    _require(plan_path.is_file(), "C5 plan file missing")
    actual_digest = hashlib.sha256(plan_path.read_bytes()).hexdigest()
    _require(plan.get("sha256") == actual_digest, "C5 plan digest drift")

    prerequisite = manifest.get("prerequisite")
    _require(isinstance(prerequisite, Mapping), "C4 prerequisite required")
    _require(
        (
            prerequisite.get("level"),
            prerequisite.get("supported"),
            prerequisite.get("partial"),
            prerequisite.get("unsupported"),
            prerequisite.get("failed"),
        )
        == ("C4", 45, 10, 17, 0),
        "C5 prerequisite assertion map drift",
    )

    boundary = manifest.get("deployment_boundary")
    _require(isinstance(boundary, Mapping), "C5 deployment boundary required")
    _require(boundary.get("deployment_class") == "CI_EPHEMERAL_SYNTHETIC", "wrong deployment class")
    _require(boundary.get("synthetic_data_only") is True, "synthetic-only boundary required")
    for key in (
        "live_user_data",
        "production_traffic",
        "network_api_exposed",
        "authority_promotion",
        "authoritative_external_side_effects",
        "ecosystem_wiring",
        "physical_deletion_claimed",
        "compliance_certification_claimed",
    ):
        _require(boundary.get(key) is False, f"unsafe C5 boundary: {key}")

    categories = manifest.get("scenario_categories")
    _require(
        set(categories or ()) == {
            "SECURITY",
            "PRIVACY",
            "RECOVERY",
            "ROLLBACK",
            "INCIDENT",
            "RELIABILITY",
            "RESILIENCE",
        },
        "C5 scenario categories drifted",
    )

    evidence = manifest.get("repository_evidence")
    _require(isinstance(evidence, Mapping), "repository evidence entry required")
    status = evidence.get("status")
    _require(status in {"PRE_CI", "PASS"}, "invalid C5 repository evidence status")
    if status == "PASS":
        head = evidence.get("head_sha")
        run_id = evidence.get("workflow_run_id")
        artifacts = evidence.get("artifacts")
        matrix = evidence.get("matrix")
        _require(
            isinstance(head, str) and len(head) == 40 and all(ch in "0123456789abcdef" for ch in head),
            "C5 PASS requires exact repository head",
        )
        _require(isinstance(run_id, str) and run_id.isdigit(), "C5 PASS requires workflow run id")
        _require(evidence.get("artifact_count") == 4, "C5 PASS requires four artifacts")
        _require(isinstance(artifacts, list) and len(artifacts) == 4, "C5 PASS artifact inventory required")
        _require(isinstance(matrix, list) and len(matrix) == 4, "C5 PASS matrix required")
        for artifact in artifacts:
            _require(
                isinstance(artifact, Mapping)
                and isinstance(artifact.get("name"), str)
                and isinstance(artifact.get("digest"), str)
                and artifact["digest"].startswith("sha256:"),
                "invalid C5 artifact entry",
            )
    else:
        _require(evidence.get("head_sha") is None, "PRE_CI must not claim repository head")
        _require(evidence.get("workflow_run_id") is None, "PRE_CI must not claim run id")
        _require(evidence.get("artifact_count") == 0, "PRE_CI must not claim artifacts")

    issue1 = manifest.get("issue_1_boundary")
    _require(isinstance(issue1, Mapping), "Issue #1 boundary required")
    _require(issue1.get("relationship") == "INDEPENDENT", "Issue #1 must remain independent")
    _require(issue1.get("historical_lineage") is None, "C5 cannot claim historical lineage")
    _require(issue1.get("may_claim_recovery") is False, "C5 cannot claim source recovery")

    issue18 = manifest.get("issue_18_boundary")
    _require(isinstance(issue18, Mapping), "Issue #18 boundary required")
    _require(issue18.get("relationship") == "INDEPENDENT", "Issue #18 must remain independent")
    _require(issue18.get("new_external_runtime_dependency") is False, "C5 cannot add runtime dependency")
    _require(issue18.get("package_published") is False, "C5 cannot claim package publication")

    limitations = " ".join(str(item).lower() for item in manifest.get("evidence_boundaries", []))
    for phrase in (
        "bounded synthetic ephemeral",
        "45 supported / 10 partial / 17 unsupported / 0 failed",
        "no production readiness",
        "no authority promotion",
    ):
        _require(phrase in limitations, f"missing C5 evidence boundary: {phrase}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "manifest",
        nargs="?",
        type=Path,
        default=Path("profiles/operational-validation-v0/c5-manifest.json"),
    )
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    manifest = _load(args.manifest)
    validate(manifest, root=args.root.resolve())
    print(
        "C5 manifest validation passed; "
        f"status={manifest['repository_evidence']['status']}; "
        f"plan={manifest['plan']['sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
