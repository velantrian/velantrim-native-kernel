#!/usr/bin/env python3
"""Verify repository-resident Native Kernel evidence bundles."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path
from typing import Any


class EvidenceBundleError(RuntimeError):
    """Raised when an evidence bundle fails closed validation."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise EvidenceBundleError(message)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise EvidenceBundleError(f"cannot read JSON {path}: {exc}") from exc
    _require(isinstance(value, dict), f"{path}: top-level JSON must be an object")
    return value


def _resolve_inside(repo: Path, relative: str) -> Path:
    path = (repo / relative).resolve()
    try:
        path.relative_to(repo.resolve())
    except ValueError as exc:
        raise EvidenceBundleError(f"evidence path escapes repository: {relative}") from exc
    return path


def validate(manifest: dict[str, Any], *, repo: Path) -> None:
    _require(manifest.get("protocol") == "nk-evidence-bundle/1", "unsupported evidence bundle protocol")
    _require(manifest.get("repository") == "velantrian/velantrim-native-kernel", "wrong repository identity")

    plan = manifest.get("plan")
    _require(isinstance(plan, dict), "plan object required")
    _require(plan.get("id") == "native-kernel/c5-bounded-rehearsal-v1", "unexpected plan id")
    _require(plan.get("protocol") == "nk-operational-plan/1", "unexpected plan protocol")
    _require(plan.get("scenario_count") == 18, "C5 plan must contain 18 scenarios")

    assertion_map = manifest.get("assertion_map")
    _require(assertion_map == {"supported": 45, "partial": 10, "unsupported": 17, "failed": 0}, "assertion map drift")
    nk_epi = manifest.get("nk_epi")
    _require(isinstance(nk_epi, dict), "NK-EPI snapshot required")
    _require((nk_epi.get("supported"), nk_epi.get("partial"), nk_epi.get("unsupported"), nk_epi.get("failed")) == (0, 0, 8, 0), "NK-EPI snapshot drift")

    checkpoints = manifest.get("checkpoints")
    _require(isinstance(checkpoints, list) and len(checkpoints) == 2, "exactly two C5 checkpoints required")
    expected_roles = {"implementation_main", "final_documentation_main"}
    _require({item.get("role") for item in checkpoints if isinstance(item, dict)} == expected_roles, "checkpoint roles drift")

    total_artifacts = 0
    for checkpoint in checkpoints:
        _require(isinstance(checkpoint, dict), "checkpoint must be an object")
        head_sha = checkpoint.get("head_sha")
        run_id = checkpoint.get("workflow_run_id")
        _require(isinstance(head_sha, str) and len(head_sha) == 40 and all(ch in "0123456789abcdef" for ch in head_sha), "invalid checkpoint SHA")
        _require(isinstance(run_id, int) and run_id > 0, "invalid workflow run id")
        artifacts = checkpoint.get("artifacts")
        _require(isinstance(artifacts, list) and len(artifacts) == 4, "each checkpoint requires four artifacts")
        total_artifacts += len(artifacts)

        for artifact in artifacts:
            _require(isinstance(artifact, dict), "artifact must be an object")
            path_text = artifact.get("path")
            _require(isinstance(path_text, str) and path_text.endswith(".zip"), "artifact ZIP path required")
            path = _resolve_inside(repo, path_text)
            _require(path.is_file(), f"artifact missing: {path_text}")
            raw = path.read_bytes()
            digest = _sha256(raw)
            _require(artifact.get("size_bytes") == len(raw), f"artifact size mismatch: {path_text}")
            _require(artifact.get("sha256") == digest, f"artifact digest mismatch: {path_text}")
            _require(artifact.get("github_digest") == f"sha256:{digest}", f"GitHub digest mismatch: {path_text}")

            expected_files = artifact.get("files")
            _require(isinstance(expected_files, list) and len(expected_files) == 6, f"six report files required: {path_text}")
            expected_by_name = {item["path"]: item for item in expected_files if isinstance(item, dict) and isinstance(item.get("path"), str)}
            _require(len(expected_by_name) == 6, f"invalid file inventory: {path_text}")

            try:
                with zipfile.ZipFile(path) as archive:
                    actual_names = sorted(archive.namelist())
                    _require(actual_names == sorted(expected_by_name), f"ZIP inventory mismatch: {path_text}")
                    for name in actual_names:
                        data = archive.read(name)
                        expected = expected_by_name[name]
                        _require(expected.get("size_bytes") == len(data), f"file size mismatch: {path_text}:{name}")
                        _require(expected.get("sha256") == _sha256(data), f"file digest mismatch: {path_text}:{name}")

                    report = json.loads(archive.read("c5-operational-report.json"))
            except (zipfile.BadZipFile, KeyError, json.JSONDecodeError) as exc:
                raise EvidenceBundleError(f"invalid artifact content {path_text}: {exc}") from exc

            _require(report.get("status") == "PASS", f"C5 report is not PASS: {path_text}")
            environment = report.get("environment")
            _require(isinstance(environment, dict), f"environment missing: {path_text}")
            _require(environment.get("commit") == head_sha, f"report commit mismatch: {path_text}")
            _require(str(environment.get("run_id")) == str(run_id), f"report run mismatch: {path_text}")
            _require(environment == artifact.get("environment"), f"environment snapshot mismatch: {path_text}")

            metrics = report.get("metrics")
            _require(isinstance(metrics, dict), f"metrics missing: {path_text}")
            _require(metrics == artifact.get("metrics"), f"metrics snapshot mismatch: {path_text}")
            _require(metrics.get("scenario_count") == 18, f"scenario count mismatch: {path_text}")
            _require(metrics.get("passed_scenarios") == 18 and metrics.get("failed_scenarios") == 0, f"scenario result mismatch: {path_text}")
            _require(metrics.get("receipt_count") == 18, f"Receipt count mismatch: {path_text}")
            _require(metrics.get("canary_leaks") == 0, f"privacy canary leak: {path_text}")
            _require(metrics.get("recovery_failures") == 0, f"recovery failure: {path_text}")
            _require(metrics.get("incident_uncontained") == 0, f"uncontained incident: {path_text}")
            _require(metrics.get("assertion_counts") == {"FAILED": 0, "PARTIAL": 10, "SUPPORTED": 45, "UNSUPPORTED": 17}, f"assertion count mismatch: {path_text}")

    _require(total_artifacts == 8, "bundle must retain eight exact ZIP artifacts")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", nargs="?", type=Path, default=Path("evidence/c5/2026-08-07/manifest.json"))
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    repo = args.repo.resolve()
    manifest_path = args.manifest if args.manifest.is_absolute() else repo / args.manifest
    try:
        validate(_load_json(manifest_path), repo=repo)
    except EvidenceBundleError as exc:
        print(f"Evidence bundle validation failed: {exc}", file=sys.stderr)
        return 1
    print(f"Evidence bundle validation passed: {manifest_path.relative_to(repo)}; checkpoints=2; artifacts=8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
