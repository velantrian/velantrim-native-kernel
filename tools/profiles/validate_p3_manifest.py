from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "profiles" / "postgresql-reference-v0" / "p3-manifest.json"


class ManifestError(ValueError):
    pass


def validate(data: dict[str, object]) -> None:
    expected = {
        "manifest_version": "nk-p3-implementation-manifest/1",
        "profile_id": "native-kernel/postgresql-reference",
        "profile_version": "0.3-p3",
        "evidence_lineage": "clean/postgresql-reference/0.1",
        "phase": "P3",
        "implementation_status": "PARTIAL",
        "kernel_runtime_conformance": "UNSUPPORTED",
        "c1": "NOT_ESTABLISHED",
        "c2": "NOT_ESTABLISHED",
        "c3": "NOT_ESTABLISHED",
    }
    for key, value in expected.items():
        if data.get(key) != value:
            raise ManifestError(f"{key} must remain {value!r}")

    language = data.get("language_profile")
    if not isinstance(language, dict):
        raise ManifestError("language_profile must be an object")
    if language.get("semantic_helper_dependency_policy") != "STANDARD_LIBRARY_ONLY":
        raise ManifestError("semantic helper dependency boundary changed")
    if language.get("postgresql_driver") != "psycopg>=3.3,<3.4":
        raise ManifestError("PostgreSQL driver range drifted")

    postgres = data.get("postgresql_profile")
    if not isinstance(postgres, dict):
        raise ManifestError("postgresql_profile must be an object")
    if postgres.get("supported_major_versions") != [16, 17, 18]:
        raise ManifestError("supported PostgreSQL matrix drifted")
    if postgres.get("ci_service_versions") != [16, 18]:
        raise ManifestError("CI PostgreSQL matrix drifted")
    if postgres.get("projection_publish_guard") != "OPTIMISTIC_INSTANCE_HEAD_COMPARE_UNDER_ROW_LOCK":
        raise ManifestError("stale projection publication guard changed")

    limits = data.get("receipt_limits")
    if not isinstance(limits, list):
        raise ManifestError("receipt_limits must be a list")
    joined_limits = "\n".join(str(item) for item in limits)
    for phrase in ("no truth", "no external authenticity", "no physical deletion", "no C1 C2 C3"):
        if phrase not in joined_limits:
            raise ManifestError(f"missing Receipt limit: {phrase}")

    validation = data.get("local_validation")
    if not isinstance(validation, dict):
        raise ManifestError("local_validation must be an object")
    if validation.get("integration_result") not in {
        "NOT_RUN_NO_POSTGRESQL",
        "PASS_LOCAL_POSTGRESQL",
        "PASS_REPOSITORY_CI",
    }:
        raise ManifestError("invalid integration evidence status")
    repository_status = validation.get("repository_ci")
    if repository_status not in {"NOT_RECORDED", "PASS_PREVIOUS_HEAD", "PASS"}:
        raise ManifestError("invalid repository CI evidence status")
    if repository_status in {"PASS_PREVIOUS_HEAD", "PASS"} and validation.get(
        "integration_result"
    ) != "PASS_REPOSITORY_CI":
        raise ManifestError("repository PASS requires repository integration evidence")

    support = data.get("assertion_support_policy")
    if not isinstance(support, dict) or support.get("reported_runtime_support") != "UNSUPPORTED":
        raise ManifestError("P3 cannot promote assertion-level runtime support")

    issue1 = data.get("issue_1_boundary")
    if not isinstance(issue1, dict) or issue1.get("may_claim_recovery") is not False:
        raise ManifestError("Issue #1 recovery boundary changed")

    forbidden = data.get("forbidden_in_p3")
    if not isinstance(forbidden, list):
        raise ManifestError("forbidden_in_p3 must be a list")
    joined = "\n".join(str(item) for item in forbidden)
    for phrase in (
        "physical or cryptographic deletion",
        "network API",
        "P4 assertion-level conformance",
        "P5 SQLite",
        "C1, C2 or C3",
        "Titan, Mentaury or Crystal",
    ):
        if phrase not in joined:
            raise ManifestError(f"missing P3 prohibition: {phrase}")


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    validate(data)
    print(
        "P3 manifest valid; phase=P3; implementation=PARTIAL; "
        f"integration={data['local_validation']['integration_result']}; "
        "runtime_conformance=UNSUPPORTED"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
