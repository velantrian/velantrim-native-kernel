# 🐘📦 Storage and Execution Profiles

**[English](./STORAGE_AND_EXECUTION_PROFILES.md) · [Русский](./STORAGE_AND_EXECUTION_PROFILES.ru.md)**

| Dimension | State |
|---|---|
| Decision status | `ACCEPTED` |
| PostgreSQL profile | `P1–P4 PARTIAL / C2 REPOSITORY-REPRODUCED` |
| SQLite profile | `P5 PARTIAL / C2 REPOSITORY-REPRODUCED ON EVIDENCE HEAD` |
| Cross-profile comparison | `C3 PARTIAL / REPOSITORY-REPRODUCED ON EVIDENCE HEAD` |
| Architecture layer | Implementation Profiles, not Architecture Canon |
| Production status | `NOT READY / NOT CLAIMED` |

> [!WARNING]
> Historical P5/C3/C4/C5 evidence used SQLite 3.45.1. ADR-0023 now requires the actually linked SQLite library to be 3.51.3+ before WAL is opened. Safe-version PR-head and final-main reproduction is captured additively; historical artifacts remain preserved and assertion arithmetic is unchanged.

> [!IMPORTANT]
> PostgreSQL and SQLite are replaceable present-day profiles. Neither database defines Claim, Event, Relation, Conflict, Projection or Receipt meaning.

## Compact model

```text
🏛️ Architecture Canon
        ↓
📐 Storage/Replay/Evidence contracts
        ↓
┌──────────────────────┬──────────────────────┐
│ PostgreSQL reference │ SQLite embedded      │
│ server/local service │ single-file embedded │
│ P1–P4                │ P5                   │
└──────────┬───────────┴──────────┬───────────┘
           └──── C3 comparison ───┘
```

## Current profiles

### 🐘 PostgreSQL reference

```text
Profile:  native-kernel/postgresql-reference@0.4-p4
Lineage:  clean/postgresql-reference/0.1
Role:     full local/server profile
```

Mechanisms:

- PostgreSQL 16–18 and Psycopg;
- checksum-locked migrations;
- transactional writer owner/epoch/expiry fencing;
- durable idempotency and rollback-safe sequence allocation;
- repeatable-read replay;
- disposable projections and bounded Receipts;
- complete P4 assertion report.

### 📦 SQLite embedded

```text
Profile:  native-kernel/sqlite-embedded@0.5-p5
Lineage:  clean/sqlite-embedded/0.1
Role:     embedded / portable / single-file profile
```

Mechanisms:

- Python standard-library `sqlite3`;
- fail-closed linked SQLite 3.51.3+ WAL gate;
- exact stored Event Envelope field/value/hash verification;
- WAL, foreign keys, synchronous FULL and busy timeout;
- checksum/digest-guarded atomic migrations;
- `BEGIN IMMEDIATE` single-writer transaction envelope;
- owner/epoch/expiry fencing;
- durable idempotency and rollback-safe ordering;
- replay, disposable projections and bounded Receipts;
- exact PostgreSQL authoritative-history import;
- complete P5 assertion report.

SQLite does not call PostgreSQL append, replay, projection or Receipt adapters.

## Offline is not a database choice

```text
❌ offline = SQLite
❌ online  = PostgreSQL

✅ local full service     = local model + Kernel + PostgreSQL localhost
✅ embedded portable tool = application + SQLite file
```

Both profiles can run without internet. Profile selection is an operational/deployment choice, not a semantic definition.

## Compute and storage are independent axes

| Compute profile | Possible storage profile |
|---|---|
| Local small model | PostgreSQL or SQLite |
| Local large model | PostgreSQL or SQLite, depending on deployment |
| Remote model | PostgreSQL or SQLite |
| Symbolic engine | any conforming profile |
| Future compute | current or future storage adapter |

A model choice must not silently select the authoritative database.

## Profile selection

Choose PostgreSQL when the deployment needs:

- multiple processes/agents;
- network access and roles;
- long-running server operation;
- larger histories and complex queries;
- mature backup/restore/replication tooling;
- broader concurrency and administration.

Choose SQLite when the deployment needs:

- one portable file;
- an embedded application;
- no separate database service;
- constrained devices or local utilities;
- fixtures, recovery tools, diagnostics or demonstrations;
- a bounded single-writer operational envelope.

```text
SQLite is not degraded semantics.
SQLite is a smaller operational profile.
```

## One authoritative profile per Kernel instance

The active authoritative storage profile is selected at deployment/startup, not per request.

```text
❌ request A → PostgreSQL authority
❌ request B → SQLite authority

✅ one instance → one active authoritative profile
✅ migration/import → explicit fenced operation with evidence
```

Random routing across authoritative stores would create ambiguous ordering, duplicated/missing Claims and non-reproducible Receipts.

## Cross-profile migration/import

P5 implements an exact PostgreSQL-history import into SQLite:

```text
PostgreSQL authoritative Events
→ verify canonical bytes/order/hash chain
→ import exact Event identifiers/timestamps/payloads/hashes
→ verify SQLite stored history
→ replay from sequence 1
→ compare canonical state
```

This proves one bounded byte/semantic path. It is not a general online migration product, failover mechanism or replication protocol.

## C3 equivalence classes

| Class | Required comparison |
|---|---|
| `BYTE` | identity vectors and exact imported Event bytes/hash chain |
| `STRUCTURAL` | required contract/report fields and relations |
| `SEMANTIC` | reducer/projection state and Receipt boundaries |
| `BEHAVIOURAL` | accepted/rejected commands, idempotency, fencing and order |

Current cross-profile map:

```text
45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
support_state: PARTIAL
```

Promoted only through cross-profile evidence:

```text
NK-SEM-008
NK-ID-008
NK-EQV-002
NK-EQV-003
```

## Allowed differences

- SQL dialect and schema/index layout;
- server process versus embedded file;
- row locks versus `BEGIN IMMEDIATE`;
- independently generated Event IDs/timestamps for separate workloads;
- IAM, networking, replication, failover, concurrency and administration;
- profile-local query plans and non-semantic metadata.

## Forbidden differences

- canonical identity and Command digest;
- semantic payload and declared order;
- hash-chain validity;
- reducer/projection state;
- idempotency, stale-writer and corruption outcomes;
- Receipt proof-boundary fields;
- exact Event bytes/hash commitments during authoritative-history import.

## Current evidence

```text
Evidence head: d43a6ed28232e9fc8b62f84d9025386fb8bce6f7
P5/C3 run:    31181341275 — PASS
Matrix:        Python 3.11/3.12 × PostgreSQL 16/18 × SQLite 3.45.1
Artifacts:     4 archives × 3 JSON reports
```

This is historical evidence from SQLite 3.45.1. It does not satisfy the current 3.51.3 WAL floor; the additive ADR-0023 bundle records the replacement proof without relabeling these rows.

## Explicit limits

```text
C3 semantic/behavioural equivalence
≠ support for all 72 assertions
≠ operational equivalence
≠ exhaustive state-space proof
≠ backup/restore or failover equivalence
≠ truth/authenticity
≠ physical deletion
≠ C4/C5
≠ production readiness
```

## Future substrates

A future storage system may have no SQL, tables, files or current transaction model. It can qualify only by implementing the accepted contracts and producing its own assertion-scoped C2/C3 evidence. PostgreSQL and SQLite remain present-day profiles, not permanent architectural definitions.
