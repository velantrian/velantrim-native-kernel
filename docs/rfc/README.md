# 📐 Research RFCs

[← Project README](../../README.md) · [Русский README](../../README.ru.md) · [ADR index](../adr/README.md)

Research RFCs describe bounded future mechanisms, contracts, and evaluation plans.

They do not prove implementation, acceptance, runtime safety, or production readiness.

```text
RFC status
≠ ADR decision status
≠ evidence level
≠ implementation status
```

## Index

| RFC | Title | Status | Implementation |
|---|---|---|---|
| [`0001`](./0001-curiosity-core-architecture.md) · [Русский](./0001-curiosity-core-architecture.ru.md) | Curiosity Core Architecture | `PROPOSED / DOCUMENTED_ONLY` | `NOT_STARTED` |

## Rules

1. An RFC may propose new event vocabulary, data contracts, policies, or evaluation stages without making them Canon.
2. Architecture-changing proposals require a linked ADR.
3. Any implementation requires a separate pull request, tests, failure cases, and status update.
4. Issue #1 controlled import must not absorb RFC mechanisms or semantic redesign.
5. Titan and Crystal integrations remain optional and require their own bounded review.
6. Multi-model agreement is design input, not acceptance evidence.
