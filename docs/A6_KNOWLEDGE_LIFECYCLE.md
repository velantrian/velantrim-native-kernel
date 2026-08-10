# 🧬 A6 — Knowledge Lifecycle

**[English](./A6_KNOWLEDGE_LIFECYCLE.md) · [Русский](./A6_KNOWLEDGE_LIFECYCLE.ru.md)**

> **Deliverable:** `A6_KNOWLEDGE_LIFECYCLE` of the [Architecture Re-foundation](./ARCHITECTURE_REFOUNDATION.md) blueprint under `ADR-0025` / [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88)
> **Depends on:** provisional A1–A5 blueprint content, in particular A3's thirteen transition families and A5's identity/time/change model
> **Evidence boundary:** architecture research and provisional semantic obligations only; no runtime, contract, evidence, assertion-map, NK-EPI, maturity, or production change
> **Review status:** first drafted slice; pending independent review and integrated A1–A10 review

```text
model_id: nk-knowledge-lifecycle/A6-draft-1
state: DRAFTED
classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL
next_content_slice: A7_CONFLICT_UNCERTAINTY_AND_REVISION
runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED
Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED
```

## 1. Purpose and authority boundary

A6 answers one bounded question: what recurring configurations does a knowledge-bearing item pass through after it is first encountered, and what legitimizes moving it from one configuration to another? It does not define what a Claim or Record *is* (A2), what transitions the abstract Kernel machine supports (A3), which laws bound those transitions (A4), or what identity/time relation holds across a transition (A5). A6 sits on top of those and names the recurring, reviewable *shape* of a knowledge item's life.

Required non-equivalences:

```text
lifecycle phase ≠ storage status column
closure ≠ deletion of history
one Event ≠ one lifecycle transition
lifecycle position ≠ epistemic validity
lifecycle order ≠ occurrence order ≠ causal order ≠ write-commit order
frequent access ≠ lifecycle advancement
recency ≠ lifecycle advancement
model confidence ≠ lifecycle advancement
retrieval rank ≠ lifecycle advancement
```

Lifecycle authority must trace to an explicit `DECIDE_DISPOSITION`, `ASSESS_EPISTEMIC_POSITION`, `RELATE`, `DETECT_TENSION`, `REVISE_OR_SUPERSEDE`, or `ACCOUNT` transition (A3) with a named Authority or method (A4), never to storage presence, retrieval rank, repetition, model confidence, recency, or usefulness alone.

## 2. Model status and qualification rule

The lifecycle is modeled as a labeled directed graph over phases, not a linear pipeline: a candidate phase qualifies only if it names a recurring configuration that (a) maps to one or more A3 transition families, (b) has a minimum obligation distinguishable from every other phase, and (c) is scoped per A5 identity kind rather than assumed global.

Because phases are scoped per identity kind, the same underlying item can occupy different phases simultaneously under different A5 identity relations — for example `RELATIONALLY_INTEGRATED` under `RECORD_IDENTITY` while still `IN_TENSION` under `CLAIM_POSITION_IDENTITY`. A6 does not require one collapsed phase per item.

## 3. Lifecycle phases

| Phase | A3 transition family | Minimum obligation | Explicit non-equivalence |
|---|---|---|---|
| `ENCOUNTERED` | `ENCOUNTER` | a Signal or Observation has been registered as present to the Kernel | encountered ≠ retained ≠ believed |
| `RETAINED` | `REGISTER` | the item has a Record with a scope and an origin | retained ≠ admitted as true |
| `POSITIONED` | `IDENTIFY_OR_DISTINGUISH`, `BIND_SCOPE_AND_ORIGIN`, `INTERPRET_AND_CLASSIFY_ROLE` | the item has a named identity relation (A5), scope/origin binding, and a classified role | positioned ≠ epistemically weighed |
| `EPISTEMICALLY_WEIGHED` | `ASSESS_EPISTEMIC_POSITION` | an explicit epistemic position (Belief/Hypothesis/Knowledge boundary from A2) has been assigned | weighed ≠ permanently settled |
| `RELATIONALLY_INTEGRATED` | `RELATE`, `DECIDE_DISPOSITION` | the item has named relations to other items and a current disposition (A3 §6) | integrated ≠ conflict-free |
| `IN_TENSION` | `DETECT_TENSION` | an open Conflict, Contradiction, or scope mismatch has been named against the item | tension ≠ falsity of either side |
| `REVISED_OR_SUPERSEDED` | `REVISE_OR_SUPERSEDE` | a named successor or correction relation exists under A5 Revision/Supersession | superseded ≠ erased or false |
| `DISPOSED` | `DECIDE_DISPOSITION` | a closure kind (§7) has been assigned with a named Authority or method | disposed ≠ forgotten |
| `ACCOUNTED` | `ACCOUNT` | a Receipt exists naming what happened and under what Authority | accounted ≠ correct or true |

`DERIVE_BOUNDED_VIEW` and `SELECT_FOR_USE` are **phase-referencing, not phase-changing**: they read the current phase of one or more items to construct a bounded view or make a selection, but performing them does not itself move an item between phases. A view over `IN_TENSION` items does not resolve the tension.

## 4. Typed lifecycle transition relation

A6 defines one typed relation rather than inventing per-phase transition vocabulary:

```text
LIFECYCLE_TRANSITION(subject, from_phase, to_phase, transition_family, context, authority_or_method, temporal_binding, identity_effect, uncertainty)
```

- `subject` — the item under a named A5 identity relation, not a bare storage row;
- `from_phase` / `to_phase` — members of §3, or `NONE` for the first transition into `ENCOUNTERED`;
- `transition_family` — the A3 family that produced the move (§3 mapping);
- `context` — the A2 Context the transition was evaluated under;
- `authority_or_method` — the named Authority or deterministic method (A4) that legitimized the move;
- `temporal_binding` — which A5 temporal dimension (`DECISION_TIME`, `EFFECTIVE_TIME`, `RECORD_TIME`, etc.) the transition is dated against;
- `identity_effect` — the A5 identity outcome the transition produces on the subject, if any;
- `uncertainty` — whether the transition itself is disputed or provisional.

A transition's outcome reuses A3's existing vocabulary rather than inventing new terms: `APPLIED`, `NO_CHANGE`, `QUARANTINED`, `REJECTED`, `PARTIAL`, `UNKNOWN`, `UNSUPPORTED`, `FAILED`. A `FAILED` or `UNSUPPORTED` lifecycle transition does not silently leave `to_phase` populated.

## 5. Non-linearity: branching, looping, and plurality

The lifecycle graph is not a straight line from `ENCOUNTERED` to `ACCOUNTED`:

- **Looping** — an item can return from `IN_TENSION` to `RELATIONALLY_INTEGRATED`, or from `RELATIONALLY_INTEGRATED` back to `EPISTEMICALLY_WEIGHED`, as many times as new Evidence or Relations arrive;
- **Branching** — a single `ENCOUNTERED` Signal can produce multiple `RETAINED` Records under different scopes, each progressing independently;
- **Concurrency** — two Authorities can drive transitions on the same item at overlapping times; A6 requires the transition to name which Authority acted, not that only one can act;
- **Simultaneity across identity kinds** — as noted in §2, an item can sit in different phases at once under different A5 identity relations;
- **Open unresolved residency** — an item may remain indefinitely in `IN_TENSION` or `EPISTEMICALLY_WEIGHED`; A6 does not require eventual resolution.

## 6. Lifecycle order

```text
LIFECYCLE_TRANSITION_ORDER ≠ OCCURRENCE_ORDER ≠ CAUSAL_DEPENDENCY_ORDER ≠ LOCAL_WRITE_COMMIT_ORDER
```

The order in which `LIFECYCLE_TRANSITION` records are produced is a distinct ordering relation from the A5 orders it references. A transition recorded later in `LOCAL_WRITE_COMMIT_ORDER` may bear an earlier `EFFECTIVE_TIME`, and a `REVISE_OR_SUPERSEDE` transition may resolve a Conflict whose `OCCURRENCE_ORDER` predates transitions already `ACCOUNTED`. A6 does not require these orders to coincide.

## 7. Disposition and closure kinds

A3 §6 already defines eight dispositions (`PENDING`, `AVAILABLE`, `QUARANTINED`, `RESTRICTED`, `REJECTED`, `HISTORICAL_ONLY`, `UNAVAILABLE`, `UNKNOWN`). A6 extends this set with three closure kinds that resolve the erasure/forgetting distinctions A5 §10 named but deferred:

| Closure kind | Minimum obligation | Explicit non-equivalence |
|---|---|---|
| `LOGICALLY_ERASED` | the item is marked non-available for ordinary use while its Record remains inspectable under Authority | logically erased ≠ physically or cryptographically erased |
| `PHYSICALLY_OR_CRYPTOGRAPHICALLY_ERASED` | the bytes or the key required to recover them have been destroyed under a named method | physically erased ≠ merely restricted or logically erased |
| `FORGOTTEN_OR_LOST` | the item is no longer reconstructible from accessible sources, without a recorded deliberate erasure method | forgotten/lost ≠ globally lost; `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST` (A5/Track H) |

A `DISPOSED` phase transition (§3) must name one of the eight A3 dispositions and, when applicable, one of these three closure kinds. Disposition and closure kind are independent axes: `RESTRICTED` may or may not be paired with `LOGICALLY_ERASED`.

## 8. Revision and Supersession as lifecycle transitions

`REVISE_OR_SUPERSEDE` (A3) driving a transition into `REVISED_OR_SUPERSEDED` (§3) is the lifecycle-level statement of A5 §9's Revision and Supersession requirements: the predecessor's Record is preserved, the successor's `LINEAGE_CONTINUITY_IDENTITY` names the predecessor, and `REVISED_OR_SUPERSEDED` never implies `LOGICALLY_ERASED` or `FORGOTTEN_OR_LOST` by itself.

A6 explicitly defers the following to Issue #74 / ADR-0024:

- whether a superseded item may have more than one successor;
- whether supersession cycles are permitted or must be rejected;
- whether an item may supersede itself under a corrected identity binding.

Reducer v1 remains immutable and reducer-v2 topology remains unauthorized; A6 does not decide these questions, it only names where the lifecycle model expects them to be decided.

## 9. Relationship to existing contracts and the reference laboratory

The following table is illustrative and **non-canonical**: it maps existing P1–C5 Event vocabulary onto A6 phases so the reference laboratory's behavior can be read against the model, not so the model is authorized to redefine the laboratory.

| P1–C5 Event vocabulary | Illustrative A6 phase | Non-canonical note |
|---|---|---|
| `ADMIT` | `RETAINED` → `POSITIONED` | admission is a laboratory-specific method, not a universal transition family |
| `LINK` | `RELATIONALLY_INTEGRATED` | `nk-p1-reducer/1` link semantics are one profile realization of `RELATE` |
| `UTILIZED` | referenced via `SELECT_FOR_USE` | utilization is phase-referencing, not phase-changing (§3) |
| `SUPERSEDED` | `REVISED_OR_SUPERSEDED` | current reducer supersession semantics remain `Issue #74 / ADR-0024` `PROPOSED / PENDING_OPERATOR` |
| `ERASED` | `DISPOSED` with `LOGICALLY_ERASED` | current `ERASED` state remains a bounded profile mechanism per `Issue #16`; it is not promoted to `PHYSICALLY_OR_CRYPTOGRAPHICALLY_ERASED` |

This mapping does not authorize new Event verbs. `CONFLICT_OPENED` and `CONFLICT_RESOLVED` remain frozen and unauthorized pending A7. It does not change `global_seq` or `stream_seq` claims, which remain reference-laboratory ordering mechanisms rather than `LIFECYCLE_TRANSITION_ORDER` itself (§6). It does not expand `Issue #16`'s deletion-execution scope.

## 10. Failure and indeterminacy cases

- a `LIFECYCLE_TRANSITION` recorded with no `authority_or_method` is invalid, not silently `APPLIED`;
- an item that never leaves `ENCOUNTERED` is a legitimate, indefinitely stable state, not an error;
- two concurrent transitions naming different `to_phase` values for the same subject and Context must be recorded as `IN_TENSION`, not silently arbitrated by write order;
- a transition whose `temporal_binding` cannot be resolved must record `UNKNOWN`, not a default timestamp;
- `FORGOTTEN_OR_LOST` must never be inferred merely from absence in one accessible index;
- retrying a `FAILED` transition must produce a new `LIFECYCLE_TRANSITION` record, not a silent overwrite of the failed one;
- a `DISPOSED` item queried again without new Evidence must not silently re-enter `EPISTEMICALLY_WEIGHED`;
- a closure kind (§7) applied without a named method is invalid;
- phase state read through `DERIVE_BOUNDED_VIEW` must not be cached past the Context that produced it without re-derivation.

## 11. Contrasting substrate mappings

### Manual archival and review process

A physical registry office receives a paper filing (`ENCOUNTERED`), stamps and shelves it under a case number (`RETAINED`), a clerk identifies the party and classifies the document type (`POSITIONED`), a reviewing officer notes whether it is a sworn statement or a note in the margin (`EPISTEMICALLY_WEIGHED`), it is cross-referenced to related case files (`RELATIONALLY_INTEGRATED`), a later filing contradicts it and both are flagged (`IN_TENSION`), a judge's ruling supersedes the earlier filing while the original stays in the case file (`REVISED_OR_SUPERSEDED`), the case is closed and archived under a retention policy (`DISPOSED`), and the closure is logged in the office's ledger (`ACCOUNTED`). No database exists; every `authority_or_method` is a named human role.

### Adaptive analog or neuromorphic substrate

A continuously-varying analog trace crossing a detection threshold is the substrate's `ENCOUNTER`; `RETAINED` may correspond to a change in synaptic weight rather than a discrete row; `POSITIONED` and `EPISTEMICALLY_WEIGHED` may be continuous rather than a step function, so a transition's `authority_or_method` must be able to name a threshold-crossing rule rather than an atomic write; `REVISED_OR_SUPERSEDED` may correspond to weight decay competing with reinforcement rather than a discrete successor record. A6 does not require phases to be discrete storage states to be meaningful.

### Conventional digital Event-sourced laboratory

This is the current P1–C5 profile: an `ADMIT` Event moves an item toward `RETAINED`/`POSITIONED`, a `LINK` Event contributes to `RELATIONALLY_INTEGRATED`, and reducer-derived state materializes the current phase. §9's table gives the illustrative, non-canonical mapping; nothing here re-authorizes reducer-v2 or new Event verbs.

## 12. Falsification criteria and open questions

A6 would be weakened or refuted by evidence that:

- recurring configurations cannot be named independently of one storage schema across the three contrasting substrates in §11;
- a phase cannot be defined without collapsing distinct A5 identity kinds into one;
- `LIFECYCLE_TRANSITION_ORDER` cannot in practice be kept distinct from `LOCAL_WRITE_COMMIT_ORDER` in any implementable substrate;
- the three closure kinds (§7) cannot be distinguished in a substrate that has no separate concept of key destruction;
- looping/branching/concurrency (§5) cannot be represented without an unbounded number of additional phases, defeating the qualification rule in §2.

Open questions deferred to later work:

- what minimum number of closure kinds is required once A7's conflict-resolution model exists;
- whether A8 requires a stronger cross-substrate equivalence claim for `authority_or_method` than "named";
- whether A9's reference-laboratory classification changes any entry in §9's illustrative table.

## 13. Deferred responsibilities and completion boundary

A6 explicitly does not decide, and defers to:

- **A7 — Conflict, Uncertainty, and Revision**: the conflict taxonomy, resolution Authority, and belief-revision policy that `IN_TENSION` and `REVISE_OR_SUPERSEDE` transitions ultimately rely on;
- **A8 — Substrate-independence Contract**: cross-substrate conformance thresholds for lifecycle phases and closure kinds;
- **A9 — Reference Laboratory Boundary**: whether §9's illustrative P1–C5 mapping is an example, an experiment, or legacy evidence;
- **A10 — Open Questions and Falsification**: the registry of unresolved architecture questions this and other slices raise;
- **Issue #14**: canonical identity encoding used to bind `subject` in `LIFECYCLE_TRANSITION`;
- **Issue #15**: portable history commitment for the sequence of `LIFECYCLE_TRANSITION` records;
- **Issue #16**: execution of physical or cryptographic erasure across actual storage locations;
- **Issue #74 / ADR-0024**: reducer-v2 topology and successor/cycle rules for `REVISED_OR_SUPERSEDED` (§8);
- **Issue #18**: license and publication terms;
- **Track H**: operator-controlled historical source admission.

A6 does not authorize runtime implementation, new Event vocabulary, new databases, LLM/vector adapters, or maturity or production authorization. It does not change the assertion map, NK-EPI status, or any existing accepted ADR.
