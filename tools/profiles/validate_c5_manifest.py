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
    _require(manifest.get("manifest_version") == "nk-c5-operational-manifest/1", "unsupported C5 manifest version")
    _require(manifest.get("phase") == "C5", "manifest phase must be C5")
    _require(manifest.get("decision_record") == "ADR-0021", "ADR-0021 required")
    _require(manifest.get("decision_status") == "ACCEPTED", "C5 decision must be accepted")
    _require(manifest.get("operator_approval") == "APPROVED", "C5 operator approval required")
    _require(manifest.get("implementation_status") == "PARTIAL", "C5 must remain partial")
    _require(manifest.get("operational_validation") == "C5_BOUNDED_REHEARSAL", "wrong C5 operational level")
    _require(manifest.get("kernel_runtime_conformance") == "C4", "C5 rehearsal must not rewrite assertion conformance")
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
        (prerequisite.get("level"), prerequisite.get("supported"), prerequisite.get("partial"), prerequisite.get("unsupported"), prerequisite.get("failed"))
        == ("C4", 45, 10, 17, 0),
        "C5 prerequisite assertion map drift",
    )

    boundary = manifest.get("deployment_boundary")
    _require(isinstance(boundary, Mapping), "C5 deployment boundary required")
    _require(boundary.get("deployment_class") == "CI_EPHEMERAL_SYNTHETIC", "wrong deployment class")
    _require(boundary.get("synthetic_data_only") is True, "synthetic-only boundary required")
    for key in (
        "live_user_data", "production_traffic", "network_api_exposed", "authority_promotion",
        "authoritative_external_side_effects", "ecosystem_wiring", "physical_deletion_claimed",
        "compliance_certification_claimed",
    ):
        _require(boundary.get(key) is False, f"unsafe C5 boundary: {key}")

    _require(
        set(manifest.get("scenario_categories") or ()) ==
        {"SECURITY", "PRIVACY", "RECOVERY", "ROLLBACK", "INCIDENT", "RELIABILITY", "RESILIENCE"},
        "C5 scenario categories drifted",
    )

    evidence = manifest.get("repository_evidence")
    _require(isinstance(evidence, Mapping), "repository evidence entry required")
    _require(evidence.get("status") == "PASS", "final C5 repository evidence must be PASS")
    _require(evidence.get("head_sha") == "3d56912260ea41b5b501b65477bff1642dfc2d58", "final-main C5 evidence SHA drift")
    _require(evidence.get("workflow_run_id") == "31205512911", "final-main C5 run drift")
    artifacts = evidence.get("artifacts")
    matrix = evidence.get("matrix")
    _require(evidence.get("artifact_count") == 4, "C5 PASS requires four artifacts")
    _require(isinstance(artifacts, list) and len(artifacts) == 4, "C5 PASS artifact inventory required")
    _require(isinstance(matrix, list) and len(matrix) == 4, "C5 PASS matrix required")
    expected_digests = {
        "c5-operational-evidence-py3.11-pg16": "sha256:7a17248c3cbd612df93b85956299160a99c5e4ca4b97d27da492958731a6b8a5",
        "c5-operational-evidence-py3.11-pg18": "sha256:b285a118c562f58df0bbe1411f1ef3cec9c9767c68f8ce3b9cee2054b4bc407a",
        "c5-operational-evidence-py3.12-pg16": "sha256:714e18a6b0974ebbfc708b6ae4de129ca1d4c8666337ac3a53e99e10d86f2e92",
        "c5-operational-evidence-py3.12-pg18": "sha256:4a68f36a17e958c1def3923d3181ebcd974e8a3adba94fb4892ec02505720f4c",
    }
    _require({item.get("name"): item.get("digest") for item in artifacts} == expected_digests, "final-main artifact digest inventory drift")

    durable = manifest.get("durable_evidence")
    _require(isinstance(durable, Mapping), "durable evidence entry required")
    _require(durable.get("protocol") == "nk-evidence-bundle/1", "durable evidence protocol drift")
    _require(durable.get("status") == "CAPTURED_REPOSITORY_RESIDENT", "durable C5 evidence is not captured")
    _require(durable.get("checkpoint_count") == 2 and durable.get("artifact_count") == 8, "durable evidence inventory drift")
    _require(durable.get("original_archives_preserved") is True, "original C5 archives must be preserved")
    durable_path = root / str(durable.get("path"))
    _require(durable_path.is_file(), "durable evidence manifest missing")

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
    for phrase in ("bounded synthetic ephemeral", "45 supported / 10 partial / 17 unsupported / 0 failed", "no production readiness", "no authority promotion", "without expanding"):
        _require(phrase in limitations, f"missing C5 evidence boundary: {phrase}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", nargs="?", type=Path, default=Path("profiles/operational-validation-v0/c5-manifest.json"))
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    manifest = _load(args.manifest)
    validate(manifest, root=args.root.resolve())
    print(
        "C5 manifest validation passed; "
        f"head={manifest['repository_evidence']['head_sha']}; "
        f"run={manifest['repository_evidence']['workflow_run_id']}; "
        f"durable={manifest['durable_evidence']['status']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
