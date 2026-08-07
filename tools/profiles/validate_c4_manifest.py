from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "profiles" / "shadow-evaluation-v0" / "c4-manifest.json"


class ManifestError(RuntimeError):
    pass


def load(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ManifestError(f"cannot load {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ManifestError(f"{path} must contain an object")
    return value


def validate(manifest: dict, *, root: Path = ROOT) -> None:
    if manifest.get("manifest_version") != "nk-c4-shadow-manifest/1":
        raise ManifestError("wrong C4 manifest version")
    if manifest.get("phase") != "C4" or manifest.get("implementation_status") != "PARTIAL":
        raise ManifestError("C4 manifest phase/status mismatch")
    if manifest.get("decision_record") != "ADR-0020" or manifest.get("decision_status") != "ACCEPTED" or manifest.get("operator_approval") != "APPROVED":
        raise ManifestError("C4 decision lineage is invalid")
    if manifest.get("shadow_report_protocol") != "nk-shadow-report/1" or manifest.get("shadow_receipt_protocol") != "nk-shadow-receipt/1" or manifest.get("dataset_protocol") != "nk-shadow-workload/1":
        raise ManifestError("C4 protocols are invalid")
    dataset = manifest.get("dataset")
    if not isinstance(dataset, dict):
        raise ManifestError("C4 dataset record is missing")
    dataset_path = root / str(dataset.get("path", ""))
    if not dataset_path.is_file():
        raise ManifestError("C4 dataset file is missing")
    raw = dataset_path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if dataset.get("sha256") != digest:
        raise ManifestError("C4 dataset digest drift")
    dataset_doc = load(dataset_path)
    if dataset_doc.get("dataset_version") != "nk-shadow-workload/1" or dataset_doc.get("dataset_id") != dataset.get("id"):
        raise ManifestError("C4 dataset identity mismatch")
    cases = dataset_doc.get("cases")
    if not isinstance(cases, list) or len(cases) != dataset.get("case_count") or len(cases) != 15:
        raise ManifestError("C4 case count mismatch")
    if dataset.get("approval_state") != "APPROVED" or dataset_doc.get("approval", {}).get("state") != "APPROVED":
        raise ManifestError("C4 dataset is not approved")
    prerequisite = manifest.get("prerequisite")
    if prerequisite != {"level": "C3", "supported": 45, "partial": 10, "unsupported": 17, "failed": 0}:
        raise ManifestError("C4 prerequisite map changed")
    coverage = manifest.get("c4_assertion_coverage")
    if coverage != {"total": 72, "shadow_evaluated_supported": 45, "inherited_partial": 10, "inherited_unsupported": 17, "failed": 0, "proposed_nk_epi_unsupported": 8}:
        raise ManifestError("C4 assertion coverage is invalid")
    policy = manifest.get("authority_boundary")
    expected_policy = {"mode": "SHADOW_ONLY", "authority_promotion": "FORBIDDEN", "authoritative_writes": "FORBIDDEN", "side_effects": "FORBIDDEN", "promotion_decision": "NOT_AUTHORIZED"}
    if policy != expected_policy:
        raise ManifestError("C4 authority boundary is unsafe")
    evidence = manifest.get("repository_evidence")
    if not isinstance(evidence, dict):
        raise ManifestError("C4 repository evidence is missing")
    if evidence.get("reports_per_artifact") != 4 or evidence.get("artifact_retention_days") != 30:
        raise ManifestError("C4 artifact contract is invalid")
    if evidence.get("status") == "PASS":
        if not evidence.get("head_sha") or not evidence.get("workflow_run_id") or evidence.get("artifact_count") != 4 or len(evidence.get("matrix", [])) != 4:
            raise ManifestError("C4 PASS requires exact repository run and four artifacts")
    elif evidence.get("status") != "PRE_CI":
        raise ManifestError("C4 evidence status must be PRE_CI or PASS")
    boundaries = " ".join(manifest.get("evidence_boundaries", [])).lower()
    for fragment in ("45 assertions", "not live production shadowing", "no authority promotion", "c5", "production"):
        if fragment not in boundaries:
            raise ManifestError(f"C4 evidence boundary missing {fragment}")
    issue1 = manifest.get("issue_1_boundary")
    if issue1 != {"relationship": "INDEPENDENT", "historical_lineage": None, "may_claim_recovery": False}:
        raise ManifestError("C4 may not claim historical recovery")
    issue18 = manifest.get("issue_18_boundary")
    if issue18 != {"relationship": "INDEPENDENT", "package_published": False, "new_external_runtime_dependency": False}:
        raise ManifestError("C4 may not alter Issue #18 boundaries")


def main() -> int:
    try:
        validate(load(MANIFEST))
    except ManifestError as exc:
        print(f"C4 manifest validation failed: {exc}", file=sys.stderr)
        return 1
    print("C4 manifest validation PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
