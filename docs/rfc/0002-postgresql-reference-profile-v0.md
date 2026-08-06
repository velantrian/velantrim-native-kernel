# RFC-0002: PostgreSQL Reference Profile v0 Planning Contract

- **RFC status:** `ACCEPTED`
- **Evidence level:** `LOCALLY_TESTED — P1 ONLY`
- **Implementation status:** `PARTIAL — P1 SEMANTIC CORE`
- **Operator approval:** `APPROVED`
- **Profile ID:** `native-kernel/postgresql-reference`
- **Planning version:** `nk-pg-profile/0.1`
- **Current implementation version:** `0.1-p1`
- **Evidence lineage:** `clean/postgresql-reference/0.1`
- **Related:** Issue #40, Issue #43, ADR-0001, ADR-0009, ADR-0011…0015

## 1. Purpose and current decision

Define the first clean Native Kernel implementation profile that can implement accepted contracts using PostgreSQL without turning PostgreSQL, Python, SQL tables, or current hardware into Architecture Canon.

The operator accepted the clean lineage and authorized only P1:

```text
accepted architecture contracts
        ↓
accepted clean profile plan
        ↓
P1 profile-independent semantic core — implemented and locally tested
        ↓
P2 PostgreSQL adapter — blocked by separate GO
        ↓
P3 replay/projections/Receipts — blocked
        ↓
P4 conformance adapter/CI — blocked
        ↓
P5 independent SQLite profile — blocked
```

Acceptance of this RFC does not authorize later phases or establish profile conformance.

## 2. Lineage boundary

```text
native-kernel/postgresql-reference
≠ recovered v0.1.2.1
≠ original 44-test suite
≠ historical prototype continuation
```

The profile uses a new clean evidence lineage. Issue #1 remains active and independent. Nothing in this RFC declares the historical source globally lost or replaces its provenance requirements.

Every implementation artifact must identify profile/version, source commit, registry version, environment, commands, evidence level, unsupported assertions and known limits.

## 3. Accepted inputs

| Input | Required meaning |
|---|---|
| ADR-0001 | Canon is separate from implementation profiles |
| ADR-0009 | PostgreSQL is the preferred full profile; SQLite remains optional |
| ADR-0011 / `nk-id/1.0` | canonical identity and migration/collision rules |
| ADR-0012 / `nk-event/1.0` | single-writer append, idempotency, order and replay boundary |
| ADR-0013 / `nk-deletion/1.0` | deletion, restriction, retention and proof limits |
| ADR-0014 / `nk-fixtures/1.0` | executable fixture and evidence protocol |
| ADR-0015 | clean lineage accepted; bounded P1 implementation authorized |
| registry `1.1.0` | stable assertion IDs and statuses |

`NK-EPI-001…008` and ADR-0008 remain proposed. P1 does not implement or promote them.

## 4. Current reality status

```text
RFC/profile plan:              ACCEPTED / APPROVED
P1 semantic core:              PARTIAL / LOCALLY_TESTED
PostgreSQL adapter:            NOT_STARTED / NOT_AUTHORIZED
Durable authoritative history: NOT_IMPLEMENTED
Kernel runtime conformance:    UNSUPPORTED
C1/C2/C3:                      NOT_ESTABLISHED
Repository Actions result:     NOT_RECORDED
```

P1 local evidence:

```text
20 semantic-core tests PASS
4 P1-manifest tests PASS
Python compileall PASS
standard-library-only boundary verified
```

Local test success proves only the declared P1 code paths.

## 5. Profile architecture

```text
Command API
   ↓
Command canonicalization + validation       ← P1 partial
   ↓
Authority port                              ← P1 deterministic local adapter
   ↓
Append service                              ← P2 absent
   ↓
PostgreSQL authoritative-history adapter    ← P2 absent
   ↓
Reducer + upcaster registry                 ← P1 reducer core partial
   ↓
Disposable projections                     ← P3 absent
   ↓
Receipt/evidence emitter                    ← P1 proof guards partial
   ↓
Conformance adapter                         ← P4 absent
```

### 5.1 Implemented P1 semantic core

Package: `native_kernel.semantic_core`.

Implemented with Python 3.11+ standard library only:

- `nk-id/1.0` canonical JSON subset and `nkh1`/`nkc1`/`nkl1` helpers;
- immutable semantic content, Claim identity, command and logical Event objects;
- explicit deny-by-default authority policy;
- deterministic version-bound in-memory reducer;
- deletion/restriction state transitions;
- admission and deletion Receipt overclaim rejection;
- provisional `nkd0` command and `nks0` state digests.

`nkd0` and `nks0` are clean-profile implementation details, not accepted cross-profile identity contracts.

### 5.2 Explicit P1 absence

P1 contains no PostgreSQL or SQLite imports, SQL schema, driver, migration framework, append store, durable idempotency, writer lease persistence, projection persistence, network API or cross-project integration.

The logical reducer is not an authoritative event store and does not prove durable replay.

### 5.3 Authority boundary

Authority enters through an explicit port. The P1 static policy is deterministic and deny-by-default. Storage presence, authentication, model confidence, retrieval rank, utility or repeated use cannot imply admission authority.

### 5.4 Storage adapter boundary

A future PostgreSQL adapter may own transactions, locks, authoritative Event persistence, idempotency records, writer epoch/lease state, replay reads, projection offsets and profile diagnostics.

SQL schema, indexes, generated IDs, constraints and query plans remain profile details. P2 requires separate operator GO.

## 6. Writer and transaction model for future P2

Version 0 retains one authoritative writer per Kernel instance.

A future implementation must:

1. validate writer epoch/lease;
2. canonicalize command and calculate digest;
3. inspect the scoped idempotency key;
4. return original result for same key + same digest;
5. reject same key + different digest;
6. allocate contiguous global and stream sequence;
7. append the authoritative Event;
8. persist idempotency result referencing that Event;
9. commit atomically;
10. acknowledge durability only after commit.

Projection work occurs after the authoritative transaction. None of this durable path is implemented by P1.

## 7. Deterministic reducer boundary

P1 implements deterministic logical reduction with:

- explicit reducer version `nk-p1-reducer/1`;
- supported Event schema version `1`;
- contiguous global and per-stream sequence checks;
- accepted Event vocabulary only: `ADMIT`, `LINK`, `UTILIZED`, `SUPERSEDED`, `ERASED`;
- sorted immutable state structures;
- explicit failure on unsupported versions or sequence gaps.

This gives executable reducer semantics but not durable replay, corruption detection, upcasting, crash recovery or projection rebuild evidence.

## 8. Deletion and Receipt boundary

P1 implements the accepted deletion/restriction transition graph and rejects forbidden transitions. It also rejects Receipts that:

- claim complete global erasure;
- mark the same location verified and pending;
- omit proof limitations while locations remain pending;
- claim that admission authority establishes truth.

P1 does not delete real bytes, backups, indexes, provider data or encryption keys.

## 9. Machine-readable manifests

Two distinct records are retained:

1. `profile-manifest.json` — immutable P0 planning snapshot before operator GO;
2. `p1-manifest.json` — accepted P1 implementation/evidence state.

The P1 manifest records Python/stdlib scope, 20 semantic tests, compile evidence, prohibited P2 capabilities and Issue #1 independence.

All 72 contract assertions remain reported as `UNSUPPORTED` for runtime conformance until a future P4 conformance adapter emits assertion-scoped evidence.

```text
implemented code path
≠ assertion-level profile support claim
```

## 10. Test and fault matrix

### P1 — implemented and locally tested

- identity golden and invalid vectors;
- content/Claim identity separation;
- command canonicalization and digest determinism;
- float/null/non-NFC rejection;
- explicit authority allow/deny;
- admission Receipt overclaim rejection;
- reducer determinism;
- global/stream sequence failure;
- unsupported schema/reducer failure;
- deletion fixture paths and forbidden transitions;
- deletion Receipt proof limits;
- forbidden database/network imports.

### P2 — not authorized

- first durable append;
- same-digest retry;
- conflicting idempotency-key reuse;
- transaction rollback;
- sequence allocation under concurrency;
- writer-epoch rejection;
- projection failure after commit.

### P3–P5 — not authorized

Replay/rebuild, conformance adapter, repository reproduction and independent SQLite comparison remain future separately governed phases.

## 11. Evidence promotion

| Level | PostgreSQL profile gate | Current state |
|---|---|---|
| Planning/P0 | accepted profile plan and manifest | complete |
| Local implementation evidence | bounded code, commands, tests and failures | P1 partial only |
| C1 | profile-level local runtime with declared assertion evidence | not established |
| C2 | committed profile, pinned environment, CI, artifacts and traceability | not established |
| C3 | independent second profile preserves declared equivalence | not established |
| C4 | approved Offline Shadow | not established |
| C5 | bounded operational security/privacy/incident evidence | not established |

P1 is intentionally not labelled C1 because no durable profile runtime or assertion-scoped conformance adapter exists.

## 12. Security, licensing and dependencies

P1 adds no external dependencies and does not publish a package. Issue #18 remains open for publication, contribution and licensing terms.

Before P2 or operational claims, the project must decide PostgreSQL/driver versions, migration tooling, credential handling, least-privilege roles, backup/restore risks, log redaction, incident fencing and deletion/retention controls.

## 13. Implementation sequence

```text
P0 — accepted RFC + planning manifest              COMPLETE
P1 — profile-independent semantic core             PARTIAL / LOCALLY_TESTED
P2 — PostgreSQL append/idempotency adapter          BLOCKED / SEPARATE GO
P3 — replay, projection rebuild and Receipts        BLOCKED
P4 — conformance adapter and repository evidence    BLOCKED
P5 — independent SQLite profile for C3 research     BLOCKED
```

## 14. Remaining decisions

1. P2 operator GO;
2. PostgreSQL version, driver and migration matrix;
3. writer lease/epoch mechanism;
4. neutral export encoding;
5. initial persistent reducer/projection design;
6. minimum deletion scope for later evidence;
7. Issue #18 license and contribution terms;
8. exact repository workflow evidence.

## 15. Accepted boundaries

- [x] operator accepts profile ID, version and clean lineage;
- [x] profile manifest and assertion mapping reviewed;
- [x] transaction/idempotency/replay boundaries accepted as future P2/P3 obligations;
- [x] test/fault matrix accepted;
- [x] deletion and security non-claims accepted;
- [x] Issue #1 separation explicit;
- [x] bounded P1 runtime implementation receives separate GO;
- [ ] P2 or later runtime work receives separate GO.

```text
RFC: ACCEPTED
P1 implementation: PARTIAL / LOCALLY_TESTED
Durable Kernel profile: ABSENT
Kernel runtime conformance: UNSUPPORTED
```
