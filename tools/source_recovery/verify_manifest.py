#!/usr/bin/env python3
"""Verify a recovered-source manifest against candidate bytes.

The verifier checks consistency, paths, sizes, SHA-256 values, archive bytes, and
optional test node-ID inventory. A successful result proves only that the bytes
match the manifest. It does not prove historical authenticity.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path, PurePosixPath
from typing import Any

MANIFEST_VERSION = "1.1"
BUFFER_SIZE = 1024 * 1024
ALLOWED_SNAPSHOT_STATUSES = {"UNVERIFIED_CANDIDATE", "AUTHENTIC_RECOVERED"}
ALLOWED_TRANSFORMATIONS = {
    "UNVERIFIED",
    "NONE",
    "LINE_ENDING_NORMALIZATION",
    "PATH_RELOCATION_ONLY",
    "REPOSITORY_WRAPPER_ONLY",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(BUFFER_SIZE):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_test_node_ids(path: Path) -> tuple[list[str], str]:
    values: list[str] = []
    seen: set[str] = set()
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        value = raw_line.strip()
        if not value:
            continue
        if value in seen:
            raise ValueError(f"duplicate test node ID: {value}")
        seen.add(value)
        values.append(value)
    if not values:
        raise ValueError("test node-ID artifact contains no non-empty IDs")
    canonical = ("\n".join(values) + "\n").encode("utf-8")
    return values, hashlib.sha256(canonical).hexdigest()


def safe_relative_path(value: Any) -> PurePosixPath:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("original_path must be a non-empty string")
    if "\\" in value:
        raise ValueError(f"backslashes are not allowed in manifest paths: {value}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise ValueError(f"unsafe manifest path: {value}")
    return path


def ensure_path_without_symlink(root: Path, relative: PurePosixPath) -> Path:
    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError(f"symlink is not allowed: {current}")
    resolved = current.resolve(strict=True)
    resolved.relative_to(root.resolve(strict=True))
    if not resolved.is_file():
        raise ValueError(f"not a regular file: {resolved}")
    return resolved


def require_dict(payload: Any, field: str, errors: list[str]) -> dict[str, Any]:
    value = payload.get(field) if isinstance(payload, dict) else None
    if not isinstance(value, dict):
        errors.append(f"{field} must be an object")
        return {}
    return value


def validate_governance(manifest: dict[str, Any], errors: list[str]) -> None:
    status = manifest.get("snapshot_status")
    if status not in ALLOWED_SNAPSHOT_STATUSES:
        errors.append(f"unsupported snapshot_status: {status!r}")

    provenance = require_dict(manifest, "provenance", errors)
    authenticity = require_dict(manifest, "authenticity", errors)

    operator_decision = provenance.get("operator_decision")
    authenticity_decision = authenticity.get("decision")

    if status == "UNVERIFIED_CANDIDATE":
        if operator_decision not in {None, "PENDING"}:
            errors.append("UNVERIFIED_CANDIDATE must not carry an approved provenance decision")
        if authenticity_decision not in {None, "PENDING"}:
            errors.append("UNVERIFIED_CANDIDATE must not carry an authenticity approval")

    if status == "AUTHENTIC_RECOVERED":
        if operator_decision != "APPROVED":
            errors.append("AUTHENTIC_RECOVERED requires provenance.operator_decision = APPROVED")
        if authenticity_decision != "APPROVED":
            errors.append("AUTHENTIC_RECOVERED requires authenticity.decision = APPROVED")
        for key in ("decided_by", "decided_at", "rationale"):
            if not authenticity.get(key):
                errors.append(f"AUTHENTIC_RECOVERED requires authenticity.{key}")


def validate_archive(manifest: dict[str, Any], archive: Path | None, errors: list[str]) -> None:
    record = manifest.get("source_archive")
    if record is None:
        if archive is not None:
            errors.append("--archive was provided but manifest source_archive is null")
        return
    if not isinstance(record, dict):
        errors.append("source_archive must be null or an object")
        return
    if archive is None:
        errors.append("manifest contains source_archive; pass --archive to verify it")
        return

    try:
        resolved = archive.resolve(strict=True)
        if archive.is_symlink() or not resolved.is_file():
            raise ValueError("archive must be a non-symlink regular file")
        expected_size = record.get("size_bytes")
        expected_hash = record.get("sha256")
        if resolved.stat().st_size != expected_size:
            errors.append(
                f"archive size mismatch: expected {expected_size}, got {resolved.stat().st_size}"
            )
        actual_hash = sha256_file(resolved)
        if actual_hash != expected_hash:
            errors.append(f"archive SHA-256 mismatch: expected {expected_hash}, got {actual_hash}")
    except (OSError, ValueError) as exc:
        errors.append(f"archive verification failed: {exc}")


def resolve_test_node_artifact(
    source_dir: Path,
    test_inventory: dict[str, Any],
    cli_path: Path | None,
) -> Path | None:
    if cli_path is not None:
        return cli_path
    artifact = test_inventory.get("node_ids_artifact")
    if not artifact:
        return None
    relative = safe_relative_path(artifact)
    return ensure_path_without_symlink(source_dir, relative)


def validate_test_inventory(
    manifest: dict[str, Any],
    source_dir: Path,
    cli_path: Path | None,
    errors: list[str],
) -> None:
    inventory = require_dict(manifest, "test_inventory", errors)
    expected_hash = inventory.get("node_ids_sha256")
    expected_count = inventory.get("collected_count")

    try:
        artifact = resolve_test_node_artifact(source_dir, inventory, cli_path)
    except (OSError, ValueError) as exc:
        errors.append(f"test node-ID artifact resolution failed: {exc}")
        return

    if expected_hash is None and expected_count is None:
        if artifact is not None:
            errors.append("test node-ID artifact supplied but manifest has no collected inventory")
        return

    if artifact is None:
        errors.append("manifest contains collected test inventory; provide --test-node-ids or node_ids_artifact")
        return

    try:
        resolved = artifact.resolve(strict=True)
        if artifact.is_symlink() or not resolved.is_file():
            raise ValueError("test node-ID artifact must be a non-symlink regular file")
        values, actual_hash = normalize_test_node_ids(resolved)
        if len(values) != expected_count:
            errors.append(f"test node-ID count mismatch: expected {expected_count}, got {len(values)}")
        if actual_hash != expected_hash:
            errors.append(f"test node-ID SHA-256 mismatch: expected {expected_hash}, got {actual_hash}")
    except (OSError, UnicodeError, ValueError) as exc:
        errors.append(f"test inventory verification failed: {exc}")


def validate_files(manifest: dict[str, Any], source_dir: Path, errors: list[str]) -> int:
    records = manifest.get("files")
    if not isinstance(records, list) or not records:
        errors.append("files must be a non-empty array")
        return 0

    seen: set[str] = set()
    verified = 0
    for index, record in enumerate(records):
        prefix = f"files[{index}]"
        if not isinstance(record, dict):
            errors.append(f"{prefix} must be an object")
            continue
        try:
            relative = safe_relative_path(record.get("original_path"))
        except ValueError as exc:
            errors.append(f"{prefix}: {exc}")
            continue

        key = relative.as_posix()
        if key in seen:
            errors.append(f"duplicate original_path: {key}")
            continue
        seen.add(key)

        transformation = record.get("transformation")
        if transformation not in ALLOWED_TRANSFORMATIONS:
            errors.append(f"{prefix}: unsupported transformation {transformation!r}")

        try:
            path = ensure_path_without_symlink(source_dir, relative)
            expected_size = record.get("size_bytes")
            expected_hash = record.get("source_sha256")
            actual_size = path.stat().st_size
            actual_hash = sha256_file(path)
            if actual_size != expected_size:
                errors.append(f"{key}: size mismatch; expected {expected_size}, got {actual_size}")
            if actual_hash != expected_hash:
                errors.append(f"{key}: SHA-256 mismatch; expected {expected_hash}, got {actual_hash}")
            if actual_size == expected_size and actual_hash == expected_hash:
                verified += 1
        except (OSError, ValueError) as exc:
            errors.append(f"{key}: verification failed: {exc}")
    return verified


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("source_dir", type=Path)
    parser.add_argument("--archive", type=Path)
    parser.add_argument("--test-node-ids", type=Path)
    parser.add_argument("--json", action="store_true", help="emit machine-readable summary")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    errors: list[str] = []

    try:
        manifest_path = args.manifest.resolve(strict=True)
        source_dir = args.source_dir.resolve(strict=True)
        if manifest_path.is_symlink() or not manifest_path.is_file():
            raise ValueError("manifest must be a non-symlink regular file")
        if source_dir.is_symlink() or not source_dir.is_dir():
            raise ValueError("source_dir must be a non-symlink directory")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if not isinstance(manifest, dict):
            raise ValueError("manifest root must be an object")
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if manifest.get("manifest_version") != MANIFEST_VERSION:
        errors.append(
            f"manifest_version must be {MANIFEST_VERSION}, got {manifest.get('manifest_version')!r}"
        )

    validate_governance(manifest, errors)
    verified_files = validate_files(manifest, source_dir, errors)
    validate_archive(manifest, args.archive, errors)
    validate_test_inventory(manifest, source_dir, args.test_node_ids, errors)

    summary = {
        "ok": not errors,
        "snapshot_id": manifest.get("snapshot_id"),
        "snapshot_status": manifest.get("snapshot_status"),
        "verified_files": verified_files,
        "declared_files": len(manifest.get("files", [])) if isinstance(manifest.get("files"), list) else 0,
        "errors": errors,
        "authenticity_proven": False,
    }

    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    elif errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
    else:
        print(f"verified {verified_files} candidate files against manifest")
        print("byte consistency passed; historical authenticity is NOT proven")

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
