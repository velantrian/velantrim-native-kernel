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
reference-laboratory boundary
        ↓
open questions / falsification
        ↓
integrated review + separate operator decision
```

## 2. Phase boundary

This phase owns ontology, semantic laws, abstract-machine obligations, identity/time/change, lifecycle, conflict/uncertainty/revision, substrate-independent obligations, reference-profile mapping, explicit unknowns and falsification criteria.

It does not own a new reducer, Event vocabulary, database, language port, LLM/vector adapter, product integration, performance-driven semantic change, production deployment, or proof that arbitrary future substrates conform.

## 3. Required deliverables

### A1 — Kernel Purpose and Non-goals

**Status:** `DRAFTED / PROVISIONAL` — [EN](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md) / [RU](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md). Defines the Kernel problem, durable qualities, non-goals and ecosystem boundaries.

### A2 — Knowledge and Memory Ontology

**Status:** `DRAFTED / PROVISIONAL` — [EN](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md) / [RU](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md). Defines technology-neutral semantic distinctions without turning current storage/runtime representations into Canon.

### A3 — Abstract Native Kernel Machine

**Status:** `DRAFTED / PROVISIONAL` — [EN](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md) / [RU](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md). Defines provisional meaning-level configuration facets, transition families, failure/indeterminacy handling, Authority boundaries, order/concurrency and contrasting substrate mappings. `transition ≠ Event envelope`; `State ≠ reducer output` universally.

### A4 — Semantic Laws and Invariants

**Status:** `DRAFTED / PROVISIONAL` — [EN](./A4_SEMANTIC_LAWS_AND_INVARIANTS.md) / [RU](./A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md). Candidate `nk-semantic-laws/A4-draft-1` contains 28 provisional laws protecting representation/epistemic boundaries, Context/Provenance/Authority, identity/time/change, conflict/uncertainty, views/accountability and substrate/conformance distinctions.

### A5 — Identity, Time, and Change Model

**Status:** `DRAFTED / PROVISIONAL` — [EN](./A5_IDENTITY_TIME_AND_CHANGE.md) / [RU](./A5_IDENTITY_TIME_AND_CHANGE.ru.md). Candidate `nk-identity-time-change/A5-draft-1` makes identity a typed/scoped relation, separates semantic from substrate-local identity, distinguishes material temporal/order relations, and requires explicit lineage/loss across migration and revision.

### A6 — Knowledge Lifecycle

**Status:** `DRAFTED / PROVISIONAL` — [EN](./A6_KNOWLEDGE_LIFECYCLE.md) / [RU](./A6_KNOWLEDGE_LIFECYCLE.ru.md). Candidate `nk-knowledge-lifecycle/A6-draft-1` models lifecycle as a non-linear graph of meaning-level positions and transitions rather than one storage-state pipeline; Event sourcing is not universalized.

### A7 — Conflict, Uncertainty, and Revision Model

**Status:** `DRAFTED / PROVISIONAL` — [EN](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.md) / [RU](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md). Candidate `nk-conflict-uncertainty-revision/A7-draft-1` keeps tension kind, assessment status and resolution status independent; preserves typed uncertainty, unresolved plurality, scoped resolution, revision lineage and reopening without selecting a universal winner algorithm.

### A8 — Substrate-independence Contract

**Status:** `DRAFTED / PROVISIONAL` — [EN](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md) / [RU](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md). Pending independent review and integrated A1–A10 review.

A8 introduces candidate model `nk-substrate-independence/A8-draft-1` and answers what radically different implementations must preserve to remain comparable as Native Kernel implementations.

Its provisional mapping relation is:

```text
SUBSTRATE_MAPPING(
  profile,
  architecture_obligation,
  realization_or_equivalent,
  preservation_state,
  context_and_scope,
  observable_check,
  declared_loss_or_none,
  uncertainty,
  authority_for_claim
)
```

Preservation states are `PRESERVED`, `PARTIAL`, `UNSUPPORTED`, `INDETERMINATE`, and `LOSSY`. They are mapping states, not assertion-map arithmetic. Known inability to preserve a materially required distinction must weaken or fail a conformance claim rather than be silently approximated.

A8 defines ten provisional preservation obligations (`A8-P01`…`A8-P10`) covering A2 ontology distinctions, A3 transition semantics, A4 laws, A5 identity/time/order, A6 lifecycle/history, A7 conflict/uncertainty/revision, Context/Provenance/Source/Authority, bounded accountability, and explicit capability/loss declarations.

It distinguishes:

```text
PHYSICAL_IDENTITY
REPRESENTATION_EQUIVALENCE
SEMANTIC_OBLIGATION_EQUIVALENCE
BEHAVIORAL_CONFORMANCE_FOR_SCOPE
LINEAGE_CONTINUITY_EQUIVALENCE
```

Physical identity is neither necessary nor sufficient for semantic equivalence. Equal bytes/hashes/output do not by themselves prove semantic equivalence, while different IDs/encodings/carriers do not by themselves prove non-equivalence.

A8 permits different physical memory, layouts, languages, data structures, persistence, synchronization, parallelism, time representation, uncertainty representation and hardware where required meaning survives. It does not require SQL, JSON, SHA-256, Event sourcing, reducers, global sequence numbers, synchronized wall clocks, LLMs, embeddings, Python, network, cloud, silicon, RAM, or one processor model.

Scoped conformance outcomes are `FULL_CONFORMANCE_FOR_SCOPE`, `BOUNDED_CONFORMANCE`, `NON_CONFORMANT_FOR_SCOPE`, and `INDETERMINATE_CONFORMANCE`.

```text
substrate-independent specification
≠ universal portability proof
```

A8 makes no claim that a neuromorphic, analog, quantum, or arbitrary future implementation already exists or conforms. Detailed grading of P1–C5 is deliberately deferred to A9.

**First-draft completion test:** satisfied for bounded drafting scope: given two radically different implementations, a reviewer can identify which meaning obligations must be preserved, separate representation/physical equality from semantic equivalence, identify explicit degradation, and scope a conformance claim without referring to PostgreSQL schemas, Python classes, JSON bytes, Event sourcing, or one processor model. Final acceptance still requires independent and integrated review.

### A9 — Reference Laboratory Boundary

**Status:** `NEXT BOUNDED SLICE`.

Classify **Python + PostgreSQL + SQLite** P1–C5 mechanisms against A1–A8: what is architecture-preserving evidence, what is partial, what is profile-specific, what is a falsification instrument, and what is not an architecture requirement. No removal/rewrite occurs merely because a mechanism is profile-specific.

### A10 — Open Questions and Falsification Criteria

Record unresolved architecture questions and evidence that would weaken/refute major hypotheses, including cross-substrate equivalence limits, minimum history/accountability equivalents, analog/neuromorphic continuity, forgetting without forbidden retention, and unresolved conformance boundaries.

## 4. Work sequence

```text
A1 Purpose and Non-goals                         DRAFTED / PROVISIONAL
→ A2 Ontology                                   DRAFTED / PROVISIONAL
→ A3 Abstract Machine                           DRAFTED / PROVISIONAL
→ A4 Semantic Laws                              DRAFTED / PROVISIONAL
→ A5 Identity / Time / Change                   DRAFTED / PROVISIONAL
→ A6 Knowledge Lifecycle                        DRAFTED / PROVISIONAL
→ A7 Conflict / Uncertainty / Revision          DRAFTED / PROVISIONAL
→ A8 Substrate-independence Contract            DRAFTED / PROVISIONAL
→ A9 Reference Laboratory Boundary              NEXT BOUNDED SLICE
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

A8 does not change ADR statuses or historical evidence. Issue #14/#15/#16/#17 retain their existing scopes. Issue #18 remains operator-controlled for license/publication. Issue #74 / ADR-0024 remains `PROPOSED / PENDING_OPERATOR`; reducer v1 stays immutable and reducer-v2 unauthorized. ADR-0003 remains `PROPOSED / NOT_STARTED`. Track H source admission remains operator-controlled.

```text
A1-A8 blueprint obligations
→ A9 reference-laboratory classification
→ A10 open questions / falsification
→ integrated review
→ existing contracts reconciled within declared scope
≠ silent retroactive rewrite
```

## 8. Blueprint completion gate

The blueprint is not complete merely because documents exist. Blueprint completion gate requires all A1–A10 deliverables, terminology reconciliation, explicit contradictions/unknowns, labelled implementation assumptions, falsification criteria, existing-contract mapping, contrasting substrate thought experiments, critical review, integrated review and a separate operator decision for any next phase.

## 9. Current progress

```text
Architecture Re-foundation decision: established by ADR-0025
Blueprint plan: this document
Blueprint content: A1-A8 DRAFTED / PROVISIONAL; A9-A10 NOT YET COMPLETE
Next bounded slice: A9 REFERENCE LABORATORY BOUNDARY
Runtime expansion: FROZEN
Existing P1–C5 laboratory: PRESERVED / BOUNDED
Production authorization: false
```

A1–A8 drafting does not establish independent approval, integrated Canon, runtime implementation, arbitrary future-substrate support, or production readiness.