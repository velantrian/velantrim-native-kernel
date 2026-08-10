# 🧬 Architecture Re-foundation — Blueprint before Runtime

**[English](./ARCHITECTURE_REFOUNDATION.md) · [Русский](./ARCHITECTURE_REFOUNDATION.ru.md)**

> **State:** `ACTIVE / BLUEPRINT-FIRST / RUNTIME EXPANSION FROZEN`  
> **Decision:** [`ADR-0025`](./adr/0025-blueprint-before-runtime-expansion.md)  
> **Issue:** [#88](https://github.com/velantrian/velantrim-native-kernel/issues/88)  
> **Evidence boundary:** architecture research/governance only; no runtime, evidence, maturity, or production promotion

## 1. Why this phase exists

Native Kernel is intended to preserve meaning, memory, knowledge, provenance, uncertainty, change and accountability independently of one current technology stack. The existing **Python + PostgreSQL + SQLite** lineage is retained as a bounded reference laboratory, not made permanent Canon merely because it exists first.

```text
meaning / ontology / laws
        ↓
abstract Kernel machine
        ↓
identity / time / lifecycle / conflict models
        ↓
substrate-independence contract
        ↓
replaceable profiles
        ↓
experiments and evidence
```

## 2. Phase boundary

This phase owns ontology, semantic laws, abstract-machine obligations, identity/time/change, lifecycle, conflict/uncertainty/revision, substrate-independent obligations, reference-profile mapping, explicit unknowns and falsification criteria.

It does not own a new reducer, Event vocabulary, database, language port, LLM/vector adapter, product integration, performance-driven semantic change, production deployment, or proof that arbitrary future substrates conform.

## 3. Required deliverables

### A1 — Kernel Purpose and Non-goals

**Status:** `DRAFTED / PROVISIONAL` — [EN](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md) / [RU](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md). Defines the Kernel problem, durable qualities, non-goals and ecosystem boundaries.

### A2 — Knowledge and Memory Ontology

**Status:** `DRAFTED / PROVISIONAL` — [EN](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md) / [RU](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md). Distinguishes Signal, Observation, Record, Proposition, Claim, Interpretation, Hypothesis, Belief, Knowledge, Memory, Evidence, Source, Provenance, Context, Relation, State, Change, Event, Conflict, Contradiction, Uncertainty, Revision, Supersession, Authority and Receipt without making current storage/runtime representations Canon.

### A3 — Abstract Native Kernel Machine

**Status:** `DRAFTED / PROVISIONAL` — [EN](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md) / [RU](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md). Defines provisional meaning-level configuration facets, transition families, failure/indeterminacy handling, Authority boundaries, order/concurrency and contrasting substrate mappings. `transition ≠ Event envelope`; `State ≠ reducer output` universally.

### A4 — Semantic Laws and Invariants

**Status:** `DRAFTED / PROVISIONAL` — [EN](./A4_SEMANTIC_LAWS_AND_INVARIANTS.md) / [RU](./A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md). Current law-set candidate `nk-semantic-laws/A4-draft-1` contains 28 provisional, reviewable laws. They protect representation/epistemic boundaries, Context/Provenance/Authority, identity/time/change, conflict/uncertainty, views/accountability and substrate/conformance distinctions.

### A5 — Identity, Time, and Change Model

**Status:** `DRAFTED / PROVISIONAL` — [EN](./A5_IDENTITY_TIME_AND_CHANGE.md) / [RU](./A5_IDENTITY_TIME_AND_CHANGE.ru.md). Pending independent review and integrated A1–A10 review.

A5 introduces candidate model `nk-identity-time-change/A5-draft-1`. Identity is a typed/scoped relation, not one universal identifier. It distinguishes:

```text
REFERENT_IDENTITY
SEMANTIC_CONTENT_IDENTITY
CLAIM_POSITION_IDENTITY
RECORD_IDENTITY
LINEAGE_CONTINUITY_IDENTITY
OCCURRENCE_IDENTITY
SUBSTRATE_LOCAL_IDENTITY
```

Candidate scoped outcomes are `SAME`, `DISTINCT`, `CONTINUATION_OF`, `VERSION_OF`, `ALIAS_OF`, `MIGRATED_FROM`, and `UNRESOLVED`.

A5 also distinguishes `OCCURRENCE_TIME`, `VALID_TIME`, `OBSERVATION_TIME`, `ASSERTION_TIME`, `RECORD_TIME`, `DECISION_TIME`, `EFFECTIVE_TIME`, and `WRITE_COMMIT_TIME`; and keeps occurrence, observation, causal/dependency, lineage, authority-decision, local-write and migration/synchronization order separate.

It classifies storage relocation, re-encoding, copying, translation, correction, reinterpretation, Revision, Supersession, restriction, logical erasure, physical/cryptographic erasure, forgetting/loss and represented-world change without assuming one identity effect for all kinds.

A5 reconciles existing accepted/versioned contracts rather than silently superseding them. `nk-id/1.0` remains one current reference encoding contract; UTF-8/NFC/JSON/SHA-256 and `asserted_at` are not promoted into the only substrate-independent identity mechanism. `global_seq`/`stream_seq` remain a reference-laboratory ordering realization. The deletion state machine remains a bounded profile mechanism.

**First-draft completion test:** satisfied for bounded drafting scope: a reader can name the identity relation, temporal/order relation and semantic effect of a Change without requiring one physical encoding. Final acceptance still requires independent and integrated review.

### A6 — Knowledge Lifecycle

**Status:** `DRAFTED / PROVISIONAL` — [EN](./A6_KNOWLEDGE_LIFECYCLE.md) / [RU](./A6_KNOWLEDGE_LIFECYCLE.ru.md). Pending independent review and integrated A1–A10 review.

A6 introduces candidate model `nk-knowledge-lifecycle/A6-draft-1`. The knowledge lifecycle is a labeled directed graph of recurring, reviewable configurations rather than a linear pipeline. It defines nine phases:

```text
ENCOUNTERED
RETAINED
POSITIONED
EPISTEMICALLY_WEIGHED
RELATIONALLY_INTEGRATED
IN_TENSION
REVISED_OR_SUPERSEDED
DISPOSED
ACCOUNTED
```

each mapped to one or more of A3's thirteen transition families, plus a typed `LIFECYCLE_TRANSITION` relation that reuses A3's outcome vocabulary rather than inventing new terms. `DERIVE_BOUNDED_VIEW` and `SELECT_FOR_USE` are phase-referencing, not phase-changing.

A6 separates `LIFECYCLE_TRANSITION_ORDER` from `OCCURRENCE_ORDER`, `CAUSAL_DEPENDENCY_ORDER` and `LOCAL_WRITE_COMMIT_ORDER`, and extends A3's eight dispositions with three closure kinds — `LOGICALLY_ERASED`, `PHYSICALLY_OR_CRYPTOGRAPHICALLY_ERASED`, `FORGOTTEN_OR_LOST` — resolving the erasure/forgetting distinctions A5 named but deferred.

A6 reconciles existing accepted/versioned contracts rather than silently superseding them. Its mapping of `ADMIT`/`LINK`/`UTILIZED`/`SUPERSEDED`/`ERASED` onto lifecycle phases is explicitly illustrative and non-canonical; it authorizes no new Event verbs, decides no `Issue #74 / ADR-0024` question, and expands no `Issue #16` deletion-execution scope.

**First-draft completion test:** satisfied for bounded drafting scope: a reader can name the phase, transition family and legitimizing Authority or method of a knowledge item's move without assuming a linear pipeline or a single storage schema. Final acceptance still requires independent and integrated review.

### A7 — Conflict, Uncertainty, and Revision Model

**Status:** `NEXT BOUNDED SLICE`.

Define candidate versus established Conflict, Contradiction versus scope mismatch, unresolved plurality, uncertainty/provenance gaps, resolution Authority, reversibility, belief revision and the ability to remain undecided. A7 may refine revision policy but must preserve A4/A5/A6 history and identity/lifecycle distinctions.

### A8 — Substrate-independence Contract

Define what future profiles must preserve/translate: semantic identity, change/history visibility, Provenance, temporal meaning, uncertainty/conflict visibility, Authority/admission boundaries, bounded accountability, migration and explicit loss. Present Event-sourcing assumptions must be labelled as mechanisms unless proven necessary.

### A9 — Reference Laboratory Boundary

Classify **Python + PostgreSQL + SQLite** P1–C5 mechanisms as examples, experiments, profile-specific choices, falsification tools or legacy evidence. No removal/rewrite occurs merely because a mechanism is profile-specific.

### A10 — Open Questions and Falsification Criteria

Record unresolved architecture questions and evidence that would weaken/refute major hypotheses. This includes identity without stable serialized bytes, minimum history/reconstruction equivalents, analog/neuromorphic continuity, forgetting without forbidden retention, and semantic equivalence across probabilistic substrates.

## 4. Work sequence

```text
A1 Purpose and Non-goals                         DRAFTED / PROVISIONAL
→ A2 Ontology                                   DRAFTED / PROVISIONAL
→ A3 Abstract Machine                           DRAFTED / PROVISIONAL
→ A4 Semantic Laws                              DRAFTED / PROVISIONAL
→ A5 Identity / Time / Change                   DRAFTED / PROVISIONAL
→ A6 Knowledge Lifecycle                        DRAFTED / PROVISIONAL
→ A7 Conflict / Uncertainty / Revision          NEXT BOUNDED SLICE
→ A8 Substrate Independence
→ A9 Reference Laboratory Boundary
→ A10 Open Questions / Falsification
→ integrated blueprint review
→ separate operator decision before runtime expansion
```

Later slices may refine earlier drafts only explicitly; they may not silently redefine them.

## 5. Research method

Each deliverable should contain definitions, non-equivalences, a candidate formal model, counterexamples/failure cases, unresolved questions, mapping to existing contracts/runtime, contrasting substrate mappings, review status and evidence boundary.

Sources, papers, existing systems and AI analysis are inputs; none becomes Canon automatically.

## 6. Runtime freeze policy

Allowed: architecture research; integrity/security/reproducibility/provenance repair; evidence preservation; current-truth/validator repair; historical recovery; isolated falsification experiments without runtime promotion.

Not authorized without a separate operator decision: new semantic runtime features, reducer v2, new Event vocabulary, new databases/language profiles/model adapters/ecosystem integrations, executable NK-EPI/Temporal/full Admission, operational deletion expansion, maturity promotion or production authorization.

## 7. Relationship to existing contracts and pending decisions

A6 does not change ADR statuses or historical evidence. Issue #14/#15/#16 remain open around their remaining evidence/portability scopes. Issue #18 remains operator-controlled for license/publication. Issue #74 / ADR-0024 remains `PROPOSED / PENDING_OPERATOR`; reducer v1 stays immutable and reducer-v2 unauthorized. Track H source admission remains operator-controlled.

```text
A5/A6 semantic and lifecycle models
→ later versioned mapping/equivalence work
→ existing contracts preserved within declared scope
≠ silent retroactive rewrite
```

## 8. Blueprint completion gate

The blueprint is not complete merely because documents exist. Blueprint completion gate requires all A1–A10 deliverables, terminology reconciliation, explicit contradictions/unknowns, labelled implementation assumptions, falsification criteria, existing-contract mapping, contrasting substrate thought experiments, critical review, integrated review and a separate operator decision for any next phase.

## 9. Current progress

```text
Architecture Re-foundation decision: established by ADR-0025
Blueprint plan: this document
Blueprint content: A1-A6 DRAFTED / PROVISIONAL; A7-A10 NOT YET COMPLETE
Next bounded slice: A7 CONFLICT, UNCERTAINTY, AND REVISION
Runtime expansion: FROZEN
Existing P1–C5 laboratory: PRESERVED / BOUNDED
Production authorization: false
```

A1–A6 drafting does not establish independent approval, integrated Canon, runtime implementation, arbitrary future-substrate support, or production readiness.
