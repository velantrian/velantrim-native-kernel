# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-06  
**Base public `main`:** `b0308452473f7577b738e95bbd5e0f9295f0ecce`  
**Active acceptance branch:** `agent/accept-contracts-11-14`

Accepted contracts, passing fixture tooling and active workflows do not close runtime, security, privacy or portability risks.

## P0 — Authentic source recovery remains unresolved

**State:** `OPEN`

The reported `v0.1.2.1` source and original 44-test suite are absent. Connected-source search found no authentic candidate; operator-controlled devices and archives remain outside connector evidence.

Required proof: authentic bytes, lineage, hashes, original tests and explicit Issue #1 operator gate.

## P0 — Support tooling may be mistaken for Kernel runtime

**State:** `OPEN`

The repository contains accepted schemas/contracts, fixtures, a reference canonicalizer, tests and a workflow definition.

```text
accepted assertion
≠ assertion implemented by a Kernel profile
fixture reader supported
≠ durable event store
≠ replay/deletion implementation
≠ C2/C3 Kernel conformance
```

Required control: the built-in report retains `kernel_runtime_conformance: UNSUPPORTED` and explicit `UNSUPPORTED` results for all 72 assertions.

## P0 — Accepted architecture may be mistaken for completed implementation

**State:** `OPEN`

ADR-0011 through ADR-0014 are `ACCEPTED / APPROVED`, while runtime remains `NOT_IMPLEMENTED`.

Required control: all public surfaces preserve:

```text
Decision status
≠ Evidence level
≠ Implementation status
≠ Operator approval
```

## P1 — GitHub Actions execution remains unrecorded

**State:** `OPEN`, mitigation added

Evidence:

- workflow `Conformance fixture integrity` is active;
- PR and push paths are declared;
- integration-originated matching pushes previously produced no Actions run;
- repository Actions settings returned `403` to the connected integration;
- this branch adds manual `workflow_dispatch`.

Current status:

```text
workflow definition: ACTIVE
manual dispatch: DECLARED AFTER MERGE
local tests: PASS (recorded package evidence)
repository execution: NOT YET RECORDED
repository-reproduced evidence: NOT ESTABLISHED
```

Required proof: exact workflow run ID, head SHA, jobs, conclusions and artifact/log evidence.

## P1 — GitHub ↔ Notion drift

**State:** `OPEN`, narrowed by dedicated contract record

Acceptance status, final PR/merge SHA, CI state and remaining runtime limits must remain synchronized. GitHub remains the authoritative technical/evidence package.

## P1 — Canonical identity accepted but unimplemented

**State:** `NARROWED BY ACCEPTED ADR-0011`, not closed

Accepted and locally exercised as fixtures:

- NFC UTF-8 compact sorted JSON;
- float/null rejection;
- domain-separated IDs;
- content/Claim/lineage/storage separation;
- collision and migration rules;
- golden and invalid vectors.

Missing: independent implementation, real-profile migration, repository execution and C3.

## P1 — Event append/replay accepted but unimplemented

**State:** `NARROWED BY ACCEPTED ADR-0012`, not closed

Accepted and fixture-tested:

- single authoritative writer;
- durable idempotency semantics;
- sequence ordering;
- payload/event commitments;
- projection-after-commit;
- replay version boundaries.

Missing: durable storage, crash injection, reducer/upcaster implementation, corruption recovery and production threat evidence. Hash chaining is not authenticity or consensus.

## P1 — Deletion/restriction accepted but unimplemented

**State:** `NARROWED BY ACCEPTED ADR-0013`, not closed

Accepted and fixture-tested:

- restriction versus logical erase versus physical deletion versus crypto-erasure;
- partial completion and retry;
- retention hold;
- restore quarantine;
- Receipt proof limits.

Missing: legal/security review, key hierarchy, providers, backups, incident handling and operational validation.

## P1 — Executable conformance remains support tooling

**State:** `NARROWED BY ACCEPTED ADR-0014`, not closed

Available:

- 72 assertion IDs and complete-status enforcement;
- identity, event, idempotency, deletion and epistemic fixtures;
- eight locally passing tests;
- tampering/missing/duplicate rejection;
- external adapter protocol;
- PR/push/manual workflow entry points.

Missing: exact repository workflow evidence, Kernel adapter, reducer outputs, two independent profiles, Shadow evidence and operational evidence.

## P1 — Registry acceptance can hide proposed NK-EPI status

**State:** `OPEN`

Registry version `1.1.0` accepts ADR-0011–0014 assertions but retains `NK-EPI-001…008` as `PROPOSED` under ADR-0008.

Required control: profiles and documentation must not treat fixture presence or overall registry publication as acceptance of ADR-0008.

## P1 — Storage neutrality unproven

**State:** `OPEN`

PostgreSQL/SQLite direction exists, but adapters and cross-profile replay evidence do not.

## P1 — Cross-project authority leakage

**State:** `OPEN`

Accepted Kernel contracts do not authorize Titan, Mentaury or Crystal integration, shared storage, shared identity or inherited authority.

## P1 — Future-substrate claims can become hype

**State:** `OPEN`

Neutrality is a versioned architecture target, not demonstrated portability, performance or superiority.

## Update rule

Record state, exact evidence/SHA, remaining uncertainty, owner and next action. Never close a risk through prose, merge, operator approval alone or support-tool success.
