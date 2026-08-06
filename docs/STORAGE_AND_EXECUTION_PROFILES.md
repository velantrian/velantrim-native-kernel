# 🐘📦 Storage and Execution Profiles

**[English](./STORAGE_AND_EXECUTION_PROFILES.md) · [Русский](./STORAGE_AND_EXECUTION_PROFILES.ru.md)**

- **Decision status:** `ACCEPTED`
- **Evidence level:** `DOCUMENTED`
- **Implementation status:** `NOT_STARTED`
- **Operator approval:** `APPROVED`
- **Scope:** current implementation-profile direction; not Architecture Canon

> [!IMPORTANT]
> PostgreSQL and SQLite are replaceable present-day implementation profiles. Neither database defines Claim, Event, Relation, epistemic state, conflict, Projection, or Receipt semantics.

## 🧭 The decision in one view

```text
🏛️ Architecture Canon
identity · history · provenance · time · conflict · receipt
                       │
                       ▼
📐 Abstract Storage Contract
append · read history · replay · verify · rebuild · migrate
                       │
          ┌────────────┴─────────────┐
          ▼                          ▼
🐘 PostgreSQL profile          📦 SQLite profile
primary full profile           optional embedded profile
local or remote                local single-file deployment
concurrent/server-oriented     compact/reference/test-oriented
```

The current direction is:

- 🐘 **PostgreSQL is the primary full contemporary storage profile** for a serious local or server deployment.
- 📦 **SQLite remains an optional embedded, portable, reference, test, recovery, or constrained-device profile.**
- 🧪 An in-memory profile may be used for narrow deterministic tests.
- 🌌 Future profiles may use technologies or physical substrates that do not resemble SQL databases.

This is a profile selection, not a permanent statement that PostgreSQL is the architecture.

## 📴 Offline does not mean SQLite

A fully offline workstation may run all required components locally:

```text
💻 One local computer — no Internet required
│
├── 🤖 local small or large model
├── 🧬 Native Kernel implementation
├── 🐘 PostgreSQL on localhost
├── 🔎 local indexes and projections
└── 📁 local documents and model files
```

PostgreSQL is a local server process as well as a network server. A local model can interact with a local Kernel service, and the Kernel can use PostgreSQL through `localhost`, without cloud services or Internet access.

```text
Local model
    │ requests through a declared Kernel interface
    ▼
Native Kernel implementation
    │ storage contract
    ▼
PostgreSQL on localhost
```

Therefore the architecture must not encode the false equivalence:

```text
❌ offline = SQLite
❌ online  = PostgreSQL
```

The more accurate distinction is:

```text
✅ full local/server profile = PostgreSQL
✅ compact embedded profile  = SQLite
```

## ⚙️ Compute profiles and storage profiles are independent

The system must separate two choices:

```text
🧠 Compute Profile
├── local small model
├── local large model
├── remote model
├── symbolic engine
└── future compute substrate

🗄️ Storage Profile
├── PostgreSQL
├── SQLite
├── in-memory test store
└── future storage substrate
```

A local LLM does not require SQLite. A remote model does not require PostgreSQL. Compute selection and storage selection are orthogonal unless a specific implementation profile explicitly documents a constraint.

## 🔀 Profile Selector, not per-request database routing

The active authoritative storage profile should normally be selected at process, node, or deployment startup:

```yaml
storage:
  profile: postgresql
  connection: postgresql://localhost/native_kernel

compute:
  profile: local_model
```

or:

```yaml
storage:
  profile: sqlite
  path: ./native-kernel.db
```

```text
Kernel startup
      ↓
read declared profile
      ↓
construct one Storage Adapter
      ↓
use one authoritative history for that instance
```

A normal request router must not alternate authoritative writes between databases:

```text
❌ request A → SQLite
❌ request B → PostgreSQL
❌ request C → SQLite again
```

That pattern can split history, reorder events, duplicate Claims, and make the source of truth ambiguous.

## 🔄 Switching profiles is a migration

Changing the authoritative storage profile is a controlled substrate migration, not an ordinary routing decision:

```text
1. stop or fence writes
2. record the source position and migration Receipt
3. export authoritative history in a canonical interchange form
4. verify identity, ordering, hashes, provenance, and counts
5. import into the destination profile
6. perform full replay
7. compare declared semantic state
8. activate the destination profile
9. preserve rollback evidence
```

The required result is documented semantic equivalence, not necessarily identical physical bytes:

```text
same authoritative history
        ↓
PostgreSQL reducer path
        ↓
semantic state A

same authoritative history
        ↓
SQLite reducer path
        ↓
semantic state B

required: A ≡ B under a declared conformance rule
```

## 🐘 Why PostgreSQL is the primary full profile

PostgreSQL is a stronger fit when an implementation needs:

- multiple concurrent writers or readers;
- long-running local services;
- multiple agents, processes, users, or devices;
- transactional integrity across related writes;
- roles, permissions, and operational isolation;
- large event histories and complex temporal queries;
- JSON, recursive queries, full-text search, and extensions;
- backup, restore, replication, and operational tooling;
- a path from one local computer to a remote server without changing the semantic contracts.

A capable offline computer that can run a local model can normally also run a local PostgreSQL service. This makes PostgreSQL a reasonable primary laboratory and deployment profile for the full system.

## 📦 Why SQLite remains useful

SQLite is retained for a narrower but valid role:

- embedded desktop or mobile applications;
- compact single-process tools;
- portable snapshots or demonstrations;
- deterministic fixtures and CI tests;
- recovery and diagnostic utilities;
- constrained devices;
- installations where a separate database service is deliberately undesirable.

SQLite is not a degraded statement of the architecture. It is a different operational profile with a smaller concurrency and administration envelope.

## 🧩 Adapter boundary

Kernel semantics should depend on an abstract contract, not SQL dialect details:

```text
StorageContract
├── append_event(...)
├── read_authoritative_history(...)
├── verify_integrity(...)
├── load_projection_source(...)
├── record_migration_receipt(...)
└── expose_declared_capabilities(...)
```

Example implementations may include:

```text
PostgreSQLStorageAdapter
SQLiteStorageAdapter
InMemoryTestAdapter
FutureSubstrateAdapter
```

Backend-generated row IDs, SQL tables, foreign keys, indexes, WAL settings, extensions, and transaction syntax must remain implementation details unless an explicit cross-profile contract promotes a behaviour above the adapter boundary.

## 🔒 Invariants

1. PostgreSQL is the preferred current full profile, not permanent Canon.
2. SQLite is optional and must not be equated with offline operation.
3. One Kernel instance has one declared authoritative history unless a separate distributed-history protocol is explicitly specified.
4. Compute routing must not silently change storage authority.
5. Per-request routing may select compute or retrieval mechanisms, but not alternate authoritative stores without a protocol.
6. Profile migration must be receipted, verifiable, replayable, and reversible where declared.
7. PostgreSQL and SQLite profiles must preserve the same declared semantic contracts.
8. Cache, replica, snapshot, and projection roles must never be confused with authoritative history.
9. A local model may operate entirely offline with local PostgreSQL.
10. Future storage substrates remain admissible through conformance, not by resemblance to SQL.

## 🧪 Required evidence before implementation claims

The repository currently contains no public runtime implementing this decision. A future profile claim should require at least:

- a committed `StorageContract` or equivalent interface;
- one canonical event-history fixture;
- expected reduced semantic state;
- PostgreSQL replay and rebuild tests;
- SQLite replay and rebuild tests if SQLite is claimed;
- cross-profile semantic-equivalence tests;
- migration and rollback tests;
- duplicate, ordering, interruption, and corruption failure cases;
- explicit Receipts for migration and rebuild;
- documented operational limits for each profile.

> One passing PostgreSQL implementation would demonstrate a PostgreSQL profile. It would not by itself prove storage neutrality. Neutrality requires at least one materially different conforming profile or equivalent cross-substrate evidence.

## 🚫 Non-goals

This document does not:

- require PostgreSQL in every implementation;
- require SQLite support in every product;
- define a production schema;
- select a PostgreSQL extension as Canon;
- define distributed consensus or offline multi-writer synchronization;
- claim that a runtime already exists in `main`;
- bind Titan, Crystal, Mentaury, or another project to this profile decision.

## 📚 Related documents

- [`FOUNDATIONAL_INTENT.md`](./FOUNDATIONAL_INTENT.md)
- [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md)
- [`INTEGRATION_BOUNDARIES.md`](./INTEGRATION_BOUNDARIES.md)
- [`adr/0001-architecture-canon-vs-implementation-profiles.md`](./adr/0001-architecture-canon-vs-implementation-profiles.md)
- [`adr/0009-postgresql-primary-sqlite-optional-profile.md`](./adr/0009-postgresql-primary-sqlite-optional-profile.md)
