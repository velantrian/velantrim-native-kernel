# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-06  
**Last verified public `main`:** `9ccbb535e22438092393e2686eb76eb362adb29d`  
**Active branch:** `agent/p1-semantic-core@5507901f688fffa49acc907de185acc287e27c63`

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

Every future package, report and release must repeat this boundary.

## P0 — P1 semantic core may be mistaken for a complete Kernel

**State:** `OPEN`

P1 implements canonical identity, domain objects, authority, logical reduction, deletion transitions and Receipt guards.

It does not implement durable history, append/idempotency, a database adapter, projection persistence, network API or profile conformance.

Required control: public surfaces use `P1 PARTIAL / SEMANTIC CORE ONLY`.

## P0 — Logical reducer may be mistaken for durable replay

**State:** `OPEN`

The reducer processes supplied in-memory `SemanticEvent` objects and checks version/sequence continuity. It does not verify durable commits, payload/event hash chains, crashes, truncation, forks, upcasters or persisted projection rebuild.

Required proof before replay claims: P2/P3 storage and failure evidence.

## P0 — Local tests may be mistaken for C1/C2

**State:** `OPEN`, machine-readable guard added

```text
20 semantic tests PASS
4 manifest tests PASS
compileall PASS
```

These prove only tested P1 behavior. `p1-manifest.json` keeps `kernel_runtime_conformance: UNSUPPORTED`, and the validator rejects C1 promotion.

Required proof for later levels: assertion-scoped conformance adapter, exact repository CI, pinned environment and artifacts.

## P0 — Provisional digests may become accidental Canon

**State:** `OPEN`

`nkd0` and `nks0` are P1 implementation details for command and state determinism. They are not accepted cross-profile contracts.

Required control: no external profile, migration or persistent schema may depend on them without a separate contract/ADR.

## P1 — GitHub Actions execution remains unrecorded

**State:** `OPEN`

The branch declares Python 3.11/3.12 workflow checks and artifact output. No exact repository run is yet recorded.

Required proof: run ID, exact head SHA, jobs, conclusions, logs/artifact.

## P1 — Python may become accidental permanent architecture

**State:** `OPEN`, narrowed

P1 uses Python standard library because it is dependency-free and aligned with existing tooling. This is a reversible profile choice.

Required control: semantic contracts stay independent from Python types, dataclass behavior and module layout.

## P1 — Authority test adapter may be mistaken for authentication/authorization system

**State:** `OPEN`

`StaticAuthorityPolicy` is deterministic and deny-by-default, but it is only a local P1 authority adapter. It has no credentials, identity provider, revocation, delegation persistence or operational audit.

Required proof: separate security/authority profile and threat model.

## P1 — Deletion state semantics may be mistaken for byte deletion

**State:** `OPEN`

P1 validates transitions and Receipt limits but deletes no primary data, backups, indexes, logs, exports or keys.

Required proof: profile-specific data-location inventory, implementation, retry/failure evidence, backup/restore behavior and legal/security review.

## P1 — Accepted contracts are only partially implemented

**State:** `OPEN`

P1 exercises parts of NK-ID, NK-SEM, NK-AUT, NK-EVT logical reduction and deletion semantics. It does not provide complete assertion-level support.

All 72 assertions therefore remain runtime `UNSUPPORTED` until P4.

## P1 — PostgreSQL work remains undecided

**State:** `OPEN / BLOCKED BY SEPARATE GO`

P2 requires decisions on PostgreSQL/server versions, driver, migration tool, writer lease/epoch, transaction schema, dependency policy and Issue #18 license compatibility.

## P1 — SQL schema may become accidental Canon

**State:** `OPEN`

Future tables, constraints, indexes and surrogate keys must remain profile details. Semantic identity must survive storage replacement.

## P1 — Registry/profile work can hide proposed NK-EPI status

**State:** `OPEN`

ADR-0008 and `NK-EPI-001…008` remain proposed. P1 does not implement them.

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

Record exact state, evidence, SHA, remaining uncertainty and next action. Never close a risk through prose, operator approval, local tests, manifest coverage or code presence alone.
