# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-07  
**Last verified public `main`:** `1dc493e9d23b99ee4bbf6015348599cd56f6cb56`  
**Latest implementation:** Issue #58 / PR #59 / P5 SQLite + assertion-scoped C3

P5 provides bounded evidence across two materially different profiles. It does not close source-recovery, deletion, authenticity, conflict, restore, operational, security, licensing or exhaustive-equivalence risks.

## P0 — Authentic source recovery remains unresolved

**State:** `OPEN`

```text
clean/postgresql-reference/0.1 + clean/sqlite-embedded/0.1
≠ v0.1.2.1
≠ original 44-test evidence
```

Required proof: authentic bytes, provenance, hashes, original test inventory and a separate Issue #1 gate.

## P0 — Top-level C3 may be mistaken for complete support

**State:** `OPEN / PRIMARY P5 COMMUNICATION RISK`

```text
support_state: PARTIAL
kernel_runtime_conformance: C3
SUPPORTED: 45
PARTIAL: 10
UNSUPPORTED: 17
```

C3 applies only to the 45 `SUPPORTED` comparison results. Every public summary must retain the counts and partial support state.

## P0 — C3 may be mistaken for operational equivalence

**State:** `OPEN`

The comparison demonstrates selected byte, structural, semantic and behavioural outcomes. It does not demonstrate equal concurrency, IAM, networking, replication, failover, administration, backup/restore, scale or managed-provider behavior.

```text
semantic/behavioural equivalence
≠ operational capability equivalence
```

## P0 — Scenario-bounded comparison may be mistaken for exhaustive proof

**State:** `OPEN`

Eight cross-profile checks exercise deterministic declared scenarios. They do not enumerate every Event sequence, failure interleaving, SQLite pragma, PostgreSQL configuration, platform or threat model.

Required future proof: property/state-machine testing, larger generated histories, fault injection and independent review.

## P0 — Normalization can hide a forbidden difference

**State:** `OPEN`, narrowed by exact-import check

Independent workloads legitimately generate different Event IDs/timestamps. Normalization must exclude only declared profile-local fields and must never hide payload, order, state, outcome or Receipt differences.

Current control: exact PostgreSQL authoritative Event import into SQLite preserves Event bytes/hash chain and replays to the same state.

## P0 — C3 assertion mapping drift

**State:** `OPEN`, machine-guarded

The mapping from cross-profile checks to 72 assertion results is code. Counts alone cannot prove semantic correctness.

Current controls:

- all 72 IDs emitted exactly once;
- exact `45/10/17/0` counts guarded;
- supported results reference passed comparison checks;
- all results include limitations;
- the promotion set is exactly `NK-SEM-008`, `NK-ID-008`, `NK-EQV-002`, `NK-EQV-003`;
- all `NK-EPI` remain unsupported;
- repository run/artifact metadata is mandatory for C3 promotion.

## P0 — Environment metadata can be spoofed outside CI

**State:** `OPEN / ACCEPTED LIMIT`

Local callers can supply commit/run/version metadata. Credible C2/C3 requires independently visible GitHub run, head and artifact evidence. A JSON file alone is insufficient.

## P0 — Proposed NK-EPI may be mistaken for accepted support

**State:** `OPEN`, machine-guarded

All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`. Fixture execution and profile agreement do not accept ADR-0008.

## P0 — Physical deletion remains absent

**State:** `OPEN`

Both profiles model semantic deletion/restriction states and bounded Receipts. Neither executes deletion across primary data, backups, logs, exports, providers or keys.

## P0 — Conflict subsystem remains incomplete

**State:** `OPEN / MOSTLY UNSUPPORTED`

Candidate conflicts, mismatch dimensions, detection/resolution separation, resolution history and cross-profile conflict preservation remain absent.

## P0 — Restore visibility enforcement is absent

**State:** `OPEN`

No restore pipeline reapplies deletion/restriction metadata before restored data becomes visible.

## P0 — Cross-project authority remains absent

**State:** `OPEN`

Titan, Mentaury and Crystal do not inherit Native Kernel identity, authority, storage or conformance. No runtime adapter is wired.

## P1 — Evidence artifacts expire

**State:** `OPEN / RETENTION 30 DAYS`

P5 artifacts expire on 2026-09-06 unless retained elsewhere. Each artifact contains PostgreSQL, SQLite and C3 reports. Digests without bytes are not reproducible evidence.

Required future control: release-attached or long-retention policy after Issue #18/publication decisions.

## P1 — SQLite file and process assumptions

**State:** `OPEN`

The profile uses one local SQLite database file, WAL and `BEGIN IMMEDIATE`. Network filesystems, multi-host writers, abrupt power loss, filesystem corruption, platform-specific locking and long-running contention are not proven.

## P1 — PostgreSQL operational faults remain under-tested

**State:** `OPEN`

Failover, process death at every statement boundary, network partitions, replica lag, managed-provider semantics, backup/restore, long replay pressure and concurrency limits remain unproven.

## P1 — Full replay cost and snapshot pressure

**State:** `OPEN / UNBENCHMARKED`

Both profiles replay from sequence 1. No trusted checkpoint/incremental strategy or scale benchmark exists.

## P1 — Upcaster provenance and review

**State:** `OPEN`

Comparison tests routing and selected outputs, not semantic correctness of every future transform. Real migrations require reviewed source/target meaning and fixtures.

## P1 — Profile technologies may become accidental Canon

**State:** `OPEN`, controlled by documentation

Python, Psycopg, PostgreSQL, SQLite, SQL layouts, files, pragmas, locks and GitHub Actions remain replaceable profile choices.

## P1 — Hash commitments may be mistaken for authentication

**State:** `OPEN`

`nkp1`, `nke1`, `nks0` and `nkr0` are commitments, not signatures, external notarization or Byzantine protection.

## P1 — Authority and fencing may be mistaken for operational security or consensus

**State:** `OPEN`

The authority adapter has no real IAM/revocation/delegation audit. PostgreSQL lease fencing and SQLite `BEGIN IMMEDIATE` serialization are not multi-region or Byzantine consensus.

## P1 — License and publication terms unresolved

**State:** `OPEN`, Issue #18

SQLite is stdlib-backed and adds no external runtime dependency, but publication, reuse, contribution and long-term evidence retention terms remain undecided.

## P1 — Final-head evidence drift

**State:** `OPEN UNTIL PR #59 FINAL GATE`

Initial P5/C3 evidence applies to `d43a6ed2…`. Documentation and governance commits require P5/C3 and AI-context checks on one final exact PR head. Previous run IDs must not be reused as evidence for another SHA.

## Update rule

Record exact support counts, SHA, run, artifacts, limitations and next action. Never close a risk through approval, prose, code presence, one matrix, a C2/C3 label or a manifest count alone.
