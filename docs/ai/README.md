# 🤖 Native Kernel AI Context Pack

This directory is the first orientation layer for AI agents, auditors, reviewers and future maintainers.

It preserves continuity without requiring full-repository scanning or private chat history. It is a map, not proof.

> **Verify material claims against the exact SHA, tests, workflow jobs, artifacts, dataset digest and declared evidence level.**

## Required reading order

1. [`../../README.md`](../../README.md) — purpose and maturity.
2. [`../../STATUS.md`](../../STATUS.md) — authoritative current boundary.
3. [`../../AGENTS.md`](../../AGENTS.md) — mandatory repository rules.
4. [`DOCUMENTATION_SYNC_PROTOCOL.md`](DOCUMENTATION_SYNC_PROTOCOL.md) — GitHub ↔ Notion definition of done.
5. [`CURRENT_STATE.md`](CURRENT_STATE.md) — last verified checkpoint and active gates.
6. [`C4_IMPLEMENTATION_RECORD.md`](C4_IMPLEMENTATION_RECORD.md) — offline dataset, evaluator, Shadow Receipts, runs, artifacts and non-claims.
7. [`P5_IMPLEMENTATION_RECORD.md`](P5_IMPLEMENTATION_RECORD.md) — SQLite profile and C3 prerequisite evidence.
8. [`P4_IMPLEMENTATION_RECORD.md`](P4_IMPLEMENTATION_RECORD.md) — PostgreSQL assertion-scoped C2 foundation.
9. [`P3_IMPLEMENTATION_RECORD.md`](P3_IMPLEMENTATION_RECORD.md) — replay/projection/Receipt foundation.
10. [`COMPONENT_MAP.md`](COMPONENT_MAP.md) — contract, ownership and evidence routes.
11. [`KNOWN_RISKS.md`](KNOWN_RISKS.md) — unresolved risks and required proof.
12. [`AUDIT_PLAYBOOK.md`](AUDIT_PLAYBOOK.md) — context-efficient audit method.
13. [`WORK_LOG.md`](WORK_LOG.md) — engineering chronology and hand-off.
14. [`NOTION_HANDOFF.md`](NOTION_HANDOFF.md) — queue when Notion is unavailable.

Then inspect only the source, tests, contracts, manifests, ADRs, workflows, PRs and issues relevant to the task.

## Current evidence boundary

```text
Repository status: RESEARCH / C4 PARTIAL OFFLINE SHADOW EVALUATION / NOT PRODUCTION-READY
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
Offline C4 scope:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
support_state:     PARTIAL
C5:                NOT_ESTABLISHED / NOT_AUTHORIZED
```

```text
C2 ≠ C3 ≠ C4
C4 OFFLINE SHADOW ≠ LIVE SHADOWING
C4 SHADOW OBSERVATION ≠ AUTHORITY PROMOTION
C4 SUPPORTED ASSERTIONS ≠ SUPPORT FOR ALL 72
C4 ≠ truth/authenticity
C4 ≠ physical deletion
C4 ≠ C5 / production readiness
```

## C4 source-of-evidence chain

```text
ADR-0020 + Issue #61
→ approved contracts/shadow-workload-v1.json bytes
→ exact dataset SHA-256
→ exact C3 prerequisite report
→ offline evaluator
→ nk-shadow-report/1
→ 15 nk-shadow-receipt/1 records
→ exact-SHA CI artifact
```

A C4 claim is invalid without the approved dataset digest, the exact C3 prerequisite, repository metadata and retained artifact bytes.

## Source-of-truth order

1. code/tests and dataset bytes at the exact commit;
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
- trace a C2/C3/C4 assertion result to checks and artifacts;
- trace C4 to an approved dataset ID/digest and Shadow Receipts;
- identify allowed/forbidden differences and authority boundaries;
- identify open risks and next gates;
- continue work safely.

No material decision, finding, blocker, evidence or next action may exist only in Notion or chat.

## Task routes

| Task | Read next |
|---|---|
| Repository maturity | `STATUS.md` + `CURRENT_STATE.md` |
| C4 claim | `C4_IMPLEMENTATION_RECORD.md` → Issue #61 → ADR-0020 → dataset → evaluator → exact artifact |
| C4 dataset change | ADR-0020 + manifest + dataset digest + validator + new evidence cycle |
| P5/C3 claim | `P5_IMPLEMENTATION_RECORD.md` → Issue #58 → ADR-0019 → comparator → exact artifacts |
| SQLite profile | `native_kernel/sqlite_profile/README.md` → adapter/replay/conformance/tests |
| P4 C2 claim | `P4_IMPLEMENTATION_RECORD.md` → Issue #55 → ADR-0018 → PostgreSQL report |
| Assertion support | assertion ID → report result → check/case IDs → exact artifact |
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

- required context files, including P4, P5 and C4 records;
- selected relative links;
- exact checkpoint syntax/existence/ancestry;
- C4 maturity marker;
- C2/C3/C4 boundaries;
- offline/live and observation/authority boundaries;
- partial 45-of-72 assertion scope.

```text
AI-context PASS
≠ semantic freshness of every statement
≠ Notion synchronization proof
≠ runtime/conformance/shadow proof
```

## Update obligation

A material PR must update relevant files in the same branch:

- `CURRENT_STATE.md`;
- `C4_IMPLEMENTATION_RECORD.md` for C4 dataset, scope or evidence changes;
- `P5_IMPLEMENTATION_RECORD.md` for P5/C3 changes;
- `P4_IMPLEMENTATION_RECORD.md` for PostgreSQL P4 changes;
- `KNOWN_RISKS.md`;
- `COMPONENT_MAP.md`;
- `WORK_LOG.md`;
- relevant ADR/status/profile/package documents;
- direct Notion record or structured hand-off.

Do not copy stale SHAs, run IDs, dataset digests, support counts or artifact claims without verification.
