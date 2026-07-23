# 📝 Architecture Decision Records

[← Project README](../../README.md) · [Русский README](../../README.ru.md)

Architecture Decision Records preserve **why** a durable architectural choice was made.

They do not turn a proposal into implementation evidence.

## Three independent dimensions

```text
Decision status
≠ Evidence level
≠ Implementation status
```

### Decision status

| Status | Meaning |
|---|---|
| `PROPOSED` | Under consideration; not accepted architecture |
| `ACCEPTED` | Explicitly approved architectural decision |
| `REJECTED` | Considered and deliberately not adopted |
| `DEPRECATED` | Still present but no longer preferred |
| `SUPERSEDED` | Replaced by another ADR |

### Evidence level

| Level | Meaning |
|---|---|
| `DOCUMENTED` | Reasoning is recorded; no runtime proof implied |
| `EXTERNALLY_OBSERVED` | Evidence exists outside the repository |
| `LOCALLY_TESTED` | Tested in a local environment |
| `REPOSITORY_REPRODUCED` | Reproduced from committed code and repository commands |
| `SHADOW_EVALUATED` | Evaluated in a bounded Shadow experiment |
| `OPERATOR_APPROVED` | Explicit operator or maintainer decision recorded |

### Implementation status

| Status | Meaning |
|---|---|
| `NOT_STARTED` | No implementation claim |
| `PARTIAL` | Some mechanism exists but the full contract is incomplete |
| `COMPLETE` | Implementation satisfies the ADR's declared acceptance criteria |

## Index

| ADR | Title | Decision | Evidence | Implementation |
|---|---|---|---|---|
| [`0001`](./0001-architecture-canon-vs-implementation-profiles.md) | Architecture Canon is separate from Implementation Profiles | `ACCEPTED` | `DOCUMENTED` + `OPERATOR_APPROVED` | Documentation complete; runtime portability unproven |
| [`0002`](./0002-state-checkpoints-are-disposable.md) | State Checkpoints are disposable replay accelerators | `PROPOSED` | `DOCUMENTED` | `NOT_STARTED` |
| [`0003`](./0003-semantic-conflicts-require-explicit-resolution.md) | Semantic conflicts require explicit resolution | `PROPOSED` | `DOCUMENTED` | `NOT_STARTED` |

## When an ADR is required

Create or update an ADR when a change affects:

- Architecture Canon;
- an abstract cross-technology contract;
- event vocabulary or replay semantics;
- admission or epistemic policy;
- conflict lifecycle;
- checkpoint or snapshot semantics;
- Titan or Crystal boundaries;
- portability or migration guarantees;
- a major implementation-profile commitment;
- a previously accepted decision.

An ADR is usually unnecessary for formatting, typo fixes, local refactors that preserve contracts, or routine test additions.

## Operational rules

1. Multi-model agreement is input, not approval.
2. `PROPOSED` ADRs must not be summarized as implemented behaviour.
3. `ACCEPTED` means the architecture decision is approved; it does not automatically mean runtime code exists.
4. Evidence must link to concrete commands, tests, reports, PRs, commits, or Shadow artifacts.
5. An accepted decision may be superseded, but historical reasoning remains visible.
6. Issue #1 controlled import remains separate from ADR-driven redesign.
7. Translation must preserve status and evidence meaning.

## Naming

```text
0000-template.md
0001-short-decision-title.md
0002-next-decision.md
```

Use the next available four-digit number. Never reuse a number.

## Template

Use [`0000-template.md`](./0000-template.md).
