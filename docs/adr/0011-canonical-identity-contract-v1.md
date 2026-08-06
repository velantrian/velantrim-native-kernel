# ADR-0011: Canonical identity contract v1

- **Decision status:** `PROPOSED`
- **Evidence level:** `LOCALLY_TESTED` for reference vectors only
- **Implementation status:** `PARTIAL` support tooling; Kernel runtime `NOT_STARTED`
- **Operator approval:** `PENDING`
- **Date:** `2026-08-06`
- **Related:** Issue #14, ADR-0010

## Context

Accepted family `NK-ID` requires deterministic identity, but exact bytes, Unicode, numeric, null, hash-domain, collision and migration rules were undefined.

## Decision proposal

Adopt `nk-id/1` as a strict UTF-8 canonical JSON subset using pre-normalized NFC strings, sorted keys, compact encoding, integers/booleans, canonical decimal strings, omitted optional fields instead of null, UTC-second timestamps, SHA-256 domain separation and distinct `nkh1`, `nkc1`, `nkl1` identifiers.

## Rejected alternatives

- backend row IDs: not portable;
- unspecified JSON serialization: non-deterministic across libraries;
- binary floats: ambiguous textual/cross-language identity;
- one identifier for content, assertion and lineage: collapses semantic roles;
- silent collision merge: corrupts identity.

## Consequences

Golden and invalid vectors become executable. Exact runtime adoption and cross-language C3 evidence remain future work. A new algorithm requires a new prefix/domain and inspectable aliases.

## Acceptance criteria

Operator acceptance, clean CI, at least one additional materially independent reader before C3, and no claim that `v0.1.2.1` used this contract.
