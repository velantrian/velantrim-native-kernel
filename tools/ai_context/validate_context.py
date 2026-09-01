#!/usr/bin/env python3
"""Validate Native Kernel AI routing and current-truth surfaces."""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

# Preserve the broad continuity inventory. This validator intentionally changes
# only *where current truth is required*, not which historical/research assets
# must remain repository-resident.
REQUIRED_PATHS = (
    "ARCHITECTURE.md",
    "AGENTS.md", "README.md", "README.ru.md", "PROJECT_OVERVIEW.md", "PROJECT_OVERVIEW.ru.md",
    "STATUS.md", "ROADMAP.md", "project-state.json",
    ".github/copilot-instructions.md", ".github/pull_request_template.md",
    "contracts/project-state-v1.schema.json", "contracts/project-state-v2.schema.json",
    "contracts/evidence-bundle-v1.schema.json", "evidence/c5/README.md",
    "evidence/c5/2026-08-07/manifest.json", "evidence/c5/2026-08-08-adr0023/manifest.json",
    "docs/README.md", "docs/README.ru.md", "docs/ARCHITECTURE_REFOUNDATION.md", "docs/ARCHITECTURE_REFOUNDATION.ru.md",
    "docs/INTEGRATED_A1_A10_REVIEW.md", "docs/INTEGRATED_A1_A10_REVIEW.ru.md",
    "docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md", "docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md",
    "docs/reviews/IAR-1_RESULT.md", "docs/reviews/IAR-1_RESULT.ru.md", "docs/reviews/IAR-1_RESULT.json",
    "docs/reviews/IAR-1_RECONCILIATION.md", "docs/reviews/IAR-1_RECONCILIATION.ru.md", "docs/reviews/IAR-1_RECONCILIATION.json",
    "docs/research/BPV1_PREREGISTRATION.md", "docs/research/BPV1_PREREGISTRATION.ru.md", "docs/research/BPV1_PREREGISTRATION.json",
    "docs/research/BPV1_D5_R1_QUALIFICATION.md", "docs/research/BPV1_D5_R1_QUALIFICATION.ru.md",
    "docs/research/RESIDUAL_A10_VALIDATION_PLAN.md", "docs/research/RESIDUAL_A10_VALIDATION_PLAN.ru.md",
    "docs/research/RESIDUAL_A10_VALIDATION_PLAN.json",
    "docs/research/H11_EXECUTION_ADMISSION.json",
    "docs/research/H11_REVIEWER_REPRODUCER_QUALIFICATION.json",
    "docs/research/H11_PREREGISTRATION.md", "docs/research/H11_PREREGISTRATION.json",
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
    "docs/adr/README.md", "docs/adr/0025-blueprint-before-runtime-expansion.md",
    "docs/adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md",
    "docs/adr/0027-retain-provisional-architecture-and-runtime-freeze-after-option-d.md",
    "docs/ai/README.md", "docs/ai/CURRENT_STATE.md", "docs/ai/POST_RESIDUAL_A10_STATE.md",
    "docs/ai/COMPONENT_MAP.md", "docs/ai/KNOWN_RISKS.md", "docs/ai/WORK_LOG.md",
    "docs/ai/ISSUE_RECONCILIATION.md", "docs/ai/NOTION_HANDOFF.md",
    "docs/ai/DOCUMENTATION_STANDARD.md", "docs/ai/project_manifest.yaml",
)

LINK_SCAN_PATHS = REQUIRED_PATHS + (
    "CONTRIBUTING.md",
)

CURRENT_STATE_CHECKPOINT_RE = re.compile(
    r"^h11_state_binding_merge:\s*([0-9a-f]{40})\s*$",
    re.MULTILINE,
)
MARKDOWN_LINK_RE = re.compile(r"(?<!\!)\[[^\]]+\]\(([^)]+)\)")
IGNORED_SCHEMES = {"http", "https", "mailto", "tel", "data"}

CURRENT_SURFACE_MARKERS = {
    "docs/ai/CURRENT_STATE.md": (
        "document_role: CURRENT_STATE",
        "authoritative_machine_source: ../../project-state.json",
        "machine_protocol: nk-project-state/2",
        "selected_family: A10-H11",
        "current_gate: A10_H11_EXECUTION_ADMISSION",
        "execution_admission_state: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER",
        "qualifying_reviewer_reproducer: NOT_ESTABLISHED",
        "h11_outcome: NOT_TESTED",
        "runtime_expansion: FROZEN",
        "product_runtime_thaw: false",
        "production: false",
        "Final Canon: DEFERRED / NOT AUTHORIZED",
        "A1–A10 first-draft provenance",
        "IAR-1 reconciliation = current provisional interpretation on conflict",
    ),
    "docs/ai/README.md": (
        "A10_H11_EXECUTION_ADMISSION",
        "BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER",
        "H11: `NOT_TESTED`",
        "runtime expansion: `FROZEN`",
        "A1–A10 first-draft provenance",
        "IAR-1 reconciliation",
        "Historical/current separation",
    ),
    "ARCHITECTURE.md": (
        "A1–A10 are preserved as first-draft provenance",
        "IAR-1-R1 reconciliation is the current provisional interpretation where it conflicts with first-draft wording",
        "docs/INTEGRATED_A1_A10_REVIEW.md",
        "docs/reviews/IAR-1_RECONCILIATION.md",
    ),
    "docs/ai/project_manifest.yaml": (
        "formal_architecture: ARCHITECTURE.md",
        "formal_architecture_series_start: docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.md",
        "formal_architecture_integrated_review: docs/INTEGRATED_A1_A10_REVIEW.md",
        "formal_architecture_reconciliation: docs/reviews/IAR-1_RECONCILIATION.md",
        "formal_architecture_role: semantic_authority",
    ),
    "STATUS.md": (
        "document_role: CHRONOLOGY_ORIENTATION",
        "current_authority: docs/ai/CURRENT_STATE.md + project-state.json + live GitHub",
        "current_gate: A10_H11_EXECUTION_ADMISSION",
        "execution_admission_state: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER",
        "HISTORICAL_D5_D6_STATUS_CHECKPOINT_NOT_CURRENT",
        "Historical hard stop — superseded as current instruction",
    ),
    "ROADMAP.md": (
        "document_role: ACTIVE_ROADMAP",
        "current_gate: A10_H11_EXECUTION_ADMISSION",
        "execution_admission_state: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER",
        "HISTORICAL_D5_D6_ROADMAP_CHECKPOINT_NOT_CURRENT",
        "Historical hard stop — superseded as current instruction",
    ),
    "README.md": (
        "A1–A10 first-draft architecture documents",
        "Integrated A1–A10 Review",
        "IAR-1-R1 reconciliation",
        "follow its canonical required reading order",
    ),
    "README.ru.md": (
        "A1–A10 first-draft architecture documents",
        "Integrated A1–A10 Review",
        "IAR-1-R1 reconciliation",
        "следовать его canonical required reading order",
    ),
    "PROJECT_OVERVIEW.md": (
        "docs/A1...A10 first-draft provenance",
        "docs/INTEGRATED_A1_A10_REVIEW.md",
        "docs/reviews/IAR-1_RECONCILIATION.md",
        "follow its canonical required reading order",
    ),
    "PROJECT_OVERVIEW.ru.md": (
        "docs/A1...A10 first-draft provenance",
        "docs/INTEGRATED_A1_A10_REVIEW.ru.md",
        "docs/reviews/IAR-1_RECONCILIATION.ru.md",
        "следовать его canonical required reading order",
    ),
    "docs/README.md": (
        "A10-H11 SELECTED / EXECUTION ADMISSION BLOCKED",
        "current gate: A10_H11_EXECUTION_ADMISSION",
        "admission: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER",
        "H11 outcome: NOT_TESTED",
    ),
    "docs/README.ru.md": (
        "A10-H11 SELECTED / EXECUTION ADMISSION BLOCKED",
        "current gate: A10_H11_EXECUTION_ADMISSION",
        "admission: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER",
        "H11 outcome: NOT_TESTED",
    ),
    "docs/adr/README.md": (
        "A10_H11_EXECUTION_ADMISSION",
        "BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER",
        "H11: NOT_TESTED",
        "supporting operator decision package for ADR-0024, not a second ADR",
    ),
}

# These strings are valid chronology in designated history/research surfaces,
# but not when presented as current instructions. Historical documents may keep
# the underlying facts if the wording is explicitly scoped to the old checkpoint.
FORBIDDEN_CURRENT_MARKERS = {
    "docs/ai/CURRENT_STATE.md": (
        "next bounded gate: D6_A10_HYPOTHESIS_CLASSIFICATION",
        "D6: NOT_STARTED",
        "The current next gate is `D6_A10_HYPOTHESIS_CLASSIFICATION`",
        "Live Notion remains at the earlier D4.5 admission checkpoint",
        "next gate: RESIDUAL_A10_VALIDATION_PLAN",
    ),
    "docs/ai/README.md": (
        "next gate: D6_A10_HYPOTHESIS_CLASSIFICATION",
        "D6: NOT_STARTED",
        "The only current next gate is `RESIDUAL_A10_VALIDATION_PLAN`",
        "Notion is intentionally still at the earlier D4.5 checkpoint",
    ),
    "STATUS.md": (
        "document_role: CURRENT_STATE",
        "The current next gate is `D6_A10_HYPOTHESIS_CLASSIFICATION`",
        "Live Notion remains synchronized through the earlier D4.5 admission checkpoint",
    ),
    "ROADMAP.md": (
        "The only current next gate is `D6_A10_HYPOTHESIS_CLASSIFICATION`",
        "## Current architecture checkpoint",
    ),
    "docs/README.md": (
        "SUBJECT-IMPLEMENTATION-NEXT",
        "next gate: BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION",
    ),
    "docs/README.ru.md": (
        "SUBJECT-IMPLEMENTATION-NEXT",
        "next gate: BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION",
    ),
    "docs/adr/README.md": (
        "BPV1-PREREGISTERED / EXECUTION-ADMISSION-NEXT",
        "next: BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION",
    ),
}


@dataclass(frozen=True)
class Finding:
    path: str
    message: str

    def render(self) -> str:
        return f"{self.path}: {self.message}"


def _run_git(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=False,
        capture_output=True,
        text=True,
    )


def validate_required_paths(repo: Path) -> list[Finding]:
    return [
        Finding(rel, "required AI-context/authority file is missing")
        for rel in REQUIRED_PATHS
        if not (repo / rel).is_file()
    ]


def _normalize_link_target(source: Path, raw_target: str, repo: Path) -> Path | None:
    target = raw_target.strip()
    if not target or target.startswith("#"):
        return None
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
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
    return (
        repo / path_text.lstrip("/")
        if path_text.startswith("/")
        else source.parent / path_text
    ).resolve()


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


def validate_current_surfaces(repo: Path) -> list[Finding]:
    findings: list[Finding] = []
    for rel, markers in CURRENT_SURFACE_MARKERS.items():
        path = repo / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                findings.append(Finding(rel, f"required current/authority marker is missing: {marker}"))
        for stale in FORBIDDEN_CURRENT_MARKERS.get(rel, ()):
            if stale in text:
                findings.append(Finding(rel, f"stale current-looking marker is present: {stale}"))
    return findings


def read_current_checkpoint(repo: Path) -> tuple[str | None, list[Finding]]:
    rel = "docs/ai/CURRENT_STATE.md"
    path = repo / rel
    if not path.is_file():
        return None, [Finding(rel, "cannot read H11 state-binding checkpoint because file is missing")]
    text = path.read_text(encoding="utf-8")
    match = CURRENT_STATE_CHECKPOINT_RE.search(text)
    if not match:
        return None, [Finding(rel, "missing exact 40-character H11 state-binding checkpoint")]
    return match.group(1), []


def validate_checkpoint(repo: Path, checkpoint: str | None) -> list[Finding]:
    if checkpoint is None or not (repo / ".git").exists():
        return []
    if _run_git(repo, "cat-file", "-e", f"{checkpoint}^{{commit}}").returncode != 0:
        return [Finding("docs/ai/CURRENT_STATE.md", f"checkpoint commit does not exist: {checkpoint}")]
    return []


def validate(repo: Path) -> list[Finding]:
    findings = validate_required_paths(repo)
    findings.extend(validate_links(repo))
    findings.extend(validate_current_surfaces(repo))
    checkpoint, checkpoint_findings = read_current_checkpoint(repo)
    findings.extend(checkpoint_findings)
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
    print(
        "AI context validation passed; authority routing reaches IAR-1 reconciliation; "
        "current-only routing and labelled chronology surfaces are consistent; "
        "current gate=A10_H11_EXECUTION_ADMISSION; admission=BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER; "
        "H11=NOT_TESTED; runtime_expansion=FROZEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())