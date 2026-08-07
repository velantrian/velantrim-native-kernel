# 🧾 Native Kernel AI Engineering Work Log

This is a concise chronology and hand-off surface. Re-verify exact SHAs and evidence before treating an entry as present reality.

---

## 2026-08-07 — P3 replay, projections and bounded Receipts merged

```text
Status:          MERGED / P3 PARTIAL / REPOSITORY-INTEGRATION-TESTED
Issue:           #49
PR:              #50
Base main:       4e6be77196c633c25dd3896660335c1448b2baf5
Final PR head:   7e615bc633cbf966211d3b2815f51b8ff9eb9716
Merge SHA:       4af642930e18752f8f8b0bce75df355f76100d6f
Changed files:   35
Profile:         native-kernel/postgresql-reference@0.3-p3
Evidence line:   clean/postgresql-reference/0.1
ADR:             ADR-0017
P3:              MERGED
P4–P5:           NOT AUTHORIZED
Notion impact:   GITHUB_AND_NOTION
```

Final-head evidence:

```text
P3 run 31173133661 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
P2 regression run 31173133709 — PASS
P1 semantic core run 31173133657 — PASS
Fixture integrity run 31173133713 — PASS
AI context run 31173133635 — PASS
```

Each P3 matrix job passed 5 semantic tests, 5 manifest/anti-overclaim tests, 8 PostgreSQL integration scenarios, P2 regressions and compileall.

Independent review hardening:

1. updated stale P2 maturity expectations in AI-context regression tests;
2. required stored projections to match their linked rebuild Receipt;
3. hardened repository PASS-like manifest statuses;
4. removed a duplicate projector wrapper and duplicate integration case;
5. stabilized the projection-link diagnostic;
6. aligned manifest and implementation record to the deduplicated 8-scenario suite;
7. closed duplicate Issue #51 in favor of canonical Issue #49.

No push-to-main workflow run was recorded for merge `4af64293…`; this is `NOT_RECORDED`, not PASS.

```text
P3 integration PASS
≠ complete Kernel runtime
≠ truth or external authenticity
≠ physical deletion
≠ assertion-level conformance
≠ C1/C2/C3
≠ production guarantee
```

All 72 assertion statuses remain `UNSUPPORTED` until P4. P4 requires a separate operator GO.

---

## 2026-08-07 — P3 development checkpoint before merge

```text
Status:          HISTORICAL PR CHECKPOINT
Issue:           #49
PR:              #50
Base main:       4e6be77196c633c25dd3896660335c1448b2baf5
Initial head:    0f8fd4ffe5d5fb0d4bc01f3e441a053f691dbba3
Profile:         native-kernel/postgresql-reference@0.3-p3
Evidence line:   clean/postgresql-reference/0.1
ADR:             ADR-0017
```

Architecture path:

```text
authoritative PostgreSQL Events
→ repeatable-read snapshot
→ canonical/Event-chain/sequence verification
→ explicit deterministic UpcasterRegistry
→ P1 reducer from empty state
→ bounded Replay Receipt
→ locked current-head comparison
→ disposable projection rebuild
→ bounded Projection Rebuild Receipt
```

Implemented during the cycle:

- standard-library `UpcasterRegistry` with missing/duplicate/cycle/invalid-path failures;
- canonical `SemanticState` decoder and form check;
- repeatable-read selected-instance history snapshot;
- Event count/max sequence versus captured instance-head validation;
- full P2 stored-event canonical/hash validation during replay;
- `GENESIS → nke1` global chain validation;
- P1 reducer execution from empty state with global/per-stream checks;
- `operation_receipts` and disposable `projections` tables;
- canonical Replay and Projection Rebuild Receipts;
- hard truth/authenticity/complete-integrity/complete-erasure non-claims;
- locked current-head comparison before publication;
- `HistoryAdvanced` rejection for stale snapshots;
- atomic Receipt + projection commit and rollback on injected fault;
- projection destroy/read/rebuild;
- monotonic generation based on committed rebuild Receipts;
- Event, projection and Receipt corruption detection;
- P3 manifest/validator and PostgreSQL matrix workflow;
- P2 regression execution inside every P3 matrix job.

---

## 2026-08-07 — P2 PostgreSQL append/idempotency merged

```text
Status:          MERGED / P2 PARTIAL / REPOSITORY-INTEGRATION-TESTED
Issue:           #46
PR:              #47
Base main:       bb94835ad612f45e2629655bc9add872d8981357
Final PR head:   36ddb1d0342914f0c06fe7f31171bac06565ee72
Merge SHA:       113452a365890bf6c143d76657b810be59530ed4
Changed files:   31
Profile:         native-kernel/postgresql-reference@0.2-p2
Evidence line:   clean/postgresql-reference/0.1
ADR:             ADR-0016
P2:              MERGED
P3–P5:           NOT AUTHORIZED AT THAT CHECKPOINT
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
- P2 manifest/validator and repository workflow;
- bilingual RFC, ADR, README and AI-continuity synchronization.

Final-head repository evidence:

```text
P2 run 31152380799 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
AI context run 31152380802 — PASS
P1 semantic core run 31152380832 — PASS
Fixture integrity run 31152380800 — PASS
```

Each P2 matrix job passed 9 unit tests, 5 PostgreSQL integration tests, 5 manifest tests, validator and compileall.

Review evidence:

```text
unresolved review threads: 0
submitted reviews:          0
Codex review:               unavailable due usage limit
merge method:               squash with expected head
```

Two quality defects were found and corrected before merge:

1. the AI-context validator still required the old P1 maturity marker;
2. an anti-overclaim test became stale after the manifest legitimately moved to repository PASS.

A documentation-depth review also restored the accumulated README, RFC, ADR guide, component map, risk history and work-log chronology before adding P2 as a new layer.

No push-to-main workflow run was recorded for merge `113452a3…`; this is recorded as `NOT_RECORDED`, not PASS.

```text
P2 PostgreSQL integration PASS
≠ P3 replay/projection runtime
≠ operational deletion
≠ assertion-level conformance
≠ C1/C2/C3
≠ production guarantee
```

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

Manual review hardening corrected malformed authority scope, enum/type failures, timestamp validation, boolean sequences, grants, Receipt identifiers and deletion evidence.

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

Repository workflows for that checkpoint were `NOT_RECORDED`.

---

## 2026-08-06 — Clean PostgreSQL reference profile RFC published

PR #41 published RFC-0002 at `1e721aeb5b116694a0dbb417c377aa9f92b6f8e5`; PR #42 finalized continuity at `9ccbb535e22438092393e2686eb76eb362adb29d`.

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

Record exact PR/SHA, scope, evidence, limitations, Notion state and next action. Never infer truth, authenticity, physical deletion, production readiness or conformance from P3 integration evidence alone.
