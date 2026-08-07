# 🧾 Native Kernel AI Engineering Work Log

Re-verify exact SHAs and workflow evidence before treating an entry as current reality.

---

## 2026-08-07 — P2 PostgreSQL append/idempotency authorized and implemented on branch

```text
Status:          ACTIVE BRANCH / P2 PARTIAL / UNIT-TESTED
Issue:           #46
Base main:       bb94835ad612f45e2629655bc9add872d8981357
Branch:          agent/p2-postgresql-append
Profile:         native-kernel/postgresql-reference@0.2-p2
Evidence line:   clean/postgresql-reference/0.1
ADR:             ADR-0016
P2:              AUTHORIZED
P3–P5:           NOT AUTHORIZED
Notion impact:   GITHUB_AND_NOTION
```

Technology decision:

```text
PostgreSQL 16–18
CI matrix 16/18 × Python 3.11/3.12
psycopg >=3.3,<3.4
numbered SQL + SHA-256 migration ledger
one DB-backed writer owner/epoch lease per instance
rollback-safe row-locked counters
```

Implemented:

- lazy driver boundary preserving P1 standard-library imports;
- profile schema for instances, leases, stream counters, Events and idempotency;
- advisory-lock-serialized migration bootstrap and checksum drift detection;
- monotonic instance writer epoch and stale/expired token failures;
- atomic Event/idempotency transaction;
- same-digest retry returning the original Event;
- conflicting key reuse failure;
- rollback-safe global and stream ordering;
- canonical payload/envelope bytes and `nkp1`/`nke1` commitments;
- stored Event consistency checks;
- unit, manifest and PostgreSQL integration suites;
- P2 manifest/validator and repository workflow definition;
- bilingual RFC, README and AI continuity updates.

Local evidence before publication:

```text
9 P2 unit tests PASS
5 P2 manifest tests PASS
P2 manifest validator PASS
compileall PASS
5 PostgreSQL integration tests SKIPPED — no local PostgreSQL/DSN
local Python 3.13.5
repository CI NOT_RECORDED
```

Evidence boundary:

```text
P2 unit PASS
≠ PostgreSQL integration PASS
≠ replay/projection runtime
≠ conformance
≠ C1/C2/C3
```

All 72 assertion results remain `UNSUPPORTED` until P4.

Next actions:

1. verify exact branch content and changed-file scope;
2. open PR and inspect PostgreSQL matrix runs;
3. fix exact-head failures without expanding into P3;
4. merge only with status limits intact;
5. synchronize final PR/merge/run evidence to Notion and Issue #46.

---

## 2026-08-06 — P1 semantic core merged

PR #44 final head `273d9369e624d8e4c4033dc7842ebbcc46642668`; merge `9fd608f3f1d2915b961644015eb6b5e1a93e84d3`; checkpoint PR #45 `bb94835ad612f45e2629655bc9add872d8981357`.

P1 added profile-independent identity, semantic objects, authority, reducer, deletion semantics and Receipt limits. Exact final content passed 31 focused local tests, while repository workflow evidence remained unrecorded.

---

## 2026-08-06 — Clean PostgreSQL profile plan accepted

RFC-0002 PR #41 → `1e721aeb5b116694a0dbb417c377aa9f92b6f8e5`; planning checkpoint → `9ccbb535e22438092393e2686eb76eb362adb29d`.

---

## 2026-08-06 — Exact contracts and fixture package

ADR-0011…0014 accepted through PR #38. Fixture package PRs #35–#37 published 72 assertion IDs, schemas, fixtures and reference integrity tooling.

---

## Continuing rule

Record exact PR/SHA, environment, evidence, limitations, Notion state and next action. Never infer production readiness, PostgreSQL integration, replay or conformance from code presence, unit tests or workflow definitions alone.
