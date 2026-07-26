# 📝 Architecture Decision Process

> **Status:** `DOCUMENTED GOVERNANCE PROCESS`  
> **Purpose:** preserve why important decisions were made and prevent AI discussions, implementation details, empirical evidence, and architectural Canon from being silently merged

## 1. Why this document exists

Native Kernel is a long-horizon research project. Its architecture will be discussed across code reviews, experiments, external research, and multiple AI systems.

Without a durable decision process, the project risks confusing:

```text
interesting idea
with
accepted architecture

working local code
with
publicly reproduced evidence

reproducible behaviour
with
operator authorization

several AI opinions
with
operator approval
```

Architecture Decision Records — ADRs — preserve the question, alternatives, decision, evidence, consequences, and conditions under which the decision should be reconsidered.

> [!NOTE]
> An ADR is not decorative documentation. It is the project's memory of why a boundary exists.

## 2. Four independent governance dimensions

Every important proposal has four independent dimensions:

```text
Decision status
≠ Evidence level
≠ Implementation status
≠ Operator approval
```

This separation is accepted in ADR-0007.

### Decision status

```text
PROPOSED
ACCEPTED
REJECTED
DEPRECATED
SUPERSEDED
```

Decision status answers: **what architectural or governance decision has been made?**

### Evidence level

```text
DOCUMENTED
EXTERNALLY_OBSERVED
LOCALLY_TESTED
REPOSITORY_REPRODUCED
SHADOW_EVALUATED
OPERATIONALLY_VALIDATED
```

Evidence level answers: **what empirical, reproducible, or operational support exists?**

`OPERATOR_APPROVED` is not an evidence level.

### Implementation status

```text
NOT_STARTED
PARTIAL
COMPLETE
REMOVED
```

Implementation status answers: **what mechanism exists in the declared scope?**

### Operator approval

```text
NOT_REQUESTED
PENDING
APPROVED
WITHDRAWN
```

Operator approval answers: **has the authorized operator accepted the decision or promotion?**

These dimensions must not be collapsed.

Example:

```yaml
decision_status: ACCEPTED
evidence_level: DOCUMENTED
implementation_status: NOT_STARTED
operator_approval: APPROVED
```

This means the architectural decision is approved and documented, but no implementation or runtime proof is claimed.

Another valid state:

```yaml
decision_status: PROPOSED
evidence_level: REPOSITORY_REPRODUCED
implementation_status: PARTIAL
operator_approval: PENDING
```

This means a bounded mechanism exists and is reproducible, but it has not been accepted as architecture or approved for promotion.

## 3. When an ADR is required

Create or update an ADR when a change:

- changes Architecture Canon or a core invariant;
- defines a new abstract contract;
- selects a long-lived implementation-profile boundary;
- adds an event verb or changes event meaning;
- changes Claim identity, canonical encoding, or migration semantics;
- changes conflict, temporal, admission, deletion, or Receipt semantics;
- changes replay, ordering, idempotency, or authoritative-history semantics;
- introduces a dependency between Native Kernel, Titan, or Crystal;
- changes the meaning of a public maturity or implementation claim;
- changes governance dimensions or promotion authority;
- accepts a significant security, privacy, replay, erasure, or migration trade-off.

An ADR is usually unnecessary for:

- typo fixes;
- formatting;
- comments that do not change meaning;
- local refactoring that preserves contracts;
- disposable benchmark scripts;
- experimental code clearly isolated from Canon;
- byte-faithful execution of an already approved import gate.

A controlled import stops being ADR-free if it changes semantics, identity, event vocabulary, public contract meaning, or long-lived profile boundaries.

## 4. Decision workflow

```text
question
   ↓
source and repository verification
   ↓
options and trade-offs
   ↓
small experiment where possible
   ↓
ADR: PROPOSED
   ↓
operator decision
   ↓
ADR: ACCEPTED or REJECTED
   ↓
implementation in separate scope
   ↓
reproducible evidence
   ↓
separate promotion decision where applicable
   ↓
review / supersession when needed
```

The operator/maintainer remains the final architecture authority.

AI systems may:

- identify options;
- challenge assumptions;
- summarize research;
- draft ADRs;
- review consistency;
- propose tests;
- report evidence and uncertainty.

AI systems may not independently:

- promote a proposal to Canon;
- claim implementation without repository evidence;
- treat reproducibility as automatic approval;
- merge Titan or Crystal semantics into Native Kernel;
- treat multi-model agreement as verification;
- silently change maturity labels;
- upgrade evidence because a document is detailed or persuasive.

## 5. Recording evidence and external AI opinions

AI opinions may be included under an `Inputs considered` section. They are inputs, not evidence and not approval.

Recommended form:

```text
Question:
Should Native Kernel include Titan CausalGraph semantics?

Inputs considered:
- Model A proposed direct inclusion.
- Model B warned about scope expansion.
- Repository review found Titan-specific ontology outside Kernel Canon.

Evidence:
- linked contracts, tests, experiments, or repository state.

Operator decision:
Do not include Titan CausalGraph as Kernel Canon.
Define a technology-neutral relation contract and evaluate adapters separately.

Validation:
A second graph implementation should preserve the declared contract without changing Claim/Event identity.
```

> [!IMPORTANT]
> Model names, confident wording, and consensus are not evidence. Repository state, tests, experiments, reviewable artifacts, and explicit operator decisions must be recorded in their correct independent dimensions.

## 6. Evidence promotion discipline

Evidence transitions require concrete artifacts.

| Evidence level | Minimum expected support |
|---|---|
| `DOCUMENTED` | explicit reasoning and declared limits |
| `EXTERNALLY_OBSERVED` | identifiable external report or artifact |
| `LOCALLY_TESTED` | recorded local command, environment, and result |
| `REPOSITORY_REPRODUCED` | committed code, tests, environment, and reviewable command |
| `SHADOW_EVALUATED` | bounded dataset, metrics, Receipts, failures, and report |
| `OPERATIONALLY_VALIDATED` | security, rollback, observability, incident, privacy, and operational evidence |

Evidence levels do not imply decision status, implementation completeness, or operator approval.

## 7. Repository layout

```text
docs/adr/
├── README.md
├── 0000-template.md
├── 0001-architecture-canon-vs-implementation-profiles.md
├── ...
└── 0007-operator-approval-is-not-evidence.md
```

The ADR index should show:

- number and title;
- decision status;
- evidence level;
- implementation status;
- operator approval;
- superseding ADR where applicable.

## 8. Review comments for humans and AI

Important architecture documents should include short explanatory callouts where a reader may otherwise misinterpret the boundary.

Use comments such as:

> [!NOTE]
> This is an abstract contract. The SQLite profile is one implementation, not the definition of the contract.

> [!WARNING]
> This section describes future research. It does not claim the mechanism exists in `main`.

> [!IMPORTANT]
> This decision preserves separation between Native Kernel, Titan, and Crystal.

Comments should explain **why** a boundary exists, not merely repeat the rule.

## 9. Superseding decisions

Architecture can evolve.

When a decision changes:

1. do not rewrite history as if the old decision never existed;
2. mark the old ADR `SUPERSEDED`;
3. link to the new ADR;
4. explain what evidence or changed constraint caused the revision;
5. document migration and compatibility consequences;
6. record whether operator approval was withdrawn or replaced.

This mirrors the Kernel principle that explicit history is more trustworthy than silent overwrite.
