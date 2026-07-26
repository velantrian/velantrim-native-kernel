# 📝 Architecture Decision Records

[← Project README](../../README.md) · [Русский README](../../README.ru.md) · [Decision process](../DECISION_PROCESS.md) · [Research RFCs](../rfc/README.md)

Architecture Decision Records preserve **why** a durable architectural choice was made.

They do not turn a proposal into implementation evidence, and operator approval does not substitute for empirical evidence.

> [!NOTE]
> An ADR is the project's memory of a decision. It should explain why a boundary exists so that a future maintainer, reviewer, or AI does not remove it as apparent complexity.

## Four independent dimensions

```text
Decision status
≠ Evidence level
≠ Implementation status
≠ Operator approval
```

See [`ADR-0007`](./0007-operator-approval-is-not-evidence.md).

### Decision status

| Status | Meaning |
|---|---|
| `PROPOSED` | Under consideration; not accepted architecture |
| `ACCEPTED` | Explicitly accepted architectural decision |
| `REJECTED` | Considered and deliberately not adopted |
| `DEPRECATED` | Still present but no longer preferred |
| `SUPERSEDED` | Replaced by another ADR |

### Evidence level

| Level | Meaning |
|---|---|
| `DOCUMENTED` | Reasoning is recorded; no runtime proof implied |
| `EXTERNALLY_OBSERVED` | Identifiable evidence exists outside the repository |
| `LOCALLY_TESTED` | Tested in a recorded local environment |
| `REPOSITORY_REPRODUCED` | Reproduced from committed code and repository commands |
| `SHADOW_EVALUATED` | Evaluated in a bounded Shadow experiment |
| `OPERATIONALLY_VALIDATED` | Security, rollback, observability, privacy, and incident evidence exists for a bounded deployment |

### Implementation status

| Status | Meaning |
|---|---|
| `NOT_STARTED` | No implementation claim |
| `PARTIAL` | Some mechanism exists but the full contract is incomplete |
| `COMPLETE` | Implementation satisfies the ADR's declared acceptance criteria |
| `REMOVED` | A former implementation is no longer present; historical reasoning remains |

### Operator approval

| Status | Meaning |
|---|---|
| `NOT_REQUESTED` | No approval decision has been requested |
| `PENDING` | Awaiting an operator decision |
| `APPROVED` | The authorized operator accepted the decision or promotion |
| `WITHDRAWN` | A prior approval was explicitly withdrawn or superseded |

Approval and evidence must remain separate. A decision may be approved with only documented reasoning, and a reproducible experiment may remain unapproved for architectural promotion.

## Index

| ADR | Title | Decision | Evidence | Implementation | Operator approval |
|---|---|---|---|---|---|
| [`0001`](./0001-architecture-canon-vs-implementation-profiles.md) | Architecture Canon is separate from Implementation Profiles | `ACCEPTED` | `DOCUMENTED` | Documentation complete; runtime portability unproven | `APPROVED` |
| [`0002`](./0002-state-checkpoints-are-disposable.md) | State Checkpoints are disposable replay accelerators | `PROPOSED` | `DOCUMENTED` | `NOT_STARTED` | `NOT_REQUESTED` |
| [`0003`](./0003-semantic-conflicts-require-explicit-resolution.md) | Semantic conflicts require explicit resolution | `PROPOSED` | `DOCUMENTED` | `NOT_STARTED` | `NOT_REQUESTED` |
| [`0004`](./0004-rebuild-from-authoritative-history.md) | Rebuild from authoritative history is the first conformance experiment | `PROPOSED` | `DOCUMENTED` | `NOT_STARTED` | `NOT_REQUESTED` |
| [`0005`](./0005-curiosity-core-is-optional-and-non-authoritative.md) | Curiosity Core is optional and non-authoritative | `PROPOSED` | `DOCUMENTED` | `NOT_STARTED` | `NOT_REQUESTED` |
| [`0006`](./0006-causal-links-are-relations.md) | Causal links are relations, not knowledge types | `ACCEPTED` | `DOCUMENTED` | `NOT_STARTED` | `APPROVED` |
| [`0007`](./0007-operator-approval-is-not-evidence.md) | Operator approval is separate from empirical evidence | `ACCEPTED` | `DOCUMENTED` | Governance documentation complete | `APPROVED` |
| [`0008`](./0008-epistemic-boundaries-are-representation-disciplines.md) | Epistemic boundaries are representation disciplines, not a fixed worldview | `PROPOSED` | `DOCUMENTED` | `NOT_STARTED` | `PENDING` |

## When an ADR is required

Create or update an ADR when a change affects:

- Architecture Canon;
- an abstract cross-technology contract;
- Claim identity or canonical encoding;
- event vocabulary, ordering, idempotency, or replay semantics;
- admission or epistemic policy;
- conflict lifecycle;
- checkpoint or snapshot semantics;
- deletion, restriction, retention, or erasure semantics;
- Titan or Crystal boundaries;
- portability or migration guarantees;
- a major implementation-profile commitment;
- governance dimensions or promotion authority;
- a previously accepted decision.

An ADR is usually unnecessary for formatting, typo fixes, local refactors that preserve contracts, routine test additions, or a byte-faithful import that only executes an already accepted gate.

## Operational rules

1. Multi-model agreement is input, not approval.
2. `PROPOSED` ADRs must not be summarized as implemented behaviour.
3. `ACCEPTED` means the architecture decision is accepted; it does not automatically mean runtime code exists.
4. Evidence must link to concrete commands, tests, reports, PRs, commits, or Shadow artifacts.
5. Operator approval must be recorded separately from evidence.
6. Reproducible evidence does not silently promote a proposal to Canon.
7. An accepted decision may be superseded, but historical reasoning remains visible.
8. Issue #1 controlled import remains separate from ADR-driven redesign.
9. Translation must preserve decision, evidence, implementation, and approval meaning.
10. Explanatory comments should state **why** a boundary exists, not merely repeat the boundary.

## Naming

```text
0000-template.md
0001-short-decision-title.md
0002-next-decision.md
```

Use the next available four-digit number. Never reuse a number.

## Template

Use [`0000-template.md`](./0000-template.md). New ADRs should include separate fields for Decision status, Evidence level, Implementation status, and Operator approval.
