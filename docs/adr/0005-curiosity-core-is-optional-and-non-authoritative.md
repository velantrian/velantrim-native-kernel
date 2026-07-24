# ADR-0005: Curiosity Core is optional and non-authoritative

- **Decision status:** `PROPOSED`
- **Evidence level:** `DOCUMENTED`
- **Implementation status:** `NOT_STARTED`
- **Date:** `2026-07-24`
- **Deciders:** `@velantrian`
- **Track:** `Integration Boundary`
- **Related:** `Issue #1`, `RFC-0001`, `ADR-0001`
- **Tags:** `curiosity, cognition, admission, truthgate, action-gate, titan, crystal`

> [!NOTE]
> This decision exists to prevent an active research module from becoming a hidden second Canon. Curiosity may decide what deserves investigation, but it must not silently decide what is true, rewrite architecture policy, or expand the controlled `v0.1.2.1` import.

## Context 🧭

Native Kernel deliberately remains a small, auditable semantic substrate: Claims, append-only Events, derived epistemic state, rebuildable projections, and Receipts. It does not define a permanent agent, reasoning loop, reward system, graph engine, model provider, or processor substrate.

A higher-level system may still need to:

- notice important uncertainty, contradiction, or missing evidence;
- prioritize a bounded investigation;
- formulate questions and competing hypotheses;
- request tools or human input;
- record capability, tooling, data-quality, or architecture limitations;
- learn from false-positive curiosity triggers.

Putting those behaviours directly into the Kernel would mix durable semantic contracts with replaceable cognitive policy. Allowing them to write directly into Canon would create an invisible second authority.

- **Problem:** define where active curiosity belongs and which authority boundaries it must preserve.
- **Constraints:** deterministic replay, explicit admission, epistemic honesty, bounded resources, optional Titan/Crystal integration, and strict separation from Issue #1.
- **Non-goals:** implementing an autonomous agent, adding curiosity events to `v0.1.2.1`, proving consciousness, selecting a permanent scoring formula, or making Crystal mandatory.
- **Current implementation boundary:** no Curiosity Core runtime or tests exist in `main`.
- **Source-derived facts:** current public status remains `DOCUMENTED_ONLY`; Titan and Crystal integration are inactive; new event verbs require an explicit decision.
- **Open uncertainty:** scoring adapters, event vocabulary, storage profile, evaluation dataset, safety thresholds, and implementation language remain unselected.

## Inputs considered 🔍

```text
Repository evidence:
- README.md and STATUS.md implementation boundary
- docs/INTEGRATION_BOUNDARIES.md
- ADR-0001 architecture/implementation separation
- Issue #1 controlled import constraints

External research:
- information-seeking and active-learning concepts
- event-sourced audit and replay patterns
- bounded agent and tool-gating patterns
- processing-in-memory and neuromorphic systems as future research context only

AI-generated inputs:
- architecture drafts and audits from multiple models
- proposed trigger, scoring, investigation, hypothesis, reflection, and guard mechanisms

Operator interpretation:
- Curiosity Core is useful as a bounded active-understanding layer
- it must remain optional, non-authoritative, and technology-neutral
- decay may change attention but must not silently change truth confidence
```

AI-generated inputs are design inputs, not implementation evidence.

## Decision drivers 🎯

- semantic durability;
- deterministic replay;
- epistemic honesty;
- explicit authority boundaries;
- portability;
- testability;
- security and privacy;
- bounded resource use;
- rollback and disablement;
- compatibility with Titan and Crystal without making either mandatory.

## Considered options 🧪

### Option A — Put Curiosity inside Native Kernel Canon

**Description**

Make trigger, scoring, hypothesis generation, and self-reflection permanent Kernel semantics.

**Advantages**

- one integrated package;
- direct access to Claims and projections;
- fewer visible interfaces.

**Disadvantages**

- binds durable semantics to one cognitive policy;
- risks a hidden second truth authority;
- expands replay and safety complexity;
- makes the Kernel harder to disable, port, and test;
- silently expands Issue #1.

### Option B — Optional non-authoritative module over abstract contracts

**Description**

Define Curiosity Core as a replaceable client of Native Kernel read, admission, Receipt, and promotion contracts. Separate operational Event Admission, Action Gate, and TruthGate responsibilities.

**Advantages**

- preserves a small and portable Kernel;
- allows different Titan and Crystal profiles;
- supports Shadow evaluation and rollback;
- keeps attention separate from validity;
- makes safety and tool permissions explicit.

**Disadvantages**

- more interfaces and governance documents;
- operational events and truth promotion require different gates;
- exact scoring and runtime behaviour remain implementation-profile work.

### Option C — Make Crystal TruthGate mandatory for all curiosity activity

**Description**

Route every curiosity decision, allocation, and record through Crystal.

**Advantages**

- one familiar validation surface;
- strong review boundary for epistemic promotion.

**Disadvantages**

- makes an independent project depend on Crystal;
- confuses operational process records with truth validation;
- prevents use outside Crystal;
- contradicts the current integration boundary.

## Decision ✅

**We will:**

- document Curiosity Core as an optional, replaceable cognitive module;
- treat Titan as the primary future host for a full profile;
- allow Crystal to define a separate restricted `Audit Curiosity` profile;
- keep operational Event Admission, external Action Gate, and epistemic TruthGate as distinct authorities;
- require explicit Receipts for curiosity-driven context influence;
- keep hypotheses, questions, gaps, and System Insights non-canonical until separately evaluated;
- require bounded budgets, stopping conditions, deduplication, cooldown, and disablement;
- require Shadow evaluation before adaptive scoring policies may influence active behaviour;
- keep the entire proposal outside the controlled `v0.1.2.1` import.

**We will not:**

- make curiosity part of the permanent Architecture Canon at this stage;
- allow direct writes to Canon or direct mutation of Epistemic State;
- equate attention, novelty, utility, or repeated use with truth;
- allow System Insights to modify code, policy, or architecture automatically;
- require Crystal for every operational curiosity record;
- claim hardware compatibility, consciousness, autonomous truth, or production readiness;
- add runtime code or new event verbs through documentation alone.

### One-line rationale

> In the context of active machine investigation, facing the risk of a hidden second Canon, we selected an optional non-authoritative module over explicit contracts to preserve epistemic integrity and portability, accepting additional interfaces because authority separation is more important than architectural convenience.

## Consequences 📌

### Positive

- Native Kernel remains small, auditable, and replaceable.
- Curiosity policies can evolve without redefining Claim identity or truth semantics.
- Titan may host broad research while Crystal remains grant-safe and independent.
- The module can be disabled without losing Kernel integrity.
- Safety, action, and truth promotion can be tested independently.

### Negative / accepted trade-offs

- More contracts, receipts, and lifecycle states must be documented.
- A future runtime must coordinate three distinct gateways.
- Deterministic replay of scoring may require frozen snapshots and adapter versions.
- Research value must be demonstrated in Shadow before integration.

### Neutral

- The ADR does not select Python, SQLite, graphs, vectors, an LLM, or a processor model.
- The ADR does not accept any proposed event verb into the current Canon.

## Invariants 🔒

1. Curiosity Core never changes Canon or Epistemic State directly.
2. Every persisted operational record passes explicit Event Admission.
3. Operational curiosity events describe process, not truth.
4. A candidate, gap, question, hypothesis, or System Insight is not established knowledge.
5. Epistemic promotion is a separate TruthGate decision under operator policy.
6. External, sensitive, or irreversible actions require an Action Gate.
7. Attention priority is not epistemic validity.
8. Utility and novelty are not evidence.
9. Curiosity-driven context influence is visible in a Receipt.
10. Replay uses recorded IDs, times, inputs, and policy versions; reducers generate no new randomness.
11. Safety and Resource Guard wraps the complete investigation lifecycle.
12. System Insights cannot apply architecture or policy changes automatically.
13. Temporal decay may change attention or dormancy, but not evidence-derived truth confidence.
14. Curiosity Core can be disabled without damaging Native Kernel integrity.
15. Adaptive policies begin in Shadow and require explicit operator approval.
16. Every investigation has budget, stopping, suspension, and reopen conditions.
17. `UNKNOWN` and `INSUFFICIENT_EVIDENCE` are valid outcomes.
18. Legal deletion, restriction, and privacy requirements remain applicable.
19. The controlled `v0.1.2.1` import remains unchanged.

## Architecture-layer placement

| Question | Answer |
|---|---|
| Architecture Canon changed? | `no` |
| Abstract contract changed? | `proposed extension only` |
| Implementation profile selected? | `no` |
| Runtime code exists? | `no` |
| Production evidence exists? | `no` |

## Implementation notes 🔧

- Primary specification: `docs/rfc/0001-curiosity-core-architecture.md`.
- Candidate ports: Kernel Read, Event Admission, Receipt, Truth Promotion, Action Gate, Clock/ID provider.
- Candidate profiles: Titan Full Curiosity; Crystal Audit Curiosity.
- Any event vocabulary requires its own review before implementation.
- Feature flags and kill switch are mandatory before active integration.
- No migration is required because no runtime data exists.
- Rollback is complete disablement plus removal of disposable projections; authoritative history remains readable.

## Validation and evidence 🧪

| Evidence | Artifact / command | Result | Required for next level |
|---|---|---|---|
| Documentation | RFC-0001 + this ADR | Proposed boundary recorded | Operator review |
| Unit tests | Not present | No implementation claim | Pure trigger/scoring tests |
| Replay test | Not present | No replay claim | Frozen-input replay suite |
| Benchmark | Not present | No performance claim | Bounded synthetic workloads |
| Offline Shadow | Not present | No value claim | Recorded Titan evaluation |
| Operator approval | PR review / merge decision | Pending | Required before `ACCEPTED` |

## Failure cases 🚨

- Curiosity silently changes ranking without a Receipt.
- A hypothesis is promoted because it was useful or novel.
- A System Insight modifies policy automatically.
- The same gap creates unbounded duplicate investigations.
- Replay generates new UUIDs, timestamps, or scores.
- Crystal becomes a mandatory dependency of Native Kernel.
- A tool executes without Action Gate permission.
- Temporal decay silently lowers truth confidence.
- Documentation is reported as implemented runtime.
- Issue #1 scope is expanded by adding curiosity code or verbs.

## Rollback / supersession

- The module can be disabled entirely because it is not required for Kernel replay or state reconstruction.
- Disposable curiosity projections may be deleted and rebuilt.
- Historical operational records remain readable under their schema versions.
- A future ADR may accept a narrower contract, supersede the three-gate model, or reject Curiosity Core if Shadow evaluation shows insufficient value or unacceptable complexity.

## Consistency checklist 🔱

- [x] Event history remains authoritative about recorded changes.
- [x] History is not equated with truth.
- [x] Projection/cache is not promoted to Canon.
- [x] Relevance/utility is not equated with truth.
- [x] Candidate conflict is not described as resolved conflict.
- [x] Current technology is not silently promoted to permanent architecture.
- [x] Titan and Crystal boundaries remain explicit.
- [x] Issue #1 import scope is not silently expanded.
- [x] Decision status, evidence level, and implementation status remain separate.

## References 📚

- [`../../README.md`](../../README.md)
- [`../../STATUS.md`](../../STATUS.md)
- [`../INTEGRATION_BOUNDARIES.md`](../INTEGRATION_BOUNDARIES.md)
- [`./0001-architecture-canon-vs-implementation-profiles.md`](./0001-architecture-canon-vs-implementation-profiles.md)
- [`../../ROADMAP.md`](../../ROADMAP.md)
- [`../../prototype/README.md`](../../prototype/README.md)
- [`../rfc/0001-curiosity-core-architecture.md`](../rfc/0001-curiosity-core-architecture.md)
