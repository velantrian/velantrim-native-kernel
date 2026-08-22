#!/usr/bin/env python3
"""Evaluate ADR-0028 H11 qualification without changing execution authority.

A QUALIFIED result is only a bounded reviewer-role result. It always stops and
requires a separate A10_H11_EXECUTION_ADMISSION reassessment.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Mapping

POLICY_PATH = Path("docs/research/H11_POSITIVE_QUALIFICATION_POLICY.json")
POLICY_PROTOCOL = "nk-h11-positive-qualification-policy/1"
REQUEST_PROTOCOL = "nk-h11-positive-qualification-request/1"
RESULT_PROTOCOL = "nk-h11-positive-qualification-evaluation/1"
DECLARATION_PROTOCOL = "nk-h11-reviewer-declaration/1"
ATTESTATION_PROTOCOL = "nk-h11-independent-attestation/1"
EXPERIMENT_ID = "H11-001"
PLAN_ID = "H11-001-c5-lab-canon-separation-v1"
PLAN_SHA256 = "60da649e675b79b3e70bf8a61cf03cb4d57bb989f4934b65ab8d50c925b19914"
REPOSITORY = "velantrian/velantrim-native-kernel"
REPOSITORY_OWNER = "velantrian"
REPOSITORY_OWNER_ID = 219592172
REVIEW_PR = 131
CANDIDATE_URL_RE = re.compile(
    r"^https://api\.github\.com/repos/velantrian/velantrim-native-kernel/pulls/131/reviews/(?P<id>[0-9]+)$"
)
SECOND_URL_RE = re.compile(
    r"^https://api\.github\.com/repos/(?P<owner>[^/]+)/(?P<repo>[^/]+)/(?:(?:issues/comments/(?P<comment_id>[0-9]+))|(?:pulls/(?P<pr>[0-9]+)/reviews/(?P<review_id>[0-9]+)))$"
)
DECLARATION_FIELD_ORDER = [
    "protocol",
    "experiment_id",
    "source_plan_id",
    "source_plan_sha256",
    "reviewer_login",
    "reviewer_role",
    "authorship_relation",
    "custody_relation",
    "conflicts",
    "repository_visible_frozen_inputs_only",
    "private_implementation_state_used",
    "statement",
]
DECLARATION_KEYS = set(DECLARATION_FIELD_ORDER)
ATTESTATION_KEYS = {
    "protocol",
    "experiment_id",
    "source_plan_id",
    "source_plan_sha256",
    "reviewer_login",
    "basis_type",
    "issuer_role",
    "attested_authorship_relation",
    "attested_custody_relation",
    "attested_conflicts",
    "attested_repository_visible_frozen_inputs_only",
    "attested_private_implementation_state_used",
    "statement",
}
REQUEST_KEYS = {
    "protocol",
    "experiment_id",
    "source_plan_id",
    "source_plan_sha256",
    "evaluated_at",
    "candidate_review_api_url",
    "second_basis_api_urls",
}
REVIEWER_ROLES = {"REVIEWER", "REPRODUCER", "REVIEWER_AND_REPRODUCER"}
AUTHORSHIP_VALUES = {
    "NOT_AUTHOR_OF_PREREGISTRATION_OR_FROZEN_RUBRIC",
    "AUTHOR_OF_PREREGISTRATION",
    "AUTHOR_OF_FROZEN_RUBRIC",
    "UNKNOWN",
}
CUSTODY_VALUES = {
    "INDEPENDENT_FOR_DECLARED_SCOPE",
    "SHARED_CUSTODY_DISCLOSED",
    "SAME_CUSTODY",
    "UNKNOWN",
}
BASIS_ROLES = {
    "ORGANIZATIONAL_SEPARATION": "ORGANIZATIONAL_AUTHORITY",
    "INDEPENDENT_EVIDENCE_CUSTODY": "INDEPENDENT_CUSTODIAN",
}


class EvidenceFailure(RuntimeError):
    def __init__(self, code: str, detail: str, *, disqualified: bool = False) -> None:
        super().__init__(detail)
        self.code = code
        self.detail = detail
        self.disqualified = disqualified


def _require(condition: bool, code: str, detail: str, *, disqualified: bool = False) -> None:
    if not condition:
        raise EvidenceFailure(code, detail, disqualified=disqualified)


def _load_json(path: Path, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise EvidenceFailure("MALFORMED_EVIDENCE", f"cannot read {label}: {exc}") from exc
    _require(isinstance(value, dict), "MALFORMED_EVIDENCE", f"{label} root must be an object")
    return value


def _default_fetch_json(url: str) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "velantrim-native-kernel-h11-qualification/1",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            payload = response.read()
    except (OSError, urllib.error.URLError) as exc:
        raise EvidenceFailure(
            "UNVERIFIABLE_EVIDENCE", f"live GitHub API verification failed for {url}"
        ) from exc
    try:
        value = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise EvidenceFailure(
            "UNVERIFIABLE_EVIDENCE", f"GitHub API returned invalid JSON for {url}"
        ) from exc
    _require(
        isinstance(value, dict),
        "UNVERIFIABLE_EVIDENCE",
        f"GitHub API object required for {url}",
    )
    return value


def _parse_time(value: Any, label: str) -> datetime:
    _require(isinstance(value, str) and value, "MALFORMED_EVIDENCE", f"{label} timestamp required")
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise EvidenceFailure("MALFORMED_EVIDENCE", f"{label} timestamp invalid") from exc
    _require(parsed.tzinfo is not None, "MALFORMED_EVIDENCE", f"{label} timestamp must include timezone")
    return parsed.astimezone(timezone.utc)


def _require_fresh(observed: Any, evaluated_at: datetime, max_age_days: int, label: str) -> str:
    observed_at = _parse_time(observed, label)
    age_seconds = (evaluated_at - observed_at).total_seconds()
    _require(age_seconds >= 0, "UNVERIFIABLE_EVIDENCE", f"{label} occurs after evaluated_at")
    _require(
        age_seconds <= max_age_days * 86400,
        "STALE_EVIDENCE",
        f"{label} is older than {max_age_days} days",
    )
    return observed_at.isoformat().replace("+00:00", "Z")


def _body_json(event: Mapping[str, Any], *, keys: set[str], label: str) -> dict[str, Any]:
    body = event.get("body")
    _require(
        isinstance(body, str) and body.strip(),
        "MALFORMED_EVIDENCE",
        f"{label} body must be JSON text",
    )
    try:
        value = json.loads(body)
    except json.JSONDecodeError as exc:
        raise EvidenceFailure("MALFORMED_EVIDENCE", f"{label} body is not valid JSON") from exc
    _require(isinstance(value, dict), "MALFORMED_EVIDENCE", f"{label} body root must be an object")
    _require(set(value) == keys, "MALFORMED_EVIDENCE", f"{label} fields drift")
    return value


def _validate_policy(policy: Mapping[str, Any]) -> None:
    _require(policy.get("protocol") == POLICY_PROTOCOL, "MALFORMED_EVIDENCE", "policy protocol drift")
    _require(
        policy.get("decision") == "ADR-0028"
        and policy.get("selected_option") == "OPTION_C_HYBRID_TWO_BASIS",
        "MALFORMED_EVIDENCE",
        "policy decision drift",
    )
    _require(policy.get("scope") == "H11_REVIEWER_REPRODUCER_ONLY", "MALFORMED_EVIDENCE", "policy scope drift")
    _require(
        isinstance(policy.get("claim_boundary"), str) and bool(policy.get("claim_boundary")),
        "MALFORMED_EVIDENCE",
        "policy claim boundary required",
    )
    _require(
        policy.get("experiment_id") == EXPERIMENT_ID
        and policy.get("source_plan_id") == PLAN_ID
        and policy.get("source_plan_sha256") == PLAN_SHA256,
        "MALFORMED_EVIDENCE",
        "policy plan binding drift",
    )
    surface = policy.get("review_surface")
    _require(isinstance(surface, Mapping), "MALFORMED_EVIDENCE", "review surface policy required")
    _require(
        surface.get("repository") == REPOSITORY
        and surface.get("pull_request") == REVIEW_PR
        and surface.get("accepted_action") == "PULL_REQUEST_REVIEW"
        and surface.get("candidate_must_not_equal_repository_owner") is True,
        "MALFORMED_EVIDENCE",
        "review surface drift",
    )
    basis1 = policy.get("basis_1")
    basis2 = policy.get("basis_2")
    _require(isinstance(basis1, Mapping) and isinstance(basis2, Mapping), "MALFORMED_EVIDENCE", "basis policies required")
    _require(
        basis1.get("required") is True
        and basis1.get("verification_method") == "LIVE_GITHUB_API"
        and basis1.get("declaration_protocol") == DECLARATION_PROTOCOL
        and basis1.get("max_age_days") == 30
        and basis1.get("required_fields") == DECLARATION_FIELD_ORDER,
        "MALFORMED_EVIDENCE",
        "basis 1 policy drift",
    )
    _require(
        basis2.get("required") is True
        and basis2.get("verification_method") == "LIVE_GITHUB_API"
        and basis2.get("attestation_protocol") == ATTESTATION_PROTOCOL
        and basis2.get("max_age_days") == 90,
        "MALFORMED_EVIDENCE",
        "basis 2 policy drift",
    )
    _require(
        basis2.get("required_basis_types") == list(BASIS_ROLES),
        "MALFORMED_EVIDENCE",
        "basis 2 required types drift",
    )
    _require(basis2.get("required_issuer_roles") == BASIS_ROLES, "MALFORMED_EVIDENCE", "basis 2 issuer roles drift")
    _require(
        basis2.get("minimum_distinct_issuers") == 2
        and basis2.get("minimum_distinct_public_repositories") == 2,
        "MALFORMED_EVIDENCE",
        "basis 2 distinctness floor drift",
    )
    _require(basis2.get("repository_owner_type") == "Organization", "MALFORMED_EVIDENCE", "basis 2 repository owner type drift")
    _require(basis2.get("issuer_author_association") == ["MEMBER", "OWNER"], "MALFORMED_EVIDENCE", "basis 2 issuer association drift")
    for key in (
        "issuer_must_not_equal_candidate",
        "issuer_must_not_equal_repository_owner",
        "evidence_repository_owner_must_not_equal_candidate",
        "evidence_repository_owner_must_not_equal_repository_owner",
    ):
        _require(basis2.get(key) is True, "MALFORMED_EVIDENCE", f"basis 2 separation rule {key} must remain true")
    qualification = policy.get("qualification")
    _require(isinstance(qualification, Mapping), "MALFORMED_EVIDENCE", "qualification policy required")
    _require(
        qualification.get("result_vocabulary")
        == ["QUALIFIED", "NOT_ESTABLISHED", "DISQUALIFIED"],
        "MALFORMED_EVIDENCE",
        "qualification result vocabulary drift",
    )
    boundary = policy.get("authority_boundary")
    _require(isinstance(boundary, Mapping), "MALFORMED_EVIDENCE", "authority boundary required")
    for key in (
        "qualification_changes_execution_admission",
        "qualification_authorizes_h11_execution",
        "qualification_authorizes_dependency_graph_execution",
        "qualification_authorizes_semantic_adjudication",
        "qualification_thaws_runtime",
        "qualification_promotes_final_canon",
        "qualification_authorizes_production",
    ):
        _require(boundary.get(key) is False, "MALFORMED_EVIDENCE", f"{key} must remain false")
    _require(
        boundary.get("qualified_next_action")
        == "SEPARATE_A10_H11_EXECUTION_ADMISSION_REASSESSMENT",
        "MALFORMED_EVIDENCE",
        "qualified next action drift",
    )


def _validate_request(request: Mapping[str, Any]) -> datetime:
    _require(set(request) == REQUEST_KEYS, "MALFORMED_EVIDENCE", "evaluation request fields drift")
    _require(request.get("protocol") == REQUEST_PROTOCOL, "MALFORMED_EVIDENCE", "request protocol drift")
    _require(
        request.get("experiment_id") == EXPERIMENT_ID
        and request.get("source_plan_id") == PLAN_ID
        and request.get("source_plan_sha256") == PLAN_SHA256,
        "MALFORMED_EVIDENCE",
        "request plan binding drift",
    )
    candidate_url = request.get("candidate_review_api_url")
    _require(
        isinstance(candidate_url, str) and CANDIDATE_URL_RE.fullmatch(candidate_url) is not None,
        "MALFORMED_EVIDENCE",
        "candidate review URL must bind PR #131",
    )
    second_urls = request.get("second_basis_api_urls")
    _require(
        isinstance(second_urls, list) and len(second_urls) == 2,
        "MISSING_EVIDENCE",
        "exactly two second-basis URLs are required",
    )
    _require(
        all(isinstance(url, str) and SECOND_URL_RE.fullmatch(url) is not None for url in second_urls),
        "MALFORMED_EVIDENCE",
        "second-basis URLs must be supported public GitHub API objects",
    )
    _require(len(set(second_urls)) == 2, "MISSING_EVIDENCE", "second-basis URLs must be distinct")
    return _parse_time(request.get("evaluated_at"), "evaluated_at")


def _event_actor(event: Mapping[str, Any], label: str) -> tuple[str, int]:
    user = event.get("user")
    _require(isinstance(user, Mapping), "UNVERIFIABLE_EVIDENCE", f"{label} GitHub user object required")
    login = user.get("login")
    actor_id = user.get("id")
    _require(isinstance(login, str) and login, "UNVERIFIABLE_EVIDENCE", f"{label} GitHub login required")
    _require(
        isinstance(actor_id, int) and not isinstance(actor_id, bool),
        "UNVERIFIABLE_EVIDENCE",
        f"{label} GitHub actor id required",
    )
    return login, actor_id


def _validate_candidate_event(
    url: str,
    event: Mapping[str, Any],
    evaluated_at: datetime,
    max_age_days: int,
) -> tuple[dict[str, Any], dict[str, Any]]:
    match = CANDIDATE_URL_RE.fullmatch(url)
    _require(match is not None, "MALFORMED_EVIDENCE", "candidate review URL invalid")
    expected_id = int(match.group("id"))
    _require(
        event.get("url") == url and event.get("id") == expected_id,
        "UNVERIFIABLE_EVIDENCE",
        "candidate review event identity mismatch",
    )
    _require(
        event.get("pull_request_url")
        == f"https://api.github.com/repos/{REPOSITORY}/pulls/{REVIEW_PR}",
        "UNVERIFIABLE_EVIDENCE",
        "candidate review is not bound to PR #131",
    )
    _require(
        event.get("state") in {"COMMENTED", "APPROVED", "CHANGES_REQUESTED"},
        "UNVERIFIABLE_EVIDENCE",
        "candidate review state is not active",
    )
    login, actor_id = _event_actor(event, "candidate review")
    _require(
        login.lower() != REPOSITORY_OWNER and actor_id != REPOSITORY_OWNER_ID,
        "OWNER_OR_SELF_REVIEW",
        "repository owner cannot qualify as the independent H11 reviewer",
        disqualified=True,
    )
    submitted_at = _require_fresh(event.get("submitted_at"), evaluated_at, max_age_days, "candidate review")
    declaration = _body_json(event, keys=DECLARATION_KEYS, label="candidate declaration")
    _require(
        declaration.get("protocol") == DECLARATION_PROTOCOL
        and declaration.get("experiment_id") == EXPERIMENT_ID
        and declaration.get("source_plan_id") == PLAN_ID
        and declaration.get("source_plan_sha256") == PLAN_SHA256,
        "MALFORMED_EVIDENCE",
        "candidate declaration plan binding drift",
    )
    _require(
        declaration.get("reviewer_login") == login,
        "UNVERIFIABLE_EVIDENCE",
        "candidate declaration login does not match authenticated GitHub actor",
    )
    _require(declaration.get("reviewer_role") in REVIEWER_ROLES, "MALFORMED_EVIDENCE", "candidate reviewer role invalid")
    authorship = declaration.get("authorship_relation")
    custody = declaration.get("custody_relation")
    _require(authorship in AUTHORSHIP_VALUES, "MALFORMED_EVIDENCE", "candidate authorship relation invalid")
    _require(custody in CUSTODY_VALUES, "MALFORMED_EVIDENCE", "candidate custody relation invalid")
    if authorship in {"AUTHOR_OF_PREREGISTRATION", "AUTHOR_OF_FROZEN_RUBRIC"}:
        raise EvidenceFailure(
            "AUTHOR_OF_PREREGISTRATION_OR_FROZEN_RUBRIC",
            "candidate authored the frozen H11 preregistration/rubric",
            disqualified=True,
        )
    _require(authorship != "UNKNOWN", "AMBIGUOUS_EVIDENCE", "candidate authorship relation is unknown")
    if custody == "SAME_CUSTODY":
        raise EvidenceFailure("SAME_CUSTODY", "candidate shares prohibited H11 custody", disqualified=True)
    _require(custody == "INDEPENDENT_FOR_DECLARED_SCOPE", "AMBIGUOUS_EVIDENCE", "candidate custody independence is not established")
    conflicts = declaration.get("conflicts")
    _require(
        isinstance(conflicts, list) and all(isinstance(item, str) and item for item in conflicts),
        "MALFORMED_EVIDENCE",
        "candidate conflicts must be a string array",
    )
    _require(conflicts == [], "UNRESOLVED_CONFLICTS", "candidate has unresolved conflicts/material dependence")
    if declaration.get("repository_visible_frozen_inputs_only") is not True:
        raise EvidenceFailure(
            "FROZEN_INPUT_BOUNDARY_VIOLATED",
            "candidate did not use repository-visible frozen inputs only",
            disqualified=True,
        )
    if declaration.get("private_implementation_state_used") is not False:
        raise EvidenceFailure(
            "PRIVATE_IMPLEMENTATION_STATE_USED",
            "candidate used private implementation state",
            disqualified=True,
        )
    _require(
        isinstance(declaration.get("statement"), str) and declaration.get("statement"),
        "MALFORMED_EVIDENCE",
        "candidate statement required",
    )
    return declaration, {
        "api_url": url,
        "event_type": "PULL_REQUEST_REVIEW",
        "repository": REPOSITORY,
        "pull_request": REVIEW_PR,
        "actor_login": login,
        "actor_id": actor_id,
        "event_id": expected_id,
        "observed_at": submitted_at,
    }


def _validate_public_evidence_repository(
    repository: str,
    owner: str,
    candidate_login: str,
    candidate_actor_id: int,
    fetch_json: Callable[[str], Mapping[str, Any]],
) -> dict[str, Any]:
    api_url = f"https://api.github.com/repos/{repository}"
    metadata = fetch_json(api_url)
    _require(isinstance(metadata, Mapping), "UNVERIFIABLE_EVIDENCE", "evidence repository metadata required")
    _require(
        str(metadata.get("full_name", "")).lower() == repository.lower(),
        "UNVERIFIABLE_EVIDENCE",
        "evidence repository full_name mismatch",
    )
    _require(metadata.get("private") is False, "UNVERIFIABLE_EVIDENCE", "second-basis repository must be public")
    repo_owner = metadata.get("owner")
    _require(isinstance(repo_owner, Mapping), "UNVERIFIABLE_EVIDENCE", "evidence repository owner metadata required")
    owner_login = repo_owner.get("login")
    owner_id = repo_owner.get("id")
    owner_type = repo_owner.get("type")
    _require(
        isinstance(owner_login, str) and owner_login.lower() == owner.lower(),
        "UNVERIFIABLE_EVIDENCE",
        "evidence repository owner mismatch",
    )
    _require(owner_type == "Organization", "UNVERIFIABLE_EVIDENCE", "second-basis repository owner must be a GitHub Organization")
    _require(
        owner_login.lower() not in {REPOSITORY_OWNER, candidate_login.lower()},
        "UNVERIFIABLE_EVIDENCE",
        "evidence repository owner conflicts with subject owner/candidate",
    )
    _require(
        isinstance(owner_id, int) and owner_id not in {REPOSITORY_OWNER_ID, candidate_actor_id},
        "UNVERIFIABLE_EVIDENCE",
        "evidence repository owner id conflicts with subject owner/candidate",
    )
    return {
        "api_url": api_url,
        "event_type": "PUBLIC_REPOSITORY_METADATA",
        "repository": repository,
        "owner_login": owner_login,
        "owner_id": owner_id,
        "owner_type": owner_type,
        "private": False,
    }


def _validate_second_basis_event(
    url: str,
    event: Mapping[str, Any],
    candidate_login: str,
    candidate_actor_id: int,
    declaration: Mapping[str, Any],
    evaluated_at: datetime,
    max_age_days: int,
) -> tuple[str, str, int, str, dict[str, Any]]:
    match = SECOND_URL_RE.fullmatch(url)
    _require(match is not None, "MALFORMED_EVIDENCE", "unsupported second-basis URL")
    owner = match.group("owner")
    repo = match.group("repo")
    repository = f"{owner}/{repo}"
    is_review = match.group("review_id") is not None
    expected_id = int(match.group("review_id") or match.group("comment_id"))
    _require(repository.lower() != REPOSITORY.lower(), "UNVERIFIABLE_EVIDENCE", "second-basis evidence must be outside the subject repository")
    _require(
        event.get("url") == url and event.get("id") == expected_id,
        "UNVERIFIABLE_EVIDENCE",
        "second-basis event identity mismatch",
    )
    if is_review:
        _require(
            event.get("pull_request_url")
            == f"https://api.github.com/repos/{repository}/pulls/{match.group('pr')}",
            "UNVERIFIABLE_EVIDENCE",
            "second-basis review PR binding mismatch",
        )
    else:
        issue_url = event.get("issue_url")
        _require(
            isinstance(issue_url, str)
            and issue_url.startswith(f"https://api.github.com/repos/{repository}/issues/"),
            "UNVERIFIABLE_EVIDENCE",
            "second-basis comment issue binding mismatch",
        )
    issuer_login, issuer_id = _event_actor(event, "second-basis evidence")
    _require(
        issuer_login.lower() != REPOSITORY_OWNER and issuer_id != REPOSITORY_OWNER_ID,
        "UNVERIFIABLE_EVIDENCE",
        "repository owner cannot issue the independent second basis",
    )
    _require(
        issuer_login.lower() != candidate_login.lower() and issuer_id != candidate_actor_id,
        "UNVERIFIABLE_EVIDENCE",
        "candidate cannot issue their own second-basis attestation",
    )
    _require(
        event.get("author_association") in {"MEMBER", "OWNER"},
        "UNVERIFIABLE_EVIDENCE",
        "second-basis issuer must be an organization member/owner for that repository",
    )
    observed_at = _require_fresh(
        event.get("submitted_at") if is_review else event.get("created_at"),
        evaluated_at,
        max_age_days,
        "second-basis evidence",
    )
    attestation = _body_json(event, keys=ATTESTATION_KEYS, label="independent attestation")
    _require(
        attestation.get("protocol") == ATTESTATION_PROTOCOL
        and attestation.get("experiment_id") == EXPERIMENT_ID
        and attestation.get("source_plan_id") == PLAN_ID
        and attestation.get("source_plan_sha256") == PLAN_SHA256,
        "MALFORMED_EVIDENCE",
        "independent attestation plan binding drift",
    )
    _require(
        attestation.get("reviewer_login") == candidate_login,
        "CONTRADICTORY_ATTESTATIONS",
        "independent attestation targets a different reviewer",
    )
    basis_type = attestation.get("basis_type")
    _require(basis_type in BASIS_ROLES, "MALFORMED_EVIDENCE", "independent attestation basis type invalid")
    _require(
        attestation.get("issuer_role") == BASIS_ROLES[basis_type],
        "MALFORMED_EVIDENCE",
        "independent attestation issuer role mismatch",
    )
    _require(
        attestation.get("attested_authorship_relation") == declaration.get("authorship_relation")
        and attestation.get("attested_custody_relation") == declaration.get("custody_relation")
        and attestation.get("attested_conflicts") == declaration.get("conflicts")
        and attestation.get("attested_repository_visible_frozen_inputs_only")
        == declaration.get("repository_visible_frozen_inputs_only")
        and attestation.get("attested_private_implementation_state_used")
        == declaration.get("private_implementation_state_used"),
        "CONTRADICTORY_ATTESTATIONS",
        "independent attestation contradicts the candidate declaration",
    )
    _require(
        isinstance(attestation.get("statement"), str) and attestation.get("statement"),
        "MALFORMED_EVIDENCE",
        "independent attestation statement required",
    )
    return str(basis_type), issuer_login, issuer_id, repository, {
        "api_url": url,
        "event_type": "PULL_REQUEST_REVIEW" if is_review else "ISSUE_COMMENT",
        "repository": repository,
        "actor_login": issuer_login,
        "actor_id": issuer_id,
        "event_id": expected_id,
        "basis_type": basis_type,
        "observed_at": observed_at,
    }


def _result(
    status: str,
    reasons: list[str],
    *,
    candidate_login: str | None = None,
    basis1_verified: bool = False,
    basis2_verified: bool = False,
    evidence: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    return {
        "protocol": RESULT_PROTOCOL,
        "experiment_id": EXPERIMENT_ID,
        "source_plan_id": PLAN_ID,
        "source_plan_sha256": PLAN_SHA256,
        "qualification_result": status,
        "candidate_login": candidate_login,
        "basis_1_verified": basis1_verified,
        "basis_2_verified": basis2_verified,
        "reasons": reasons,
        "verified_evidence": evidence or [],
        "execution_admission_changed": False,
        "h11_execution_authorized": False,
        "dependency_graph_execution_authorized": False,
        "semantic_adjudication_authorized": False,
        "runtime_thaw_authorized": False,
        "final_canon_authorized": False,
        "production_authorized": False,
        "stop_required_if_qualified": status == "QUALIFIED",
        "next_action": (
            "SEPARATE_A10_H11_EXECUTION_ADMISSION_REASSESSMENT"
            if status == "QUALIFIED"
            else "REMAIN_BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER"
        ),
    }


def evaluate(
    request: Mapping[str, Any],
    *,
    policy: Mapping[str, Any],
    fetch_json: Callable[[str], Mapping[str, Any]] = _default_fetch_json,
) -> dict[str, Any]:
    candidate_login: str | None = None
    basis1_verified = False
    evidence: list[dict[str, Any]] = []
    try:
        _validate_policy(policy)
        evaluated_at = _validate_request(request)
        basis1_policy = policy["basis_1"]
        basis2_policy = policy["basis_2"]
        candidate_url = str(request["candidate_review_api_url"])
        candidate_event = fetch_json(candidate_url)
        declaration, candidate_evidence = _validate_candidate_event(
            candidate_url,
            candidate_event,
            evaluated_at,
            int(basis1_policy["max_age_days"]),
        )
        candidate_login = str(declaration["reviewer_login"])
        candidate_actor_id = int(candidate_evidence["actor_id"])
        basis1_verified = True
        evidence.append(candidate_evidence)

        basis_types: set[str] = set()
        issuer_logins: set[str] = set()
        issuer_ids: set[int] = set()
        repositories: set[str] = set()
        for raw_url in request["second_basis_api_urls"]:
            url = str(raw_url)
            match = SECOND_URL_RE.fullmatch(url)
            _require(match is not None, "MALFORMED_EVIDENCE", "unsupported second-basis URL")
            repository = f"{match.group('owner')}/{match.group('repo')}"
            evidence.append(
                _validate_public_evidence_repository(
                    repository,
                    str(match.group("owner")),
                    candidate_login,
                    candidate_actor_id,
                    fetch_json,
                )
            )
            event = fetch_json(url)
            basis_type, issuer_login, issuer_id, repository, verified = _validate_second_basis_event(
                url,
                event,
                candidate_login,
                candidate_actor_id,
                declaration,
                evaluated_at,
                int(basis2_policy["max_age_days"]),
            )
            _require(
                basis_type not in basis_types,
                "MISSING_EVIDENCE",
                "second basis must cover distinct required basis types",
            )
            basis_types.add(basis_type)
            issuer_logins.add(issuer_login.lower())
            issuer_ids.add(issuer_id)
            repositories.add(repository.lower())
            evidence.append(verified)

        _require(
            basis_types == set(BASIS_ROLES),
            "MISSING_EVIDENCE",
            "organizational separation and independent custody attestations are both required",
        )
        minimum_issuers = int(basis2_policy["minimum_distinct_issuers"])
        _require(
            len(issuer_logins) >= minimum_issuers and len(issuer_ids) >= minimum_issuers,
            "NON_DISTINCT_ISSUERS",
            "second-basis issuers must be distinct",
        )
        _require(
            len(repositories) >= int(basis2_policy["minimum_distinct_public_repositories"]),
            "NON_DISTINCT_EVIDENCE_REPOSITORIES",
            "second-basis evidence repositories must be distinct",
        )
        return _result(
            "QUALIFIED",
            [
                "BASIS_1_VERIFIED",
                "BASIS_2_VERIFIED",
                "NO_CONTRADICTIONS",
                "SEPARATE_ADMISSION_REASSESSMENT_REQUIRED",
            ],
            candidate_login=candidate_login,
            basis1_verified=True,
            basis2_verified=True,
            evidence=evidence,
        )
    except EvidenceFailure as exc:
        return _result(
            "DISQUALIFIED" if exc.disqualified else "NOT_ESTABLISHED",
            [exc.code],
            candidate_login=candidate_login,
            basis1_verified=basis1_verified,
            basis2_verified=False,
            evidence=evidence,
        )
    except (KeyError, TypeError, ValueError):
        return _result(
            "NOT_ESTABLISHED",
            ["MALFORMED_EVIDENCE"],
            candidate_login=candidate_login,
            basis1_verified=basis1_verified,
            basis2_verified=False,
            evidence=evidence,
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", type=Path)
    parser.add_argument("--policy", type=Path, default=POLICY_PATH)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        request = _load_json(args.request, "positive qualification request")
        policy = _load_json(args.policy, "positive qualification policy")
        result = evaluate(request, policy=policy)
    except EvidenceFailure as exc:
        result = _result("NOT_ESTABLISHED", [exc.code])
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(rendered, encoding="utf-8")
    sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
