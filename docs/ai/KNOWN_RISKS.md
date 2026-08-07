# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-07  
**Last verified public `main`:** `bb94835ad612f45e2629655bc9add872d8981357`  
**Active implementation:** Issue #46 / PR #47 / P2 PostgreSQL append profile

P2 repository integration narrows the storage-implementation gap. It does not close replay, projection, operational fault, security, privacy, licensing, portability or conformance risks.

## P0 — Authentic source recovery remains unresolved

**State:** `OPEN`

The reported `v0.1.2.1` source and original 44-test suite remain absent from accessible sources.

Required proof: authentic bytes, lineage, hashes, original test inventory and explicit Issue #1 operator gate.

## P0 — Clean P1/P2 may be mistaken for recovered history

**State:** `OPEN`, narrowed by ADR-0015/0016 and manifest guards

```text
clean/postgresql-reference/0.1
≠ v0.1.2.1
≠ original 44-test evidence
```

Every future package, report and release must preserve this boundary.

## P0 — P2 profile may be mistaken for a complete Kernel

**State:** `OPEN`

P1 implements semantic identity/objects/authority/reduction/deletion semantics. P2 implements bounded PostgreSQL append/idempotency and writer fencing.

Missing: replay/upcasters, projection persistence/rebuild, operational Receipts, deletion execution, network API, P4 conformance and independent-profile evidence.

Required control: public surfaces use `P2 PARTIAL / NOT PRODUCTION-READY`.

## P0 — Durable append may be mistaken for durable replay

**State:** `OPEN`

P2 proves atomic append/idempotency and tested rollback/concurrency. It does not execute reducer replay from persisted history, detect every truncation/fork/privileged rewrite, run upcasters or rebuild projections.

Required proof: separately authorized P3.

## P0 — P2 integration may be mistaken for C1/C2

**State:** `OPEN`, machine-readable guard retained

PR #47 evidence run:

```text
run 31151297646 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
```

This establishes the bounded P2 scenarios in the declared matrix. It does not establish complete assertion-scoped profile support, artifacts/traceability for every contract or independent-profile equivalence.

```text
kernel_runtime_conformance: UNSUPPORTED
C1/C2/C3: NOT_ESTABLISHED
```

## P0 — Provisional digests may become accidental Canon

**State:** `OPEN`

`nkd0` and `nks0` remain P1 implementation details. `nkp1` and `nke1` implement accepted fixture algorithms but the PostgreSQL envelope/table layout remains profile-specific.

Required control: no unrelated profile/migration may depend on implementation-only layouts without explicit contract review.

## P0 — Hash chain may be mistaken for authentication

**State:** `OPEN`

`nkp1`/`nke1` detect tested inconsistencies but are not signatures, external notarization or defense against every privileged rewrite.

Required proof for authenticity: separate key/signature or external-evidence design.

## P0 — Single-writer lease may be mistaken for consensus

**State:** `OPEN`

Owner/epoch/expiry fencing serializes one PostgreSQL profile. It is not multi-writer consensus, cross-region leadership or Byzantine protection.

## P1 — Exact final-head workflow drift

**State:** `OPEN UNTIL MERGE GATE`

Evidence is valid for its exact SHA. Later documentation/manifest changes require same-head affected checks before merge.

## P1 — Python may become accidental permanent architecture

**State:** `OPEN`, narrowed

P1/P2 use Python as a reversible profile choice. Semantic contracts must remain independent from Python dataclasses, types and module layout.

## P1 — Psycopg/PostgreSQL may become accidental Canon

**State:** `OPEN`, controlled by profile separation

Psycopg, SQL schema, indexes and locks are profile technologies. Cross-profile neutrality remains unproven until P5/C3 evidence.

## P1 — Authority adapter may be mistaken for operational security

**State:** `OPEN`

P2 calls explicit authority before append, but the local authority adapter has no credentials, identity provider, revocation, persisted delegation or operational audit.

Required proof: separate authority/security profile and threat model.

## P1 — Writer lease behavior under operational faults

**State:** `OPEN`

Database failover, abrupt process death, network partitions, managed-provider behavior and very long transactions require future fault evidence.

## P1 — Row-lock serialization throughput

**State:** `ACCEPTED TRADE-OFF / UNBENCHMARKED`

Contiguous instance-global ordering serializes authoritative appends per instance. Performance and contention limits are unknown.

## P1 — Migration operational safety

**State:** `OPEN`, partially controlled

Checksums and advisory locking are tested. Downgrade, partial rollout, managed migrations, long-lock behavior and restore-time migration remain untested.

## P1 — Stored JSONB/canonical-byte divergence

**State:** `OPEN`, bounded checks present

Idempotent reads verify canonical payload/envelope bytes and hashes. Whole-history scanning, repair and periodic audit remain future work.

## P1 — Deletion semantics may be mistaken for byte deletion

**State:** `OPEN`

P1 validates transitions and Receipt limits; P2 stores Events. Neither deletes primary data, backups, indexes, logs, exports or keys.

Required proof: profile-specific location inventory, retries/failures, backup/restore behavior and security/legal review.

## P1 — Accepted contracts remain only partially implemented

**State:** `OPEN`

P1/P2 exercise selected NK-ID, NK-SEM, NK-AUT, NK-EVT and deletion paths. They do not emit complete assertion-level evidence.

All 72 assertions remain runtime `UNSUPPORTED` until P4.

## P1 — SQL schema may become accidental Canon

**State:** `OPEN`

Tables, constraints, indexes and surrogate IDs are PostgreSQL profile details. Semantic identity must survive storage replacement.

## P1 — NK-EPI status may be hidden by implementation progress

**State:** `OPEN`

ADR-0008 and `NK-EPI-001…008` remain proposed. P2 does not implement or accept them.

## P1 — Storage neutrality remains unproven

**State:** `OPEN`

One PostgreSQL profile exists. C3 requires a materially independent second profile and declared equivalence.

## P1 — Cross-project authority leakage

**State:** `OPEN`

P2 does not authorize Titan, Mentaury or Crystal integration, shared storage, identity or inherited conformance.

## P1 — License and contribution terms unresolved

**State:** `OPEN`, Issue #18

Psycopg is declared as an integration dependency but not vendored or packaged. Publication, reuse and contribution terms remain undecided.

## Update rule

Record exact state, evidence, SHA, remaining uncertainty and next action. Never close a risk through prose, approval, code presence, one integration matrix or manifest coverage alone.
