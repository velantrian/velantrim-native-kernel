#!/usr/bin/env python3
"""Validate repository-visible IAR-1 reviewer, submission and input-packet evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Mapping

EVIDENCE_PATH = Path("docs/reviews/IAR-1_INDEPENDENCE_EVIDENCE.json")
RESULT_PATH = Path("docs/reviews/IAR-1_RESULT.json")
PACKET_EVIDENCE_PATH = Path("docs/reviews/IAR-1_INPUT_PACKET_EVIDENCE.json")
EXPECTED_REPOSITORY = "velantrian/velantrim-native-kernel"
EXPECTED_REVIEW_ID = "IAR-1"
EXPECTED_REVIEWED_COMMIT = "2dd51723e30d5f3c5e86268365bf4cf7639b5e9a"
EXPECTED_REVIEW_PR = 107
EXPECTED_REVIEWER_IDENTITY = "github-codex-review-agent"
EXPECTED_GITHUB_ACTOR = "chatgpt-codex-connector[bot]"
EXPECTED_REVIEW_REQUEST_DOCUMENT = "docs/reviews/IAR-1_CODEX_REVIEW_REQUEST.md"
EXPECTED_REVIEW_PROTOCOL_DOCUMENT = "docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md"
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
EXPECTED_SOURCE_PACKET_ATTESTATION = [
    "AGENTS.md and mandatory orientation surfaces",
    "A1-A10 provisional architecture documents",
    "integrated A1-A10 reconciliation",
    "ADR-0025",
    "ADR-0026",
    "nk-independent-architecture-review/1",
    "P1-C5 contract/evidence/runtime context sufficient to test implementation capture",
]
EXPECTED_EXACT_PACKET_PATHS = [
    "AGENTS.md",
    "README.md",
    "STATUS.md",
    "project-state.json",
    "docs/ai/README.md",
    "docs/ai/CURRENT_STATE.md",
    "docs/ai/KNOWN_RISKS.md",
    "ROADMAP.md",
    "docs/ARCHITECTURE_REFOUNDATION.md",
    "docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.md",
    "docs/A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md",
    "docs/A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md",
    "docs/A4_SEMANTIC_LAWS_AND_INVARIANTS.md",
    "docs/A5_IDENTITY_TIME_AND_CHANGE.md",
    "docs/A6_KNOWLEDGE_LIFECYCLE.md",
    "docs/A7_CONFLICT_UNCERTAINTY_AND_REVISION.md",
    "docs/A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md",
    "docs/A9_REFERENCE_LABORATORY_BOUNDARY.md",
    "docs/A10_OPEN_QUESTIONS_AND_FALSIFICATION.md",
    "docs/INTEGRATED_A1_A10_REVIEW.md",
    "docs/adr/0025-blueprint-before-runtime-expansion.md",
    "docs/adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md",
    EXPECTED_REVIEW_PROTOCOL_DOCUMENT,
]


class IndependenceEvidenceError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise IndependenceEvidenceError(message)


def _load(path: Path, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise IndependenceEvidenceError(f"cannot read {label}: {exc}") from exc
    _require(isinstance(value, dict), f"{label} must be an object")
    return value


def _identity_digest(value: Mapping[str, Any]) -> str:
    canonical = json.dumps(dict(value), sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _git_path_exists(repo: Path, commit: str, rel: str) -> bool:
    if not (repo / ".git").exists():
        return True
    completed = subprocess.run(
        ["git", "-C", str(repo), "cat-file", "-e", f"{commit}:{rel}"],
        check=False,
        capture_output=True,
        text=True,
    )
    return completed.returncode == 0


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

    _require(record.get("review_submission_source") == EXPECTED_REVIEW_SUBMISSION_SOURCE, "exact review submission evidence source drift")
    submission = record.get("review_submission")
    _require(isinstance(submission, Mapping), "exact review submission identity required")
    _require(dict(submission) == EXPECTED_REVIEW_SUBMISSION, "exact review submission identity drift")
    _require(record.get("review_submission_identity_canonicalization") == EXPECTED_CANONICALIZATION, "review submission canonicalization drift")
    _require(_identity_digest(submission) == EXPECTED_REVIEW_SUBMISSION_IDENTITY_SHA256, "computed review submission identity digest drift")
    _require(record.get("review_submission_identity_sha256") == EXPECTED_REVIEW_SUBMISSION_IDENTITY_SHA256, "recorded review submission identity digest drift")
    _require(submission.get("actor_login") == record.get("github_actor_login"), "review submission actor binding drift")

    contributor_logins = contributors.get("logins")
    collaborator_logins = collaborators.get("logins")
    _require(EXPECTED_GITHUB_ACTOR not in contributor_logins, "review actor appears in contributor snapshot")
    _require(EXPECTED_GITHUB_ACTOR not in collaborator_logins, "review actor appears in collaborator snapshot")
    _require(record.get("reviewer_in_contributors_snapshot") is False, "reviewer contributor separation drift")
    _require(record.get("reviewer_in_collaborators_snapshot") is False, "reviewer collaborator separation drift")
    _require(
        record.get("repository_authorship_inference") == "NO_REPOSITORY_COMMIT_ATTRIBUTED_TO_REVIEWER_IN_VISIBLE_CONTRIBUTOR_SNAPSHOT",
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


def validate_cross_records(
    independence: Mapping[str, Any],
    result: Mapping[str, Any],
    packet: Mapping[str, Any],
    repo: Path | None = None,
) -> None:
    validate_record(independence)
    submission = independence["review_submission"]

    _require(result.get("protocol") == "nk-independent-architecture-review-result/1", "IAR-1 result protocol drift")
    _require(result.get("review_id") == EXPECTED_REVIEW_ID, "IAR-1 result review id drift")
    _require(result.get("reviewed_commit") == EXPECTED_REVIEWED_COMMIT, "IAR-1 result reviewed commit drift")
    _require(
        result.get("review_request_commit") == submission.get("commit_id"),
        "IAR-1 result review_request_commit must match exact review submission commit",
    )
    _require(result.get("input_packet_read") == EXPECTED_SOURCE_PACKET_ATTESTATION, "source review input-packet attestation drift")

    _require(packet.get("protocol") == "nk-independent-review-input-packet-evidence/1", "input-packet evidence protocol drift")
    _require(packet.get("review_id") == EXPECTED_REVIEW_ID, "input-packet evidence review id drift")
    _require(packet.get("reviewed_commit") == EXPECTED_REVIEWED_COMMIT, "input-packet reviewed commit drift")
    _require(packet.get("review_request_commit") == submission.get("commit_id"), "input-packet review request commit binding drift")
    _require(packet.get("review_request_document") == EXPECTED_REVIEW_REQUEST_DOCUMENT, "input-packet review request document drift")
    _require(packet.get("review_protocol_document") == EXPECTED_REVIEW_PROTOCOL_DOCUMENT, "input-packet review protocol document drift")
    _require(packet.get("source_review_attestation") == result.get("input_packet_read"), "packet normalization must preserve source review attestation")

    exact_paths = packet.get("normalized_exact_paths")
    _require(isinstance(exact_paths, list), "normalized exact input-packet paths required")
    _require(exact_paths == EXPECTED_EXACT_PACKET_PATHS, "normalized exact input-packet inventory drift")
    _require(len(exact_paths) == len(set(exact_paths)), "normalized exact input-packet inventory contains duplicates")
    _require(packet.get("normalization_scope") == "MANDATORY_NAMED_FILES_ONLY", "input-packet normalization scope drift")
    _require(packet.get("telemetry_boundary") == "NO_PER_FILE_REVIEWER_ACCESS_TELEMETRY_AVAILABLE", "input-packet telemetry boundary drift")
    _require(
        packet.get("p1_c5_context_read_attestation") == EXPECTED_SOURCE_PACKET_ATTESTATION[-1],
        "P1-C5 context read attestation drift",
    )
    _require(packet.get("p1_c5_exact_file_telemetry") == "NOT_AVAILABLE", "P1-C5 telemetry overclaim")

    basis = packet.get("normalization_basis")
    _require(isinstance(basis, str) and "duplicate-free expansion" in basis and "per-file access telemetry" in basis, "input-packet normalization basis incomplete")
    interpretation = packet.get("qualification_interpretation")
    _require(isinstance(interpretation, str) and "must not claim independent per-file read telemetry" in interpretation, "input-packet qualification boundary missing")

    if repo is not None:
        _require(
            _git_path_exists(repo, submission["commit_id"], EXPECTED_REVIEW_REQUEST_DOCUMENT),
            "IAR-1 review request document absent at exact review submission commit",
        )
        _require(
            _git_path_exists(repo, EXPECTED_REVIEWED_COMMIT, EXPECTED_REVIEW_PROTOCOL_DOCUMENT),
            "IAR-1 review protocol absent at immutable reviewed commit",
        )
        missing = [rel for rel in exact_paths if not _git_path_exists(repo, EXPECTED_REVIEWED_COMMIT, rel)]
        _require(not missing, f"normalized input-packet path absent at reviewed commit: {missing}")


def validate(repo: Path) -> None:
    independence = _load(repo / EVIDENCE_PATH, "IAR-1 independence evidence")
    result = _load(repo / RESULT_PATH, "IAR-1 result")
    packet = _load(repo / PACKET_EVIDENCE_PATH, "IAR-1 input-packet evidence")
    validate_cross_records(independence, result, packet, repo=repo)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    try:
        validate(args.repo.resolve())
    except IndependenceEvidenceError as exc:
        print(f"IAR-1 independence evidence failed: {exc}", file=sys.stderr)
        return 1
    print("IAR-1 independence evidence passed; exact review submission/result/request and mandatory named-file packet are cross-bound without inventing per-file reviewer telemetry")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
