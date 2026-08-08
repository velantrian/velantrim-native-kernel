# 📚 Документация Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

> **Текущая граница:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`

## Начать здесь

| Документ | Назначение |
|---|---|
| [`QUICKSTART.ru.md`](./QUICKSTART.ru.md) | человеческий setup, закреплённый SQLite и первые test commands |
| [`GLOSSARY.ru.md`](./GLOSSARY.ru.md) | краткие термины и обязательные неэквивалентности |
| [`../STATUS.md`](../STATUS.md) | текущее состояние реализации/evidence |
| [`../project-state.json`](../project-state.json) | машиночитаемый snapshot состояния |
| [`../AGENTS.md`](../AGENTS.md) | обязательные правила репозитория |
| [`ai/README.md`](./ai/README.md) | карта continuity |
| [`ai/C5_IMPLEMENTATION_RECORD.md`](./ai/C5_IMPLEMENTATION_RECORD.md) | реализация и сохранение C5 evidence |
| [`../evidence/c5/README.md`](../evidence/c5/README.md) | точные сохранённые ZIP-архивы |
| [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md) | C0–C5 и границы assertions |
| [`adr/README.md`](./adr/README.md) | индекс решений |
| [`research/POST_C5_RESEARCH_BACKLOG.md`](./research/POST_C5_RESEARCH_BACKLOG.md) | только предлагаемые post-C5 исследования |
| [`INTEGRATION_BOUNDARIES.md`](./INTEGRATION_BOUNDARIES.md) | границы authority экосистемы |

## Текущая карта

```text
H historical recovery: OPEN / BLOCKED / independent
C clean implementation: P1–P5 + C4 + C5 / ACTIVE / PARTIAL
R long-horizon research: PROPOSED / BOUNDED

kernel_runtime_conformance: C4
operational_validation: C5_BOUNDED_REHEARSAL
assertions: 45 / 10 / 17 / 0
NK-EPI: 0 / 8 SUPPORTED
production: NOT AUTHORIZED
```

## Порядок чтения

```text
QUICKSTART + GLOSSARY
→ STATUS + project-state
→ AGENTS + AI context
→ C5 implementation/evidence archive
→ contracts + conformance model
→ ADRs
→ source/tests/workflows
→ research только для будущих направлений
```

## Центральное различие

```text
Architecture Canon
≠ Abstract Contract
≠ Accepted Decision
≠ Implementation Profile
≠ Evidence Layer
≠ Assertion Result
≠ Authority Promotion
≠ Production Evidence
```

PostgreSQL, SQLite, Python, JSON, graphs, vectors, LLM и hardware — инструменты, а не Canon.
