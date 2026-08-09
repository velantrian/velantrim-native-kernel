#!/usr/bin/env python3
"""Validate Native Kernel's AI context pack and checkpoint provenance."""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

REQUIRED_PATHS = (
    "AGENTS.md",
    "STATUS.md",
    "project-state.json",
    ".github/copilot-instructions.md",
    ".github/pull_request_template.md",
    "contracts/project-state-v1.schema.json",
    "contracts/project-state-v2.schema.json",
    "contracts/evidence-bundle-v1.schema.json",
    "evidence/c5/README.md",
    "evidence/c5/2026-08-07/manifest.json",
    "evidence/c5/2026-08-08-adr0023/manifest.json",
    "docs/ARCHITECTURE_REFOUNDATION.md",
    "docs/ARCHITECTURE_REFOUNDATION.ru.md",
    "docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.md",
    "docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md",
    "docs/A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md",
    "docs/A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md",
    "docs/adr/0025-blueprint-before-runtime-expansion.md",
    "docs/ai/README.md",
    "docs/ai/CURRENT_STATE.md",
    "docs/ai/COMPONENT_MAP.md",
    "docs/ai/KNOWN_RISKS.md",
    "docs/ai/WORK_LOG.md",
    "docs/ai/P4_IMPLEMENTATION_RECORD.md",
    "docs/ai/P5_IMPLEMENTATION_RECORD.md",
    "docs/ai/C4_IMPLEMENTATION_RECORD.md",
    "docs/ai/C5_IMPLEMENTATION_RECORD.md",
    "docs/ai/AUDIT_PLAYBOOK.md",
    "docs/ai/DOCUMENTATION_SYNC_PROTOCOL.md",
    "docs/ai/NOTION_HANDOFF.md",
    "docs/research/POST_C5_RESEARCH_BACKLOG.md",
)

LINK_SCAN_PATHS = (
    "README.md",
    "README.ru.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    ".github/copilot-instructions.md",
    ".github/pull_request_template.md",
    "docs/README.md",
    "docs/README.ru.md",
    "docs/ARCHITECTURE_REFOUNDATION.md",
    "docs/ARCHITECTURE_REFOUNDATION.ru.md",
    "docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.md",
    "docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md",
    "docs/A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md",
    "docs/A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md",
    "docs/adr/0025-blueprint-before-runtime-expansion.md",
    "docs/ai/README.md",
    "docs/ai/CURRENT_STATE.md",
    "docs/ai/COMPONENT_MAP.md",
    "docs/ai/KNOWN_RISKS.md",
    "docs/ai/WORK_LOG.md",
    "docs/ai/P4_IMPLEMENTATION_RECORD.md",
    "docs/ai/P5_IMPLEMENTATION_RECORD.md",
    "docs/ai/C4_IMPLEMENTATION_RECORD.md",
    "docs/ai/C5_IMPLEMENTATION_RECORD.md",
    "docs/ai/AUDIT_PLAYBOOK.md",
    "docs/ai/DOCUMENTATION_SYNC_PROTOCOL.md",
    "docs/ai/NOTION_HANDOFF.md",
    "docs/adr/README.md",
    "evidence/c5/README.md",
    "docs/research/POST_C5_RESEARCH_BACKLOG.md",
)

CHECKPOINT_RE = re.compile(
    r"^machine_truth_reconciliation_merge:\s*([0-9a-f]{40})\s*$",
    re.MULTILINE,
)
MARKDOWN_LINK_RE = re.compile(r"(?<!\!)\[[^\]]+\]\(([^)]+)\)")
IGNORED_SCHEMES = {"http", "https", "mailto", "tel", "data"}
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
    "Architecture Re-foundation: ACTIVE / BLUEPRINT-FIRST",
    "No new semantic/runtime expansion before blueprint gate completion.",
    "BOUNDED REFERENCE LABORATORY",
    "blueprint content A1–A2 is `DRAFTED / PROVISIONAL`",
    "next bounded content slice is `A3 — Abstract Native Kernel Machine`",
)
FORBIDDEN_STATUS_MARKERS = (
    "Notion remains synchronized only through the recorded publication checkpoint",
    "Next work is limited to explicit operator decisions",
    "next bounded content slice is `A2 — Knowledge and Memory Ontology`",
)


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
    return [Finding(rel, "required AI-context file is missing") for rel in REQUIRED_PATHS if not (repo / rel).is_file()]


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
    return (repo / path_text.lstrip("/") if path_text.startswith("/") else source.parent / path_text).resolve()


def validate_links(repo: Path) -> list[Finding]:
    findings: list[Finding] = []
    repo_resolved = repo.resolve()
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
                candidate.relative_to(repo_resolved)
            except ValueError:
                findings.append(Finding(rel, f"relative link escapes repository: {raw}"))
                continue
            if not candidate.exists():
                findings.append(Finding(rel, f"broken relative link: {raw}"))
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
    head = _run_git(repo, "rev-parse", "HEAD")
    if head.returncode != 0:
        return [Finding(".git", "cannot resolve HEAD")]
    if _run_git(repo, "merge-base", "--is-ancestor", checkpoint, "HEAD").returncode != 0:
        return [
            Finding(
                "docs/ai/CURRENT_STATE.md",
                f"checkpoint {checkpoint} is not an ancestor of HEAD {head.stdout.strip()}",
            )
        ]
    return []


def validate(repo: Path) -> list[Finding]:
    findings = validate_required_paths(repo)
    findings.extend(validate_links(repo))
    checkpoint, more = read_checkpoint(repo)
    findings.extend(more)
    findings.extend(validate_checkpoint(repo, checkpoint))
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    repo = args.repo.resolve()
    if not (repo / ".git").exists():
        print(f"ERROR: not a git repository: {repo}", file=sys.stderr)
        return 2
    findings = validate(repo)
    if findings:
        print("AI context validation failed:", file=sys.stderr)
        for finding in findings:
            print(f"- {finding.render()}", file=sys.stderr)
        return 1
    checkpoint, _ = read_checkpoint(repo)
    head = _run_git(repo, "rev-parse", "HEAD").stdout.strip()
    print(
        "AI context validation passed; "
        f"machine_truth_reconciliation_merge={checkpoint}; head={head}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
