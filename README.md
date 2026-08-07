<div align="center">

# 🧬 Velantrim Native Kernel

### Technology-neutral contracts and replaceable profiles for verifiable memory

**[English](./README.md) · [Русский](./README.ru.md)**

![Status](https://img.shields.io/badge/status-P4%20PARTIAL-6f42c1)
![Evidence](https://img.shields.io/badge/evidence-C2%20ASSERTION--SCOPED-blue)
![Profile](https://img.shields.io/badge/profile-PostgreSQL-orange)
![Production](https://img.shields.io/badge/production-NOT%20READY-red)

**Claims · Events · Provenance · Time · Conflict visibility · Deterministic reduction · Auditable evidence**

> **Preserve meaning when technologies change. Verify before promotion.**

</div>

> [!IMPORTANT]
> **Current branch state:** `RESEARCH / P4 PARTIAL ASSERTION CONFORMANCE / NOT PRODUCTION-READY`.  
> P1–P3 implement a bounded semantic and PostgreSQL profile. P4 now emits a complete 72-assertion report: **41 `SUPPORTED`, 13 `PARTIAL`, 18 `UNSUPPORTED`, 0 `FAILED`**. Repository C2 evidence exists for the 41 supported results only. P5/C3, physical deletion, truth/authenticity certification and production guarantees remain absent.

## ⚡ In 30 seconds

Velantrim Native Kernel is an independent, long-horizon architecture and implementation research project.

It studies how memory, recorded change and evidence can preserve meaning when databases, languages, models, processors and future computational substrates change.

```text
🏛️ Architecture Canon
        ↓
📐 Accepted abstract contracts
        ↓
🔌 Replaceable implementation profiles
        ↓
🧪 Assertion-scoped reproducible evidence
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
| Clean PostgreSQL profile | **Accepted** — RFC-0002 / ADR-0015 |
| P1 semantic core | **Partial implementation; repository-tested** |
| P2 PostgreSQL append/idempotency | **Partial implementation; repository-integration-tested** |
| P3 persisted replay/projections/Receipts | **Partial implementation; repository-integration-tested** |
| P4 assertion-scoped adapter | **Partial implementation; C2 repository-reproduced on evidence head** |
| P4 support map | **41 supported / 13 partial / 18 unsupported / 0 failed** |
| P5 independent SQLite profile | **Not implemented / not authorized** |
| C3 cross-profile equivalence | **Not established** |
| Physical/cryptographic deletion execution | **Not implemented** |
| Historical `v0.1.2.1` source and original 44 tests | **Not found in accessible sources; Issue #1 open** |
| Titan, Mentaury or Crystal runtime integration | **Not active** |
| Production readiness | **Not claimed** |

```text
P4 C2 for 41 SUPPORTED assertions
≠ all 72 assertions supported
≠ C3
≠ storage neutrality
≠ truth or authenticity
≠ physical deletion
≠ production readiness
```

## 🧩 P1 — semantic core

Package: [`native_kernel.semantic_core`](./native_kernel/semantic_core/README.md)

- canonical JSON subset and `nkh1` / `nkc1` / `nkl1` identifiers;
- immutable semantic content, Claim identity, Command and logical Event objects;
- explicit deny-by-default authority;
- deterministic version-bound reduction;
- deletion/restriction transition semantics;
- admission/deletion Receipt overclaim guards;
- deterministic upcaster registry and canonical state decoder;
- standard-library-only semantic layer.

## 🐘 P2 — authoritative PostgreSQL append

Package: [`native_kernel.postgresql_profile`](./native_kernel/postgresql_profile/README.md)

```text
explicit authority
→ writer owner/epoch fence
→ scoped durable idempotency
→ rollback-safe sequence allocation
→ atomic Event + idempotency commit
→ canonical payload/envelope commitments
```

Profile technologies:

- PostgreSQL `16–18`;
- Psycopg `>=3.3,<3.4`;
- Python `>=3.11,<3.13`;
- numbered SQL migrations with a SHA-256 ledger;
- one writer lease per Kernel instance.

These are replaceable profile choices, not Canon.

## 🔁 P3 — replay, projections and operational Receipts

```text
authoritative PostgreSQL Events
→ repeatable-read verified snapshot
→ explicit schema upcasting
→ P1 reduction from empty state
→ bounded Replay Receipt
→ locked head comparison
→ disposable projection rebuild
→ bounded Projection Rebuild Receipt
```

P3 provides:

- full selected-instance replay from sequence `1`;
- canonical Event and global hash-chain checks;
- explicit failures for unsupported schema paths;
- deterministic projection destroy/rebuild;
- monotonic committed generation;
- stale-head rejection;
- atomic Receipt + projection publication;
- projection-to-Receipt consistency verification;
- explicit non-claims for truth, external authenticity, complete integrity and physical erasure.

## 🧪 P4 — assertion-scoped conformance

P4 connects executable behavior to all 72 registry IDs:

```text
registry + fixtures
→ semantic checks
→ PostgreSQL checks
→ one result for every assertion
→ passed check IDs + limitations
→ strict independent validation
→ JSON evidence artifact
```

Current result map:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
```

Every `SUPPORTED` or `PARTIAL` result references one or more passed checks and states limitations. Missing, duplicate, unknown or untraceable results fail validation.

All `NK-EPI-001…008` assertions remain `UNSUPPORTED` because their registry decision remains `PROPOSED`.

### C1 / C2 boundary

- `C1 / LOCALLY_TESTED` — commands and failures were exercised locally;
- `C2 / REPOSITORY_REPRODUCED` — the exact implementation/environment was reproduced in repository CI with artifacts;
- `C3` — requires a materially independent second profile and comparison evidence.

The report remains:

```text
support_state: PARTIAL
kernel_runtime_conformance: C2
```

This means C2 for the **41 supported results**, not full support for the profile.

## ✅ Initial P4 repository evidence

Evidence head:

```text
93710131fffdea7d9a586cc05e7f258c07fae707
```

Workflow:

```text
P4 run 31175767586 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
P1/P2/P3 regressions — PASS
4 JSON evidence artifacts — retained
```

Each P4 matrix job generated and validated a C2 report, ran the P1–P3 regression suites, compiled the implementation and uploaded a profile-specific artifact.

Exact artifact digests and limitations are recorded in [`docs/ai/P4_IMPLEMENTATION_RECORD.md`](./docs/ai/P4_IMPLEMENTATION_RECORD.md).

## 🚫 Explicitly absent

```text
P5 independent SQLite profile
C3 cross-profile equivalence
complete conflict subsystem
physical/cryptographic deletion execution
restore-before-visibility enforcement
cross-project authority adapter
truth/signature/notarization certification
network API
C4/C5
production security/privacy/backup/HA/compliance guarantees
```

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
| **Evidence report** | Assertion-by-assertion support state and check traceability |

Accepted Event vocabulary remains deliberately small:

```text
ADMIT · LINK · UTILIZED · SUPERSEDED · ERASED
```

## 🐘 Clean profile lineage

```text
Profile ID:       native-kernel/postgresql-reference
Profile version:  0.4-p4
Evidence lineage: clean/postgresql-reference/0.1
```

```text
P0 — RFC and planning manifest                     COMPLETE
P1 — semantic core                                MERGED
P2 — PostgreSQL append/idempotency                 MERGED
P3 — replay/projections/Receipts                   MERGED
P4 — assertion-scoped conformance                  ACTIVE / PARTIAL / C2 EVIDENCE
P5 — independent SQLite profile / C3 research      BLOCKED / SEPARATE GO
```

Read:

- [`STATUS.md`](./STATUS.md)
- [`RFC-0002`](./docs/rfc/0002-postgresql-reference-profile-v0.md)
- [`ADR-0018`](./docs/adr/0018-authorize-p4-assertion-scoped-conformance.md)
- [`P4 implementation record`](./docs/ai/P4_IMPLEMENTATION_RECORD.md)
- [`Conformance model`](./docs/CONFORMANCE_MODEL.md)
- [`Profile manifests`](./profiles/postgresql-reference-v0/)

## ⚖️ Evidence and truth boundary

```text
recorded history ≠ reality itself
integrity commitment ≠ signature
operator approval ≠ empirical evidence
retrieval relevance ≠ truth
C2 reproduction ≠ C3 equivalence
Receipt/report ≠ unlimited proof
```

## 🔗 Ecosystem boundary

Native Kernel does not automatically become the memory runtime or authority of other Velantrim projects.

- **Titan** owns cognition, retrieval, tools and orchestration;
- **Mentaury Soul** owns digital individuality and continuity;
- **Crystal** owns verifiable-memory, evidence and grant-facing product boundaries;
- **Native Kernel** owns neutral semantic memory/Event/evidence contracts and bounded implementation profiles.

Integration requires separate contracts, authority and evidence.

## 🧭 Next gate

P5 and any C3 claim require a new explicit operator GO, a materially independent SQLite profile and declared semantic-equivalence comparison. P4 does not authorize that work.
