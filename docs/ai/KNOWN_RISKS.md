# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-07  
**Last verified public `main`:** `4af642930e18752f8f8b0bce75df355f76100d6f`  
**Latest implementation:** PR #50 / P3 replay, projection rebuild and bounded Receipts — merged

P3 repository integration narrows the persisted-replay and projection gap. It does not close physical deletion, external authenticity, complete Event Integrity, operational fault, security, privacy, licensing, portability or conformance risks.

## P0 — Authentic source recovery remains unresolved

**State:** `OPEN`

The reported `v0.1.2.1` source and original 44-test suite remain absent from accessible sources.

Required proof: authentic bytes, lineage, hashes, original test inventory and explicit Issue #1 operator gate.

## P0 — Clean P1/P2/P3 may be mistaken for recovered history

**State:** `OPEN`, narrowed by ADR-0015…0017 and manifest guards

```text
clean/postgresql-reference/0.1
≠ v0.1.2.1
≠ original 44-test evidence
```

Every future package, report and release must preserve this boundary.

## P0 — P3 profile may be mistaken for a complete Kernel

**State:** `OPEN`

P1 implements semantic identity/objects/authority/reduction. P2 implements bounded PostgreSQL append/idempotency. P3 implements bounded persisted replay, disposable projection rebuild and operational Receipts.

Still missing: physical deletion, network/API surface, P4 complete assertion evidence, P5 independent profile, C1/C2/C3 and production operation.

Required control: public surfaces use `P3 PARTIAL / NOT PRODUCTION-READY`.

## P0 — Replay integrity may be mistaken for truth or authenticity

**State:** `OPEN`

P3 validates selected-instance sequence, canonical bytes, `nkp1`/`nke1` commitments, one global hash chain, explicit schema routing and deterministic reduction.

This does not establish:

- truth of recorded Claims;
- signatures or external notarization;
- protection from every privileged rewrite that also updates all internal commitments;
- correctness of external observations or actor identities.

Required proof for authenticity: separately governed signing/key/notarization or external-evidence design.

## P0 — P3 Receipt may be mistaken for unlimited proof

**State:** `OPEN`, narrowed by Python and SQL overclaim guards

P3 Receipts are bounded to one selected replay/rebuild operation. They explicitly set truth, external-authenticity, complete-integrity and complete-erasure claims to false.

Required control: never summarize a P3 Receipt as truth certification, complete Event Integrity, physical erasure, C-level conformance or production validation.

## P0 — P3 integration may be mistaken for C1/C2

**State:** `OPEN`, machine-readable guard retained

Final PR evidence:

```text
head 7e615bc633cbf966211d3b2815f51b8ff9eb9716
P3 run 31173133661 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
P2 regression run 31173133709 — PASS
```

This establishes the bounded P3 scenarios in the declared matrix. It does not establish complete assertion-scoped profile support, release artifacts, independent-profile equivalence or operational guarantees.

```text
kernel_runtime_conformance: UNSUPPORTED
C1/C2/C3: NOT_ESTABLISHED
```

## P0 — Provisional digests may become accidental Canon

**State:** `OPEN`

`nkd0`, `nks0` and P3 `nkr0` remain clean-profile implementation details. `nkp1` and `nke1` implement accepted fixture algorithms, while PostgreSQL rows/envelopes/projection layouts remain profile-specific.

Required control: no unrelated profile or migration may depend on implementation-only layouts/digests without explicit contract review.

## P0 — Hash chain may be mistaken for authentication

**State:** `OPEN`

`nkp1`/`nke1` detect tested inconsistencies but are not signatures, external notarization or defense against every privileged rewrite.

## P0 — Disposable projection may be mistaken for authority

**State:** `OPEN`, narrowed by design and tests

The projection can be destroyed and rebuilt. It is not authoritative history and must not be used to admit facts, bypass Event history or establish truth.

Required control: all repair/rebuild logic continues to derive from authoritative Events.

## P0 — Stale-head protection is optimistic, not consensus

**State:** `OPEN / ACCEPTED BOUNDED MODEL`

P3 compares the captured snapshot head with a locked current instance head before publication. This prevents publishing a projection after an ordinary concurrent append.

It is not multi-writer consensus, cross-database atomicity, cross-region leadership or Byzantine protection.

## P1 — Exact final-head workflow drift

**State:** `NARROWED / PR #50 GATE COMPLETE`

PR #50 final head `7e615bc6…` passed P3, P2, P1, fixture and AI-context workflows before squash merge `4af64293…`. No push-to-main run was recorded. Any future implementation change requires new exact-head evidence; this checkpoint does not carry PR #50 evidence forward to later code automatically.

## P1 — Python may become accidental permanent architecture

**State:** `OPEN`, narrowed

P1–P3 use Python as a reversible profile choice. Semantic contracts must remain independent from dataclasses, module layout and Python-only behavior.

## P1 — Psycopg/PostgreSQL may become accidental Canon

**State:** `OPEN`, controlled by profile separation

Psycopg, SQL schema, JSONB, bytea, row locks, isolation modes and indexes are profile technologies. Cross-profile neutrality remains unproven until P5/C3 evidence.

## P1 — Upcaster graph is intentionally narrow

**State:** `ACCEPTED P3 LIMIT`

`UpcasterRegistry` permits one successor per source version and one deterministic path to the target. It rejects branching/ambiguous paths.

Future multi-branch migration policy requires a separate semantic contract; do not silently broaden the registry.

## P1 — Upcaster code provenance and audit

**State:** `OPEN`

An upcaster can transform persisted payload semantics. P3 proves deterministic invocation and failure behavior, not the correctness or security of every future transformation.

Required proof before adding real migrations: reviewed transform code, fixtures, source/target semantics and replay comparison evidence.

## P1 — Repeatable-read snapshot performance

**State:** `OPEN / UNBENCHMARKED`

P3 reads the full selected-instance history from sequence `1`. Large histories may hold snapshots for long periods and create memory, I/O or vacuum pressure.

Required evidence: scale benchmarks, pagination/streaming design, cancellation, observability and operational limits.

## P1 — Full replay cost and checkpoint strategy

**State:** `OPEN`

P3 deliberately proves replay from empty. It does not yet provide trusted checkpoints, incremental rebuild or bounded replay windows.

Any checkpoint optimization must remain disposable and verify its relationship to authoritative history.

## P1 — Projection generation contention

**State:** `OPEN / LOW-SCALE TESTED`

Generation is derived from committed rebuild Receipts while the instance row is locked. Concurrent rebuild throughput and contention limits are not benchmarked.

## P1 — Receipt/projection retention growth

**State:** `OPEN`

Every committed rebuild retains a Receipt. Long-term retention, compaction, export and deletion policies are unresolved. Receipt history must not be silently deleted as routine projection cleanup.

## P1 — Stored JSONB/canonical-byte divergence

**State:** `OPEN`, broader checks added

P3 verifies Event, projection and Receipt canonical bytes on relevant read paths. Whole-database periodic scan, repair tooling and external audit remain absent.

## P1 — Database operational faults

**State:** `OPEN`

Tests cover transaction rollback and ordinary concurrent append/rebuild. They do not cover failover, abrupt process death at every statement, network partitions, managed-provider behavior, replica lag or restore from backup.

## P1 — Migration operational safety

**State:** `OPEN`, partially controlled

Checksums and advisory locking are tested. Downgrade, partial rollout, long-lock behavior, managed migrations and restore-time migration remain untested.

## P1 — Authority adapter may be mistaken for operational security

**State:** `OPEN`

P2 calls explicit authority before append, but the local authority adapter has no credentials, identity provider, revocation, persisted delegation or operational audit.

## P1 — Single-writer lease may be mistaken for consensus

**State:** `OPEN`

Owner/epoch/expiry fencing serializes one PostgreSQL profile. It is not multi-writer consensus, cross-region leadership or Byzantine protection.

## P1 — Row-lock serialization throughput

**State:** `ACCEPTED TRADE-OFF / UNBENCHMARKED`

Contiguous instance-global ordering serializes authoritative appends per instance. Performance and contention limits are unknown.

## P1 — Deletion semantics may be mistaken for byte deletion

**State:** `OPEN`

P1 validates semantic transitions; P2 stores Events; P3 stores projections and Receipts. None deletes primary data, backups, indexes, logs, exports, provider data or keys.

Required proof: separately authorized location inventory, deletion workers, retry/failure evidence, backup/restore behavior and security/legal review.

## P1 — Accepted contracts remain only partially implemented

**State:** `OPEN`

P1–P3 exercise selected NK-ID, NK-SEM, NK-AUT, NK-EVT and deletion paths. They do not emit complete assertion-level evidence.

All 72 assertions remain runtime `UNSUPPORTED` until P4.

## P1 — Proposed ADRs/NK-EPI may be hidden by implementation progress

**State:** `OPEN`

ADR-0002, ADR-0004 and ADR-0008 retain their own statuses. `NK-EPI-001…008` remain proposed. P3 mechanisms do not silently accept or promote them.

## P1 — Storage neutrality remains unproven

**State:** `OPEN`

One PostgreSQL profile exists. C3 requires a materially independent second profile and declared semantic equivalence.

## P1 — Cross-project authority leakage

**State:** `OPEN`

P3 does not authorize Titan, Mentaury or Crystal integration, shared storage, identity, authority or inherited conformance.

## P1 — License and contribution terms unresolved

**State:** `OPEN`, Issue #18

Psycopg is declared as an integration dependency but not vendored or packaged. Publication, reuse and contribution terms remain undecided.

## Update rule

Record exact state, evidence, SHA, remaining uncertainty and next action. Never close a risk through prose, approval, code presence, one matrix, one Receipt or manifest coverage alone.
