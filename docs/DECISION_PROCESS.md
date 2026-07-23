# 📝 Architecture Decision Process

> **Status:** `DOCUMENTED GOVERNANCE PROCESS`  
> **Purpose:** preserve why important decisions were made and prevent AI discussions, implementation details, and architectural Canon from being silently merged

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

several AI opinions
with
operator approval
```

Architecture Decision Records — ADRs — preserve the question, alternatives, decision, evidence, consequences, and conditions under which the decision should be reconsidered.

> [!NOTE]
> An ADR is not decorative documentation. It is the project's memory of why a boundary exists.

---

## 2. Separate three dimensions

Every important proposal has three independent dimensions.

### Decision status

```text
PROPOSED
ACCEPTED
REJECTED
DEPRECATED
SUPERSEDED
```

### Evidence level

```text
DOCUMENTED
EXTERNALLY_OBSERVED
LOCALLY_TESTED
REPOSITORY_REPRODUCED
SHADOW_EVALUATED
OPERATOR_APPROVED
```

### Implementation status

```text
NOT_STARTED
PARTIAL
COMPLETE
REMOVED
```

These dimensions must not be collapsed.

Example:

```yaml
status: ACCEPTED
evidence_level: DOCUMENTED
implementation_status: NOT_STARTED
```

This means the architectural decision is accepted, but no implementation claim is being made.

---

## 3. When an ADR is required

Create or update an ADR when a change:

- changes Architecture Canon or a core invariant;
- defines a new abstract contract;
- selects a long-lived implementation-profile boundary;
- adds an event verb or changes event meaning;
- changes conflict, temporal, admission, deletion, or Receipt semantics;
- introduces a dependency between Native Kernel, Titan, or Crystal;
- changes the meaning of a public maturity or implementation claim;
- accepts a significant security, privacy, replay, or migration trade-off.

An ADR is usually unnecessary for:

- typo fixes;
- formatting;
- comments that do not change meaning;
- local refactoring that preserves contracts;
- disposable benchmark scripts;
- experimental code clearly isolated from Canon.

---

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
review / supersession when needed
```

The operator/maintainer remains the final architecture authority.

AI systems may:

- identify options;
- challenge assumptions;
- summarize research;
- draft ADRs;
- review consistency;
- propose tests.

AI systems may not independently:

- promote a proposal to Canon;
- claim implementation without repository evidence;
- merge Titan or Crystal semantics into Native Kernel;
- treat multi-model agreement as verification;
- silently change maturity labels.

---

## 5. Recording external AI opinions

AI opinions may be included under an `Inputs considered` section.

Recommended form:

```text
Question:
Should Native Kernel include Titan CausalGraph semantics?

Inputs considered:
- Model A proposed direct inclusion.
- Model B warned about scope expansion.
- Repository review found Titan-specific ontology outside Kernel Canon.

Operator decision:
Do not include Titan CausalGraph as Kernel Canon.
Define a technology-neutral relation contract and evaluate adapters separately.

Validation:
A second graph implementation should preserve the declared contract without changing Claim/Event identity.
```

> [!IMPORTANT]
> Model names and confident wording are not evidence. Repository state, tests, experiments, and explicit operator decisions are evidence-bearing artifacts.

---

## 6. Repository layout

```text
docs/adr/
├── README.md
├── 0000-template.md
├── 0001-separate-architecture-from-implementation.md
└── future decisions...
```

The ADR index should show:

- number and title;
- decision status;
- evidence level;
- implementation status;
- superseding ADR where applicable.

---

## 7. Review comments for humans and AI

Important architecture documents should include short explanatory callouts where a reader may otherwise misinterpret the boundary.

Use comments such as:

> [!NOTE]
> This is an abstract contract. The SQLite profile is one implementation, not the definition of the contract.

> [!WARNING]
> This section describes future research. It does not claim the mechanism exists in `main`.

> [!IMPORTANT]
> This decision preserves separation between Native Kernel, Titan, and Crystal.

Comments should explain **why** a boundary exists, not merely repeat the rule.

---

## 8. Superseding decisions

Architecture can evolve.

When a decision changes:

1. do not rewrite history as if the old decision never existed;
2. mark the old ADR `SUPERSEDED`;
3. link to the new ADR;
4. explain what evidence or changed constraint caused the revision;
5. document migration and compatibility consequences.

This mirrors the Kernel principle that explicit history is more trustworthy than silent overwrite.
