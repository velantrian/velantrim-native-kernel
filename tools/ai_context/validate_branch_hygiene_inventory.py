#!/usr/bin/env python3
"""Validate bounded branch-hygiene inventory without granting deletion authority."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

MANIFEST = Path("evidence/branch-hygiene-inventory-v1.json")
PROTOCOL = "nk-branch-hygiene-inventory/1"
STATUS = "READ_ONLY_CLASSIFICATION_NO_DELETION_AUTHORITY"
REQUIRED_PROTECTED = {
    "archive/bootstrap-v0.1.2.1-docs-lineage",
    "bootstrap/research-kernel-v0.1.2.1",
}
FORBIDDEN_CLASSES = {"SAFE_DELETE", "DELETE", "AUTO_DELETE", "DELETION_AUTHORIZED"}


class BranchHygieneInventoryError(RuntimeError):
    pass


def _require(value: bool, message: str) -> None:
    if not value:
        raise BranchHygieneInventoryError(message)


def validate(repo: Path, manifest: Path | None = None) -> None:
    path = manifest or repo / MANIFEST
    data = json.loads(path.read_text(encoding="utf-8"))
    _require(data.get("protocol") == PROTOCOL, "protocol drift")
    _require(data.get("status") == STATUS, "status drift")

    boundary = data.get("authority_boundary")
    _require(isinstance(boundary, dict), "authority_boundary required")
    for key in (
        "h11_outcome_changed",
        "runtime_authorized",
        "canon_authorized",
        "production_authorized",
        "branch_deletion_authorized",
        "auto_delete_authorized",
    ):
        _require(boundary.get(key) is False, f"authority boundary must remain false: {key}")

    entries = data.get("entries")
    _require(isinstance(entries, list) and entries, "entries must be non-empty")
    refs = [item.get("ref") for item in entries]
    _require(all(isinstance(ref, str) and ref for ref in refs), "every ref must be non-empty")
    _require(len(set(refs)) == len(refs), "duplicate branch ref")

    classes = [item.get("classification") for item in entries]
    _require(not any(c in FORBIDDEN_CLASSES for c in classes), "deletion-authorizing class forbidden")

    actual = dict(Counter(classes))
    _require(actual == data.get("classification_counts"), "classification_counts mismatch")
    _require(data.get("observed_non_main_count") == len(entries), "non-main count mismatch")
    _require(data.get("observed_branch_count_including_main") == len(entries) + 1, "total branch count mismatch")

    by_ref = {item["ref"]: item for item in entries}
    for ref in REQUIRED_PROTECTED:
        _require(ref in by_ref, f"required protected ref missing: {ref}")
        _require(by_ref[ref].get("classification") == "KEEP_PROTECTED", f"protected ref class drift: {ref}")


if __name__ == "__main__":
    try:
        validate(Path("."))
    except (BranchHygieneInventoryError, json.JSONDecodeError) as exc:
        raise SystemExit(f"BRANCH_HYGIENE_INVENTORY_INVALID: {exc}")
    print("BRANCH_HYGIENE_INVENTORY_VALID")
