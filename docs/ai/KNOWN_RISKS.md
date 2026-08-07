# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-07  
**Last verified public `main`:** `bb94835ad612f45e2629655bc9add872d8981357`  
**Active work:** Issue #46 / PR #47

## P0 — Authentic source recovery remains unresolved

**State:** `OPEN`

```text
clean/postgresql-reference/0.1
≠ recovered v0.1.2.1
≠ original 44-test evidence
```

## P0 — P2 may be mistaken for a complete Kernel

**State:** `OPEN`

P2 repository evidence covers migrations, writer fencing, append/idempotency, rollback-safe ordering and tested concurrency. It does not cover replay/upcasters, projections, operational Receipts, deletion execution, API, conformance or ecosystem wiring.

Required control: public status remains `P2 PARTIAL / NOT PRODUCTION-READY`.

## P0 — PostgreSQL integration evidence may be overgeneralized

**State:** `NARROWED`

Run `31151297646` passed PostgreSQL 16/18 × Python 3.11/3.12. This closes the former “integration not run” gap for the bounded test scenarios.

It does not prove:

- arbitrary PostgreSQL configuration/version behavior;
- real host/process crash recovery;
- managed-provider failover;
- high-load throughput;
- production security, backup or restore;
- P3 replay/projection behavior.

## P0 — Durable append may be mistaken for replay conformance

**State:** `OPEN`

The adapter appends and returns original idempotent results. It does not execute reducer/upcaster replay or rebuild projections.

Required proof: separately authorized P3.

## P0 — Single-writer lease may be mistaken for consensus

**State:** `OPEN`

Owner/epoch/expiry fencing is one-profile single-writer coordination, not multi-writer consensus or cross-region leadership.

## P0 — Hash chain may be mistaken for authentication

**State:** `OPEN`

`nkp1`/`nke1` are integrity commitments, not signatures or external notarization.

## P1 — Migration operational safety

**State:** `OPEN`, partially controlled

Checksums and advisory locking are tested. Downgrade, managed rollout, long-lock behavior and restore-time migration remain untested.

## P1 — Writer lease behavior under operational faults

**State:** `OPEN`

Database failover, abrupt process death, network partitions and very long transactions require future fault evidence.

## P1 — Row-lock serialization throughput

**State:** `ACCEPTED TRADE-OFF / UNBENCHMARKED`

Contiguous instance-global ordering serializes authoritative appends per instance. Performance and contention limits are unknown.

## P1 — Psycopg/PostgreSQL may become accidental Canon

**State:** `OPEN`, controlled by profile separation

Cross-profile neutrality remains unproven until a materially independent profile and C3 comparison exist.

## P1 — Stored JSONB/canonical-byte divergence

**State:** `OPEN`, bounded checks present

Idempotent reads verify canonical payload/envelope bytes and hashes. Whole-history scanning and repair remain future work.

## P1 — Exact final-head workflow drift

**State:** `OPEN UNTIL MERGE GATE`

Evidence run `31151297646` is valid for its exact head. Any later code/manifest change requires rechecking affected workflows before merge.

## P1 — Deletion semantics still delete no bytes

**State:** `OPEN`

P2 adds no deletion execution for primary data, backups, exports, indexes or keys.

## P1 — Assertion-level conformance remains absent

**State:** `OPEN`

All 72 assertion statuses remain runtime `UNSUPPORTED` until P4.

## P1 — License/publication terms unresolved

**State:** `OPEN`, Issue #18

Psycopg is an integration dependency, not vendored code. Packaging and contribution terms remain separate.

## P1 — Cross-project authority leakage

**State:** `OPEN`

P2 does not authorize Titan, Mentaury or Crystal integration, shared storage or inherited conformance.

## Update rule

Never close a risk through prose, operator approval, code presence or one test layer alone. Record exact environment, SHA, run, limitations and remaining proof.
