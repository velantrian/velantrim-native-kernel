# RFC-0001: Curiosity Core Architecture

- **Status:** `PROPOSED / DOCUMENTED_ONLY`
- **Version:** `RFC-0.1`
- **Date:** `2026-07-24`
- **Primary host:** `Titan research runtime`
- **Restricted profile:** `Crystal Audit Curiosity`
- **Native Kernel relationship:** `optional client of abstract contracts`
- **Direct Canon write:** `forbidden`
- **Runtime implementation:** `not present`
- **Production readiness:** `not claimed`
- **Controlled v0.1.2.1 import:** `out of scope`
- **Boundary ADR:** [`ADR-0005`](../adr/0005-curiosity-core-is-optional-and-non-authoritative.md)

> [!IMPORTANT]
> Curiosity Core is an active investigation policy, not a truth authority. It decides which unknowns deserve bounded attention. It does not decide what becomes Canon.

## 1. Purpose

Curiosity Core is a replaceable metacognitive module that detects meaningful unknowns, evaluates whether they deserve investigation, allocates bounded attention, formulates questions and competing hypotheses, requests evidence or tools through explicit gates, and records testable limitations of the system.

Its functional objective is:

> Detect an important gap between current epistemic state and required understanding, then organize a safe, auditable, and bounded attempt to reduce that gap.

It does not implement a biological reward system, claim emotion, or prove consciousness. Phrases such as “wants to understand” are explanatory metaphors only.

## 2. Why it is separate from Native Kernel

Native Kernel preserves durable meaning through:

- immutable semantic Claims;
- append-only Event History;
- deterministic state reconstruction;
- rebuildable projections;
- provenance and lineage;
- temporal and conflict semantics;
- task-specific context selection;
- auditable Receipts.

The Kernel intentionally does not define a permanent agent loop, curiosity score, graph traversal strategy, LLM, tool runtime, or processor activation model.

Curiosity Core closes the gap between passive memory and active investigation:

```text
memory
  ↓
attention
  ↓
question
  ↓
investigation
  ↓
hypothesis set
  ↓
evidence and validation
  ↓
epistemic promotion or explicit unknown
```

The module remains optional so that changing a curiosity policy never requires rewriting Claim identity, authoritative history, or truth semantics.

## 3. Architectural formula

```text
Native Kernel
→ preserves meaning and recorded history.

Curiosity Core
→ decides which unknown deserves investigation.

Investigation Runtime
→ performs bounded analysis and evidence collection.

Action Gate
→ controls tools and external or irreversible actions.

TruthGate
→ controls epistemic promotion and rejection.

Operator / Maintainer
→ approves architecture and policy changes.
```

## 4. System placement

```text
┌──────────────────────────────────────────────────────────┐
│ 🧠 TITAN COGNITIVE RUNTIME                              │
│ Goals · SituationModel · Working Notebook · Tools        │
│ WhyEngine · Causal Context · RouteMemoryGate             │
└────────────────────────┬─────────────────────────────────┘
                         │ context / goals / constraints
                         ▼
┌──────────────────────────────────────────────────────────┐
│ 🔍 CURIOSITY CORE                                      │
│ 🛡 Guard Wrapper                                       │
│ Trigger · Evaluation · Allocation · Planning             │
│ Investigation · Hypothesis Sets · System Insights        │
│ Calibration · Stopping / Suspension                      │
└────────────┬────────────────────┬────────────────────────┘
             │                    │
             ▼                    ▼
      🧾 Event Admission     🛡 Action Gate
      operational records    tools / external actions
             │                    │
             ▼                    ▼
┌──────────────────────────────────────────────────────────┐
│ 🔱 VELANTRIM NATIVE KERNEL                             │
│ Claims · Events · Receipts · Replay · Projections        │
│ Questions · Candidates · Evidence · Experimental records │
└────────────────────────┬─────────────────────────────────┘
                         │ promotion request
                         ▼
┌──────────────────────────────────────────────────────────┐
│ 💎 TRUTHGATE                                             │
│ Evidence · Provenance · Conflict · Policy · Review       │
└────────────────────────┬─────────────────────────────────┘
                         ▼
                 ⚖️ Epistemic State
```

## 5. Three authority gates

Curiosity Core must not use one universal gate for every operation.

### 5.1 Event Admission

Event Admission controls whether an operational process record may be appended.

Examples:

- candidate detected;
- trigger evaluated;
- budget reserved;
- question raised;
- investigation suspended;
- capability gap detected;
- cycle completed.

These records describe process. They do not establish truth.

Admission checks may include:

- event and payload schema;
- actor and permission;
- idempotency key;
- expected stream version;
- size and retention policy;
- Receipt requirements;
- privacy classification;
- supported event type.

### 5.2 TruthGate

TruthGate is required when a result may change epistemic status.

```text
hypothesis
→ evidence attached
→ validation requested
→ TruthGate evaluation
→ supported / rejected / unresolved
```

TruthGate is not required for every temporary ranking or attention allocation.

### 5.3 Action Gate

Action Gate controls capability use beyond read-only analysis.

It applies to:

- web or external-source access;
- code execution;
- file and repository changes;
- external APIs;
- communications;
- sensitive data;
- financial, legal, physical, or irreversible actions.

Possible decisions:

```text
ALLOW
ALLOW_WITH_LIMITS
ANALYSE_ONLY
SANDBOX_REQUIRED
REDACT_REQUIRED
HUMAN_APPROVAL_REQUIRED
DENY
HALT
```

## 6. Safety and Resource Guard

The Guard is a wrapper around the entire lifecycle, not a final filter.

```text
Guard(
  Trigger → Evaluation → Allocation → Investigation
  → Hypotheses → System Insights → Calibration
)
```

### 6.1 Mandatory quotas

A ResourceBudget may limit:

- wall-clock duration;
- compute units;
- model tokens;
- tool calls;
- graph or projection expansion;
- causal depth;
- active context size;
- number of questions;
- number of hypotheses;
- number of System Insights;
- retries and context switches;
- human-attention requests.

### 6.2 Circuit breaker

The cycle halts or suspends when:

- any hard quota is exhausted;
- the same question repeats without progress;
- hypothesis count grows without discriminating evidence;
- recursive investigation becomes unbounded;
- tools return cyclic failures;
- an action violates policy;
- an input appears adversarial or designed to consume resources;
- the module attempts to modify Guard policy;
- a Native Kernel invariant is threatened.

### 6.3 Capability-aware safety

A topic is not automatically forbidden merely because it is sensitive. The allowed capability is scoped.

```text
analyse a security-policy failure       → may be allowed
propose a reviewed correction           → may be allowed
silently disable the security policy    → denied
retrieve protected secrets              → denied
apply a patch without approval          → approval or deny
```

### 6.4 Meta-reflection bound

For the first implementation profile:

> A SystemInsight cannot directly trigger another SystemInsight.

Bounded meta-curiosity may be considered later under a separate policy and depth limit.

## 7. Trigger Layer

Trigger Layer is a cheap and conservative screening stage. It answers:

> Should an investigation candidate be created?

### 7.1 Hard triggers

Hard triggers create a high-priority candidate:

- architecture invariant violation;
- critical epistemic conflict;
- impossible derived state;
- severe loss of confidence in a previously high-confidence Claim;
- broken provenance or replay;
- critical evidence inconsistency;
- security incident;
- imminent irreversible action under uncertainty;
- semantic divergence across implementations of the same contract.

### 7.2 Soft triggers

Soft triggers create a normal candidate for evaluation:

- uncertainty;
- missing evidence;
- possible causal or temporal gap;
- unresolved contradiction;
- undefined concept;
- repeated failure;
- newly observed pattern;
- changing environment;
- new operator question;
- mismatch with an active goal.

### 7.3 Gap taxonomy

```text
SCHEMA_GAP
CAUSAL_GAP
EVIDENCE_GAP
CONFLICT_GAP
TEMPORAL_GAP
DEFINITION_GAP
CAPABILITY_GAP
TOOLING_GAP
GOAL_PATH_GAP
DATA_QUALITY_GAP
IMPLEMENTATION_GAP
```

A missing edge or node is only a candidate gap. It is not proof that a hidden Claim exists.

### 7.4 Contextual importance

Importance is not an intrinsic property of a stimulus.

```text
ContextualImportance = f(
  stimulus,
  active goal,
  SituationModel,
  consequences,
  constraints,
  time sensitivity,
  affected invariants
)
```

A weather observation may be irrelevant to an architecture audit and critical to an autonomous robot or equipment-safety task.

## 8. Evaluation Layer

Evaluation estimates research priority. It does not estimate truth directly.

### 8.1 Positive factors

#### Epistemic Need

Signals may include:

- low or uncalibrated confidence;
- unresolved conflict;
- weak provenance;
- absent or insufficient evidence;
- unclear scope or applicability;
- uncertain temporal validity;
- incomplete causal structure.

#### Expected Information Value

This is an implementation-neutral research-value concept. Early profiles should use explicit heuristics rather than falsely claiming exact Shannon Information Gain.

Possible proxies:

- number of dependent Claims or decisions;
- downstream impact;
- probability of resolving a conflict;
- availability of a discriminating test;
- number of open questions affected;
- expected reduction in operator uncertainty;
- ability to unlock another blocked investigation.

#### Goal Relevance

Relationship to:

- CoreGoal;
- current task;
- long-term mission;
- active constraints;
- operator obligation;
- risk or deadline.

#### Conflict Severity

Severity depends on:

- Claim type and scope;
- consequence of error;
- affected dependencies;
- source independence;
- possibility of irreversible decisions.

#### Actionability

Progress is more likely when:

- an evidence source exists;
- a tool is available;
- a test can distinguish hypotheses;
- a human can answer a precise question;
- an experiment has measurable output.

#### Downstream Impact and Time Urgency

A small gap may receive high priority when many decisions depend on it or when its useful window is short.

### 8.2 Negative factors

- estimated computation and latency;
- token and API cost;
- safety and privacy risk;
- duplication;
- context-switch cost;
- repeated failure history;
- stale context;
- low probability of actionable progress.

### 8.3 Novelty

Novelty is a supporting signal only.

High novelty may indicate:

- a valuable new pattern;
- parser error;
- random noise;
- adversarial input;
- rare but irrelevant content.

Novelty must never become truth evidence by itself.

### 8.4 Reference priority formula

```text
ResearchPriority =
    + epistemic_need
    + expected_information_value
    + goal_relevance
    + conflict_severity
    + actionability
    + downstream_impact
    + time_urgency

    - estimated_cost
    - safety_risk
    - duplication_penalty
    - context_switch_cost
    - repeated_failure_penalty
    - staleness
```

The formula is a replaceable policy, not Architecture Canon.

### 8.5 Metric adapters

Native Kernel must not require a graph, vector index, or probabilistic model.

```text
UncertaintyAdapter
├─ epistemic-state heuristic
├─ conflict and evidence proxy
└─ probabilistic model

InformationValueAdapter
├─ dependency impact
├─ graph centrality
├─ question density
└─ decision impact

NoveltyAdapter
├─ lexical
├─ symbolic
├─ graph pattern
└─ vector distance

GoalRelevanceAdapter
├─ operator rule
├─ causal path
├─ symbolic match
└─ semantic similarity
```

Every evaluation records adapter and policy versions.

## 9. Attention Allocator

Attention Allocator assigns a temporary bounded budget. It may influence retrieval and investigation order without changing truth or Canon.

It may select:

- Claims and Links;
- questions;
- subgraphs or projection ranges;
- Working Notebook entries;
- model calls;
- tool preparations;
- deferred candidates.

Possible decisions:

```text
ALLOCATE
QUEUE
MERGE_WITH_EXISTING
DEFER
COOLDOWN
DROP_AS_DUPLICATE
REQUIRE_OPERATOR
REJECT_BY_POLICY
```

Required properties:

- explicit budget;
- TTL or expiry condition;
- explanation and reason codes;
- bounded preemption;
- duplicate merging;
- context-switch cost;
- starvation prevention through bounded priority aging;
- Receipt visibility.

### 9.1 Selective activation and future hardware

Today, selective activation may mean retrieval filtering, context loading, graph traversal, caching, and selective model calls.

Future implementation profiles may map the same semantic contract to memory-local compute, processing-in-memory, neuromorphic routing, analog systems, or another substrate.

The durable contract is:

> Select the semantically relevant work region without making the physical activation method part of Canon.

No future-hardware compatibility or superiority is claimed.

## 10. Investigation Runtime

Curiosity Core chooses and plans an investigation. Investigation Runtime performs the bounded work.

### 10.1 Lifecycle

```text
DETECTED
  ↓
SCREENING
  ↓
QUEUED
  ↓
ALLOCATED
  ↓
PLANNING
  ↓
INVESTIGATING
  ↓
┌───────────────┬──────────────────┐
│               │                  │
▼               ▼                  ▼
ANSWER        GAP FOUND       HYPOTHESIS NEEDED
│               │                  │
▼               ▼                  ▼
VALIDATION   ACTIVE QUERY      HYPOTHESIZING
│               │                  │
└───────────────┴──────────┬───────┘
                           ▼
                    RESULT EVALUATION
                           ↓
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
    SUPPORTED          REJECTED          UNRESOLVED
        └──────────────────┼──────────────────┘
                           ▼
                 PROMOTION REQUEST / CLOSE
```

Additional states:

```text
DUPLICATE
COOLDOWN
SUSPENDED
BUDGET_EXHAUSTED
BLOCKED_BY_TOOL
BLOCKED_BY_EVIDENCE
BLOCKED_BY_OPERATOR
POLICY_DENIED
STALE
DORMANT
ABORTED
REOPENED
HALTED
```

### 10.2 Investigation patterns

#### Decompose

```text
object
→ components
→ functions
→ dependencies
→ constraints
→ failure modes
```

#### Root-Cause Drill

Follow a causal path until a known mechanism, explicit gap, budget limit, or diminishing-return condition is reached.

#### Contradiction Analysis

Compare Claim scope, time, definitions, source, applicability, and evidence before declaring a real contradiction.

#### Active Query

Formulate a precise request to an operator, knowledge source, tool, or another agent.

#### Counterfactual Check

```text
if hypothesis is true  → what should be observed?
if hypothesis is false → what should be observed?
```

#### Falsification Search

Actively seek evidence that would disprove a hypothesis rather than only confirming it.

### 10.3 Stopping criteria

Stop, suspend, or close when:

- evidence is sufficient under declared policy;
- no available test can discriminate further;
- expected information value falls below threshold;
- budget is exhausted;
- new steps repeat old steps;
- operator input is required;
- policy denies an action;
- context is stale;
- the task loses goal relevance;
- a higher-severity risk appears;
- the valid result is `UNKNOWN` or `INSUFFICIENT_EVIDENCE`.

## 11. Hypothesis Engine

Hypothesis Engine creates a Hypothesis Set, not one privileged answer.

```text
Question
  ↓
Hypothesis Set
├─ H1
├─ H2
├─ H3
└─ H0: unknown cause / insufficient information
```

Each HypothesisRecord should include:

- semantic Claim reference;
- assumptions;
- scope and applicability;
- generation lineage;
- supporting and contradicting evidence;
- missing evidence;
- competing hypotheses;
- falsification conditions;
- discriminating tests;
- confidence provenance;
- risk;
- lifecycle status;
- dormancy and reopen conditions.

Possible set outcomes:

```text
BEST_SUPPORTED
MULTIPLE_PLAUSIBLE
UNDERDETERMINED
INSUFFICIENT_EVIDENCE
ALL_REJECTED
UNKNOWN_CAUSE
```

The system is not required to select one hypothesis.

### 11.1 Confidence and decay

Confidence must derive from explicit evidence and a versioned policy. It must not be initialized from an unexplained magic constant.

Temporal decay may change:

- attention priority;
- retrieval rank;
- activity;
- urgency;
- `DORMANT` status.

Temporal decay must not silently change:

- truth;
- evidence-derived confidence;
- provenance;
- historical state.

Absence of new evidence is not automatically evidence against a hypothesis.

### 11.2 Pruning and archival

A hypothesis may be archived when it is a duplicate, superseded, out of scope, explicitly rejected, impossible to test under current capabilities, or closed by operator decision. Archival does not erase its historical existence.

## 12. SystemInsight

`Self-Reflection` may remain an explanatory label, but the structured domain record is `SystemInsight`.

A SystemInsight is a falsifiable diagnostic proposal about a limitation of the system.

Types:

```text
KNOWLEDGE_DEFICIT
CAPABILITY_DEFICIT
TOOLING_DEFICIT
DATA_QUALITY_ISSUE
PERFORMANCE_REGRESSION
ARCHITECTURE_LIMITATION
CALIBRATION_FAILURE
RESOURCE_BOTTLENECK
POLICY_CONFLICT
HARDWARE_LIMITATION
OBSERVABILITY_GAP
```

Required fields:

- subject and affected scope;
- observed symptoms;
- evidence references;
- inferred limitation;
- confidence and severity;
- proposed action;
- falsification condition;
- policy version;
- provenance;
- review status.

Possible statuses:

```text
OPEN
ACKNOWLEDGED
UNDER_REVIEW
ACCEPTED_FOR_EXPERIMENT
REJECTED
RESOLVED
SUPERSEDED
DORMANT
```

A SystemInsight:

- is not truth about the system;
- is not an executable command;
- does not change code or policy;
- does not become an ADR automatically;
- cannot disable Guard policy;
- may become input to a separately reviewed experiment or ADR.

## 13. Calibration Loop

Curiosity Core must record when its own prioritization was wrong or wasteful.

Post-cycle labels may include:

```text
TRUE_POSITIVE
FALSE_POSITIVE
MISSED_IMPORTANCE
OVER_ALLOCATED
UNDER_ALLOCATED
DUPLICATE_TRIGGER
NO_PROGRESS
USEFUL_BUT_EXPENSIVE
POLICY_BLOCKED_CORRECTLY
```

Calibration evaluates:

- whether uncertainty was reduced;
- whether new evidence appeared;
- whether the budget was justified;
- whether novelty was noise;
- whether the same topic already existed;
- whether the trigger or allocation was too sensitive;
- whether the stopping rule worked.

Policy adaptation stages:

```text
v0.1  static policy
v0.2  operator-selected profiles
v0.3  Shadow recommendations
v0.4  operator-approved policy updates
```

The active module must not silently rewrite its own scoring policy.

## 14. Abstract data contracts

The following are semantic contracts, not mandatory Python classes or SQLite tables.

### 14.1 TargetRef

```text
TargetRef {
  kind: CLAIM | LINK | EVENT | QUESTION | GAP | HYPOTHESIS | INSIGHT
  id: string
}
```

### 14.2 CuriosityCandidate

```text
CuriosityCandidate {
  candidate_id
  stimulus_ref
  trigger_reasons[]
  gap_type?
  affected_scope[]
  context_ref
  detected_at
  policy_version
  deduplication_key
}
```

### 14.3 CuriosityEvaluation

```text
CuriosityEvaluation {
  evaluation_id
  candidate_id

  epistemic_need
  expected_information_value
  goal_relevance
  conflict_severity
  actionability
  downstream_impact
  novelty

  estimated_cost
  safety_risk
  duplication_penalty
  context_switch_cost
  repeated_failure_penalty

  raw_score
  normalized_priority

  metric_versions
  policy_version
  input_snapshot_hash
  evaluated_at
}
```

### 14.4 AttentionAllocation

```text
AttentionAllocation {
  allocation_id
  investigation_id
  total_budget
  reserved_budget
  selected_targets[]
  deferred_targets[]
  rejected_targets[]
  expires_at
  policy_version
  created_at
}
```

### 14.5 InvestigationRecord

```text
InvestigationRecord {
  investigation_id
  candidate_id
  state
  active_question_ids[]
  hypothesis_set_ids[]
  evidence_refs[]
  tool_request_refs[]
  system_insight_ids[]
  attempt_count
  started_at
  last_progress_at
  suspended_at?
  completed_at?
  stopping_reason?
  reopen_condition?
}
```

### 14.6 HypothesisSet

```text
HypothesisSet {
  set_id
  question_id
  hypothesis_ids[]
  comparison_policy_version
  result
  created_at
  evaluated_at?
}
```

### 14.7 HypothesisRecord

```text
HypothesisRecord {
  hypothesis_id
  claim_ref
  assumptions[]
  scope
  generated_from[]
  supporting_evidence[]
  contradicting_evidence[]
  competing_hypotheses[]
  falsification_conditions[]
  proposed_tests[]
  confidence_record
  lifecycle_status
  created_at
}
```

### 14.8 ResourceBudget

```text
ResourceBudget {
  policy_version
  max_duration_ms
  max_compute_units
  max_tokens
  max_tool_calls
  max_projection_expansion
  max_depth
  max_hypotheses
  max_questions
  max_system_insights
  max_retries
}
```

## 15. Proposed event namespace

The following vocabulary is proposed research only. It is not accepted into the current small event vocabulary and must not enter Issue #1.

### Detection and screening

```text
curiosity.candidate_detected
curiosity.trigger_evaluated
curiosity.candidate_accepted
curiosity.candidate_rejected
```

### Planning and allocation

```text
curiosity.investigation_queued
curiosity.budget_reserved
curiosity.attention_allocated
curiosity.plan_created
```

### Questions and evidence

```text
curiosity.question_raised
curiosity.evidence_requested
curiosity.evidence_observed
curiosity.tool_requested
curiosity.tool_result_attached
```

### Hypotheses

```text
curiosity.hypothesis_proposed
curiosity.hypothesis_revised
curiosity.hypothesis_challenged
curiosity.hypothesis_supported
curiosity.hypothesis_rejected
curiosity.hypothesis_superseded
```

### System insights

```text
curiosity.system_insight_detected
curiosity.architecture_change_proposed
curiosity.capability_gap_detected
curiosity.calibration_issue_detected
```

### Lifecycle

```text
curiosity.investigation_suspended
curiosity.investigation_resumed
curiosity.investigation_completed
curiosity.investigation_aborted
curiosity.budget_exhausted
curiosity.policy_denied
```

### Promotion

```text
curiosity.promotion_requested
curiosity.promotion_approved
curiosity.promotion_rejected
```

## 16. Replay, time, and idempotency

Reducers must not generate new UUIDs, timestamps, random scores, policy versions, or evidence links.

Unique IDs may be generated once during original command creation, including UUIDv4, UUIDv7, ULID, or another implementation-profile choice. Replay reads the recorded ID from the event.

### 16.1 Command envelope

```text
CommandEnvelope {
  command_id
  idempotency_key
  actor
  issued_at
  context_id
  policy_version
  expected_stream_version
  input_snapshot_hash
  payload
}
```

### 16.2 Event envelope

```text
EventEnvelope {
  event_id
  event_type
  schema_version
  stream_id
  stream_version
  idempotency_key
  occurred_at
  recorded_at
  actor
  payload
  previous_event_hash?
  event_hash?
}
```

### 16.3 Time semantics

```text
observed_at
received_at
evaluated_at
occurred_at
recorded_at
```

Times must be timezone-aware, preferably UTC.

### 16.4 Recomputing evaluations

Exact score reproduction requires:

- a frozen input snapshot;
- policy version;
- metric-adapter versions;
- normalization version;
- stable external inputs;
- deterministic model settings where a model is used.

If exact reproduction is impossible, the Receipt records the actual reproducibility level rather than claiming deterministic equivalence.

## 17. Deduplication, cooldown, and reopening

Each investigation should record:

```text
deduplication_key
stimulus_fingerprint
topic_fingerprint
attempt_count
previous_investigation_ids[]
cooldown_until
last_progress_at
failure_reason
reopen_condition
```

Example stopping policy:

```text
same gap investigated three times
+ no new evidence
+ no new tool
+ low expected information value
→ DORMANT
```

Reopen conditions may include:

- new evidence;
- changed active goal;
- new tool or capability;
- policy change;
- new conflict;
- higher severity;
- changed affected scope;
- explicit operator request.

## 18. Curiosity invariants

1. Curiosity Core never changes Canon or Epistemic State directly.
2. Every persisted record passes explicit Event Admission.
3. Operational curiosity events describe process, not truth.
4. Candidates, gaps, questions, hypotheses, and System Insights are not established knowledge.
5. Epistemic promotion is a separate TruthGate decision.
6. External, sensitive, or irreversible actions require Action Gate permission.
7. Attention is not validity.
8. Utility and novelty are not evidence.
9. Curiosity-driven context influence is visible in a Receipt.
10. Replay uses recorded values and generates no new randomness in reducers.
11. Scoring and Guard policies are versioned.
12. Guard wraps the complete lifecycle.
13. SystemInsight is not automatic self-modification.
14. Temporal decay changes attention, not evidence-derived truth confidence.
15. Curiosity Core can be disabled without damaging Native Kernel integrity.
16. Adaptive policy starts in Shadow.
17. Operator approval is required for architecture-policy promotion.
18. Legal deletion, restriction, and privacy requirements remain applicable.
19. Every investigation has budget, stopping, suspension, and reopen conditions.
20. `UNKNOWN` and `INSUFFICIENT_EVIDENCE` are valid outcomes.
21. Issue #1 controlled import remains unchanged.

## 19. Integration with Velantrim modules

```text
WhyEngine
→ explains why investigation matters

SituationModel
→ supplies current situational context

CausalContextBuilder
→ builds active causal relationships

FQKVE / RouteMemoryGate
→ routes memory and retrieval

Working Notebook
→ holds goal, question, constraints, and open items

Curiosity Core
→ decides what deserves investigation

Investigation Runtime
→ performs bounded work

Hypothesis Workspace
→ stores competing explanations

TruthGate
→ controls epistemic promotion

Native Kernel
→ preserves history, Claims, state, and Receipts
```

Curiosity Core coordinates these components; it does not redefine them.

## 20. Titan profile

Titan is the primary future host for the full profile.

Candidate capabilities:

- gap and conflict detection;
- goal-aware prioritization;
- causal investigation;
- active queries;
- external tools through Action Gate;
- Hypothesis Sets and falsification;
- counterfactual checks;
- collaborative hypothesis building;
- System Insights;
- calibration and Shadow adaptation.

Titan remains independent and is not reduced to Native Kernel projections.

## 21. Crystal Audit Curiosity profile

Crystal may use a restricted profile focused on trust infrastructure:

```text
Audit Curiosity
├─ evidence gap
├─ provenance gap
├─ contradiction
├─ compliance uncertainty
├─ missing validation
├─ temporal-validity gap
├─ policy conflict
└─ recommended verification step
```

Crystal does not require broad autonomous world investigation, unrestricted theory generation, or self-modifying curiosity.

Crystal remains functional without Native Kernel. Any transfer requires its own RFC, threat model, tests, privacy review, rollback, and approval.

## 22. MVP roadmap

### Phase 0 — Documentation

- boundary ADR;
- architecture RFC;
- threat and resource model;
- event namespace;
- `DOCUMENTED_ONLY` status.

### Phase 1 — Passive Shadow evaluator

- read frozen snapshots;
- detect conflict and evidence gaps;
- compute explainable scores;
- produce reports only;
- call no external tools;
- change no live context selection.

Evaluate trigger precision, false positives, duplicates, scoring stability, and replay behaviour.

### Phase 2 — Receipted attention

- budget and queue;
- TTL;
- allocation and reason codes;
- cooldown and deduplication;
- operator-visible Receipts.

### Phase 3 — Questions and Hypothesis Sets

- structured questions;
- competing hypotheses;
- explicit H0 unknown hypothesis;
- falsification conditions;
- Experimental Workspace.

### Phase 4 — Controlled investigation

- Action Gate;
- sandboxed tools;
- evidence collection;
- suspension and resume;
- promotion requests.

### Phase 5 — System Insights

- capability and tooling gaps;
- data-quality and performance issues;
- calibration reports;
- operator-review workflow.

### Phase 6 — Shadow adaptation

- alternative weight profiles;
- offline policy comparison;
- rollback plan;
- operator approval.

### Phase 7 — Future hardware profiles

- memory-local compute;
- processing-in-memory;
- neuromorphic routing;
- other future substrates.

No hardware claim is promoted without implementation evidence.

## 23. Minimum tests

### Determinism and replay

- same authoritative events yield equivalent state;
- replay creates no new IDs or times;
- frozen-input scoring is reproducible under the declared policy;
- adapter and policy versions are present.

### Authority boundaries

- Curiosity cannot directly change Epistemic State;
- SystemInsight cannot apply changes;
- tools cannot run without Action Gate;
- a hypothesis cannot become Canon automatically.

### Safety and resources

- budget exhaustion suspends or halts;
- recursive investigation is bounded;
- meta-reflection loop is blocked;
- denied action is not executed;
- sensitive data policy is enforced.

### Idempotency

- repeated command does not create duplicate hypotheses;
- one stimulus does not create unbounded investigations;
- equivalent questions are merged under policy.

### Hypotheses

- competing hypotheses remain visible;
- explicit unknown is supported;
- contradiction remains visible;
- temporal decay does not modify truth confidence.

### Calibration

- false-positive labels can be recorded;
- repeated failure affects operational priority only;
- new policy cannot become active without approval.

## 24. Quality metrics

```text
trigger_precision
trigger_recall
false_positive_rate
duplicate_investigation_rate
mean_information_value
cost_per_resolved_gap
budget_exhaustion_rate
operator_acceptance_rate
hypothesis_falsification_rate
unknown_completion_rate
unsafe_action_block_rate
replay_consistency_rate
context_switch_cost
time_to_first_useful_question
```

These metrics evaluate the module. They are not evidence that its hypotheses are true.

## 25. Anti-Canon

Curiosity Core must not claim:

- consciousness or biological desire;
- novelty equals importance;
- priority equals validity;
- repeated use or utility equals truth;
- model agreement equals approval;
- an unverified hypothesis is established;
- future hardware compatibility has been demonstrated;
- its scoring policy is universal;
- SystemInsight is philosophical self-awareness;
- autonomous self-modification is safe;
- absence of evidence automatically falsifies a hypothesis;
- documentation is runtime implementation.

## 26. Final status

```text
Name: Curiosity Core
Document version: RFC-0.1
Maturity: PROPOSED / DOCUMENTED_ONLY
Architecture role: optional active-cognition module
Primary host: Titan
Restricted profile: Crystal Audit Curiosity
Native Kernel dependency: abstract read, admission, Receipt, and promotion contracts
Direct Canon write: forbidden
Autonomous self-modification: forbidden
Adaptive policy: Shadow-only until operator approval
Issue #1 integration: forbidden
Production readiness: not claimed
```

## 27. Summary

```text
“I do not know”
→ “this unknown matters”
→ “here is the precise question”
→ “here are competing explanations”
→ “here is what would distinguish them”
→ “here is what was established”
→ “here is what remains unknown”
```

Curiosity Core is not a second Canon and not an unbounded autonomous agent. It is a bounded, auditable, replaceable engine for active investigation.

> Native Kernel preserves what the system recorded and knows under declared policy.  
> Curiosity Core decides what is worth attempting to learn.  
> TruthGate decides what may change epistemic state.  
> The operator decides which architecture and policy changes are accepted.
