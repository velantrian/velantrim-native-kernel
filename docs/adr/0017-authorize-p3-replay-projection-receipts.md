# ADR-0017: Authorize bounded P3 replay, projection rebuild and operational Receipts

- **Decision status:** `ACCEPTED`
- **Evidence level:** `LOCALLY_TESTED_UNIT_ONLY` pending repository PostgreSQL matrix
- **Implementation status:** `PARTIAL — P3 CODE UNDER REVIEW`
- **Operator approval:** `APPROVED`
- **Date:** `2026-08-07`
- **Decider:** `@velantrian`
- **Track:** `Implementation Profile`
- **Related:** Issue #49, PR #50, RFC-0002, ADR-0012, ADR-0015, ADR-0016

## Context

P1 provides deterministic semantic reduction. P2 provides authoritative PostgreSQL append, durable idempotency, writer fencing and hash commitments. Neither phase replays persisted history into state, rebuilds disposable projections or records bounded operational evidence for those operations.

The operator separately authorized P3 on 2026-08-07.

## Decision

Implement the following bounded profile path:

```text
authoritative PostgreSQL Events
→ repeatable-read read-only snapshot
→ canonical payload/envelope verification
→ global and stream sequence verification
→ global hash-chain verification
→ explicit deterministic upcaster registry
→ P1 reducer from empty state
→ bounded Replay Receipt
→ locked history-head comparison
→ disposable projection upsert/generation
→ bounded Projection Rebuild Receipt
```

The replay target is the accepted P1 reducer version and explicitly declared target Event schema. A missing, ambiguous, cyclic or non-progressing upcaster path fails rather than silently coercing persisted history.

## Projection publication boundary

A replay snapshot is read independently. Before a projection or persisted Replay Receipt is published, the implementation locks the Kernel instance row and compares the authoritative global sequence/hash head with the replay snapshot.

If history advanced, publication fails as `HistoryAdvanced`. The implementation must not publish an obsolete projection as current.

Projection records are disposable read models. They may be destroyed and rebuilt. Projection generation is monotonic per instance/projection and is derived from prior committed rebuild Receipts, so deleting a projection does not reset its evidence lineage.

## Receipt boundary

P3 persists canonical Receipts for `REPLAY` and `PROJECTION_REBUILD`. A Receipt may establish only:

- the selected Kernel instance;
- the Event range and head observed;
- the reducer and target schema version;
- the resulting state digest;
- the projection name/generation when applicable;
- the declared proof limitations.

A P3 Receipt must not claim:

- truth of recorded Claims;
- external authenticity, signatures or notarization;
- absence of every privileged rewrite before the snapshot;
- complete Event Integrity under every threat model;
- physical deletion of bytes, backups, exports, logs or keys;
- C1, C2, C3, production durability, security, privacy or compliance.

## Integrity boundary

Replay reuses P2 stored-event validation and additionally checks:

- instance head equals Event count/max global sequence;
- every sequence from 1 through the captured head exists;
- `prev_global_hash` forms one contiguous chain from `GENESIS`;
- the replayed final hash equals the captured instance head;
- reducer global/per-stream sequence checks pass;
- every Event reaches the declared target schema through the explicit registry.

This is bounded integrity evidence, not cryptographic authenticity or protection from every privileged database rewrite.

## Rejected and deferred alternatives

- replaying directly from mutable projections: rejected because projections are disposable;
- silently treating unknown schemas as current: rejected;
- publishing projection state without a post-replay head comparison: rejected;
- resetting generation after projection deletion: rejected;
- adding P4 assertion evidence in the same phase: deferred;
- physical deletion and backup/key evidence: deferred to a separate decision;
- multi-writer consensus, network API and ecosystem integration: outside P3.

## Evidence gate

Initial local evidence:

```text
5 P3 semantic tests PASS
5 P3 manifest tests PASS
P3 manifest validator PASS
compile/py_compile PASS
7 PostgreSQL integration scenarios DECLARED / NOT RUN LOCALLY
```

Repository PostgreSQL 16/18 × Python 3.11/3.12 evidence is required before P3 may be described as repository-integration-tested.

All 72 registry assertions remain runtime `UNSUPPORTED` until P4 emits complete assertion-scoped evidence.

## Explicit non-goals

- no P2 append redesign;
- no physical or cryptographic deletion;
- no network API;
- no P4 conformance adapter or assertion promotion;
- no P5 SQLite profile;
- no C1/C2/C3;
- no package publication decision under Issue #18;
- no Titan, Mentaury or Crystal runtime wiring;
- no Issue #1 recovery claim;
- no ADR-0008 or NK-EPI promotion;
- no production credentials, HA, backup, restore or compliance guarantee.

## Next gate

P4 requires a separate operator GO and must produce a complete assertion-scoped conformance report without inferring support from P1/P2/P3 code presence alone.
