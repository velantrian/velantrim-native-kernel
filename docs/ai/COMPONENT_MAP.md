# 🗺️ Native Kernel Document, Contract and Authority Map

Use exact SHAs, statuses and evidence. A C2 report with `support_state: PARTIAL` is not complete profile conformance.

## Primary orientation surfaces

| Surface | Role | Authority / caution |
|---|---|---|
| `README.md` / `README.ru.md` | Public purpose and maturity | Must state P4 partial assertion conformance |
| `STATUS.md` | Authoritative current implementation/evidence boundary | Verify exact branch/main SHA |
| `ARCHITECTURE.md` | Canon shape and invariants | Architecture, not runtime proof |
| `docs/contracts/NORMATIVE_CONTRACTS_V1*` | Accepted identity/event/deletion/fixture contracts | Registry support remains assertion-scoped |
| `contracts/registry.json` | Stable 72 assertion IDs and decision statuses | `NK-EPI` remains proposed |
| `contracts/evidence-report-v1.schema.json` | Evidence report protocol | Schema validity alone is not runtime evidence |
| `docs/rfc/0002-*` | Accepted clean PostgreSQL profile | P1–P4 implementation contract |
| `docs/adr/0015-*` | Clean lineage and P1 authorization | Approval, not conformance |
| `docs/adr/0016-*` | P2 append/idempotency decision | Bounded P2 evidence only |
| `docs/adr/0017-*` | P3 replay/projection/Receipt decision | Bounded P3 evidence only |
| `docs/adr/0018-*` | P4 assertion-scoped conformance decision | C2 applies only to supported assertions |
| `profiles/postgresql-reference-v0/p4-manifest.json` | P4 support/evidence summary | 41 supported, 13 partial, 18 unsupported |
| `docs/ai/P4_IMPLEMENTATION_RECORD.md` | Exact P4 implementation, runs, artifacts and limitations | Re-verify final PR head |
| `native_kernel/semantic_core/` | P1 semantics + P3 helpers | Standard-library profile code, not Canon |
| `native_kernel/postgresql_profile/` | P2/P3 runtime + P4 adapter | One PostgreSQL profile, not C3 |
| `tools/conformance/runner.py` | External adapter protocol and base report validation | Fixture/runtime boundary |
| `tools/conformance/postgresql_profile_adapter.py` | P4 adapter CLI | Emits report, no hidden skip |
| `tools/conformance/validate_p4_report.py` | Strict P4 traceability and anti-overclaim guard | Requires exact 72-result map |
| `tools/profiles/validate_p4_manifest.py` | P4 manifest guard | Rejects false C2/C3/P5/recovery promotion |
| `.github/workflows/p4-conformance.yml` | 4× C2 matrix + artifacts + regressions | Only exact completed runs are evidence |
| `docs/ai/*` | Current state, risks, routes and work log | Orientation plus evidence references |

## Architecture-to-evidence route

```text
Architecture Canon
        ↓
accepted exact contracts + registry 1.1.0
        ↓
RFC-0002 / clean PostgreSQL profile
        ↓
P1 semantic core
        ↓
P2 authoritative append/idempotency
        ↓
P3 persisted replay/projections/Receipts
        ↓
P4 assertion-scoped evidence adapter
        ↓
41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED
        ↓
separate P5 operator GO + independent profile before C3
```

## Semantic-core ownership

```text
native_kernel.semantic_core
│
├── canonical.py
│   ├── canonical JSON subset
│   ├── nkh1 / nkc1 / nkl1
│   └── provisional nkd0 / nks0
├── models.py
│   ├── SemanticContent / SemanticRole
│   ├── ClaimIdentity / LineageSeed
│   ├── Command
│   └── SemanticEvent
├── authority.py
│   └── explicit deny-by-default local policy
├── reducer.py
│   └── version-bound deterministic reduction
├── state_codec.py
│   └── canonical SemanticState reconstruction
├── upcasting.py
│   └── explicit deterministic schema paths
├── deletion.py / receipt.py
│   └── semantic transitions and bounded Receipts
└── errors.py
    └── explicit contract/authority/version/sequence failures
```

## PostgreSQL P2/P3 ownership

```text
native_kernel.postgresql_profile
│
├── adapter.py
│   ├── instance registration
│   ├── writer owner/epoch/expiry fencing
│   ├── atomic append + idempotency
│   └── rollback-safe global/stream ordering
├── hashing.py
│   ├── nkp1 payload commitment
│   └── nke1 Event/hash-chain commitment
├── migrations.py + sql/0001_*.sql
│   └── checksum-locked authoritative-history schema
├── history.py
│   └── verified repeatable-read replay snapshot
├── replay.py
│   ├── Replay Receipt
│   ├── projection read/destroy/rebuild
│   ├── stale-head guard
│   └── projection-to-Receipt consistency
├── receipt_store.py / replay_models.py
│   └── canonical bounded operational evidence
└── sql/0002_*.sql
    └── disposable projections and operational Receipts
```

## P4 ownership

```text
native_kernel.postgresql_profile.conformance
│
├── semantic check execution
├── PostgreSQL check execution
├── assertion support map
├── check/result traceability
├── C1/C2 metadata boundary
└── nk-evidence-report/1 rendering

external validation
│
├── tools/conformance/runner.py
├── tools/conformance/validate_p4_report.py
├── tests/test_p4_conformance_unit.py
├── tests/test_p4_postgresql_integration.py
├── tests/test_p4_manifest.py
└── .github/workflows/p4-conformance.yml
```

P4 evaluates existing bounded behavior. It does not add new authoritative storage semantics or fill unsupported subsystems through documentation.

## Assertion families

```text
NK-SEM — semantic roles and admission meaning
NK-ID  — identity and canonical encoding
NK-EVT — events, time, order and replay
NK-AUT — authority, admission and Receipts
NK-CFL — conflict and explicit unknowns
NK-EQV — conformance and semantic equivalence
NK-EPI — proposed epistemic family
```

Current profile summary:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
```

The 18 unsupported results include all eight proposed `NK-EPI` assertions and accepted gaps such as P5 translation, conflict representation, restore enforcement and cross-project authority.

## P4 evidence route

Read in order:

1. Issue #55;
2. ADR-0018;
3. RFC-0002;
4. `P4_IMPLEMENTATION_RECORD.md`;
5. `conformance.py`;
6. adapter CLI and strict validator;
7. P4 tests and manifest guard;
8. P4 workflow;
9. exact run/jobs/artifacts for the PR head.

Initial C2 evidence:

```text
head 93710131fffdea7d9a586cc05e7f258c07fae707
P4 run 31175767586 — PASS
PostgreSQL 16/18 × Python 3.11/3.12 — PASS
4 JSON evidence artifacts retained
P1/P2/P3 regressions — PASS
```

Required interpretation:

```text
P4 C2 for SUPPORTED assertions
≠ all assertions supported
≠ C3
≠ accepted NK-EPI
≠ truth/authenticity
≠ physical deletion
≠ production guarantee
```

## Source-recovery route

Start with `STATUS.md`, Issue #1, import specs, `docs/source-recovery/`, `tools/source_recovery/` and its isolated workflow.

```text
clean P1–P4 implementation
≠ controlled v0.1.2.1 import
≠ recovered original tests
```

## World and epistemic boundary

Preserve:

```text
representation ≠ represented reality
observation ≠ explanation
unknown ≠ false
retrieval/model output ≠ admitted knowledge
storage presence ≠ truth or authority
C2 report ≠ unlimited proof
```

ADR-0008 and `NK-EPI-001…008` remain proposed and are not promoted by P4.

## Ecosystem boundary

- Native Kernel — semantic memory/Event/replay/evidence contracts and bounded profiles;
- Titan — cognition, retrieval, tools and orchestration;
- Mentaury Soul — digital individuality and continuity;
- Crystal — verifiable memory, evidence and audit.

No P1–P4 component authorizes shared runtime, storage, identity or authority.

## Decision ownership

- architecture/contract acceptance — operator through ADR process;
- phase authorization — separate explicit operator GO;
- assertion support — exact P4 report at a named SHA/run;
- source authenticity — Issue #1 provenance gate;
- C3 — materially independent second profile plus comparison evidence;
- Notion — rationale/history, never overriding GitHub behavior/evidence.

## Task routes

| Task | Minimum route |
|---|---|
| P1 audit | Issue #43 → ADR-0015 → source → tests → manifest |
| P2 audit | Issue #46 → ADR-0016 → SQL/source → tests → matrix |
| P3 audit | Issue #49 → ADR-0017 → replay source → tests → matrix |
| P4 audit | Issue #55 → ADR-0018 → adapter/map → report validator → artifacts |
| Identity | ADR-0011 → canonical.py → identity fixtures/tests → P4 results |
| Authority | NK-AUT → authority.py → append port → Receipt tests → P4 results |
| Replay | ADR-0012/0017 → history.py/replay.py → P3/P4 checks |
| Conformance claim | assertion ID → P4 result → check IDs → exact artifact |
| Deletion | ADR-0013 → semantic transitions/Receipts; physical execution absent |
| P5/C3 | separate GO → independent profile → equivalence comparison |
| Source candidate | Issue #1 import spec and provenance tooling |
| Cross-project work | ecosystem boundaries plus target-project governance |
