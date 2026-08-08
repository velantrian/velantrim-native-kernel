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
- fail-closed linked SQLite `>= 3.51.3` requirement before WAL is opened;
- exact Event Envelope field-set and stored-column verification;
- numbered migration ledger with digest drift detection;
- statement-by-statement atomic migration execution;
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

## WAL safety prerequisite

The profile does not start on a linked SQLite older than 3.51.3. Historical repository evidence used SQLite 3.45.1 and remains preserved with that explicit limitation; it is not the current runtime minimum.

For reproducible Linux validation:

```bash
tools/sqlite/build_safe_sqlite.sh /tmp/native-kernel-sqlite-3.51.3 /usr/bin/python3
LD_LIBRARY_PATH=/tmp/native-kernel-sqlite-3.51.3/lib \
  /usr/bin/python3 -m unittest tests.test_sqlite_profile_unit -v
```

Known fixed backports are not accepted by a loose numeric comparison. Adding one requires an explicit allowlist and separate evidence.

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

The bounded comparison map is `45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED`; repository C3 is not established until the exact matrix and retained comparison artifacts pass.

Allowed differences include SQL dialect, table/index layout, server versus file topology, independent Event IDs/timestamps during separate append, and operational concurrency/IAM/network capabilities.

C3 does not establish support for all 72 assertions, production readiness, truth, external authenticity, physical deletion, C4/C5, or operational equivalence with PostgreSQL.
