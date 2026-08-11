# 📚 Документация Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

> **Текущая граница:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`  
> **Активная фаза:** `POST-BLUEPRINT VALIDATION / IAR-1 RECONCILED / BPV1 PLAN NEXT / RUNTIME EXPANSION FROZEN`

## Начать здесь

| Документ | Роль |
|---|---|
| [`../STATUS.md`](../STATUS.md) | authoritative human current state |
| [`../project-state.json`](../project-state.json) | committed machine state (`nk-project-state/2`) |
| [`../ROADMAP.md`](../ROADMAP.md) | active sequence и authorization boundaries |
| [`ARCHITECTURE_REFOUNDATION.ru.md`](./ARCHITECTURE_REFOUNDATION.ru.md) | blueprint/refoundation history и current validation gate |
| [`INTEGRATED_A1_A10_REVIEW.ru.md`](./INTEGRATED_A1_A10_REVIEW.ru.md) | historical integrated review / provisional reconciliation |
| [`INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md`](./INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md) | normative independent-review protocol; publication-time status является историческим |
| [`reviews/IAR-1_RESULT.ru.md`](./reviews/IAR-1_RESULT.ru.md) / [`EN`](./reviews/IAR-1_RESULT.md) / [`JSON`](./reviews/IAR-1_RESULT.json) | qualifying independent review result |
| [`reviews/IAR-1_RECONCILIATION.ru.md`](./reviews/IAR-1_RECONCILIATION.ru.md) / [`EN`](./reviews/IAR-1_RECONCILIATION.md) / [`JSON`](./reviews/IAR-1_RECONCILIATION.json) | current provisional architecture reconciliation |
| [`adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md`](./adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md) | operator-approved Option D decision |
| [`ai/CURRENT_STATE.md`](./ai/CURRENT_STATE.md) | compact AI current state |
| [`../AGENTS.md`](../AGENTS.md) | обязательные repository instructions |

First-draft документы A1–A10 сохраняются и остаются `DRAFTED / PROVISIONAL / RECONCILED BY OVERLAY`.

## Порядок чтения

```text
STATUS + project-state
→ ROADMAP
→ Architecture Re-foundation
→ first drafts A1–A10
→ Integrated A1–A10 Review
→ ADR-0026 Option D
→ Independent Architecture Review Protocol
→ IAR-1 result
→ IAR-1-R1 reconciliation
→ relevant accepted contracts/ADRs
→ reference runtime/tests/evidence
```

## Текущая карта

```text
H historical recovery: OPEN / BLOCKED / independent
C clean implementation: PRESERVED / PARTIAL / BOUNDED REFERENCE LABORATORY
R post-blueprint validation: ACTIVE / IAR-1-RECONCILED / BPV1-PLAN-NEXT
blueprint content: A1-A10 DRAFTED / PROVISIONAL / RECONCILED BY OVERLAY
integrated review: COMPLETED / PROVISIONAL
operator post-blueprint choice: OPTION D / ADR-0026 / APPROVED
independent architecture review: IAR-1 / QUALIFYING_REVIEW_COMPLETE
IAR-1 findings: 10 total / 7 BLOCKING / 3 MATERIAL
IAR-1-R1: COMPLETE / open blockers 0 / open material 0
next gate: BPV1_PLAN_AND_PREREGISTRATION
BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN
kernel runtime: C4
operational validation: C5_BOUNDED_REHEARSAL
assertions: 45 / 10 / 17 / 0
NK-EPI: 0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
production: NOT AUTHORIZED
runtime expansion: FROZEN
```

Integrated review identity: `nk-integrated-blueprint-review/A1-A10-review-1`. Independent-review protocol identity: `nk-independent-architecture-review/1`. Reconciliation identity: `IAR-1-R1`.

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
reference laboratory ≠ final architecture
existing mechanism ≠ architecture requirement
substrate-independent specification ≠ universal portability proof
qualifying independent review ≠ architecture proof
review reconciliation ≠ BPV-1 execution authorization
falsification instrument ≠ product runtime
```

## Hard stop

`BPV1_PLAN_AND_PREREGISTRATION` — следующий gate. BPV-1 implementation/execution нельзя начинать до authoritative plan, фиксирующего required scope, obligations, applicability, observables, equivalence predicates, allowed losses, failure thresholds, hard refutations, grounding mode, threat model и oracle Authority. Runtime остаётся `FROZEN`; A1–A10 остаётся provisional. Issue #18, Issue #74 / ADR-0024, ADR-0003 и Track H остаются unchanged/operator-controlled.