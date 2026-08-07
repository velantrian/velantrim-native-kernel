# RFC-0002: PostgreSQL Reference Profile v0 Planning and Implementation Contract

- **RFC status:** `ACCEPTED`
- **Evidence level:** `REPOSITORY_REPRODUCED — P4 ASSERTION-SCOPED C2 ON PREVIOUS HEAD`
- **Implementation status:** `PARTIAL — P1 + P2 + P3 + P4`
- **Operator approval:** `APPROVED`
- **Profile ID:** `native-kernel/postgresql-reference`
- **Planning version:** `nk-pg-profile/0.1`
- **Current implementation version:** `0.4-p4`
- **Evidence lineage:** `clean/postgresql-reference/0.1`
- **Related:** Issues #40, #43, #46, #49, #55; PRs #47, #50, #56; ADR-0001, ADR-0009, ADR-0011…0018

## 1. Purpose and current decision

Define the first clean Native Kernel implementation profile using PostgreSQL without turning PostgreSQL, Python, Psycopg, SQL tables, locks or current hardware into Architecture Canon.

```text
accepted architecture contracts
        ↓
P1 profile-independent semantic core — merged
        ↓
P2 PostgreSQL append/idempotency — merged
        ↓
P3 replay/projection rebuild/Receipts — merged
        ↓
P4 assertion-scoped conformance — authorized and implemented in PR #56
        ↓
P5 independent SQLite profile — blocked by separate GO
```

P4 does not authorize P5 or establish C3.

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
| ADR-0018 | P4 assertion-scoped conformance authorized |
| registry `1.1.0` | stable 72 assertion IDs and decision statuses |

`NK-EPI-001…008` and ADR-0008 remain proposed. P4 emits them as `UNSUPPORTED`; it does not accept or promote them.

## 4. Current reality

```text
P1 semantic core:              PARTIAL / REPOSITORY-TESTED
P2 PostgreSQL append profile:  PARTIAL / REPOSITORY-INTEGRATION-TESTED
P3 replay/projection profile:  PARTIAL / REPOSITORY-INTEGRATION-TESTED
P4 conformance adapter:        PARTIAL / C2 REPOSITORY-REPRODUCED
support_state:                 PARTIAL
P5 independent SQLite:         NOT_AUTHORIZED / NOT_IMPLEMENTED
C3/C4/C5:                      NOT_ESTABLISHED
Physical deletion:             NOT_IMPLEMENTED
```

P4 support map:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
TOTAL:       72
```

The top-level C2 label applies only to the 41 `SUPPORTED` assertion results in the exact report.

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
Assertion-scoped conformance adapter         ← P4
Independent second profile                   ← P5 absent
```

### 5.1 P1 semantic core

Package: `native_kernel.semantic_core`.

- canonical JSON and identity helpers;
- immutable semantic objects;
- explicit authority boundary;
- deterministic reducer;
- deletion/restriction transitions and Receipt overclaim guards;
- deterministic upcaster registry;
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

### 5.3 P3 persisted replay and projections

For one selected Kernel instance, P3:

1. opens a repeatable-read snapshot;
2. captures the authoritative head;
3. verifies Event count, sequence and canonical commitments;
4. verifies one global hash chain from `GENESIS`;
5. routes schema versions through an explicit upcaster path;
6. reduces from empty through the P1 reducer;
7. emits a bounded Replay Receipt;
8. compares the captured head under lock before projection publication;
9. atomically commits the rebuild Receipt and disposable projection.

Projection deletion does not remove Events or committed Receipt history and does not reset generation lineage.

### 5.4 P3 Receipt boundary

Replay and Projection Rebuild Receipts may establish only their declared operation, selected instance, Event range/head, reducer/schema versions, state digest, projection identity/generation and proof limitations.

They do not establish truth, external authenticity, complete Event Integrity, physical deletion, C-levels or production guarantees.

### 5.5 P4 assertion-scoped adapter

P4 uses `nk-evidence-report/1` and emits all 72 registry IDs exactly once.

```text
registry + fixture pack
→ semantic checks
→ PostgreSQL checks
→ assertion result map
→ evidence references + limitations
→ strict report validation
→ repository artifact
```

Each result is one of:

- `SUPPORTED` — bounded assertion behavior was directly reproduced;
- `PARTIAL` — meaningful behavior was reproduced but an explicit gap remains;
- `UNSUPPORTED` — sufficient executable support is absent or the assertion is proposed;
- `FAILED` — a required declared check executed and failed.

No assertion may be omitted or promoted through prose.

## 6. P4 executable checks

Profile-neutral checks:

- registry version/coverage/decision status;
- identity golden vectors and invalid canonical inputs;
- semantic roles, explicit scope and source-bound Claim identity;
- explicit deny-by-default authority;
- Admission/Deletion Receipt proof limits;
- deterministic reduction and explicit sequence/schema failures;
- semantic deletion/restriction transitions.

PostgreSQL checks:

- migration idempotency;
- writer lease/epoch fencing;
- append, retry and conflicting idempotency reuse;
- rollback-safe contiguous ordering;
- persisted replay equals direct reduction;
- projection destroy/rebuild and monotonic generation;
- stale-head rejection;
- stored canonical corruption detection.

These checks do not implement missing conflict, restore, deletion-worker, cross-project or cross-profile behavior.

## 7. C1, C2 and C3 boundary

Conformance is assertion-scoped.

- C1: locally exercised commands/failures with recorded evidence;
- C2: exact repository reproduction with committed implementation, environment, CI traceability and retained artifacts;
- C3: materially independent profile plus declared equivalence and comparison evidence.

```text
support_state: PARTIAL
kernel_runtime_conformance: C2
```

This combination is valid because C2 applies only to the `SUPPORTED` assertion results. `PARTIAL` and `UNSUPPORTED` remain outside the supported set.

```text
C2 in four Python/PostgreSQL combinations
≠ four independent profiles
≠ C3
```

## 8. Initial P4 evidence

Evidence head:

```text
93710131fffdea7d9a586cc05e7f258c07fae707
```

```text
P4 run 31175767586 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
P1/P2/P3 regressions — PASS
4 retained JSON evidence artifacts
```

The initial failure run `31175593261` is retained as negative evidence. The full C1 report passed, but the standalone adapter did not include repository root on `sys.path`. The CLI bootstrap was corrected without weakening checks or validation.

Exact artifact digests are recorded in `docs/ai/P4_IMPLEMENTATION_RECORD.md`.

## 9. Evidence report rules

A valid P4 report must:

1. use `nk-evidence-report/1`;
2. name `native-kernel/postgresql-reference`;
3. retain `support_state: PARTIAL`;
4. emit all 72 assertion IDs exactly once;
5. match the guarded support counts;
6. require evidence for every supported/partial result;
7. reference only passed checks in the same report;
8. include limitations for every result;
9. retain all proposed `NK-EPI` results as unsupported;
10. state that C2 is not C3, truth, authenticity, deletion or production proof.

Repository C2 additionally requires non-local commit/run/environment metadata and retained artifacts.

## 10. Technology neutrality

PostgreSQL, Psycopg, Python, JSONB, SQL tables, row locks and GitHub Actions are profile technologies.

The following remain semantic/contract concerns:

- stable Claim identity roles;
- authority and admission distinction;
- Event meaning and order obligations;
- deterministic reduction;
- deletion/restriction proof limits;
- Receipt/report boundaries;
- assertion support states and equivalence classes.

P4 C2 does not promote profile technology into Canon.

## 11. Explicit non-goals

- no P5 SQLite implementation;
- no C3 cross-profile equivalence;
- no physical or cryptographic deletion execution;
- no truth, signature, notarization or external-authenticity certification;
- no C4/C5 or production claim;
- no network API;
- no Titan, Mentaury or Crystal runtime wiring;
- no `v0.1.2.1` recovery claim;
- no ADR-0008 or `NK-EPI` promotion;
- no package publication decision under Issue #18.

## 12. Remaining gaps

- complete conflict representation/resolution;
- identity migration/alias adjudication;
- restore-before-visibility enforcement;
- durable deletion execution across locations/backups/keys;
- cross-project authority adapter;
- independent second profile;
- scale, failover, backup/restore and managed-provider evidence;
- long-term evidence artifact retention.

## 13. Phase lifecycle

```text
P0 — RFC and planning manifest                     COMPLETE
P1 — profile-independent semantic core              MERGED
P2 — PostgreSQL append/idempotency                   MERGED
P3 — replay/projection rebuild/Receipts              MERGED
P4 — assertion-scoped conformance                    ACTIVE / PARTIAL / C2 EVIDENCE
P5 — independent SQLite profile / C3 research        BLOCKED / SEPARATE GO
```

## 14. Next gate

P5 requires a separate explicit operator GO. Any C3 claim must identify a materially independent implementation, the declared equivalence classes, allowed differences, exact comparison commands and retained evidence.
