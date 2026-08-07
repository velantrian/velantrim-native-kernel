# 🧾 Native Kernel AI Engineering Work Log

This is a concise chronology and hand-off surface. Re-verify exact SHAs, runs and artifacts before treating an entry as present reality.

---

## 2026-08-07 — P5 independent SQLite profile and C3 under review

```text
Status:          PR OPEN / P5 PARTIAL / C2+C3 PREVIOUS-HEAD EVIDENCE
Issue / PR:      #58 / #59
Base main:       1dc493e9d23b99ee4bbf6015348599cd56f6cb56
Evidence head:   d43a6ed28232e9fc8b62f84d9025386fb8bce6f7
PostgreSQL:      native-kernel/postgresql-reference@0.4-p4
SQLite:          native-kernel/sqlite-embedded@0.5-p5
SQLite lineage:  clean/sqlite-embedded/0.1
ADR:             ADR-0019
C4/C5/production: NOT AUTHORIZED / NOT ESTABLISHED
Notion impact:   GITHUB_AND_NOTION
```

Single-profile C2 map:

```text
41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
```

Cross-profile C3 map:

```text
45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
support_state: PARTIAL
```

Implemented:

- materially independent stdlib `sqlite3` profile;
- SQLite migrations, instance registration, WAL/pragmas and digest drift guards;
- `BEGIN IMMEDIATE` single-writer transaction envelope;
- owner/epoch/expiry fencing;
- append, retry, idempotency conflict and rollback-safe ordering;
- canonical Event commitments and hash-chain verification;
- SQLite replay, projection rebuild and bounded Receipts;
- stale-head and stored-corruption detection;
- exact PostgreSQL authoritative-history import into SQLite;
- complete SQLite 72-ID evidence report;
- separate `nk-equivalence-report/1` comparator;
- BYTE / STRUCTURAL / SEMANTIC / BEHAVIOURAL equivalence classes;
- strict SQLite/C3 validators and P5 manifest guards;
- Python 3.11/3.12 × PostgreSQL 16/18 workflow with SQLite version capture;
- three reports per artifact and P1–P4 regressions.

Cross-profile evidence promotes exactly:

```text
NK-SEM-008
NK-ID-008
NK-EQV-002
NK-EQV-003
```

All eight `NK-EPI` assertions remain `UNSUPPORTED / PROPOSED`.

Defects and corrections:

1. P5 tests referenced `contracts/fixtures/fixture-pack.json`; corrected to the canonical committed `contracts/fixture-pack.json`.
2. Generic evidence runner rejected `nk-equivalence-report/1`; C3 generation now uses the comparator directly and the dedicated equivalence validator. The distinct protocol was preserved.
3. GitHub `GITHUB_TOKEN` bot commits produced `action_required` nested workflows; a connector-authored commit triggered genuine CI. No bot-only status was counted as evidence.

Initial successful evidence:

```text
P5/C3 run 31181341275 — PASS
P4 run     31181341370 — PASS
P1 run     31181341405 — PASS
Fixtures   31181340889 — PASS
```

Matrix:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Four artifacts were retained for 30 days. Each contains:

```text
postgresql-p4-report.json
sqlite-p5-report.json
c3-equivalence-report.json
```

One archive was downloaded and inspected. It contained all three reports, exact head/run/version metadata, 72 results and eight passed cross-profile checks.

```text
C3 for 45 SUPPORTED assertions
≠ all 72 supported
≠ PostgreSQL/SQLite operational equivalence
≠ accepted NK-EPI
≠ truth/authenticity
≠ physical deletion
≠ C4/C5
≠ production readiness
```

Remaining work in this cycle:

1. finish public/RFC/profile/AI/Notion synchronization;
2. repeat P5/C3 and governance checks on one final exact PR head;
3. verify four final-head artifacts and inspect one archive;
4. inspect final diff, comments, reviews and unresolved threads;
5. merge PR #59 with expected head;
6. publish post-merge continuity evidence;
7. close Issue #58;
8. keep later phases and operational claims separately gated.

---

## 2026-08-07 — P4 assertion-scoped conformance merged

```text
Issue / PR:    #55 / #56
Final PR head: 0e7adf71475d37d5c096718762cbc08086c5e465
Merge:         db6d65f69f7fc0c42861e5ab45869ec9c2f3d8ad
Checkpoint:    1dc493e9d23b99ee4bbf6015348599cd56f6cb56
ADR:           ADR-0018
```

Implemented a complete PostgreSQL 72-ID evidence adapter with `41/13/18/0`, strict traceability and four retained C2 artifacts.

---

## 2026-08-07 — P3 replay, projections and bounded Receipts merged

```text
Issue / PR: #49 / #50
Merge:      4af642930e18752f8f8b0bce75df355f76100d6f
ADR:        ADR-0017
```

Implemented verified persisted replay, deterministic upcasting, disposable projection rebuild, stale-head rejection and bounded operational Receipts.

---

## 2026-08-07 — P2 PostgreSQL append/idempotency merged

```text
Issue / PR: #46 / #47
Merge:      113452a365890bf6c143d76657b810be59530ed4
ADR:        ADR-0016
```

Implemented checksum-locked migrations, writer fencing, atomic Event/idempotency persistence and rollback-safe ordering.

---

## 2026-08-06 — P1 semantic core merged

```text
Issue / PR: #43 / #44
Merge:      9fd608f3f1d2915b961644015eb6b5e1a93e84d3
ADR:        ADR-0015
```

Implemented canonical identity, immutable semantic objects, authority, deterministic reduction, semantic deletion transitions and Receipt overclaim guards.

---

## Continuing rule

Record exact PR/SHA, support counts, evidence level, artifacts, limitations, Notion state and next action. Never infer complete support, truth, authenticity, physical deletion, operational equivalence or production readiness from C2/C3 evidence.
