# 🧬 Переоснование архитектуры — Blueprint before Runtime

**[English](./ARCHITECTURE_REFOUNDATION.md) · [Русский](./ARCHITECTURE_REFOUNDATION.ru.md)**

> **State:** `ACTIVE / BLUEPRINT-FIRST / RUNTIME EXPANSION FROZEN`  
> **Decision:** [`ADR-0025`](./adr/0025-blueprint-before-runtime-expansion.md)  
> **Issue:** [#88](https://github.com/velantrian/velantrim-native-kernel/issues/88)  
> **Граница evidence:** только architecture research/governance; без runtime, evidence, maturity или production promotion

## 1. Зачем нужна эта фаза

Native Kernel должен сохранять meaning, memory, knowledge, provenance, uncertainty, Change и accountability независимо от одного current technology stack. Существующая линия **Python + PostgreSQL + SQLite** сохраняется как bounded reference laboratory, но не становится permanent Canon только потому, что появилась первой.

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

## 2. Граница фазы

Этой фазе принадлежат ontology, semantic laws, abstract-machine obligations, identity/time/change, lifecycle, conflict/uncertainty/revision, substrate-independent obligations, mapping reference profiles, explicit unknowns и falsification criteria.

Ей не принадлежат new reducer, Event vocabulary, database, language port, LLM/vector adapter, product integration, performance-driven semantic change, production deployment или proof, что arbitrary future substrates уже conform.

## 3. Обязательные deliverables

### A1 — Purpose и Non-goals Kernel

**Status:** `DRAFTED / PROVISIONAL` — [RU](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md) / [EN](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md). Определяет Kernel problem, durable qualities, non-goals и ecosystem boundaries.

### A2 — Knowledge and Memory Ontology

**Status:** `DRAFTED / PROVISIONAL` — [RU](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md) / [EN](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md). Различает Signal, Observation, Record, Proposition, Claim, Interpretation, Hypothesis, Belief, Knowledge, Memory, Evidence, Source, Provenance, Context, Relation, State, Change, Event, Conflict, Contradiction, Uncertainty, Revision, Supersession, Authority и Receipt без превращения current storage/runtime representations в Canon.

### A3 — Абстрактная машина Native Kernel

**Status:** `DRAFTED / PROVISIONAL` — [RU](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md) / [EN](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md). Определяет provisional meaning-level configuration facets, transition families, failure/indeterminacy handling, Authority boundaries, order/concurrency и contrasting substrate mappings. `transition ≠ Event envelope`; `State ≠ reducer output` universally.

### A4 — Semantic Laws and Invariants

**Status:** `DRAFTED / PROVISIONAL` — [RU](./A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md) / [EN](./A4_SEMANTIC_LAWS_AND_INVARIANTS.md). Current law-set candidate `nk-semantic-laws/A4-draft-1` содержит 28 provisional/reviewable laws, защищающих representation/epistemic boundaries, Context/Provenance/Authority, identity/time/change, conflict/uncertainty, views/accountability и substrate/conformance distinctions.

### A5 — Модель Identity, Time и Change

**Status:** `DRAFTED / PROVISIONAL` — [RU](./A5_IDENTITY_TIME_AND_CHANGE.ru.md) / [EN](./A5_IDENTITY_TIME_AND_CHANGE.md). Ожидает independent review и integrated A1–A10 review.

A5 вводит candidate model `nk-identity-time-change/A5-draft-1`. Identity — typed/scoped relation, а не один universal identifier. Draft различает:

```text
REFERENT_IDENTITY
SEMANTIC_CONTENT_IDENTITY
CLAIM_POSITION_IDENTITY
RECORD_IDENTITY
LINEAGE_CONTINUITY_IDENTITY
OCCURRENCE_IDENTITY
SUBSTRATE_LOCAL_IDENTITY
```

Candidate scoped outcomes: `SAME`, `DISTINCT`, `CONTINUATION_OF`, `VERSION_OF`, `ALIAS_OF`, `MIGRATED_FROM`, `UNRESOLVED`.

A5 также различает `OCCURRENCE_TIME`, `VALID_TIME`, `OBSERVATION_TIME`, `ASSERTION_TIME`, `RECORD_TIME`, `DECISION_TIME`, `EFFECTIVE_TIME`, `WRITE_COMMIT_TIME`; и отделяет occurrence, observation, causal/dependency, lineage, authority-decision, local-write и migration/synchronization order.

Draft классифицирует storage relocation, re-encoding, copying, translation, correction, reinterpretation, Revision, Supersession, restriction, logical erasure, physical/cryptographic erasure, forgetting/loss и represented-world change без предположения одного identity effect для всех kinds.

A5 reconciles existing accepted/versioned contracts, а не silently supersede их. `nk-id/1.0` остаётся current versioned reference encoding contract; UTF-8/NFC/JSON/SHA-256 и `asserted_at` не становятся единственным substrate-independent identity mechanism. `global_seq`/`stream_seq` остаются reference-laboratory ordering realization. Deletion state machine остаётся bounded profile mechanism.

**First-draft completion test:** выполнен для bounded drafting scope: reader может назвать identity relation, temporal/order relation и semantic effect Change без требования одного physical encoding. Final acceptance всё ещё требует independent и integrated review.

### A6 — Knowledge Lifecycle

**Status:** `NEXT BOUNDED SLICE`.

Смоделировать lifecycle от encounter/registration через possible interpretation, support, admission/use, contest, revision, restriction и historical retention/forgetting. Lifecycle Authority не может возникать только из storage presence, retrieval rank, repetition, model confidence, recency или usefulness.

### A7 — Conflict, Uncertainty и Revision Model

Определить candidate vs established Conflict, Contradiction vs scope mismatch, unresolved plurality, uncertainty/provenance gaps, resolution Authority, reversibility, belief revision и возможность оставаться undecided. A7 может refine revision policy, но обязан сохранять A4/A5 history и identity distinctions.

### A8 — Substrate-independence Contract

Определить, что future profiles обязаны preserve/translate: semantic identity, Change/history visibility, Provenance, temporal meaning, uncertainty/conflict visibility, Authority/admission boundaries, bounded accountability, migration и explicit loss. Present Event-sourcing assumptions должны быть labelled как mechanisms, если их necessity не доказана.

### A9 — Граница Reference Laboratory

Классифицировать **Python + PostgreSQL + SQLite** P1–C5 mechanisms как examples, experiments, profile-specific choices, falsification tools или legacy evidence. Ничего не удаляется/переписывается только из-за profile-specific classification.

### A10 — Open Questions и Falsification Criteria

Зафиксировать unresolved architecture questions и evidence, которое способно weaken/refute major hypotheses: identity без stable serialized bytes, minimum history/reconstruction equivalents, analog/neuromorphic continuity, forgetting без forbidden retention и semantic equivalence across probabilistic substrates.

## 4. Последовательность работы

```text
A1 Purpose and Non-goals                         DRAFTED / PROVISIONAL
→ A2 Ontology                                   DRAFTED / PROVISIONAL
→ A3 Abstract Machine                           DRAFTED / PROVISIONAL
→ A4 Semantic Laws                              DRAFTED / PROVISIONAL
→ A5 Identity / Time / Change                   DRAFTED / PROVISIONAL
→ A6 Knowledge Lifecycle                       NEXT BOUNDED SLICE
→ A7 Conflict / Uncertainty / Revision
→ A8 Substrate Independence
→ A9 Reference Laboratory Boundary
→ A10 Open Questions / Falsification
→ integrated blueprint review
→ separate operator decision before runtime expansion
```

Later slices могут refine earlier drafts только явно; они не могут silently redefine их.

## 5. Research method

Каждый deliverable должен содержать definitions, non-equivalences, candidate formal model, counterexamples/failure cases, unresolved questions, mapping к existing contracts/runtime, contrasting substrate mappings, review status и evidence boundary.

Sources, papers, existing systems и AI analysis являются inputs и не становятся Canon автоматически.

## 6. Runtime freeze policy

Разрешены architecture research; integrity/security/reproducibility/provenance repair; evidence preservation; current-truth/validator repair; historical recovery; isolated falsification experiments без runtime promotion.

Не разрешены без separate operator decision: new semantic runtime features, reducer v2, new Event vocabulary, new databases/language profiles/model adapters/ecosystem integrations, executable NK-EPI/Temporal/full Admission, operational deletion expansion, maturity promotion или production authorization.

## 7. Связь с existing contracts и pending decisions

A5 не меняет ADR statuses или historical evidence. Issue #14/#15/#16 остаются open в своих remaining evidence/portability scopes. Issue #18 остаётся operator-controlled для license/publication. Issue #74 / ADR-0024 остаётся `PROPOSED / PENDING_OPERATOR`; reducer v1 immutable, reducer-v2 unauthorized. Track H source admission остаётся operator-controlled.

```text
A5 semantic model
→ later versioned mapping/equivalence work
→ existing contracts preserved within declared scope
≠ silent retroactive rewrite
```

## 8. Gate завершения blueprint

Blueprint не завершён только из-за наличия документов. Gate завершения blueprint требует всех A1–A10 deliverables, terminology reconciliation, explicit contradictions/unknowns, labelled implementation assumptions, falsification criteria, existing-contract mapping, contrasting substrate thought experiments, critical review, integrated review и separate operator decision для next phase.

## 9. Текущий прогресс

```text
Architecture Re-foundation decision: established by ADR-0025
Blueprint plan: this document
Blueprint content: A1-A5 DRAFTED / PROVISIONAL; A6-A10 NOT YET COMPLETE
Next bounded slice: A6 KNOWLEDGE LIFECYCLE
Runtime expansion: FROZEN
Existing P1–C5 laboratory: PRESERVED / BOUNDED
Production authorization: false
```

Drafting A1–A5 не устанавливает independent approval, integrated Canon, runtime implementation, arbitrary future-substrate support или production readiness.
