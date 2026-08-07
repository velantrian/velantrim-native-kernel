# 🗺️ Native Kernel Document, Contract and Authority Map

Use exact SHAs, statuses and evidence. Code presence is not complete profile conformance.

## Primary orientation surfaces

| Surface | Role | Authority / caution |
|---|---|---|
| `README.md` / `README.ru.md` | Public overview and maturity | Must state `P2 PARTIAL`, not full Kernel |
| `STATUS.md` | Authoritative current implementation/evidence boundary | Verify exact branch/main SHA |
| `ARCHITECTURE.md` | Canon shape and invariants | Architecture, not runtime proof |
| `docs/contracts/NORMATIVE_CONTRACTS_V1*` | Accepted identity/event/deletion/fixture contracts | Full profile support not established |
| `contracts/*.json` | Registry, schemas and fixtures | 72 assertion IDs; P4 absent |
| `docs/rfc/0002-*` | Accepted clean PostgreSQL profile | P2 integration repository-reproduced |
| `docs/adr/0015-*` | Clean lineage and P1 authorization | Approval, not conformance |
| `docs/adr/0016-*` | P2 profile/transaction decision | Bounded P2 evidence only |
| `profiles/postgresql-reference-v0/profile-manifest.json` | Historical P0 proposal snapshot | Intentionally historical |
| `profiles/postgresql-reference-v0/p1-manifest.json` | P1 implementation/evidence record | Runtime conformance `UNSUPPORTED` |
| `profiles/postgresql-reference-v0/p2-manifest.json` | P2 integration evidence record | P3/P4/C1 absent |
| `native_kernel/semantic_core/` | Bounded P1 implementation | No durable profile by itself |
| `native_kernel/postgresql_profile/` | Bounded P2 PostgreSQL implementation | No replay/projections/conformance |
| `tools/profiles/validate_p2_manifest.py` | P2 anti-overclaim guard | Rejects false promotion |
| `.github/workflows/p2-postgresql.yml` | PostgreSQL/Python matrix | Only exact runs are evidence |
| `docs/ai/*` | Current state, risks, routes and work log | Orientation plus exact evidence references |

## Architecture-to-runtime route

```text
ARCHITECTURE.md
        ↓
accepted family and exact contracts
        ↓
RFC-0002 + ADR-0015
        ↓
P1 profile-independent semantic core
        ↓
ADR-0016 + Issue #46
        ↓
P2 PostgreSQL append/idempotency profile
        ↓
separate P3 operator GO
        ↓
future replay/projections/operational Receipts
        ↓
P4 conformance adapter and exact assertion evidence
        ↓
independent second profile before C3
```

## P1 component ownership

```text
native_kernel.semantic_core
│
├── canonical.py
│   ├── canonical JSON subset
│   ├── nkh1 / nkc1 / nkl1
│   └── provisional nkd0 / nks0
│
├── models.py
│   ├── SemanticContent
│   ├── ClaimIdentity / LineageSeed
│   ├── Command
│   └── logical SemanticEvent
│
├── authority.py
│   └── explicit deny-by-default local policy
│
├── reducer.py
│   ├── version-bound deterministic reduction
│   ├── global/stream sequence checks
│   └── immutable sorted SemanticState
│
├── deletion.py
│   ├── accepted transition graph
│   └── DeletionReceipt proof limits
│
├── receipt.py
│   └── AdmissionReceipt proof limits
│
└── errors.py
    └── explicit contract/authority/version/sequence failures
```

## P2 component ownership

```text
native_kernel.postgresql_profile
│
├── adapter.py
│   ├── instance registration
│   ├── writer owner/epoch/expiry fencing
│   ├── atomic append + idempotency
│   ├── rollback-safe global/stream ordering
│   └── stored-event consistency checks
│
├── hashing.py
│   ├── canonical Event envelope
│   ├── nkp1 payload commitment
│   └── nke1 global hash chain
│
├── migrations.py
│   ├── numbered SQL discovery
│   ├── SHA-256 ledger
│   └── advisory-lock serialization
│
├── models.py
│   ├── WriterToken
│   ├── StoredEvent
│   └── AppendResult
│
├── errors.py
│   └── explicit lease/idempotency/migration/corruption failures
│
└── sql/0001_p2_authoritative_history.sql
    ├── kernel_instances
    ├── writer_leases
    ├── stream_counters
    ├── events
    └── idempotency_records
```

SQL tables and indexes are profile details, not Canon.

## Stable contract families

```text
NK-SEM — semantic roles
NK-ID  — identity and canonical encoding
NK-EVT — event, observation and recorded change
NK-AUT — authority and admission
NK-CFL — conflict and explicit unknowns
NK-EQV — conformance and semantic equivalence
NK-EPI — proposed epistemic fixture family
```

P1/P2 implement selected code paths across accepted families but do not claim complete assertion-level support through the evidence-report protocol.

## P1 evidence route

Read in order:

1. Issue #43;
2. ADR-0015;
3. RFC-0002;
4. `native_kernel/semantic_core/README.md`;
5. source modules;
6. `tests/test_semantic_core.py`;
7. `p1-manifest.json`;
8. P1 validator/tests;
9. exact P1 workflow evidence.

## P2 evidence route

Read in order:

1. Issue #46;
2. ADR-0016;
3. RFC-0002;
4. `native_kernel/postgresql_profile/README.md`;
5. SQL migration and source modules;
6. unit/integration tests;
7. `p2-manifest.json` and validator;
8. `.github/workflows/p2-postgresql.yml`;
9. exact run/jobs/logs for the PR head.

Recorded repository evidence:

```text
P2 run 31151297646 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
AI context run 31151298002 — PASS
```

Required interpretation:

```text
P2 integration PASS
≠ replay/projection runtime
≠ assertion-level conformance
≠ C1/C2/C3
≠ production guarantee
```

## Source recovery route

Start with `STATUS.md`, Issue #1, import specs, `docs/source-recovery/`, `tools/source_recovery/` and its isolated workflow.

```text
clean P1/P2 implementation
≠ controlled v0.1.2.1 import
≠ recovered original tests
```

## Conformance route

For fixture integrity use ADR-0014, registry/schema/fixture packs, `tools/conformance/runner.py` and `tests/test_conformance_runner.py`.

P4 must emit all 72 assertion results exactly once. Until then runtime support remains `UNSUPPORTED`.

## Storage route

ADR-0009 accepts PostgreSQL as preferred full profile and SQLite as optional. P2 now implements the bounded PostgreSQL append/idempotency route.

```text
PostgreSQL profile owns persistence mechanics
≠ PostgreSQL defines semantic architecture
```

Replay reads, upcasters, projections and operational Receipts remain P3.

## World and epistemic boundary

Preserve:

```text
representation ≠ represented reality
observation ≠ explanation
unknown ≠ false
retrieval/model output ≠ admitted knowledge
storage presence ≠ truth or authority
```

ADR-0008 and `NK-EPI-001…008` remain proposed and are not implemented by P2.

## Ecosystem boundary

- Native Kernel — semantic memory/event/replay contracts and bounded profiles;
- Titan — cognition, retrieval, tools and orchestration;
- Mentaury Soul — digital individuality and continuity;
- Crystal — verifiable memory, evidence and audit.

No P1/P2 component authorizes shared runtime, storage, identity or authority.

## Decision ownership

- architecture/contract acceptance — operator through ADR process;
- phase authorization — separate explicit operator GO;
- implementation evidence — exact code/tests/CI at a named SHA;
- source authenticity — Issue #1 provenance gate;
- C3 — two materially independent profiles and declared equivalence;
- Notion — rationale/history, never overriding GitHub behavior/evidence.

## Task routes

| Task | Minimum route |
|---|---|
| P1 audit | Issue #43 → ADR-0015 → source → tests → manifest → workflow |
| P2 audit | Issue #46 → ADR-0016 → SQL/source → unit/integration tests → manifest → exact matrix run |
| Identity | ADR-0011 → canonical.py → identity fixtures/tests |
| Authority | NK-AUT contracts → authority.py → adapter authority call → Receipt tests |
| Append/idempotency | ADR-0012 → adapter.py → SQL → integration tests |
| Writer fencing | ADR-0016 → writer lease schema → adapter → lease tests |
| Reducer | ADR-0012 → reducer.py → sequence/version tests |
| Deletion | ADR-0013 → deletion.py → fixture/Receipt tests |
| Future P3 | separate operator GO + new issue/PR |
| Conformance | ADR-0014 → registry/runner → future P4 adapter |
| Source candidate | Issue #1 import spec and provenance tooling |
| Cross-project work | ecosystem/integration boundaries plus target-project governance |
