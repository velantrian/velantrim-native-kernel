#!/usr/bin/env python3
"""Validate repository-visible evidence supporting the IAR-1 independence claim."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Mapping

EVIDENCE_PATH = Path("docs/reviews/IAR-1_INDEPENDENCE_EVIDENCE.json")
EXPECTED_REPOSITORY = "velantrian/velantrim-native-kernel"
EXPECTED_REVIEW_ID = "IAR-1"
EXPECTED_REVIEWED_COMMIT = "2dd51723e30d5f3c5e86268365bf4cf7639b5e9a"
EXPECTED_REVIEW_PR = 107
EXPECTED_REVIEWER_IDENTITY = "github-codex-review-agent"
EXPECTED_GITHUB_ACTOR = "chatgpt-codex-connector[bot]"
EXPECTED_VISIBLE_REPOSITORY_ACTORS = ["velantrian"]
EXPECTED_CONTRIBUTORS_SOURCE = (
    "https://api.github.com/repos/velantrian/velantrim-native-kernel/contributors?per_page=100"
)
EXPECTED_COLLABORATORS_SOURCE = (
    "https://api.github.com/repos/velantrian/velantrim-native-kernel/collaborators?affiliation=all&per_page=100"
)
EXPECTED_REVIEW_SUBMISSION_SOURCE = (
    "https://api.github.com/repos/velantrian/velantrim-native-kernel/pulls/107/reviews/4904562661"
)
EXPECTED_REVIEW_SUBMISSION = {
    "id": 4904562661,
    "node_id": "PRR_kwDOTgZ4oc8AAAABJFWv5Q",
    "actor_login": EXPECTED_GITHUB_ACTOR,
    "actor_id": 199175422,
    "submitted_at": "2026-08-11T09:03:03Z",
    "commit_id": "925a33f33d1a252a71475d11d82edd2c53307dbb",
    "state": "COMMENTED",
    "html_url": "https://github.com/velantrian/velantrim-native-kernel/pull/107#pullrequestreview-4904562661",
}
EXPECTED_REVIEW_SUBMISSION_IDENTITY_SHA256 = (
    "a74166d124dcf99622607c7e655a9fa9e941f99ff81255d02ffe07b5be387b04"
)
EXPECTED_CANONICALIZATION = "UTF-8 JSON; keys sorted; separators ',' and ':'; identity projection only"


class IndependenceEvidenceError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise IndependenceEvidenceError(message)


def _load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise IndependenceEvidenceError(f"cannot read IAR-1 independence evidence: {exc}") from exc
    _require(isinstance(value, dict), "IAR-1 independence evidence must be an object")
    return value


def _identity_digest(value: Mapping[str, Any]) -> str:
    canonical = json.dumps(dict(value), sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def validate_record(record: Mapping[str, Any]) -> None:
    _require(record.get("protocol") == "nk-independent-review-evidence/1", "independence evidence protocol drift")
    _require(record.get("review_id") == EXPECTED_REVIEW_ID, "independence evidence review id drift")
    _require(record.get("repository") == EXPECTED_REPOSITORY, "independence evidence repository drift")
    _require(record.get("reviewed_commit") == EXPECTED_REVIEWED_COMMIT, "independence evidence reviewed commit drift")
    _require(record.get("review_pr") == EXPECTED_REVIEW_PR, "independence evidence PR drift")
    _require(record.get("reviewer_identity") == EXPECTED_REVIEWER_IDENTITY, "independence evidence reviewer identity drift")
    _require(record.get("github_actor_login") == EXPECTED_GITHUB_ACTOR, "independence evidence GitHub actor drift")

    contributors = record.get("contributors_snapshot")
    collaborators = record.get("collaborators_snapshot")
    _require(isinstance(contributors, Mapping), "contributors snapshot required")
    _require(isinstance(collaborators, Mapping), "collaborators snapshot required")
    _require(contributors.get("source") == EXPECTED_CONTRIBUTORS_SOURCE, "contributors evidence source drift")
    _require(collaborators.get("source") == EXPECTED_COLLABORATORS_SOURCE, "collaborators evidence source drift")
    _require(contributors.get("logins") == EXPECTED_VISIBLE_REPOSITORY_ACTORS, "contributors snapshot drift")
    _require(collaborators.get("logins") == EXPECTED_VISIBLE_REPOSITORY_ACTORS, "collaborators snapshot drift")

    _require(
        record.get("review_submission_source") == EXPECTED_REVIEW_SUBMISSION_SOURCE,
        "exact review submission evidence source drift",
    )
    submission = record.get("review_submission")
    _require(isinstance(submission, Mapping), "exact review submission identity required")
    _require(dict(submission) == EXPECTED_REVIEW_SUBMISSION, "exact review submission identity drift")
    _require(
        record.get("review_submission_identity_canonicalization") == EXPECTED_CANONICALIZATION,
        "review submission canonicalization drift",
    )
    _require(
        _identity_digest(submission) == EXPECTED_REVIEW_SUBMISSION_IDENTITY_SHA256,
        "computed review submission identity digest drift",
    )
    _require(
        record.get("review_submission_identity_sha256") == EXPECTED_REVIEW_SUBMISSION_IDENTITY_SHA256,
        "recorded review submission identity digest drift",
    )
    _require(submission.get("actor_login") == record.get("github_actor_login"), "review submission actor binding drift")

    contributor_logins = contributors.get("logins")
    collaborator_logins = collaborators.get("logins")
    _require(EXPECTED_GITHUB_ACTOR not in contributor_logins, "review actor appears in contributor snapshot")
    _require(EXPECTED_GITHUB_ACTOR not in collaborator_logins, "review actor appears in collaborator snapshot")
    _require(record.get("reviewer_in_contributors_snapshot") is False, "reviewer contributor separation drift")
    _require(record.get("reviewer_in_collaborators_snapshot") is False, "reviewer collaborator separation drift")
    _require(
        record.get("repository_authorship_inference")
        == "NO_REPOSITORY_COMMIT_ATTRIBUTED_TO_REVIEWER_IN_VISIBLE_CONTRIBUTOR_SNAPSHOT",
        "repository-visible authorship inference drift",
    )

    basis = record.get("separation_basis")
    _require(isinstance(basis, str) and len(basis.strip()) >= 180, "substantive repository-visible separation basis required")
    for marker in (
        EXPECTED_GITHUB_ACTOR,
        "4904562661",
        EXPECTED_REVIEW_SUBMISSION["commit_id"],
        "absent from both repository contributor and collaborator snapshots",
        "immutable architecture subject",
        "PR review channel",
    ):
        _require(marker in basis, f"repository-visible separation basis missing marker: {marker}")

    limitations = record.get("limitations")
    _require(isinstance(limitations, list) and len(limitations) >= 2, "independence evidence limitations required")
    joined = " ".join(str(item) for item in limitations).lower()
    for marker in ("does not prove model-training independence", "future independent review"):
        _require(marker in joined, f"independence evidence limitation missing: {marker}")


def validate(repo: Path) -> None:
    validate_record(_load(repo / EVIDENCE_PATH))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    try:
        validate(args.repo.resolve())
    except IndependenceEvidenceError as exc:
        print(f"IAR-1 independence evidence failed: {exc}", file=sys.stderr)
        return 1
    print("IAR-1 independence evidence passed; exact GitHub review submission and repository-visible reviewer separation are recorded and scope-limited")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
