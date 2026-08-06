# 📐 Research RFCs

[← Project README](../../README.md) · [Русский README](../../README.ru.md) · [ADR index](../adr/README.md)

Research RFCs describe bounded future mechanisms, contracts, implementation-profile plans and evaluation stages.

An RFC status remains separate from implementation and evidence:

```text
RFC acceptance
≠ implementation completeness
≠ runtime conformance
≠ production readiness
```

## Index

| RFC | Title | Decision / evidence | Implementation |
|---|---|---|---|
| [`0001`](./0001-curiosity-core-architecture.md) · [Русский](./0001-curiosity-core-architecture.ru.md) | Curiosity Core Architecture | `PROPOSED / DOCUMENTED_ONLY` | `NOT_STARTED` |
| [`0002`](./0002-postgresql-reference-profile-v0.md) · [Русский](./0002-postgresql-reference-profile-v0.ru.md) | PostgreSQL Reference Profile v0 Planning Contract | `ACCEPTED / APPROVED / P1 LOCALLY_TESTED` | `PARTIAL — P1 SEMANTIC CORE` |

## RFC-0002 current boundary

RFC-0002 accepts the clean profile lineage `clean/postgresql-reference/0.1` and authorizes only P1.

```text
P0 profile planning:                       COMPLETE
P1 profile-independent semantic core:      PARTIAL / LOCALLY_TESTED
P2 PostgreSQL append/idempotency adapter:   NOT_AUTHORIZED
P3–P5:                                      NOT_AUTHORIZED
Kernel runtime conformance:                 UNSUPPORTED
```

Read together:

- [`../adr/0015-accept-clean-profile-and-authorize-p1-semantic-core.md`](../adr/0015-accept-clean-profile-and-authorize-p1-semantic-core.md);
- historical P0 planning manifest: [`../../profiles/postgresql-reference-v0/profile-manifest.json`](../../profiles/postgresql-reference-v0/profile-manifest.json);
- current P1 implementation manifest: [`../../profiles/postgresql-reference-v0/p1-manifest.json`](../../profiles/postgresql-reference-v0/p1-manifest.json);
- semantic-core boundary: [`../../native_kernel/semantic_core/README.md`](../../native_kernel/semantic_core/README.md).

```text
clean P1 implementation
≠ recovered v0.1.2.1
≠ PostgreSQL adapter
≠ C1/C2/C3
```

## Rules

1. An RFC may propose or govern mechanisms, policies, profiles or evaluation stages without making implementation complete.
2. Architecture-changing proposals require a linked ADR.
3. Every implementation phase requires a separately scoped PR, tests, failure cases and status update.
4. Issue #1 controlled import must not absorb clean-profile redesign.
5. Titan, Mentaury and Crystal integrations require their own bounded review.
6. Multi-model agreement is design input, not acceptance evidence.
7. Planning coverage and code presence must not be converted into assertion-level conformance without an evidence adapter.
8. Later RFC-0002 phases require separate operator GO.
