# 🤖 Velantrim Native Kernel repository guidance

This file is the mandatory entry point for AI coding agents, auditors, reviewers, and automated contributors.
It applies to the whole repository unless a more local `AGENTS.md` explicitly narrows the rules.

## 1. Read before auditing or changing anything

Read in this order:

1. [`README.md`](README.md) — public purpose, maturity and ecosystem role.
2. [`STATUS.md`](STATUS.md) — authoritative implementation and evidence boundary.
3. [`docs/ai/README.md`](docs/ai/README.md) — AI context-pack manifest.
4. [`docs/ai/DOCUMENTATION_SYNC_PROTOCOL.md`](docs/ai/DOCUMENTATION_SYNC_PROTOCOL.md) — GitHub and Notion definition of done.
5. [`docs/ai/CURRENT_STATE.md`](docs/ai/CURRENT_STATE.md) — last verified repository checkpoint and current gates.
6. Relevant section of [`docs/ai/COMPONENT_MAP.md`](docs/ai/COMPONENT_MAP.md).
7. Relevant entries in [`docs/ai/KNOWN_RISKS.md`](docs/ai/KNOWN_RISKS.md).
8. Recent relevant entries in [`docs/ai/WORK_LOG.md`](docs/ai/WORK_LOG.md).
9. [`docs/ai/AUDIT_PLAYBOOK.md`](docs/ai/AUDIT_PLAYBOOK.md) for audit work.
10. [`docs/ai/NOTION_HANDOFF.md`](docs/ai/NOTION_HANDOFF.md) when required Notion synchronization cannot be completed directly.

Then inspect only the affected source-recovery tools, tests, contracts, ADRs, RFCs, PRs, issues and workflows.
Do not load every historical document by default.

> Documentation is an orientation map, not self-proving evidence. Verify material claims at the exact commit or PR head under review.

## 2. Source-of-truth order

When sources disagree, use this order:

1. executable repository code and committed tests at the exact SHA;
2. current CI results and workflow definitions for that exact SHA;
3. [`STATUS.md`](STATUS.md) and accepted current-state records;
4. accepted ADRs and normative contracts;
5. current roadmap, RFCs and research documents with their explicit status labels;
6. PR descriptions, work-log entries and issues;
7. historical audits, chats, journals and external reports.

Never treat an open PR, a detailed research note, an AI consensus, or a Notion plan as behavior already present in `main`.

## 3. Required status language

Distinguish these claims:

- **documented** — a specification or explanation exists;
- **proposed** — a design exists but is not accepted;
- **accepted** — the operator approved a decision; implementation may still be absent;
- **implemented** — code exists in the declared scope;
- **tested** — committed tests exist and their result is known;
- **wired** — a real runtime caller exists;
- **enabled** — configuration activates it;
- **observed** — a running system produced operational evidence.

Do not replace these with an unqualified statement that a feature “works”.

Preserve the independent governance dimensions:

```text
Decision status
≠ Evidence level
≠ Implementation status
≠ Operator approval
```

## 4. Native Kernel architecture discipline

- Preserve `Architecture Canon → Abstract Contracts → Replaceable Implementation Profiles`.
- Treat event history as authoritative about recorded history, not automatically as truth.
- Keep Claim identity, provenance, temporal meaning, conflict visibility, reduction and Receipt semantics independent from one database, model, runtime or processor.
- PostgreSQL and SQLite are implementation profiles, not Canon.
- LLMs, embeddings, graph databases, FTS, CPUs, GPUs and future substrates are replaceable instruments.
- Relevance, recency, utility, repetition, write order and model confidence do not independently establish truth.
- A Receipt proves only what its declared contract and evidence support.
- Operator approval is authority, not empirical evidence.

## 5. Issue #1 and source-recovery boundary

The repository is currently `RESEARCH / P2 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`.
A clean P1 semantic core and bounded P2 PostgreSQL append/idempotency profile exist. This is not the recovered historical `v0.1.2.1`, not the original 44-test suite, not a complete Kernel, and not C1/C2/C3 evidence.

- Do not reconstruct an approximation and label it `v0.1.2.1`.
- Do not replace the original suite with newly written tests and call it recovered evidence.
- Do not treat source-recovery tooling as Kernel runtime.
- `NOT_FOUND_IN_ACCESSIBLE_SOURCES` is not `GLOBALLY_LOST`.
- Controlled import must remain separate from architecture redesign.
- Clean implementation lineage is `clean/postgresql-reference/0.1`.
- P2 code or unit tests do not prove PostgreSQL integration, replay, conformance or production readiness.

## 6. Cross-project boundaries

- Native Kernel is not the universal truth authority of Velantrim.
- Mentaury Soul owns digital-individuality, identity-continuity, relationship and commitment semantics in its own project.
- Titan owns its cognition, retrieval, tool and orchestration architecture in its own project.
- Crystal owns its verifiable-memory, evidence, trust and grant-facing product boundaries in its own project.
- Cross-links explain roles; they do not imply one runtime, one database or one Canon.
- No cross-project capability, consent, identity, credential, event authority or implementation status is inherited implicitly.

## 7. Verification

Run the narrowest relevant checks first.

For source-recovery tooling, use the commands declared in `docs/source-recovery/README.md` and the retained source-recovery workflow.
For P1 use the semantic-core tests and P1 manifest guard.
For P2 run unit/manifest checks first, then the PostgreSQL integration suite with an explicit DSN and inspect exact PostgreSQL/Python matrix evidence.
For documentation changes, verify links, status labels, bilingual parity, ADR references and exact SHAs.

Do not claim:

- Kernel CI when only utility CI ran;
- PostgreSQL integration when integration tests were skipped or no run exists;
- public reproduction of the 44-test checkpoint;
- portability without cross-profile conformance evidence;
- production safety, privacy, security, replay or migration guarantees without committed proof.

## 8. Documentation and Notion synchronization obligation

Any PR that materially changes architecture, contracts, implementation status, evidence, project direction, cross-project boundaries, a known risk, source-recovery status or an accepted decision must update the relevant public GitHub documentation:

- `docs/ai/CURRENT_STATE.md` for verified status changes;
- `docs/ai/KNOWN_RISKS.md` for opened, narrowed or closed risks;
- `docs/ai/COMPONENT_MAP.md` for ownership or first-read path changes;
- `docs/ai/WORK_LOG.md` for significant work and hand-off;
- an ADR/RFC for durable architectural decisions;
- affected `STATUS.md`, `ROADMAP.md`, security, conformance, profile, integration or user-facing documents.

Every PR must follow [`docs/ai/DOCUMENTATION_SYNC_PROTOCOL.md`](docs/ai/DOCUMENTATION_SYNC_PROTOCOL.md) and classify its impact as `NONE`, `GITHUB_ONLY`, or `GITHUB_AND_NOTION`.

### GitHub completeness invariant

GitHub must contain enough public technical, evidence and audit context for an AI or human reviewer to understand, verify and continue the work without Notion access.
Implemented behavior, material findings, known risks, exact evidence, architectural decisions, blockers and next actions must never exist only in Notion or only in a chat.

### When Notion is available

For `GITHUB_AND_NOTION`, update the corresponding Notion record in the same work cycle.
Record motivation, intended function, decision, alternatives, exact reality status, evidence, limitations, PR and final merge SHA.

### When Notion is unavailable

Complete the GitHub record and add a structured item to [`docs/ai/NOTION_HANDOFF.md`](docs/ai/NOTION_HANDOFF.md).
Never claim that Notion was updated when it was not.

## 9. Change discipline

Before writing:

1. establish exact base/head SHA and task scope;
2. identify whether the claim concerns `main`, an open PR, an external checkpoint, a proposed document or a future runtime;
3. inspect affected contracts, ADRs, tests and downstream documentation;
4. choose the lowest-risk owning document or component;
5. preserve Issue #1 and cross-project boundaries;
6. make the smallest coherent change;
7. validate it;
8. update GitHub documentation and Notion, or create a structured hand-off;
9. open a PR with exact evidence and remaining limitations.

Do not silently combine unrelated cleanup, source recovery, architecture redesign, runtime implementation, profile activation or cross-project integration.
