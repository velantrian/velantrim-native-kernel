# 🗺️ Native Kernel Document, Contract and Authority Map

Use exact SHAs, status labels and evidence. Code presence is not complete profile conformance.

## Primary orientation surfaces

| Surface | Role | Authority / caution |
|---|---|---|
| `README.md` / `README.ru.md` | Public overview | Must state `P2 PARTIAL`, not full Kernel |
| `STATUS.md` | Authoritative maturity/evidence boundary | Verify exact branch/main SHA |
| `docs/ai/CURRENT_STATE.md` | Active task and gates | Check PR/workflow evidence |
| `ARCHITECTURE.md` | Canon shape and invariants | Architecture, not runtime proof |
| `docs/contracts/NORMATIVE_CONTRACTS_V1*` | Accepted contracts | Assertion-level runtime support absent |
| `contracts/*.json` | Registry, schemas and fixtures | 72 assertion IDs; P4 not implemented |
| `docs/rfc/0002-*` | Accepted PostgreSQL profile | P2 integration repository-reproduced |
| `docs/adr/0015-*` | Clean lineage and P1 authorization | Accepted decision |
| `docs/adr/0016-*` | P2 technology/transaction decision | P2 matrix evidence; P3 absent |
| `profiles/postgresql-reference-v0/profile-manifest.json` | Historical P0 snapshot | Do not rewrite as current evidence |
| `profiles/postgresql-reference-v0/p1-manifest.json` | P1 record | P1 evidence boundary |
| `profiles/postgresql-reference-v0/p2-manifest.json` | P2 record | Integration PASS; conformance `UNSUPPORTED` |

## Executable ownership

```text
native_kernel.semantic_core
├── canonical.py       # profile-independent canonical identity helpers
├── models.py          # semantic objects, Commands and logical Events
├── authority.py       # explicit local authority adapter
├── reducer.py         # deterministic logical reduction
├── deletion.py        # deletion/restriction semantics
└── receipt.py         # P1 proof limits

native_kernel.postgresql_profile
├── adapter.py         # P2 instance, lease and atomic append/idempotency
├── hashing.py         # nkp1/nke1 fixture-compatible commitments
├── migrations.py      # numbered SQL + checksum ledger
├── models.py          # WriterToken, StoredEvent and AppendResult
├── errors.py          # explicit profile failures
└── sql/               # PostgreSQL profile schema, not Canon
```

## Test/evidence ownership

| Surface | What it tests | What it does not establish |
|---|---|---|
| `tests/test_semantic_core.py` | P1 deterministic semantics | durable storage |
| `tests/test_postgresql_profile_unit.py` | P2 hashes, migrations and object boundaries | PostgreSQL behavior alone |
| `tests/test_postgresql_profile_integration.py` | migration, lease, append, rollback, concurrency | P3 replay, production operations or conformance |
| `tests/test_p2_manifest.py` | anti-overclaim invariants | adapter behavior |
| `tools/profiles/validate_p2_manifest.py` | machine-readable status discipline | C1/C2/C3 |
| `.github/workflows/p2-postgresql.yml` | PG16/18 × Python3.11/3.12 matrix | only exact successful runs are evidence |

## Repository evidence

```text
P2 run 31151297646: PASS
3.11/PG16: PASS
3.11/PG18: PASS
3.12/PG16: PASS
3.12/PG18: PASS
AI context run 31151298002: PASS
```

## Authority boundaries

- Architecture Canon owns semantic invariants.
- Commands require explicit authority before append.
- PostgreSQL owns persistence only for this profile; storage presence is not authority or truth.
- `writer_epoch` fences one authoritative writer; it is not consensus.
- Event hash chain is an integrity signal, not authentication.
- P3 owns future replay/projections/operational Receipts.
- P4 owns assertion-scoped conformance.
- Titan, Mentaury and Crystal remain independent.

## Current gates

```text
P1: MERGED
P2: PARTIAL / REPOSITORY-INTEGRATION-TESTED
P3–P5: NOT AUTHORIZED
72 assertion statuses: UNSUPPORTED
C1/C2/C3: NOT_ESTABLISHED
Issue #1 and Issue #18: INDEPENDENT
```
