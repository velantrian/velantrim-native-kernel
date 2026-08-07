# 🧩 P5 SQLite & Cross-Profile C3 Implementation Record

**Recorded:** 2026-08-07  
**Base public `main`:** `1dc493e9d23b99ee4bbf6015348599cd56f6cb56`  
**Canonical issue:** #58  
**Pull request:** #59  
**Decision:** ADR-0019 `ACCEPTED / APPROVED`

## Profiles and lineages

```text
PostgreSQL: native-kernel/postgresql-reference@0.4-p4
Lineage:    clean/postgresql-reference/0.1

SQLite:     native-kernel/sqlite-embedded@0.5-p5
Lineage:    clean/sqlite-embedded/0.1
```

SQLite is a materially different embedded profile implemented with Python standard-library `sqlite3`. It does not call PostgreSQL append, replay, projection or Receipt adapters.

## Maturity

```text
P1–P4:                 MERGED / REPOSITORY-REPRODUCED
P5 SQLite profile:     PARTIAL / C2 REPOSITORY-REPRODUCED ON PREVIOUS HEAD
Cross-profile C3:      PARTIAL / REPOSITORY-REPRODUCED ON PREVIOUS HEAD
support_state:         PARTIAL
C4/C5:                 NOT ESTABLISHED / NOT AUTHORIZED
Production readiness: NOT CLAIMED
```

## Result maps

SQLite profile report:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
TOTAL:       72
```

PostgreSQL↔SQLite comparison:

```text
SUPPORTED:   45
PARTIAL:     10
UNSUPPORTED: 17
FAILED:       0
TOTAL:       72
```

Cross-profile evidence promotes exactly four assertion results relative to the single-profile C2 map:

- `NK-SEM-008`;
- `NK-ID-008`;
- `NK-EQV-002`;
- `NK-EQV-003`.

All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

## Independent SQLite route

```text
stdlib sqlite3
→ numbered migration ledger + digest drift guard
→ Kernel-instance registration
→ BEGIN IMMEDIATE single-writer transaction
→ owner / epoch / expiry fence
→ scoped durable idempotency
→ rollback-safe sequence allocation
→ canonical Event commitments and hash chain
→ persisted replay
→ disposable projection rebuild
→ bounded operational Receipts
```

Implemented checks cover:

- migration idempotency;
- stale writer and lease expiry rejection;
- append/retry/idempotency conflict;
- rollback without sequence gaps;
- global and per-stream ordering;
- replay and projection equivalence;
- stale-head rejection;
- stored canonical corruption detection;
- exact authoritative-history import.

## Equivalence route

```text
same registry + fixture pack
→ independent PostgreSQL workload
→ independent SQLite workload
→ normalized append/Event outcomes
→ replay and projection comparison
→ Receipt proof-boundary comparison
→ exact PostgreSQL Event import into SQLite
→ assertion-to-cross-profile-check mapping
→ nk-equivalence-report/1
```

### Equivalence classes

| Class | Evidence |
|---|---|
| `BYTE` | identity golden vectors and exact imported Event bytes/hash chain |
| `STRUCTURAL` | complete 72-ID report shape and declared fields |
| `SEMANTIC` | reducer/projection canonical state and Receipt proof fields |
| `BEHAVIOURAL` | accepted/rejected commands, idempotency, fencing and ordering |

## Allowed differences

- PostgreSQL SQL versus SQLite SQL;
- server/database topology versus a local file;
- row locks versus `BEGIN IMMEDIATE`;
- independently generated Event IDs and timestamps;
- IAM, networking, replication, failover, concurrency and administration;
- non-semantic storage metadata and query plans.

## Forbidden differences

- canonical identity vectors;
- Command digest and payload meaning;
- declared sequence/order semantics;
- hash-chain validity;
- reducer/projection state digest and canonical bytes;
- idempotency, stale-writer and corruption rejection results;
- Receipt proof-boundary booleans;
- bytes/hash commitments during exact authoritative-history import.

## Initial repository evidence

```text
Evidence head: d43a6ed28232e9fc8b62f84d9025386fb8bce6f7
P5/C3 run:    31181341275 — PASS
P4 run:       31181341370 — PASS
P1 run:       31181341405 — PASS
Fixtures:     31181340889 — PASS
```

Matrix:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Each P5 matrix job passed:

- 2 SQLite runtime unit tests;
- 1 full SQLite profile report integration test;
- 5 SQLite report anti-overclaim tests;
- 5 P5 manifest anti-overclaim tests;
- 1 full PostgreSQL↔SQLite C3 integration test;
- exact PostgreSQL P4, SQLite P5 and C3 report generation/validation;
- P1–P4 regressions;
- compileall;
- artifact upload.

## Artifacts

Each artifact contains:

```text
postgresql-p4-report.json
sqlite-p5-report.json
c3-equivalence-report.json
```

| Environment | Artifact digest |
|---|---|
| Python 3.11 / PostgreSQL 16 | `sha256:6e74f1be560afa54033beaa0c396d8395ed47d27ee89961746cda416e42cb8a5` |
| Python 3.11 / PostgreSQL 18 | `sha256:dec4f52dd6f7d6b6d71251bc9f931bcfc115ba65deae5a1ed888f77ea71ca680` |
| Python 3.12 / PostgreSQL 16 | `sha256:727b2a204035acb1d9fd116faecb284e8c8dda81722cb3646510cd1e779143bb` |
| Python 3.12 / PostgreSQL 18 | `sha256:705182b68f5806274723c43ea0d4c3cb1f240baf623db5260f151f24bacfea29` |

Artifacts are retained for 30 days.

One archive was independently inspected after download. It contained all three reports; the C3 report was bound to the exact head/run/environment, emitted 72 results with `45/10/17/0`, and all eight cross-profile checks were `PASS`.

## Negative evidence and fixes

1. Initial P5 test run failed because three tests referenced a non-existent `contracts/fixtures/fixture-pack.json`; all were corrected to the canonical committed `contracts/fixture-pack.json`.
2. Generic `nk-evidence-report/1` runner rejected the separate `nk-equivalence-report/1` protocol. The workflow was corrected to generate C3 directly through the comparator and validate it with the dedicated equivalence validator. The protocol distinction was preserved rather than weakened.
3. Bot-generated commits produced GitHub `action_required` instead of nested CI. A connector-authored commit triggered the actual matrix; this was not treated as test evidence.

## Exact boundary

```text
C3 for 45 SUPPORTED assertions
≠ support for all 72
≠ PostgreSQL and SQLite operational equivalence
≠ truth/authenticity
≠ physical or cryptographic deletion
≠ complete conflict subsystem
≠ C4/C5
≠ production readiness
```

## Remaining risks

- comparison scenarios are bounded, not exhaustive;
- SQLite and PostgreSQL failure behavior outside declared scenarios may diverge;
- concurrency, failover, backup/restore and managed-provider behavior are not equivalent;
- complete conflict representation/resolution remains absent;
- physical deletion and restore-before-visibility remain absent;
- artifacts expire;
- future contract/profile changes can invalidate C3 and require new evidence;
- Issue #18 publication/licensing remains unresolved.

## Finalization gate

1. synchronize public and AI documentation;
2. run P5/C3, P4, P1, fixtures and AI-context on one final exact PR head;
3. verify four final-head artifacts and inspect one archive;
4. inspect PR diff, comments, reviews and unresolved threads;
5. merge only with C4/C5/production/deletion/ecosystem scope absent;
6. publish a post-merge continuity checkpoint and synchronize Notion;
7. require a new explicit GO for any later phase or operational claim.
