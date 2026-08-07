from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "profiles" / "postgresql-reference-v0" / "p4-manifest.json"


class ManifestError(ValueError):
    pass


def validate(data: dict[str, object]) -> None:
    expected = {
        "manifest_version": "nk-p4-implementation-manifest/1",
        "profile_id": "native-kernel/postgresql-reference",
        "profile_version": "0.4-p4",
        "evidence_lineage": "clean/postgresql-reference/0.1",
        "decision_record": "ADR-0018",
        "decision_status": "ACCEPTED",
        "operator_approval": "APPROVED",
        "phase": "P4",
        "implementation_status": "PARTIAL",
        "evidence_report_protocol": "nk-evidence-report/1",
        "contract_registry": "nk-contract-registry/1.1.0",
    }
    for key, value in expected.items():
        if data.get(key) != value:
            raise ManifestError(f"{key} must remain {value!r}")

    coverage = data.get("assertion_coverage")
    if not isinstance(coverage, dict):
        raise ManifestError("assertion_coverage must be an object")
    if coverage != {
        "total": 72,
        "supported": 41,
        "partial": 13,
        "unsupported": 18,
        "failed": 0,
        "proposed_nk_epi_unsupported": 8,
    }:
        raise ManifestError("assertion support summary drifted")

    state = data.get("conformance_state")
    if not isinstance(state, dict):
        raise ManifestError("conformance_state must be an object")
    if state.get("support_state") != "PARTIAL":
        raise ManifestError("P4 support_state must remain PARTIAL")
    if state.get("local_c1") not in {"NOT_RECORDED", "LOCALLY_TESTED"}:
        raise ManifestError("invalid local C1 state")
    if state.get("repository_c2") not in {
        "NOT_ESTABLISHED",
        "REPOSITORY_REPRODUCED",
    }:
        raise ManifestError("invalid repository C2 state")
    for level in ("c3", "c4", "c5"):
        if state.get(level) != "NOT_ESTABLISHED":
            raise ManifestError(f"P4 cannot promote {level.upper()}")

    evidence = data.get("repository_evidence")
    if not isinstance(evidence, dict):
        raise ManifestError("repository_evidence must be an object")
    status = evidence.get("status")
    if status not in {"NOT_RECORDED", "PASS_PREVIOUS_HEAD", "PASS"}:
        raise ManifestError("invalid repository evidence status")
    matrix = evidence.get("matrix")
    if not isinstance(matrix, list) or len(matrix) != 4:
        raise ManifestError("repository matrix must have four entries")
    if status == "NOT_RECORDED":
        if state.get("repository_c2") != "NOT_ESTABLISHED":
            raise ManifestError("C2 cannot be established without repository evidence")
        if evidence.get("head_sha") is not None or evidence.get("workflow_run_id") is not None:
            raise ManifestError("unrecorded evidence cannot name a head or run")
        if evidence.get("artifacts") != "NOT_RECORDED":
            raise ManifestError("unrecorded evidence cannot claim artifacts")
        if any(not str(item).endswith(":NOT_RUN") for item in matrix):
            raise ManifestError("unrecorded matrix entries must be NOT_RUN")
    else:
        if state.get("repository_c2") != "REPOSITORY_REPRODUCED":
            raise ManifestError("repository PASS requires C2 reproduction")
        head = evidence.get("head_sha")
        run_id = evidence.get("workflow_run_id")
        if not isinstance(head, str) or len(head) != 40:
            raise ManifestError("repository PASS requires exact head SHA")
        if isinstance(run_id, bool) or not isinstance(run_id, int) or run_id < 1:
            raise ManifestError("repository PASS requires workflow run ID")
        if evidence.get("artifacts") != "RETAINED_PER_MATRIX_JOB":
            raise ManifestError("repository PASS requires retained artifacts")
        if any(not str(item).endswith(":PASS") for item in matrix):
            raise ManifestError("repository PASS requires every matrix entry PASS")
        for key in ("p1_regression", "p2_regression", "p3_regression"):
            if evidence.get(key) != "PASS":
                raise ManifestError(f"repository PASS requires {key}=PASS")

    boundaries = data.get("evidence_boundaries")
    if not isinstance(boundaries, list):
        raise ManifestError("evidence_boundaries must be a list")
    joined_boundaries = "\n".join(str(item) for item in boundaries)
    for phrase in (
        "only to assertion results marked SUPPORTED",
        "not C3",
        "no truth",
        "no physical",
        "no C4 C5",
    ):
        if phrase not in joined_boundaries:
            raise ManifestError(f"missing evidence boundary: {phrase}")

    issue1 = data.get("issue_1_boundary")
    if not isinstance(issue1, dict):
        raise ManifestError("issue_1_boundary must be an object")
    if issue1.get("relationship") != "INDEPENDENT":
        raise ManifestError("Issue #1 must remain independent")
    if issue1.get("historical_lineage") is not None:
        raise ManifestError("P4 cannot claim historical lineage")
    if issue1.get("may_claim_recovery") is not False:
        raise ManifestError("P4 cannot claim recovery")

    forbidden = data.get("forbidden_in_p4")
    if not isinstance(forbidden, list):
        raise ManifestError("forbidden_in_p4 must be a list")
    joined = "\n".join(str(item) for item in forbidden)
    for phrase in (
        "P5 SQLite",
        "C3 cross-profile",
        "physical or cryptographic deletion",
        "truth or external authenticity",
        "C4 or C5",
        "production",
        "Titan Mentaury or Crystal",
        "v0.1.2.1",
        "NK-EPI promotion",
    ):
        if phrase not in joined:
            raise ManifestError(f"missing P4 prohibition: {phrase}")


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    validate(data)
    state = data["conformance_state"]
    evidence = data["repository_evidence"]
    print(
        "P4 manifest valid; implementation=PARTIAL; "
        f"C2={state['repository_c2']}; repository={evidence['status']}; "
        "C3=NOT_ESTABLISHED"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
