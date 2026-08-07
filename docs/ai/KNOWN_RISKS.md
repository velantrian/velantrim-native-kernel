# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-07  
**Last verified public `main`:** `bb94835ad612f45e2629655bc9add872d8981357`  
**Active work:** Issue #46 / P2 PostgreSQL append profile

## P0 — Authentic source recovery remains unresolved

**State:** `OPEN`

The reported `v0.1.2.1` source and original 44-test suite remain absent from accessible sources.

```text
clean/postgresql-reference/0.1
≠ recovered v0.1.2.1
≠ original 44-test evidence
```

## P0 — P2 may be mistaken for a complete Kernel

**State:** `OPEN`

P2 adds a bounded append/idempotency profile. It does not add replay/upcasters, projections, operational Receipts, deletion execution, API, conformance or ecosystem wiring.

Required control: public status remains `P2 PARTIAL / NOT PRODUCTION-READY`.

## P0 — Unit tests may be mistaken for PostgreSQL integration

**State:** `OPEN`

```text
9 P2 unit tests PASS
5 P2 manifest tests PASS
5 PostgreSQL tests DECLARED / NOT RUN NO DSN
repository run NOT_RECORDED
```

Required proof: exact PostgreSQL 16/18 × Python 3.11/3.12 jobs, logs and conclusions.

## P0 — Durable append may be mistaken for replay conformance

**State:** `OPEN`

The adapter appends and retrieves original idempotent results. It does not execute reducer/upcaster replay, rebuild projections, detect every privileged rewrite or prove recovery after real process/host failures.

Required proof: separately authorized P3 fault/replay work.

## P0 — Single-writer lease may be mistaken for consensus

**State:** `OPEN`

Owner/epoch/expiry fencing serializes this PostgreSQL profile. It is not multi-writer consensus, cross-region leadership or Byzantine protection.

Required control: keep multi-writer out of `nk-event/1.0` claims.

## P0 — Hash chain may be mistaken for authentication

**State:** `OPEN`

`nkp1`/`nke1` detect tested inconsistencies but are not signatures, external notarization or defense against every privileged database rewrite.

Required proof for authenticity: separately designed key/signature or external evidence system.

## P1 — Migration drift and operational migration safety

**State:** `OPEN`, partially controlled

Numbered SQL checksums and an advisory transaction lock detect modified applied migrations and serialize migration execution. Restore, downgrade, partial operational rollout and long-lock behavior remain untested.

## P1 — Writer lease clock/availability assumptions

**State:** `OPEN`

Lease expiry uses PostgreSQL transaction time. Long transactions, connection loss, database failover and operational clock behavior require integration/fault evidence.

## P1 — Rollback-safe counters serialize writes

**State:** `ACCEPTED TRADE-OFF / UNBENCHMARKED`

Instance-row locking provides contiguous global ordering but serializes authoritative appends per instance. Throughput and contention are unknown.

Required proof: performance and failure tests before operational claims.

## P1 — Psycopg/PostgreSQL may become accidental Canon

**State:** `OPEN`, controlled by profile separation

Python, Psycopg, SQL schema, indexes and locks are replaceable implementation details. Cross-profile neutrality remains unproven until P5/C3 evidence.

## P1 — P1 dependency boundary may regress

**State:** `OPEN`, guarded

Psycopg must remain lazy and P2-only. `native_kernel.semantic_core` stays standard-library-only.

## P1 — Stored JSONB may diverge from canonical bytes

**State:** `OPEN`, checked on idempotent load

P2 stores JSONB for profile queries and canonical bytes for commitments. Original-result loading validates payload/envelope bytes and hashes, but full history scans are future work.

## P1 — Integration workflow may not execute

**State:** `OPEN`

The workflow definition is not evidence. Connector-created commits have previously produced no run.

Required proof: exact run IDs and matrix jobs; no missing run may be described as PASS.

## P1 — Deletion semantics still delete no bytes

**State:** `OPEN`

P2 adds no deletion execution. Backups, exports, indexes, keys and provider acknowledgements remain outside evidence.

## P1 — Assertion-level conformance remains absent

**State:** `OPEN`

All 72 assertion results remain runtime `UNSUPPORTED` until a P4 adapter emits complete assertion-scoped evidence.

## P1 — License/publication terms unresolved

**State:** `OPEN`, Issue #18

Psycopg is declared for CI/profile integration but not vendored or packaged. Repository publication/contribution decisions remain separate.

## P1 — Cross-project authority leakage

**State:** `OPEN`

P2 does not authorize Titan, Mentaury or Crystal integration, shared storage, identity or inherited conformance.

## Update rule

Never close a risk through prose, operator approval, local unit tests, code presence or a workflow definition alone. Record exact environment, SHA, result, limitations and remaining proof.
