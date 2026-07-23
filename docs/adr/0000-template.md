# ADR-XXXX: Short decision title

- **Decision status:** `PROPOSED | ACCEPTED | REJECTED | DEPRECATED | SUPERSEDED`
- **Evidence level:** `DOCUMENTED | EXTERNALLY_OBSERVED | LOCALLY_TESTED | REPOSITORY_REPRODUCED | SHADOW_EVALUATED | OPERATOR_APPROVED`
- **Implementation status:** `NOT_STARTED | PARTIAL | COMPLETE`
- **Date:** `YYYY-MM-DD`
- **Deciders:** `@maintainer`
- **Track:** `Architecture Canon | Abstract Contract | Implementation Profile | Evaluation | Integration Boundary`
- **Related:** `Issue #… | PR #… | ADR-… | commit SHA`
- **Tags:** `tag-one, tag-two`

## Context 🧭

Describe the actual problem, constraints, current evidence, and why a durable decision is needed.

- **Problem:**
- **Constraints:**
- **Non-goals:**
- **Current implementation boundary:**
- **Source-derived facts:**
- **Open uncertainty:**

## Decision drivers 🎯

- semantic durability;
- deterministic replay;
- epistemic honesty;
- conflict visibility;
- portability;
- testability;
- security/privacy;
- complexity budget;
- rollback and migration.

Remove drivers that do not apply and add missing ones.

## Considered options 🧪

### Option A — Name

**Description**

...

**Advantages**

- ...

**Disadvantages**

- ...

### Option B — Name

**Description**

...

**Advantages**

- ...

**Disadvantages**

- ...

## Decision ✅

**We will:**

...

**We will not:**

...

### One-line rationale

> In the context of `<use case>`, facing `<concern>`, we selected `<option>` to achieve `<quality>`, accepting `<trade-off>`, because `<reason>`.

## Consequences 📌

### Positive

- ...

### Negative / accepted trade-offs

- ...

### Neutral

- ...

## Invariants 🔒

1. ...
2. ...
3. ...

## Architecture-layer placement

| Question | Answer |
|---|---|
| Architecture Canon changed? | `yes / no` |
| Abstract contract changed? | `yes / no` |
| Implementation profile selected? | `yes / no` |
| Runtime code exists? | `yes / no` |
| Production evidence exists? | `yes / no` |

## Implementation notes 🔧

- affected paths;
- schema/events;
- feature flags;
- migration/upcast;
- compatibility;
- rollback;
- Titan/Crystal boundary impact.

## Validation and evidence 🧪

| Evidence | Artifact / command | Result | Required for next level |
|---|---|---|---|
| Documentation | link | ... | ... |
| Unit tests | command | ... | ... |
| Replay test | command | ... | ... |
| Benchmark | report | ... | ... |
| Offline Shadow | artifact | ... | ... |
| Operator approval | decision link | ... | ... |

## Failure cases 🚨

- ...

## Rollback / supersession

- How can this decision be disabled, reverted, or superseded?
- Which data or history must remain readable?

## Consistency checklist 🔱

- [ ] Event history remains authoritative about recorded changes.
- [ ] History is not equated with truth.
- [ ] Projection/cache is not promoted to Canon.
- [ ] Relevance/utility is not equated with truth.
- [ ] Candidate conflict is not described as resolved conflict.
- [ ] Current technology is not silently promoted to permanent architecture.
- [ ] Titan and Crystal boundaries remain explicit.
- [ ] Issue #1 import scope is not silently expanded.
- [ ] Decision status, evidence level, and implementation status remain separate.

## References 📚

List sources as inputs. A citation alone is not proof that the decision applies to Native Kernel.
