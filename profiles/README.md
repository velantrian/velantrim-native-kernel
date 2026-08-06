# Native Kernel Implementation Profiles

This directory contains machine-readable planning and evidence surfaces for replaceable implementation profiles.

```text
profile manifest
≠ Architecture Canon
≠ accepted runtime implementation
≠ conformance evidence
```

## Current profile plans

| Profile | Status | Runtime | Evidence |
|---|---|---|---|
| [`postgresql-reference-v0`](./postgresql-reference-v0/profile-manifest.json) | `PROPOSED / OPERATOR_APPROVAL_PENDING` | `NOT_STARTED` | `DOCUMENTED` |

## PostgreSQL reference profile

The proposed profile:

- uses ID `native-kernel/postgresql-reference`;
- uses clean evidence lineage `clean/postgresql-reference/0.1`;
- maps all 72 registry assertions without claiming runtime support;
- plans one authoritative writer;
- keeps SQL schema and generated IDs as profile details;
- separates semantic core, authority port, append adapter, reducer, projections, Receipts and conformance adapter;
- keeps `NK-EPI` deferred while ADR-0008 remains proposed;
- remains independent from Issue #1 and the historical `v0.1.2.1` claim.

Read:

- [`../docs/rfc/0002-postgresql-reference-profile-v0.md`](../docs/rfc/0002-postgresql-reference-profile-v0.md)
- [`../docs/rfc/0002-postgresql-reference-profile-v0.ru.md`](../docs/rfc/0002-postgresql-reference-profile-v0.ru.md)
- [Issue #40](https://github.com/velantrian/velantrim-native-kernel/issues/40)

## Status vocabulary

Planning manifests may use terms such as `PLANNED`, `DEFERRED_PROPOSED_FAMILY` and `REQUIRES_SEPARATE_GO`. These are not runtime conformance results.

A runtime evidence report must use the accepted evidence-report schema and include explicit support status for every registered assertion.

## Promotion boundary

```text
PROPOSED manifest
→ operator accepts planning contract
→ separate runtime GO
→ implementation PRs
→ C1 local evidence
→ C2 repository reproduction
→ independent second profile
→ possible C3
```

No profile may claim recovery, production readiness, storage neutrality or ecosystem integration through a manifest alone.
