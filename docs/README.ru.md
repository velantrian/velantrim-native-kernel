# 📚 Документация Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

> **Текущая граница:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`  
> **Активная фаза:** `ARCHITECTURE RE-FOUNDATION / BLUEPRINT-FIRST / RUNTIME EXPANSION FROZEN`

## Начать здесь

| Документ | Роль |
|---|---|
| [`../STATUS.md`](../STATUS.md) | authoritative human current state |
| [`../project-state.json`](../project-state.json) | committed machine state (`nk-project-state/2`) |
| [`../ROADMAP.md`](../ROADMAP.md) | active sequence и authorization boundaries |
| [`ARCHITECTURE_REFOUNDATION.ru.md`](./ARCHITECTURE_REFOUNDATION.ru.md) | активный blueprint plan |
| [`ARCHITECTURE_REFOUNDATION.md`](./ARCHITECTURE_REFOUNDATION.md) | English blueprint plan |
| [`A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md`](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md) | A1 drafted / provisional |
| [`A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md`](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md) | A2 drafted / provisional |
| [`A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md`](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md) | A3 drafted / provisional |
| [`A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md`](./A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md) | A4 drafted / provisional |
| [`A5_IDENTITY_TIME_AND_CHANGE.ru.md`](./A5_IDENTITY_TIME_AND_CHANGE.ru.md) | A5 drafted / provisional |
| [`A5_IDENTITY_TIME_AND_CHANGE.md`](./A5_IDENTITY_TIME_AND_CHANGE.md) | English A5 |
| [`A6_KNOWLEDGE_LIFECYCLE.ru.md`](./A6_KNOWLEDGE_LIFECYCLE.ru.md) | A6 drafted / provisional |
| [`A6_KNOWLEDGE_LIFECYCLE.md`](./A6_KNOWLEDGE_LIFECYCLE.md) | English A6 |
| [`../AGENTS.md`](../AGENTS.md) | обязательные repository instructions |
| [`ai/CURRENT_STATE.md`](./ai/CURRENT_STATE.md) | compact AI continuity state |
| [`ai/KNOWN_RISKS.md`](./ai/KNOWN_RISKS.md) | active risks |
| [`adr/README.md`](./adr/README.md) | accepted/proposed decisions |
| [`../evidence/c5/README.md`](../evidence/c5/README.md) | immutable evidence boundaries |
| [`QUICKSTART.ru.md`](./QUICKSTART.ru.md) | setup/tests reference laboratory |
| [`GLOSSARY.ru.md`](./GLOSSARY.ru.md) | onboarding terminology; provisional A2–A6 blueprint distinctions имеют приоритет during integrated review |

## Порядок чтения

```text
STATUS + project-state
→ active ROADMAP
→ Architecture Re-foundation plan
→ provisional blueprint deliverables A1–A6
→ relevant Canon и ADRs
→ только затем reference runtime, tests и evidence
```

## Текущая карта

```text
H historical recovery: OPEN / BLOCKED / independent
C clean implementation: PRESERVED / PARTIAL / BOUNDED REFERENCE LABORATORY
R architecture re-foundation: ACTIVE / BLUEPRINT-FIRST

blueprint content: A1-A6 DRAFTED / PROVISIONAL
next content slice: A7 CONFLICT, UNCERTAINTY, AND REVISION
kernel runtime: C4
operational validation: C5_BOUNDED_REHEARSAL
assertions: 45 / 10 / 17 / 0
NK-EPI: 0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
production: NOT AUTHORIZED
```

A4 law-set candidate — `nk-semantic-laws/A4-draft-1` с 28 provisional laws. A5 candidate — `nk-identity-time-change/A5-draft-1`, defining typed/scoped identity, named temporal/order relations и explicit change effects без требования одного physical encoding. A6 candidate — `nk-knowledge-lifecycle/A6-draft-1`, моделирующий knowledge lifecycle как labeled directed graph девяти повторяющихся phases, отображённых на transition families A3, без сворачивания в единый linear pipeline.

## Активная последовательность

```text
A1 Purpose and Non-goals                         DRAFTED / PROVISIONAL
→ A2 Knowledge and Memory Ontology              DRAFTED / PROVISIONAL
→ A3 Abstract Native Kernel Machine             DRAFTED / PROVISIONAL
→ A4 Semantic Laws and Invariants               DRAFTED / PROVISIONAL
→ A5 Identity / Time / Change                   DRAFTED / PROVISIONAL
→ A6 Knowledge Lifecycle                        DRAFTED / PROVISIONAL
→ A7 Conflict / Uncertainty / Revision          NEXT BOUNDED SLICE
→ A8 Substrate-independence Contract
→ A9 Reference Laboratory Boundary
→ A10 Open Questions / Falsification
→ integrated blueprint review
→ separate operator decision before runtime expansion
```

ADR-0025 сохраняет current implementation как bounded laboratory и замораживает semantic/runtime expansion. Issue #18 остаётся `PENDING_OPERATOR`; Issue #74 / ADR-0024 остаётся `PROPOSED / PENDING_OPERATOR`, reducer-v2 unauthorized.

## Обязательные различия

```text
reference laboratory ≠ final architecture
blueprint documentation ≠ implementation evidence
Observation ≠ Claim
Claim ≠ Truth
Evidence ≠ Source
Repetition ≠ Evidence
Belief ≠ Knowledge
Memory ≠ merely a stored Record
retrieval relevance ≠ epistemic validity
Conflict ≠ necessarily Contradiction
Unknown ≠ False
Event usage in P1-C5 ≠ Event as universal primitive
State ≠ necessarily reducer output
Knowledge ≠ LLM / embeddings / SQL / JSON / specific processor
abstract machine ≠ runtime implementation
transition ≠ Event envelope
history visibility ≠ mandatory Event sourcing
semantic identity ≠ storage identity
equal bytes/hash/text ≠ universal semantic identity
write order ≠ represented-world or causal order
Revision ≠ silent overwrite
Supersession ≠ deletion or falsity
restriction ≠ logical erasure ≠ physical deletion ≠ cryptographic erasure ≠ forgetting
Receipt/accountability ≠ correctness or truth
profile conformance ≠ production authorization
C5 PASS ≠ production readiness
logical ERASED ≠ physical deletion
public repository ≠ open-source license
future-facing design ≠ demonstrated future substrate support
lifecycle phase ≠ storage status column
closure ≠ deletion of history
one Event ≠ one lifecycle transition
```

Current technologies остаются заменяемыми research instruments, а не Architecture Canon.
