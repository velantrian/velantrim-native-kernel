# 🤖 Native Kernel AI Context Pack

This directory is the first orientation layer for AI agents, auditors, reviewers and future maintainers working on Velantrim Native Kernel.

It exists to preserve project continuity without forcing every actor to scan the full repository or rely on private chat history.
It is a map, not a substitute for checking the exact repository state.

> **Documentation is orientation, not proof.** Verify every material claim against the exact SHA, committed artifacts, tests, workflow results and declared evidence level.

## Required reading order

1. [`../../README.md`](../../README.md) — purpose, maturity and ecosystem role.
2. [`../../STATUS.md`](../../STATUS.md) — authoritative implementation boundary.
3. [`../../AGENTS.md`](../../AGENTS.md) — mandatory repository rules.
4. [`DOCUMENTATION_SYNC_PROTOCOL.md`](DOCUMENTATION_SYNC_PROTOCOL.md) — GitHub ↔ Notion synchronization contract.
5. [`CURRENT_STATE.md`](CURRENT_STATE.md) — last verified checkpoint and active gates.
6. [`COMPONENT_MAP.md`](COMPONENT_MAP.md) — document, contract, authority and evidence map.
7. [`KNOWN_RISKS.md`](KNOWN_RISKS.md) — unresolved engineering, epistemic and governance risks.
8. [`AUDIT_PLAYBOOK.md`](AUDIT_PLAYBOOK.md) — context-efficient audit method.
9. [`WORK_LOG.md`](WORK_LOG.md) — significant work, decisions and hand-offs.
10. [`NOTION_HANDOFF.md`](NOTION_HANDOFF.md) — synchronization queue when Notion is unavailable.

Then open only the source-recovery tooling, ADRs, RFCs, contracts, issues, PRs and workflows relevant to the task.

## Source-of-truth order

1. code and tests at the exact commit;
2. CI and workflow evidence for that exact commit;
3. `STATUS.md` and this pack's last verified checkpoint;
4. accepted ADRs and normative contracts;
5. roadmap and explicitly labelled research proposals;
6. PR descriptions, work log and issues;
7. historical audits, chats and external reports.

`CURRENT_STATE.md` is a checkpoint, not a magical live database. Always compare its recorded SHA with the actual branch under review.

## GitHub must remain sufficient without Notion

GitHub must preserve enough public context to:

- establish current reality at an exact SHA;
- distinguish documentation, proposal, acceptance, implementation and evidence;
- locate Architecture Canon, contracts, profiles and Anti-Canon boundaries;
- reproduce source-recovery tooling evidence;
- identify open risks and next gates;
- continue implementation or review safely.

No material finding, accepted decision, blocker, exact evidence or required next action may exist only in Notion or only in a chat.

## Task-specific routes

| Task | Read next |
|---|---|
| Repository maturity or implementation claim | `STATUS.md` + `CURRENT_STATE.md` |
| Architecture or invariant | `ARCHITECTURE.md`, `FOUNDATIONAL_INTENT`, relevant ADR |
| Source recovery / Issue #1 | `ISSUE_1_IMPORT_SPEC`, `docs/source-recovery/`, `prototype/README.md` |
| Storage or compute profile | `STORAGE_AND_EXECUTION_PROFILES*`, ADR-0009 |
| Conformance or portability | `CONFORMANCE_MODEL.md`, ADR-0004 |
| Curiosity or causality | relevant RFC/research note + ADR-0005/0006 |
| Titan, Mentaury or Crystal boundary | `VELANTRIM_ECOSYSTEM.md`, `INTEGRATION_BOUNDARIES.md` |
| General audit | `AUDIT_PLAYBOOK.md` + affected component route |
| Durable decision | `DECISION_PROCESS.md`, ADR template, sync protocol |
| No Notion access | `NOTION_HANDOFF.md` |

## Automated integrity check

The standard-library validator is documented in [`../../tools/ai_context/README.md`](../../tools/ai_context/README.md).

Run it from the repository root:

```bash
python tools/ai_context/validate_context.py --repo .
```

The guard checks the mandatory context surface, selected repository-relative links, exact checkpoint syntax, commit existence, ancestry and required status-boundary markers. CI runs it with full Git history on Python 3.11 and 3.12.

The guard is intentionally limited:

```text
AI-context guard PASS
≠ semantic freshness of every statement
≠ Notion synchronization proof
≠ Architecture Canon validation
≠ Native Kernel runtime evidence
```

An ancestor checkpoint is permitted because `CURRENT_STATE.md` is a last-verified checkpoint. Reviewers must still decide whether a later material change required a semantic status update.

## Update obligation

A material PR must update the affected context files in the same branch:

- `CURRENT_STATE.md` for verified state changes;
- `KNOWN_RISKS.md` for changed risk;
- `COMPONENT_MAP.md` for new ownership or first-read paths;
- `WORK_LOG.md` for significant work;
- an ADR/RFC for durable decisions;
- direct Notion record or a structured hand-off when required.

Do not copy stale SHAs, test counts or implementation claims forward without verification.
