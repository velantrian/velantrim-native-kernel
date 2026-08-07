# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-07  
**Last verified public `main`:** `07bf1cc955307783f8eaa3becbaa924087b8b325`  
**Latest merged phase:** C4 authority-free offline shadow evaluation / PR #62

C4 adds bounded repository evidence for an approved immutable recorded workload. It does not close source recovery, live-traffic, deletion, authenticity, conflict, restore, operational, security, licensing, exhaustive-equivalence or production risks.

## P0 — Offline shadow may be mistaken for live production shadowing

```text
approved synthetic recorded dataset
≠ captured production traffic
≠ replay of live user traffic
≠ deployed shadow runtime
```

**State:** `OPEN / PRIMARY C4 COMMUNICATION RISK`.

Future live evidence would require separately authorized privacy-safe capture/replay, governance, redaction, retention, incident controls and explicit authority isolation.

## P0 — Shadow observation may be mistaken for authority promotion

**State:** `OPEN`, machine-guarded.

```text
authority promotion:  FORBIDDEN
authoritative writes: FORBIDDEN
side effects:          FORBIDDEN
promotion decision:   NOT_AUTHORIZED
```

The evaluator must never become a command path, mutate authoritative history, approve a candidate or trigger actions.

## P0 — Passing 15 cases may be mistaken for exhaustive equivalence

**State:** `OPEN`.

The dataset covers all 45 C3-supported assertion IDs but only 15 recorded cases. It does not enumerate every Event sequence, failure interleaving, timing distribution, platform, configuration, fault model or adversarial input.

Future evidence would require generated histories, state-machine/property testing, mutation testing, broader fault injection and independent review.

## P0 — Synthetic observations can encode the expected answer

**State:** `OPEN / DESIGN LIMIT`.

Reference and candidate observations are recorded in the same approved dataset. Exact digest binding prevents unnoticed drift but does not prove independent generation or real operating conditions.

## P0 — Threshold or normalization drift

**State:** `OPEN`, machine-guarded but not eliminated.

Semantic/critical thresholds are zero. A future threshold or allowed-difference change could hide meaningful degradation. Any material change requires a new dataset version, digest, ADR/manifest update and evidence cycle.

Normalization must never remove canonical identity, payload, order, reducer/projection state, failure outcome, integrity commitment or Receipt proof differences.

## P0 — C4 may be mistaken for support for all 72 assertions

```text
SUPPORTED / C4 evaluated: 45
PARTIAL:                   10
UNSUPPORTED:               17
FAILED:                     0
```

**State:** `OPEN / PRIMARY ASSERTION-SCOPE RISK`.

All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

## P0 — C4 report/Receipt may be mistaken for truth or safety proof

**State:** `OPEN`.

`nk-shadow-report/1` and `nk-shadow-receipt/1` prove only that declared observations were compared under the recorded dataset digest and authority boundary. They do not prove truth, authenticity, production safety, physical deletion or external correctness.

## P0 — Authentic source recovery remains unresolved

```text
clean/postgresql-reference/0.1
+ clean/sqlite-embedded/0.1
+ approved C4 dataset
≠ v0.1.2.1
≠ original 44-test evidence
```

**State:** `OPEN`; Issue #1 remains independent. `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.

## P0 — C3/C4 may be mistaken for operational equivalence

**State:** `OPEN`.

Selected byte, structural, semantic and behavioural outcomes match. Concurrency, IAM, networking, replication, failover, administration, backup/restore, scale, managed-provider behaviour and filesystem durability are not equivalent.

## P0 — Assertion/dataset/evidence drift

**State:** `OPEN`, machine-guarded by:

- exact 72-ID report coverage;
- exact `45/10/17/0` counts;
- exact 45-ID C3-supported scope;
- approved 15-case dataset digest;
- one Receipt per case;
- `NK-EPI` non-promotion;
- zero semantic/critical divergence thresholds;
- exact repository SHA/run/environment;
- required limitations and authority boundary.

A JSON file alone is insufficient evidence; externally visible run, head, artifact digest and retained bytes are required.

## P0 — Physical deletion remains absent

**State:** `OPEN`.

Neither profile nor C4 deletes across primary data, backups, logs, exports, providers or keys. Recorded proof-boundary comparison is not deletion execution.

## P0 — Conflict subsystem remains incomplete

**State:** `OPEN / MOSTLY UNSUPPORTED`.

Candidate conflicts, mismatch dimensions, detection/resolution separation, resolution history and complete cross-profile conflict preservation remain absent.

## P0 — Restore visibility enforcement is absent

**State:** `OPEN`.

No restore pipeline reapplies deletion/restriction metadata before restored data becomes visible.

## P0 — Cross-project authority remains absent

**State:** `OPEN`.

Titan, Mentaury and Crystal inherit no Native Kernel identity, authority, storage, C4 observation or conformance. C4 does not authorize wiring.

## P1 — Evidence artifacts expire

**State:** `OPEN / RETENTION UNTIL 2026-09-06`.

Each C4 artifact contains PostgreSQL P4, SQLite P5, C3 equivalence and C4 shadow reports. Digests without retained bytes are not independently reproducible evidence.

## P1 — Dataset governance is repository-local

**State:** `OPEN`.

Approval relies on ADR-0020, Issue #61 and committed bytes. There is no separate signed dataset registry, reviewer quorum, revocation list or long-term immutable archive.

## P1 — Future Receipt volume and retention

**State:** `OPEN`.

The current dataset produces 15 Receipts. A larger corpus needs bounded storage, indexing, deduplication, retention and review without turning Receipts into authoritative state.

## P1 — Profile operational assumptions

**State:** `OPEN`.

SQLite network filesystems, multi-host writers, abrupt power loss and platform locking remain unproven. PostgreSQL failover, process death at every statement boundary, partitions, replica lag, managed-provider semantics, backup/restore and concurrency limits remain unproven.

## P1 — Replay cost and upcaster provenance

**State:** `OPEN`.

Both profiles replay from sequence 1; no trusted incremental checkpoint strategy exists. C3/C4 does not establish semantic correctness of every future upcaster.

## P1 — Accidental Canon

**State:** `OPEN`, controlled by documentation.

PostgreSQL, SQLite, Python, Psycopg, files, pragmas, locks, CI runners, JSON protocols and the evaluator remain replaceable technologies.

## P1 — Commitments may be mistaken for authentication or consensus

**State:** `OPEN`.

`nkp1`, `nke1`, `nks0`, `nkr0`, dataset SHA-256 and comparison digests are commitments, not signatures, notarization or Byzantine protection. Current fencing is not IAM, delegated authority audit, multi-region consensus or Byzantine consensus.

## P1 — License and publication terms unresolved

**State:** `OPEN`, Issue #18.

C4 adds no external runtime dependency and publishes no package, but publication, reuse, contribution and long-term evidence terms remain undecided.

## P1 — Exact-SHA publication continuity

**State:** `IMPLEMENTATION PR DRIFT CLOSED / CONTINUING CONTROL`.

PR #62 final-head evidence passed on `b7786c08…`; implementation-main evidence independently passed on `07bf1cc9…`. The documentation checkpoint must now reproduce its own C4/AI gates. Its later merge SHA must not be described as already covered by implementation-main evidence.

## Update rule

Record exact dataset ID/digest, assertion scope, SHA, run, artifacts, thresholds, limitations, authority boundary and next action. Never close a risk through approval, prose, code presence, one matrix, a C2/C3/C4 label or a manifest count alone.
