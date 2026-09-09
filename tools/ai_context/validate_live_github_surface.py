#!/usr/bin/env python3
"""Validate the current external GitHub routing surface against live GitHub state.

This is support/governance tooling only. A PASS proves that the repository's
current routing points at a live-open GitHub object. It does not qualify an H11
reviewer, change H11 admission, authorize execution, thaw runtime, promote
Final Canon, or authorize production.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

CURRENT_STATE_PATH = "docs/ai/CURRENT_STATE.md"
PROJECT_STATE_PATH = "project-state.json"
CURRENT_SURFACE_RE = re.compile(
    r"^open_review_surface:\s*(Issue|PR)\s+#([1-9][0-9]*)\s*$",
    re.IGNORECASE | re.MULTILINE,
)
GITHUB_API_VERSION = "2022-11-28"
USER_AGENT = "velantrim-native-kernel-live-surface-validator/1"


@dataclass(frozen=True)
class Finding:
    path: str
    message: str

    def render(self) -> str:
        return f"{self.path}: {self.message}"


LiveFetcher = Callable[[str, str, int], dict[str, Any]]


def _load_json(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    if not path.is_file():
        return None, [Finding(str(path), "required machine-readable state file is missing")]
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return None, [Finding(str(path), f"cannot parse JSON: {exc}")]
    if not isinstance(value, dict):
        return None, [Finding(str(path), "top-level JSON value must be an object")]
    return value, []


def _read_current_surface(repo: Path) -> tuple[tuple[str, int] | None, list[Finding]]:
    path = repo / CURRENT_STATE_PATH
    if not path.is_file():
        return None, [Finding(CURRENT_STATE_PATH, "current-state surface is missing")]
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return None, [Finding(CURRENT_STATE_PATH, f"cannot read current-state surface: {exc}")]
    matches = list(CURRENT_SURFACE_RE.finditer(text))
    if len(matches) != 1:
        return None, [
            Finding(
                CURRENT_STATE_PATH,
                "expected exactly one machine-readable 'open_review_surface: Issue|PR #N' binding",
            )
        ]
    kind_text, number_text = matches[0].groups()
    kind = "issue" if kind_text.lower() == "issue" else "pull_request"
    return (kind, int(number_text)), []


def _repository_name(project_state: dict[str, Any]) -> str | None:
    repository = project_state.get("repository")
    if not isinstance(repository, dict):
        return None
    full_name = repository.get("full_name")
    return full_name if isinstance(full_name, str) and full_name else None


def _default_live_fetcher(repository: str, kind: str, number: int) -> dict[str, Any]:
    try:
        owner, name = repository.split("/", 1)
    except ValueError as exc:
        raise RuntimeError("repository.full_name must have owner/name form") from exc
    resource = "issues" if kind == "issue" else "pulls"
    url = (
        "https://api.github.com/repos/"
        f"{quote(owner, safe='')}/{quote(name, safe='')}/{resource}/{number}"
    )
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": GITHUB_API_VERSION,
        "User-Agent": USER_AGENT,
    }
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(url, headers=headers, method="GET")
    try:
        with urlopen(request, timeout=10) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        raise RuntimeError(f"GitHub API HTTP {exc.code}") from exc
    except URLError as exc:
        raise RuntimeError(f"GitHub API unavailable: {exc.reason}") from exc
    except (TimeoutError, UnicodeError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"GitHub API response unavailable or invalid: {exc}") from exc
    if not isinstance(payload, dict):
        raise RuntimeError("GitHub API response is not an object")
    return payload


def _observed_state(kind: str, payload: dict[str, Any]) -> str:
    if kind == "issue":
        if "pull_request" in payload:
            raise RuntimeError("configured Issue resolved to a pull request object")
        state = payload.get("state")
        if state not in {"open", "closed"}:
            raise RuntimeError("Issue response has no recognized state")
        return state.upper()
    if kind == "pull_request":
        if payload.get("merged_at") is not None:
            return "MERGED"
        state = payload.get("state")
        if state not in {"open", "closed"}:
            raise RuntimeError("pull-request response has no recognized state")
        return state.upper()
    raise RuntimeError(f"unsupported current surface kind: {kind}")


def validate(repo: Path, *, live_fetcher: LiveFetcher | None = None) -> list[Finding]:
    repo = repo.resolve()
    findings: list[Finding] = []

    surface, surface_findings = _read_current_surface(repo)
    findings.extend(surface_findings)

    project_state, state_findings = _load_json(repo / PROJECT_STATE_PATH)
    findings.extend(
        Finding(PROJECT_STATE_PATH, finding.message) for finding in state_findings
    )

    if surface is None or project_state is None:
        return findings

    repository = _repository_name(project_state)
    if repository is None:
        findings.append(
            Finding(PROJECT_STATE_PATH, "repository.full_name is missing or invalid")
        )
        return findings

    kind, number = surface

    # The field is intentionally named open_review_surface. Whatever object it
    # points to must therefore be live OPEN. This would have rejected the old
    # stale routing to merged PR #131 without introducing a second authority.
    expected_state = "OPEN"

    if kind == "issue":
        issues = project_state.get("issues")
        entry = issues.get(str(number)) if isinstance(issues, dict) else None
        if not isinstance(entry, dict):
            findings.append(
                Finding(
                    PROJECT_STATE_PATH,
                    f"current Issue #{number} is missing from project-state issues",
                )
            )
        else:
            machine_state = entry.get("state")
            if machine_state != expected_state:
                findings.append(
                    Finding(
                        PROJECT_STATE_PATH,
                        f"current Issue #{number} machine state is {machine_state!r}, expected 'OPEN'",
                    )
                )

    fetcher = live_fetcher or _default_live_fetcher
    try:
        payload = fetcher(repository, kind, number)
        observed_number = payload.get("number")
        if observed_number != number:
            raise RuntimeError(
                f"GitHub API returned object #{observed_number!r}, expected #{number}"
            )
        observed_state = _observed_state(kind, payload)
    except Exception as exc:  # fail closed: unavailable live truth is UNKNOWN, never PASS
        findings.append(
            Finding(
                CURRENT_STATE_PATH,
                f"live GitHub state UNKNOWN for {kind} #{number}: {exc}",
            )
        )
        return findings

    if observed_state != expected_state:
        label = "Issue" if kind == "issue" else "PR"
        findings.append(
            Finding(
                CURRENT_STATE_PATH,
                f"stale current routing: {label} #{number} is live {observed_state}, expected OPEN",
            )
        )

    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo_path", nargs="?", type=Path, default=None)
    parser.add_argument("--repo", dest="repo_flag", type=Path, default=None)
    args = parser.parse_args(argv)
    if args.repo_path is not None and args.repo_flag is not None:
        parser.error("repository may be supplied either positionally or with --repo, not both")
    repo = (args.repo_flag or args.repo_path or Path.cwd()).resolve()

    findings = validate(repo)
    if findings:
        for finding in findings:
            print(finding.render(), file=sys.stderr)
        return 1

    surface, _ = _read_current_surface(repo)
    assert surface is not None
    kind, number = surface
    label = "Issue" if kind == "issue" else "PR"
    print(
        f"Live GitHub surface validation passed; {label} #{number}=OPEN; "
        "routing freshness only; no H11/runtime/Canon/production authority granted"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
