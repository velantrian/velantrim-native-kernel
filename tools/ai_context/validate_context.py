#!/usr/bin/env python3
"""Validate Native Kernel AI continuity and post-blueprint truth surfaces."""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

REQUIRED_PATHS = (
    "AGENTS.md", "STATUS.md", "ROADMAP.md", "project-state.json",
    ".github/copilot-instructions.md", ".github/pull_request_template.md",
    "contracts/project-state-v1.schema.json", "contracts/project-state-v2.schema.json",
    "contracts/evidence-bundle-v1.schema.json", "evidence/c5/README.md",
    "evidence/c5/2026-08-07/manifest.json", "evidence/c5/2026-08-08-adr0023/manifest.json",
    "docs/ARCHITECTURE_REFOUNDATION.md", "docs/ARCHITECTURE_REFOUNDATION.ru.md",
    "docs/INTEGRATED_A1_A10_REVIEW.md", "docs/INTEGRATED_A1_A10_REVIEW.ru.md",
    "docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md", "docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md",
    "docs/reviews/IAR-1_RESULT.md", "docs/reviews/IAR-1_RESULT.ru.md", "docs/reviews/IAR-1_RESULT.json",
    "docs/reviews/IAR-1_RECONCILIATION.md", "docs/reviews/IAR-1_RECONCILIATION.ru.md", "docs/reviews/IAR-1_RECONCILIATION.json",
    "docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.md", "docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md",
    "docs/A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md", "docs/A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md",
    "docs/A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md", "docs/A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md",
    "docs/A4_SEMANTIC_LAWS_AND_INVARIANTS.md", "docs/A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md",
    "docs/A5_IDENTITY_TIME_AND_CHANGE.md", "docs/A5_IDENTITY_TIME_AND_CHANGE.ru.md",
    "docs/A6_KNOWLEDGE_LIFECYCLE.md", "docs/A6_KNOWLEDGE_LIFECYCLE.ru.md",
    "docs/A7_CONFLICT_UNCERTAINTY_AND_REVISION.md", "docs/A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md",
    "docs/A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md", "docs/A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md",
    "docs/A9_REFERENCE_LABORATORY_BOUNDARY.md", "docs/A9_REFERENCE_LABORATORY_BOUNDARY.ru.md",
    "docs/A10_OPEN_QUESTIONS_AND_FALSIFICATION.md", "docs/A10_OPEN_QUESTIONS_AND_FALSIFICATION.ru.md",
    "docs/adr/0025-blueprint-before-runtime-expansion.md",
    "docs/adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md",
    "docs/ai/README.md", "docs/ai/CURRENT_STATE.md", "docs/ai/COMPONENT_MAP.md",
    "docs/ai/KNOWN_RISKS.md", "docs/ai/WORK_LOG.md", "docs/ai/ISSUE_RECONCILIATION.md",
    "docs/ai/NOTION_HANDOFF.md",
)

LINK_SCAN_PATHS = REQUIRED_PATHS + (
    "README.md", "README.ru.md", "CONTRIBUTING.md", "docs/README.md", "docs/README.ru.md", "docs/adr/README.md",
)

CHECKPOINT_RE = re.compile(r"^machine_truth_reconciliation_merge:\s*([0-9a-f]{40})\s*$", re.MULTILINE)
MARKDOWN_LINK_RE = re.compile(r"(?<!\!)\[[^\]]+\]\(([^)]+)\)")
IGNORED_SCHEMES = {"http", "https", "mailto", "tel", "data"}

# These compatibility names are intentionally retained because the unit-test
# suite imports them as part of the validator's tested interface.
REQUIRED_STATUS_MARKERS = (
    "RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY",
    "authoritative_machine_source: ../../project-state.json",
    "machine_protocol: nk-project-state/2",
    "0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED",
    "C5 bounded rehearsal ≠ production readiness",
    "repository-resident evidence ≠ independent custody",
    "logical ERASED ≠ physical deletion",
    "public repository ≠ open-source license",
    "No AI agent may select the license or accept ADR-0024",
    "The later Notion synchronization checkpoint does not rewrite or replace the earlier publication checkpoint.",
    "Architecture Re-foundation: `BLUEPRINT COMPLETE / PROVISIONAL / VALIDATION ACTIVE`",
    "blueprint content A1-A10: DRAFTED / PROVISIONAL / RECONCILED BY OVERLAY",
    "integrated review: COMPLETED / PROVISIONAL",
    "operator post-blueprint choice: OPTION D / ADR-0026 / APPROVED",
    "IAR-1: QUALIFYING_REVIEW_COMPLETE",
    "IAR-1-R1 reconciliation: COMPLETE",
    "next bounded gate: BPV1_PLAN_AND_PREREGISTRATION",
    "BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN",
)
CURRENT_MARKERS = REQUIRED_STATUS_MARKERS

FORBIDDEN_STATUS_MARKERS = (
    "next bounded gate is `INTEGRATED_A1_A10_REVIEW`",
    "next bounded content slice is `A10 — Open Questions and Falsification`",
    "Next work is limited to explicit operator decisions",
    "next bounded gate is `OPERATOR_POST_BLUEPRINT_DECISION`",
    "next bounded gate is INDEPENDENT_ARCHITECTURE_REVIEW",
    "independent architectural validation: NOT ESTABLISHED",
    "BPV-1: BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION",
)

BLUEPRINT_PROGRESS_SURFACES = {
    "STATUS.md": (
        "blueprint content: A1-A10 DRAFTED / PROVISIONAL / RECONCILED BY OVERLAY",
        "IAR-1: QUALIFYING_REVIEW_COMPLETE",
        "IAR-1-R1 reconciliation: COMPLETE",
        "next content gate: BPV1_PLAN_AND_PREREGISTRATION",
        "BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN",
    ),
    "ROADMAP.md": (
        "integrated A1-A10 review                 COMPLETE / PROVISIONAL",
        "OPERATOR_POST_BLUEPRINT_DECISION         COMPLETE / OPTION D / ADR-0026",
        "INDEPENDENT_ARCHITECTURE_REVIEW          COMPLETE / IAR-1 / QUALIFYING",
        "REVIEW_FINDING_RECONCILIATION            COMPLETE / IAR-1-R1",
        "BPV1_PLAN_AND_PREREGISTRATION            NEXT GATE",
        "BPV-1 CROSS-LINEAGE FALSIFICATION        BLOCKED BY PREREGISTERED PLAN",
    ),
    "docs/ARCHITECTURE_REFOUNDATION.md": (
        "Independent architecture review: IAR-1 / QUALIFYING_REVIEW_COMPLETE",
        "Review finding reconciliation: IAR-1-R1 / COMPLETE",
        "Next bounded gate: BPV1_PLAN_AND_PREREGISTRATION",
        "BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN",
    ),
    "docs/ARCHITECTURE_REFOUNDATION.ru.md": (
        "Independent architecture review: IAR-1 / QUALIFYING_REVIEW_COMPLETE",
        "Review finding reconciliation: IAR-1-R1 / COMPLETE",
        "Next bounded gate: BPV1_PLAN_AND_PREREGISTRATION",
        "BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN",
    ),
    "docs/ai/README.md": (
        "IAR-1: QUALIFYING_REVIEW_COMPLETE",
        "IAR-1-R1 reconciliation: COMPLETE",
        "next gate: BPV1_PLAN_AND_PREREGISTRATION",
        "BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN",
    ),
    "docs/INTEGRATED_A1_A10_REVIEW.md": (
        "nk-integrated-blueprint-review/A1-A10-review-1",
        "no known blocking internal semantic contradiction remains",
        "OPERATOR_POST_BLUEPRINT_DECISION",
    ),
    "docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md": (
        "nk-independent-architecture-review/1",
        "AUTHORIZED / REVIEW NOT YET ESTABLISHED",
        "BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION",
        "BLOCKED_NO_QUALIFYING_REVIEWER",
    ),
    "docs/reviews/IAR-1_RESULT.md": (
        "QUALIFYING_REVIEW_COMPLETE",
        "10 findings",
        "7",
        "BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION",
    ),
    "docs/reviews/IAR-1_RECONCILIATION.md": (
        "IAR-1-R1",
        "BPV1_PLAN_AND_PREREGISTRATION",
        "BLOCKED_PENDING_PREREGISTERED_PLAN",
        "open BLOCKING findings: 0",
    ),
}
SURFACE_MARKERS = BLUEPRINT_PROGRESS_SURFACES

FORBIDDEN_BLUEPRINT_PROGRESS_MARKERS = (
    "next content slice: INTEGRATED_A1_A10_REVIEW",
    "Next bounded gate: INTEGRATED_A1_A10_REVIEW",
    "→ integrated A1-A10 review                     NEXT GATE",
    "next content slice: OPERATOR_POST_BLUEPRINT_DECISION",
    "Next bounded gate: OPERATOR_POST_BLUEPRINT_DECISION",
    "next content gate: INDEPENDENT_ARCHITECTURE_REVIEW",
    "Next bounded gate: INDEPENDENT_ARCHITECTURE_REVIEW",
    "INDEPENDENT_ARCHITECTURE_REVIEW          NEXT GATE",
)
FORBIDDEN_PROGRESS = FORBIDDEN_BLUEPRINT_PROGRESS_MARKERS


@dataclass(frozen=True)
class Finding:
    path: str
    message: str

    def render(self) -> str:
        return f"{self.path}: {self.message}"


def _run_git(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", "-C", str(repo), *args], check=False, capture_output=True, text=True)


def validate_required_paths(repo: Path) -> list[Finding]:
    return [Finding(rel, "required AI-context file is missing") for rel in REQUIRED_PATHS if not (repo / rel).is_file()]


def _normalize_link_target(source: Path, raw_target: str, repo: Path) -> Path | None:
    target = raw_target.strip()
    if not target or target.startswith("#"):
        return None
    if target.startswith("<") and ">" in target:
        target = target[1:target.index(">")]
    elif ' "' in target:
        target = target.split(' "', 1)[0]
    elif " '" in target:
        target = target.split(" '", 1)[0]
    parsed = urlsplit(target)
    if parsed.scheme.lower() in IGNORED_SCHEMES or parsed.netloc:
        return None
    path_text = unquote(parsed.path)
    if not path_text:
        return None
    return (repo / path_text.lstrip("/") if path_text.startswith("/") else source.parent / path_text).resolve()


def validate_links(repo: Path) -> list[Finding]:
    findings: list[Finding] = []
    root = repo.resolve()
    for rel in LINK_SCAN_PATHS:
        source = repo / rel
        if not source.is_file():
            continue
        for match in MARKDOWN_LINK_RE.finditer(source.read_text(encoding="utf-8")):
            raw = match.group(1)
            candidate = _normalize_link_target(source, raw, repo)
            if candidate is None:
                continue
            try:
                candidate.relative_to(root)
            except ValueError:
                findings.append(Finding(rel, f"relative link escapes repository: {raw}"))
                continue
            if not candidate.exists():
                findings.append(Finding(rel, f"broken relative link: {raw}"))
    return findings


def validate_blueprint_progress_surfaces(repo: Path) -> list[Finding]:
    findings: list[Finding] = []
    for rel, markers in BLUEPRINT_PROGRESS_SURFACES.items():
        path = repo / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                findings.append(Finding(rel, f"required blueprint-progress marker is missing: {marker}"))
        # Protocol and historical review documents intentionally preserve their
        # publication-time gate language. Stale-current markers are forbidden
        # only on surfaces that claim to describe present progress.
        if rel not in {
            "docs/INTEGRATED_A1_A10_REVIEW.md",
            "docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md",
            "docs/reviews/IAR-1_RESULT.md",
        }:
            for stale in FORBIDDEN_BLUEPRINT_PROGRESS_MARKERS:
                if stale in text:
                    findings.append(Finding(rel, f"forbidden stale blueprint-progress marker is present: {stale}"))
    return findings


def validate_surfaces(repo: Path) -> list[Finding]:
    return validate_blueprint_progress_surfaces(repo)


def read_checkpoint(repo: Path) -> tuple[str | None, list[Finding]]:
    rel = "docs/ai/CURRENT_STATE.md"
    path = repo / rel
    if not path.is_file():
        return None, [Finding(rel, "cannot read checkpoint because file is missing")]
    text = path.read_text(encoding="utf-8")
    findings: list[Finding] = []
    match = CHECKPOINT_RE.search(text)
    if not match:
        findings.append(Finding(rel, "missing exact 40-character machine truth reconciliation checkpoint"))
        return None, findings
    for marker in REQUIRED_STATUS_MARKERS:
        if marker not in text:
            findings.append(Finding(rel, f"required current-state marker is missing: {marker}"))
    for marker in FORBIDDEN_STATUS_MARKERS:
        if marker in text:
            findings.append(Finding(rel, f"forbidden legacy current-state marker is present: {marker}"))
    return match.group(1), findings


def validate_checkpoint(repo: Path, checkpoint: str | None) -> list[Finding]:
    if checkpoint is None or not (repo / ".git").exists():
        return []
    if _run_git(repo, "cat-file", "-e", f"{checkpoint}^{{commit}}").returncode != 0:
        return [Finding("docs/ai/CURRENT_STATE.md", f"checkpoint commit does not exist: {checkpoint}")]
    return []


def validate(repo: Path) -> list[Finding]:
    findings = validate_required_paths(repo)
    findings.extend(validate_links(repo))
    findings.extend(validate_blueprint_progress_surfaces(repo))
    checkpoint, extra = read_checkpoint(repo)
    findings.extend(extra)
    findings.extend(validate_checkpoint(repo, checkpoint))
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
    print("AI context validation passed; A1-A10=provisional_reconciled; IAR-1=qualifying; reconciliation=complete; next=BPV1_PLAN_AND_PREREGISTRATION; BPV-1_execution=blocked; runtime_expansion_frozen=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
