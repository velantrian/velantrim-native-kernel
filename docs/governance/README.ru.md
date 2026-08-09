# ⚖️ Governance и operator decisions

**[English](./README.md) · [Русский](./README.ru.md)**

Эта директория содержит decision packages и машиночитаемое состояние незавершённых решений. Она не предоставляет automatic authorization.

## Текущие пакеты

| Решение | Issue | Состояние | Пакет |
|---|---:|---|---|
| License и publication terms | #18 | `PENDING_OPERATOR` | [`LICENSE_PUBLICATION_DECISION_OPTIONS.ru.md`](./LICENSE_PUBLICATION_DECISION_OPTIONS.ru.md) |
| ADR-0024 reducer referential semantics | #74 | `PENDING_OPERATOR` | [`../adr/0024-operator-decision-package.ru.md`](../adr/0024-operator-decision-package.ru.md) |

Машиночитаемое состояние:

- [`operator-decisions-v1.json`](./operator-decisions-v1.json)

## Текущий эффект

```text
license selected:             NO
external contributions open: NO
package publication allowed: NO
ADR-0024 accepted:            NO
reducer-v2 runtime allowed:   NO
production authorized:        NO
```

## Правило решения

Только explicit operator decision может заменить `PENDING_OPERATOR`. Финальное решение должно указывать точный scope, rationale, effective checkpoint и необходимые follow-up PRs.

```text
decision package
≠ operator decision
≠ runtime implementation
≠ evidence
≠ production authorization
```
