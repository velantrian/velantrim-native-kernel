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
| [`ARCHITECTURE_REFOUNDATION.ru.md`](./ARCHITECTURE_REFOUNDATION.ru.md) | blueprint plan/current phase |
| [`INTEGRATED_A1_A10_REVIEW.ru.md`](./INTEGRATED_A1_A10_REVIEW.ru.md) | integrated review / current provisional reconciliation |
| [`INTEGRATED_A1_A10_REVIEW.md`](./INTEGRATED_A1_A10_REVIEW.md) | English integrated review |
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
→ relevant accepted contracts/ADRs
→ reference runtime/tests/evidence
```

## Текущая карта

```text
H historical recovery: OPEN / BLOCKED / independent
C clean implementation: PRESERVED / PARTIAL / BOUNDED REFERENCE LABORATORY
R architecture re-foundation: ACTIVE / BLUEPRINT-FIRST
blueprint content: A1-A10 DRAFTED / PROVISIONAL
integrated review: COMPLETED / PROVISIONAL / OPERATOR_DECISION_PENDING
next gate: OPERATOR_POST_BLUEPRINT_DECISION
kernel runtime: C4
operational validation: C5_BOUNDED_REHEARSAL
assertions: 45 / 10 / 17 / 0
NK-EPI: 0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
production: NOT AUTHORIZED
```

Integrated review identity: `nk-integrated-blueprint-review/A1-A10-review-1`. Он явно reconciles `IR-F01`…`IR-F07`. Если first-draft wording конфликтует с review, нужно ссылаться на integrated review, а не silent rewrite history.

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
```

После explicit reconciliation review не нашёл remaining known blocking internal semantic contradiction, но independent architectural validation остаётся `NOT ESTABLISHED`.

## Hard stop

`OPERATOR_POST_BLUEPRINT_DECISION` — следующий gate. Это не A11 и не runtime thaw. Issue #18, Issue #74 / ADR-0024, ADR-0003 и Track H boundaries остаются unchanged/operator-controlled.
