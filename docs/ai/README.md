# 🤖 Native Kernel AI Context Pack

This directory is the first orientation layer for AI agents, auditors, reviewers and future maintainers.

It preserves continuity without requiring full-repository scanning or private chat history. It is a map, not proof.

> **Verify material claims against the exact SHA, tests, workflow jobs, artifacts and declared evidence level.**

## Required reading order

1. [`../../README.md`](../../README.md) — purpose and maturity.
2. [`../../STATUS.md`](../../STATUS.md) — authoritative current boundary.
3. [`../../AGENTS.md`](../../AGENTS.md) — mandatory repository rules.
4. [`DOCUMENTATION_SYNC_PROTOCOL.md`](DOCUMENTATION_SYNC_PROTOCOL.md) — GitHub ↔ Notion definition of done.
5. [`CURRENT_STATE.md`](CURRENT_STATE.md) — last verified checkpoint and active gates.
6. [`P4_IMPLEMENTATION_RECORD.md`](P4_IMPLEMENTATION_RECORD.md) — assertion map, checks, C2 evidence, artifacts and limitations.
7. [`P3_IMPLEMENTATION_RECORD.md`](P3_IMPLEMENTATION_RECORD.md) — replay/projection/Receipt foundation.
8. [`COMPONENT_MAP.md`](COMPONENT_MAP.md) — contract, ownership and evidence routes.
9. [`KNOWN_RISKS.md`](KNOWN_RISKS.md) — unresolved risks and required proof.
10. [`AUDIT_PLAYBOOK.md`](AUDIT_PLAYBOOK.md) — context-efficient audit method.
11. [`WORK_LOG.md`](WORK_LOG.md) — engineering chronology and hand-off.
12. [`NOTION_HANDOFF.md`](NOTION_HANDOFF.md) — queue when Notion is unavailable.

Then inspect only the source, tests, contracts, manifests, ADRs, RFCs, workflows, PRs and issues relevant to the task.

## Current evidence boundary

```text
Repository status: RESEARCH / P4 PARTIAL ASSERTION CONFORMANCE / NOT PRODUCTION-READY
P4 map:           41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
support_state:    PARTIAL
C2:               assertion-scoped for SUPPORTED results
C3:               NOT_ESTABLISHED
P5:               NOT_AUTHORIZED
```

```text
P4 C2 ≠ all 72 supported
P4 C2 ≠ C3
P4 C2 ≠ truth/authenticity
P4 C2 ≠ physical deletion
```

## Source-of-truth order

1. code/tests at the exact commit;
2. exact-SHA CI jobs, logs and artifacts;
3. `STATUS.md` and current-state checkpoint;
4. accepted ADRs and normative contracts;
5. explicitly labelled RFCs/research;
6. PR descriptions, issues and work log;
7. historical chats, audits and external reports.

`CURRENT_STATE.md` is a checkpoint, not a live database. Compare its recorded SHA with the actual branch under review.

## GitHub completeness invariant

GitHub must remain sufficient without Notion to:

- establish current reality at an exact SHA;
- distinguish proposed, accepted, implemented and evidenced behavior;
- locate Canon, contracts, profiles and Anti-Canon boundaries;
- trace an assertion result to checks and artifacts;
- identify open risks and next gates;
- continue work safely.

No material decision, finding, blocker, evidence or next action may exist only in Notion or chat.

## Task routes

| Task | Read next |
|---|---|
| Repository maturity | `STATUS.md` + `CURRENT_STATE.md` |
| P4 conformance claim | `P4_IMPLEMENTATION_RECORD.md` → Issue #55 → ADR-0018 → adapter/map → exact artifact |
| P3 replay/projection | `P3_IMPLEMENTATION_RECORD.md` → Issue #49 → ADR-0017 → source/tests |
| Assertion support | assertion ID → P4 report result → check IDs → exact run/artifact |
| Architecture/invariant | `ARCHITECTURE.md`, foundational intent, relevant ADR |
| Source recovery | Issue #1 import spec + `docs/source-recovery/` |
| Storage profile | storage/execution profiles + ADR-0009 |
| P5/C3 | conformance model + separate operator GO + independent profile evidence |
| Ecosystem boundary | ecosystem and integration-boundary documents |
| General audit | `AUDIT_PLAYBOOK.md` + affected route |
| Durable decision | decision process + ADR template + sync protocol |

## Automated integrity guard

Run:

```bash
python tools/ai_context/validate_context.py --repo .
```

The guard checks:

- required context files, including the P4 record;
- selected relative links;
- exact checkpoint syntax/existence/ancestry;
- P4 maturity marker;
- `P4 C2 ≠ C3` boundary.

```text
AI-context PASS
≠ semantic freshness of every statement
≠ Notion synchronization proof
≠ runtime/conformance proof
```

## Update obligation

A material PR must update relevant files in the same branch:

- `CURRENT_STATE.md`;
- `P4_IMPLEMENTATION_RECORD.md` for P4 scope/evidence changes;
- `KNOWN_RISKS.md`;
- `COMPONENT_MAP.md`;
- `WORK_LOG.md`;
- relevant ADR/RFC/status/profile/package documents;
- direct Notion record or structured hand-off.

Do not copy stale SHAs, run IDs, support counts or artifact claims without verification.
