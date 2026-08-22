#!/usr/bin/env python3
"""Validate operator decision packages without allowing implicit runtime authorization."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

MANIFEST_PATH = Path("docs/governance/operator-decisions-v1.json")
LICENSE_EN = Path("docs/governance/LICENSE_PUBLICATION_DECISION_OPTIONS.md")
LICENSE_RU = Path("docs/governance/LICENSE_PUBLICATION_DECISION_OPTIONS.ru.md")
ADR_EN = Path("docs/adr/0024-operator-decision-package.md")
ADR_RU = Path("docs/adr/0024-operator-decision-package.ru.md")
ADR_NORMATIVE = Path("docs/adr/0024-version-reducer-referential-semantics.md")
PROJECT_STATE = Path("project-state.json")
CURRENT_STATE = Path("docs/ai/CURRENT_STATE.md")
ADR0024_OPERATOR_DECISION_REF = "issue-74-operator-decision-2026-08-22"
ADR0024_DECISION_BLOCK = "ADR-0024: ACCEPT_WITH_CHANGES\nreducer v1: IMMUTABLE HISTORICAL CONTRACT\nreducer-v2 runtime: NOT AUTHORIZED"
ADR0024_DECISION_BLOCK_SHA256 = hashlib.sha256(ADR0024_DECISION_BLOCK.encode("utf-8")).hexdigest()
ADR0024_PROVENANCE = {
    "source_type": "GITHUB_ISSUE_COMMENT",
    "repository": "velantrian/velantrim-native-kernel",
    "issue": 74,
    "comment_id": 5379224144,
    "canonical_url": "https://github.com/velantrian/velantrim-native-kernel/issues/74#issuecomment-5379224144",
    "operator_login": "velantrian",
    "decision_date": "2026-08-22",
    "decision_block_sha256": ADR0024_DECISION_BLOCK_SHA256,
}


class OperatorDecisionError(RuntimeError):
    """Raised when a decision package drifts from its bounded operator state."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise OperatorDecisionError(message)


def _load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise OperatorDecisionError(f"cannot read {path}: {exc}") from exc
    _require(isinstance(value, dict), f"{path} must contain an object")
    return value


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise OperatorDecisionError(f"cannot read {path}: {exc}") from exc


def validate(repo: Path) -> None:
    manifest = _load_json(repo / MANIFEST_PATH)
    _require(manifest.get("protocol") == "nk-operator-decisions/1", "operator decision protocol drift")
    _require(manifest.get("overall_state") == "PARTIALLY_DECIDED", "overall decision state drift")

    license_decision = manifest.get("license_publication")
    adr_decision = manifest.get("adr_0024")
    _require(isinstance(license_decision, Mapping), "license decision object required")
    _require(isinstance(adr_decision, Mapping), "ADR-0024 decision object required")

    _require(license_decision.get("state") == "PENDING_OPERATOR", "license/publication state drift")
    _require(license_decision.get("selected_option") is None, "license selected without operator decision")
    _require(license_decision.get("operator_decision_ref") is None, "license decision reference set prematurely")
    _require(license_decision.get("runtime_effect") == "NO_LICENSE_OR_PUBLICATION_POLICY_CHANGE", "license runtime effect drift")
    _require(license_decision.get("issue") == 18, "license issue binding drift")

    _require(adr_decision.get("issue") == 74 and adr_decision.get("adr") == "ADR-0024", "ADR issue binding drift")
    _require(adr_decision.get("state") == "OPERATOR_APPROVED", "ADR-0024 approval state drift")
    _require(adr_decision.get("selected_option") == "ACCEPT_WITH_CHANGES", "ADR-0024 selected option drift")
    _require(adr_decision.get("operator_decision_ref") == ADR0024_OPERATOR_DECISION_REF, "ADR-0024 operator decision reference drift")
    _require(dict(adr_decision.get("operator_decision_provenance") or {}) == ADR0024_PROVENANCE, "ADR-0024 operator decision provenance drift")
    _require(adr_decision.get("decision_date") == "2026-08-22", "ADR-0024 decision date drift")
    _require(adr_decision.get("runtime_effect") == "REDUCER_V2_NOT_AUTHORIZED", "ADR-0024 runtime effect drift")

    non_authorizations = manifest.get("non_authorizations")
    _require(isinstance(non_authorizations, list), "non-authorizations required")
    joined = " ".join(str(item) for item in non_authorizations).lower()
    for phrase in (
        "no license is selected",
        "no external contribution policy is activated",
        "reducer v2 runtime is not authorized",
        "no semantic assertion is promoted",
        "no h11 execution is authorized",
        "no final canon adoption is authorized",
        "no production authorization is granted",
    ):
        _require(phrase in joined, f"missing non-authorization: {phrase}")

    license_en = _read(repo / LICENSE_EN)
    license_ru = _read(repo / LICENSE_RU)
    adr_en = _read(repo / ADR_EN)
    adr_ru = _read(repo / ADR_RU)
    normative = _read(repo / ADR_NORMATIVE)
    current_state = _read(repo / CURRENT_STATE)
    project_state = _load_json(repo / PROJECT_STATE)

    for text, label in ((license_en, "English license package"), (license_ru, "Russian license package")):
        _require("decision_state: PENDING_OPERATOR" in text, f"{label} pending marker missing")
        _require("selected_option: null" in text, f"{label} unselected marker missing")
        for option in ("Apache License 2.0", "MIT License", "Mozilla Public License 2.0", "Business Source License 1.1", "All rights reserved", "Dual licensing"):
            _require(option.lower() in text.lower(), f"{label} missing option: {option}")
        _require("NOT LEGAL ADVICE" in text, f"{label} legal boundary missing")
        _require("package publication" in text.lower(), f"{label} package boundary missing")

    provenance_markers = (
        "operator_decision_comment_id: 5379224144",
        ADR0024_PROVENANCE["canonical_url"],
        f"operator_decision_block_sha256: {ADR0024_DECISION_BLOCK_SHA256}",
    )
    for text, label in ((adr_en, "English ADR package"), (adr_ru, "Russian ADR package")):
        _require("decision_state: OPERATOR_APPROVED" in text, f"{label} approved marker missing")
        _require("selected_option: ACCEPT_WITH_CHANGES" in text, f"{label} decision marker missing")
        _require("REDUCER_V2_NOT_AUTHORIZED" in text, f"{label} runtime boundary missing")
        _require("CONTINUE_V1" in text and "START_NEW_V2_INSTANCE" in text, f"{label} migration boundary missing")
        _require("SILENT_V1_TO_V2_UPGRADE" in text, f"{label} silent-upgrade prohibition missing")
        for marker in provenance_markers:
            _require(marker in text, f"{label} provenance marker missing: {marker}")

    for marker in (
        "**Decision status:** `ACCEPTED`",
        "**Implementation status:** `NOT_STARTED`",
        "**Operator approval:** `APPROVED`",
        "**Operator decision:** `ACCEPT_WITH_CHANGES`",
        "runtime_authorized_after_decision: false",
        "SILENT_V1_TO_V2_UPGRADE",
        "REDUCER_V2_NOT_AUTHORIZED",
    ):
        _require(marker in normative or marker in adr_en, f"ADR-0024 accepted-boundary marker missing: {marker}")

    issue74 = ((project_state.get("issues") or {}).get("74") or {})
    _require(issue74.get("state") == "CLOSED", "Issue #74 current state drift")
    _require(issue74.get("state_reason") == "COMPLETED", "Issue #74 completion reason drift")
    issue74_meaning = str(issue74.get("meaning", ""))
    for marker in (
        "ACCEPTED / ACCEPT_WITH_CHANGES",
        "immutable historical contract",
        "reducer-v1-bounded",
        "NOT_STARTED",
        "NOT_AUTHORIZED",
    ):
        _require(marker in issue74_meaning, f"Issue #74 current-truth boundary drift: {marker}")

    for marker in (
        "adr_0024: ACCEPTED / ACCEPT_WITH_CHANGES",
        "adr_0024_implementation: NOT_STARTED",
        "reducer_v2_runtime: NOT_AUTHORIZED",
        "reducer v1: IMMUTABLE HISTORICAL CONTRACT",
        "existing P1-C5 evidence: REDUCER-V1-BOUNDED",
        "H11 execution",
        "Final Canon",
        "runtime thaw",
        "production",
        "reinterpretation of historical evidence",
    ):
        _require(marker in current_state, f"CURRENT_STATE ADR-0024 boundary drift: {marker}")

    h11 = project_state["tracks"]["long_horizon_research"]["post_blueprint_validation"]["residual_a10_validation_plan"]["h11_execution_admission"]
    _require(h11.get("status") == "BLOCKED", "H11 status drift")
    _require(h11.get("h11_outcome") == "NOT_TESTED", "H11 outcome drift")
    _require(h11.get("implementation_authorized") is False and h11.get("execution_authorized") is False, "H11 authorization drift")
    _require(h11.get("runtime_expansion") == "FROZEN" and h11.get("product_runtime_thaw") is False, "runtime freeze drift")
    _require(h11.get("final_canon") == "DEFERRED / NOT_AUTHORIZED", "Final Canon drift")
    _require(h11.get("production_authorized") is False, "production authorization drift")

    combined = " ".join((license_en, license_ru, adr_en, adr_ru, normative, current_state)).lower()
    for forbidden in (
        "selected_option: apache",
        "selected_option: mit",
        "selected_option: mpl",
        "runtime_effect: reducer_v2_authorized",
        "runtime_authorized_after_decision: true",
        "reducer_v2_runtime: authorized",
    ):
        _require(forbidden not in combined, f"forbidden implicit authorization marker: {forbidden}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    validate(args.repo.resolve())
    print("Operator decision validation passed; ADR-0024=ACCEPT_WITH_CHANGES; issue74=CLOSED/COMPLETED; provenance=pinned; reducer-v2-runtime=NOT_AUTHORIZED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
