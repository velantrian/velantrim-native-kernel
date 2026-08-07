<div align="center">

# 🧬 Velantrim Native Kernel

### Technology-neutral contracts and replaceable profiles for verifiable memory

**[English](./README.md) · [Русский](./README.ru.md)**

![Status](https://img.shields.io/badge/status-P2%20PARTIAL-6f42c1)
![Maturity](https://img.shields.io/badge/maturity-RESEARCH-blue)
![Runtime](https://img.shields.io/badge/runtime-APPEND%20PROFILE-orange)
![Production](https://img.shields.io/badge/production-NOT%20READY-red)

**Claims · Events · Provenance · Time · Conflict visibility · Deterministic reduction · Auditable Receipts**

> **Preserve meaning when technologies change. Verify before promotion.**

</div>

> [!IMPORTANT]
> **Current repository state:** `RESEARCH / P2 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`.  
> The profile-independent P1 semantic core and bounded P2 PostgreSQL append/idempotency profile exist. P2 integration is repository-reproduced on PostgreSQL 16/18 × Python 3.11/3.12. Replay/projections, operational deletion, assertion-level conformance, C1/C2/C3 and production guarantees remain absent.

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
| P1 profile-independent semantic core | **Partial implementation; repository-tested** |
| P2 PostgreSQL append/idempotency | **Partial implementation; repository-integration-tested** |
| Replay, projections and operational Receipts | **Not implemented / P3 not authorized** |
| Profile conformance adapter | **Not implemented / P4 not authorized** |
| Profile C1/C2/C3 | **Not established** |
| Historical `v0.1.2.1` source and original 44 tests | **Not found in accessible sources; Issue #1 remains open** |
| Titan, Mentaury or Crystal integration | **Not active** |
| Production readiness | **Not claimed** |

```text
P2 PostgreSQL integration PASS
≠ complete Kernel runtime
≠ replay/projection runtime
≠ assertion-level conformance
≠ C1/C2/C3
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
- Python standard-library-only implementation.

## 🐘 What P2 implements

Package: [`native_kernel.postgresql_profile`](./native_kernel/postgresql_profile/README.md)

```text
explicit authority
→ DB-backed writer owner/epoch fence
→ durable scoped idempotency
→ rollback-safe global and stream counters
→ atomic Event + idempotency commit
→ canonical payload/envelope bytes
→ nkp1 / nke1 integrity chain
```

Profile choices:

- PostgreSQL `16–18`;
- Psycopg `>=3.3,<3.4`, loaded lazily;
- Python `>=3.11,<3.13`;
- numbered SQL migrations with a SHA-256 ledger;
- one authoritative writer lease per Kernel instance.

These are replaceable profile technologies, not Canon.

## 🧪 P2 repository evidence

PR #47 evidence head `e80492bcacde2ff2be3a2ee03aa5aa53a714d288`:

```text
P2 workflow run 31151297646 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
AI context integrity run 31151298002 — PASS
P1 semantic core — PASS
Conformance fixture integrity — PASS
```

Each P2 matrix job passed:

- 9 P2 unit tests;
- 5 PostgreSQL integration tests;
- 5 P2 manifest tests;
- manifest validation and compileall.

The integration suite covers migration idempotency, writer fencing, append/retry/conflict atomicity, rollback-safe sequence reuse and concurrent same-digest append.

## 🚫 What is still absent

```text
P3 replay and upcaster execution
projection persistence and rebuild
operational replay/deletion Receipts
physical or cryptographic deletion execution
network API
P4 assertion-scoped conformance adapter
P5 independent SQLite profile
C1 / C2 / C3
production security, privacy, backup, HA or compliance guarantees
```

P3–P5 require separate operator decisions.

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

Concrete laboratory realizations. PostgreSQL is the accepted preferred full-profile direction; SQLite remains optional for embedded/portable research. Neither is Canon.

### Evidence

Code presence, local tests, repository CI, cross-profile comparison, Shadow evaluation and operational evidence are separate promotion levels.

## 🐘 Clean PostgreSQL profile lineage

```text
Profile ID:       native-kernel/postgresql-reference
Evidence lineage: clean/postgresql-reference/0.1
Current phase:    P2
```

Implementation plan:

```text
P0 — accepted RFC and planning manifest             COMPLETE
P1 — profile-independent semantic core              MERGED / REPOSITORY-TESTED
P2 — PostgreSQL append/idempotency adapter           PARTIAL / INTEGRATION-TESTED
P3 — replay, projections, deletion work, Receipts    BLOCKED / SEPARATE GO
P4 — conformance adapter and assertion evidence      BLOCKED / SEPARATE GO
P5 — independent SQLite profile for C3 research      BLOCKED / SEPARATE GO
```

Read [`RFC-0002`](./docs/rfc/0002-postgresql-reference-profile-v0.md), [`ADR-0015`](./docs/adr/0015-accept-clean-profile-and-authorize-p1-semantic-core.md), [`ADR-0016`](./docs/adr/0016-authorize-p2-postgresql-append-profile.md), and [`profiles/README.md`](./profiles/README.md).

## 🔒 Source-recovery boundary

The reported external checkpoint remains:

```text
v0.1.2.1
44 deterministic tests reported externally
source and original suite not located in accessible sources
```

Clean profile work is not recovered history:

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

P1:

```bash
python -m unittest discover -s tests -p 'test_semantic_core.py' -v
python -m unittest discover -s tests -p 'test_p1_manifest.py' -v
python tools/profiles/validate_p1_manifest.py
```

P2 unit and manifest checks:

```bash
python -m unittest discover -s tests -p 'test_postgresql_profile_unit.py' -v
python -m unittest discover -s tests -p 'test_p2_manifest.py' -v
python tools/profiles/validate_p2_manifest.py
```

P2 PostgreSQL integration:

```bash
python -m pip install -r profiles/postgresql-reference-v0/requirements-p2-ci.txt
NK_TEST_POSTGRES_DSN='postgresql://...' \
  python -m unittest discover -s tests -p 'test_postgresql_profile_integration.py' -v
```

Contract fixture tooling remains separate:

```bash
python -m unittest discover -s tests -p 'test_conformance_runner.py' -v
python tools/conformance/runner.py validate
```

A missing run is recorded as `NOT_RECORDED`, never as PASS.

## 📚 Repository map

| Path | Purpose |
|---|---|
| [`STATUS.md`](./STATUS.md) | authoritative current maturity/evidence boundary |
| [`ARCHITECTURE.md`](./ARCHITECTURE.md) | Canon shape and invariants |
| [`docs/contracts/`](./docs/contracts/) | accepted exact contracts |
| [`contracts/`](./contracts/) | registry, schemas and fixtures |
| [`native_kernel/semantic_core/`](./native_kernel/semantic_core/) | bounded P1 implementation |
| [`native_kernel/postgresql_profile/`](./native_kernel/postgresql_profile/) | bounded P2 PostgreSQL profile |
| [`profiles/`](./profiles/) | planning and implementation manifests |
| [`docs/adr/`](./docs/adr/) | durable decisions |
| [`docs/rfc/`](./docs/rfc/) | bounded research/profile specifications |
| [`docs/ai/`](./docs/ai/) | current state, risks, map and work log |
| [`prototype/`](./prototype/) | source-recovery boundary, not reconstructed runtime |

## 🛣️ Next gates

1. merge PR #47 only after same-head P2 and AI-context checks pass;
2. keep all assertion-level runtime support `UNSUPPORTED` until P4;
3. decide Issue #18 publication/licensing terms;
4. require separate operator GO before P3;
5. preserve Issue #1 and ecosystem separation;
6. require an independently developed second profile before C3.

## ⚖️ License

The repository is public but currently has no open-source license. Public visibility alone does not grant permission to copy, modify, redistribute or deploy the material. See [Issue #18](https://github.com/velantrian/velantrim-native-kernel/issues/18).

---

**[English](./README.md) · [Русский](./README.ru.md)**
