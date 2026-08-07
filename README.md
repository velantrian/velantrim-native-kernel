<div align="center">

# 🧬 Velantrim Native Kernel

### Technology-neutral contracts, replaceable profiles and bounded evidence for verifiable memory

**[English](./README.md) · [Русский](./README.ru.md)**

![Status](https://img.shields.io/badge/status-C4%20PARTIAL-6f42c1)
![Evidence](https://img.shields.io/badge/evidence-OFFLINE%20SHADOW-blue)
![Profiles](https://img.shields.io/badge/profiles-PostgreSQL%20%2B%20SQLite-orange)
![Production](https://img.shields.io/badge/production-NOT%20READY-red)

**Claims · Events · Provenance · Time · Deterministic replay · Cross-profile evidence · Offline shadow evaluation**

> **Preserve meaning when technologies change. Verify before promotion.**

</div>

> [!IMPORTANT]
> **Current branch state:** `RESEARCH / C4 PARTIAL OFFLINE SHADOW EVALUATION / NOT PRODUCTION-READY`.  
> PostgreSQL and an independent stdlib-`sqlite3` profile have assertion-scoped repository evidence. C4 adds an authority-free evaluator over one explicitly approved immutable recorded workload. It does not add live shadowing, candidate promotion, production authority or C5.

## ⚡ In 30 seconds

Velantrim Native Kernel is an independent long-horizon architecture and implementation research project.

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
⚖️ Cross-profile equivalence
        ↓
🪞 Authority-free offline shadow evaluation
```

Modern technologies are laboratory instruments, not permanent definitions:

```text
PostgreSQL · SQLite · Python · JSON · files · graph · vector · LLM · CPU/GPU
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
| P5 independent SQLite profile | **Partial; C2 repository-reproduced** |
| PostgreSQL↔SQLite C3 | **Partial; repository-reproduced** |
| C4 offline shadow evaluator | **Partial; repository-reproduced on approved recorded dataset** |
| Single-profile C2 map | **41 supported / 13 partial / 18 unsupported / 0 failed** |
| Cross-profile C3 and C4 scope | **45 supported / 10 partial / 17 unsupported / 0 failed** |
| Live shadowing / candidate promotion | **Not implemented / not authorized** |
| Physical or cryptographic deletion | **Not implemented** |
| Complete conflict subsystem | **Not implemented** |
| C5 / production readiness | **Not authorized / not established** |
| Historical `v0.1.2.1` source | **Not found in accessible sources; Issue #1 open** |
| Titan/Mentaury/Crystal integration | **Not active** |

```text
C4 for one approved 15-case recorded dataset and 45 SUPPORTED assertions
≠ live production shadowing
≠ authority promotion
≠ support for all 72 assertions
≠ exhaustive equivalence
≠ operational equivalence
≠ truth, authenticity or physical deletion
≠ C5 or production readiness
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
 ↓
C4  approved offline recorded workload / shadow reports / Shadow Receipts
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

The SQLite profile owns its migrations, schema, transactions, append, replay, projection and Receipt implementation. It does **not** call PostgreSQL adapters.

It also supports exact authoritative-history import: PostgreSQL Event bytes and hash commitments are inserted into SQLite and reverified before replay.

## ⚖️ P5 cross-profile C3 prerequisite

Four declared equivalence classes are compared:

| Class | Compared meaning |
|---|---|
| `BYTE` | canonical identity vectors and exact imported Event bytes/hash chain |
| `STRUCTURAL` | complete report shape and declared fields |
| `SEMANTIC` | reducer state, projection state and Receipt proof fields |
| `BEHAVIOURAL` | accepted/rejected commands, idempotency, fencing and order |

Allowed differences include SQL dialect, table layout, server topology, lock mechanisms, independently generated Event IDs/timestamps and operational capabilities.

Forbidden differences include canonical identity, payload meaning, declared ordering, hash-chain validity, reducer/projection state, failure outcomes, Receipt proof fields and exact imported bytes/hashes.

Cross-profile evidence promotes exactly:

```text
NK-SEM-008
NK-ID-008
NK-EQV-002
NK-EQV-003
```

All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

## 🪞 C4 offline shadow evaluation

Package: [`native_kernel.shadow_evaluation`](./native_kernel/shadow_evaluation/README.md)

Protocols:

```text
nk-shadow-workload/1
nk-shadow-report/1
nk-shadow-receipt/1
```

Approved dataset:

```text
dataset_id:      native-kernel/c4-offline-shadow-v1
sha256:          15fb81d8858dcc4e349ffe87c257b25450db026473614582faa7817f90249da3
cases:           15
assertion scope: 45 / 45 C3-supported assertions
approval:        ADR-0020 / Issue #61 / OFFLINE_RECORDED_WORKLOAD_ONLY
```

Evaluation flow:

```text
approved immutable dataset bytes
+ exact C3 prerequisite report
→ validate dataset/protocol/digest
→ enforce SHADOW_ONLY authority boundary
→ compare declared reference/candidate observations
→ separate allowed operational differences
→ compute semantic/critical divergence metrics
→ emit one bounded Shadow Receipt per case
→ emit complete 72-ID C4 report
```

Mandatory authority boundary:

```text
authority promotion:   FORBIDDEN
authoritative writes:  FORBIDDEN
side effects:           FORBIDDEN
promotion decision:    NOT_AUTHORIZED
```

A Shadow Receipt proves only that one recorded case was compared under the recorded dataset digest, fields and limits. It does not approve a candidate or authorize an action.

## ✅ First repository C4 evidence

```text
Evidence head: 97abce685a68e24aec9afab451c009df5783b96b
C4 run:       31187532364 — PASS
P5/C3 run:    31187532391 — PASS
P4 run:       31187532618 — PASS
P1 run:       31187532346 — PASS
Fixtures:     31187532580 — PASS
```

Matrix:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Each retained artifact contains:

```text
postgresql-p4-report.json
sqlite-p5-report.json
c3-equivalence-report.json
c4-shadow-report.json
```

One archive was downloaded and inspected independently:

```text
15 / 15 cases matched
15 Shadow Receipts
45 / 45 C3-supported assertions covered
0 semantic divergences
0 critical divergences
0 missing Receipts
30 declared allowed operational differences
72 assertion results
status: PASS
support_state: PARTIAL
```

Exact artifact digests, defect history and proof limits are recorded in [`docs/ai/C4_IMPLEMENTATION_RECORD.md`](./docs/ai/C4_IMPLEMENTATION_RECORD.md).

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
   ↓
🪞 Non-authoritative shadow observation
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
| **Shadow report** | Comparison of approved recorded observations without authority |
| **Shadow Receipt** | Bounded proof that one declared case was observed and compared |

## 🚫 Explicitly absent

```text
live production traffic capture or replay
authority promotion / candidate approval / automatic action
exhaustive equivalence proof
PostgreSQL/SQLite operational equivalence
complete conflict subsystem
physical/cryptographic deletion execution
restore-before-visibility enforcement
cross-project authority adapter
truth/signature/notarization certification
network API
C5 security/privacy/incident evidence
production security/backup/HA/compliance guarantees
```

## 🧭 Read next

- [`STATUS.md`](./STATUS.md)
- [`ADR-0020`](./docs/adr/0020-authorize-c4-offline-shadow-evaluation.md)
- [`C4 implementation record`](./docs/ai/C4_IMPLEMENTATION_RECORD.md)
- [`C4 implementation details`](./docs/implementation/c4-offline-shadow-evaluation.md)
- [`C4 manifest`](./profiles/shadow-evaluation-v0/c4-manifest.json)
- [`Approved shadow workload`](./contracts/shadow-workload-v1.json)
- [`Conformance model`](./docs/CONFORMANCE_MODEL.md)
- [`P5 implementation record`](./docs/ai/P5_IMPLEMENTATION_RECORD.md)

## ⚖️ Evidence and truth boundary

```text
recorded history ≠ reality itself
integrity commitment ≠ signature
operator approval ≠ empirical evidence
retrieval relevance ≠ truth
C2 reproduction ≠ C3 comparison
C3 comparison ≠ C4 offline observation
C4 observation ≠ authority promotion
Receipt/report ≠ unlimited proof
```

## 🔗 Ecosystem boundary

Native Kernel does not automatically become the memory runtime or authority of other Velantrim projects.

- **Titan** owns cognition, retrieval, tools and orchestration;
- **Mentaury Soul** owns digital individuality and continuity;
- **Crystal** owns verifiable-memory, evidence and product boundaries;
- **Native Kernel** owns neutral semantic memory/Event/evidence contracts and bounded profiles/evidence protocols.

Integration requires separate contracts, authority and evidence.

## 🧭 Next gate

The current publication gate is to repeat C4 and all prerequisite checks on one exact final PR #62 head, inspect final artifacts, review and merge, then reproduce evidence on `main` and synchronize Notion.

C5, live shadowing, production, deletion execution and ecosystem integration require separate explicit authorization.
