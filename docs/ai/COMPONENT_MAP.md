# 🗺️ Native Kernel Document, Contract and Authority Map

Use exact SHAs, statuses and evidence. A C3 report with `support_state: PARTIAL` is not complete conformance or operational equivalence.

## Primary orientation surfaces

| Surface | Role | Authority / caution |
|---|---|---|
| `README.md` / `README.ru.md` | Public purpose and maturity | Must state P5 partial C3 counts and non-claims |
| `STATUS.md` | Authoritative current implementation/evidence boundary | Verify exact branch/main SHA |
| `ARCHITECTURE.md` | Canon shape and invariants | Architecture, not runtime proof |
| `contracts/registry.json` | Stable 72 assertion IDs and decision statuses | `NK-EPI` remains proposed |
| `contracts/evidence-report-v1.schema.json` | Single-profile evidence protocol | Schema validity alone is not runtime evidence |
| `docs/rfc/0002-*` | Accepted clean PostgreSQL profile lifecycle | P1–P5 implementation contract |
| `docs/adr/0018-*` | P4 assertion-scoped C2 decision | C2 applies only to supported results |
| `docs/adr/0019-*` | P5 SQLite/C3 decision | C3 is partial and non-operational |
| `profiles/postgresql-reference-v0/p4-manifest.json` | PostgreSQL C2 summary | 41/13/18 |
| `profiles/sqlite-embedded-v0/p5-manifest.json` | SQLite C2 and cross-profile C3 summary | SQLite 41/13/18; C3 45/10/17 |
| `docs/ai/P4_IMPLEMENTATION_RECORD.md` | Exact P4 evidence | Historical prerequisite |
| `docs/ai/P5_IMPLEMENTATION_RECORD.md` | Exact P5/C3 runs, artifacts and limits | Re-verify final PR head |
| `native_kernel/semantic_core/` | Profile-neutral semantics | Standard-library implementation, not Canon |
| `native_kernel/postgresql_profile/` | PostgreSQL append/replay/projection/P4 | Server profile |
| `native_kernel/sqlite_profile/` | Independent SQLite append/replay/projection/P5 | Embedded profile |
| `tools/conformance/postgresql_profile_adapter.py` | PostgreSQL P4 report CLI | `nk-evidence-report/1` |
| `tools/conformance/sqlite_profile_adapter.py` | SQLite P5 report CLI | `nk-evidence-report/1` |
| `tools/conformance/cross_profile_comparator.py` | PostgreSQL↔SQLite comparator | `nk-equivalence-report/1` |
| `tools/conformance/validate_p5_report.py` | Strict SQLite/C3 anti-overclaim guard | Requires exact maps and evidence |
| `tools/profiles/validate_p5_manifest.py` | P5 manifest guard | Rejects false C3/C4/C5/recovery |
| `.github/workflows/p5-sqlite-c3.yml` | 4× C2/C3 matrix, reports and regressions | Only completed exact runs are evidence |

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
PostgreSQL ↔ SQLite comparison
        ↓
45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / C3 PARTIAL
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

## P5 evidence route

Read in order:

1. Issue #58;
2. ADR-0019;
3. `P5_IMPLEMENTATION_RECORD.md`;
4. SQLite adapter/replay/conformance source;
5. cross-profile comparator;
6. strict report and manifest validators;
7. P5 tests and workflow;
8. exact run/jobs/artifacts for the PR head.

Initial evidence:

```text
head d43a6ed28232e9fc8b62f84d9025386fb8bce6f7
P5/C3 run 31181341275 — PASS
Python 3.11/3.12 × PostgreSQL 16/18 × SQLite 3.45.1 — PASS
4 artifacts × 3 JSON reports
P1–P4 regressions — PASS
```

Required interpretation:

```text
C3 for 45 SUPPORTED assertions
≠ all assertions supported
≠ operational equivalence
≠ accepted NK-EPI
≠ truth/authenticity
≠ physical deletion
≠ production guarantee
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
clean P1–P5 implementation
≠ controlled v0.1.2.1 import
≠ recovered original tests
```

Issue #1 remains independent.

## Ecosystem boundary

- Native Kernel — semantic memory/Event/replay/evidence contracts and bounded profiles;
- Titan — cognition, retrieval, tools and orchestration;
- Mentaury Soul — digital individuality and continuity;
- Crystal — verifiable memory, evidence and audit.

No P1–P5 component authorizes shared runtime, storage, identity or authority.

## Decision ownership

- architecture/contract acceptance — operator through ADR process;
- phase authorization — separate explicit operator GO;
- C2 support — exact single-profile report at a named SHA/run;
- C3 support — exact cross-profile report and comparison artifacts;
- source authenticity — Issue #1 provenance gate;
- Notion — rationale/history, never overriding GitHub behavior/evidence.

## Task routes

| Task | Minimum route |
|---|---|
| P4 audit | Issue #55 → ADR-0018 → PostgreSQL report → artifacts |
| P5/C3 audit | Issue #58 → ADR-0019 → SQLite source → comparator → reports/artifacts |
| Identity | ADR-0011 → canonical vectors → C2/C3 results |
| Authority | NK-AUT → profile adapters → Receipt tests → exact report |
| Replay | ADR-0012/0017 → both replay implementations → comparison checks |
| Conformance claim | assertion ID → profile/C3 result → check IDs → exact artifact |
| Deletion | ADR-0013 → semantic transitions/Receipts; physical execution absent |
| Source candidate | Issue #1 provenance/import tooling |
| Cross-project work | ecosystem boundaries plus target-project governance |
