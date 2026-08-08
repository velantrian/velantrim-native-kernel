# ADR-0024: Version reducer referential semantics without rewriting history

- **Decision status:** `PROPOSED`
- **Evidence level:** `DOCUMENTED`
- **Implementation status:** `NOT_STARTED`
- **Operator approval:** `PENDING`
- **Date:** `2026-08-08`
- **Deciders:** pending `@velantrian` decision
- **Track:** `Abstract Contract / Clean Implementation`
- **Related:** Issue #74, ADR-0003, ADR-0006, ADR-0012, ADR-0015, PR #72, PR #73
- **Tags:** `reducer, referential-integrity, replay, compatibility, supersession, links`

> [!IMPORTANT]
> The current `nk-p1-reducer/1` is part of already published P1–C5 evidence. Tightening its behavior in place would reinterpret old Event histories. This proposal therefore separates a future strict reducer contract from historical reducer v1 and does not authorize runtime changes.

## Context 🧭

The current reducer validates Event version and sequence, then applies structurally valid payloads to an immutable semantic state. It does not currently require referenced Claims to have been admitted and does not constrain supersession topology.

Observed behavior includes:

```text
LINK unknown source or target              accepted by reducer v1
UTILIZED unknown or erased Claim           accepted by reducer v1
SUPERSEDED unknown source or successor      accepted by reducer v1
SUPERSEDED self-reference or cycle          not rejected by reducer v1
SUPERSEDED different second successor       silently replaces prior mapping
ERASED unknown Claim                        accepted by reducer v1
generic LINK self-reference or cycle        not classified
```

Existing tests intentionally admit Claim `a`, then link and supersede it to Claim `b` without first admitting `b`. This behavior is repository evidence for reducer v1 and cannot be silently changed after publication.

PostgreSQL and SQLite replay currently import one process-wide `REDUCER_VERSION`. A direct constant change would cause all histories to be replayed under new semantics without an instance-level compatibility declaration.

- **Problem:** define honest referential semantics without rewriting already evidenced history.
- **Constraints:** deterministic replay, technology neutrality, explicit versioning, no silent semantic migration, generic relation extensibility, and fail-closed strict behavior.
- **Non-goals:** implement runtime v2, add Event verbs, implement conflict resolution, implement NK-EPI-004, define causal truth, or integrate another Velantrim project.
- **Current implementation boundary:** only `nk-p1-reducer/1` exists; no strict reducer or per-instance reducer-version selection exists.
- **Source-derived facts:** reducer v1 accepts dangling references; replay uses a global reducer version; typed relations may be cyclic or reflexive; supersession requires a coherent successor chain.
- **Open uncertainty:** exact profile schema for reducer-version selection, old-history migration protocol, relation registry, restoration after logical erasure, and Receipt shape for validation/migration.

## Inputs considered 🔍

```text
Repository evidence:
- native_kernel/semantic_core/reducer.py performs no referential validation
- tests/test_semantic_core.py relies on a not-yet-admitted LINK/SUPERSEDED target
- PostgreSQL and SQLite replay bind to one imported REDUCER_VERSION
- ADR-0003 rejects silent semantic resolution
- ADR-0006 permits typed directed relation graphs and defers relation-specific rules

Codex review lessons:
- integrity comparisons must be type-exact and evidence identities exact
- follow-up changes must not relabel earlier artifacts as proof of later code

External AI-generated inputs supplied by the operator:
- several audits recommended explicit dangling/self/cycle rules
- one recommendation treated cycle handling generically; repository review narrowed this to relation-specific topology and supersession cycles

Operator interpretation:
- current instruction authorizes continued investigation and proposal drafting
- final acceptance of this abstract contract remains a separate operator decision
```

AI-generated inputs are design inputs, not evidence or approval.

## Decision drivers 🎯

- preserve historical replay and evidence identity;
- prevent unknown or erased references from becoming silent current state;
- prevent supersession cycles and last-write overwrite;
- avoid imposing false acyclicity on generic typed relations;
- keep relation meaning outside storage technology;
- make failures deterministic and cross-profile testable;
- require explicit migration rather than inference from current code or date.

## Considered options 🧪

### Option A — Tighten `nk-p1-reducer/1` in place

**Advantages**

- smallest code diff;
- every replay immediately receives stricter validation.

**Disadvantages**

- changes the meaning of existing Event histories;
- invalidates current fixtures and prior evidence boundaries;
- makes historical replay depend on whichever code version is installed;
- silently converts a new policy into old Canon.

### Option B — Add strict checks outside the reducer only

**Advantages**

- append-time admission can fail early;
- reducer v1 remains unchanged.

**Disadvantages**

- imported or corrupted history can bypass append-time checks;
- replay would not independently verify referential semantics;
- PostgreSQL and SQLite adapters could diverge;
- semantics become profile policy rather than reducer contract.

### Option C — Version the strict reducer contract and require explicit selection

**Advantages**

- preserves v1 history exactly;
- makes strict behavior deterministic during append and replay;
- supports cross-profile fixtures;
- permits future relation-specific policies without rewriting generic topology;
- makes migration an explicit auditable act.

**Disadvantages**

- requires profile metadata and version dispatch;
- old histories remain v1 until explicitly validated or migrated;
- multiple reducer versions increase testing and maintenance cost.

## Proposed decision 💭

Select **Option C** if approved.

### Compatibility boundary

1. `nk-p1-reducer/1` remains readable with its published behavior.
2. No existing history, projection, Receipt, assertion report, or retained ZIP is relabelled as strict-reducer evidence.
3. A future strict contract uses a new reducer identifier; candidate identifier: `nk-p1-reducer/2`.
4. Reducer version is selected explicitly per Kernel instance or equivalent authoritative history boundary.
5. Selection must not be inferred from wall-clock date, software version, database type, current default, or first replay after upgrade.
6. Mixed reducer semantics inside one history are prohibited unless a separate migration contract defines an explicit boundary and replay algorithm.
7. A v1 history is not v2-conformant merely because its final projection resembles a v2 state.

### Proposed strict Event rules

#### `ADMIT`

- first admission of a Claim adds it to `admitted_claims`;
- repeated admission of the same non-erased Claim is a deterministic no-op while the Event remains in authoritative history;
- admission of a logically erased Claim fails closed;
- admission does not establish truth, authenticity, or epistemic validity.

#### `LINK`

- source and target Claims must already be admitted;
- source and target must not be logically erased at the Event position;
- an identical repeated `(source, relation, target)` link is a deterministic no-op;
- the generic reducer does **not** reject self-links or generic relation cycles globally;
- reflexivity, symmetry, transitivity, acyclicity, evidence, direction and other relation meaning require a separately accepted typed-relation contract;
- relation existence is not truth or causal proof.

#### `UTILIZED`

- the Claim must already be admitted and not erased;
- unknown or erased Claim utilization fails closed;
- utilization count is operational history, not truth, relevance authority, or epistemic promotion.

#### `SUPERSEDED`

- source and successor must already be admitted and not erased;
- source and successor must be different;
- repeated declaration of the same source/successor pair is a deterministic no-op;
- a different second successor for the same source fails closed; no last-write overwrite;
- adding the edge must not create a cycle in the `superseded_by` chain;
- successor chains are permitted, for example `A → B → C`;
- supersession records an explicit relation in history and does not silently erase the superseded Claim or prove the successor true.

#### `ERASED`

- the Claim must already be admitted;
- repeated erasure is a deterministic no-op;
- erasure does not delete or rewrite earlier Events, links, utilization, or supersession records;
- later LINK, UTILIZED, SUPERSEDED, or ADMIT operations involving that erased Claim fail closed under the strict reducer;
- this state remains logical erasure only and does not claim physical or cryptographic deletion.

### Deterministic failure surface

A future implementation should expose a dedicated bounded failure class such as `ReferentialIntegrityViolation`, derived from `ContractViolation`, with stable machine-readable reason codes. Candidate reasons:

```text
CLAIM_NOT_ADMITTED
CLAIM_ERASED
SELF_SUPERSESSION
SUPERSESSION_CONFLICT
SUPERSESSION_CYCLE
REDUCER_VERSION_UNDECLARED
REDUCER_VERSION_UNSUPPORTED
MIXED_REDUCER_HISTORY
```

Exact names are implementation details until separately authorized, but profiles must emit equivalent failure meaning.

## Required fixture matrix before runtime authorization 🧪

| Event | Case | Proposed strict result |
|---|---|---|
| ADMIT | first admission | PASS / add Claim |
| ADMIT | duplicate live Claim | PASS / no-op |
| ADMIT | erased Claim | FAIL |
| LINK | both admitted and live | PASS |
| LINK | unknown source | FAIL |
| LINK | unknown target | FAIL |
| LINK | erased endpoint | FAIL |
| LINK | duplicate exact edge | PASS / no-op |
| LINK | self-link | PRESERVE / relation-specific policy deferred |
| LINK | generic graph cycle | PRESERVE / relation-specific policy deferred |
| UTILIZED | admitted live Claim | PASS / increment |
| UTILIZED | unknown Claim | FAIL |
| UTILIZED | erased Claim | FAIL |
| SUPERSEDED | admitted live A → B | PASS |
| SUPERSEDED | duplicate A → B | PASS / no-op |
| SUPERSEDED | A → A | FAIL |
| SUPERSEDED | unknown endpoint | FAIL |
| SUPERSEDED | erased endpoint | FAIL |
| SUPERSEDED | A → B after A → C | FAIL |
| SUPERSEDED | A → B completing B → … → A | FAIL |
| ERASED | admitted Claim | PASS / mark erased |
| ERASED | duplicate erase | PASS / no-op |
| ERASED | unknown Claim | FAIL |

Fixtures must prove identical outcomes and equivalent failure reasons in the semantic core, PostgreSQL profile, SQLite profile, replay, projection rebuild, and cross-profile comparison before any support claim changes.

## Consequences 📌

### Positive

- old evidence remains honest and replayable;
- strict histories cannot silently accumulate dangling current references;
- supersession becomes a deterministic acyclic successor relation;
- generic relation graphs remain extensible rather than falsely constrained;
- append and replay can share one explicit contract;
- migration requires an auditable decision.

### Negative / accepted trade-offs

- v1 and a future v2 must coexist;
- storage profiles need explicit reducer-version metadata and dispatch;
- a v1 history with dangling references cannot be silently promoted;
- logical erasure may leave historical edges pointing to an erased Claim, which projections must represent honestly;
- relation-specific validity remains deferred.

### Neutral

- no assertion map, NK-EPI, C4/C5, production, deletion, or ecosystem status changes;
- no current Event vocabulary changes;
- Track H remains independent.

## Invariants 🔒

1. Published reducer v1 history is never replayed under v2 semantics without explicit authorization and migration evidence.
2. Reducer version is part of authoritative interpretation context, not a process-local default.
3. Strict referential validation runs during replay as well as append/admission.
4. Unknown and erased references fail closed under the strict contract.
5. Supersession never uses last-write overwrite and never forms a cycle.
6. Generic relation topology is not declared acyclic by the base reducer.
7. Logical erasure does not rewrite authoritative history or claim physical deletion.
8. Deterministic failure does not establish semantic falsehood; it only states that the Event is invalid under the declared reducer contract.
9. Profile technology does not change the result.
10. Acceptance of this ADR does not authorize implementation.

## Architecture-layer placement

| Question | Answer |
|---|---|
| Architecture Canon changed? | `no` |
| Abstract contract changed? | `proposed` |
| Implementation profile selected? | `no` |
| Runtime code exists? | `no strict reducer` |
| Production evidence exists? | `no` |

## Implementation notes 🔧

A separate authorization ADR/PR must define:

- authoritative storage of reducer version per instance/history;
- default for existing instances and newly created instances;
- version dispatcher API in the semantic core;
- PostgreSQL and SQLite schema migration;
- append-time validation and replay-time validation;
- projection and Receipt binding to exact reducer version;
- v1 validation report and optional migration protocol;
- stable failure reason representation;
- exact conformance fixtures and assertion-map impact;
- rollback to v1 for newly created experimental instances without rewriting history.

The safest initial implementation is likely:

```text
existing instances → explicit v1
new opt-in test instances → explicit v2
no automatic conversion
no mixed history
```

This is a design recommendation, not authorization.

## Validation and evidence 🧪

| Evidence | Artifact / command | Result | Required for next level |
|---|---|---|---|
| Repository review | reducer, tests, replay paths | gap reproduced | exact code references preserved in Issue #74 |
| Documentation | ADR-0024 + ADR index + roadmap/status | proposed contract | independent review + operator decision |
| Unit tests | none in this slice | `NOT_STARTED` | v1 regression + v2 matrix |
| Replay test | none in this slice | `NOT_STARTED` | exact per-version replay tests |
| Cross-profile test | none in this slice | `NOT_STARTED` | PostgreSQL/SQLite equivalence |
| Operator approval | pending | `PENDING` | explicit accept/reject/revise |

## Failure cases 🚨

- changing `REDUCER_VERSION` and replaying all old histories as v2;
- silently treating all existing instances as strict because deployment was upgraded;
- accepting at append time but skipping checks during replay;
- prohibiting every LINK cycle without a relation-specific contract;
- allowing a second successor to overwrite the first;
- removing historical edges when a Claim is erased;
- reporting referential failure as proof that the represented statement is false;
- claiming retained P1–C5 artifacts prove the future reducer;
- introducing Titan, Crystal, or Mentaury semantics into the reducer contract.

## Rollback / supersession

Because this slice is documentation-only, rollback is removal or revision before acceptance. If accepted later, a superseding ADR must preserve reducer v1 readability and explain migration consequences. Runtime rollback must select an already declared reducer version for a compatible history; it must never reinterpret an existing v2 history as v1 by changing a default.

## Consistency checklist 🔱

- [x] Event history remains authoritative about recorded changes.
- [x] History is not equated with truth.
- [x] Projection/cache is not promoted to Canon.
- [x] Relevance/utility is not equated with truth.
- [x] Candidate conflict is not described as resolved conflict.
- [x] Current technology is not silently promoted to permanent architecture.
- [x] Titan and Crystal boundaries remain explicit.
- [x] Issue #1 import scope is not silently expanded.
- [x] Decision status, evidence level, implementation status and approval remain separate.

## References 📚

- [Issue #74](https://github.com/velantrian/velantrim-native-kernel/issues/74)
- [`native_kernel/semantic_core/reducer.py`](../../native_kernel/semantic_core/reducer.py)
- [`tests/test_semantic_core.py`](../../tests/test_semantic_core.py)
- [`ADR-0003`](./0003-semantic-conflicts-require-explicit-resolution.md)
- [`ADR-0006`](./0006-causal-links-are-relations.md)
- [`ADR-0012`](./0012-single-writer-append-and-replay-contract-v1.md)
- [`ADR-0015`](./0015-accept-clean-profile-and-authorize-p1-semantic-core.md)
- [`DECISION_PROCESS.md`](../DECISION_PROCESS.md)
