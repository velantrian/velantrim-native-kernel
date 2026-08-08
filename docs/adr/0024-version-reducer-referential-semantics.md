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
> The current `nk-p1-reducer/1` is part of published P1–C5 evidence. Tightening it in place would reinterpret old Event histories. This proposal separates a future strict reducer contract from historical reducer v1 and does not authorize runtime changes.

## Context 🧭

The current reducer validates Event schema version and contiguous sequence, then applies structurally valid payloads to immutable state. It does not require referenced Claims to have been admitted and does not constrain supersession topology.

Observed reducer-v1 behavior:

```text
LINK unknown source or target              accepted
UTILIZED unknown or erased Claim           accepted
SUPERSEDED unknown source or successor      accepted
SUPERSEDED self-reference or cycle          not rejected
SUPERSEDED different second successor       replaces prior mapping
ERASED unknown Claim                        accepted
generic LINK self-reference or cycle        not classified
```

Existing tests intentionally admit Claim `a`, then link and supersede it to Claim `b` without first admitting `b`. That is repository evidence for reducer v1 and cannot be silently changed after publication.

PostgreSQL and SQLite replay currently import one process-wide `REDUCER_VERSION`. Changing that constant would replay all histories under new semantics without an instance-level compatibility declaration.

- **Problem:** define honest referential semantics without rewriting already evidenced history.
- **Constraints:** deterministic replay, technology neutrality, explicit versioning, no silent migration, generic relation extensibility and fail-closed strict behavior.
- **Non-goals:** implement runtime v2, add Event verbs, implement conflict resolution, implement NK-EPI-004, define causal truth or integrate another Velantrim project.
- **Current implementation boundary:** only `nk-p1-reducer/1` exists; no strict reducer or per-history version selection exists.
- **Open uncertainty:** profile schema, migration protocol, relation registry, restoration after logical erasure and Receipt shape for validation/migration.

## Inputs considered 🔍

```text
Repository evidence:
- semantic_core/reducer.py performs no referential validation
- test_semantic_core.py relies on a not-yet-admitted target
- PostgreSQL and SQLite replay bind to one imported REDUCER_VERSION
- ADR-0012 already requires explicit reducer versions
- ADR-0003 rejects silent semantic resolution
- ADR-0006 permits typed directed relation graphs and defers relation-specific rules

Codex review lessons from PRs #69/#70:
- integrity comparisons must be exact
- later fixes must not relabel earlier artifacts as proof

External AI-generated inputs supplied by the operator:
- several audits recommended explicit dangling/self/cycle rules
- repository review narrowed generic cycle handling to relation-specific topology and supersession cycles

Operator interpretation:
- current instruction authorizes continued investigation and proposal drafting
- final acceptance remains a separate operator decision
```

AI-generated inputs are design inputs, not evidence or approval.

## Decision drivers 🎯

- preserve historical replay and evidence identity;
- prevent unknown or erased references from becoming silent current state;
- prevent supersession cycles and last-write overwrite;
- avoid false acyclicity for generic typed relations;
- keep relation meaning independent of storage technology;
- make failures deterministic and cross-profile testable;
- require explicit migration rather than inference from code version or date.

## Considered options 🧪

### Option A — Tighten reducer v1 in place

**Advantages:** smallest implementation change; every replay receives strict checks.

**Disadvantages:** changes existing history meaning, breaks fixtures/evidence boundaries and makes interpretation depend on installed code.

### Option B — Validate only outside the reducer

**Advantages:** append-time rejection can fail early while v1 remains unchanged.

**Disadvantages:** imported/corrupted history can bypass checks, replay cannot verify independently, and profile behavior may diverge.

### Option C — Version the strict reducer and require explicit selection

**Advantages:** preserves v1 exactly, makes append/replay deterministic, supports cross-profile fixtures and makes migration auditable.

**Disadvantages:** requires version metadata and dispatch; multiple reducer versions increase maintenance and test cost.

## Proposed decision 💭

Select **Option C** if approved.

### Compatibility boundary

1. `nk-p1-reducer/1` remains readable with its published behavior.
2. Existing histories, projections, Receipts, reports and ZIPs are not relabelled as strict-reducer evidence.
3. A future strict contract uses a new identifier; candidate: `nk-p1-reducer/2`.
4. Reducer version is selected explicitly per Kernel instance or equivalent authoritative history boundary.
5. Selection is not inferred from date, software release, database type, current default or first replay after upgrade.
6. Mixed semantics inside one history are prohibited unless a separate migration contract defines the boundary and replay algorithm.
7. A v1 history is not v2-conformant merely because its final projection resembles a v2 state.

## Proposed strict Event rules

### `ADMIT`

- first admission adds the Claim;
- repeated admission of the same live Claim is a deterministic no-op while the Event remains in history;
- admission of a logically erased Claim fails closed;
- admission does not establish truth or authenticity.

### `LINK`

- source and target must already be admitted and live at that Event position;
- an identical repeated edge is a deterministic no-op;
- the base reducer does **not** reject self-links or generic graph cycles globally;
- reflexivity, symmetry, transitivity, acyclicity, evidence and other relation meaning require a separate typed-relation contract;
- relation existence is not causal proof or truth.

### `UTILIZED`

- the Claim must already be admitted and live;
- unknown or erased Claim utilization fails closed;
- utilization count is operational history, not epistemic promotion.

### `SUPERSEDED`

- source and successor must already be admitted and live;
- source and successor must differ;
- repeated identical source/successor is a deterministic no-op;
- a different second successor for the same source fails closed; no last-write overwrite;
- the new edge must not create a cycle in the `superseded_by` chain;
- successor chains such as `A → B → C` are allowed;
- supersession does not erase the source or prove the successor true.

### `ERASED`

- the Claim must already be admitted;
- repeated erasure is a deterministic no-op;
- erasure does not rewrite earlier Events, links, utilization or supersession records;
- later LINK, UTILIZED, SUPERSEDED or ADMIT operations involving the erased Claim fail closed;
- this remains logical erasure, not physical or cryptographic deletion.

## Deterministic failure surface

A future implementation should expose a bounded failure class, such as `ReferentialIntegrityViolation`, derived from `ContractViolation`, with stable machine-readable reasons. Candidate reasons:

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

Exact names remain implementation details until separately authorized, but profiles must preserve equivalent meaning.

## Required fixture matrix before runtime authorization 🧪

| Event | Case | Proposed strict result |
|---|---|---|
| ADMIT | first admission | PASS / add |
| ADMIT | duplicate live Claim | PASS / no-op |
| ADMIT | erased Claim | FAIL |
| LINK | both admitted/live | PASS |
| LINK | unknown endpoint | FAIL |
| LINK | erased endpoint | FAIL |
| LINK | duplicate exact edge | PASS / no-op |
| LINK | self-link | PRESERVE / relation policy deferred |
| LINK | generic graph cycle | PRESERVE / relation policy deferred |
| UTILIZED | admitted/live Claim | PASS / increment |
| UTILIZED | unknown or erased Claim | FAIL |
| SUPERSEDED | admitted/live A → B | PASS |
| SUPERSEDED | duplicate A → B | PASS / no-op |
| SUPERSEDED | A → A | FAIL |
| SUPERSEDED | unknown or erased endpoint | FAIL |
| SUPERSEDED | A → B after A → C | FAIL |
| SUPERSEDED | edge completing a successor cycle | FAIL |
| ERASED | admitted Claim | PASS / mark erased |
| ERASED | duplicate erase | PASS / no-op |
| ERASED | unknown Claim | FAIL |

Fixtures must prove identical results and equivalent failure reasons in the semantic core, PostgreSQL, SQLite, replay, projection rebuild and cross-profile comparison before any support claim changes.

## Consequences 📌

### Positive

- old evidence remains honest and replayable;
- strict histories cannot silently accumulate dangling current references;
- supersession becomes a deterministic acyclic successor relation;
- generic relation graphs remain extensible;
- append and replay can share one explicit contract;
- migration becomes auditable.

### Negative / accepted trade-offs

- v1 and a future v2 must coexist;
- profiles need explicit reducer-version metadata and dispatch;
- a v1 history with dangling references cannot be silently promoted;
- logical erasure may leave historical edges pointing to an erased Claim;
- relation-specific validity remains deferred.

### Neutral

- assertion map, NK-EPI, C4/C5, production, deletion and ecosystem status do not change;
- Event vocabulary does not change;
- Track H remains independent.

## Invariants 🔒

1. Published reducer-v1 history is never replayed under v2 semantics without explicit authorization and migration evidence.
2. Reducer version is authoritative interpretation context, not a process-local default.
3. Strict validation runs during replay as well as append/admission.
4. Unknown and erased references fail closed under the strict contract.
5. Supersession never uses last-write overwrite and never forms a cycle.
6. Generic relation topology is not declared acyclic by the base reducer.
7. Logical erasure does not rewrite history or claim physical deletion.
8. Referential failure does not prove a represented statement false; it only marks the Event invalid under the declared reducer.
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

- authoritative reducer-version storage per instance/history;
- default for existing and new instances;
- semantic-core version dispatcher;
- PostgreSQL and SQLite schema migration;
- append-time and replay-time validation;
- projection and Receipt binding to exact reducer version;
- v1 validation report and optional migration protocol;
- stable failure representation;
- exact conformance fixtures and assertion-map impact;
- rollback without reinterpreting history.

Safest initial implementation candidate:

```text
existing instances → explicit v1
new opt-in test instances → explicit v2
no automatic conversion
no mixed history
```

This is a recommendation, not authorization.

## Validation and evidence 🧪

| Evidence | Artifact / command | Result | Required for next level |
|---|---|---|---|
| Repository review | reducer, tests and replay paths | gap reproduced | Issue #74 |
| Documentation | ADR-0024, ADR index, Roadmap and Notion handoff | proposal recorded | independent review + operator decision |
| Repository CI | PR #75 workflows | required before merge | exact-head PASS |
| Unit/replay/cross-profile tests | none in this slice | `NOT_STARTED` | required for runtime authorization |
| Operator approval | pending | `PENDING` | explicit accept/reject/revise |

## Failure cases 🚨

- changing `REDUCER_VERSION` and replaying old histories as v2;
- treating existing instances as strict merely because deployment was upgraded;
- validating append but not replay;
- prohibiting every LINK cycle without a relation contract;
- allowing a second successor to overwrite the first;
- removing historical edges when a Claim is erased;
- reporting referential failure as semantic falsehood;
- claiming earlier P1–C5 artifacts prove the future reducer;
- introducing Titan, Crystal or Mentaury semantics into this contract.

## Rollback / supersession

This slice is documentation-only and may be revised or removed before acceptance. A later superseding ADR must preserve reducer-v1 readability and explain migration. Runtime rollback must select a declared version compatible with the history; it must not reinterpret v2 history as v1 by changing a default.

## Consistency checklist 🔱

- [x] Event history remains authoritative about recorded changes.
- [x] History is not equated with truth.
- [x] Projection/cache is not promoted to Canon.
- [x] Relevance/utility is not equated with truth.
- [x] Candidate conflict is not described as resolved conflict.
- [x] Current technology is not silently promoted to permanent architecture.
- [x] Titan and Crystal boundaries remain explicit.
- [x] Issue #1 import scope is not silently expanded.
- [x] Decision, evidence, implementation and approval remain separate.

## References 📚

- [Issue #74](https://github.com/velantrian/velantrim-native-kernel/issues/74)
- [`native_kernel/semantic_core/reducer.py`](../../native_kernel/semantic_core/reducer.py)
- [`tests/test_semantic_core.py`](../../tests/test_semantic_core.py)
- [`ADR-0003`](./0003-semantic-conflicts-require-explicit-resolution.md)
- [`ADR-0006`](./0006-causal-links-are-relations.md)
- [`ADR-0012`](./0012-single-writer-append-and-replay-contract-v1.md)
- [`ADR-0015`](./0015-accept-clean-profile-and-authorize-p1-semantic-core.md)
- [`DECISION_PROCESS.md`](../DECISION_PROCESS.md)
