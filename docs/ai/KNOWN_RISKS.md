# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-06  
**Last verified public `main`:** `9fd608f3f1d2915b961644015eb6b5e1a93e84d3`  
**Latest implementation:** PR #44 / P1 semantic core

P1 code reduces architecture-only risk, but it does not close storage, replay, security, privacy, licensing or portability risks.

## P0 — Authentic source recovery remains unresolved

**State:** `OPEN`

The reported `v0.1.2.1` source and original 44-test suite remain absent from accessible sources.

Required proof: authentic bytes, lineage, hashes, original test inventory and explicit Issue #1 operator gate.

## P0 — Clean P1 may be mistaken for recovered history

**State:** `OPEN`, narrowed by ADR-0015 and manifest guards

```text
clean/postgresql-reference/0.1
≠ v0.1.2.1
≠ original 44-test evidence
```

Every future package, report and release must preserve this boundary.

## P0 — P1 semantic core may be mistaken for a complete Kernel

**State:** `OPEN`

P1 implements canonical identity, domain objects, authority, logical reduction, deletion transitions and Receipt guards.

It does not implement durable history, append/idempotency, a database adapter, projection persistence, network API or profile conformance.

Required control: public surfaces use `P1 PARTIAL / SEMANTIC CORE ONLY`.

## P0 — Logical reducer may be mistaken for durable replay

**State:** `OPEN`

The reducer processes supplied in-memory `SemanticEvent` objects and checks version/sequence continuity. It does not verify durable commits, event chains, crashes, truncation, forks, upcasters or persisted projection rebuild.

Required proof before replay claims: separate P2/P3 storage and failure evidence.

## P0 — Local tests may be mistaken for C1/C2

**State:** `OPEN`, machine-readable guard retained

Final P1 content passed 31 focused tests and compile/manifest validation in local Python 3.13.5. The declared profile range is Python 3.11/3.12, and no exact repository workflow run was created.

```text
local final-content evidence: LOCALLY_TESTED
repository Python 3.11/3.12: NOT_RECORDED
kernel_runtime_conformance:  UNSUPPORTED
```

Required proof for later levels: exact declared-range CI, pinned environment, artifacts and an assertion-scoped conformance adapter.

## P0 — Provisional digests may become accidental Canon

**State:** `OPEN`

`nkd0` and `nks0` are P1 implementation details. They are not accepted cross-profile contracts.

Required control: no external profile, migration or persistent schema may depend on them without a separate contract/ADR.

## P1 — GitHub Actions execution remains unrecorded

**State:** `OPEN`

Workflow definitions exist for P1 and AI-context validation, but PR head `273d9369…` and merge `9fd608f3…` have no recorded run.

Required proof: exact run ID, head SHA, Python 3.11/3.12 jobs, conclusions, logs and artifacts.

## P1 — Python may become accidental permanent architecture

**State:** `OPEN`, narrowed

P1 uses Python standard library as a reversible profile choice. Semantic contracts must remain independent from Python dataclasses, types and module layout.

## P1 — Authority adapter may be mistaken for an operational security system

**State:** `OPEN`

`StaticAuthorityPolicy` is deterministic and deny-by-default, but has no credentials, identity provider, revocation, persisted delegation or operational audit.

Required proof: separate authority/security profile and threat model.

## P1 — Deletion state semantics may be mistaken for byte deletion

**State:** `OPEN`

P1 validates transitions and Receipt limits but deletes no primary data, backups, indexes, logs, exports or keys.

Required proof: profile-specific data-location implementation, retries/failures, backup/restore evidence and security/legal review.

## P1 — Accepted contracts are only partially implemented

**State:** `OPEN`

P1 exercises selected NK-ID, NK-SEM, NK-AUT, NK-EVT and deletion code paths. It does not provide complete assertion-level support.

All 72 assertions remain runtime `UNSUPPORTED` until P4.

## P1 — PostgreSQL work remains blocked

**State:** `OPEN / REQUIRES SEPARATE GO`

P2 requires explicit decisions on PostgreSQL versions, driver, migration tool, writer lease/epoch, transaction schema, dependency policy and Issue #18 license compatibility.

## P1 — SQL schema may become accidental Canon

**State:** `OPEN`

Future tables, constraints, indexes and surrogate keys must remain profile details. Semantic identity must survive storage replacement.

## P1 — NK-EPI status may be hidden by implementation progress

**State:** `OPEN`

ADR-0008 and `NK-EPI-001…008` remain proposed. P1 does not implement or accept them.

## P1 — Storage neutrality remains unproven

**State:** `OPEN`

No storage adapter exists. C3 requires a materially independent second profile and declared equivalence.

## P1 — Cross-project authority leakage

**State:** `OPEN`

P1 does not authorize Titan, Mentaury or Crystal integration, shared storage, identity or inherited conformance.

## P1 — License and contribution terms unresolved

**State:** `OPEN`, Issue #18

P1 uses no external dependencies and is not packaged, but publication, reuse and contribution terms remain undecided.

## Update rule

Record exact state, evidence, SHA, remaining uncertainty and next action. Never close a risk through prose, approval, local tests, manifest coverage or code presence alone.
