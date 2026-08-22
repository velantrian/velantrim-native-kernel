#!/usr/bin/env python3
"""Validate operator decision packages without allowing implicit runtime authorization."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping

MANIFEST_PATH = Path("docs/governance/operator-decisions-v1.json")
LICENSE_EN = Path("docs/governance/LICENSE_PUBLICATION_DECISION_OPTIONS.md")
LICENSE_RU = Path("docs/governance/LICENSE_PUBLICATION_DECISION_OPTIONS.ru.md")
ADR_EN = Path("docs/adr/0024-operator-decision-package.md")
ADR_RU = Path("docs/adr/0024-operator-decision-package.ru.md")
ADR_NORMATIVE = Path("docs/adr/0024-version-reducer-referential-semantics.md")


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
    _require(bool(adr_decision.get("operator_decision_ref")), "ADR-0024 decision reference required")
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

    for text, label in ((license_en, "English license package"), (license_ru, "Russian license package")):
        _require("decision_state: PENDING_OPERATOR" in text, f"{label} pending marker missing")
        _require("selected_option: null" in text, f"{label} unselected marker missing")
        for option in (
            "Apache License 2.0",
            "MIT License",
            "Mozilla Public License 2.0",
            "Business Source License 1.1",
            "All rights reserved",
            "Dual licensing",
        ):
            _require(option.lower() in text.lower(), f"{label} missing option: {option}")
        _require("NOT LEGAL ADVICE" in text, f"{label} legal boundary missing")
        _require("package publication" in text.lower(), f"{label} package boundary missing")

    for text, label in ((adr_en, "English ADR package"), (adr_ru, "Russian ADR package")):
        _require("decision_state: OPERATOR_APPROVED" in text, f"{label} approved marker missing")
        _require("selected_option: ACCEPT_WITH_CHANGES" in text, f"{label} decision marker missing")
        _require("REDUCER_V2_NOT_AUTHORIZED" in text, f"{label} runtime boundary missing")
        _require("CONTINUE_V1" in text and "START_NEW_V2_INSTANCE" in text, f"{label} migration boundary missing")
        _require("SILENT_V1_TO_V2_UPGRADE" in text, f"{label} silent-upgrade prohibition missing")

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

    combined = " ".join((license_en, license_ru, adr_en, adr_ru, normative)).lower()
    for forbidden in (
        "selected_option: apache",
        "selected_option: mit",
        "selected_option: mpl",
        "runtime_effect: reducer_v2_authorized",
        "runtime_authorized_after_decision: true",
    ):
        _require(forbidden not in combined, f"forbidden implicit authorization marker: {forbidden}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    validate(args.repo.resolve())
    print("Operator decision validation passed; ADR-0024=ACCEPT_WITH_CHANGES; reducer-v2-runtime=NOT_AUTHORIZED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
