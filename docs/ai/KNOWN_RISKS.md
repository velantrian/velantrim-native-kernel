# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-07  
**Last verified public `main`:** `db6d65f69f7fc0c42861e5ab45869ec9c2f3d8ad`  
**Latest implementation:** merged PR #56 / P4 assertion-scoped conformance

P4 makes support and non-support visible per assertion. It does not close source-recovery, deletion, authenticity, conflict, restore, operational, licensing or portability risks.

## P0 — Authentic source recovery remains unresolved

**State:** `OPEN`

```text
clean/postgresql-reference/0.1
≠ v0.1.2.1
≠ original 44-test evidence
```

Required proof: authentic bytes, provenance, hashes, original test inventory and a separate Issue #1 gate.

## P0 — Top-level C2 may be mistaken for complete support

**State:** `OPEN / PRIMARY P4 COMMUNICATION RISK`

```text
support_state: PARTIAL
kernel_runtime_conformance: C2
SUPPORTED: 41
PARTIAL: 13
UNSUPPORTED: 18
```

C2 applies only to the 41 `SUPPORTED` results. Every public summary must retain the counts and partial support state.

## P0 — C2 may be mistaken for C3

**State:** `OPEN`

Python/PostgreSQL matrix diversity is environment compatibility for one profile, not a materially independent implementation.

Required proof: separately authorized P5, independent SQLite profile, declared equivalence classes and retained comparison evidence.

## P0 — P4 evidence may be mistaken for truth or authenticity

**State:** `OPEN`

P4 proves only that declared checks passed at a named profile/SHA/run. It does not establish truth, external signatures/notarization, observation correctness, absence of privileged rewrite or complete integrity under every threat model.

## P0 — Assertion mapping drift

**State:** `OPEN`, narrowed by tests and manifest guards

Controls now require all 72 IDs exactly once, guarded counts, passed-check references, limitations, explicit failures and `NK-EPI` non-promotion. Mapping changes still require contract-owner review and artifact inspection.

## P0 — Environment metadata can be spoofed outside CI

**State:** `OPEN / ACCEPTED P4 LIMIT`

A local caller can supply arbitrary environment metadata. Credible C2 therefore requires independently visible GitHub run/head/artifact evidence. A JSON file alone is insufficient.

## P0 — Proposed NK-EPI may be mistaken for accepted support

**State:** `OPEN`, machine-guarded

All `NK-EPI-001…008` remain `UNSUPPORTED` with a `PROPOSED` limitation. Fixture execution does not accept ADR-0008.

## P0 — Physical deletion remains absent

**State:** `OPEN`

P1 models semantic states; P2 stores Events; P3 stores projections/Receipts; P4 reports boundaries. None deletes primary data, backups, logs, exports, providers or keys.

## P0 — Conflict subsystem remains incomplete

**State:** `OPEN / MOSTLY UNSUPPORTED`

Dedicated candidate conflicts, mismatch dimensions, detection/resolution separation, resolution history and cross-profile conflict preservation remain absent.

## P0 — Restore visibility enforcement is absent

**State:** `OPEN`

No restore pipeline reapplies deletion/restriction metadata before restored data becomes visible.

## P0 — Cross-project authority remains absent

**State:** `OPEN`

Titan, Mentaury and Crystal do not inherit Native Kernel identity, authority, storage or conformance. No runtime adapter is wired.

## P1 — Evidence artifacts expire

**State:** `OPEN / RETENTION 30 DAYS`

PR-head and main-bound P4 artifacts expire on 2026-09-06 unless retained elsewhere. Digests without bytes are not reproducible evidence.

Required future control: release-attached or long-retention policy after Issue #18/publication decisions.

## P1 — Adapter checks are bounded scenarios

**State:** `OPEN`

The checks are representative deterministic scenarios, not exhaustive state-space or threat-model exploration.

## P1 — PostgreSQL operational faults remain under-tested

**State:** `OPEN`

Failover, process death at every statement boundary, network partitions, managed-provider semantics, replica lag, backup/restore, long replay pressure and concurrency limits remain unproven.

## P1 — Full replay cost and snapshot pressure

**State:** `OPEN / UNBENCHMARKED`

Replay starts at sequence 1 under repeatable-read. No trusted checkpoint/incremental strategy or scale benchmark exists.

## P1 — Upcaster provenance and review

**State:** `OPEN`

P4 tests routing behavior, not semantic correctness of every future transform. Real migrations require reviewed source/target meaning and fixtures.

## P1 — Profile technologies may become accidental Canon

**State:** `OPEN`, controlled by documentation

Python, Psycopg, PostgreSQL, JSONB, SQL layouts, row locks and GitHub Actions remain replaceable profile choices.

## P1 — Hash commitments may be mistaken for authentication

**State:** `OPEN`

`nkp1`, `nke1`, `nks0` and `nkr0` are commitments, not signatures, external notarization or Byzantine protection.

## P1 — Authority adapter may be mistaken for operational security

**State:** `OPEN`

The local authority adapter has no real credentials, IAM, revocation, persisted delegation chain or operational audit.

## P1 — Single-writer fencing may be mistaken for consensus

**State:** `OPEN`

PostgreSQL owner/epoch/expiry fencing is not multi-writer, cross-region or Byzantine consensus.

## P1 — License and publication terms unresolved

**State:** `OPEN`, Issue #18

Publication, reuse, contribution and long-term evidence retention terms remain undecided.

## P1 — Final-head evidence drift

**State:** `CLOSED FOR PR #56 / OPEN AS CONTINUING CONTROL`

PR #56 final head and exact `main@db6d65f6…` both passed P4/P3/P2/P1/fixture/AI gates, and both retained four P4 artifacts. Future changes must repeat affected checks and must not reuse these run IDs as evidence for a different SHA.

## Update rule

Record exact support counts, SHA, run, artifacts, limitations and next action. Never close a risk through approval, prose, code presence, one matrix, a C2 label or a manifest count alone.
