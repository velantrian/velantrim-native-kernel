#!/usr/bin/env python3
"""Fail closed on hidden Russian-document parity coverage drift."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

MANIFEST = Path("tools/docs/bilingual-coverage-v1.json")
PROTOCOL = "nk-bilingual-coverage/1"


class CoverageError(RuntimeError):
    """Raised when the committed coverage inventory is inconsistent."""


def req(value: object, message: str) -> None:
    if not value:
        raise CoverageError(message)


def committed_russian_documents(repo: Path) -> list[str]:
    """Return Russian Markdown paths present in the committed HEAD tree only."""

    try:
        result = subprocess.run(
            [
                "git",
                "-C",
                str(repo),
                "ls-tree",
                "--full-tree",
                "--name-only",
                "-r",
                "-z",
                "HEAD",
            ],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except OSError as exc:
        raise CoverageError(f"cannot enumerate committed Russian Markdown: {exc}") from exc

    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise CoverageError(f"cannot enumerate committed Russian Markdown from HEAD: {detail}")

    try:
        paths = [
            path.decode("utf-8")
            for path in result.stdout.split(b"\0")
            if path.endswith(b".ru.md")
        ]
    except UnicodeDecodeError as exc:
        raise CoverageError("committed Russian Markdown paths are not valid UTF-8") from exc
    return sorted(paths)


def validate(repo: Path) -> None:
    try:
        data = json.loads((repo / MANIFEST).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CoverageError(f"cannot read coverage manifest: {exc}") from exc

    req(data.get("protocol") == PROTOCOL, "protocol drift")
    boundary = data.get("authority_boundary") or {}
    for key in (
        "semantic_equivalence_certified",
        "legal_equivalence_certified",
        "canon_changed",
        "runtime_changed",
    ):
        req(boundary.get(key) is False, f"authority boundary must remain false: {key}")

    actual = committed_russian_documents(repo)
    validated = data.get("validated") or []
    unvalidated = data.get("explicitly_unvalidated") or []
    validated_paths = [item.get("path") for item in validated]
    unvalidated_paths = [item.get("path") for item in unvalidated]
    req(len(validated_paths) == len(set(validated_paths)), "duplicate validated path")
    req(len(unvalidated_paths) == len(set(unvalidated_paths)), "duplicate unvalidated path")
    req(
        not (set(validated_paths) & set(unvalidated_paths)),
        "path appears in validated and unvalidated sets",
    )
    req(
        sorted(validated_paths + unvalidated_paths) == actual,
        "Russian-document coverage inventory drift",
    )

    counts = data.get("counts") or {}
    req(counts.get("russian_documents") == len(actual), "russian_documents count drift")
    req(counts.get("validated_by_config") == len(validated_paths), "validated count drift")
    req(
        counts.get("explicitly_unvalidated") == len(unvalidated_paths),
        "unvalidated count drift",
    )

    for item in validated:
        config_path = repo / item["config"]
        req(config_path.is_file(), f"missing parity config: {item['config']}")
        try:
            config_data = json.loads(config_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise CoverageError(f"invalid parity config {item['config']}: {exc}") from exc
        pairs = config_data.get("pairs", [])
        matches = [
            pair
            for pair in pairs
            if pair.get("pair_id") == item["pair_id"] and pair.get("russian") == item["path"]
        ]
        req(len(matches) == 1, f"configured coverage binding drift: {item['path']}")

    for item in unvalidated:
        req(
            isinstance(item.get("reason"), str) and item["reason"].strip(),
            f"reason required: {item.get('path')}",
        )


if __name__ == "__main__":
    try:
        validate(Path(".").resolve())
    except (CoverageError, json.JSONDecodeError) as exc:
        raise SystemExit(f"BILINGUAL_COVERAGE_INVALID: {exc}")
    print("BILINGUAL_COVERAGE_VALID (committed inventory only; translation equivalence not certified)")
