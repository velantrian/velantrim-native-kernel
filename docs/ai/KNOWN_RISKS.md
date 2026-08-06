# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-06  
**Last verified public `main`:** `350734c8ce8d8cbc742def7df9f3d5044a5953ab`  
**Active proposal:** Draft PR #41 / RFC-0002 / Issue #40

Accepted contracts, passing tooling and a detailed profile plan do not close runtime, security, privacy, licensing or portability risks.

## P0 — Authentic source recovery remains unresolved

**State:** `OPEN`

The reported `v0.1.2.1` source and original 44-test suite are absent. Connected-source search found no authentic candidate; operator-controlled devices and archives remain outside connector evidence.

Required proof: authentic bytes, lineage, hashes, original tests and explicit Issue #1 operator gate.

## P0 — Clean profile may be mistaken for recovered history

**State:** `OPEN`, narrowed by RFC-0002 guardrails

RFC-0002 proposes `clean/postgresql-reference/0.1` and explicitly forbids:

- historical lineage claims;
- use of the `v0.1.2.1` identity;
- replacement of the original 44-test evidence;
- closing Issue #1 through new implementation work.

The planning validator rejects a non-null historical lineage and any permission to claim recovery.

Required control: every runtime package, migration, test report and release must repeat the clean-lineage boundary.

## P0 — Planning manifest may be mistaken for runtime support

**State:** `OPEN`, narrowed by machine-readable enforcement

The proposed manifest maps all 72 assertions, but mapping means planned coverage, not implementation.

```text
PLANNED
≠ SUPPORTED
≠ LOCALLY_TESTED runtime
≠ C2
```

All assertion rows currently state:

```text
runtime_support: UNSUPPORTED
evidence_state: NONE
```

The validator rejects missing/duplicate assertions, false support claims, historical lineage and silent promotion of `NK-EPI`.

## P0 — Support tooling may be mistaken for Kernel runtime

**State:** `OPEN`

```text
accepted assertion
≠ assertion implemented by a Kernel profile
fixture reader supported
≠ durable event store
≠ replay/deletion implementation
≠ C2/C3 Kernel conformance
```

Required control: built-in evidence reports retain `kernel_runtime_conformance: UNSUPPORTED` until a real profile demonstrates scoped behaviour.

## P0 — Accepted architecture may be mistaken for completed implementation

**State:** `OPEN`

ADR-0011 through ADR-0014 are accepted/approved, while RFC-0002 is proposed and runtime is not started.

```text
Decision status
≠ RFC status
≠ Evidence level
≠ Implementation status
≠ Operator approval
```

## P1 — GitHub Actions execution remains unrecorded

**State:** `OPEN`, validation surface expanded

The conformance workflow now includes profile-manifest tests and reports on Python 3.11/3.12. No exact repository run is claimed before GitHub records one.

Required proof: exact workflow run ID, head SHA, jobs, conclusions and artifacts for both conformance and profile-manifest reports.

## P1 — Profile implementation language and dependency policy undecided

**State:** `OPEN`

RFC-0002 deliberately does not select a permanent language, package layout, PostgreSQL driver or migration framework.

Issue #18 also leaves repository publication/contribution licensing unresolved. Dependency selection, package publication and outside contributions must not begin under assumed license permissions.

Required decisions before runtime:

- language/runtime range;
- dependency and package policy;
- PostgreSQL version matrix;
- driver/migration tooling;
- license compatibility and contribution terms.

## P1 — Single-writer boundary may be weakened by PostgreSQL concurrency

**State:** `OPEN`

PostgreSQL supports concurrent transactions, but RFC-0002 requires one authoritative writer per Kernel instance. Database concurrency alone does not create a safe multi-writer protocol.

Required proof: explicit writer lease/epoch mechanism, mismatch rejection, transaction/fault tests and incident fencing.

## P1 — SQL schema may become accidental Canon

**State:** `OPEN`

Tables, columns, constraints, surrogate keys, indexes and SQL transaction syntax are profile details. Semantic IDs and accepted contracts must survive schema or backend replacement.

Required proof: neutral export, replay, migration Receipt and future independent SQLite comparison.

## P1 — Deletion planning is insufficient for sensitive data

**State:** `OPEN`

RFC-0002 inventories payloads, commands, projections, evidence, logs, backups, replicas and migration artifacts but implements none of the deletion mechanisms.

Required proof: profile-specific location matrix, key hierarchy if used, retry/partial-failure tests, backup/restore evidence and security/legal review.

## P1 — GitHub ↔ Notion drift

**State:** `OPEN`

RFC status, PR/head/merge SHA, operator decision, runtime GO and evidence must remain synchronized. GitHub remains authoritative for technical/evidence claims.

## P1 — Canonical identity accepted but unimplemented

**State:** `NARROWED BY ACCEPTED ADR-0011`, not closed

Missing: independent implementation, real-profile migration, repository execution and C3.

## P1 — Event append/replay accepted but unimplemented

**State:** `NARROWED BY ACCEPTED ADR-0012`, not closed

Missing: durable storage, crash injection, reducer/upcaster implementation, corruption recovery and production threat evidence.

## P1 — Deletion/restriction accepted but unimplemented

**State:** `NARROWED BY ACCEPTED ADR-0013`, not closed

Missing: legal/security review, key hierarchy, providers, backups, incident handling and operational validation.

## P1 — Executable conformance remains support tooling

**State:** `NARROWED BY ACCEPTED ADR-0014`, not closed

Missing: exact repository workflow evidence, Kernel adapter, reducer outputs, two independent profiles, Shadow evidence and operational evidence.

## P1 — Registry/profile plan can hide proposed NK-EPI status

**State:** `OPEN`

`NK-EPI-001…008` remains proposed under ADR-0008. The profile manifest correctly defers all eight assertions with no implementation phase.

Required control: planning or fixture presence must not be described as architecture acceptance or runtime enforcement.

## P1 — Storage neutrality unproven

**State:** `OPEN`

A proposed PostgreSQL profile is not storage-neutrality evidence. C3 requires an independently developed second profile and declared equivalence.

## P1 — Cross-project authority leakage

**State:** `OPEN`

RFC-0002 does not authorize Titan, Mentaury or Crystal integration, shared storage, shared identity or inherited authority.

## P1 — Future-substrate claims can become hype

**State:** `OPEN`

Neutrality remains a versioned architecture target, not demonstrated portability or superiority.

## Update rule

Record state, exact evidence/SHA, remaining uncertainty, owner and next action. Never close a risk through prose, merge, operator approval alone, planning coverage or support-tool success.
