# Velantrim Memory Evaluation Protocol v0

**Status:** RESEARCH / NON-CANONICAL / NOT RUNTIME AUTHORITY  
**Purpose:** define a reproducible, falsifiable evaluation discipline for memory-bearing and memory-improving agents without promoting benchmark scores, graders, retrieval signals, or self-generated lessons into epistemic authority.

## 1. Core non-conflation rules

```text
benchmark score        != system truth
retrieval hit          != evidence sufficiency
LLM grader verdict     != epistemic authority
reward                 != causal evidence
successful trajectory  != validated lesson
failed trajectory      != proof every used strategy was wrong
repetition             != validity
reuse                   != generalizability
self-improvement        != self-authorization
observed score delta   != demonstrated improvement
```

A memory item derived from experience is a **LessonCandidate** until the declared evaluation profile provides the evidence required for its intended scope.

## 2. Evaluation Manifest

Every comparable run MUST bind an immutable manifest containing at least:

- dataset name and version/digest;
- task subset and task ordering;
- random seed(s), where applicable;
- model/provider identity and version;
- reader/retriever configuration;
- grader model identity and version;
- grader prompt/template digest;
- extraction/memory-construction prompt digest;
- environment and capability profile;
- token/context budgets;
- retrieval limits;
- benchmark harness version/commit;
- memory initial-state identifier/digest;
- run identifier and timestamp.

A score produced under a materially different manifest is not silently comparable to an earlier score.

## 3. Required baseline families

Where applicable, an evaluation SHOULD include:

1. **No-memory baseline** — same agent/harness without retrieved or accumulated memory.
2. **Frozen-memory baseline** — fixed memory snapshot, no online writes.
3. **Self-improving condition** — online memory writes enabled under the declared policy.

A method does not count as improved merely because it performs well in absolute terms. The claim must be scoped against the declared baseline and manifest.

## 4. Multi-run stability

Single-run improvement is insufficient evidence for a self-improvement claim.

Report at minimum:

- mean task success / answer score;
- standard deviation across runs;
- best-worst gap;
- failure count;
- abstention count when meaningful;
- memory-state divergence indicators where representable.

If a memory method increases variance materially, that increase must be reported even when mean performance improves.

## 5. Task-order robustness

Self-improving systems MUST be stress-tested against alternative permissible task orders when ordering can affect memory construction.

Recommended minimum:

- declared/default order;
- at least two shuffled orders;
- optional adversarial/curriculum order where justified.

The evaluation MUST distinguish:

```text
content effect
!= curriculum/order effect
```

A claim of general self-improvement is weakened when gains disappear or reverse under reasonable reorderings.

## 6. LessonCandidate validation

A generated lesson, workflow, strategy, rule, preference abstraction, or reusable memory SHOULD carry enough context to evaluate applicability, including as relevant:

- source trajectory / event references;
- success/failure signal provenance;
- environment assumptions;
- required capabilities;
- forbidden or unavailable capabilities;
- scope/domain;
- observed counterexamples;
- independent reuse evidence;
- known evaluator ambiguity;
- current validation state.

Suggested states:

```text
PROPOSED
OBSERVED_USEFUL
CONTESTED
VALIDATED_FOR_SCOPE
REJECTED
SUPERSEDED
```

These are research-profile labels, not Final Canon.

## 7. Evaluator integrity

Evaluator output is itself an observation with provenance.

The protocol MUST permit the distinction:

```text
evaluator says FAIL
!= task strategy actually failed

evaluator says PASS
!= strategy is causally correct
```

Where deterministic grading is possible, prefer deterministic checks. Where semantic grading is necessary, freeze the grader stack and record its identity in the Evaluation Manifest.

Changing the grader model, prompt, rubric, or extraction stage creates a new evaluation condition unless an explicit bridge experiment demonstrates comparability.

## 8. Environment applicability

A strategy valid under one capability/environment profile is not automatically valid under another.

```text
semantic similarity
!= operational applicability
```

Memory construction and validation should receive the environment constraints materially relevant to the lesson. Unsupported actions must not become trusted reusable strategies merely because they are plausible in another environment.

## 9. Memory contagion / feedback-loop test

The evaluation SHOULD detect self-reinforcing bad memories:

```text
stochastic strategy
-> accidental success or evaluator pass
-> memory write
-> retrieval
-> repeated use
-> increasing retrieval frequency
```

Measure, where feasible:

- first appearance of a strategy;
- retrieval frequency over time;
- downstream usage count;
- performance before/after introduction;
- whether removal/quarantine reverses the effect.

## 10. Conflict, correction, deletion and temporal profiles

This protocol may compose with independent stress profiles for:

- dynamic/static/conditional memory conflicts;
- correction and supersession;
- deletion durability and resurrection resistance;
- valid-time vs knowledge/record-time behavior;
- long-horizon recall and multi-hop retrieval.

Composing a benchmark does not grant that benchmark authority over system truth or Canon.

## 11. Efficiency reporting

Accuracy SHOULD be reported next to the resources used to obtain it.

Recommended fields:

- retrieved tokens / question;
- reader tokens / question;
- write tokens / task;
- latency p50/p95/p99;
- cost / task or question where meaningful;
- accuracy gain per 1k reader tokens;
- memory growth over time.

A system that obtains a small score gain by consuming dramatically more context is not silently labeled more efficient or strictly better.

## 12. Positive obligations and negative invariants

Evaluation SHOULD separate:

**Positive obligations** — behavior the system must successfully perform.

**Negative invariants** — forbidden failures the system must avoid.

A no-memory or always-abstain system may satisfy many negative invariants while failing the actual memory obligations. Aggregate scoring must not hide this distinction.

## 13. Self-improvement claim contract

A claim that a system self-improves should state:

- baseline;
- evaluation manifest identity;
- run count;
- task-order conditions;
- mean change;
- variance change;
- worst-case change;
- resource-cost change;
- known evaluator limitations;
- whether the learned memories were validated or merely generated.

Recommended conservative interpretation:

```text
mean gain + unstable variance + order sensitivity
= fragile improvement claim

mean gain + stable/repeated runs + order robustness
+ bounded cost + validated memories
= stronger scoped improvement evidence
```

## 14. Current evidence inspirations

This research profile is informed by recent external evaluation work including:

- MemConflict-style dynamic/static/conditional conflict testing;
- Agent Memory Atlas-style correction/deletion/governance evaluation;
- long-horizon memory benchmarks such as LoCoMo, LongMemEval and BEAM;
- self-improving-agent fragility studies emphasizing multi-run variance, task-order sensitivity, evaluator effects and underspecification.

External benchmarks are evidence instruments, not architecture authorities.

## 15. Authority boundary

This document:

```text
DOES define a research/evaluation proposal.
DOES NOT modify runtime behavior.
DOES NOT authorize self-modification.
DOES NOT authorize Canon writes.
DOES NOT make any external benchmark normative authority.
DOES NOT change existing Native Kernel Final Canon status.
```

Any executable conformance harness, accepted invariant family, or promotion into provisional architecture authority requires a separate governed decision and review.