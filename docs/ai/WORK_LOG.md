# 🧾 Native Kernel AI Engineering Work Log

This is a concise chronology and hand-off surface. Re-verify exact SHAs and evidence before treating an entry as present reality.

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
P2–P5:           NOT AUTHORIZED
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

Repository evidence:

```text
PR #44 unresolved review threads: 0
submitted reviews:               0
Codex review:                    unavailable due usage limit
PR-head workflow runs:           0 / NOT_RECORDED
merge workflow runs:             0 / NOT_RECORDED
```

The declared profile range is Python 3.11/3.12. The local Python 3.13 result is an extra compatibility check and does not establish declared-range repository evidence.

```text
P1 local PASS
≠ PostgreSQL adapter
≠ durable append/idempotency
≠ authoritative replay
≠ assertion-level conformance
≠ C1/C2/C3
```

All 72 registry assertions remain runtime `UNSUPPORTED` until P4.

Next gates:

1. merge the post-P1 continuity checkpoint;
2. synchronize final SHA to Notion and close Issue #43;
3. keep P2 blocked until a separate operator GO;
4. obtain exact Python 3.11/3.12 workflow evidence when available;
5. preserve Issue #1 and Issue #18 as independent gates.

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

Record exact PR/SHA, scope, evidence, limitations, Notion state and next action. Never infer durable runtime, CI PASS or conformance from accepted architecture, local tests or code presence alone.
