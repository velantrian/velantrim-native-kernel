# ADR-0012: Single-writer append and replay contract v1

- **Decision status:** `PROPOSED`
- **Evidence level:** `LOCALLY_TESTED` fixture integrity only
- **Implementation status:** `PARTIAL` support tooling; Kernel runtime `NOT_STARTED`
- **Operator approval:** `PENDING`
- **Date:** `2026-08-06`
- **Related:** Issue #15, ADR-0010

## Context

Command validation, idempotency, authority, append, ordering, crash recovery, schema evolution and replay were named but not joined by one normative boundary.

## Decision proposal

Define v1 as a single-authoritative-writer model with durable idempotency, contiguous global and stream sequences, domain-separated payload/event commitments, explicit authority, atomic append plus idempotency record, post-commit disposable projections, explicit schema/reducer versions and replay from empty state.

The hash chain is an integrity signal under a declared threat model, not authenticity, consensus or complete Event Integrity.

## Rejected alternatives

- timestamp ordering;
- last-write-wins semantic resolution;
- projection and history in one mutable authority;
- multi-writer claims without a consensus contract;
- treating read-time deduplication as durable idempotency.

## Consequences

Fixtures can validate envelope continuity and projection-rebuild boundaries. Runtime append, crash injection and reducer evidence remain absent.
