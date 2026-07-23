# ADR-0003: Semantic conflicts require explicit resolution

- **Decision status:** `PROPOSED`
- **Evidence level:** `DOCUMENTED`
- **Implementation status:** `NOT_STARTED`
- **Date:** `2026-07-23`
- **Deciders:** pending operator decision
- **Track:** `Architecture Canon / Abstract Contract`
- **Related:** `ARCHITECTURE.md`, `STATUS.md`, `ROADMAP.md`
- **Tags:** `conflict, contradiction, multi-writer, epistemic-state`

## Context 🧭

Native Kernel already distinguishes:

- candidate contradiction from established contradiction;
- conflict detection from conflict resolution;
- relevance from epistemic validity;
- write order from represented-world validity.

Future decentralized or multi-writer systems may introduce several different failure classes. Treating all of them as one generic conflict risks silent semantic loss.

```text
duplicate delivery
≠ write-version race
≠ divergent history
≠ semantic contradiction
≠ epistemic disagreement
≠ projection drift
```

No complete conflict lifecycle, OCC contract, CRDT policy, multi-writer merge, or human-review API is currently implemented.

## Decision drivers 🎯

- preserve incompatible Claims and provenance;
- prevent last-write order from becoming truth;
- distinguish technical collisions from semantic disagreement;
- support replayable resolution history;
- permit future decentralized implementations without silent merge;
- avoid prematurely choosing one algorithm or storage model.

## Considered options 🧪

### Option A — Last Write Wins for all conflicts

**Advantages**

- deterministic and simple;
- low implementation cost.

**Disadvantages**

- time/order becomes semantic authority;
- contradictory evidence may disappear;
- provenance and minority states are lost.

### Option B — Automatic semantic merge

**Advantages**

- minimal operator burden;
- attractive for distributed systems.

**Disadvantages**

- merge logic may invent meaning;
- domain-specific contradictions cannot be resolved generically;
- hidden uncertainty becomes false certainty.

### Option C — Explicit Conflict Set and explicit resolution record

**Advantages**

- both sides remain visible;
- provenance and temporal scope are preserved;
- resolution becomes replayable and auditable;
- technical ordering remains separate from semantic judgment.

**Disadvantages**

- requires lifecycle design and operator/policy interfaces;
- unresolved conflicts may remain open;
- distributed implementations become more complex.

## Proposed decision 💭

Semantic conflicts should remain visible until an explicit resolution decision is recorded.

Write order may establish deterministic ordering, but it must not independently establish semantic correctness.

A future Conflict Set contract may include:

```text
conflict_id
conflict_class
involved_claims_or_histories
detection_basis
candidate_or_established_status
provenance
temporal_scope
opened_at
review_state
resolution_history
receipts
```

Possible lifecycle concepts:

```text
CONFLICT_OPENED
CONFLICT_REVIEWED
CONFLICT_RESOLVED
CONFLICT_REOPENED
```

These names are proposals only. They are not added to the current event vocabulary by this ADR.

## Proposed conflict classes

| Class | Meaning | Default architectural response |
|---|---|---|
| Duplicate delivery | Same command/event observed again | Idempotency contract; no semantic promotion |
| Write-version race | Concurrent technical write collision | Retry, branch, or explicit failure according to profile |
| Divergent history | Histories share an ancestor and then diverge | Preserve divergence; evaluate merge policy |
| Semantic contradiction | Claims cannot jointly hold under declared scope | Open/maintain Conflict Set |
| Epistemic disagreement | Evidence or status differs without direct contradiction | Preserve evidence and status differences |
| Projection drift | Derived view differs from replay | Rebuild projection; do not rewrite history |
| Schema/order conflict | Event versions or ordering cannot be interpreted safely | Fail closed or use explicit migration/upcast policy |

## Proposed invariants 🔒

1. Last Write Wins must not independently determine semantic truth.
2. Candidate conflict must not be reported as established conflict.
3. Detection must not silently resolve a conflict.
4. Conflicting Claims and provenance remain visible until explicit resolution or supersession.
5. Resolution must be represented through explicit history, not mutable overwrite.
6. Projection drift is corrected by rebuilding projection, not rewriting authoritative history.
7. Technical ordering and semantic validity remain separate dimensions.
8. Conflict policy must not be silently added to Issue #1.

## Non-decisions 🚫

This ADR does not yet select:

- OCC or compare-and-swap semantics;
- event or command idempotency schema;
- Claim-per-stream boundaries;
- CRDT acceptance or prohibition;
- LWW for non-semantic data;
- decentralized branch exchange protocol;
- hash-tip or common-ancestor algorithm;
- human-in-the-loop API;
- automatic policy resolution;
- integration with Crystal TruthGate;
- exact lifecycle event names.

A future implementation may use CRDT-like or other mathematical mechanisms internally, but it must still preserve the explicit semantic conflict contract. The architecture rejects silent semantic resolution, not a mathematical technique by name.

## Required evidence before acceptance 🧪

- formal conflict taxonomy review;
- concrete examples for technical and semantic conflict classes;
- replayable resolution model;
- tests showing unresolved conflicts remain visible;
- tests showing write order does not determine truth status;
- projection-drift rebuild tests;
- threat model for multi-writer scenarios;
- failure and rollback analysis;
- operator approval.

## Consequences if accepted 📌

### Positive

- stronger epistemic honesty;
- auditable resolution;
- compatibility with future decentralized profiles;
- reduced risk of silent information loss.

### Negative

- more complex state and interfaces;
- unresolved conflicts may accumulate;
- automatic merge becomes intentionally bounded.

## Issue #1 boundary

The exact `v0.1.2.1` import remains unchanged. This proposal does not add new conflict events, OCC, CRDT, or multi-writer code to the import PR.
