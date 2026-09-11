#!/usr/bin/env python3
"""Bounded static guard for tests/test*.py CI declarations.

This tool does not execute workflows and is not proof of runtime CI reachability.
It inventories test modules against supported explicit unittest command forms and
pull_request path filters. Unsupported YAML/shell indirection remains outside the
claim boundary.
"""
from __future__ import annotations

import argparse
import fnmatch
import re
from dataclasses import dataclass
from pathlib import Path

WORKFLOWS_DIR = Path(".github/workflows")
TESTS_DIR = Path("tests")
TEST_FILE_PATTERN = "test*.py"
PR_EVENT = "pull_request"

DISCOVER_PATTERN_RE = re.compile(r"unittest\s+discover\s+-s\s+tests\s+-p\s+['\"]([^'\"]+)['\"]")
DISCOVER_DEFAULT_RE = re.compile(r"unittest\s+discover\s+-s\s+tests(?!\s+-p\b)")
MODULE_RE = re.compile(r"unittest\s+(?!discover\b)(tests\.[A-Za-z_][A-Za-z0-9_]*)")
TOP_LEVEL_KEY_RE = re.compile(r"^([A-Za-z_][\w-]*)\s*:")


@dataclass(frozen=True)
class WorkflowCoverage:
    path: str
    pull_request_paths: tuple[str, ...] | None
    discover_patterns: tuple[str, ...]
    modules: tuple[str, ...]
    default_discover: bool


@dataclass(frozen=True)
class DiscoveryGap:
    test_path: str
    reason: str


def github_glob_match(path: str, pattern: str) -> bool:
    if path == pattern:
        return True
    return _github_glob_to_regex(pattern).fullmatch(path) is not None


def _github_glob_to_regex(pattern: str) -> re.Pattern[str]:
    parts: list[str] = []
    index = 0
    while index < len(pattern):
        if pattern.startswith("**/", index):
            parts.append("(?:.*/)?")
            index += 3
            continue
        if pattern.startswith("**", index):
            parts.append(".*")
            index += 2
            continue
        char = pattern[index]
        if char == "*":
            parts.append("[^/]*")
        elif char == "?":
            parts.append("[^/]")
        else:
            parts.append(re.escape(char))
        index += 1
    return re.compile("".join(parts))


def list_test_modules(repo: Path) -> list[Path]:
    tests = repo / TESTS_DIR
    return sorted(path for path in tests.glob(TEST_FILE_PATTERN) if path.is_file() and path.name.endswith(".py"))


def _block_for_key(text: str, key: str) -> tuple[int, str] | None:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        match = TOP_LEVEL_KEY_RE.match(line)
        if match is None or match.group(1) != key:
            continue
        collected: list[str] = []
        for following in lines[index + 1 :]:
            if following and not following.startswith((" ", "\t")) and TOP_LEVEL_KEY_RE.match(following):
                break
            collected.append(following)
        return index, "\n".join(collected)
    return None


def _event_block(on_text: str, event: str) -> str | None:
    lines = on_text.splitlines()
    header = re.compile(rf"^(\s*){re.escape(event)}\s*:")
    for index, line in enumerate(lines):
        match = header.match(line)
        if match is None:
            continue
        indent = len(match.group(1))
        collected: list[str] = []
        for following in lines[index + 1 :]:
            if not following.strip():
                collected.append(following)
                continue
            current = len(following) - len(following.lstrip(" "))
            if current <= indent and following.lstrip().split(":", 1)[0].isidentifier():
                break
            if current <= indent and following.lstrip().startswith("#"):
                continue
            if current <= indent:
                break
            collected.append(following)
        return "\n".join(collected)
    return None


def parse_pull_request_paths(workflow_text: str) -> tuple[str, ...] | None:
    on_block = _block_for_key(workflow_text, "on")
    if on_block is None:
        return ()
    event = _event_block(on_block[1], PR_EVENT)
    if event is None:
        return ()
    if re.search(r"^\s*paths\s*:", event, re.MULTILINE) is None:
        return None
    patterns: list[str] = []
    in_paths = False
    paths_indent: int | None = None
    for line in event.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" "))
        if re.match(r"paths\s*:", stripped):
            in_paths = True
            paths_indent = indent
            continue
        if in_paths:
            if paths_indent is not None and indent <= paths_indent and not stripped.startswith("-"):
                break
            if stripped.startswith("-"):
                item = stripped[1:].strip().strip("'\"")
                if item:
                    patterns.append(item)
    return tuple(patterns)


def _strip_comment_only_lines(text: str) -> str:
    return "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("#"))


def parse_unittest_invocations(workflow_text: str) -> tuple[tuple[str, ...], tuple[str, ...], bool]:
    active_text = _strip_comment_only_lines(workflow_text)
    patterns = tuple(DISCOVER_PATTERN_RE.findall(active_text))
    modules = tuple(MODULE_RE.findall(active_text))
    default_discover = DISCOVER_DEFAULT_RE.search(active_text) is not None
    return patterns, modules, default_discover


def parse_workflow(path: Path) -> WorkflowCoverage:
    text = path.read_text(encoding="utf-8")
    patterns, modules, default_discover = parse_unittest_invocations(text)
    return WorkflowCoverage(path=path.as_posix(), pull_request_paths=parse_pull_request_paths(text), discover_patterns=patterns, modules=modules, default_discover=default_discover)


def _invoked(module_filename: str, coverage: WorkflowCoverage) -> bool:
    if coverage.default_discover:
        return fnmatch.fnmatch(module_filename, TEST_FILE_PATTERN)
    module_name = "tests." + Path(module_filename).stem
    if module_name in coverage.modules:
        return True
    return any(fnmatch.fnmatch(module_filename, pattern) for pattern in coverage.discover_patterns)


def _path_triggered(rel_posix: str, coverage: WorkflowCoverage) -> bool:
    if coverage.pull_request_paths is None:
        return True
    return any(github_glob_match(rel_posix, pattern) for pattern in coverage.pull_request_paths)


def audit_test_discovery(repo: Path) -> list[DiscoveryGap]:
    workflows_root = repo / WORKFLOWS_DIR
    coverages = [parse_workflow(path) for path in sorted(workflows_root.glob("*.yml")) + sorted(workflows_root.glob("*.yaml")) if path.is_file()]
    gaps: list[DiscoveryGap] = []
    for test_path in list_test_modules(repo):
        rel = test_path.relative_to(repo).as_posix()
        filename = test_path.name
        covering = [coverage for coverage in coverages if _invoked(filename, coverage) and _path_triggered(rel, coverage)]
        if covering:
            continue
        invoked_by = [coverage.path for coverage in coverages if _invoked(filename, coverage)]
        triggered_by = [coverage.path for coverage in coverages if _path_triggered(rel, coverage)]
        if not invoked_by:
            gaps.append(DiscoveryGap(rel, "not declared by any supported workflow unittest form"))
        elif not triggered_by:
            gaps.append(DiscoveryGap(rel, "declared but no pull_request path filter would run that workflow when the file changes"))
        else:
            gaps.append(DiscoveryGap(rel, "declared by " + ", ".join(invoked_by) + " but those workflows do not path-trigger this file (path-triggering workflows: " + ", ".join(triggered_by) + ")"))
    return gaps


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    repo = args.repo.resolve()
    gaps = audit_test_discovery(repo)
    if gaps:
        print("CI static test-declaration coverage FAILED:", file=__import__("sys").stderr)
        for gap in gaps:
            print(f"  {gap.test_path}: {gap.reason}", file=__import__("sys").stderr)
        return 1
    modules = list_test_modules(repo)
    print(f"CI static test-declaration coverage PASS ({len(modules)} tests/{TEST_FILE_PATTERN} modules declared and path-triggered within supported syntax; execution not proven)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
