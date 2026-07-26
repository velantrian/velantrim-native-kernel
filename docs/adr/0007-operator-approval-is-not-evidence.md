# ADR-0007: Operator approval is separate from empirical evidence

> **Decision status:** `ACCEPTED`  
> **Evidence level:** `DOCUMENTED`  
> **Implementation status:** `COMPLETE FOR GOVERNANCE DOCUMENTATION`  
> **Operator approval:** `APPROVED`  
> **Date:** 2026-07-26

## Context

The original governance taxonomy described three dimensions:

```text
decision status
evidence level
implementation status
```

It also placed `OPERATOR_APPROVED` inside the evidence-level sequence.

That placement conflates two different questions:

```text
What empirical or reproducible support exists?
≠
Has the authorized operator accepted a decision or promotion?
```

An operator may approve a documented architecture proposal with no runtime implementation. Conversely, repository tests may reproduce behaviour that the operator has not accepted for promotion, integration, or Canon status.

Collapsing approval into evidence makes it possible to misread authorization as empirical proof or to treat empirical reproduction as automatic authorization.

## Decision

Native Kernel governance uses four independent dimensions:

```text
Decision status
≠ Evidence level
≠ Implementation status
≠ Operator approval
```

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
OPERATIONALLY_VALIDATED
```

### Implementation status

```text
NOT_STARTED
PARTIAL
COMPLETE
REMOVED
```

### Operator approval

```text
NOT_REQUESTED
PENDING
APPROVED
WITHDRAWN
```

The dimensions may progress independently. Every public status record must avoid implying transitions in one dimension from changes in another.

Example:

```yaml
decision_status: ACCEPTED
evidence_level: DOCUMENTED
implementation_status: NOT_STARTED
operator_approval: APPROVED
```

This means the architecture decision is approved and documented, but no runtime implementation or empirical reproduction is claimed.

Another example:

```yaml
decision_status: PROPOSED
evidence_level: REPOSITORY_REPRODUCED
implementation_status: PARTIAL
operator_approval: PENDING
```

This means a bounded mechanism exists and is reproducible, but it has not been accepted as architecture or approved for promotion.

## Consequences

### Positive

- authorization cannot be mistaken for empirical proof;
- reproducible code cannot silently become accepted architecture;
- AI or reviewer consensus cannot substitute for operator approval;
- evidence gates remain independently auditable;
- maturity and promotion records become less ambiguous.

### Costs

- ADR indexes and status summaries require one additional column or field;
- older documents containing `DOCUMENTED + OPERATOR_APPROVED` must be interpreted as two dimensions and updated when touched;
- tooling must preserve the distinction.

## Compatibility

This ADR does not revoke previous operator decisions. Existing records such as:

```text
Evidence: DOCUMENTED + OPERATOR_APPROVED
```

are migrated semantically to:

```yaml
evidence_level: DOCUMENTED
operator_approval: APPROVED
```

No runtime, Canon, event, Claim, replay, or integration semantics are changed.

## Non-goals

This ADR does not:

- define who may become an operator;
- implement cryptographic approval signatures;
- establish a production change-management system;
- upgrade any proposal or implementation evidence.

## Validation

The governance documents and ADR index must expose all four dimensions. New ADRs should use the separate `Operator approval` field.
