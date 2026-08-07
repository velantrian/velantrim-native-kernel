# RFC-0002: PostgreSQL Reference Profile v0 Planning and Implementation Contract

- **RFC status:** `ACCEPTED`
- **Evidence level:** `REPOSITORY_REPRODUCED — POSTGRESQL C2 + SQLITE C2 + CROSS-PROFILE C3 ON PREVIOUS HEAD`
- **Implementation status:** `PARTIAL — P1 + P2 + P3 + P4 + P5`
- **Operator approval:** `APPROVED`
- **PostgreSQL profile:** `native-kernel/postgresql-reference@0.4-p4`
- **SQLite comparison profile:** `native-kernel/sqlite-embedded@0.5-p5`
- **Lineages:** `clean/postgresql-reference/0.1`, `clean/sqlite-embedded/0.1`
- **Related:** Issues #40, #43, #46, #49, #55, #58; PRs #47, #50, #56, #59; ADR-0001, ADR-0009, ADR-0011…0019

## 1. Purpose

Define the first clean Native Kernel implementation lifecycle without turning PostgreSQL, SQLite, Python, Psycopg, SQL layouts, locks, files or current hardware into Architecture Canon.

```text
accepted architecture contracts
        ↓
P1 profile-independent semantic core
        ↓
P2 PostgreSQL append/idempotency
        ↓
P3 replay/projection rebuild/Receipts
        ↓
P4 PostgreSQL assertion-scoped C2
        ↓
P5 independent SQLite profile + assertion-scoped C3
```

P5 validates a bounded technology-neutral claim across two materially different storage profiles. It does not authorize C4/C5, production, deletion execution or ecosystem wiring.

## 2. Lineage boundary

```text
clean/postgresql-reference/0.1
clean/sqlite-embedded/0.1
≠ recovered v0.1.2.1
≠ original 44-test suite
≠ historical prototype continuation
```

Issue #1 remains active and independent. Nothing in this RFC declares historical source globally lost or replaces provenance requirements.

## 3. Accepted inputs

| Input | Required meaning |
|---|---|
| ADR-0001 | Canon is separate from implementation profiles |
| ADR-0009 | PostgreSQL full profile; SQLite embedded profile |
| ADR-0011 / `nk-id/1.0` | canonical identity |
| ADR-0012 / `nk-event/1.0` | single-writer append, idempotency, order and replay |
| ADR-0013 / `nk-deletion/1.0` | deletion/restriction/retention meaning and proof limits |
| ADR-0014 / `nk-fixtures/1.0` | executable fixture/evidence protocol |
| ADR-0015…0018 | P1–P4 authorization and boundaries |
| ADR-0019 | P5 SQLite and assertion-scoped C3 authorization |
| registry `1.1.0` | stable 72 assertion IDs and decisions |

`NK-EPI-001…008` and ADR-0008 remain proposed. Both profile reports and C3 retain them as `UNSUPPORTED`.

## 4. Current reality

```text
P1 semantic core:              PARTIAL / REPOSITORY-TESTED
P2 PostgreSQL append:          PARTIAL / REPOSITORY-INTEGRATION-TESTED
P3 replay/projections:         PARTIAL / REPOSITORY-INTEGRATION-TESTED
P4 PostgreSQL conformance:     PARTIAL / C2 REPOSITORY-REPRODUCED
P5 SQLite profile:             PARTIAL / C2 REPOSITORY-REPRODUCED ON EVIDENCE HEAD
Cross-profile comparison:      PARTIAL / C3 REPOSITORY-REPRODUCED ON EVIDENCE HEAD
support_state:                 PARTIAL
C4/C5/production:              NOT_ESTABLISHED / NOT_AUTHORIZED
Physical deletion:             NOT_IMPLEMENTED
```

Single-profile maps:

```text
41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
```

Cross-profile map:

```text
45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
```

C2/C3 labels apply only to results marked `SUPPORTED` in the exact reports.

## 5. Architecture and ownership

```text
Command canonicalization / semantic reducer      ← P1
PostgreSQL authoritative append/idempotency       ← P2
PostgreSQL replay/projections/Receipts             ← P3
PostgreSQL complete assertion report               ← P4
Independent SQLite append/replay/projections       ← P5
PostgreSQL↔SQLite equivalence comparator           ← P5
```

### 5.1 P1 semantic core

`native_kernel.semantic_core` owns canonical JSON/identity, immutable semantic objects, authority boundaries, deterministic reduction, deletion/restriction transitions, bounded Receipt guards, upcasting and state decoding.

### 5.2 PostgreSQL profile

`native_kernel.postgresql_profile` owns:

- checksum-locked migrations;
- instance/history heads and writer fencing;
- atomic Event/idempotency persistence;
- rollback-safe sequence allocation;
- canonical commitments and hash chain;
- verified replay;
- disposable projections and bounded Receipts;
- complete P4 report.

### 5.3 SQLite profile

`native_kernel.sqlite_profile` independently owns:

- stdlib `sqlite3` schema and migrations;
- WAL/foreign-key/synchronous configuration;
- `BEGIN IMMEDIATE` single-writer envelope;
- owner/epoch/expiry fencing;
- append/idempotency/order/hash-chain behavior;
- replay, projections and bounded Receipts;
- exact PostgreSQL authoritative-history import;
- SQLite profile report and C3 comparison.

SQLite does not call PostgreSQL append, replay, projection or Receipt adapters.

## 6. P4 single-profile evidence

`nk-evidence-report/1` emits every registry ID exactly once with result status, passed check references and limitations.

PostgreSQL and SQLite single-profile maps are guarded at `41/13/18/0`.

```text
C2
≠ support for all 72
≠ C3
≠ truth/authenticity
≠ physical deletion
```

## 7. P5 cross-profile comparison

P5 uses a separate `nk-equivalence-report/1` protocol.

```text
shared accepted contracts + fixture pack
→ independent PostgreSQL execution
→ independent SQLite execution
→ normalized observable outcomes
→ replay/projection/Receipt comparison
→ exact PostgreSQL Event import into SQLite
→ 72 assertion results
```

Equivalence classes:

| Class | Required comparison |
|---|---|
| `BYTE` | canonical identity and exact imported Event bytes/hash chain |
| `STRUCTURAL` | required contract/report fields |
| `SEMANTIC` | reducer/projection state and Receipt proof boundaries |
| `BEHAVIOURAL` | accepted/rejected commands, idempotency, fencing and order |

Cross-profile evidence promotes only:

```text
NK-SEM-008
NK-ID-008
NK-EQV-002
NK-EQV-003
```

## 8. Allowed and forbidden differences

Allowed:

- SQL dialect/schema/index layout;
- server topology versus embedded file;
- row locks versus `BEGIN IMMEDIATE`;
- independently generated Event IDs/timestamps;
- IAM/network/replication/failover/concurrency/administration;
- non-semantic metadata and query plans.

Forbidden:

- canonical identity and Command digest;
- payload meaning and declared order;
- hash-chain validity;
- reducer/projection canonical state;
- idempotency/stale-writer/corruption outcomes;
- Receipt proof fields;
- exact bytes/hash commitments during authoritative-history import.

## 9. Initial P5 evidence

```text
Evidence head: d43a6ed28232e9fc8b62f84d9025386fb8bce6f7
P5/C3 run:    31181341275 — PASS
P4 run:       31181341370 — PASS
P1 run:       31181341405 — PASS
Fixtures:     31181340889 — PASS
```

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Each of four artifacts contains PostgreSQL P4, SQLite P5 and C3 comparison reports. One archive was downloaded and inspected.

## 10. Evidence boundaries

```text
C3 for 45 SUPPORTED assertions
≠ all 72 supported
≠ exhaustive equivalence
≠ PostgreSQL/SQLite operational equivalence
≠ truth/authenticity
≠ physical deletion
≠ complete conflict handling
≠ C4/C5
≠ production readiness
```

Approval, code presence, one local run or a manifest count is never sufficient repository evidence.

## 11. Explicitly absent

- complete conflict representation/resolution;
- physical/cryptographic deletion workers;
- restore-before-visibility enforcement;
- cross-project authority adapter;
- network API;
- C4 shadow workload evaluation;
- C5 operational security/privacy/incident evidence;
- production HA/backup/restore/compliance guarantees;
- Titan/Mentaury/Crystal runtime wiring;
- historical source recovery;
- package-publication decision under Issue #18.

## 12. Finalization and later gates

P5 PR #59 must repeat P5/C3, P4, P1, fixtures and AI-context checks on one final exact documentation head and retain four artifacts before merge.

Any later C4, C5, production, deletion-execution or ecosystem-integration work requires a new explicit operator GO and separate evidence plan.
