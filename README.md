<div align="center">

# 🧬 Velantrim Native Kernel

### Technology-neutral contracts and replaceable profiles for verifiable memory

**[English](./README.md) · [Русский](./README.ru.md)**

![Status](https://img.shields.io/badge/status-P5%20PARTIAL-6f42c1)
![Evidence](https://img.shields.io/badge/evidence-C3%20ASSERTION--SCOPED-blue)
![Profiles](https://img.shields.io/badge/profiles-PostgreSQL%20%2B%20SQLite-orange)
![Production](https://img.shields.io/badge/production-NOT%20READY-red)

**Claims · Events · Provenance · Time · Deterministic replay · Cross-profile evidence**

> **Preserve meaning when technologies change. Verify before promotion.**

</div>

> [!IMPORTANT]
> **Current branch state:** `RESEARCH / P5 PARTIAL CROSS-PROFILE CONFORMANCE / NOT PRODUCTION-READY`.  
> PostgreSQL and an independent stdlib-`sqlite3` profile now have repository C2 evidence. Their declared cross-profile comparison reports **45 `SUPPORTED`, 10 `PARTIAL`, 17 `UNSUPPORTED`, 0 `FAILED`**. C3 applies only to those 45 supported results; it is not complete support or operational equivalence.

## ⚡ In 30 seconds

Velantrim Native Kernel is an independent, long-horizon architecture and implementation research project.

It studies how semantic memory, recorded change and evidence can preserve meaning when databases, languages, models, processors and future computational substrates change.

```text
🏛️ Architecture Canon
        ↓
📐 Accepted abstract contracts
        ↓
🔌 Replaceable implementation profiles
        ↓
🧪 Assertion-scoped reproducible evidence
        ↓
⚖️ Explicit cross-profile equivalence
```

Modern technologies are laboratory instruments, not permanent definitions:

```text
PostgreSQL · SQLite · Python · files · graph · vector · LLM · CPU/GPU
                         ≠
                 Architecture Canon
```

## 📊 Exact current status

| Area | State |
|---|---|
| Architecture and invariants | **Documented** |
| Exact identity/event/deletion/fixture contracts | **Accepted** — ADR-0011…0014 |
| P1 semantic core | **Partial implementation; repository-tested** |
| P2 PostgreSQL append/idempotency | **Partial; repository-integration-tested** |
| P3 persisted replay/projections/Receipts | **Partial; repository-integration-tested** |
| P4 PostgreSQL assertion adapter | **Partial; C2 repository-reproduced** |
| P5 independent SQLite profile | **Partial; C2 repository-reproduced on evidence head** |
| PostgreSQL/SQLite C3 | **Partial; repository-reproduced on evidence head** |
| Single-profile map | **41 supported / 13 partial / 18 unsupported / 0 failed** |
| Cross-profile C3 map | **45 supported / 10 partial / 17 unsupported / 0 failed** |
| Physical/cryptographic deletion | **Not implemented** |
| Complete conflict subsystem | **Not implemented** |
| C4/C5 / production readiness | **Not established / not claimed** |
| Historical `v0.1.2.1` source | **Not found in accessible sources; Issue #1 open** |
| Titan/Mentaury/Crystal integration | **Not active** |

```text
C3 for 45 SUPPORTED assertions
≠ all 72 assertions supported
≠ PostgreSQL and SQLite operational equivalence
≠ truth or authenticity
≠ physical deletion
≠ production readiness
```

## 🧩 Implementation route

```text
P1  canonical identity / semantic objects / authority / reducer
 ↓
P2  PostgreSQL append / idempotency / writer fencing
 ↓
P3  persisted replay / projection rebuild / bounded Receipts
 ↓
P4  complete PostgreSQL 72-ID report / C2
 ↓
P5  independent SQLite profile / complete SQLite report
 ↓
C3  PostgreSQL ↔ SQLite equivalence comparison
```

## 🐘 PostgreSQL reference profile

Package: [`native_kernel.postgresql_profile`](./native_kernel/postgresql_profile/README.md)

- PostgreSQL `16–18`;
- Psycopg `>=3.3,<3.4`;
- checksum-locked migrations;
- owner/epoch/expiry writer fencing;
- durable idempotency and rollback-safe ordering;
- canonical Event commitments and hash chain;
- replay, disposable projections and bounded Receipts;
- complete assertion-scoped P4 report.

## 🗃️ SQLite embedded profile

Package: [`native_kernel.sqlite_profile`](./native_kernel/sqlite_profile/README.md)

```text
stdlib sqlite3
→ WAL + foreign keys + synchronous FULL
→ BEGIN IMMEDIATE single-writer transaction
→ owner / epoch / expiry fence
→ append / retry / rollback-safe ordering
→ Event hash chain
→ replay / projections / Receipts
```

The SQLite profile uses its own migrations, schema, transactions, append, replay, projection and Receipt implementation. It does **not** call the PostgreSQL adapters.

It also supports exact authoritative-history import: PostgreSQL Event bytes and hash commitments are inserted into SQLite and reverified before replay.

## ⚖️ P5 cross-profile C3

The comparison uses four declared equivalence classes:

| Class | Compared meaning |
|---|---|
| `BYTE` | canonical identity vectors and exact imported Event bytes/hash chain |
| `STRUCTURAL` | complete report shape and declared fields |
| `SEMANTIC` | reducer state, projection state and Receipt proof fields |
| `BEHAVIOURAL` | accepted/rejected commands, idempotency, fencing and order |

Allowed differences include:

- SQL dialect and table/index layout;
- server topology versus a single local file;
- PostgreSQL row locks versus SQLite `BEGIN IMMEDIATE`;
- independently generated Event IDs/timestamps;
- IAM, networking, replication, failover, concurrency and administration.

Forbidden differences include:

- canonical identity and Command digest;
- payload meaning and declared ordering;
- hash-chain validity;
- reducer/projection canonical state;
- idempotency, stale-writer and corruption outcomes;
- bounded Receipt proof fields;
- bytes/hashes in exact authoritative-history import.

Cross-profile evidence promotes exactly:

```text
NK-SEM-008
NK-ID-008
NK-EQV-002
NK-EQV-003
```

All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

## ✅ Initial P5 repository evidence

```text
Evidence head: d43a6ed28232e9fc8b62f84d9025386fb8bce6f7
P5/C3 run:    31181341275 — PASS
P4 run:       31181341370 — PASS
P1 run:       31181341405 — PASS
Fixtures:     31181340889 — PASS
```

Matrix:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Each environment retains one artifact containing:

```text
postgresql-p4-report.json
sqlite-p5-report.json
c3-equivalence-report.json
```

One archive was downloaded and inspected independently. It contained all three reports, exact SHA/run/version metadata, all 72 results and eight passed cross-profile checks.

Exact digests and defect history are recorded in [`docs/ai/P5_IMPLEMENTATION_RECORD.md`](./docs/ai/P5_IMPLEMENTATION_RECORD.md).

## 🧬 Canon shape

```text
🧩 Claim
   ↓
📜 Append-only Event history
   ↓
🧠 Deterministic state reconstruction
   ↓
🗂️ Rebuildable projections
   ↓
🧾 Bounded Receipts and evidence reports
```

| Component | Meaning |
|---|---|
| **Claim** | Stable semantic identity; existence does not establish truth |
| **Event** | Explicit record of an authority-admitted change |
| **Reducer** | Deterministically derives state from declared history/version |
| **Projection** | Disposable read model derived from authoritative Events |
| **Receipt** | Evidence for one declared operation with explicit limits |
| **Evidence report** | Assertion-by-assertion profile support and traceability |
| **Equivalence report** | Assertion-by-assertion comparison across declared profiles |

## 🚫 Explicitly absent

```text
exhaustive equivalence proof
PostgreSQL/SQLite operational equivalence
complete conflict subsystem
physical/cryptographic deletion execution
restore-before-visibility enforcement
cross-project authority adapter
truth/signature/notarization certification
network API
C4/C5
production security/privacy/backup/HA/compliance guarantees
```

## 🧭 Read next

- [`STATUS.md`](./STATUS.md)
- [`ADR-0019`](./docs/adr/0019-authorize-p5-sqlite-and-c3-equivalence.md)
- [`P5 implementation record`](./docs/ai/P5_IMPLEMENTATION_RECORD.md)
- [`Conformance model`](./docs/CONFORMANCE_MODEL.md)
- [`Storage and execution profiles`](./docs/STORAGE_AND_EXECUTION_PROFILES.md)
- [`P5 manifest`](./profiles/sqlite-embedded-v0/p5-manifest.json)

## ⚖️ Evidence and truth boundary

```text
recorded history ≠ reality itself
integrity commitment ≠ signature
operator approval ≠ empirical evidence
retrieval relevance ≠ truth
C2 reproduction ≠ C3 comparison
C3 comparison ≠ operational equivalence
Receipt/report ≠ unlimited proof
```

## 🔗 Ecosystem boundary

Native Kernel does not automatically become the memory runtime or authority of other Velantrim projects.

- **Titan** owns cognition, retrieval, tools and orchestration;
- **Mentaury Soul** owns digital individuality and continuity;
- **Crystal** owns verifiable-memory, evidence and grant-facing product boundaries;
- **Native Kernel** owns neutral semantic memory/Event/evidence contracts and bounded profiles.

Integration requires separate contracts, authority and evidence.

## 🧭 Next gate

The current task is to finish documentation synchronization, repeat P5/C3 on one final exact PR head, inspect the final artifacts and merge PR #59. Any C4, C5, production, deletion-execution or ecosystem-integration work requires a separate explicit authorization.
