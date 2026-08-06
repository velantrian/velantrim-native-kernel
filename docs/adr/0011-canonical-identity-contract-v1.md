# ADR-0011: Canonical identity contract v1

- **Decision status:** `ACCEPTED`
- **Evidence level:** `LOCALLY_TESTED` for reference vectors only
- **Implementation status:** `PARTIAL` support tooling; Kernel runtime `NOT_STARTED`
- **Operator approval:** `APPROVED`
- **Date:** `2026-08-06`
- **Deciders:** `@velantrian`
- **Track:** `Abstract Contract / NK-ID`
- **Related:** Issue #14, ADR-0010

## Context

Accepted family `NK-ID` requires deterministic identity, but exact bytes, Unicode, numeric, null, hash-domain, collision and migration rules were undefined.

## Decision

Adopt `nk-id/1.0` as a strict UTF-8 canonical JSON subset using pre-normalized NFC strings, sorted keys, compact encoding, integers/booleans, canonical decimal strings, omitted optional fields instead of null, UTC-second timestamps, SHA-256 domain separation and distinct `nkh1`, `nkc1`, `nkl1` identifiers.

The operator approved this architectural contract on 2026-08-06 after the proposal, fixture pack, limitations and remaining evidence gates were presented. Approval accepts the contract meaning; it does not promote local fixture evidence to repository reproduction and does not claim a Kernel runtime.

## Rejected alternatives

- backend row IDs: not portable;
- unspecified JSON serialization: non-deterministic across libraries;
- binary floats: ambiguous textual/cross-language identity;
- one identifier for content, assertion and lineage: collapses semantic roles;
- silent collision merge: corrupts identity.

## Consequences

Golden and invalid vectors become the accepted executable review surface for this contract. Exact runtime adoption and cross-language C3 evidence remain future work. A new algorithm requires a new prefix/domain and inspectable aliases.

## Evidence and promotion gates

- operator decision: `APPROVED`;
- reference vectors and canonicalizer: `LOCALLY_TESTED`;
- repository workflow result: not yet recorded;
- Kernel implementation: absent;
- at least one materially independent reader is required before C3;
- no claim may be made that historical `v0.1.2.1` used this contract.
