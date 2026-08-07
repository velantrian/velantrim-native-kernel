# Velantrim Native Kernel

> **Maturity:** `RESEARCH / P2 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`

Velantrim Native Kernel is a technology-neutral architecture for preserving semantic identity, recorded change, authority, conflict, replayability and evidence across replaceable storage and compute profiles.

```text
Architecture Canon
→ accepted abstract contracts
→ replaceable implementation profiles
→ exact tests and evidence
```

PostgreSQL, SQLite, Python, LLMs, embeddings, graph systems, CPUs, GPUs and future substrates are instruments. None defines the permanent semantic architecture.

## Current implementation

```text
Profile ID:       native-kernel/postgresql-reference
Evidence lineage: clean/postgresql-reference/0.1
Version:          0.2-p2
```

### P1 — profile-independent semantic core

`native_kernel.semantic_core` provides canonical identity, immutable semantic objects, explicit authority, deterministic logical reduction, deletion/restriction semantics and bounded Receipts.

### P2 — PostgreSQL authoritative append/idempotency

`native_kernel.postgresql_profile` provides:

```text
explicit authority
→ DB-backed writer owner/epoch fence
→ scoped durable idempotency
→ rollback-safe global and stream counters
→ atomic Event + idempotency commit
→ canonical payload/envelope bytes
→ nkp1 / nke1 integrity chain
```

Profile choices:

- PostgreSQL `16–18`;
- Psycopg `>=3.3,<3.4`, loaded lazily;
- Python `>=3.11,<3.13`;
- numbered SQL migrations with SHA-256 ledger;
- one authoritative writer lease per Kernel instance.

These are implementation details, not Canon.

## Repository evidence

PR #47 head `e80492bcacde2ff2be3a2ee03aa5aa53a714d288` produced:

```text
P2 workflow run 31151297646 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
AI context integrity run 31151298002 — PASS
P1 semantic core — PASS
Conformance fixture integrity — PASS
```

Each P2 matrix job passed:

- 9 P2 unit tests;
- 5 PostgreSQL integration tests;
- 5 P2 manifest tests;
- manifest validation and compileall.

Therefore the bounded P2 PostgreSQL behaviors are repository-reproduced in the declared matrix.

```text
P2 PostgreSQL integration PASS
≠ replay/projection runtime
≠ assertion-level conformance
≠ C1/C2/C3
≠ production durability/security/privacy guarantee
```

All 72 registry assertions remain runtime `UNSUPPORTED` until P4 emits a complete assertion-scoped report.

## Contracts

Accepted exact contracts:

- `nk-id/1.0` — canonical identity;
- `nk-event/1.0` — single-writer append, idempotency, order and replay boundary;
- `nk-deletion/1.0` — restriction/deletion/retention meaning;
- `nk-fixtures/1.0` — executable evidence protocol.

Start with:

- [`STATUS.md`](STATUS.md)
- [`ARCHITECTURE.md`](ARCHITECTURE.md)
- [`docs/contracts/NORMATIVE_CONTRACTS_V1.md`](docs/contracts/NORMATIVE_CONTRACTS_V1.md)
- [`docs/rfc/0002-postgresql-reference-profile-v0.md`](docs/rfc/0002-postgresql-reference-profile-v0.md)
- [`docs/adr/0016-authorize-p2-postgresql-append-profile.md`](docs/adr/0016-authorize-p2-postgresql-append-profile.md)
- [`native_kernel/postgresql_profile/README.md`](native_kernel/postgresql_profile/README.md)

## Validation

```bash
python -m unittest discover -s tests -p 'test_semantic_core.py' -v
python -m unittest discover -s tests -p 'test_postgresql_profile_unit.py' -v
python -m unittest discover -s tests -p 'test_p2_manifest.py' -v
python tools/profiles/validate_p2_manifest.py

python -m pip install -r profiles/postgresql-reference-v0/requirements-p2-ci.txt
NK_TEST_POSTGRES_DSN='postgresql://...' \
  python -m unittest discover -s tests -p 'test_postgresql_profile_integration.py' -v
```

## Explicitly absent

- P3 projection persistence/rebuild and replay/upcasters;
- operational replay/deletion Receipts;
- physical or cryptographic deletion execution;
- network API;
- P4 conformance adapter;
- P5 SQLite independent profile;
- C1/C2/C3;
- packaging/publication decision under Issue #18;
- Titan, Mentaury or Crystal runtime wiring;
- recovery of historical `v0.1.2.1` or its original 44 tests.

## Source-recovery boundary

```text
clean/postgresql-reference/0.1
≠ recovered v0.1.2.1
≠ original 44-test evidence
```

Issue #1 remains independent. `NOT_FOUND_IN_ACCESSIBLE_SOURCES` does not mean `GLOBALLY_LOST`.
