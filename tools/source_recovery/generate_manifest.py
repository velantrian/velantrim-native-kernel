#!/usr/bin/env python3
"""Generate a deterministic manifest for an unverified recovered-source candidate.

This utility inventories bytes. It never authenticates a candidate and always emits
``snapshot_status = UNVERIFIED_CANDIDATE``. Operator provenance review is a separate
manual decision.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

MANIFEST_VERSION = "1.1"
GENERATOR_VERSION = "1"
BUFFER_SIZE = 1024 * 1024


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(BUFFER_SIZE):
            digest.update(chunk)
    return digest.hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def relative_posix(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def classify_role(relative_path: str) -> str:
    lowered = relative_path.lower()
    name = Path(relative_path).name.lower()

    if lowered.startswith(("tests/", "test/")) or name.startswith("test_") or name.endswith("_test.py"):
        return "test"
    if "benchmark" in lowered or name.startswith(("bench_", "benchmark_")):
        return "benchmark"
    if name in {
        "requirements.txt",
        "requirements-dev.txt",
        "pyproject.toml",
        "poetry.lock",
        "pdm.lock",
        "pipfile",
        "pipfile.lock",
        "setup.py",
        "setup.cfg",
        "tox.ini",
    }:
        return "environment"
    if path_is_runtime(relative_path):
        return "runtime"
    return "other"


def path_is_runtime(relative_path: str) -> bool:
    path = Path(relative_path)
    return path.suffix.lower() == ".py" and not any(part.lower() in {"tests", "test", "benchmarks"} for part in path.parts)


def ensure_no_symlinks(root: Path) -> None:
    for current_root, dir_names, file_names in os.walk(root, followlinks=False):
        current = Path(current_root)
        for name in [*dir_names, *file_names]:
            candidate = current / name
            if candidate.is_symlink():
                raise ValueError(f"symlink is not allowed in a candidate snapshot: {candidate}")


def iter_regular_files(root: Path, excluded: Iterable[Path]) -> list[Path]:
    excluded_resolved = {path.resolve() for path in excluded}
    files: list[Path] = []

    ensure_no_symlinks(root)
    for current_root, _, file_names in os.walk(root, followlinks=False):
        current = Path(current_root)
        for name in file_names:
            candidate = current / name
            resolved = candidate.resolve(strict=True)
            if resolved in excluded_resolved:
                continue
            if not candidate.is_file():
                raise ValueError(f"non-regular file is not allowed: {candidate}")
            files.append(candidate)

    files.sort(key=lambda item: relative_posix(item, root))
    if not files:
        raise ValueError("candidate directory contains no regular files")
    return files


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


def build_manifest(args: argparse.Namespace) -> dict[str, object]:
    source_dir = args.source_dir.resolve(strict=True)
    if not source_dir.is_dir():
        raise ValueError(f"source directory is not a directory: {source_dir}")

    output = args.output.resolve()
    excluded = [output]
    if args.test_node_ids:
        excluded.append(args.test_node_ids.resolve())
    if args.archive:
        excluded.append(args.archive.resolve())

    files = []
    for path in iter_regular_files(source_dir, excluded):
        rel = relative_posix(path, source_dir)
        files.append(
            {
                "original_path": rel,
                "repository_path": None,
                "source_sha256": sha256_file(path),
                "repository_sha256": None,
                "size_bytes": path.stat().st_size,
                "role": classify_role(rel),
                "transformation": "UNVERIFIED",
            }
        )

    source_archive: dict[str, object] | None = None
    if args.archive:
        archive = args.archive.resolve(strict=True)
        if not archive.is_file() or archive.is_symlink():
            raise ValueError("archive must be a non-symlink regular file")
        source_archive = {
            "filename": archive.name,
            "sha256": sha256_file(archive),
            "size_bytes": archive.stat().st_size,
        }

    test_inventory: dict[str, object] = {
        "declared_count": args.declared_test_count,
        "collected_count": None,
        "node_ids_sha256": None,
        "node_ids_artifact": None,
        "original_command": args.original_test_command,
    }
    if args.test_node_ids:
        node_ids_path = args.test_node_ids.resolve(strict=True)
        if not node_ids_path.is_file() or node_ids_path.is_symlink():
            raise ValueError("test node-ID artifact must be a non-symlink regular file")
        node_ids, node_ids_hash = normalize_test_node_ids(node_ids_path)
        test_inventory.update(
            {
                "collected_count": len(node_ids),
                "node_ids_sha256": node_ids_hash,
                "node_ids_artifact": node_ids_path.name,
            }
        )

    generated_at = utc_now()
    return {
        "manifest_version": MANIFEST_VERSION,
        "snapshot_id": args.snapshot_id,
        "snapshot_status": "UNVERIFIED_CANDIDATE",
        "generated_at": generated_at,
        "generator": {
            "name": "tools/source_recovery/generate_manifest.py",
            "version": GENERATOR_VERSION,
        },
        "provenance": {
            "recovered_from": args.recovered_from,
            "recovered_by": args.recovered_by,
            "recovered_at": args.recovered_at or generated_at,
            "chain_of_custody_notes": args.chain_of_custody_notes,
            "operator_decision": "PENDING",
        },
        "source_archive": source_archive,
        "files": files,
        "test_inventory": test_inventory,
        "environment": {
            "original_python": args.original_python,
            "python_implementation": args.python_implementation,
            "os": args.original_os,
            "architecture": args.original_architecture,
            "locale": args.original_locale,
            "timezone": args.original_timezone,
            "dependency_lock_path": None,
            "dependency_lock_sha256": None,
            "environment_notes": args.environment_notes,
        },
        "repository": {"import_pr": None, "import_commit": None},
        "authenticity": {
            "decision": "PENDING",
            "decided_by": None,
            "decided_at": None,
            "rationale": None,
        },
    }


def write_json_atomic(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=False) + "\n"

    descriptor, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temp_path = Path(temp_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(rendered)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, path)
    except Exception:
        temp_path.unlink(missing_ok=True)
        raise


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_dir", type=Path, help="read-only extracted candidate directory")
    parser.add_argument("--output", type=Path, required=True, help="manifest output path")
    parser.add_argument("--archive", type=Path, help="original immutable archive to hash")
    parser.add_argument("--snapshot-id", default="v0.1.2.1")
    parser.add_argument("--recovered-from", required=True)
    parser.add_argument("--recovered-by", required=True)
    parser.add_argument("--recovered-at", help="ISO-8601 timestamp; defaults to generation time")
    parser.add_argument("--chain-of-custody-notes")
    parser.add_argument("--test-node-ids", type=Path, help="UTF-8 file with one collected node ID per line")
    parser.add_argument("--declared-test-count", type=int, default=44)
    parser.add_argument("--original-test-command")
    parser.add_argument("--original-python")
    parser.add_argument("--python-implementation")
    parser.add_argument("--original-os")
    parser.add_argument("--original-architecture")
    parser.add_argument("--original-locale")
    parser.add_argument("--original-timezone")
    parser.add_argument("--environment-notes")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        manifest = build_manifest(args)
        write_json_atomic(args.output.resolve(), manifest)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print(f"wrote unverified candidate manifest: {args.output}")
    print("status remains UNVERIFIED_CANDIDATE; byte inventory is not proof of authenticity")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
