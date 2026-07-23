# ADR-0002: State Checkpoints are disposable replay accelerators

- **Decision status:** `PROPOSED`
- **Evidence level:** `DOCUMENTED`
- **Implementation status:** `NOT_STARTED`
- **Date:** `2026-07-23`
- **Deciders:** pending operator decision
- **Track:** `Abstract Contract / Implementation Profile`
- **Related:** `ARCHITECTURE.md`, `ROADMAP.md`, Issue #1
- **Tags:** `checkpoint, replay, performance, snapshot`

## Context 🧭

Replay cost may grow as authoritative event history becomes longer. A cached state checkpoint could accelerate reconstruction without changing event authority.

The term `snapshot` is currently overloaded and may refer to:

1. cached reducer state;
2. a structural read snapshot;
3. a frozen evaluation dataset used by Offline Shadow.

These meanings must not be conflated. Claim freshness must also remain separate from checkpoint completeness.

No checkpoint implementation is part of Issue #1, and the repository does not yet have performance evidence showing that persisted checkpoints are necessary.

## Decision drivers 🎯

- preserve authoritative event history;
- accelerate replay only when evidence justifies it;
- permit deletion and rebuild of caches;
- expose corruption and schema incompatibility;
- avoid coupling Canon to SQLite or Claim-per-stream;
- preserve terminology and maturity honesty.

## Considered options 🧪

### Option A — Always replay from the beginning

**Advantages**

- simplest authority model;
- no cache corruption risk.

**Disadvantages**

- replay may become expensive for long histories;
- hot-state recovery may scale poorly.

### Option B — Treat persisted current state as authoritative

**Advantages**

- fast reads;
- conventional CRUD implementation.

**Disadvantages**

- weakens event sourcing;
- silent state repair may rewrite meaning;
- replay and audit can diverge.

### Option C — Use disposable State Checkpoints

**Advantages**

- faster replay while preserving event authority;
- corruption can fall back to full replay;
- policy remains implementation-specific.

**Disadvantages**

- additional schema/version management;
- additional tests and observability;
- risk of accidental checkpoint canonization.

## Proposed decision 💭

Define a **State Checkpoint** as a discardable cached reducer state associated with an explicit authoritative-history position.

```text
checkpoint at source position V
+
authoritative history after V
=
current derived state
```

The abstract checkpoint contract should include:

```text
scope
source_position
reducer_version
state_schema_version
state_digest
created_at
optional source_tip_commitment
```

Exact table schemas, storage engines, checkpoint frequency, thresholds, retention, and checkpoint scope remain implementation-profile decisions.

## Proposed terminology

| Term | Meaning |
|---|---|
| **State Checkpoint** | Cached reducer state at a declared history position |
| **Read Snapshot** | Structural representation used by a read path |
| **Evaluation Snapshot** | Frozen dataset used for an evaluation experiment |
| **Claim freshness** | Operational recency/decay concept; unrelated to checkpoint coverage |
| **Replay completeness** | Whether the declared authoritative range has been fully reduced |

## Proposed invariants 🔒

1. Deleting every State Checkpoint must not destroy authoritative history.
2. Checkpoint plus uncovered authoritative history must equal full replay under a documented semantic-equivalence rule.
3. Corrupt or incompatible checkpoints must be discardable.
4. Checkpoint source position and reducer/schema version must be explicit.
5. A checkpoint must never be edited to repair authoritative meaning.
6. Checkpoint policy must remain an implementation profile unless later evidence justifies a stronger contract.
7. State Checkpoints must not be introduced into the exact Issue #1 import.

## Non-decisions 🚫

This ADR does not select:

- SQLite or another checkpoint store;
- `every_n` values;
- time or latency thresholds;
- `keep_last_k` retention;
- Claim-per-stream architecture;
- hash-chain requirements;
- asynchronous checkpoint creation;
- a `StaleSnapshotError` API;
- checkpoint implementation in `v0.1.2.2`.

## Required evidence before acceptance 🧪

- repository-reproduced replay benchmark;
- a demonstrated hot-history reconstruction cost;
- `checkpoint + tail == full replay` tests;
- corrupted-checkpoint fallback tests;
- schema/reducer-version compatibility tests;
- deletion-and-rebuild tests;
- failure and rollback analysis;
- explicit operator approval.

## Consequences if accepted 📌

### Positive

- bounded replay acceleration without replacing history;
- explicit terminology;
- portability across checkpoint stores.

### Negative

- more versioning and test obligations;
- possible operational complexity;
- continued risk of users treating cache as truth.

## Issue #1 boundary

Issue #1 remains an exact prototype and 44-test import. It must not acquire checkpoint code or semantic redesign through this proposal.
