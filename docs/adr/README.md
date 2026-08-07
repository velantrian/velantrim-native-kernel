# 📝 Architecture Decision Records

[← Project README](../../README.md) · [Русский README](../../README.ru.md) · [Decision process](../DECISION_PROCESS.md) · [Research RFCs](../rfc/README.md)

Architecture Decision Records preserve why a durable architectural or implementation-profile boundary exists. They do not turn acceptance into empirical proof.

## Four independent dimensions

```text
Decision status
≠ Evidence level
≠ Implementation status
≠ Operator approval
```

## Index

| ADR | Title | Decision | Evidence | Implementation | Approval |
|---|---|---|---|---|---|
| [`0001`](./0001-architecture-canon-vs-implementation-profiles.md) | Architecture Canon is separate from Implementation Profiles | `ACCEPTED` | `DOCUMENTED` | documentation complete; portability unproven | `APPROVED` |
| [`0002`](./0002-state-checkpoints-are-disposable.md) | State Checkpoints are disposable replay accelerators | `PROPOSED` | `DOCUMENTED` | `NOT_STARTED` | `NOT_REQUESTED` |
| [`0003`](./0003-semantic-conflicts-require-explicit-resolution.md) | Semantic conflicts require explicit resolution | `PROPOSED` | `DOCUMENTED` | `NOT_STARTED` | `NOT_REQUESTED` |
| [`0004`](./0004-rebuild-from-authoritative-history.md) | Rebuild from authoritative history is the first conformance experiment | `PROPOSED` | `DOCUMENTED` | `NOT_STARTED` | `NOT_REQUESTED` |
| [`0005`](./0005-curiosity-core-is-optional-and-non-authoritative.md) | Curiosity Core is optional and non-authoritative | `PROPOSED` | `DOCUMENTED` | `NOT_STARTED` | `NOT_REQUESTED` |
| [`0006`](./0006-causal-links-are-relations.md) | Causal links are relations, not knowledge types | `ACCEPTED` | `DOCUMENTED` | `NOT_STARTED` | `APPROVED` |
| [`0007`](./0007-operator-approval-is-not-evidence.md) | Operator approval is separate from empirical evidence | `ACCEPTED` | `DOCUMENTED` | governance complete | `APPROVED` |
| [`0008`](./0008-epistemic-boundaries-are-representation-disciplines.md) | Epistemic boundaries are representation disciplines | `PROPOSED` | `DOCUMENTED` | `NOT_STARTED` | `PENDING` |
| [`0009`](./0009-postgresql-primary-sqlite-optional-profile.md) | PostgreSQL primary, SQLite optional | `ACCEPTED` | `DOCUMENTED` | profile direction | `APPROVED` |
| [`0010`](./0010-foundational-contract-families.md) | Foundational contracts separated by semantic role | `ACCEPTED` | `DOCUMENTED` | `NOT_STARTED` | `APPROVED` |
| [`0011`](./0011-canonical-identity-contract-v1.md) | Canonical identity contract v1 | `ACCEPTED` | vectors `LOCALLY_TESTED` | P1 path `PARTIAL` | `APPROVED` |
| [`0012`](./0012-single-writer-append-and-replay-contract-v1.md) | Single-writer append and replay contract v1 | `ACCEPTED` | fixtures `LOCALLY_TESTED` | P2 append path `PARTIAL`; replay absent | `APPROVED` |
| [`0013`](./0013-deletion-restriction-retention-contract-v1.md) | Deletion, restriction and retention contract v1 | `ACCEPTED` | fixtures/P1 transitions `LOCALLY_TESTED` | operational deletion absent | `APPROVED` |
| [`0014`](./0014-executable-conformance-fixture-protocol-v1.md) | Executable conformance fixture protocol v1 | `ACCEPTED` | tooling `LOCALLY_TESTED` | runtime adapter absent | `APPROVED` |
| [`0015`](./0015-accept-clean-profile-and-authorize-p1-semantic-core.md) | Accept clean lineage and authorize P1 | `ACCEPTED` | `LOCALLY_TESTED` | `PARTIAL — P1` | `APPROVED` |
| [`0016`](./0016-authorize-p2-postgresql-append-profile.md) | Authorize P2 PostgreSQL authoritative append profile | `ACCEPTED` | `LOCALLY_TESTED_UNIT_ONLY` | `PARTIAL — P2`; integration unproven | `APPROVED` |

## Current decision boundary

```text
accepted clean profile + P1/P2 code
≠ complete Kernel
≠ PostgreSQL integration evidence when tests are skipped
≠ replay/projection runtime
≠ assertion-level conformance
≠ C1/C2/C3
≠ recovered v0.1.2.1
```

P3–P5 require separate operator decisions.

## When an ADR is required

Create or update an ADR when a change affects Canon, cross-technology contracts, identity, event/replay semantics, authority, conflict, deletion, integration boundaries, portability, a major implementation-profile commitment, promotion authority or a previously accepted decision.

Routine refactors, formatting and narrow tests usually do not need a new ADR when they preserve accepted meaning.

## Operational rules

1. Multi-model agreement is input, not approval.
2. Proposed decisions must not be summarized as implemented behavior.
3. `ACCEPTED` does not mean complete runtime.
4. Evidence must link to commands, tests, reports, PRs, commits or Shadow artifacts.
5. Approval and evidence remain separate.
6. Reproducible evidence does not silently promote proposals.
7. Historical reasoning remains after supersession.
8. Issue #1 controlled import remains separate from clean implementation work.
9. Translation must preserve decision/evidence/implementation/approval meaning.
10. Comments should explain why a boundary exists.

## Naming and template

Use the next available four-digit number and never reuse one. Start new records from [`0000-template.md`](./0000-template.md).
