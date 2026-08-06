# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-06  
**Last verified public `main`:** `3243336dc7ff7ef88583c6f2c419c375c26947cf`

Passing fixture tooling, merged proposals and active workflows do not close runtime, security, privacy or portability risks.

## P0 — Authentic source recovery remains unresolved

**State:** `OPEN`

The reported `v0.1.2.1` source and original 44-test suite are absent. Connected-source search found no authentic candidate; operator-controlled devices and archives remain outside connector evidence.

Required proof: authentic bytes, lineage, hashes, original tests and explicit Issue #1 operator gate.

## P0 — Support tooling may be mistaken for Kernel runtime

**State:** `OPEN`

PR #35 published schemas, fixtures, a reference canonicalizer, tests and a workflow definition.

```text
fixture reader supported
≠ registered assertions supported by a Kernel runtime
≠ durable event store
≠ replay/deletion implementation
≠ C2/C3 Kernel conformance
```

The built-in report must retain `kernel_runtime_conformance: UNSUPPORTED` and 72 explicit `UNSUPPORTED` assertion results.

## P0 — ADR publication may be mistaken for acceptance

**State:** `OPEN`

ADR-0011 through ADR-0014 are present in `main` but remain `PROPOSED / OPERATOR_APPROVAL_PENDING`.

Required control: only an explicit operator decision may promote each ADR or the bounded package.

## P1 — GitHub Actions workflow execution not triggered

**State:** `OPEN`

Evidence:

- workflow `Conformance fixture integrity` is active, ID `328870784`;
- YAML and path filters are valid;
- PR #36 intentionally changed `contracts/README.md` and merged to `main`;
- no GitHub Actions run or GitHub Actions check suite was created for PR/merge heads;
- Actions permission settings returned `403` to the connected integration;
- external app suites were queued, showing the commit event existed.

Current status:

```text
workflow definition: ACTIVE
local tests: PASS
GitHub Actions execution: NOT_TRIGGERED / NOT_RECORDED
repository-reproduced evidence: NOT ESTABLISHED
```

Required proof: a user-originated push or manual workflow dispatch, followed by exact run/job/artifact inspection. The connector cannot dispatch the workflow.

## P1 — GitHub ↔ Notion drift

**State:** `OPEN`, narrowed by dedicated PR #35 record

Final main SHA, merge evidence and CI-not-triggered status must remain synchronized. GitHub remains the authoritative technical/evidence package.

## P1 — Foundational responsibility collapse

**State:** `NARROWED BY ADR-0010 AND PR #35`, not closed

The ownership map and 72-assertion registry now exist. Residual proof requires operator acceptance, real profile mappings, migration evidence and independent implementations.

## P1 — Canonical identity contract unaccepted/unimplemented

**State:** `NARROWED BY ADR-0011`, not closed

Defined and locally tested: NFC UTF-8 compact sorted JSON, float/null rejection, domain-separated IDs, collision/migration rules, golden and invalid vectors.

Missing: acceptance, independent implementation, real-profile migration and C3.

## P1 — Event append/replay unimplemented

**State:** `NARROWED BY ADR-0012`, not closed

Defined/tested as fixtures: single writer, durable idempotency semantics, sequence ordering, payload/event commitments, projection-after-commit and replay version boundaries.

Missing: durable storage, crash injection, reducer/upcaster implementation, corruption recovery and production threat evidence. Hash chaining is not authenticity or consensus.

## P1 — Deletion/restriction unimplemented

**State:** `NARROWED BY ADR-0013`, not closed

Defined/tested as fixtures: restriction, logical erase, physical deletion, crypto-erasure, partial retry, restore quarantine and Receipt limits.

Missing: legal/security review, key hierarchy, providers, backups, incidents and operational validation.

## P1 — Executable conformance remains support tooling

**State:** `NARROWED BY ADR-0014`, not closed

Available:

- 72 assertion IDs and complete-status enforcement;
- identity, event, idempotency, deletion and epistemic fixtures;
- eight locally passing tests;
- tampering/missing/duplicate rejection;
- external adapter protocol;
- active but not-yet-executed workflow.

Missing: repository workflow evidence, Kernel adapter, reducer outputs, two independent profiles, Shadow and operational evidence.

## P1 — Storage neutrality unproven

**State:** `OPEN`

PostgreSQL/SQLite direction exists, but adapters and cross-profile replay evidence do not.

## P1 — Epistemic fixtures do not accept ADR-0008

**State:** `NARROWED`, not closed

Positive/negative fixtures cover `NK-EPI-001…008`; ADR-0008 remains proposed and runtime enforcement absent.

## P1 — Future-substrate claims can become hype

**State:** `OPEN`

Neutrality is a versioned architecture target, not demonstrated portability, performance or superiority.

## Update rule

Record state, exact evidence/SHA, remaining uncertainty, owner and next action. Never close a risk through prose, merge, operator approval alone or support-tool success.
