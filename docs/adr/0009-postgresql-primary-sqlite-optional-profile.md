# ADR-0009: PostgreSQL is the primary full profile and SQLite is optional

- **Decision status:** `ACCEPTED`
- **Evidence level:** `DOCUMENTED`
- **Implementation status:** `NOT_STARTED`
- **Operator approval:** `APPROVED`
- **Date:** `2026-08-06`
- **Deciders:** `@velantrian`
- **Track:** `Implementation Profile`
- **Related:** `ADR-0001`, `CONFORMANCE_MODEL.md`, `STORAGE_AND_EXECUTION_PROFILES.md`
- **Tags:** `storage, postgresql, sqlite, offline, profile-selection, migration`

> [!NOTE]
> This decision prevents three recurring confusions: that offline operation requires SQLite, that PostgreSQL is only a remote paid service, and that a request router may freely alternate authoritative writes between databases.

## Context 🧭

Native Kernel is intended to preserve semantic meaning independently from one database or compute technology. The project still needs concrete contemporary profiles to test contracts.

A capable local computer may run a local model, a local Kernel implementation, and PostgreSQL on `localhost` without Internet access. Therefore `offline = SQLite` is not a valid architectural assumption.

PostgreSQL provides a stronger full-system profile for concurrency, transactions, roles, long-running services, temporal queries, backup, restore, and a later transition from local deployment to a server deployment. SQLite remains valuable where embedding, portability, a single-file database, testing, recovery, or constrained operation matters.

- **Problem:** choose a clear present-day storage-profile direction without turning a database into Canon.
- **Constraints:** public Kernel runtime is not currently present in `main`; semantic neutrality remains unproven; Issue #1 import scope must not expand.
- **Non-goals:** production schema, distributed consensus, offline multi-writer synchronization, or mandatory support for every profile.
- **Current implementation boundary:** documentation only.
- **Source-derived facts:** PostgreSQL and SQLite are already described as replaceable implementation candidates; the Canon is storage-independent.
- **Open uncertainty:** future operational limits, migration format, conformance fixtures, and profile capability negotiation remain to be implemented and tested.

## Inputs considered 🔍

```text
Repository evidence:
- ADR-0001 separates Architecture Canon from Implementation Profiles.
- CONFORMANCE_MODEL requires declared semantic equivalence across profiles.
- main currently contains documentation, not a public Kernel runtime.

Operator interpretation:
- PostgreSQL can be run locally and offline.
- a local LLM can work with local PostgreSQL.
- SQLite should remain available as a narrower optional profile.

AI-generated inputs:
- use a startup/deployment Profile Selector rather than per-request database routing.
- treat a storage change as a controlled migration with replay and Receipts.
```

AI-generated inputs are design inputs, not implementation evidence.

## Decision drivers 🎯

- semantic durability;
- local-first and offline operation;
- concurrency and transactional integrity;
- portability across local and server deployment;
- explicit migration and rollback;
- conformance testability;
- minimal coupling between compute and storage;
- preservation of compact embedded deployments.

## Considered options 🧪

### Option A — SQLite as the default offline profile

**Advantages**

- simple installation;
- one-file portability;
- embedded operation.

**Disadvantages**

- falsely couples offline operation to SQLite;
- provides a narrower concurrency and operational envelope;
- makes later full-system growth more likely to require a profile transition.

### Option B — PostgreSQL as the only supported profile

**Advantages**

- one implementation path;
- strong full-system capabilities.

**Disadvantages**

- removes valid embedded, test, recovery, and constrained-device use cases;
- weakens evidence that the architecture is independent from one storage implementation;
- risks turning a preferred profile into an accidental definition of the system.

### Option C — PostgreSQL primary, SQLite optional, selected per instance

**Advantages**

- supports serious local and server deployment with one full profile;
- preserves embedded and portable use cases;
- keeps offline operation independent from database choice;
- enables cross-profile conformance testing;
- avoids split authoritative history caused by per-request routing.

**Disadvantages**

- requires adapter discipline;
- requires migration tooling and semantic-equivalence tests;
- supports more than one operational envelope.

## Decision ✅

**We will:**

1. treat PostgreSQL as the preferred current full storage profile for local or server implementations;
2. retain SQLite as an optional embedded, portable, reference, test, recovery, or constrained-device profile;
3. keep compute-profile selection independent from storage-profile selection;
4. select the authoritative storage profile at instance, process, node, or deployment startup;
5. treat an authoritative-profile change as a controlled migration, not an ordinary request-routing decision;
6. require one declared authoritative history per Kernel instance unless a separate distributed-history protocol is specified;
7. require declared cross-profile semantic equivalence before claiming storage neutrality.

**We will not:**

- make PostgreSQL part of Architecture Canon;
- equate offline with SQLite;
- alternate authoritative writes between PostgreSQL and SQLite through a normal request router;
- claim implementation or production evidence before committed runtime tests exist;
- bind Titan, Crystal, Mentaury, or another project to this profile choice automatically.

### One-line rationale

> For a full local-first Kernel that may later operate as a server, PostgreSQL provides the stronger primary contemporary profile while optional SQLite preserves embedded portability, and instance-level selection prevents split authority without promoting either database into Canon.

## Consequences 📌

### Positive

- offline operation can use local PostgreSQL and a local model;
- one profile can serve both serious local and remote deployments;
- SQLite retains a clear, bounded purpose;
- compute routing and storage authority remain separate;
- future conformance work has two materially different SQL profiles to compare.

### Negative / accepted trade-offs

- PostgreSQL requires a local service and more operational setup;
- two profiles increase test and migration obligations;
- the preferred profile may still be mistaken for permanent architecture unless documentation remains explicit.

### Neutral

- no runtime code is added by this ADR;
- Issue #1 controlled source import is unchanged;
- future non-SQL profiles remain possible.

## Invariants 🔒

1. PostgreSQL is a preferred Implementation Profile, not Canon.
2. SQLite is optional and does not define offline operation.
3. A local model may use local PostgreSQL without Internet access.
4. One instance must expose one declared authoritative history.
5. Compute routing must not silently change storage authority.
6. Storage-profile switching requires migration, verification, replay, and a Receipt.
7. Caches, replicas, snapshots, and Projections are not authoritative history.
8. Cross-profile claims require a declared semantic-equivalence rule and committed evidence.

## Architecture-layer placement

| Question | Answer |
|---|---|
| Architecture Canon changed? | `no` |
| Abstract contract changed? | `no`; migration and capability details remain future contract work |
| Implementation profile selected? | `yes` |
| Runtime code exists? | `no` |
| Production evidence exists? | `no` |

## Implementation notes 🔧

Future work should define:

- a storage adapter or capability contract;
- canonical event-history fixtures;
- PostgreSQL and SQLite profile manifests;
- migration Receipts and rollback rules;
- profile capability declaration;
- replay, corruption, interruption, duplicate, and ordering tests;
- explicit operational limits for each profile.

This ADR must not modify the byte-faithful controlled import scope of Issue #1.

## Validation and evidence 🧪

| Evidence | Artifact / command | Result | Required for next level |
|---|---|---|---|
| Documentation | `STORAGE_AND_EXECUTION_PROFILES.md` | decision explained | merged documentation |
| Unit tests | not present | no implementation claim | adapter tests |
| Replay test | not present | no conformance claim | shared fixtures and expected state |
| Migration test | not present | no migration claim | export/import/replay/rollback test |
| Operator approval | direct project decision, 2026-08-06 | approved | recorded in ADR |

## Failure cases 🚨

- a router writes different events to different authoritative databases;
- a local deployment is described as requiring SQLite solely because it is offline;
- backend row IDs become Claim identity;
- PostgreSQL tables or extensions become undocumented semantic contracts;
- a SQLite cache is mistaken for authoritative history;
- profile migration activates before replay and equivalence checks complete;
- one passing PostgreSQL implementation is described as proof of storage neutrality.

## Rollback / supersession

This decision may be superseded if:

- evidence shows a different primary profile better satisfies the declared contracts;
- PostgreSQL imposes unacceptable operational or portability constraints;
- a non-SQL profile becomes the strongest reference implementation;
- the project chooses multiple equal reference profiles instead of one preferred full profile.

Historical event fixtures, Receipts, migration evidence, and semantic-equivalence rules must remain readable after supersession.

## Consistency checklist 🔱

- [x] Event history remains authoritative about recorded changes.
- [x] History is not equated with truth.
- [x] Projection/cache is not promoted to Canon.
- [x] Relevance/utility is not equated with truth.
- [x] Current technology is not silently promoted to permanent architecture.
- [x] Titan and Crystal boundaries remain explicit.
- [x] Issue #1 import scope is not silently expanded.
- [x] Decision status, evidence level, implementation status, and operator approval remain separate.

## References 📚

- [`../STORAGE_AND_EXECUTION_PROFILES.md`](../STORAGE_AND_EXECUTION_PROFILES.md)
- [`0001-architecture-canon-vs-implementation-profiles.md`](./0001-architecture-canon-vs-implementation-profiles.md)
- [`../CONFORMANCE_MODEL.md`](../CONFORMANCE_MODEL.md)
- [`../DECISION_PROCESS.md`](../DECISION_PROCESS.md)
