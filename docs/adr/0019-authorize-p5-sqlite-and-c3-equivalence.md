# ADR-0019 — Authorize P5 independent SQLite profile and assertion-scoped C3 equivalence

- **Status:** `ACCEPTED`
- **Operator approval:** `APPROVED`
- **Decision date:** 2026-08-07
- **Issue:** #58
- **Pull request:** #59
- **Evidence lineages:** `clean/postgresql-reference/0.1` and `clean/sqlite-embedded/0.1`

## Context

P1–P4 established a bounded PostgreSQL reference profile and assertion-scoped C2 evidence. That did not demonstrate storage neutrality or cross-profile equivalence because one implementation profile cannot prove that accepted meaning survives a materially different storage substrate.

P5 introduces an independent embedded SQLite profile using Python standard-library `sqlite3`. It must implement the accepted semantic/Event/evidence contracts without calling the PostgreSQL append, replay, projection or Receipt adapters.

## Decision

Authorize P5 and C3 under the following constraints:

1. SQLite is an independent implementation profile, not an Architecture Canon dependency.
2. Cross-profile comparison is assertion-scoped and uses declared equivalence classes.
3. C3 may be claimed only for assertion results backed by passed repository comparison checks and retained artifacts.
4. `PARTIAL` and `UNSUPPORTED` assertions remain outside the supported C3 set.
5. Operational differences between PostgreSQL and SQLite remain explicit and are not normalized away.
6. All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.
7. Issue #1 historical recovery and Issue #18 publication/licensing remain independent.

## Equivalence classes

| Class | Required equivalence |
|---|---|
| `BYTE` | `nk-id/1.0` canonical vectors and exact imported authoritative Event bytes/hash chain |
| `STRUCTURAL` | complete assertion/report shape and declared contract fields |
| `SEMANTIC` | reducer state, projection state and bounded Receipt proof fields |
| `BEHAVIOURAL` | accepted/rejected commands, idempotency, writer fencing and ordering outcomes |

## Allowed differences

- SQL dialect, table/index layout and migration mechanics;
- PostgreSQL server topology versus SQLite single-file embedding;
- PostgreSQL row locks versus SQLite `BEGIN IMMEDIATE` serialization;
- independently generated Event IDs and recorded-at timestamps for separately executed workloads;
- IAM, networking, replication, failover, concurrency and administration capabilities;
- profile-local query plans and non-semantic storage metadata.

## Forbidden differences

- canonical semantic identity vectors;
- Command digest and canonical payload meaning;
- global/stream ordering under the declared single-writer model;
- hash-chain validity;
- reducer/projection canonical state and digest;
- idempotency, stale-writer and corruption rejection outcomes;
- bounded Receipt proof booleans and limitations;
- exact bytes/hash commitments when PostgreSQL authoritative history is imported into SQLite.

## Initial repository evidence

```text
Evidence head: d43a6ed28232e9fc8b62f84d9025386fb8bce6f7
P5/C3 run:    31181341275 — PASS
Matrix:        Python 3.11/3.12 × PostgreSQL 16/18
SQLite:        3.45.1 on the evidence runner
Artifacts:     4 archives × 3 JSON reports
```

SQLite profile result map:

```text
41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
```

Cross-profile comparison result map:

```text
45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
support_state: PARTIAL
```

Four assertions are promoted only by passed cross-profile evidence:

```text
NK-SEM-008
NK-ID-008
NK-EQV-002
NK-EQV-003
```

## Consequences

Positive:

- storage-neutral claims now have bounded executable evidence across two materially different profiles;
- PostgreSQL and SQLite can be compared by observable meaning rather than schema similarity;
- exact authoritative-history import demonstrates byte/hash preservation across profiles;
- C3 overclaim is machine-guarded by manifest and report validators.

Costs and limits:

- C3 remains partial and scenario-bounded;
- SQLite does not inherit PostgreSQL operational capabilities;
- physical deletion, complete conflict handling, C4/C5 and production evidence remain absent;
- artifact retention is finite;
- future contract/profile changes require renewed comparison evidence.

## Non-claims

```text
C3 for 45 SUPPORTED assertions
≠ support for all 72
≠ PostgreSQL/SQLite operational equivalence
≠ truth or external authenticity
≠ physical or cryptographic deletion
≠ C4/C5
≠ production readiness
≠ historical source recovery
```
