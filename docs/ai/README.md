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
6. [`P5_IMPLEMENTATION_RECORD.md`](P5_IMPLEMENTATION_RECORD.md) — SQLite profile, C3 checks, reports, runs, artifacts and limitations.
7. [`P4_IMPLEMENTATION_RECORD.md`](P4_IMPLEMENTATION_RECORD.md) — PostgreSQL assertion-scoped C2 foundation.
8. [`P3_IMPLEMENTATION_RECORD.md`](P3_IMPLEMENTATION_RECORD.md) — replay/projection/Receipt foundation.
9. [`COMPONENT_MAP.md`](COMPONENT_MAP.md) — contract, ownership and evidence routes.
10. [`KNOWN_RISKS.md`](KNOWN_RISKS.md) — unresolved risks and required proof.
11. [`AUDIT_PLAYBOOK.md`](AUDIT_PLAYBOOK.md) — context-efficient audit method.
12. [`WORK_LOG.md`](WORK_LOG.md) — engineering chronology and hand-off.
13. [`NOTION_HANDOFF.md`](NOTION_HANDOFF.md) — queue when Notion is unavailable.

Then inspect only the source, tests, contracts, manifests, ADRs, RFCs, workflows, PRs and issues relevant to the task.

## Current evidence boundary

```text
Repository status: RESEARCH / P5 PARTIAL CROSS-PROFILE CONFORMANCE / NOT PRODUCTION-READY
SQLite C2 map:     41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
C3 map:            45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
support_state:     PARTIAL
C4/C5:             NOT_ESTABLISHED / NOT_AUTHORIZED
```

```text
C2 ≠ C3
C3 SUPPORTED ASSERTIONS ≠ SUPPORT FOR ALL 72
C3 SEMANTIC EQUIVALENCE ≠ OPERATIONAL EQUIVALENCE
C3 ≠ truth/authenticity
C3 ≠ physical deletion
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
- trace a C2/C3 assertion result to checks and artifacts;
- identify allowed/forbidden cross-profile differences;
- identify open risks and next gates;
- continue work safely.

No material decision, finding, blocker, evidence or next action may exist only in Notion or chat.

## Task routes

| Task | Read next |
|---|---|
| Repository maturity | `STATUS.md` + `CURRENT_STATE.md` |
| P5/C3 claim | `P5_IMPLEMENTATION_RECORD.md` → Issue #58 → ADR-0019 → comparator → exact artifacts |
| SQLite profile | `native_kernel/sqlite_profile/README.md` → adapter/replay/conformance/tests |
| P4 C2 claim | `P4_IMPLEMENTATION_RECORD.md` → Issue #55 → ADR-0018 → PostgreSQL report |
| Assertion support | assertion ID → SQLite/C3 report result → check IDs → exact artifact |
| Architecture/invariant | `ARCHITECTURE.md`, foundational intent, relevant ADR |
| Source recovery | Issue #1 import spec + `docs/source-recovery/` |
| Storage profile | storage/execution profiles + ADR-0009/0019 |
| Ecosystem boundary | ecosystem and integration-boundary documents |
| General audit | `AUDIT_PLAYBOOK.md` + affected route |
| Durable decision | decision process + ADR template + sync protocol |

## Automated integrity guard

Run:

```bash
python tools/ai_context/validate_context.py --repo .
```

The guard checks:

- required context files, including P4 and P5 records;
- selected relative links;
- exact checkpoint syntax/existence/ancestry;
- P5 maturity marker;
- C2/C3 and semantic/operational-equivalence boundaries.

```text
AI-context PASS
≠ semantic freshness of every statement
≠ Notion synchronization proof
≠ runtime/conformance proof
```

## Update obligation

A material PR must update relevant files in the same branch:

- `CURRENT_STATE.md`;
- `P5_IMPLEMENTATION_RECORD.md` for P5/C3 scope or evidence changes;
- `P4_IMPLEMENTATION_RECORD.md` when PostgreSQL P4 evidence changes;
- `KNOWN_RISKS.md`;
- `COMPONENT_MAP.md`;
- `WORK_LOG.md`;
- relevant ADR/RFC/status/profile/package documents;
- direct Notion record or structured hand-off.

Do not copy stale SHAs, run IDs, support counts or artifact claims without verification.
