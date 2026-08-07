# 🧾 Native Kernel AI Engineering Work Log

This is a concise chronology and hand-off surface. Re-verify exact SHAs and evidence before treating an entry as present reality.

---

## 2026-08-07 — P2 PostgreSQL append/idempotency implemented and repository-tested

```text
Status:          PR OPEN / P2 PARTIAL / REPOSITORY-INTEGRATION-TESTED
Issue:           #46
PR:              #47
Base main:       bb94835ad612f45e2629655bc9add872d8981357
Evidence head:   e80492bcacde2ff2be3a2ee03aa5aa53a714d288
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
repository matrix PG16/18 × Python 3.11/3.12
psycopg >=3.3,<3.4
numbered SQL + SHA-256 migration ledger
one DB-backed writer owner/epoch lease per instance
rollback-safe row-locked counters
```

Implemented:

- lazy Psycopg boundary preserving P1 standard-library imports;
- checksum-locked migrations with advisory-lock serialization;
- Kernel instance/history head;
- monotonic writer owner/epoch/expiry lease;
- stale and expired writer failures;
- atomic Event/idempotency transaction;
- same-digest original-result return and conflicting-key rejection;
- rollback-safe global/stream counters;
- canonical payload/envelope bytes and `nkp1`/`nke1` commitments;
- stored-event consistency checks;
- P2 manifest/validator and repository workflow.

Repository evidence:

```text
P2 run 31151297646 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
AI context run 31151298002 — PASS
P1 semantic core run 31151297696 — PASS
Fixture integrity run 31151298177 — PASS
```

Each P2 matrix job passed 9 unit tests, 5 PostgreSQL integration tests, 5 manifest tests, validator and compileall.

The first PR head exposed a stale P1 marker in the AI-context validator. The validator and regression test were updated; the next evidence head passed AI-context on Python 3.11/3.12.

Manual documentation review also found over-compression of the README, RFC and component map. Their original architecture/navigation depth was restored, then P2 was added as a new layer rather than replacing historical context.

```text
P2 PostgreSQL integration PASS
≠ P3 replay/projection runtime
≠ operational deletion
≠ assertion-level conformance
≠ C1/C2/C3
≠ production guarantee
```

All 72 assertion statuses remain `UNSUPPORTED` until P4.

Remaining work in this cycle:

1. pass P2 and AI-context checks on one final PR head;
2. inspect full diff, comments and review threads;
3. merge only with P3/P4/P5 scope absent;
4. record final merge/main SHA in GitHub and Notion;
5. close Issue #46 and keep P3 blocked.

---

## 2026-08-06 — P1 profile-independent semantic core merged

```text
Status:          MERGED / P1 PARTIAL / LOCALLY_TESTED
Issue:           #43
PR:              #44
Base main:       9ccbb535e22438092393e2686eb76eb362adb29d
Final PR head:   273d9369e624d8e4c4033dc7842ebbcc46642668
Merge SHA:       9fd608f3f1d2915b961644015eb6b5e1a93e84d3
Changed files:   30
Profile ID:      native-kernel/postgresql-reference
Evidence line:   clean/postgresql-reference/0.1
RFC-0002:        ACCEPTED / APPROVED
ADR:             ADR-0015
P1:              MERGED
P2–P5:           NOT AUTHORIZED AT THAT CHECKPOINT
Issue #1:        ACTIVE / INDEPENDENT
Notion impact:   GITHUB_AND_NOTION
```

Technology choice:

```text
Python profile: >=3.11,<3.13
standard library only
package: native_kernel.semantic_core
```

This is a reversible implementation-profile choice, not Architecture Canon.

Implemented:

- canonical `nk-id/1.0` JSON/identity helpers;
- immutable semantic content, Claim identity, command and logical Event models;
- explicit deny-by-default local authority policy;
- deterministic version-bound in-memory reducer;
- deletion/restriction transition graph;
- admission/deletion Receipt overclaim rejection;
- explicit contract/authority/version/sequence/transition failures;
- historical P0 and current P1 manifests kept separate;
- P1 manifest validator and negative tests;
- Python 3.11/3.12 workflow definition;
- bilingual RFC, ADR, README and AI-continuity updates.

Manual review hardening corrected:

1. duplicated authority scope `stream:stream:*`;
2. late enum/type failures;
3. calendar-invalid UTC timestamps;
4. boolean values accepted as integer sequences;
5. malformed authority grants and Receipt identifiers/limits;
6. malformed deletion-state/location evidence.

Exact final-content local evidence:

```text
20 semantic-core tests PASS
4 P1-manifest tests PASS
7 AI-context validator tests PASS
Python compileall PASS
P1 manifest validator PASS
local interpreter Python 3.13.5
external dependencies NONE
```

Repository evidence at that checkpoint:

```text
PR #44 unresolved review threads: 0
submitted reviews:               0
Codex review:                    unavailable due usage limit
PR-head workflow runs:           0 / NOT_RECORDED
merge workflow runs:             0 / NOT_RECORDED
```

The declared profile range was Python 3.11/3.12. The local Python 3.13 result was an extra compatibility check, not declared-range repository evidence.

```text
P1 local PASS
≠ PostgreSQL adapter
≠ durable append/idempotency
≠ authoritative replay
≠ assertion-level conformance
≠ C1/C2/C3
```

---

## 2026-08-06 — Clean PostgreSQL reference profile RFC published

PR #41 published RFC-0002 at `1e721aeb5b116694a0dbb417c377aa9f92b6f8e5`; PR #42 finalized continuity at `9ccbb535e22438092393e2686eb76eb362adb29d`.

The plan introduced `native-kernel/postgresql-reference`, clean lineage `clean/postgresql-reference/0.1`, a 72-assertion planning manifest, validator and phased P0–P5 roadmap.

---

## 2026-08-06 — Exact contracts accepted and finalized

PR #38 accepted ADR-0011…0014 at `ff88809fe7d7c79033a150140d20618e04aa1f9d`; PR #39 finalized continuity at `350734c8ce8d8cbc742def7df9f3d5044a5953ab`.

---

## 2026-08-06 — Contract fixture package published

PR #35 → `0552ae284d56148972e9bcc8de5f80a7f462c0f3`; PR #36 → `3243336dc7ff7ef88583c6f2c419c375c26947cf`; PR #37 → `b0308452473f7577b738e95bbd5e0f9295f0ecce`.

---

## 2026-08-06 — Foundational contract skeleton accepted

PR #28 → `2d42a1517ba87b39d2395aa5c22b966328615305`.

---

## Continuing rule

Record exact PR/SHA, scope, evidence, limitations, Notion state and next action. Never infer replay, production readiness or conformance from P2 integration evidence alone.
