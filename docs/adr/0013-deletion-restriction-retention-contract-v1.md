# ADR-0013: Deletion, restriction and retention contract v1

- **Decision status:** `ACCEPTED`
- **Evidence level:** `LOCALLY_TESTED` state-machine fixtures only
- **Implementation status:** `PARTIAL` support tooling; Kernel runtime `NOT_STARTED`
- **Operator approval:** `APPROVED`
- **Date:** `2026-08-06`
- **Deciders:** `@velantrian`
- **Track:** `Abstract Contract / NK-AUT`
- **Related:** Issue #16, ADR-0010

## Context

`ERASED` records a logical transition but cannot by itself prove deletion from payloads, projections, indexes, exports, providers, backups or logs.

## Decision

Adopt `nk-deletion/1.0` and separate restriction, logical erase, physical deletion and cryptographic erasure. Require data-location inventory, authority/policy, idempotent retries, visible partial completion, quarantine-before-restore, retention holds, key-destruction evidence and Receipts limited to verified locations.

The operator approved this architectural contract on 2026-08-06. Approval establishes the required semantic distinctions and proof limits; it does not assert legal compliance, provider deletion, physical media erasure or an implemented runtime mechanism.

## Rejected alternatives

- append-only history overrides deletion duties;
- tombstone equals physical deletion;
- provider acknowledgement equals global proof;
- one shared destruction key without scope isolation;
- hiding partial failures.

## Consequences

Profiles must declare unknown and residual locations. Runtime security/privacy review is still required before sensitive data or live ecosystem integration.

## Evidence and promotion gates

- operator decision: `APPROVED`;
- state-machine and Receipt-limit fixtures: `LOCALLY_TESTED`;
- repository workflow result: not yet recorded;
- deletion/key-management implementation: absent;
- legal, security, backup and provider evidence: absent;
- no Receipt may exceed verified locations or hide pending residual data.
