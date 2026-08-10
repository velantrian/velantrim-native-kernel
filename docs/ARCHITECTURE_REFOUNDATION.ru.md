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

**Status:** `DRAFTED / PROVISIONAL` — [RU](./A6_KNOWLEDGE_LIFECYCLE.ru.md) / [EN](./A6_KNOWLEDGE_LIFECYCLE.md). Ожидает independent review и integrated A1–A10 review.

A6 вводит candidate model `nk-knowledge-lifecycle/A6-draft-1`. Knowledge lifecycle — labeled directed graph повторяющихся, reviewable конфигураций, а не linear pipeline. Определяет девять phases:

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

каждая отображается на одну или несколько из тринадцати transition families A3, плюс typed `LIFECYCLE_TRANSITION` relation, переиспользующий A3 outcome vocabulary вместо изобретения новых терминов. `DERIVE_BOUNDED_VIEW` и `SELECT_FOR_USE` — phase-referencing, not phase-changing.

A6 отделяет `LIFECYCLE_TRANSITION_ORDER` от `OCCURRENCE_ORDER`, `CAUSAL_DEPENDENCY_ORDER` и `LOCAL_WRITE_COMMIT_ORDER`, и расширяет восемь dispositions A3 тремя closure kinds — `LOGICALLY_ERASED`, `PHYSICALLY_OR_CRYPTOGRAPHICALLY_ERASED`, `FORGOTTEN_OR_LOST` — разрешающими erasure/forgetting distinctions, которые A5 назвал, но отложил.

A6 reconciles existing accepted/versioned contracts, а не silently supersede их. Mapping `ADMIT`/`LINK`/`UTILIZED`/`SUPERSEDED`/`ERASED` на lifecycle phases явно illustrative и non-canonical; он не авторизует новые Event verbs, не решает вопрос `Issue #74 / ADR-0024` и не расширяет deletion-execution scope `Issue #16`.

**First-draft completion test:** выполнен для bounded drafting scope: reader может назвать phase, transition family и legitimizing Authority или method перемещения knowledge item без предположения linear pipeline или единой storage schema. Final acceptance всё ещё требует independent и integrated review.

### A7 — Conflict, Uncertainty и Revision Model

**Status:** `DRAFTED / PROVISIONAL` — [RU](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md) / [EN](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.md). Ожидает independent review и integrated A1–A10 review.

A7 вводит candidate model `nk-conflict-uncertainty-revision/A7-draft-1`. Он уточняет accepted semantic boundary `NK-CFL`, не принимая proposed ADR-0003 и не добавляя conflict runtime.

Модель сохраняет независимыми:

```text
tension kind
≠ assessment status
≠ resolution status
```

Assessment status различает `CANDIDATE`, `ESTABLISHED`, `NOT_A_CONFLICT`, `UNRESOLVED_ASSESSMENT`. Resolution status различает `UNRESOLVED`, `DEFERRED`, `RESOLVED_FOR_SCOPE`, `REOPENED`. Scoped resolution — accountable decision, не objective truth.

Provisional taxonomy охватывает duplicate delivery, write-version race, divergent history, semantic contradiction, temporal/scope mismatch, provenance conflict, measurement disagreement, Authority/policy conflict, epistemic disagreement, projection drift и unclassified tension. Strict contradiction требует materially adequate alignment interpretation, Context/scope, time, modality/quantification, assumptions, identity, assessment Authority и known uncertainty.

A7 определяет meaning-level patterns `UNCERTAINTY_POSITION`, `TENSION_POSITION`, `EPISTEMIC_REVISION`. Uncertainty остаётся typed и не принуждается к одному global confidence scalar; universal uncertainty-combination algebra не выбирается. Detection Authority/method отделяется от resolution, epistemic-assessment, operational-disposition и architecture/governance Authority.

A7 явно допускает unresolved plurality, deferral, scoped preference, explicit revision, Supersession-for-scope, no-authorized-resolution и reopening. Он сохраняет A5 lineage и не меняет A6 phase inventory. `IN_TENSION` может оставаться open indefinitely; `RESOLVED_FOR_SCOPE` не означает автоматически `REVISED_OR_SUPERSEDED`.

A7 не принимает ADR-0003, не разрешает `CONFLICT_OPENED`/`CONFLICT_RESOLVED` Event verbs и не решает Issue #74 / ADR-0024 one/multi-successor topology, self-supersession, cycles или reducer-v2 migration.

**First-draft completion test:** выполнен для bounded drafting scope: reviewer может указать participants, tension kind, assessment status, alignment basis, uncertainty/provenance gaps, resolution status, Authority/policy/basis, resulting revision/non-revision effect и reopening conditions без обязательного winner algorithm, confidence scalar, Event vocabulary или physical substrate. Final acceptance всё ещё требует independent и integrated review.

### A8 — Substrate-independence Contract

**Status:** `NEXT BOUNDED SLICE`.

Определить, что future profiles обязаны preserve/translate: semantic identity, Change/history visibility, Provenance, temporal meaning, uncertainty/conflict visibility, Authority/admission boundaries, bounded accountability, migration и explicit loss. A8 должен превратить meaning-level obligations A1–A7 в substrate-independent conformance/equivalence requirements, не принимая current Event sourcing, SQL, Python или digital serialization за universal necessities.

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
→ A6 Knowledge Lifecycle                        DRAFTED / PROVISIONAL
→ A7 Conflict / Uncertainty / Revision          DRAFTED / PROVISIONAL
→ A8 Substrate-independence Contract            NEXT BOUNDED SLICE
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

A7 не меняет ADR statuses или historical evidence. Issue #14/#15/#16/#17 сохраняют existing scopes. Issue #18 остаётся operator-controlled для license/publication. Issue #74 / ADR-0024 остаётся `PROPOSED / PENDING_OPERATOR`; reducer v1 immutable, reducer-v2 unauthorized. ADR-0003 остаётся `PROPOSED / NOT_STARTED`. Track H source admission остаётся operator-controlled.

```text
A5/A6/A7 semantic, lifecycle, conflict and revision models
→ later A8 versioned mapping/equivalence work
→ existing contracts preserved within declared scope
≠ silent retroactive rewrite
```

## 8. Gate завершения blueprint

Blueprint не завершён только из-за наличия документов. Gate завершения blueprint требует всех A1–A10 deliverables, terminology reconciliation, explicit contradictions/unknowns, labelled implementation assumptions, falsification criteria, existing-contract mapping, contrasting substrate thought experiments, critical review, integrated review и separate operator decision для next phase.

## 9. Текущий прогресс

```text
Architecture Re-foundation decision: established by ADR-0025
Blueprint plan: this document
Blueprint content: A1-A7 DRAFTED / PROVISIONAL; A8-A10 NOT YET COMPLETE
Next bounded slice: A8 SUBSTRATE-INDEPENDENCE CONTRACT
Runtime expansion: FROZEN
Existing P1–C5 laboratory: PRESERVED / BOUNDED
Production authorization: false
```

Drafting A1–A7 не устанавливает independent approval, integrated Canon, runtime implementation, arbitrary future-substrate support или production readiness.