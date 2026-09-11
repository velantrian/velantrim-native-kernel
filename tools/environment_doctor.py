#!/usr/bin/env python3
"""Read-only diagnostic of Native Kernel checkout environment readiness.

Does not install packages, mutate the environment, create or migrate databases,
execute H11, thaw runtime, or authorize Canon/production.

Default exit status is CORE-only readiness. Exit 0 without --strict does not
mean SQLite, PostgreSQL, Rust, full git history, or FULL_SUITE are ready.
"""
from __future__ import annotations

import argparse
import importlib
import os
import re
import shutil
import sqlite3
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Mapping, Sequence

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from native_kernel.sqlite_profile.runtime import (  # noqa: E402
    MINIMUM_WAL_SAFE_SQLITE,
    sqlite_wal_version_is_safe,
)

VALIDATED_PYTHON_MINOR_VERSIONS = ((3, 11), (3, 12))
POSTGRES_DSN_ENV = "NK_TEST_POSTGRES_DSN"
RUST_TOOLCHAIN_PATH = Path("experiments/bpv1/BPV1-001/rust-toolchain.toml")
CHANNEL_RE = re.compile(r'(?m)^channel\s*=\s*"([^"]+)"\s*$')

RunCommand = Callable[..., subprocess.CompletedProcess[str]]
Which = Callable[[str], str | None]


@dataclass(frozen=True)
class GitProbe:
    git_available: bool
    is_repository: bool
    is_shallow: bool | None
    head: str | None
    error: str | None = None


@dataclass(frozen=True)
class EnvironmentProbe:
    python_version: tuple[int, int, int]
    python_executable: str
    sqlite_version: str
    git: GitProbe
    postgres_dsn: str | None
    psycopg_importable: bool
    rustup_path: str | None
    cargo_path: str | None
    pinned_rust_channel: str | None
    rust_channel_available: bool
    rustc_version: str | None
    rust_error: str | None = None


@dataclass(frozen=True)
class CheckResult:
    name: str
    ready: bool
    detail: str


@dataclass(frozen=True)
class Diagnosis:
    core: CheckResult
    sqlite_integration: CheckResult
    postgres_integration: CheckResult
    bpv1_execution: CheckResult
    git_history: CheckResult
    full_suite: CheckResult
    lines: tuple[str, ...]


def read_pinned_rust_channel(repo: Path) -> str:
    text = (repo / RUST_TOOLCHAIN_PATH).read_text(encoding="utf-8")
    match = CHANNEL_RE.search(text)
    if match is None:
        raise ValueError(f"pinned Rust channel missing in {RUST_TOOLCHAIN_PATH.as_posix()}")
    return match.group(1)


def probe_git(
    repo: Path,
    *,
    run: RunCommand = subprocess.run,
    which: Which = shutil.which,
) -> GitProbe:
    if which("git") is None:
        return GitProbe(
            git_available=False,
            is_repository=False,
            is_shallow=None,
            head=None,
            error="git executable not found",
        )

    def git(*args: str) -> subprocess.CompletedProcess[str]:
        return run(
            ["git", *args],
            cwd=repo,
            capture_output=True,
            text=True,
            check=False,
        )

    inside = git("rev-parse", "--is-inside-work-tree")
    if inside.returncode != 0 or inside.stdout.strip() != "true":
        return GitProbe(
            git_available=True,
            is_repository=False,
            is_shallow=None,
            head=None,
            error="not a git repository",
        )
    shallow = git("rev-parse", "--is-shallow-repository")
    head = git("rev-parse", "HEAD")
    return GitProbe(
        git_available=True,
        is_repository=True,
        is_shallow=shallow.stdout.strip() == "true",
        head=head.stdout.strip() or None,
        error=None if head.returncode == 0 and head.stdout.strip() else "HEAD could not be resolved",
    )


def probe_rust_channel(
    channel: str,
    *,
    run: RunCommand = subprocess.run,
    which: Which = shutil.which,
) -> tuple[str | None, str | None, bool, str | None, str | None]:
    rustup_path = which("rustup")
    cargo_path = which("cargo")
    if rustup_path is None or cargo_path is None:
        missing = []
        if rustup_path is None:
            missing.append("rustup")
        if cargo_path is None:
            missing.append("cargo")
        return rustup_path, cargo_path, False, None, "missing " + ", ".join(missing)
    result = run(
        ["rustup", "run", channel, "rustc", "--version"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return (
            rustup_path,
            cargo_path,
            False,
            None,
            f"rustup run {channel} rustc failed",
        )
    return rustup_path, cargo_path, True, result.stdout.strip() or None, None


def collect_probe(
    repo: Path,
    *,
    environ: Mapping[str, str] | None = None,
    python_version: Sequence[int] | None = None,
    python_executable: str | None = None,
    sqlite_version: str | None = None,
    run: RunCommand = subprocess.run,
    which: Which = shutil.which,
    psycopg_importable: bool | None = None,
) -> EnvironmentProbe:
    env = os.environ if environ is None else environ
    version_info = sys.version_info if python_version is None else python_version
    py_version = (int(version_info[0]), int(version_info[1]), int(version_info[2]))
    dsn = env.get(POSTGRES_DSN_ENV)
    if dsn is not None and not dsn.strip():
        dsn = None
    if psycopg_importable is None:
        try:
            importlib.import_module("psycopg")
            psycopg_ok = True
        except ImportError:
            psycopg_ok = False
    else:
        psycopg_ok = psycopg_importable
    try:
        pinned = read_pinned_rust_channel(repo)
        rust_error = None
    except (OSError, ValueError) as exc:
        pinned = None
        rust_error = str(exc)
    if pinned is None:
        rustup_path = which("rustup")
        cargo_path = which("cargo")
        rust_ok = False
        rustc_version = None
    else:
        rustup_path, cargo_path, rust_ok, rustc_version, rust_probe_error = probe_rust_channel(
            pinned, run=run, which=which
        )
        rust_error = rust_error or rust_probe_error
    return EnvironmentProbe(
        python_version=py_version,
        python_executable=python_executable or sys.executable,
        sqlite_version=sqlite3.sqlite_version if sqlite_version is None else sqlite_version,
        git=probe_git(repo, run=run, which=which),
        postgres_dsn=dsn,
        psycopg_importable=psycopg_ok,
        rustup_path=rustup_path,
        cargo_path=cargo_path,
        pinned_rust_channel=pinned,
        rust_channel_available=rust_ok,
        rustc_version=rustc_version,
        rust_error=rust_error,
    )


def diagnose(probe: EnvironmentProbe) -> Diagnosis:
    py_minor = probe.python_version[:2]
    python_ok = py_minor in VALIDATED_PYTHON_MINOR_VERSIONS
    git_ok = (
        probe.git.git_available
        and probe.git.is_repository
        and bool(probe.git.head)
        and probe.git.error is None
    )
    core_ok = python_ok and git_ok
    validated = ", ".join(f"{major}.{minor}" for major, minor in VALIDATED_PYTHON_MINOR_VERSIONS)
    core = CheckResult(
        name="CORE",
        ready=core_ok,
        detail=(
            f"Python {py_minor[0]}.{py_minor[1]}.{probe.python_version[2]} "
            f"({probe.python_executable}); validated CI versions: {validated}"
            + ("" if python_ok else " — unvalidated Python minor")
            + "; git "
            + (
                f"HEAD {probe.git.head}"
                if git_ok
                else (probe.git.error or "repository/HEAD not ready")
            )
        ),
    )
    sqlite_ok = sqlite_wal_version_is_safe(probe.sqlite_version)
    sqlite = CheckResult(
        name="SQLITE_INTEGRATION",
        ready=sqlite_ok,
        detail=(
            f"linked sqlite3.sqlite_version={probe.sqlite_version}; "
            f"required >= {MINIMUM_WAL_SAFE_SQLITE} "
            f"({Path('native_kernel/sqlite_profile/runtime.py').as_posix()})"
        ),
    )
    postgres_ok = bool(probe.postgres_dsn) and probe.psycopg_importable
    postgres = CheckResult(
        name="POSTGRES_INTEGRATION",
        ready=postgres_ok,
        detail=(
            f"{POSTGRES_DSN_ENV}={'set' if probe.postgres_dsn else 'absent'}; "
            f"psycopg={'importable' if probe.psycopg_importable else 'not importable'} "
            "(optional; integration tests SKIP when DSN is absent)"
        ),
    )
    bpv1_ok = bool(probe.pinned_rust_channel) and probe.rust_channel_available
    bpv1 = CheckResult(
        name="BPV1_EXECUTION",
        ready=bpv1_ok,
        detail=(
            f"pinned channel={probe.pinned_rust_channel or 'UNAVAILABLE'} "
            f"({RUST_TOOLCHAIN_PATH.as_posix()}); "
            f"rustup={'yes' if probe.rustup_path else 'no'}; "
            f"cargo={'yes' if probe.cargo_path else 'no'}; "
            + (probe.rustc_version or probe.rust_error or "toolchain not available")
            + " (optional; BPV1SubjectExecutionTests SKIP when absent)"
        ),
    )
    history_ok = git_ok and probe.git.is_shallow is False
    history = CheckResult(
        name="GIT_HISTORY",
        ready=history_ok,
        detail=(
            "complete (not shallow)"
            if history_ok
            else (
                "shallow clone; git-bound checkpoint tests SKIP "
                "(unshallow: git fetch --unshallow)"
                if probe.git.is_shallow
                else (probe.git.error or "history not established")
            )
        ),
    )
    full_ok = all(
        item.ready for item in (core, sqlite, postgres, bpv1, history)
    )
    missing = [
        item.name
        for item in (core, sqlite, postgres, bpv1, history)
        if not item.ready
    ]
    full = CheckResult(
        name="FULL_SUITE",
        ready=full_ok,
        detail="all optional layers ready" if full_ok else "not ready: " + ", ".join(missing),
    )
    lines = (
        "Native Kernel environment doctor (read-only)",
        "DEFAULT_EXIT_SCOPE: CORE_ONLY — exit 0 without --strict means only CORE is ready.",
        "CORE: " + ("READY" if core.ready else "NOT_READY") + " — " + core.detail,
        "SQLITE_INTEGRATION: "
        + ("READY" if sqlite.ready else "NOT_READY")
        + " — "
        + sqlite.detail,
        "POSTGRES_INTEGRATION: "
        + ("READY" if postgres.ready else "NOT_READY")
        + " — "
        + postgres.detail,
        "BPV1_EXECUTION: "
        + ("READY" if bpv1.ready else "NOT_READY")
        + " — "
        + bpv1.detail,
        "GIT_HISTORY: "
        + ("COMPLETE" if history.ready else "NOT_COMPLETE")
        + " — "
        + history.detail,
        "FULL_SUITE: " + ("READY" if full.ready else "NOT_READY") + " — " + full.detail,
        "Optional PostgreSQL/Rust/SQLite/history gaps are not a core-red of Python/git readiness.",
        "CORE READY does not authorize SQLite/WAL integration or imply FULL_SUITE readiness.",
        "This probe does not authorize H11, runtime thaw, Final Canon, or production.",
    )
    return Diagnosis(
        core=core,
        sqlite_integration=sqlite,
        postgres_integration=postgres,
        bpv1_execution=bpv1,
        git_history=history,
        full_suite=full,
        lines=lines,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit 1 unless FULL_SUITE is ready (SQLite + Postgres + Rust + complete git history)",
    )
    args = parser.parse_args(argv)
    repo = args.repo.resolve()
    diagnosis = diagnose(collect_probe(repo))
    print("\n".join(diagnosis.lines))
    if args.strict:
        return 0 if diagnosis.full_suite.ready else 1
    return 0 if diagnosis.core.ready else 1


if __name__ == "__main__":
    raise SystemExit(main())
