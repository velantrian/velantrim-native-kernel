# 🗺️ Native Kernel Document, Contract and Authority Map

Use exact SHAs, statuses and evidence. Code presence is not complete profile conformance.

## Primary orientation surfaces

| Surface | Role | Authority / caution |
|---|---|---|
| `README.md` / `README.ru.md` | Public overview and maturity | Must state `P3 PARTIAL`, not full Kernel |
| `STATUS.md` | Authoritative current implementation/evidence boundary | Verify exact branch/main SHA |
| `ARCHITECTURE.md` | Canon shape and invariants | Architecture, not runtime proof |
| `docs/contracts/NORMATIVE_CONTRACTS_V1*` | Accepted identity/event/deletion/fixture contracts | Full profile support not established |
| `contracts/*.json` | Registry, schemas and fixtures | 72 assertion IDs; P4 absent |
| `docs/rfc/0002-*` | Accepted clean PostgreSQL profile | P1–P3 implementation contract |
| `docs/adr/0015-*` | Clean lineage and P1 authorization | Approval, not conformance |
| `docs/adr/0016-*` | P2 append/idempotency decision | Bounded P2 evidence only |
| `docs/adr/0017-*` | P3 replay/projection/Receipt decision | Bounded P3 evidence only |
| `profiles/postgresql-reference-v0/profile-manifest.json` | Historical P0 proposal snapshot | Intentionally historical |
| `profiles/postgresql-reference-v0/p1-manifest.json` | P1 implementation/evidence record | Runtime conformance `UNSUPPORTED` |
| `profiles/postgresql-reference-v0/p2-manifest.json` | P2 append integration record | P3/P4/C-levels not inferred |
| `profiles/postgresql-reference-v0/p3-manifest.json` | P3 replay/projection/Receipt record | P4/P5/C-levels not inferred |
| `native_kernel/semantic_core/` | P1 semantics + P3 standard-library helpers | No durable profile by itself |
| `native_kernel/postgresql_profile/` | Bounded P2/P3 PostgreSQL profile | No physical deletion/conformance/production claim |
| `tools/profiles/validate_p3_manifest.py` | P3 anti-overclaim guard | Rejects false promotion and missing Receipt limits |
| `.github/workflows/p3-replay-projections.yml` | P3 PostgreSQL/Python matrix + P2 regression | Only exact runs are evidence |
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
P2 PostgreSQL append/idempotency
        ↓
ADR-0017 + Issue #49
        ↓
P3 persisted replay + disposable projections + bounded Receipts
        ↓
separate P4 operator GO
        ↓
assertion-scoped conformance adapter
        ↓
separate P5 operator GO and independent second profile before C3
```

## P1/P3 semantic-helper ownership

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
├── state_codec.py
│   └── canonical SemanticState reconstruction and form check
│
├── upcasting.py
│   ├── explicit one-successor UpcastStep registry
│   ├── missing/duplicate/cycle rejection
│   └── deterministic target-schema routing
│
├── deletion.py / receipt.py
│   └── semantic transitions and bounded P1 Receipts
│
└── errors.py
    └── explicit contract/authority/version/sequence failures
```

The upcaster registry and state codec are standard-library helpers. Their Python structure is not Architecture Canon.

## P2 authoritative append ownership

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
└── sql/0001_p2_authoritative_history.sql
    ├── kernel_instances / writer_leases
    ├── stream_counters / events
    └── idempotency_records
```

## P3 replay/projection ownership

```text
native_kernel.postgresql_profile
│
├── history.py
│   ├── repeatable-read read-only snapshot
│   ├── instance-head/Event-count consistency
│   ├── P2 stored-event verification
│   ├── GENESIS → nke1 chain verification
│   ├── UpcasterRegistry routing
│   └── P1 reduction from empty
│
├── replay.py
│   ├── PostgreSQLReplayProjector
│   ├── Replay Receipt publication
│   ├── projection read/destroy/rebuild
│   ├── locked head comparison
│   └── atomic Receipt + projection publication
│
├── replay_models.py
│   ├── ReplaySnapshot
│   ├── OperationalReceipt
│   ├── StoredProjection
│   └── Replay/ProjectionRebuild results
│
├── receipt_store.py
│   ├── mandatory proof limitations
│   ├── canonical Receipt bytes
│   ├── provisional nkr0 profile commitment
│   └── Receipt reload/corruption checks
│
└── sql/0002_p3_replay_projection_receipts.sql
    ├── operation_receipts
    └── projections
```

SQL tables, indexes, generation allocation and locking are PostgreSQL profile details, not Canon.

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

P1–P3 implement selected paths across accepted families but do not claim complete assertion-level support through the evidence-report protocol.

## P3 evidence route

Read in order:

1. Issue #49;
2. ADR-0017;
3. RFC-0002;
4. `native_kernel/postgresql_profile/README.md`;
5. `upcasting.py`, `state_codec.py`, `history.py`, `replay.py`, `receipt_store.py`, `replay_models.py`;
6. migration `0002_p3_replay_projection_receipts.sql`;
7. `tests/test_p3_semantic.py`;
8. `tests/test_p3_postgresql_integration.py`;
9. `p3-manifest.json`, validator and tests;
10. `.github/workflows/p3-replay-projections.yml`;
11. exact run/jobs/logs for the final PR head.

Initial executable-head evidence:

```text
head 0f8fd4ffe5d5fb0d4bc01f3e441a053f691dbba3
P3 run 31171581859 — PASS
PostgreSQL 16/18 × Python 3.11/3.12 — PASS
P2 regression run 31171581795 — PASS
P1 run 31171581787 — PASS
fixture run 31171581791 — PASS
```

Required interpretation:

```text
P3 integration PASS
≠ complete Kernel runtime
≠ truth or external authenticity
≠ physical deletion
≠ assertion-level conformance
≠ C1/C2/C3
≠ production guarantee
```

## Source recovery route

Start with `STATUS.md`, Issue #1, import specs, `docs/source-recovery/`, `tools/source_recovery/` and its isolated workflow.

```text
clean P1/P2/P3 implementation
≠ controlled v0.1.2.1 import
≠ recovered original tests
```

## Conformance route

For fixture integrity use ADR-0014, registry/schema/fixture packs, `tools/conformance/runner.py` and `tests/test_conformance_runner.py`.

P4 must emit all 72 assertion results exactly once. Until then runtime support remains `UNSUPPORTED`.

## Storage, replay and Receipt route

```text
P2 events = authoritative recorded history for this profile
P3 projection = disposable read model
P3 Receipt = bounded evidence about one declared operation
```

Neither PostgreSQL persistence nor a Receipt establishes truth. P3 checks do not constitute signatures, complete Event Integrity or physical erasure evidence.

## World and epistemic boundary

Preserve:

```text
representation ≠ represented reality
observation ≠ explanation
unknown ≠ false
retrieval/model output ≠ admitted knowledge
storage presence ≠ truth or authority
Receipt evidence ≠ unlimited proof
```

ADR-0008 and `NK-EPI-001…008` remain proposed and are not promoted by P3.

## Ecosystem boundary

- Native Kernel — semantic memory/Event/replay/evidence contracts and bounded profiles;
- Titan — cognition, retrieval, tools and orchestration;
- Mentaury Soul — digital individuality and continuity;
- Crystal — verifiable memory, evidence and audit.

No P1/P2/P3 component authorizes shared runtime, storage, identity or authority.

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
| P2 audit | Issue #46 → ADR-0016 → SQL/source → tests → manifest → exact matrix |
| P3 audit | Issue #49 → ADR-0017 → replay source/migration → tests → manifest → exact matrix |
| Identity | ADR-0011 → canonical.py → identity fixtures/tests |
| Authority | NK-AUT contracts → authority.py → append authority call → Receipt tests |
| Append/idempotency | ADR-0012 → adapter.py → SQL 0001 → P2 integration tests |
| Replay/upcasting | ADR-0012/0017 → history.py/upcasting.py → P3 tests |
| Projection rebuild | ADR-0017 → replay.py → SQL 0002 → stale/fault tests |
| Operational Receipt | ADR-0017 → replay_models.py/receipt_store.py → corruption/overclaim tests |
| Deletion | ADR-0013 → deletion.py → fixture/Receipt tests; physical execution absent |
| P4 conformance | separate GO → ADR-0014 → registry/runner → future adapter |
| Source candidate | Issue #1 import spec and provenance tooling |
| Cross-project work | ecosystem/integration boundaries plus target-project governance |
