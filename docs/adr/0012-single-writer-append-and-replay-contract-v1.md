# ADR-0012: Single-writer append and replay contract v1

- **Decision status:** `ACCEPTED`
- **Evidence level:** `LOCALLY_TESTED` fixture integrity only
- **Implementation status:** `PARTIAL` support tooling; Kernel runtime `NOT_STARTED`
- **Operator approval:** `APPROVED`
- **Date:** `2026-08-06`
- **Deciders:** `@velantrian`
- **Track:** `Abstract Contract / NK-EVT`
- **Related:** Issue #15, ADR-0010

## Context

Command validation, idempotency, authority, append, ordering, crash recovery, schema evolution and replay were named but not joined by one normative boundary.

## Decision

Adopt `nk-event/1.0` as a single-authoritative-writer model with durable idempotency, contiguous global and stream sequences, domain-separated payload/event commitments, explicit authority, atomic append plus idempotency record, post-commit disposable projections, explicit schema/reducer versions and replay from empty state.

The hash chain is an integrity signal under a declared threat model, not authenticity, consensus or complete Event Integrity.

The operator approved this architectural contract on 2026-08-06. Approval accepts the semantic and ordering boundary; it does not claim that append, crash recovery, reducer execution or replay is implemented in a Native Kernel runtime.

## Rejected alternatives

- timestamp ordering;
- last-write-wins semantic resolution;
- projection and history in one mutable authority;
- multi-writer claims without a consensus contract;
- treating read-time deduplication as durable idempotency.

## Consequences

Fixtures can validate envelope continuity, idempotency cases and projection-rebuild boundaries. Runtime append, crash injection, reducer/upcaster execution and durable replay evidence remain absent.

## Evidence and promotion gates

- operator decision: `APPROVED`;
- event/idempotency fixture integrity: `LOCALLY_TESTED`;
- repository workflow result: not yet recorded;
- durable event store and reducer: absent;
- C2 requires a committed runtime profile, exact tests and repository reproduction;
- C3 requires materially independent profiles and declared equivalence.
