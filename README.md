<div align="center">

# 🧬 Velantrim Native Kernel

### Technology-neutral contracts and replaceable profiles for verifiable memory

**[English](./README.md) · [Русский](./README.ru.md)**

![Status](https://img.shields.io/badge/status-P1%20PARTIAL-6f42c1)
![Maturity](https://img.shields.io/badge/maturity-RESEARCH-blue)
![Runtime](https://img.shields.io/badge/runtime-SEMANTIC%20CORE%20ONLY-orange)
![Production](https://img.shields.io/badge/production-NOT%20READY-red)

**Claims · Events · Provenance · Time · Conflict visibility · Deterministic reduction · Auditable Receipts**

> **Preserve meaning when technologies change. Verify before promotion.**

</div>

> [!IMPORTANT]
> **Current repository state:** `RESEARCH / P1 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`.  
> A profile-independent semantic core now exists in `main`, but there is still no durable Native Kernel history store, PostgreSQL adapter, projection runtime, network service, C1/C2/C3 profile conformance, or recovered `v0.1.2.1` implementation.

## ⚡ In 30 seconds

Velantrim Native Kernel is an independent, personal, long-horizon architecture and implementation research project.

It studies how memory, recorded change and epistemic state can preserve meaning when databases, programming languages, model providers, processors and future computational substrates change.

```text
🏛️ Architecture Canon
        ↓
📐 Accepted abstract contracts
        ↓
🔌 Replaceable implementation profiles
        ↓
🧪 Reproducible evidence
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
| Foundational contract families | **Accepted** — ADR-0010 |
| Exact identity/event/deletion/fixture contracts | **Accepted** — ADR-0011…0014 |
| Clean PostgreSQL profile plan | **Accepted** — RFC-0002 / ADR-0015 |
| P1 profile-independent semantic core | **Partial implementation; locally tested** |
| PostgreSQL or SQLite adapter | **Not implemented / not authorized** |
| Durable append, idempotency and replay | **Not implemented** |
| Profile C1/C2/C3 | **Not established** |
| Historical `v0.1.2.1` source and original 44 tests | **Not found in accessible sources; Issue #1 remains open** |
| Titan, Mentaury or Crystal integration | **Not active** |
| Production readiness | **Not claimed** |

```text
P1 code exists
≠ complete Kernel runtime
≠ PostgreSQL profile
≠ repository-reproduced C2
≠ storage neutrality
```

## 🧩 What P1 implements

Package: [`native_kernel.semantic_core`](./native_kernel/semantic_core/README.md)

- canonical JSON subset and `nkh1` / `nkc1` / `nkl1` identity helpers;
- immutable semantic content, Claim identity, command and logical Event objects;
- explicit deny-by-default authority decisions;
- deterministic version-bound in-memory reduction;
- deletion/restriction transition semantics;
- admission and deletion Receipt overclaim guards;
- Python 3.11+ standard-library-only implementation.

Local branch evidence recorded for P1:

```text
20 semantic-core tests PASS
4 P1-manifest tests PASS
Python compileall PASS
```

The logical reducer is not an authoritative event store. The local PASS is not GitHub Actions or operational evidence.

## 🚫 What is still absent

```text
PostgreSQL / SQLite adapter
SQL schema and migrations
durable event append
persistent idempotency
writer lease persistence
projection persistence and rebuild
network API
profile conformance adapter
C1 / C2 / C3
production security, privacy or deletion guarantees
```

P2–P5 require separate operator decisions.

## 🧬 Canon shape

```text
🧩 Claim
   ↓
📜 Append-only Event History
   ↓
🧠 Deterministic State Reconstruction
   ↓
🗂️ Rebuildable Projections
   ↓
🎯 Task-Specific Context Selection
   ↓
🧾 Auditable Receipt
```

| Component | Meaning |
|---|---|
| **Claim** | Stable semantic identity; existence does not establish truth |
| **Event** | Explicit record of a command-admitted change |
| **Reducer** | Deterministically derives state from declared history/version |
| **Projection** | Disposable read model that must be rebuildable |
| **Receipt** | Declares processing evidence, omissions and proof limits |

Accepted Event vocabulary remains deliberately small:

```text
ADMIT · LINK · UTILIZED · SUPERSEDED · ERASED
```

## 🏗️ Architecture layers

### Architecture Canon

Meaning that should survive technology replacement: identity roles, provenance, time, conflict visibility, authority boundaries and Receipt semantics.

### Abstract contracts

Versioned behavioural obligations such as `nk-id/1.0`, `nk-event/1.0`, `nk-deletion/1.0` and `nk-fixtures/1.0`.

### Implementation profiles

Concrete laboratory realizations. PostgreSQL is the accepted preferred full profile direction; SQLite remains optional for embedded/portable research. Neither is Canon.

### Evidence

Code presence, local tests, repository CI, cross-profile comparison, Shadow evaluation and operational evidence are separate promotion levels.

## 🐘 Clean PostgreSQL profile lineage

```text
Profile ID:       native-kernel/postgresql-reference
Evidence lineage: clean/postgresql-reference/0.1
Current phase:    P1
```

Implementation plan:

```text
P0 — accepted RFC and planning manifest             COMPLETE
P1 — profile-independent semantic core              PARTIAL / LOCALLY_TESTED
P2 — PostgreSQL append/idempotency adapter           BLOCKED / SEPARATE GO
P3 — replay, projections, deletion work, Receipts    BLOCKED
P4 — conformance adapter and repository evidence     BLOCKED
P5 — independent SQLite profile for C3 research      BLOCKED
```

Read [`RFC-0002`](./docs/rfc/0002-postgresql-reference-profile-v0.md), [`ADR-0015`](./docs/adr/0015-accept-clean-profile-and-authorize-p1-semantic-core.md), and [`profiles/README.md`](./profiles/README.md).

## 🔒 Source-recovery boundary

The reported external checkpoint remains:

```text
v0.1.2.1
44 deterministic tests reported externally
source and original suite not located in accessible sources
```

Clean P1 work is not recovered history:

```text
clean/postgresql-reference/0.1
≠ v0.1.2.1
≠ original 44-test evidence
≠ declaration that the source is globally lost
```

See [Issue #1](https://github.com/velantrian/velantrim-native-kernel/issues/1).

## 🌐 Ecosystem boundaries

- **Native Kernel** — semantic memory/event/replay contract research;
- **Titan** — cognition, retrieval, tools and orchestration in its own project;
- **Mentaury Soul** — digital individuality and continuity in its own project;
- **Crystal** — verifiable memory, evidence and audit in its own project.

Cross-links do not create one runtime, database, identity authority or Canon.

## 🧪 Validation

P1 commands:

```bash
python -m unittest discover -s tests -p 'test_semantic_core.py' -v
python -m unittest discover -s tests -p 'test_p1_manifest.py' -v
python -m compileall -q native_kernel
python tools/profiles/validate_p1_manifest.py
```

Contract fixture tooling remains separate:

```bash
python -m unittest discover -s tests -p 'test_conformance_runner.py' -v
python tools/conformance/runner.py validate
```

A missing GitHub Actions run is recorded as `NOT_RECORDED`, never as PASS.

## 📚 Repository map

| Path | Purpose |
|---|---|
| [`STATUS.md`](./STATUS.md) | authoritative current maturity/evidence boundary |
| [`ARCHITECTURE.md`](./ARCHITECTURE.md) | Canon shape and invariants |
| [`docs/contracts/`](./docs/contracts/) | accepted exact contracts |
| [`contracts/`](./contracts/) | registry, schemas and fixtures |
| [`native_kernel/semantic_core/`](./native_kernel/semantic_core/) | bounded P1 implementation |
| [`profiles/`](./profiles/) | planning and implementation manifests |
| [`docs/adr/`](./docs/adr/) | durable decisions |
| [`docs/rfc/`](./docs/rfc/) | bounded research/profile specifications |
| [`docs/ai/`](./docs/ai/) | current state, risks, map and work log |
| [`prototype/`](./prototype/) | source-recovery boundary, not reconstructed runtime |

## 🛣️ Next gates

1. merge and reproduce P1 workflow evidence at an exact SHA;
2. keep all assertion-level runtime support `UNSUPPORTED` until a conformance adapter exists;
3. decide Issue #18 publication/licensing terms;
4. require a separate operator GO before P2 PostgreSQL work;
5. preserve Issue #1 and ecosystem separation;
6. require an independently developed second profile before C3.

## ⚖️ License

The repository is public but currently has no open-source license. Public visibility alone does not grant permission to copy, modify, redistribute or deploy the material. See [Issue #18](https://github.com/velantrian/velantrim-native-kernel/issues/18).

---

**[English](./README.md) · [Русский](./README.ru.md)**
