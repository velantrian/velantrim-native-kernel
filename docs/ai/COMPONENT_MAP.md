# 🗺️ Native Kernel Document, Contract and Authority Map

Use exact SHAs, statuses and evidence. Code presence is not complete profile conformance.

## Primary orientation surfaces

| Surface | Role | Authority / caution |
|---|---|---|
| `README.md` / `README.ru.md` | Public overview and maturity | Must state `P1 PARTIAL`, not full Kernel |
| `STATUS.md` | Authoritative current implementation/evidence boundary | Verify exact branch/main SHA |
| `ARCHITECTURE.md` | Canon shape and invariants | Architecture, not runtime proof |
| `docs/contracts/NORMATIVE_CONTRACTS_V1*` | Accepted identity/event/deletion/fixture contracts | Full profile support not established |
| `contracts/*.json` | Registry, schemas and fixtures | Machine-readable contract surface |
| `docs/rfc/0002-*` | Accepted clean PostgreSQL profile plan | Only P1 authorized |
| `docs/adr/0015-*` | Operator decision accepting lineage and P1 | Approval, not C1/C2 evidence |
| `profiles/postgresql-reference-v0/profile-manifest.json` | Historical P0 proposal snapshot | Intentionally remains proposed/pending |
| `profiles/postgresql-reference-v0/p1-manifest.json` | Current P1 implementation/evidence record | Runtime conformance remains `UNSUPPORTED` |
| `native_kernel/semantic_core/` | Bounded P1 implementation | No durable storage or profile adapter |
| `tools/profiles/validate_p1_manifest.py` | P1 anti-overclaim guard | Rejects C1/recovery/dependency drift |
| `.github/workflows/p1-semantic-core.yml` | P1 repository check definition | Declared workflow is not an executed result |
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
separate P2 operator GO
        ↓
future PostgreSQL durable adapter
        ↓
P3 replay/projections/Receipts
        ↓
P4 conformance adapter and exact evidence
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

P1 implements selected code paths across accepted families but does not claim complete support for any family through the evidence-report protocol.

## P1 evidence route

Read in order:

1. Issue #43;
2. ADR-0015;
3. RFC-0002;
4. `native_kernel/semantic_core/README.md`;
5. source modules;
6. `tests/test_semantic_core.py`;
7. `p1-manifest.json`;
8. P1 manifest validator/tests;
9. P1 workflow and exact run evidence.

Recorded local evidence:

```text
20 semantic-core tests PASS
4 P1-manifest tests PASS
compileall PASS
```

Required interpretation:

```text
local P1 PASS
≠ durable history
≠ PostgreSQL adapter
≠ assertion-level conformance
≠ C1/C2/C3
```

## Source recovery route

Start with `STATUS.md`, Issue #1, import specs, `docs/source-recovery/`, `tools/source_recovery/` and its isolated workflow.

```text
P1 clean implementation
≠ controlled v0.1.2.1 import
≠ recovered original tests
```

## Conformance route

For fixture integrity use ADR-0014, registry/schema/fixture packs, `tools/conformance/runner.py` and `tests/test_conformance_runner.py`.

For future profile conformance, P4 must emit all 72 assertion results exactly once. Until then, runtime support remains `UNSUPPORTED`.

## Storage route

ADR-0009 accepts PostgreSQL as preferred full profile direction and SQLite as optional. No storage adapter currently exists. P2 requires separate operator GO.

## World and epistemic boundary

Preserve:

```text
representation ≠ represented reality
observation ≠ explanation
unknown ≠ false
retrieval/model output ≠ admitted knowledge
```

ADR-0008 and `NK-EPI-001…008` remain proposed and are not implemented by P1.

## Ecosystem boundary

- Native Kernel — semantic memory/event/replay contracts and bounded profiles;
- Titan — cognition, retrieval, tools and orchestration;
- Mentaury Soul — digital individuality and continuity;
- Crystal — verifiable memory, evidence and audit.

No P1 component authorizes shared runtime, storage, identity or authority.

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
| Identity | ADR-0011 → canonical.py → identity fixtures/tests |
| Authority | NK-AUT contracts → authority.py → Receipt tests |
| Reducer | ADR-0012 → reducer.py → sequence/version tests |
| Deletion | ADR-0013 → deletion.py → fixture/Receipt tests |
| Future PostgreSQL P2 | accepted RFC + new operator GO + separate issue/PR |
| Conformance | ADR-0014 → registry/runner → future P4 adapter |
| Source candidate | Issue #1 import spec and provenance tooling |
| Cross-project work | ecosystem/integration boundaries plus target-project governance |
