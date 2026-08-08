#!/usr/bin/env python3
"""Validate explicitly declared English/Russian documentation obligations.

This tool checks bounded structural properties only. It does not score translation
quality, compare document length, or certify semantic/legal equivalence.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

PROTOCOL = "nk-bilingual-doc-parity/1"
DEFAULT_CONFIG = Path("tools/docs/bilingual-pairs-v1.json")
PAIR_KEYS = {
    "pair_id",
    "english",
    "russian",
    "selectors",
    "shared_literals",
    "english_literals",
    "russian_literals",
    "compare_heading_levels",
    "require_single_h1",
}
HEADING_RE = re.compile(r"^[ ]{0,3}(#{1,6})[ \t]+\S")
FENCE_RE = re.compile(r"^[ ]{0,3}(`{3,}|~{3,})(.*)$")


@dataclass(frozen=True, slots=True)
class Finding:
    pair_id: str
    path: str
    message: str

    def render(self) -> str:
        return f"[{self.pair_id}] {self.path}: {self.message}"


class ConfigurationError(ValueError):
    """Raised when the parity configuration is malformed or unsafe."""


def _require_string(value: Any, *, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise ConfigurationError(f"{field} must be a non-empty string")
    return value


def _require_string_list(value: Any, *, field: str) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) or not item for item in value):
        raise ConfigurationError(f"{field} must be a list of non-empty strings")
    if len(set(value)) != len(value):
        raise ConfigurationError(f"{field} must not contain duplicate literals")
    return value


def _safe_relative_path(value: Any, *, field: str) -> str:
    raw = _require_string(value, field=field)
    path = PurePosixPath(raw)
    if path.is_absolute() or ".." in path.parts or raw.startswith("./"):
        raise ConfigurationError(f"{field} must be a repository-relative path without '..' or './'")
    if any(part in {"", "."} for part in path.parts):
        raise ConfigurationError(f"{field} contains an invalid path component")
    return path.as_posix()


def load_configuration(path: Path) -> list[dict[str, Any]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ConfigurationError(f"configuration file not found: {path}") from exc
    except UnicodeDecodeError as exc:
        raise ConfigurationError(f"configuration is not valid UTF-8: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ConfigurationError(f"configuration is not valid JSON: {exc}") from exc

    if not isinstance(data, dict):
        raise ConfigurationError("configuration root must be an object")
    if set(data) != {"protocol", "pairs"}:
        raise ConfigurationError("configuration root must contain only protocol and pairs")
    if data.get("protocol") != PROTOCOL:
        raise ConfigurationError(f"protocol must be {PROTOCOL!r}")

    raw_pairs = data.get("pairs")
    if not isinstance(raw_pairs, list) or not raw_pairs:
        raise ConfigurationError("pairs must be a non-empty list")

    pairs: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    for index, raw_pair in enumerate(raw_pairs):
        prefix = f"pairs[{index}]"
        if not isinstance(raw_pair, dict):
            raise ConfigurationError(f"{prefix} must be an object")
        unknown = set(raw_pair) - PAIR_KEYS
        missing = PAIR_KEYS - set(raw_pair)
        if unknown:
            raise ConfigurationError(f"{prefix} has unknown fields: {sorted(unknown)}")
        if missing:
            raise ConfigurationError(f"{prefix} is missing fields: {sorted(missing)}")

        pair_id = _require_string(raw_pair["pair_id"], field=f"{prefix}.pair_id")
        if pair_id in seen_ids:
            raise ConfigurationError(f"duplicate pair_id: {pair_id}")
        seen_ids.add(pair_id)

        english = _safe_relative_path(raw_pair["english"], field=f"{prefix}.english")
        russian = _safe_relative_path(raw_pair["russian"], field=f"{prefix}.russian")
        if english == russian:
            raise ConfigurationError(f"{pair_id} must use two different files")
        for document_path in (english, russian):
            if document_path in seen_paths:
                raise ConfigurationError(f"document appears in more than one pair: {document_path}")
            seen_paths.add(document_path)

        compare_heading_levels = raw_pair["compare_heading_levels"]
        require_single_h1 = raw_pair["require_single_h1"]
        if not isinstance(compare_heading_levels, bool):
            raise ConfigurationError(f"{prefix}.compare_heading_levels must be boolean")
        if not isinstance(require_single_h1, bool):
            raise ConfigurationError(f"{prefix}.require_single_h1 must be boolean")

        pairs.append(
            {
                "pair_id": pair_id,
                "english": english,
                "russian": russian,
                "selectors": _require_string_list(raw_pair["selectors"], field=f"{prefix}.selectors"),
                "shared_literals": _require_string_list(
                    raw_pair["shared_literals"], field=f"{prefix}.shared_literals"
                ),
                "english_literals": _require_string_list(
                    raw_pair["english_literals"], field=f"{prefix}.english_literals"
                ),
                "russian_literals": _require_string_list(
                    raw_pair["russian_literals"], field=f"{prefix}.russian_literals"
                ),
                "compare_heading_levels": compare_heading_levels,
                "require_single_h1": require_single_h1,
            }
        )
    return pairs


def _read_document(repo: Path, relative_path: str) -> tuple[str | None, Finding | None]:
    candidate = (repo / relative_path).resolve()
    try:
        candidate.relative_to(repo)
    except ValueError:
        return None, Finding("configuration", relative_path, "resolved path escapes repository")
    try:
        return candidate.read_text(encoding="utf-8"), None
    except FileNotFoundError:
        return None, Finding("document", relative_path, "configured document does not exist")
    except UnicodeDecodeError:
        return None, Finding("document", relative_path, "document is not valid UTF-8")
    except OSError as exc:
        return None, Finding("document", relative_path, f"document cannot be read: {exc}")


def heading_levels(markdown: str) -> tuple[int, ...]:
    """Return Markdown ATX heading levels, ignoring fenced code blocks."""

    levels: list[int] = []
    active_fence: tuple[str, int] | None = None
    for line in markdown.splitlines():
        fence_match = FENCE_RE.match(line)
        if fence_match:
            token = fence_match.group(1)
            trailing = fence_match.group(2)
            marker = (token[0], len(token))
            if active_fence is None:
                active_fence = marker
            elif (
                active_fence[0] == marker[0]
                and marker[1] >= active_fence[1]
                and not trailing.strip()
            ):
                active_fence = None
            continue
        if active_fence is not None:
            continue
        heading_match = HEADING_RE.match(line)
        if heading_match:
            levels.append(len(heading_match.group(1)))
    return tuple(levels)


def _missing_literals(text: str, literals: Iterable[str]) -> list[str]:
    return [literal for literal in literals if literal not in text]


def validate(repo: Path, config_path: Path | None = None) -> list[Finding]:
    repo = repo.resolve()
    selected_config = config_path or DEFAULT_CONFIG
    if not selected_config.is_absolute():
        selected_config = repo / selected_config

    try:
        pairs = load_configuration(selected_config)
    except ConfigurationError as exc:
        return [Finding("configuration", str(selected_config), str(exc))]

    findings: list[Finding] = []
    for pair in pairs:
        pair_id = pair["pair_id"]
        english_path = pair["english"]
        russian_path = pair["russian"]
        english, english_error = _read_document(repo, english_path)
        russian, russian_error = _read_document(repo, russian_path)
        if english_error:
            findings.append(Finding(pair_id, english_path, english_error.message))
        if russian_error:
            findings.append(Finding(pair_id, russian_path, russian_error.message))
        if english is None or russian is None:
            continue

        for selector in pair["selectors"]:
            if selector not in english:
                findings.append(Finding(pair_id, english_path, f"missing language selector literal {selector!r}"))
            if selector not in russian:
                findings.append(Finding(pair_id, russian_path, f"missing language selector literal {selector!r}"))

        for literal in _missing_literals(english, pair["shared_literals"]):
            findings.append(Finding(pair_id, english_path, f"missing shared literal {literal!r}"))
        for literal in _missing_literals(russian, pair["shared_literals"]):
            findings.append(Finding(pair_id, russian_path, f"missing shared literal {literal!r}"))
        for literal in _missing_literals(english, pair["english_literals"]):
            findings.append(Finding(pair_id, english_path, f"missing English obligation {literal!r}"))
        for literal in _missing_literals(russian, pair["russian_literals"]):
            findings.append(Finding(pair_id, russian_path, f"missing Russian obligation {literal!r}"))

        english_outline = heading_levels(english)
        russian_outline = heading_levels(russian)
        if pair["require_single_h1"]:
            if english_outline.count(1) != 1:
                findings.append(
                    Finding(pair_id, english_path, f"expected exactly one level-1 heading, found {english_outline.count(1)}")
                )
            if russian_outline.count(1) != 1:
                findings.append(
                    Finding(pair_id, russian_path, f"expected exactly one level-1 heading, found {russian_outline.count(1)}")
                )
        if pair["compare_heading_levels"] and english_outline != russian_outline:
            findings.append(
                Finding(
                    pair_id,
                    f"{english_path} ↔ {russian_path}",
                    f"heading-level outlines differ: {english_outline} != {russian_outline}",
                )
            )
    return findings


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."), help="repository root")
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG,
        help=f"configuration path relative to repo (default: {DEFAULT_CONFIG})",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    findings = validate(args.repo, args.config)
    if findings:
        for finding in findings:
            print(f"ERROR {finding.render()}")
        print(f"bilingual parity validation FAILED ({len(findings)} finding(s))")
        return 1
    print("bilingual parity validation PASS (bounded configured obligations only)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
