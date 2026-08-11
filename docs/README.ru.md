# 📚 Документация Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

> **Текущая граница:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`  
> **Активная фаза:** `POST-BLUEPRINT VALIDATION / INDEPENDENT-REVIEW-FIRST / RUNTIME EXPANSION FROZEN`

## Начать здесь

| Документ | Роль |
|---|---|
| [`../STATUS.md`](../STATUS.md) | authoritative human current state |
| [`../project-state.json`](../project-state.json) | committed machine state (`nk-project-state/2`) |
| [`../ROADMAP.md`](../ROADMAP.md) | active sequence и authorization boundaries |
| [`ARCHITECTURE_REFOUNDATION.ru.md`](./ARCHITECTURE_REFOUNDATION.ru.md) | blueprint/refoundation history и current validation gate |
| [`INTEGRATED_A1_A10_REVIEW.ru.md`](./INTEGRATED_A1_A10_REVIEW.ru.md) | integrated review / current provisional reconciliation |
| [`INTEGRATED_A1_A10_REVIEW.md`](./INTEGRATED_A1_A10_REVIEW.md) | English integrated review |
| [`INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md`](./INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md) | active independent-review protocol |
| [`INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md`](./INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md) | English independent-review protocol |
| [`adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md`](./adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md) | operator-approved Option D decision |
| [`ai/CURRENT_STATE.md`](./ai/CURRENT_STATE.md) | compact AI current state |
| [`../AGENTS.md`](../AGENTS.md) | mandatory repository instructions |

First-draft документы A1–A10 сохраняются и остаются `DRAFTED / PROVISIONAL`.

## Порядок чтения

```text
STATUS + project-state
→ ROADMAP
→ Architecture Re-foundation plan
→ first drafts A1–A10
→ Integrated A1–A10 Review
→ ADR-0026 Option D decision
→ Independent Architecture Review Protocol
→ relevant accepted contracts/ADRs
→ reference runtime/tests/evidence
```

## Текущая карта

```text
H historical recovery: OPEN / BLOCKED / independent
C clean implementation: PRESERVED / PARTIAL / BOUNDED REFERENCE LABORATORY
R post-blueprint validation: ACTIVE / INDEPENDENT-REVIEW-FIRST
blueprint content: A1-A10 DRAFTED / PROVISIONAL
integrated review: COMPLETED / PROVISIONAL
completed review gate identity: INTEGRATED_A1_A10_REVIEW
operator post-blueprint choice: OPTION D / ADR-0026 / APPROVED
next gate: INDEPENDENT_ARCHITECTURE_REVIEW
independent architectural validation: NOT ESTABLISHED
BPV-1: BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION
kernel runtime: C4
operational validation: C5_BOUNDED_REHEARSAL
assertions: 45 / 10 / 17 / 0
NK-EPI: 0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
production: NOT AUTHORIZED
```

Integrated review identity: `nk-integrated-blueprint-review/A1-A10-review-1`. Independent-review protocol identity: `nk-independent-architecture-review/1`.

## Current integrated distinctions

```text
PHYSICALLY_ERASED ≠ CRYPTOGRAPHICALLY_ERASED
FORGOTTEN_OR_LOST ≠ deliberate erasure claim
Uncertainty ≠ one universal confidence scalar
Conflict ≠ necessarily Contradiction
A6 lifecycle positions ≠ mandatory pipeline
A10 outcome protocol = SUPPORTED_FOR_SCOPE / WEAKENED / REFUTED / INDETERMINATE / NOT_TESTED
NOT_TESTED ≠ SUPPORTED
reference laboratory ≠ final architecture
existing mechanism ≠ architecture requirement
substrate-independent specification ≠ universal portability proof
operator approval ≠ independent validation
independent review protocol ≠ completed independent review
falsification instrument ≠ product runtime
```

После explicit reconciliation integrated review не нашёл remaining known blocking internal semantic contradiction, но independent architectural validation остаётся `NOT ESTABLISHED`.

## Hard stop

`INDEPENDENT_ARCHITECTURE_REVIEW` — следующий gate. BPV-1 нельзя начинать до qualifying independent review и reconciliation. Runtime остаётся `FROZEN`; A1–A10 остаётся provisional. Issue #18, Issue #74 / ADR-0024, ADR-0003 и Track H boundaries остаются unchanged/operator-controlled.