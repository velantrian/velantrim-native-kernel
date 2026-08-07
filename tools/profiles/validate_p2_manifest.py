from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "profiles" / "postgresql-reference-v0" / "p2-manifest.json"


class ManifestError(ValueError):
    pass


def validate(data: dict[str, object]) -> None:
    expected = {
        "manifest_version": "nk-p2-implementation-manifest/1",
        "profile_id": "native-kernel/postgresql-reference",
        "profile_version": "0.2-p2",
        "evidence_lineage": "clean/postgresql-reference/0.1",
        "phase": "P2",
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
    if language.get("p1_dependency_policy") != "STANDARD_LIBRARY_ONLY":
        raise ManifestError("P1 dependency boundary changed")
    if language.get("p2_driver") != "psycopg>=3.3,<3.4":
        raise ManifestError("P2 driver range drifted")

    postgres = data.get("postgresql_profile")
    if not isinstance(postgres, dict):
        raise ManifestError("postgresql_profile must be an object")
    if postgres.get("supported_major_versions") != [16, 17, 18]:
        raise ManifestError("supported PostgreSQL matrix drifted")
    if postgres.get("ci_service_versions") != [16, 18]:
        raise ManifestError("CI PostgreSQL matrix drifted")

    validation = data.get("local_validation")
    if not isinstance(validation, dict):
        raise ManifestError("local_validation must be an object")
    if validation.get("integration_result") not in {
        "NOT_RUN_NO_POSTGRESQL",
        "PASS_LOCAL_POSTGRESQL",
        "PASS_REPOSITORY_CI",
    }:
        raise ManifestError("invalid integration evidence status")
    if validation.get("repository_ci") == "PASS" and validation.get("integration_result") != "PASS_REPOSITORY_CI":
        raise ManifestError("repository PASS requires repository integration evidence")

    support = data.get("assertion_support_policy")
    if not isinstance(support, dict) or support.get("reported_runtime_support") != "UNSUPPORTED":
        raise ManifestError("P2 cannot promote assertion-level runtime support")

    issue1 = data.get("issue_1_boundary")
    if not isinstance(issue1, dict) or issue1.get("may_claim_recovery") is not False:
        raise ManifestError("Issue #1 recovery boundary changed")

    forbidden = data.get("forbidden_in_p2")
    if not isinstance(forbidden, list):
        raise ManifestError("forbidden_in_p2 must be a list")
    joined = "\n".join(str(item) for item in forbidden)
    for phrase in (
        "projection persistence",
        "network API",
        "C1, C2 or C3",
        "Titan, Mentaury or Crystal",
    ):
        if phrase not in joined:
            raise ManifestError(f"missing P2 prohibition: {phrase}")


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    validate(data)
    print(
        "P2 manifest valid; phase=P2; implementation=PARTIAL; "
        f"integration={data['local_validation']['integration_result']}; "
        "runtime_conformance=UNSUPPORTED"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
