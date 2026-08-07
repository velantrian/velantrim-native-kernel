# 📐 Research RFCs

[← Project README](../../README.md) · [Русский README](../../README.ru.md) · [ADR index](../adr/README.md)

Research RFCs describe bounded mechanisms, contracts, implementation-profile plans and evaluation stages.

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
| [`0002`](./0002-postgresql-reference-profile-v0.md) · [Русский](./0002-postgresql-reference-profile-v0.ru.md) | Clean PostgreSQL/SQLite profile lifecycle | `ACCEPTED / APPROVED / C2+C3 PREVIOUS-HEAD EVIDENCE` | `PARTIAL — P1…P5` |

## RFC-0002 current boundary

```text
P0 planning:                       COMPLETE
P1 semantic core:                 MERGED / REPOSITORY-TESTED
P2 PostgreSQL append/idempotency: MERGED / REPOSITORY-INTEGRATION-TESTED
P3 replay/projections/Receipts:   MERGED / REPOSITORY-INTEGRATION-TESTED
P4 PostgreSQL C2:                 MERGED / PARTIAL
P5 SQLite C2 + cross-profile C3:  IMPLEMENTED / PARTIAL / PREVIOUS-HEAD EVIDENCE
C4/C5/production:                 NOT_AUTHORIZED / NOT_ESTABLISHED
```

Result maps:

```text
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
support_state:     PARTIAL
```

Read together:

- [`../adr/0019-authorize-p5-sqlite-and-c3-equivalence.md`](../adr/0019-authorize-p5-sqlite-and-c3-equivalence.md);
- [`../ai/P5_IMPLEMENTATION_RECORD.md`](../ai/P5_IMPLEMENTATION_RECORD.md);
- [`../../profiles/sqlite-embedded-v0/p5-manifest.json`](../../profiles/sqlite-embedded-v0/p5-manifest.json);
- [`../../native_kernel/sqlite_profile/README.md`](../../native_kernel/sqlite_profile/README.md);
- [`../CONFORMANCE_MODEL.md`](../CONFORMANCE_MODEL.md).

```text
clean P1–P5 implementation
≠ recovered v0.1.2.1
≠ support for all 72
≠ operational equivalence
≠ C4/C5 or production readiness
```

## Rules

1. An RFC can govern mechanisms/profiles without making implementation complete.
2. Architecture-changing proposals require a linked ADR.
3. Every implementation phase requires a scoped PR, tests, failures, evidence and status update.
4. Issue #1 controlled import must remain separate from clean-profile implementation.
5. Titan, Mentaury and Crystal integrations require their own bounded review.
6. Multi-model agreement is design input, not acceptance evidence.
7. Code presence and planning coverage are not assertion-level conformance.
8. C2/C3 require exact report/check/run/artifact traceability.
9. C3 semantic equivalence must not be described as operational equivalence.
10. C4/C5/production/deletion/integration require separate explicit operator GO.
