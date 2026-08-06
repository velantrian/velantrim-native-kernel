# ADR-0013: Deletion, restriction and retention contract v1

- **Decision status:** `PROPOSED`
- **Evidence level:** `LOCALLY_TESTED` state-machine fixtures only
- **Implementation status:** `PARTIAL` support tooling; Kernel runtime `NOT_STARTED`
- **Operator approval:** `PENDING`
- **Date:** `2026-08-06`
- **Related:** Issue #16, ADR-0010

## Context

`ERASED` records a logical transition but cannot by itself prove deletion from payloads, projections, indexes, exports, providers, backups or logs.

## Decision proposal

Separate restriction, logical erase, physical deletion and cryptographic erasure. Require data-location inventory, authority/policy, idempotent retries, visible partial completion, quarantine-before-restore, retention holds, key-destruction evidence and Receipts limited to verified locations.

## Rejected alternatives

- append-only history overrides deletion duties;
- tombstone equals physical deletion;
- provider acknowledgement equals global proof;
- one shared destruction key without scope isolation;
- hiding partial failures.

## Consequences

Profiles must declare unknown and residual locations. Runtime security/privacy review is still required before sensitive data or live ecosystem integration.
