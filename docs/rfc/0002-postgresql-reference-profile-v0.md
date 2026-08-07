# RFC-0002: PostgreSQL Reference Profile v0 Planning and Implementation Contract

- **RFC status:** `ACCEPTED`
- **Evidence level:** `REPOSITORY_REPRODUCED — P3 INTEGRATION`
- **Implementation status:** `PARTIAL — P1 + P2 + BOUNDED P3`
- **Operator approval:** `APPROVED`
- **Profile ID:** `native-kernel/postgresql-reference`
- **Planning version:** `nk-pg-profile/0.1`
- **Current implementation version:** `0.3-p3`
- **Evidence lineage:** `clean/postgresql-reference/0.1`
- **Related:** Issues #40, #43, #46, #49; PRs #47, #50; ADR-0001, ADR-0009, ADR-0011…0017

## 1. Purpose and current decision

Define the first clean Native Kernel implementation profile using PostgreSQL without turning PostgreSQL, Python, Psycopg, SQL tables, locks or current hardware into Architecture Canon.

```text
accepted architecture contracts
        ↓
P1 profile-independent semantic core — merged and tested
        ↓
P2 PostgreSQL append/idempotency — repository-integration-tested
        ↓
P3 replay/projection rebuild/Receipts — repository-integration-tested
        ↓
P4 assertion-scoped conformance adapter — blocked by separate GO
        ↓
P5 independent SQLite profile — blocked by separate GO
```

P3 implementation does not authorize P4/P5 or establish C1/C2/C3.

## 2. Lineage boundary

```text
native-kernel/postgresql-reference
≠ recovered v0.1.2.1
≠ original 44-test suite
≠ historical prototype continuation
```

Issue #1 remains active and independent. Nothing in this RFC declares historical source globally lost or replaces its provenance requirements.

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
| ADR-0016 | bounded P2 append/idempotency profile authorized |
| ADR-0017 | bounded P3 replay/projection/Receipt profile authorized |
| registry `1.1.0` | stable assertion IDs and statuses |

`NK-EPI-001…008` and ADR-0008 remain proposed. P3 does not implement or promote them.

## 4. Current reality

```text
P1 semantic core:              PARTIAL / REPOSITORY-TESTED
P2 PostgreSQL append profile:  PARTIAL / REPOSITORY-INTEGRATION-TESTED
P3 replay/projection profile:  PARTIAL / REPOSITORY-INTEGRATION-TESTED
Physical deletion:             NOT_IMPLEMENTED
P4 conformance adapter:        NOT_AUTHORIZED / NOT_IMPLEMENTED
P5 independent SQLite:         NOT_AUTHORIZED / NOT_IMPLEMENTED
Kernel runtime conformance:    UNSUPPORTED
C1/C2/C3:                      NOT_ESTABLISHED
```

Initial P3 executable-head evidence:

```text
head 0f8fd4ffe5d5fb0d4bc01f3e441a053f691dbba3
P3 run 31171581859 — PASS
P2 regression run 31171581795 — PASS
P1 run 31171581787 — PASS
fixture run 31171581791 — PASS
PostgreSQL 16/18 × Python 3.11/3.12 — PASS
```

The final PR head must repeat affected checks after documentation/evidence changes.

## 5. Profile architecture

```text
Command canonicalization + validation       ← P1
Authority port                              ← P1
PostgreSQL append/idempotency                ← P2
Authoritative Event history                 ← P2
Explicit UpcasterRegistry                   ← P3
Persisted replay from empty                 ← P3
Disposable semantic-state projection        ← P3
Replay/Projection Rebuild Receipts           ← P3
Assertion-scoped conformance adapter         ← P4 absent
Independent second profile                   ← P5 absent
```

### 5.1 P1 semantic core

Package: `native_kernel.semantic_core`.

- canonical JSON and identity helpers;
- immutable semantic objects;
- explicit authority boundary;
- deterministic reducer;
- deletion/restriction transitions and Receipt overclaim guards;
- standard-library deterministic upcaster registry;
- canonical semantic-state decoder.

`nkd0` and `nks0` remain clean-profile details unless separately promoted.

### 5.2 P2 authoritative append

Package: `native_kernel.postgresql_profile`.

- lazy Psycopg boundary;
- numbered SQL migrations and checksum ledger;
- Kernel instance/history head;
- writer owner/epoch/expiry lease;
- atomic Event + idempotency transaction;
- rollback-safe global and stream counters;
- canonical payload/envelope bytes;
- `nkp1` and `nke1` commitments;
- stored-event consistency validation.

### 5.3 P3 persisted replay

For one selected Kernel instance, P3:

1. opens a repeatable-read, read-only snapshot;
2. captures instance `last_global_seq` and `last_event_hash`;
3. requires Event count/max sequence to equal the captured head;
4. loads every Event from sequence `1` through the head using P2 commitment checks;
5. requires one `prev_global_hash` chain from `GENESIS`;
6. routes each Event through an explicit deterministic upcaster path;
7. reduces from empty using the declared P1 reducer;
8. requires the replayed final hash to equal the captured head;
9. emits a bounded state digest and Replay Receipt.

Missing, duplicate, cyclic, invalid or non-progressing upcaster paths fail explicitly.

### 5.4 Disposable projection rebuild

The `semantic-state` projection is a replaceable read model, not authoritative history.

```text
verified replay snapshot
→ lock Kernel instance row
→ compare current sequence/hash head
→ reject stale snapshot if history advanced
→ allocate monotonic generation from committed rebuild Receipts
→ insert Receipt
→ upsert projection
→ commit atomically
```

Projection deletion removes only the disposable projection row. It does not remove authoritative Events or Receipt history and does not reset generation lineage.

### 5.5 Operational Receipt boundary

P3 persists canonical Receipts for `REPLAY` and `PROJECTION_REBUILD`.

They may establish only:

- selected instance and observed Event range;
- observed final Event hash;
- reducer and target schema version;
- resulting state digest;
- projection name/generation when applicable;
- declared proof limitations.

They must not claim:

- truth of Claims;
- external authenticity, signatures or notarization;
- absence of every privileged rewrite before the snapshot;
- complete Event Integrity under every threat model;
- physical deletion of bytes, backups, exports, logs or keys;
- C1/C2/C3 or production durability/security/privacy/compliance.

## 6. Writer and transaction model

P2 append retains one authoritative writer owner/epoch lease per instance. P3 does not redesign append or introduce multi-writer consensus.

Replay reads a stable snapshot. Receipt/projection publication uses a separate write transaction and a locked instance-head comparison to prevent publishing stale state as current.

## 7. Determinism and integrity boundary

P3 validates:

- contiguous selected-instance global sequence;
- per-stream sequence through the reducer;
- canonical stored payload/envelope bytes;
- `nkp1` payload and `nke1` Event commitments;
- contiguous global hash chain;
- explicit schema path;
- reducer-version and canonical state digest;
- projection and Receipt canonical bytes on load.

These checks are integrity signals, not external authentication or a defense against every privileged rewrite.

## 8. Deletion boundary

P1 models semantic deletion/restriction state. P2/P3 store Events, projections and Receipts. They do not delete primary bytes, backups, indexes, provider data, logs, exports or encryption keys.

Physical/cryptographic deletion and its evidence require a separate decision and operational design.

## 9. Machine-readable manifests

Distinct phase records are retained:

1. `profile-manifest.json` — P0 planning snapshot;
2. `p1-manifest.json` — P1 implementation boundary;
3. `p2-manifest.json` — P2 append evidence;
4. `p3-manifest.json` — P3 replay/projection/Receipt evidence.

P3 manifest status:

```text
implementation: PARTIAL
evidence: REPOSITORY_REPRODUCED_P3_INTEGRATION
runtime conformance: UNSUPPORTED
C1/C2/C3: NOT_ESTABLISHED
```

All 72 assertions remain runtime `UNSUPPORTED` until P4 emits a complete assertion-scoped report.

## 10. Test and fault matrix

### P3 semantic tests

- identity and multi-step upcasting;
- missing/duplicate/cyclic/invalid path rejection;
- canonical state round-trip and noncanonical rejection;
- canonical bounded Receipt;
- Receipt overclaim and operation-shape rejection.

### P3 PostgreSQL integration tests

- persisted replay equals direct P1 reduction;
- Replay Receipt persistence and reload;
- projection rebuild determinism;
- destroy/rebuild with monotonic generation;
- injected precommit failure preserves previous projection and Receipt count;
- history advancement rejects stale projection publication;
- stored Event canonical corruption detection;
- projection canonical/state-digest corruption detection;
- Receipt canonical/hash corruption detection;
- explicit upcaster path requirement;
- P2 regression suite.

## 11. Evidence promotion

| Level | Gate | Current state |
|---|---|---|
| P0 planning | accepted plan/manifests | complete |
| P1 semantics | bounded deterministic core | repository tested |
| P2 append | declared DB matrix | repository reproduced |
| P3 replay/projection | declared DB matrix and fault scenarios | repository reproduced |
| C1 | complete declared assertion support evidence | not established |
| C2 | pinned reproducibility/artifacts/traceability for complete profile claim | not established |
| C3 | materially independent second profile | not established |
| C4/C5 | Shadow/operational evidence | not established |

P3 integration is not labelled C1 or C2 because P4 assertion-scoped evidence does not exist.

## 12. Security, licensing and dependencies

Psycopg remains a lazy profile dependency and is not vendored. Issue #18 remains open.

Operational claims still require credential/role design, backup and restore evidence, provider behavior, performance limits, incident fencing, log redaction and deletion/retention controls.

## 13. Implementation sequence

```text
P0 — accepted RFC + planning manifest              COMPLETE
P1 — semantic core                                 MERGED / REPOSITORY-TESTED
P2 — PostgreSQL append/idempotency                  PARTIAL / INTEGRATION-TESTED
P3 — persisted replay/projection/Receipts           PARTIAL / INTEGRATION-TESTED
P4 — assertion-scoped conformance adapter           BLOCKED / SEPARATE GO
P5 — independent SQLite profile                     BLOCKED / SEPARATE GO
```

## 14. Remaining decisions

1. separate P4 operator GO;
2. complete assertion-to-runtime evidence mapping;
3. neutral export/migration encoding;
4. physical/cryptographic deletion design;
5. Issue #18 license/contribution terms;
6. performance and operational fault evidence;
7. independent P5 profile before C3.

## 15. Accepted boundaries

- [x] clean profile and lineage accepted;
- [x] P1 separately authorized and tested;
- [x] P2 separately authorized and repository-integration-tested;
- [x] P3 separately authorized and repository-integration-tested;
- [x] Receipt non-claims and stale-head guard retained;
- [x] Issue #1 separation explicit;
- [ ] P4/P5 receive separate GO.

```text
RFC: ACCEPTED
P1/P2/P3 implementation: PARTIAL
P3 integration: REPOSITORY_REPRODUCED
Complete assertion conformance: ABSENT
C1/C2/C3: NOT ESTABLISHED
```
