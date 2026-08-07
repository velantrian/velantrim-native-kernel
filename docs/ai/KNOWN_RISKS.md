# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-07  
**Last verified public `main`:** `a8bb0ae232b977856730a1a4f21f977c1f69ca0a`  
**Latest implementation:** P5 SQLite + assertion-scoped PostgreSQL↔SQLite C3

P5 provides bounded evidence across two materially different profiles. It does not close source-recovery, deletion, authenticity, conflict, restore, operational, security, licensing or exhaustive-equivalence risks.

## P0 — Authentic source recovery remains unresolved

```text
clean/postgresql-reference/0.1 + clean/sqlite-embedded/0.1
≠ v0.1.2.1
≠ original 44-test evidence
```

**State:** `OPEN`; Issue #1 remains independent.

## P0 — C3 may be mistaken for complete support

```text
support_state: PARTIAL
SUPPORTED: 45
PARTIAL: 10
UNSUPPORTED: 17
```

**State:** `OPEN / PRIMARY COMMUNICATION RISK`. C3 applies only to 45 supported results.

## P0 — C3 may be mistaken for operational equivalence

**State:** `OPEN`. Selected byte/structural/semantic/behavioural outcomes match; concurrency, IAM, networking, replication, failover, administration, backup/restore, scale and managed-provider behavior are not equivalent.

## P0 — Scenario-bounded comparison may be mistaken for exhaustive proof

**State:** `OPEN`. Eight checks do not enumerate every Event sequence, failure interleaving, SQLite pragma, PostgreSQL configuration, platform or threat model.

Required future evidence: generated histories, state-machine/property testing, fault injection and independent review.

## P0 — Normalization can hide a forbidden difference

**State:** `OPEN`, narrowed by exact-import evidence. Normalization may exclude only declared profile-local IDs/timestamps; it must never hide payload, order, state, outcome or Receipt differences.

## P0 — C3 assertion mapping drift

**State:** `OPEN`, machine-guarded by:

- exact 72-ID coverage;
- exact `45/10/17/0` counts;
- passed comparison-check references;
- required limitations;
- exact four-assertion promotion set;
- `NK-EPI` non-promotion;
- repository run/artifact requirements.

## P0 — Environment metadata can be spoofed outside CI

**State:** `OPEN / ACCEPTED LIMIT`. A JSON file alone is insufficient C2/C3 evidence; exact visible run/head/artifact evidence is required.

## P0 — Proposed NK-EPI may be mistaken for accepted support

**State:** `OPEN`, machine-guarded. All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

## P0 — Physical deletion remains absent

**State:** `OPEN`. Neither profile deletes across primary data, backups, logs, exports, providers or keys.

## P0 — Conflict subsystem remains incomplete

**State:** `OPEN / MOSTLY UNSUPPORTED`. Candidate conflicts, mismatch dimensions, detection/resolution separation, resolution history and cross-profile conflict preservation remain absent.

## P0 — Restore visibility enforcement is absent

**State:** `OPEN`. No restore pipeline reapplies deletion/restriction metadata before restored data becomes visible.

## P0 — Cross-project authority remains absent

**State:** `OPEN`. Titan, Mentaury and Crystal inherit no Native Kernel identity, authority, storage or conformance.

## P1 — Evidence artifacts expire

**State:** `OPEN / RETENTION UNTIL 2026-09-06`. Each P5 artifact contains PostgreSQL, SQLite and C3 reports. Digests without retained bytes are not reproducible evidence.

## P1 — SQLite operational assumptions

**State:** `OPEN`. Network filesystems, multi-host writers, abrupt power loss, filesystem corruption, platform-specific locking and long contention are not proven.

## P1 — PostgreSQL operational faults remain under-tested

**State:** `OPEN`. Failover, process death at every statement boundary, partitions, replica lag, managed-provider semantics, backup/restore and concurrency limits remain unproven.

## P1 — Replay cost and snapshot pressure

**State:** `OPEN / UNBENCHMARKED`. Both profiles replay from sequence 1; no trusted incremental checkpoint strategy exists.

## P1 — Upcaster provenance

**State:** `OPEN`. Current comparisons do not establish semantic correctness of every future transform.

## P1 — Profile technologies may become accidental Canon

**State:** `OPEN`, controlled by documentation. PostgreSQL, SQLite, Python, Psycopg, files, pragmas and locks remain replaceable.

## P1 — Commitments may be mistaken for authentication

**State:** `OPEN`. `nkp1`, `nke1`, `nks0` and `nkr0` are commitments, not signatures, notarization or Byzantine protection.

## P1 — Fencing may be mistaken for consensus/security

**State:** `OPEN`. Current authority/fencing is not IAM, delegated authority audit, multi-region consensus or Byzantine consensus.

## P1 — License and publication terms unresolved

**State:** `OPEN`, Issue #18. SQLite adds no external runtime dependency, but publication/reuse/contribution/long-term evidence terms remain undecided.

## P1 — Final-head evidence drift

**State:** `CLOSED FOR PR #59 / CONTINUING CONTROL`.

Final PR head `6483c9a2…` passed P5/C3, P4, P1, fixtures and AI-context with four artifacts. Implementation main `a8bb0ae2…` repeated those gates and produced four main-bound artifacts. Any later source or documentation change must use new exact-SHA evidence rather than reusing these runs.

## Update rule

Record exact support counts, SHA, run, artifacts, limitations and next action. Never close a risk through approval, prose, code presence, one matrix, a C2/C3 label or a manifest count alone.
