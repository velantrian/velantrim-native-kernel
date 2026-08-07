<div align="center">

# 🧬 Velantrim Native Kernel

### Technology-neutral contracts and replaceable profiles for verifiable memory

**[English](./README.md) · [Русский](./README.ru.md)**

![Status](https://img.shields.io/badge/status-P3%20PARTIAL-6f42c1)
![Maturity](https://img.shields.io/badge/maturity-RESEARCH-blue)
![Runtime](https://img.shields.io/badge/runtime-REPLAY%20PROFILE-orange)
![Production](https://img.shields.io/badge/production-NOT%20READY-red)

**Claims · Events · Provenance · Time · Conflict visibility · Deterministic reduction · Auditable Receipts**

> **Preserve meaning when technologies change. Verify before promotion.**

</div>

> [!IMPORTANT]
> **Current repository state:** `RESEARCH / P3 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`.  
> P1 semantic reduction, P2 PostgreSQL append/idempotency, and bounded P3 persisted replay/projection rebuild/operational Receipts now exist. P3 integration was reproduced on PostgreSQL 16/18 × Python 3.11/3.12. Physical deletion, P4 assertion-level conformance, P5 independent-profile portability, C1/C2/C3 and production guarantees remain absent.

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
| P3 persisted replay/projection rebuild/Receipts | **Partial implementation; repository-integration-tested** |
| Physical/cryptographic deletion execution | **Not implemented** |
| P4 profile conformance adapter | **Not implemented / not authorized** |
| P5 independent SQLite profile | **Not implemented / not authorized** |
| Profile C1/C2/C3 | **Not established** |
| Historical `v0.1.2.1` source and original 44 tests | **Not found in accessible sources; Issue #1 remains open** |
| Titan, Mentaury or Crystal integration | **Not active** |
| Production readiness | **Not claimed** |

```text
P3 replay/projection integration PASS
≠ complete Kernel runtime
≠ physical deletion
≠ assertion-level conformance
≠ C1/C2/C3
≠ storage neutrality
≠ production readiness
```

## 🧩 What P1 implements

Package: [`native_kernel.semantic_core`](./native_kernel/semantic_core/README.md)

- canonical JSON subset and `nkh1` / `nkc1` / `nkl1` identity helpers;
- immutable semantic content, Claim identity, Command and logical Event objects;
- explicit deny-by-default authority decisions;
- deterministic version-bound reduction;
- deletion/restriction transition semantics;
- admission/deletion Receipt overclaim guards;
- standard-library deterministic upcaster registry and canonical state decoder;
- Python standard-library-only semantic layer.

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

## 🔁 What P3 implements

```text
authoritative PostgreSQL Events
→ repeatable-read snapshot
→ canonical payload/envelope checks
→ Event count, global/stream sequence and hash-chain checks
→ explicit upcaster path
→ P1 reducer from empty state
→ bounded Replay Receipt
→ locked authoritative-head comparison
→ disposable projection rebuild
→ bounded Projection Rebuild Receipt
```

P3 adds:

- replay of the full selected instance history from sequence `1`;
- explicit identity/multi-step schema upcaster routing;
- failure on missing, ambiguous, cyclic or invalid upcaster paths;
- deterministic state digest reconstruction;
- disposable `semantic-state` projection persistence;
- projection destroy and deterministic rebuild;
- monotonic projection generation through committed rebuild Receipts;
- stale-head rejection before projection publication;
- transactional rollback if Receipt/projection publication fails;
- canonical persisted Replay and Projection Rebuild Receipts;
- hard non-claims for truth, external authenticity, complete integrity, physical erasure and C-levels.

The hash chain and replay checks are bounded integrity evidence. They are not signatures, consensus, external notarization or protection from every privileged database rewrite.

## 🧪 Repository evidence

### P2 final-head evidence

```text
PR #47 final head: 36ddb1d0342914f0c06fe7f31171bac06565ee72
P2 run 31152380799 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
```

### P3 initial executable-head evidence

```text
PR #50 executable head: 0f8fd4ffe5d5fb0d4bc01f3e441a053f691dbba3
P3 run 31171581859 — PASS
P2 regression run 31171581795 — PASS
P1 semantic core run 31171581787 — PASS
Fixture integrity run 31171581791 — PASS
```

P3 passed PostgreSQL `16/18 × Python 3.11/3.12`. Every P3 job ran:

- 5 semantic unit tests;
- 5 P3 manifest tests and validator;
- 7 PostgreSQL replay/projection/Receipt integration scenarios;
- the P2 unit/integration regression suite;
- compileall.

The final PR head must repeat affected checks after documentation/evidence changes. Earlier PASS remains evidence only for its exact SHA.

## 🚫 What is still absent

```text
physical or cryptographic deletion execution
backup/export/provider/key erasure evidence
network API
P4 assertion-scoped conformance adapter
P5 independent SQLite profile
C1 / C2 / C3
production credentials, security, privacy, backup, HA or compliance guarantees
```

P4–P5 require separate operator decisions.

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

Concrete laboratory realizations. PostgreSQL is the accepted preferred full-profile direction; SQLite remains optional for independent embedded/portable research. Neither is Canon.

### Evidence

Code presence, local tests, repository CI, assertion-scoped conformance, cross-profile comparison, Shadow evaluation and operational evidence are separate promotion levels.

## 🐘 Clean PostgreSQL profile lineage

```text
Profile ID:       native-kernel/postgresql-reference
Evidence lineage: clean/postgresql-reference/0.1
Current phase:    P3
```

Implementation plan:

```text
P0 — accepted RFC and planning manifest             COMPLETE
P1 — profile-independent semantic core              MERGED / REPOSITORY-TESTED
P2 — PostgreSQL append/idempotency adapter           PARTIAL / INTEGRATION-TESTED
P3 — replay, projection rebuild and Receipts         PARTIAL / INTEGRATION-TESTED
P4 — conformance adapter and assertion evidence      BLOCKED / SEPARATE GO
P5 — independent SQLite profile for C3 research      BLOCKED / SEPARATE GO
```

Read [`RFC-0002`](./docs/rfc/0002-postgresql-reference-profile-v0.md), [`ADR-0015`](./docs/adr/0015-accept-clean-profile-and-authorize-p1-semantic-core.md), [`ADR-0016`](./docs/adr/0016-authorize-p2-postgresql-append-profile.md), [`ADR-0017`](./docs/adr/0017-authorize-p3-replay-projection-receipts.md), and [`profiles/README.md`](./profiles/README.md).

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

- **Native Kernel** — semantic memory, Event, replay and evidence-profile research;
- **Titan** — cognition, retrieval, tools and orchestration in its own project;
- **Mentaury Soul** — digital individuality and continuity in its own project;
- **Crystal** — verifiable memory, evidence and audit in its own project.

Cross-links do not create one runtime, database, identity authority or Canon.

## 🧪 Validation

P3 semantic and manifest checks:

```bash
python -m unittest discover -s tests -p 'test_p3_semantic.py' -v
python -m unittest discover -s tests -p 'test_p3_manifest.py' -v
python tools/profiles/validate_p3_manifest.py
```

P3 PostgreSQL integration:

```bash
python -m pip install -r profiles/postgresql-reference-v0/requirements-p2-ci.txt
NK_TEST_POSTGRES_DSN='postgresql://...' \
  python -m unittest discover -s tests -p 'test_p3_postgresql_integration.py' -v
```

P2 and contract fixture tooling remain separate regression/evidence surfaces. A missing run is recorded as `NOT_RECORDED`, never as PASS.

## 📚 Repository map

| Path | Purpose |
|---|---|
| [`STATUS.md`](./STATUS.md) | authoritative current maturity/evidence boundary |
| [`ARCHITECTURE.md`](./ARCHITECTURE.md) | Canon shape and invariants |
| [`docs/contracts/`](./docs/contracts/) | accepted exact contracts |
| [`contracts/`](./contracts/) | registry, schemas and fixtures |
| [`native_kernel/semantic_core/`](./native_kernel/semantic_core/) | P1 semantics plus P3 standard-library schema helpers |
| [`native_kernel/postgresql_profile/`](./native_kernel/postgresql_profile/) | bounded P2/P3 PostgreSQL profile |
| [`profiles/`](./profiles/) | P0/P1/P2/P3 manifests |
| [`docs/adr/`](./docs/adr/) | durable decisions |
| [`docs/rfc/`](./docs/rfc/) | bounded research/profile specifications |
| [`docs/ai/`](./docs/ai/) | current state, risks, map and work log |
| [`prototype/`](./prototype/) | source-recovery boundary, not reconstructed runtime |

## 🛣️ Next gates

1. complete same-final-head P3, P2, P1, fixture and AI-context checks;
2. keep all assertion-level runtime support `UNSUPPORTED` until P4;
3. require separate operator GO before P4;
4. decide Issue #18 publication/licensing terms;
5. preserve Issue #1 and ecosystem separation;
6. require a materially independent second profile before C3.

## ⚖️ License

The repository is public but currently has no open-source license. Public visibility alone does not grant permission to copy, modify, redistribute or deploy the material. See [Issue #18](https://github.com/velantrian/velantrim-native-kernel/issues/18).

---

**[English](./README.md) · [Русский](./README.ru.md)**
