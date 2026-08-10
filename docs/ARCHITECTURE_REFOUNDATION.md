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
**Status:** `DRAFTED / PROVISIONAL` — [EN](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md) / [RU](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md).

### A2 — Knowledge and Memory Ontology
**Status:** `DRAFTED / PROVISIONAL` — [EN](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md) / [RU](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md).

### A3 — Abstract Native Kernel Machine
**Status:** `DRAFTED / PROVISIONAL` — [EN](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md) / [RU](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md).

### A4 — Semantic Laws and Invariants
**Status:** `DRAFTED / PROVISIONAL` — [EN](./A4_SEMANTIC_LAWS_AND_INVARIANTS.md) / [RU](./A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md). Candidate `nk-semantic-laws/A4-draft-1` contains 28 provisional laws.

### A5 — Identity, Time, and Change Model
**Status:** `DRAFTED / PROVISIONAL` — [EN](./A5_IDENTITY_TIME_AND_CHANGE.md) / [RU](./A5_IDENTITY_TIME_AND_CHANGE.ru.md). Candidate `nk-identity-time-change/A5-draft-1`.

### A6 — Knowledge Lifecycle
**Status:** `DRAFTED / PROVISIONAL` — [EN](./A6_KNOWLEDGE_LIFECYCLE.md) / [RU](./A6_KNOWLEDGE_LIFECYCLE.ru.md). Candidate `nk-knowledge-lifecycle/A6-draft-1`.

### A7 — Conflict, Uncertainty, and Revision Model
**Status:** `DRAFTED / PROVISIONAL` — [EN](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.md) / [RU](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md). Candidate `nk-conflict-uncertainty-revision/A7-draft-1`.

### A8 — Substrate-independence Contract
**Status:** `DRAFTED / PROVISIONAL` — [EN](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md) / [RU](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md). Candidate `nk-substrate-independence/A8-draft-1` defines preservation of meaning-level obligations rather than physical sameness. `substrate-independent specification ≠ universal portability proof`.

### A9 — Reference Laboratory Boundary

**Status:** `DRAFTED / PROVISIONAL` — [EN](./A9_REFERENCE_LABORATORY_BOUNDARY.md) / [RU](./A9_REFERENCE_LABORATORY_BOUNDARY.ru.md). Candidate `nk-reference-laboratory-boundary/A9-draft-1`.

A9 classifies P1–C5 mechanisms against A1–A8 with six scoped roles:

```text
ARCHITECTURE_PRESERVING_EVIDENCE
PROFILE_SPECIFIC_REALIZATION
PARTIAL_ARCHITECTURE_COVERAGE
FALSIFICATION_INSTRUMENT
LABORATORY_ONLY_CONSTRAINT
NOT_ARCHITECTURE_EVIDENCE
```

A mechanism may have multiple roles. Current Python/PostgreSQL/SQLite/Event/reducer/Receipt/hash/sequence/CI mechanisms remain valid within accepted versioned laboratory contracts without becoming universal Canon.

P5/C3 is real but narrow evidence for replaceable storage-profile realization inside a shared Python/conventional-digital lineage:

```text
PostgreSQL ↔ SQLite C3
= useful cross-profile evidence
≠ independent-language equivalence
≠ independent-computation-model equivalence
≠ arbitrary-substrate portability proof
```

A9 also establishes the preservation rule:

```text
profile-specific
→ label correctly
→ preserve reproducibility
→ keep evidence lineage
→ prevent silent Canon promotion
≠ delete or rewrite automatically
```

P4/C4/C5 remain useful measurement/falsification instruments; C5 remains synthetic bounded operational evidence, not production or independent-custody evidence.

**First-draft completion test:** satisfied for the principal P1–C5 mechanisms. A reviewer can identify the A1–A8 obligation exercised, A9 role, actual proof boundary, non-proof boundary, and whether replacement of the mechanism would necessarily alter Native Kernel meaning.

### A10 — Open Questions and Falsification Criteria

**Status:** `DRAFTED / PROVISIONAL` — [EN](./A10_OPEN_QUESTIONS_AND_FALSIFICATION.md) / [RU](./A10_OPEN_QUESTIONS_AND_FALSIFICATION.ru.md). Candidate `nk-open-questions-falsification/A10-draft-1`.

A10 records major unproved hypotheses, falsifiers, weakening conditions, open questions, evidence-independence dimensions, contrasting substrate thought experiments and stop conditions. It distinguishes `SUPPORTED_FOR_SCOPE`, `WEAKENED`, `REFUTED`, `INDETERMINATE`, and `NOT_TESTED`; these are research outcomes rather than replacements for P4 or A8 states.

A10 explicitly covers minimum non-event-sourced history/accountability, reconstruction without exact replay, lossy identity continuity, independent-language evidence thresholds, analog/neuromorphic persistence, probabilistic conformance, forgetting/physical-deletion observability, bounded-memory auditability, decentralized Authority, non-classical computation and evidence independence.

**First-draft completion test:** satisfied as a falsification/open-question inventory. It does not prove the hypotheses. Final acceptance still requires integrated A1–A10 review and a separate operator decision.

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
→ A9 Reference Laboratory Boundary              DRAFTED / PROVISIONAL
→ A10 Open Questions and Falsification           DRAFTED / PROVISIONAL
→ integrated A1-A10 review                     NEXT GATE
→ separate operator decision before runtime expansion
```

Later review may refine earlier drafts only explicitly; it may not silently redefine them.

## 5. Research method

Each deliverable should contain definitions, non-equivalences, a candidate formal model, counterexamples/failure cases, unresolved questions, mapping to existing contracts/runtime, contrasting substrate mappings, review status and evidence boundary.

Sources, papers, existing systems and AI analysis are inputs; none becomes Canon automatically.

## 6. Runtime freeze policy

Allowed: architecture research; integrity/security/reproducibility/provenance repair; evidence preservation; current-truth/validator repair; historical recovery; isolated falsification experiments without runtime promotion.

Not authorized without a separate operator decision: new semantic runtime features, reducer v2, new Event vocabulary, new databases/language profiles/model adapters/ecosystem integrations, executable NK-EPI/Temporal/full Admission, operational deletion expansion, maturity promotion or production authorization.

## 7. Relationship to existing contracts and pending decisions

A10 does not change ADR statuses or historical evidence. Issue #14/#15/#16/#17 retain their existing scopes. Issue #18 remains operator-controlled for license/publication. Issue #74 / ADR-0024 remains `PROPOSED / PENDING_OPERATOR`; reducer v1 stays immutable and reducer-v2 unauthorized. ADR-0003 remains `PROPOSED / NOT_STARTED`. Track H source admission remains operator-controlled.

```text
A1-A10 drafted blueprint
→ integrated A1-A10 review
→ existing contracts reconciled within declared scope
→ separate operator decision
≠ silent retroactive rewrite
≠ automatic runtime thaw
```

## 8. Blueprint completion gate

The blueprint is not complete merely because documents exist. Draft inventory completion now has all A1–A10 deliverables, but blueprint acceptance still requires terminology reconciliation, explicit contradictions/unknowns, labelled implementation assumptions, falsification coverage, existing-contract mapping, contrasting substrate thought experiments, critical integrated review and a separate operator decision for any next phase.

## 9. Current progress

```text
Architecture Re-foundation decision: established by ADR-0025
Blueprint plan: this document
Blueprint content: A1-A10 DRAFTED / PROVISIONAL
Next bounded gate: INTEGRATED_A1_A10_REVIEW
Runtime expansion: FROZEN
Existing P1–C5 laboratory: PRESERVED / BOUNDED
Production authorization: false
```

A1–A10 drafting does not establish independent approval, integrated Canon, runtime implementation, arbitrary future-substrate support, or production readiness.
