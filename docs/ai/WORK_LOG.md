# 🧾 Native Kernel AI Engineering Work Log

This is a concise chronology and hand-off surface. Re-verify exact SHAs, runs and artifacts before treating an entry as present reality.

---

## 2026-08-07 — P5 SQLite and assertion-scoped C3 merged

```text
Status:          MERGED / P5 PARTIAL / SQLITE C2 + CROSS-PROFILE C3
Issue / PR:      #58 / #59
Base main:       1dc493e9d23b99ee4bbf6015348599cd56f6cb56
Final PR head:   6483c9a229aea7d49929745b7652e67f1c39949c
Merge/main:      a8bb0ae232b977856730a1a4f21f977c1f69ca0a
PostgreSQL:      native-kernel/postgresql-reference@0.4-p4
SQLite:          native-kernel/sqlite-embedded@0.5-p5
ADR:             ADR-0019
C4/C5/production: NOT AUTHORIZED / NOT ESTABLISHED
Notion impact:   GITHUB_AND_NOTION
```

```text
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
support_state:     PARTIAL
```

Implemented:

- materially independent stdlib `sqlite3` profile;
- SQLite migrations, instance registration and transaction pragmas;
- `BEGIN IMMEDIATE` single-writer envelope;
- owner/epoch/expiry fencing;
- append/retry/idempotency conflict and rollback-safe ordering;
- Event commitments/hash-chain verification;
- replay, projection rebuild and bounded Receipts;
- stale-head/corruption detection;
- exact PostgreSQL authoritative-history import into SQLite;
- complete SQLite 72-ID report;
- separate `nk-equivalence-report/1` comparator;
- BYTE / STRUCTURAL / SEMANTIC / BEHAVIOURAL checks;
- strict validators and P5 manifest guards;
- 4× matrix with three reports per artifact and P1–P4 regressions.

Cross-profile evidence promotes only:

```text
NK-SEM-008
NK-ID-008
NK-EQV-002
NK-EQV-003
```

All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

### Final PR-head evidence

```text
P5/C3 31182711376 — PASS
P4    31182710450 — PASS
P1    31182711652 — PASS
Fixtures 31182710461 — PASS
AI context 31182710710 — PASS
Artifacts: 4 × 3 reports
```

### Main-push evidence

```text
P5/C3 31183074126 — PASS
P4    31183074048 — PASS
P1    31183073948 — PASS
Fixtures 31183073969 — PASS
AI context 31183073997 — PASS
Artifacts: 4 × 3 reports
```

Matrix in both gates:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

A final-head archive and a main-bound archive were each downloaded and inspected. Both contained PostgreSQL P4, SQLite P5 and C3 reports; C3 covered all 72 assertions with `45/10/17/0` and eight passed comparison checks.

Defects corrected without weakening requirements:

1. stale nested fixture path;
2. incorrect use of the single-profile runner for the separate equivalence protocol;
3. bot-generated `action_required` statuses excluded from evidence;
4. temporary bootstrap artifacts/workflows removed.

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

Remaining publication work: merge docs-only checkpoint, synchronize Notion and close Issue #58. Later phases remain separately gated.

---

## 2026-08-07 — P4 assertion-scoped conformance merged

```text
Issue / PR:    #55 / #56
Final PR head: 0e7adf71475d37d5c096718762cbc08086c5e465
Merge:         db6d65f69f7fc0c42861e5ab45869ec9c2f3d8ad
Checkpoint:    1dc493e9d23b99ee4bbf6015348599cd56f6cb56
ADR:           ADR-0018
```

PostgreSQL P4 added complete 72-ID evidence reporting with `41/13/18/0` and assertion-scoped C2.

---

## 2026-08-07 — P3 replay/projections/Receipts merged

```text
Issue / PR: #49 / #50
Merge:      4af642930e18752f8f8b0bce75df355f76100d6f
ADR:        ADR-0017
```

---

## 2026-08-07 — P2 PostgreSQL append/idempotency merged

```text
Issue / PR: #46 / #47
Merge:      113452a365890bf6c143d76657b810be59530ed4
ADR:        ADR-0016
```

---

## 2026-08-06 — P1 semantic core merged

```text
Issue / PR: #43 / #44
Merge:      9fd608f3f1d2915b961644015eb6b5e1a93e84d3
ADR:        ADR-0015
```

---

## Continuing rule

Record exact PR/SHA, support counts, evidence level, artifacts, limitations, Notion state and next action. Never infer complete support, truth, authenticity, physical deletion, operational equivalence or production readiness from C2/C3 evidence.
