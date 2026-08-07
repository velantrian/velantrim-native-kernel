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
| `docs/rfc/0002-*` | Accepted PostgreSQL profile | Current phase P2 partial |
| `docs/adr/0015-*` | Clean lineage and P1 authorization | Accepted decision |
| `docs/adr/0016-*` | P2 technology/transaction decision | Unit evidence only until integration runs |
| `profiles/postgresql-reference-v0/profile-manifest.json` | Historical P0 snapshot | Do not rewrite as current evidence |
| `profiles/postgresql-reference-v0/p1-manifest.json` | P1 record | P1 evidence boundary |
| `profiles/postgresql-reference-v0/p2-manifest.json` | P2 record | Conformance remains `UNSUPPORTED` |

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
| `tests/test_postgresql_profile_unit.py` | P2 hashes, migrations and object boundaries | real PostgreSQL behavior |
| `tests/test_postgresql_profile_integration.py` | migration, lease, append, rollback, concurrency | production guarantees or conformance |
| `tests/test_p2_manifest.py` | anti-overclaim invariants | adapter behavior |
| `tools/profiles/validate_p2_manifest.py` | machine-readable status discipline | C1/C2/C3 |
| `.github/workflows/p2-postgresql.yml` | declared PG16/18 × Python3.11/3.12 matrix | no evidence until a run exists |

## Authority boundaries

- Architecture Canon owns semantic invariants.
- Commands require explicit authority before append.
- PostgreSQL owns persistence only for this profile; storage presence is not authority or truth.
- `writer_epoch` fences the one authoritative writer; it is not consensus.
- Event hash chain is an integrity signal, not authentication.
- P3 owns future replay/projections/operational Receipts.
- P4 owns assertion-scoped conformance.
- Titan, Mentaury and Crystal remain independent projects.

## Current gates

```text
P1: MERGED
P2: AUTHORIZED / ACTIVE BRANCH / UNIT-TESTED
PostgreSQL integration: NOT_ESTABLISHED
P3–P5: NOT AUTHORIZED
72 assertion results: UNSUPPORTED
C1/C2/C3: NOT_ESTABLISHED
Issue #1 and Issue #18: INDEPENDENT
```
