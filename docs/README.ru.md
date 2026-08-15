# 📚 Документация Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

> **Текущая граница:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`  
> **Активная фаза:** `POST-BLUEPRINT VALIDATION / A10-H11 SELECTED / EXECUTION ADMISSION BLOCKED / RUNTIME EXPANSION FROZEN`

## Начать здесь

| Документ | Роль |
|---|---|
| [`../STATUS.md`](../STATUS.md) | primary human current-status summary + явно помеченная история |
| [`../project-state.json`](../project-state.json) | committed machine state (`nk-project-state/2`) |
| [`../ROADMAP.md`](../ROADMAP.md) | active residual order и authorization boundaries + помеченная chronology |
| [`../ARCHITECTURE.md`](../ARCHITECTURE.md) | Formal Architecture entrypoint и current provisional authority route |
| [`ARCHITECTURE_REFOUNDATION.ru.md`](./ARCHITECTURE_REFOUNDATION.ru.md) | blueprint/refoundation history |
| [`INTEGRATED_A1_A10_REVIEW.ru.md`](./INTEGRATED_A1_A10_REVIEW.ru.md) | integrated review / provisional architecture evidence |
| [`reviews/IAR-1_RESULT.ru.md`](./reviews/IAR-1_RESULT.ru.md) / [`EN`](./reviews/IAR-1_RESULT.md) / [`JSON`](./reviews/IAR-1_RESULT.json) | qualifying independent architecture-review result |
| [`reviews/IAR-1_RECONCILIATION.ru.md`](./reviews/IAR-1_RECONCILIATION.ru.md) / [`EN`](./reviews/IAR-1_RECONCILIATION.md) / [`JSON`](./reviews/IAR-1_RECONCILIATION.json) | current provisional interpretation там, где reconciliation сужает first-draft wording |
| [`research/RESIDUAL_A10_VALIDATION_PLAN.ru.md`](./research/RESIDUAL_A10_VALIDATION_PLAN.ru.md) / [`JSON`](./research/RESIDUAL_A10_VALIDATION_PLAN.json) | residual A10 research order |
| [`research/H11_PREREGISTRATION.md`](./research/H11_PREREGISTRATION.md) / [`JSON`](./research/H11_PREREGISTRATION.json) | frozen H11 preregistration |
| [`research/H11_EXECUTION_ADMISSION.json`](./research/H11_EXECUTION_ADMISSION.json) | текущая fail-closed H11 admission record |
| [`ai/CURRENT_STATE.md`](./ai/CURRENT_STATE.md) | current-only AI/agent projection |
| [`../AGENTS.md`](../AGENTS.md) | repository operating constraints |

First-draft документы A1–A10 сохраняются и остаются provisional. Они не являются Final Canon; architecture meaning разрешается через Integrated Review / IAR-1 / IAR-1-R1 и более позднюю accepted authority только для явно принадлежащего ей scope.

## Порядок чтения

```text
STATUS + project-state
→ ROADMAP
→ ARCHITECTURE
→ first-draft provenance A1–A10
→ Integrated A1–A10 Review
→ IAR-1 result
→ IAR-1-R1 reconciliation
→ current residual-A10 / H11 records
→ relevant accepted contracts/ADRs
→ reference runtime/tests/evidence
```

## Historical architecture milestones — not current gates

Bilingual documentation contract явно сохраняет эти исторические identities:

```text
A1-A10 DRAFTED / PROVISIONAL
ADR-0026
INDEPENDENT_ARCHITECTURE_REVIEW
```

Они фиксируют завершённые/provisional milestones architecture-refoundation lineage и **не** переопределяют текущий H11 gate ниже.

## Текущая карта

```text
H historical recovery: OPEN / BLOCKED / operator-controlled source admission
C clean implementation: PRESERVED / PARTIAL / BOUNDED_REFERENCE_LABORATORY
R post-blueprint validation: ACTIVE / H11 EXECUTION ADMISSION BLOCKED
architecture: PROVISIONAL / interpreted through IAR-1-R1 / Final Canon deferred
selected family: A10-H11
current gate: A10_H11_EXECUTION_ADMISSION
admission: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER
reviewer/reproducer: NOT_ESTABLISHED
H11 outcome: NOT_TESTED
H11 implementation/execution: NOT AUTHORIZED
runtime expansion: FROZEN
kernel runtime: C4
operational validation: C5_BOUNDED_REHEARSAL
assertions: 45 / 10 / 17 / 0
NK-EPI: 0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
production: NOT AUTHORIZED
```

Frozen H11 plan identity: `H11-001-c5-lab-canon-separation-v1`; SHA-256 `60da649e675b79b3e70bf8a61cf03cb4d57bb989f4934b65ab8d50c925b19914`. PR #131 остаётся external reviewer/reproducer surface. CI, owner review, model agreement или repository-local identity не могут создать qualifying independence.

## Current reconciled distinctions

```text
PHYSICALLY_ERASED ≠ CRYPTOGRAPHICALLY_ERASED
physical/crypto erasure assertion ≠ independently verified substrate condition
FORGOTTEN_OR_LOST ≠ deliberate erasure claim
Uncertainty ≠ one universal confidence scalar
Conflict ≠ necessarily Contradiction
A3 transition catalogue ≠ mandatory Kernel shape
A6 lifecycle positions ≠ mandatory Kernel shape
bounded accountability ≠ exact reconstruction
history visibility ≠ mandatory Event sourcing
local scoped conformance ≠ composition/federation conformance
A10 outcome protocol = SUPPORTED_FOR_SCOPE / WEAKENED / REFUTED / INDETERMINATE / NOT_TESTED
NOT_TESTED ≠ SUPPORTED
reference laboratory ≠ architecture authority
existing mechanism ≠ architecture requirement
substrate-independent specification ≠ universal portability proof
qualifying review ≠ execution admission
blocked admission ≠ INDETERMINATE
falsification instrument ≠ product runtime
```

## Hard stop

`A10_H11_EXECUTION_ADMISSION` — текущий gate, и он fail-closed. H11 остаётся `NOT_TESTED`, пока не установлен qualifying independent reviewer/reproducer и admission не будет отдельно reassessed. Runtime остаётся `FROZEN`; Final Canon и production не авторизованы. Issue #18, Issue #74 / ADR-0024, ADR-0003 и Track H остаются unchanged/operator-controlled.