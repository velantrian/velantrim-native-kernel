# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-07  
**Last verified public `main`:** `4f8cb0a8b7d9ca678a8578cf005b118fd6dff150`  
**Latest implementation:** Issue #55 / PR #56 / P4 assertion-scoped conformance

P4 makes support and non-support visible per assertion. It does not close source-recovery, physical deletion, external authenticity, conflict, restore, operational, security, licensing or portability risks.

## P0 — Authentic source recovery remains unresolved

**State:** `OPEN`

The reported `v0.1.2.1` source and original 44-test suite remain absent from accessible sources.

```text
clean/postgresql-reference/0.1
≠ v0.1.2.1
≠ original 44-test evidence
```

Required proof: authentic bytes, provenance, hashes, original test inventory and a separate Issue #1 gate.

## P0 — Top-level C2 may be mistaken for complete support

**State:** `OPEN / PRIMARY P4 COMMUNICATION RISK`

The P4 report has:

```text
support_state: PARTIAL
kernel_runtime_conformance: C2
SUPPORTED: 41
PARTIAL: 13
UNSUPPORTED: 18
```

`C2` applies only to the 41 `SUPPORTED` results. It does not promote the other 31 results.

Required control: every public summary must state both the support counts and `support_state: PARTIAL`.

## P0 — C2 may be mistaken for C3

**State:** `OPEN`

One PostgreSQL profile was reproduced in four environment combinations. The combinations share the same implementation profile and semantic code.

```text
Python/PostgreSQL matrix diversity
≠ materially independent profile
≠ cross-profile equivalence
≠ C3
```

Required proof: separately authorized P5, independent SQLite profile, declared equivalence classes and comparison evidence.

## P0 — P4 evidence may be mistaken for truth or authenticity

**State:** `OPEN`

P4 proves only that declared checks passed at the named profile/SHA/run. It does not establish:

- truth of recorded Claims;
- external signatures/notarization;
- correctness of observations;
- absence of every privileged rewrite;
- complete Event Integrity under every threat model.

Required control: retain explicit truth/authenticity limitations in every report and summary.

## P0 — Assertion mapping drift

**State:** `OPEN`, narrowed by unit and manifest guards

The mapping from 72 assertion IDs to `SUPPORTED/PARTIAL/UNSUPPORTED` is code. It can drift from implementation meaning even when counts remain unchanged.

Current controls:

- all 72 IDs emitted exactly once;
- exact support counts guarded;
- every supported/partial result references passed check IDs;
- all results require limitations;
- unknown and failed checks reject report generation;
- `NK-EPI` non-promotion is tested.

Required future control: contract-owner review for every mapping change and exact artifact comparison.

## P0 — Environment metadata can be spoofed outside repository CI

**State:** `OPEN / ACCEPTED P4 LIMIT`

The adapter receives commit/run/Python/PostgreSQL metadata through environment variables. A local caller can provide arbitrary values.

Credible C2 therefore requires an independently visible GitHub run and artifact bound to the named head. A JSON file alone is not sufficient C2 proof.

## P0 — Proposed NK-EPI may be mistaken for accepted support

**State:** `OPEN`, machine-guarded

All `NK-EPI-001…008` results remain `UNSUPPORTED` with a `PROPOSED` limitation. Running their fixtures does not accept ADR-0008.

## P0 — Physical deletion remains absent

**State:** `OPEN`

P1 models semantic deletion states. P2 stores Events. P3 stores projections and Receipts. P4 reports semantic/deletion boundaries. None executes deletion across primary data, backups, logs, exports, providers or keys.

Required proof: separately authorized location inventory, workers, idempotency/retry evidence, backup/restore behavior, provider evidence and security/legal review.

## P0 — Conflict subsystem remains incomplete

**State:** `OPEN / MOSTLY UNSUPPORTED`

Dedicated candidate-conflict representation, mismatch dimensions, detection/resolution separation, resolution history and cross-profile conflict preservation remain unsupported. `UNKNOWN` and selected non-truth boundaries do not constitute a full conflict engine.

## P0 — Restore visibility enforcement is absent

**State:** `OPEN`

The profile has no restore pipeline that reapplies deletion/restriction metadata before restored data becomes visible.

## P0 — Cross-project authority remains absent

**State:** `OPEN`

P4 does not authorize Titan, Mentaury or Crystal to inherit Native Kernel identity, authority, conformance or storage. No runtime adapter is wired.

## P1 — Evidence artifacts expire

**State:** `OPEN / RETENTION 30 DAYS`

Initial P4 artifacts expire after 30 days unless retained elsewhere. Artifact digests are recorded, but digests without bytes are not reproducible evidence.

Required future control: release-attached or long-retention evidence policy after Issue #18/publication decisions.

## P1 — Adapter checks are bounded scenarios

**State:** `OPEN`

P4 checks representative deterministic scenarios, not exhaustive state-space exploration. Passing them does not establish behavior under every input, scale or threat model.

## P1 — PostgreSQL operational faults remain under-tested

**State:** `OPEN`

Not covered comprehensively:

- failover;
- process death at every statement boundary;
- network partitions;
- managed-provider semantics;
- replica lag;
- backup/restore;
- long-running replay pressure;
- concurrency/throughput limits.

## P1 — Full replay cost and snapshot pressure

**State:** `OPEN / UNBENCHMARKED`

P3/P4 replay from sequence 1 under repeatable-read. Large histories may create I/O, memory and vacuum pressure. No trusted checkpoint/incremental strategy is implemented.

## P1 — Upcaster provenance and review

**State:** `OPEN`

P4 tests registry behavior, not the semantic correctness of every future transform. Real migrations require reviewed source/target meaning and fixtures.

## P1 — Profile technologies may become accidental Canon

**State:** `OPEN`, controlled by documentation

Python, Psycopg, PostgreSQL, JSONB, SQL layouts, row locks and artifact workflows are replaceable profile choices. P4/C2 does not make them Architecture Canon.

## P1 — Hash commitments may be mistaken for authentication

**State:** `OPEN`

`nkp1`, `nke1`, `nks0` and `nkr0` are integrity/profile commitments, not signatures, external notarization or Byzantine protection.

## P1 — Authority adapter may be mistaken for operational security

**State:** `OPEN`

The P1 authority adapter is deterministic and explicit but has no real credentials, IAM, revocation, delegated-chain persistence or operational audit.

## P1 — Single-writer fencing may be mistaken for consensus

**State:** `OPEN`

PostgreSQL owner/epoch/expiry fencing is not multi-writer, cross-region or Byzantine consensus.

## P1 — License and publication terms unresolved

**State:** `OPEN`, Issue #18

Psycopg is an integration dependency but is not vendored. Publication, reuse, contribution and long-term artifact terms remain undecided.

## P1 — Final-head evidence drift

**State:** `OPEN UNTIL PR #56 MERGE GATE`

Initial C2 evidence applies to `93710131…`. Documentation and governance commits require P4 and AI-context checks on one final exact PR head before merge.

## Update rule

Record exact support counts, SHA, run, artifacts, limitations and next action. Never close a risk through approval, prose, code presence, one matrix, a C2 label or a manifest count alone.
