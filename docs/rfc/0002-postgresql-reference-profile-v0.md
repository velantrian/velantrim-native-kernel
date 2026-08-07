# RFC-0002: PostgreSQL Reference Profile v0 Planning Contract

- **RFC status:** `ACCEPTED`
- **Evidence level:** `REPOSITORY_REPRODUCED — P2 INTEGRATION`
- **Implementation status:** `PARTIAL — P1 SEMANTIC CORE + P2 APPEND/IDEMPOTENCY`
- **Operator approval:** `APPROVED`
- **Profile ID:** `native-kernel/postgresql-reference`
- **Planning version:** `nk-pg-profile/0.1`
- **Current implementation version:** `0.2-p2`
- **Evidence lineage:** `clean/postgresql-reference/0.1`
- **Related:** Issues #40, #43, #46; PR #47; ADR-0001, ADR-0009, ADR-0011…0016

## 1. Purpose and current decision

Define the first clean Native Kernel implementation profile that can implement accepted contracts using PostgreSQL without turning PostgreSQL, Python, SQL tables or current hardware into Architecture Canon.

```text
accepted architecture contracts
        ↓
accepted clean profile plan
        ↓
P1 profile-independent semantic core — merged and tested
        ↓
P2 PostgreSQL append/idempotency — partial and repository-integration-tested
        ↓
P3 replay/projections/Receipts — blocked by separate GO
        ↓
P4 conformance adapter — blocked
        ↓
P5 independent SQLite profile — blocked
```

Acceptance of P2 does not authorize later phases or establish profile conformance.

## 2. Lineage boundary

```text
native-kernel/postgresql-reference
≠ recovered v0.1.2.1
≠ original 44-test suite
≠ historical prototype continuation
```

The profile uses a clean evidence lineage. Issue #1 remains active and independent. Nothing here declares the historical source globally lost or replaces its provenance requirements.

Every implementation artifact must identify profile/version, source commit, registry version, environment, commands, evidence level, unsupported assertions and known limits.

## 3. Accepted inputs

| Input | Required meaning |
|---|---|
| ADR-0001 | Canon is separate from implementation profiles |
| ADR-0009 | PostgreSQL is preferred full profile; SQLite remains optional |
| ADR-0011 / `nk-id/1.0` | canonical identity and migration/collision rules |
| ADR-0012 / `nk-event/1.0` | single-writer append, idempotency, order and replay boundary |
| ADR-0013 / `nk-deletion/1.0` | deletion, restriction, retention and proof limits |
| ADR-0014 / `nk-fixtures/1.0` | executable fixture and evidence protocol |
| ADR-0015 | clean lineage accepted; P1 authorized |
| ADR-0016 | bounded P2 PostgreSQL append profile authorized |
| registry `1.1.0` | stable assertion IDs and statuses |

`NK-EPI-001…008` and ADR-0008 remain proposed. P2 does not implement or promote them.

## 4. Current reality status

```text
RFC/profile plan:              ACCEPTED / APPROVED
P1 semantic core:              PARTIAL / REPOSITORY-TESTED
P2 PostgreSQL append profile:  PARTIAL / REPOSITORY-INTEGRATION-TESTED
P3 replay/projections:         NOT_AUTHORIZED / NOT_IMPLEMENTED
Kernel runtime conformance:    UNSUPPORTED
C1/C2/C3:                      NOT_ESTABLISHED
```

Repository evidence for PR #47 head `e80492bcacde2ff2be3a2ee03aa5aa53a714d288`:

```text
P2 workflow run 31151297646 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
AI context run 31151298002 — PASS
P1 semantic core and fixture integrity — PASS
```

Each P2 matrix job passed 9 unit tests, 5 PostgreSQL integration tests, 5 manifest tests, validator and compileall.

## 5. Profile architecture

```text
Command API
   ↓
Command canonicalization + validation       ← P1 partial
   ↓
Authority port                              ← P1 explicit adapter
   ↓
Append service                              ← P2 implemented
   ↓
PostgreSQL authoritative-history adapter    ← P2 partial
   ↓
Reducer + upcaster registry                 ← reducer core P1; upcasters absent
   ↓
Disposable projections                     ← P3 absent
   ↓
Receipt/evidence emitter                    ← P1 proof guards; operational P3 absent
   ↓
Conformance adapter                         ← P4 absent
```

### 5.1 Implemented P1 semantic core

Package: `native_kernel.semantic_core`.

- `nk-id/1.0` canonical JSON subset and `nkh1`/`nkc1`/`nkl1` helpers;
- immutable semantic content, Claim identity, Command and logical Event objects;
- explicit deny-by-default authority policy;
- deterministic version-bound in-memory reducer;
- deletion/restriction state transitions;
- admission and deletion Receipt overclaim rejection;
- provisional `nkd0` command and `nks0` state digests.

`nkd0` and `nks0` remain profile implementation details, not accepted cross-profile contracts.

### 5.2 Implemented P2 PostgreSQL profile

Package: `native_kernel.postgresql_profile`.

Implemented:

- lazy Psycopg connection boundary;
- numbered SQL migrations with SHA-256 checksum ledger;
- advisory transaction lock for migration bootstrap;
- Kernel instance registration and history head;
- durable writer owner/epoch/expiry lease;
- stale and expired token failures;
- atomic Event and idempotency persistence;
- same-key/same-digest original-result return;
- same-key/different-digest conflict rejection;
- rollback-safe instance-global and per-stream counters;
- exact canonical payload and Event-envelope bytes;
- fixture-compatible `nkp1` payload commitment and `nke1` global chain;
- stored-event consistency validation on idempotent reads.

### 5.3 Authority boundary

Authority enters through an explicit port before storage work. Storage presence, authentication, model confidence, retrieval rank, utility or repetition cannot imply admission authority.

### 5.4 Storage adapter boundary

PostgreSQL owns transactions, locks, Event persistence, idempotency records and writer epoch/lease state only for this profile.

SQL schema, indexes, generated IDs, constraints and query plans remain profile details. P2 does not own projections, replay/upcasters, deletion execution, network API or conformance.

## 6. Writer and transaction model

Version 0 retains one authoritative writer per Kernel instance.

The implementation:

1. validates explicit authority;
2. locks the Kernel instance;
3. validates writer owner, epoch and expiry;
4. inspects scoped idempotency `(instance_id, command_contract, key)`;
5. returns the original result for same key + same digest;
6. rejects same key + different digest;
7. allocates contiguous global and stream sequence values;
8. builds canonical payload/envelope bytes and commitments;
9. appends the authoritative Event;
10. advances history/stream counters;
11. persists idempotency result referencing that Event;
12. commits atomically;
13. acknowledges only after commit.

PostgreSQL sequences are not used for authoritative counters because rollback does not return consumed sequence values. Normal rows plus locks preserve the tested contiguous-order invariant.

Projection work occurs after this transaction and remains P3.

## 7. Deterministic reducer boundary

P1 implements logical reduction with:

- reducer version `nk-p1-reducer/1`;
- Event schema version `1`;
- contiguous global and per-stream checks;
- vocabulary `ADMIT`, `LINK`, `UTILIZED`, `SUPERSEDED`, `ERASED`;
- sorted immutable state structures;
- explicit unsupported-version/sequence failures.

P2 persists Events but does not execute authoritative replay, corruption-wide scans, upcasting, crash recovery or projection rebuild.

## 8. Deletion and Receipt boundary

P1 implements deletion/restriction transitions and Receipt overclaim guards. P2 does not delete real bytes, backups, indexes, exports, provider data or encryption keys.

Operational deletion and provider/location evidence require later separately governed work.

## 9. Machine-readable manifests

Three distinct records are retained:

1. `profile-manifest.json` — historical P0 planning snapshot;
2. `p1-manifest.json` — P1 implementation/evidence state;
3. `p2-manifest.json` — P2 append/idempotency implementation and repository matrix evidence.

The P2 manifest records:

```text
implementation: PARTIAL
integration: PASS_REPOSITORY_CI
runtime conformance: UNSUPPORTED
C1/C2/C3: NOT_ESTABLISHED
```

All 72 contract assertions remain `UNSUPPORTED` for runtime conformance until P4 emits complete assertion-scoped evidence.

```text
implemented code path
≠ assertion-level profile support claim
```

## 10. Test and fault matrix

### P1 — implemented

- identity golden/invalid vectors;
- content/Claim identity separation;
- command canonicalization;
- float/null/non-NFC rejection;
- authority allow/deny;
- Receipt overclaim rejection;
- reducer determinism and sequence/version failures;
- deletion fixture paths and forbidden transitions;
- forbidden database/network imports.

### P2 — implemented and repository-tested

- migration and instance-registration idempotency;
- migration checksum drift detection;
- lease busy/release/monotonic epoch fencing;
- first append;
- same-digest retry;
- conflicting idempotency-key reuse;
- transaction rollback before commit;
- rollback-safe sequence reuse;
- concurrent same-digest append producing one Event;
- canonical payload/envelope and fixture hash commitments;
- P1 lazy-dependency boundary.

### P3–P5 — not authorized

Replay/rebuild, operational Receipts, complete conformance adapter and independent SQLite comparison remain future phases.

## 11. Evidence promotion

| Level | PostgreSQL profile gate | Current state |
|---|---|---|
| Planning/P0 | accepted profile plan and manifest | complete |
| Implementation evidence | bounded code, tests and explicit failures | P1/P2 partial |
| P2 integration evidence | declared PostgreSQL/Python matrix | repository reproduced |
| C1 | profile runtime with complete declared assertion evidence | not established |
| C2 | committed profile, pinned environment, CI, artifacts and traceability | not established |
| C3 | independent second profile preserves declared equivalence | not established |
| C4 | approved Offline Shadow | not established |
| C5 | bounded operational security/privacy/incident evidence | not established |

P2 integration is intentionally not labelled C1 because no P4 assertion-scoped conformance adapter exists.

## 12. Security, licensing and dependencies

P2 declares Psycopg for profile integration; it is lazy-loaded and not vendored. Issue #18 remains open for publication, contribution and licensing terms.

Operational claims still require credential handling, least-privilege roles, backup/restore evidence, log redaction, incident fencing, provider behavior and deletion/retention controls.

## 13. Implementation sequence

```text
P0 — accepted RFC + planning manifest              COMPLETE
P1 — profile-independent semantic core             MERGED / REPOSITORY-TESTED
P2 — PostgreSQL append/idempotency adapter          PARTIAL / INTEGRATION-TESTED
P3 — replay, projection rebuild and Receipts        BLOCKED / SEPARATE GO
P4 — conformance adapter and assertion evidence     BLOCKED / SEPARATE GO
P5 — independent SQLite profile for C3 research     BLOCKED / SEPARATE GO
```

## 14. Remaining decisions

1. P3 operator GO;
2. reducer/upcaster persistence and replay API;
3. projection checkpoint/rebuild protocol;
4. neutral export encoding;
5. deletion execution scope and evidence;
6. Issue #18 license/contribution terms;
7. operational fault, performance and backup/restore evidence;
8. future P4 assertion support policy.

## 15. Accepted boundaries

- [x] profile ID, version and clean lineage accepted;
- [x] profile manifests and assertion mapping reviewed;
- [x] transaction/idempotency boundaries accepted;
- [x] test/fault matrix accepted;
- [x] Issue #1 separation explicit;
- [x] P1 receives separate GO and is implemented;
- [x] P2 receives separate GO and is repository-integration-tested;
- [ ] P3 or later work receives separate GO.

```text
RFC: ACCEPTED
P1/P2 implementation: PARTIAL
P2 integration: REPOSITORY_REPRODUCED
Complete Kernel profile: ABSENT
Kernel runtime conformance: UNSUPPORTED
```
