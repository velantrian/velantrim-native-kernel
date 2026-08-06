# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-06  
**Last verified public `main`:** `c7610bc42fbc879c24e1a3a1408ebfaae1ac7340`  
**Active proposal:** `agent/contracts-14-17`

A detailed contract or passing fixture test does not close a runtime, security, privacy or portability risk.

## P0 — Authentic source recovery remains unresolved

**State:** `OPEN`

The reported `v0.1.2.1` source and original 44-test suite are not present in `main`. Connected accessible-source search found no authentic candidate bytes; operator-controlled devices and archives remain outside connector evidence.

Required proof: authentic archive/location, lineage, hashes, original tests and explicit operator GO.

## P0 — Documentation/support tooling can be mistaken for Kernel runtime

**State:** `OPEN`

The Issues #14–#17 branch adds schemas, fixtures, a reference canonicalizer, tests and CI definition. These are support/evidence tooling.

```text
fixture-integrity PASS
≠ durable event store
≠ reducer/replay runtime
≠ deletion implementation
≠ storage profile
≠ C2/C3 Kernel conformance
```

Required control: every report must retain `kernel_runtime_conformance: UNSUPPORTED` until a real profile maps and implements the assertions.

## P0 — AI/documentation continuity drift

**State:** `NARROWED`, not closed

The AI context guard checks structural integrity and checkpoint ancestry. It does not prove semantic freshness, bilingual equivalence or Notion synchronization.

## P1 — GitHub ↔ Notion drift

**State:** `OPEN`

Material architecture work requires a deep Notion record and final PR/merge SHA. GitHub remains the complete public technical/evidence package.

## P1 — Cross-project semantic or authority leakage

**State:** `OPEN`

Kernel events, Titan output, Mentaury identity and Crystal evidence remain independent authority domains. No fixture or shared identifier authorizes runtime integration.

## P1 — Foundational responsibilities collapse

**State:** `NARROWED BY ADR-0010 AND THE ISSUES #14–#17 PROPOSAL`, not closed

ADR-0010 accepts ownership separation. The branch adds proposed exact v1 contracts and stable machine-readable assertion IDs.

Residual proof:

- operator acceptance of ADR-0011–0014;
- real profile mappings;
- independently implemented readers/profiles;
- migration evidence;
- no silent discard of unsupported assertions.

## P1 — Canonical identity contract remains unaccepted

**State:** `NARROWED BY ADR-0011 PROPOSAL`, not closed

Available in the branch:

- NFC UTF-8 compact sorted JSON subset;
- floats and explicit null rejected;
- domain-separated `nkh1`, `nkc1`, `nkl1` identifiers;
- collision and migration rules;
- two golden and four invalid vectors;
- locally passing reference canonicalizer tests.

Still missing: operator acceptance, a materially independent reader, migration in a real profile and C3 evidence.

## P1 — Event append/replay integrity remains unimplemented

**State:** `NARROWED BY ADR-0012 PROPOSAL`, not closed

The proposal defines a single-writer baseline, durable idempotency semantics, contiguous ordering, atomic history/idempotency boundary, projection-after-commit rule, domain-separated commitments and replay/version boundaries.

Still missing: durable storage implementation, crash injection, reducer/upcaster implementation, corruption recovery and production threat evidence. A hash chain is not authenticity or consensus.

## P1 — Deletion/restriction remains unimplemented

**State:** `NARROWED BY ADR-0013 PROPOSAL`, not closed

The proposal distinguishes restriction, logical erase, physical deletion and crypto-erasure; defines location inventory, partial failure, retry, restore quarantine and Receipt limits.

Still missing: legal/security review, key hierarchy implementation, provider integration, backup lifecycle evidence, incident handling and operational validation.

## P1 — Executable conformance is partial support tooling

**State:** `NARROWED BY ADR-0014 PROPOSAL`, not closed

Available in the branch:

- 72 unique assertion IDs;
- schema and fixture bundles;
- identity, event, deletion and `NK-EPI` scenarios;
- five locally passing tests;
- standard-library validator and external adapter protocol;
- proposed Python 3.11/3.12 workflow.

Still missing:

- exact CI result for the final PR head;
- a Kernel implementation adapter;
- expected reducer state from a real runtime;
- two materially independent profiles before C3;
- Shadow or operational evidence.

## P1 — Storage neutrality is unproven

**State:** `OPEN`

PostgreSQL/SQLite direction exists, but no adapters or cross-profile replay evidence exist. The identity/event fixture proposal is necessary but insufficient.

## P1 — Epistemic fixture family is not accepted architecture

**State:** `NARROWED`, not closed

Positive and negative fixtures cover `NK-EPI-001…008`, but ADR-0008 remains proposed. Executable reviewability does not imply operator acceptance or runtime enforcement.

## P1 — Context sufficiency remains unproven

**State:** `OPEN`

```text
selected context ≠ sufficient evidence
minimal changed answer ≠ globally minimal Grip
stable answer ≠ correct answer
```

## P1 — Future-substrate claims can become hype

**State:** `OPEN`

Architecture neutrality remains a target. It is not proof of portability, performance or superiority on future substrates.

## Update rule

For every risk record state, exact evidence/SHA, what remains unproven, owner and next action. Do not close a risk through wording, ADR acceptance or fixture tooling alone.
