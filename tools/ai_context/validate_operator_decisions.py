#!/usr/bin/env python3
"""Validate that prepared operator decision packages remain pending and non-authorizing."""
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


class OperatorDecisionError(RuntimeError):
    """Raised when a decision package silently selects or authorizes work."""


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


def _validate_decision(
    decision: Mapping[str, Any],
    *,
    label: str,
    runtime_effect: str,
) -> None:
    _require(decision.get("state") == "PENDING_OPERATOR", f"{label} state drift")
    _require(decision.get("selected_option") is None, f"{label} option selected without operator decision")
    _require(decision.get("operator_decision_ref") is None, f"{label} decision reference set prematurely")
    _require(decision.get("runtime_effect") == runtime_effect, f"{label} runtime effect drift")


def validate(repo: Path) -> None:
    manifest = _load_json(repo / MANIFEST_PATH)
    _require(manifest.get("protocol") == "nk-operator-decisions/1", "operator decision protocol drift")
    _require(manifest.get("overall_state") == "PENDING_OPERATOR", "overall decision state drift")

    license_decision = manifest.get("license_publication")
    adr_decision = manifest.get("adr_0024")
    _require(isinstance(license_decision, Mapping), "license decision object required")
    _require(isinstance(adr_decision, Mapping), "ADR-0024 decision object required")
    _validate_decision(
        license_decision,
        label="license/publication",
        runtime_effect="NO_LICENSE_OR_PUBLICATION_POLICY_CHANGE",
    )
    _validate_decision(
        adr_decision,
        label="ADR-0024",
        runtime_effect="REDUCER_V2_NOT_AUTHORIZED",
    )
    _require(license_decision.get("issue") == 18, "license issue binding drift")
    _require(adr_decision.get("issue") == 74 and adr_decision.get("adr") == "ADR-0024", "ADR issue binding drift")

    non_authorizations = manifest.get("non_authorizations")
    _require(isinstance(non_authorizations, list), "non-authorizations required")
    joined = " ".join(str(item) for item in non_authorizations).lower()
    for phrase in (
        "no license is selected",
        "no external contribution policy is activated",
        "adr-0024 remains proposed",
        "reducer v2 runtime is not authorized",
        "no semantic assertion is promoted",
        "no production authorization is granted",
    ):
        _require(phrase in joined, f"missing non-authorization: {phrase}")

    license_en = _read(repo / LICENSE_EN)
    license_ru = _read(repo / LICENSE_RU)
    adr_en = _read(repo / ADR_EN)
    adr_ru = _read(repo / ADR_RU)

    for text, label in (
        (license_en, "English license package"),
        (license_ru, "Russian license package"),
        (adr_en, "English ADR package"),
        (adr_ru, "Russian ADR package"),
    ):
        _require("decision_state: PENDING_OPERATOR" in text, f"{label} pending marker missing")
        _require("selected_option: null" in text, f"{label} unselected marker missing")

    for text, label in ((license_en, "English license package"), (license_ru, "Russian license package")):
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
        for option in ("ACCEPT", "ACCEPT_WITH_CHANGES", "REVISE", "REJECT"):
            _require(option in text, f"{label} missing decision option: {option}")
        _require("REDUCER_V2_NOT_AUTHORIZED" in text, f"{label} runtime boundary missing")
        _require("CONTINUE_V1" in text and "START_NEW_V2_INSTANCE" in text, f"{label} migration boundary missing")
        _require("SILENT_V1_TO_V2_UPGRADE" in text, f"{label} silent-upgrade prohibition missing")

    combined = " ".join((license_en, license_ru, adr_en, adr_ru)).lower()
    for forbidden in (
        "decision_state: accepted",
        "selected_option: apache",
        "selected_option: mit",
        "selected_option: mpl",
        "runtime_effect: reducer_v2_authorized",
    ):
        _require(forbidden not in combined, f"forbidden implicit decision marker: {forbidden}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    validate(args.repo.resolve())
    print("Operator decision packages validation passed; state=PENDING_OPERATOR; selections=0; runtime_authorizations=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
