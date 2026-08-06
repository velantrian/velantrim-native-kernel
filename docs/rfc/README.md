# 📐 Research RFCs

[← Project README](../../README.md) · [Русский README](../../README.ru.md) · [ADR index](../adr/README.md)

Research RFCs describe bounded future mechanisms, contracts, implementation-profile plans, and evaluation stages.

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
| [`0002`](./0002-postgresql-reference-profile-v0.md) · [Русский](./0002-postgresql-reference-profile-v0.ru.md) | PostgreSQL Reference Profile v0 Planning Contract | `PROPOSED / DOCUMENTED_ONLY / OPERATOR_APPROVAL_PENDING` | `NOT_STARTED` |

## RFC-0002 boundary

RFC-0002 plans the first clean PostgreSQL implementation profile under evidence lineage `clean/postgresql-reference/0.1`.

```text
clean profile planning
≠ recovered v0.1.2.1
≠ runtime implementation GO
≠ C2/C3 evidence
```

Machine-readable planning manifest: [`../../profiles/postgresql-reference-v0/profile-manifest.json`](../../profiles/postgresql-reference-v0/profile-manifest.json).

## Rules

1. An RFC may propose new event vocabulary, data contracts, policies, profiles, or evaluation stages without making them Canon.
2. Architecture-changing proposals require a linked ADR.
3. Any implementation requires a separate pull request, tests, failure cases, and status update.
4. Issue #1 controlled import must not absorb RFC mechanisms or semantic redesign.
5. Titan and Crystal integrations remain optional and require their own bounded review.
6. Multi-model agreement is design input, not acceptance evidence.
7. A planning manifest must not use planned coverage as runtime support evidence.
8. New clean implementation lineages require explicit operator approval before runtime code begins.
