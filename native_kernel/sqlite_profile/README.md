# SQLite Embedded Profile — P5

`native_kernel.sqlite_profile` is a materially different storage profile for the accepted Native Kernel contracts.

```text
Profile ID:       native-kernel/sqlite-embedded
Profile version:  0.5-p5
Evidence lineage: clean/sqlite-embedded/0.1
Role:             embedded / portable / single-file profile
```

## Implemented boundary

- Python standard-library `sqlite3` only;
- numbered migration ledger with digest drift detection;
- explicit Kernel-instance registration;
- `BEGIN IMMEDIATE` single-writer transaction envelope;
- writer owner/epoch/expiry fencing;
- contiguous global and per-stream ordering;
- append, same-command retry and conflicting-key rejection;
- canonical payload/Event commitments and hash-chain verification;
- exact authoritative-history import preserving Event bytes and hashes;
- persisted replay, disposable projection rebuild and bounded operational Receipts;
- assertion-complete C1/C2 profile report;
- assertion-scoped C3 comparison against the PostgreSQL reference profile.

## Independence boundary

The SQLite implementation does not call the PostgreSQL append, replay, projection or receipt adapters. It shares only accepted semantic contracts and profile-neutral test/registry utilities.

```text
same contracts
≠ same SQL
≠ same tables
≠ same locks
≠ same operational capabilities
```

## C3 meaning

C3 compares declared equivalence classes:

- byte equivalence for `nk-id/1.0` and exact imported Event history;
- structural equivalence for report/contract shape;
- semantic equivalence for reducer/projection state and Receipt boundaries;
- behavioural equivalence for accepted/rejected commands and ordering.

Allowed differences include SQL dialect, table/index layout, server versus file topology, independent Event IDs/timestamps during separate append, and operational concurrency/IAM/network capabilities.

C3 does not establish production readiness, truth, external authenticity, physical deletion, C4/C5, or operational equivalence with PostgreSQL.
