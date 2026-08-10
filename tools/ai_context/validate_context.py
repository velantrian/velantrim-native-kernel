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

CURRENT_MARKERS = (
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
    "Architecture Re-foundation: ACTIVE / BLUEPRINT-FIRST",
    "blueprint content A1–A10 is `DRAFTED / PROVISIONAL`",
    "integrated review: COMPLETED / PROVISIONAL / OPERATOR_DECISION_PENDING",
    "next bounded gate is `OPERATOR_POST_BLUEPRINT_DECISION`",
)

SURFACE_MARKERS = {
    "STATUS.md": (
        "blueprint content: A1-A10 DRAFTED / PROVISIONAL",
        "integrated review: COMPLETED / PROVISIONAL / OPERATOR_DECISION_PENDING",
        "next content slice: OPERATOR_POST_BLUEPRINT_DECISION",
    ),
    "ROADMAP.md": (
        "integrated A1-A10 review                 COMPLETE / PROVISIONAL",
        "OPERATOR_POST_BLUEPRINT_DECISION          NEXT GATE",
        "Integrated review complete ≠ runtime thaw",
    ),
    "docs/ARCHITECTURE_REFOUNDATION.md": (
        "Integrated review: COMPLETED / PROVISIONAL / OPERATOR_DECISION_PENDING",
        "Next bounded gate: OPERATOR_POST_BLUEPRINT_DECISION",
    ),
    "docs/ARCHITECTURE_REFOUNDATION.ru.md": (
        "Integrated review: COMPLETED / PROVISIONAL / OPERATOR_DECISION_PENDING",
        "Next bounded gate: OPERATOR_POST_BLUEPRINT_DECISION",
    ),
    "docs/ai/README.md": (
        "blueprint content: A1-A10 DRAFTED / PROVISIONAL",
        "next content slice: OPERATOR_POST_BLUEPRINT_DECISION",
        "OPERATOR_POST_BLUEPRINT_DECISION ≠ A11",
    ),
    "docs/INTEGRATED_A1_A10_REVIEW.md": (
        "nk-integrated-blueprint-review/A1-A10-review-1",
        "no known blocking internal semantic contradiction remains",
        "OPERATOR_POST_BLUEPRINT_DECISION",
    ),
}

FORBIDDEN_PROGRESS = (
    "next content slice: INTEGRATED_A1_A10_REVIEW",
    "Next bounded gate: INTEGRATED_A1_A10_REVIEW",
    "→ integrated A1-A10 review                     NEXT GATE",
)


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


def validate_surfaces(repo: Path) -> list[Finding]:
    findings: list[Finding] = []
    for rel, markers in SURFACE_MARKERS.items():
        path = repo / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                findings.append(Finding(rel, f"required blueprint-progress marker is missing: {marker}"))
        for stale in FORBIDDEN_PROGRESS:
            if stale in text:
                findings.append(Finding(rel, f"forbidden stale blueprint-progress marker is present: {stale}"))
    return findings


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
    for marker in CURRENT_MARKERS:
        if marker not in text:
            findings.append(Finding(rel, f"required current-state marker is missing: {marker}"))
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
    findings.extend(validate_surfaces(repo))
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
    print("AI context validation passed; A1-A10 drafted/provisional; integrated_review=complete/provisional; next=OPERATOR_POST_BLUEPRINT_DECISION; runtime_expansion_frozen=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
