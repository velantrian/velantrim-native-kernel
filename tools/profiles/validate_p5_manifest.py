from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Mapping

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "profiles" / "sqlite-embedded-v0" / "p5-manifest.json"
SHA_RE = re.compile(r"^[0-9a-f]{40}$")


class ManifestError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ManifestError("P5 manifest must be a JSON object")
    return value


def _require_counts(value: object, expected: Mapping[str, object], label: str) -> None:
    if not isinstance(value, dict):
        raise ManifestError(f"{label} must be an object")
    for key, expected_value in expected.items():
        if value.get(key) != expected_value:
            raise ManifestError(f"{label}.{key} must be {expected_value!r}")


def validate_manifest(manifest: Mapping[str, Any]) -> None:
    exact = {
        "manifest_version": "nk-p5-implementation-manifest/1",
        "profile_id": "native-kernel/sqlite-embedded",
        "profile_version": "0.5-p5",
        "evidence_lineage": "clean/sqlite-embedded/0.1",
        "comparison_profile_id": "native-kernel/postgresql-reference",
        "comparison_profile_version": "0.4-p4",
        "decision_record": "ADR-0019",
        "decision_status": "ACCEPTED",
        "operator_approval": "APPROVED",
        "phase": "P5",
        "implementation_status": "PARTIAL",
        "evidence_report_protocol": "nk-evidence-report/1",
        "equivalence_report_protocol": "nk-equivalence-report/1",
        "contract_registry": "nk-contract-registry/1.1.0",
    }
    for key, expected in exact.items():
        if manifest.get(key) != expected:
            raise ManifestError(f"{key} must be {expected!r}")
    _require_counts(
        manifest.get("sqlite_assertion_coverage"),
        {
            "total": 72,
            "supported": 41,
            "partial": 13,
            "unsupported": 18,
            "failed": 0,
            "proposed_nk_epi_unsupported": 8,
        },
        "sqlite_assertion_coverage",
    )
    _require_counts(
        manifest.get("c3_assertion_coverage"),
        {
            "total": 72,
            "supported": 45,
            "partial": 10,
            "unsupported": 17,
            "failed": 0,
            "proposed_nk_epi_unsupported": 8,
        },
        "c3_assertion_coverage",
    )
    c3 = manifest["c3_assertion_coverage"]
    if set(c3.get("promoted_by_cross_profile_evidence", [])) != {
        "NK-SEM-008", "NK-ID-008", "NK-EQV-002", "NK-EQV-003"
    }:
        raise ManifestError("unexpected C3 promotion set")
    state = manifest.get("conformance_state")
    if not isinstance(state, dict) or state.get("support_state") != "PARTIAL":
        raise ManifestError("conformance support_state must remain PARTIAL")
    if state.get("c4") != "NOT_ESTABLISHED" or state.get("c5") != "NOT_ESTABLISHED":
        raise ManifestError("P5 cannot establish C4/C5")
    if state.get("sqlite_repository_c2") not in {"NOT_ESTABLISHED", "REPOSITORY_REPRODUCED"}:
        raise ManifestError("invalid sqlite_repository_c2")
    if state.get("cross_profile_c3") not in {"NOT_ESTABLISHED", "REPOSITORY_REPRODUCED"}:
        raise ManifestError("invalid cross_profile_c3")
    classes = manifest.get("equivalence_classes")
    if not isinstance(classes, dict) or set(classes) != {"BYTE", "STRUCTURAL", "SEMANTIC", "BEHAVIOURAL"}:
        raise ManifestError("all four equivalence classes are required")
    for key in ("allowed_differences", "forbidden_differences", "evidence_boundaries", "forbidden_in_p5"):
        values = manifest.get(key)
        if not isinstance(values, list) or not values or not all(isinstance(item, str) and item for item in values):
            raise ManifestError(f"{key} must be a non-empty string list")
    forbidden_text = "\n".join(manifest["forbidden_in_p5"])
    for phrase in (
        "all 72", "operational equivalence", "physical", "C4 or C5",
        "production", "Titan Mentaury or Crystal", "v0.1.2.1", "NK-EPI"
    ):
        if phrase not in forbidden_text:
            raise ManifestError(f"missing forbidden boundary: {phrase}")
    issue_1 = manifest.get("issue_1_boundary")
    if not isinstance(issue_1, dict) or issue_1.get("may_claim_recovery") is not False:
        raise ManifestError("P5 may not claim historical recovery")
    if issue_1.get("historical_lineage") is not None:
        raise ManifestError("P5 historical_lineage must remain null")
    evidence = manifest.get("repository_evidence")
    if not isinstance(evidence, dict):
        raise ManifestError("repository_evidence must be an object")
    reproduced = (
        state.get("sqlite_repository_c2") == "REPOSITORY_REPRODUCED"
        or state.get("cross_profile_c3") == "REPOSITORY_REPRODUCED"
    )
    if reproduced:
        if evidence.get("status") not in {"PASS_PREVIOUS_HEAD", "PASS_FINAL_HEAD", "PASS_MAIN"}:
            raise ManifestError("reproduced evidence requires a PASS status")
        head = evidence.get("head_sha")
        run_id = evidence.get("workflow_run_id")
        if not isinstance(head, str) or not SHA_RE.fullmatch(head):
            raise ManifestError("reproduced evidence requires exact head_sha")
        if isinstance(run_id, bool) or not isinstance(run_id, int) or run_id < 1:
            raise ManifestError("reproduced evidence requires workflow_run_id")
        if evidence.get("artifact_count", 0) < 3:
            raise ManifestError("reproduced P5 evidence requires at least three artifacts")
    else:
        if evidence.get("status") != "NOT_RECORDED":
            raise ManifestError("unreproduced P5 evidence must remain NOT_RECORDED")
        if evidence.get("head_sha") is not None or evidence.get("workflow_run_id") is not None:
            raise ManifestError("unreproduced P5 evidence cannot name a head/run")


def main() -> int:
    try:
        validate_manifest(_load(MANIFEST))
    except (OSError, json.JSONDecodeError, ManifestError) as exc:
        print(f"P5 manifest validation failed: {exc}")
        return 1
    print("P5 manifest validation PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
