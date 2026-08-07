# 🗺️ Native Kernel Document, Contract and Authority Map

Use exact SHAs, dataset digests, statuses and evidence. A C4 report with `support_state: PARTIAL` is not complete conformance, live shadowing or authority promotion.

## Primary orientation surfaces

| Surface | Role | Authority / caution |
|---|---|---|
| `README.md` / `README.ru.md` | Public purpose and maturity | Must state C4 offline-only scope and non-claims |
| `STATUS.md` | Authoritative current implementation/evidence boundary | Verify exact branch/main SHA |
| `ARCHITECTURE.md` | Canon shape and invariants | Architecture, not runtime proof |
| `contracts/registry.json` | Stable 72 assertion IDs and decision statuses | `NK-EPI` remains proposed |
| `contracts/evidence-report-v1.schema.json` | Single-profile evidence protocol | Schema validity alone is not runtime evidence |
| `contracts/shadow-workload-v1.json` | Approved C4 recorded observations | Immutable version/digest; synthetic, not live traffic |
| `contracts/shadow-report-v1.schema.json` | C4 report shape | Schema validity alone is not C4 evidence |
| `docs/adr/0018-*` | P4 assertion-scoped C2 decision | C2 applies only to supported results |
| `docs/adr/0019-*` | P5 SQLite/C3 decision | C3 is partial and non-operational |
| `docs/adr/0020-*` | C4 offline shadow authorization | No authority promotion, writes or side effects |
| `profiles/postgresql-reference-v0/p4-manifest.json` | PostgreSQL C2 summary | `41/13/18` |
| `profiles/sqlite-embedded-v0/p5-manifest.json` | SQLite C2 and cross-profile C3 summary | SQLite `41/13/18`; C3 `45/10/17` |
| `profiles/shadow-evaluation-v0/c4-manifest.json` | C4 dataset/evidence summary | C4 limited to 45 C3-supported assertions |
| `docs/ai/P4_IMPLEMENTATION_RECORD.md` | Exact P4 evidence | Historical prerequisite |
| `docs/ai/P5_IMPLEMENTATION_RECORD.md` | Exact P5/C3 evidence | C4 prerequisite |
| `docs/ai/C4_IMPLEMENTATION_RECORD.md` | Exact C4 dataset, runs, artifacts and limits | Re-verify final PR head |
| `native_kernel/semantic_core/` | Profile-neutral semantics | Standard-library implementation, not Canon |
| `native_kernel/postgresql_profile/` | PostgreSQL append/replay/projection/P4 | Server profile |
| `native_kernel/sqlite_profile/` | Independent SQLite append/replay/projection/P5 | Embedded profile |
| `native_kernel/shadow_evaluation/` | Authority-free recorded-observation evaluator | Evidence layer, not storage/runtime authority |
| `tools/conformance/cross_profile_comparator.py` | PostgreSQL↔SQLite C3 comparator | `nk-equivalence-report/1` |
| `tools/conformance/offline_shadow_evaluator.py` | Approved-dataset C4 evaluator | `nk-shadow-report/1` |
| `tools/conformance/validate_c4_report.py` | Strict C4 report guard | Exact dataset/scope/authority/repository metadata |
| `tools/profiles/validate_c4_manifest.py` | C4 manifest guard | Rejects false C4/C5/recovery/authority claims |
| `.github/workflows/c4-offline-shadow.yml` | 4× C4 matrix and P1–P5 regressions | Only completed exact runs/artifacts are evidence |

## Architecture-to-evidence route

```text
Architecture Canon
        ↓
accepted exact contracts + registry 1.1.0
        ↓
P1 semantic core
        ↓
P2 PostgreSQL append/idempotency
        ↓
P3 replay/projections/Receipts
        ↓
P4 PostgreSQL assertion report / C2
        ↓
P5 independent SQLite profile
        ↓
PostgreSQL ↔ SQLite C3 comparison
        ↓
45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
        ↓
approved immutable recorded workload
        ↓
C4 non-authoritative shadow report + 15 Shadow Receipts
```

## PostgreSQL ownership

```text
native_kernel.postgresql_profile
├── adapter.py        append / idempotency / writer fencing
├── history.py        verified authoritative snapshot
├── replay.py         replay / projection rebuild / Receipts
├── hashing.py        payload and Event commitments
├── migrations.py    checksum-locked migrations
└── conformance.py   72-ID PostgreSQL report
```

## SQLite ownership

```text
native_kernel.sqlite_profile
├── adapter.py        independent sqlite3 append / fencing
├── hashing.py        SQLite Event commitments
├── replay.py         replay / projection rebuild / Receipts
├── conformance.py    complete SQLite 72-ID report
├── equivalence.py    cross-profile workload and C3 map
├── models.py         SQLite profile domain records
└── errors.py         explicit profile failures
```

The SQLite implementation does not call PostgreSQL append, replay, projection or Receipt adapters.

## C3 ownership

```text
same fixture pack
├── PostgreSQL execution
├── SQLite execution
├── normalized behavioural comparison
├── reducer/projection/Receipt comparison
├── exact PostgreSQL Event import into SQLite
└── BYTE / STRUCTURAL / SEMANTIC / BEHAVIOURAL checks
        ↓
nk-equivalence-report/1
        ↓
45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
```

Promoted by cross-profile evidence:

```text
NK-SEM-008
NK-ID-008
NK-EQV-002
NK-EQV-003
```

All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

## C4 ownership

```text
contracts/shadow-workload-v1.json
├── exact approved bytes / dataset SHA-256
├── 15 recorded cases
├── reference and candidate observations
├── declared compared fields
├── declared allowed operational differences
├── thresholds
└── authority policy
        +
exact C3 prerequisite report
        ↓
native_kernel.shadow_evaluation
├── protocol and digest validation
├── authority-boundary validation
├── declared-field comparison
├── semantic/critical metrics
├── one nk-shadow-receipt/1 per case
└── complete 72-ID nk-shadow-report/1
```

C4 owns observation evidence only. It does not own command admission, profile persistence, promotion or deployment.

## C4 authority boundary

```text
SHADOW_ONLY
├── authority promotion:   FORBIDDEN
├── authoritative writes:  FORBIDDEN
├── side effects:           FORBIDDEN
└── promotion decision:    NOT_AUTHORIZED
```

## C4 evidence route

Read in order:

1. Issue #61;
2. ADR-0020;
3. `C4_IMPLEMENTATION_RECORD.md`;
4. exact approved dataset bytes and digest;
5. evaluator/report/Receipt source;
6. strict report and manifest validators;
7. C4 tests and workflow;
8. exact run/jobs/artifacts for the PR head.

First complete evidence:

```text
head 97abce685a68e24aec9afab451c009df5783b96b
C4 run 31187532364 — PASS
Python 3.11/3.12 × PostgreSQL 16/18 × SQLite 3.45.1 — PASS
4 artifacts × 4 JSON reports
P1–P5 regressions — PASS
```

Required interpretation:

```text
C4 for one approved 15-case dataset and 45 SUPPORTED assertions
≠ live production shadowing
≠ authority promotion / candidate approval
≠ all assertions supported
≠ exhaustive or operational equivalence
≠ accepted NK-EPI
≠ truth/authenticity
≠ physical deletion
≠ C5 / production guarantee
```

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

## Source-recovery boundary

```text
clean P1–P5 implementation + C4 evidence layer
≠ controlled v0.1.2.1 import
≠ recovered original tests
```

Issue #1 remains independent.

## Ecosystem boundary

- Native Kernel — semantic memory/Event/replay/evidence contracts and bounded profiles/evidence protocols;
- Titan — cognition, retrieval, tools and orchestration;
- Mentaury Soul — digital individuality and continuity;
- Crystal — verifiable memory, evidence and audit.

No P1–P5 or C4 component authorizes shared runtime, storage, identity, authority or promotion.

## Decision ownership

- architecture/contract acceptance — operator through ADR process;
- phase authorization — separate explicit operator GO;
- C2 support — exact single-profile report at a named SHA/run;
- C3 support — exact cross-profile report and comparison artifacts;
- C4 support — exact approved dataset/digest, C3 prerequisite, report, Receipts and artifact;
- authority promotion/live deployment/C5 — separately authorized future decisions;
- source authenticity — Issue #1 provenance gate;
- Notion — rationale/history, never overriding GitHub behavior/evidence.

## Task routes

| Task | Minimum route |
|---|---|
| C4 audit | Issue #61 → ADR-0020 → dataset digest → evaluator → report/Receipts → exact artifact |
| Dataset change | new dataset version/digest → ADR/manifest/tests → new repository evidence |
| P5/C3 audit | Issue #58 → ADR-0019 → SQLite source → comparator → reports/artifacts |
| P4 audit | Issue #55 → ADR-0018 → PostgreSQL report → artifacts |
| Assertion claim | assertion ID → C2/C3/C4 result → check/case IDs → exact artifact |
| Authority | NK-AUT → profile adapters → Receipt tests → C4 no-promotion boundary |
| Replay | ADR-0012/0017 → both replay implementations → comparison/shadow cases |
| Deletion | ADR-0013 → semantic transitions/Receipts; physical execution absent |
| Source candidate | Issue #1 provenance/import tooling |
| Cross-project work | ecosystem boundaries plus target-project governance |
