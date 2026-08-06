# RFC-0002: PostgreSQL Reference Profile v0 Planning Contract

- **RFC status:** `PROPOSED / DOCUMENTED_ONLY`
- **Evidence level:** `DOCUMENTED`
- **Implementation status:** `NOT_STARTED`
- **Operator approval:** `PENDING`
- **Profile ID:** `native-kernel/postgresql-reference`
- **Planning version:** `nk-pg-profile/0.1-proposed`
- **Evidence lineage:** `clean/postgresql-reference/0.1`
- **Related:** Issue #40, ADR-0001, ADR-0009, ADR-0011…0014

## 1. Purpose

Define the first clean Native Kernel implementation profile that can implement accepted contracts using PostgreSQL without turning PostgreSQL, Python, SQL tables, or current hardware into Architecture Canon.

```text
accepted architecture contracts
        ↓
clean PostgreSQL profile specification
        ↓
separate implementation PRs
        ↓
local evidence
        ↓
repository reproduction
        ↓
future independent SQLite profile
        ↓
possible C3 comparison
```

This RFC is a planning contract. It does not contain a Kernel runtime and does not authorize implementation until separately approved.

## 2. Lineage boundary

```text
native-kernel/postgresql-reference
≠ recovered v0.1.2.1
≠ original 44-test suite
≠ historical prototype continuation
```

The profile begins a new clean evidence lineage. Issue #1 remains active and independent. Nothing in this RFC declares the historical source globally lost or replaces its provenance requirements.

Every future implementation artifact must identify:

- profile ID and version;
- source commit;
- contract registry version;
- schema and reducer versions;
- environment and commands;
- evidence level;
- unsupported assertions and known limits.

## 3. Accepted inputs

The profile must map to these accepted decisions:

| Input | Required meaning |
|---|---|
| ADR-0001 | Canon is separate from implementation profiles |
| ADR-0009 | PostgreSQL is the preferred full profile; SQLite remains optional |
| ADR-0011 / `nk-id/1.0` | canonical identity and migration/collision rules |
| ADR-0012 / `nk-event/1.0` | single-writer append, idempotency, order and replay boundary |
| ADR-0013 / `nk-deletion/1.0` | deletion, restriction, retention and proof limits |
| ADR-0014 / `nk-fixtures/1.0` | executable fixture and evidence protocol |
| registry `1.1.0` | stable assertion IDs and statuses |

`NK-EPI-001…008` remains proposed. The profile may report these assertions as unsupported or experimental but must not silently promote ADR-0008.

## 4. Non-goals

This RFC does not define or claim:

- production readiness;
- multi-writer consensus or distributed authority;
- a universal SQL schema;
- PostgreSQL-specific semantics as Canon;
- live Titan, Mentaury, or Crystal integration;
- legal compliance or global deletion proof;
- C2 or C3 from documentation;
- historical compatibility with `v0.1.2.1`;
- a permanent programming language or PostgreSQL major version.

## 5. Profile architecture

```text
Command API
   ↓
Command canonicalization + validation
   ↓
Authority port
   ↓
Append service
   ↓
PostgreSQL authoritative-history adapter
   ↓
Reducer + upcaster registry
   ↓
Disposable projections
   ↓
Receipt/evidence emitter
   ↓
Conformance adapter
```

### 5.1 Semantic core

The semantic core owns:

- accepted identity algorithms;
- command and event domain objects;
- reducer/upcaster interfaces;
- deletion state transitions;
- Receipt proof boundaries;
- profile-independent errors.

It must not import PostgreSQL drivers or expose table IDs as semantic identity.

### 5.2 Authority port

Authority decisions enter through an explicit port. Initial tests may use a deterministic local policy adapter, but storage presence, authentication success, model confidence, retrieval rank, or repeated use must not imply admission authority.

### 5.3 Storage adapter

The PostgreSQL adapter owns:

- transactions and locks;
- authoritative event persistence;
- idempotency records;
- writer epoch/lease state;
- replay reads;
- projection offsets and rebuild metadata;
- profile-local diagnostics.

SQL schema, indexes, generated IDs, constraints and query plans are profile details.

### 5.4 Reducer and projections

Reducers are deterministic functions bound to explicit versions. Projections are disposable and may be destroyed and rebuilt from authoritative history.

A projection failure cannot roll back, edit, or conceal an already committed authoritative Event.

### 5.5 Evidence emitter

The profile emits machine-readable evidence reports compatible with `nk-evidence-report/1`. Unsupported assertions remain visible.

## 6. Writer and transaction model

Version 0 planning adopts one authoritative writer per Kernel instance.

A future implementation must establish the writer boundary through an explicit process/instance lease or equivalent profile-local mechanism. It must not infer safe multi-writer behaviour from PostgreSQL availability alone.

### Atomic command path

Inside one database transaction:

1. validate writer epoch/lease;
2. canonicalize command and calculate command digest;
3. look up scoped idempotency key;
4. return the original result for same key + same digest;
5. reject same key + different digest;
6. allocate contiguous `global_seq` and stream sequence;
7. append the authoritative Event;
8. persist idempotency result referencing that Event;
9. commit;
10. acknowledge durability only after successful commit.

Projection work occurs after the authoritative transaction.

### Required failure behaviour

| Failure | Required outcome |
|---|---|
| validation or authority failure | no append |
| duplicate same digest | original result, no second Event |
| duplicate different digest | explicit idempotency conflict |
| transaction rollback | no visible Event or success result |
| projection failure after commit | Event remains authoritative; projection marked behind |
| unsupported schema/reducer | replay stops explicitly |
| writer-epoch mismatch | append rejected |

## 7. Profile-local storage map

The initial implementation may use profile-local structures equivalent to:

| Logical structure | Role |
|---|---|
| profile metadata | profile ID/version, registry version and writer epoch |
| commands/idempotency | command digest, key scope and original result |
| authoritative events | immutable ordered Event envelopes |
| reducer versions | declared reducer/upcaster compatibility |
| projection offsets | disposable read-model progress |
| deletion work | requests, attempts, locations and residual limits |
| evidence records | replay, rebuild and migration Receipts |

Names and columns are non-normative. Semantic identifiers must remain independent from surrogate database keys.

## 8. Capability manifest

The proposed machine-readable manifest must state, for every contract family:

- contract version;
- planning state;
- intended implementation phase;
- explicitly unsupported assertions;
- evidence level;
- known operational limits.

Planning terms such as `PLANNED` or `DEFERRED` are not conformance results. Runtime evidence reports use only the accepted evidence-report status vocabulary.

## 9. Deletion and data locations

The planning profile must inventory at least:

- authoritative Event payloads;
- command/idempotency data;
- projections and indexes;
- evidence records and exports;
- diagnostic logs and dead-letter data;
- backups, replicas and migration artifacts.

The first runtime stages may support only logical restriction and fixture-scoped deletion behaviour. Physical deletion, provider deletion, backup expiry and crypto-erasure remain unsupported until implemented and evidenced.

Every Receipt must list verified, pending and unknown locations.

## 10. Replay and rebuild

A profile replay experiment must:

1. start with an empty derived-state store;
2. read authoritative Events in `global_seq` order;
3. verify payload and chain commitments;
4. apply declared upcasters and reducer version;
5. stop on unsupported versions or corruption;
6. emit final state digest, counts, offsets and limitations;
7. compare against declared expected outputs;
8. repeat after destroying projections.

Fixture integrity alone does not satisfy this experiment.

## 11. Migration boundary

Export/import is a separate controlled operation:

```text
fence writes
→ record source position
→ export neutral authoritative history
→ verify identity/order/commitments
→ import target profile
→ replay from empty
→ compare declared equivalence
→ activate or roll back
→ emit migration Receipt
```

A future SQLite profile must consume the same neutral history and contract versions. Physical SQL equality is not required; declared semantic and behavioural equivalence is.

## 12. Test and fault matrix

### P1 — Semantic core

- identity golden and invalid vectors;
- command canonicalization;
- reducer determinism;
- unknown/unsupported version failures;
- deletion state transitions;
- Receipt overclaim rejection.

### P2 — PostgreSQL adapter

- first append;
- same-digest retry;
- conflicting key reuse;
- transaction rollback;
- sequence contiguity;
- writer-epoch rejection;
- concurrent attempts under the single-writer boundary;
- projection failure after commit.

### P3 — Replay and rebuild

- replay from empty;
- destroy/rebuild projections;
- truncated history;
- reordered history;
- modified payload commitment;
- unsupported upcaster/reducer;
- interrupted rebuild and resume/rollback rules.

### P4 — Conformance adapter

- all 72 assertion IDs reported exactly once;
- unsupported assertions visible;
- exact profile/environment/commit metadata;
- machine-readable evidence artifact;
- CI reproduction at an exact SHA.

### P5 — Cross-profile

- independently developed SQLite adapter;
- shared neutral history;
- declared byte/structural/semantic/behavioural comparisons;
- no C3 until differences and limitations are reviewed.

## 13. Evidence promotion

| Level | PostgreSQL profile gate |
|---|---|
| C0 | profile manifest and assertion mapping merged |
| C1 | implementation runs locally with recorded commands and failures |
| C2 | committed code, pinned environment, CI, artifacts and traceability reproduce scoped assertions |
| C3 | independent SQLite or other profile preserves declared equivalence |
| C4 | approved Offline Shadow workload and Receipts |
| C5 | bounded operational security/privacy/rollback/incident evidence |

Acceptance of this RFC would authorize planning, not automatic promotion through these levels.

## 14. Packaging and environment

A future implementation PR must pin or declare:

- programming-language/runtime range;
- PostgreSQL server major(s);
- driver and migration-tool versions;
- container or local-service startup path;
- schema migration identifier;
- exact test and conformance commands;
- supported operating assumptions.

No environment is chosen permanently by this RFC.

## 15. Security and incident boundaries

The initial profile is not production-safe by default. Before operational claims it requires:

- credentials and secret handling;
- least-privilege database roles;
- backup/restore threat review;
- log and diagnostic redaction;
- corruption and partial-write response;
- explicit disable/fence procedure;
- migration rollback;
- deletion and retention review;
- incident Receipts and operator visibility.

## 16. Implementation sequence

```text
P0 — merge profile RFC and planning manifest
P1 — implement profile-independent semantic core
P2 — implement PostgreSQL authoritative append/idempotency adapter
P3 — implement reducer, projection rebuild and Receipts
P4 — implement conformance adapter and repository CI
P5 — implement independent SQLite profile for C3 research
```

Each stage requires a separate PR with exact status and evidence. Runtime work must not be labelled as recovered `v0.1.2.1`.

## 17. Open decisions before implementation

1. programming language and package layout;
2. PostgreSQL version matrix;
3. writer lease/epoch mechanism;
4. neutral export encoding;
5. initial reducer/state model;
6. first projection set;
7. minimum deletion scope for C1/C2;
8. dependency and repository license constraints;
9. whether runtime implementation may begin while Issue #1 remains active.

## 18. Acceptance gate

- [ ] operator accepts profile ID, version and clean lineage;
- [ ] profile manifest and assertion mapping are reviewed;
- [ ] transaction/idempotency/replay boundaries are accepted;
- [ ] test/fault matrix is accepted;
- [ ] deletion and security non-claims are accepted;
- [ ] Issue #1 separation is explicit;
- [ ] runtime implementation receives a separate GO.

Until then:

```text
RFC: PROPOSED
Implementation: NOT_STARTED
Evidence: DOCUMENTED
Kernel runtime: ABSENT
```
