# Independent Architecture Review Protocol

**State:** `AUTHORIZED / REVIEW NOT YET ESTABLISHED`  
**Protocol identity:** `nk-independent-architecture-review/1`  
**Governing decision:** `ADR-0026`  
**Architecture issue:** `#88`  
**Reviewed subject:** A1–A10 provisional blueprint + integrated reconciliation  
**Runtime expansion:** `FROZEN`

## 1. Purpose

This protocol defines how Native Kernel must obtain an architectural review that is meaningfully independent from the authorship lineage that drafted A1–A10 and performed the first integrated review.

The goal is not approval. The goal is to **find reasons the blueprint may be wrong, over-specified, non-falsifiable, implementation-captured, internally circular, or insufficiently portable** before a bounded cross-lineage experiment is designed.

A review performed under this protocol does not itself promote Canon, runtime, maturity, or production status.

## 2. Review authority boundary

A qualifying reviewer must have a declared identity and independence basis showing that the reviewer did not author the reviewed A1–A10 draft set or `nk-integrated-blueprint-review/A1-A10-review-1`.

The review record must state:

```yaml
reviewer_identity: <declared>
reviewer_kind: HUMAN | AGENT | TEAM | OTHER
independence_basis: <why this reviewer is meaningfully separate from the authorship lineage>
prior_authorship_of_A1_A10: false
prior_authorship_of_integrated_review: false
review_scope: A1-A10 + integrated reconciliation
review_mode: ADVERSARIAL_FALSIFICATION
current_runtime_used_as_architectural_oracle: false
```

A fresh model session, a different model, or a different person is not automatically independent merely by label. The record must explain the concrete separation that matters for the review.

If meaningful independence cannot be established, record:

```text
INDEPENDENT_REVIEW_STATUS = BLOCKED_NO_QUALIFYING_REVIEWER
```

Do not self-certify.

## 3. Required input packet

The reviewer must be given the architecture truth surfaces, not only a handoff summary. The reviewer must read `AGENTS.md` and then follow the live mandatory orientation order declared there.

Minimum packet:

1. `AGENTS.md`
2. `README.md`
3. `STATUS.md`
4. `project-state.json`
5. `docs/ai/README.md`
6. `docs/ai/CURRENT_STATE.md`
7. `docs/ai/KNOWN_RISKS.md`
8. `ROADMAP.md`
9. `docs/ARCHITECTURE_REFOUNDATION.md`
10. A1–A10 English documents
11. `docs/INTEGRATED_A1_A10_REVIEW.md`
12. `docs/A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md`
13. `docs/A9_REFERENCE_LABORATORY_BOUNDARY.md`
14. `docs/A10_OPEN_QUESTIONS_AND_FALSIFICATION.md`
15. `docs/adr/0025-blueprint-before-runtime-expansion.md`
16. `docs/adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md`
17. enough P1–C5 contract/evidence context to detect implementation capture, without treating that implementation as normative authority.

Russian translations may be supplied as a parallel reading surface but must not silently change semantic status.

## 4. Reviewer mandate

The reviewer is explicitly asked to challenge the blueprint, not to make it look coherent.

The review must attempt to find:

- hidden dependence on Python, SQL, event sourcing, exact replay, JSON, SHA-256, current ID schemes, current reducer semantics, or conventional digital hardware;
- concepts that are merely implementation conveniences disguised as architecture;
- architecture obligations that are stronger than necessary;
- concepts that can be removed without losing the project's purpose;
- circular definitions or definitions that depend on their own conclusions;
- non-falsifiable claims;
- conflicts between A1–A10 that the first integrated review missed;
- places where `Unknown`, `False`, `Unsupported`, `Indeterminate`, `Conflict`, `Contradiction`, `Resolution`, `Authority`, `Evidence`, `Source`, `Identity`, `Revision`, `Supersession`, `Deletion`, `Erasure`, or `Forgetting` can collapse incorrectly;
- portability claims that cannot be operationalized as scoped preservation/loss tests;
- assumptions that require unbounded memory, global ordering, exact historical replay, or permanent identifiers without being declared;
- obligations that cannot survive lossy/probabilistic/bounded representations;
- contradictions between semantic accountability and forgetting/deletion;
- areas where current laboratory evidence is being used as proof of architecture rather than as bounded evidence.

## 5. Required questions

The review must answer, with findings or explicit `NO_FINDING_FOR_SCOPE`, at least these questions:

### Q1 — Minimal kernel

What is the smallest set of obligations that still deserves the name Native Kernel? Which A1–A10 concepts are useful taxonomy but not architectural necessities?

### Q2 — Event-sourcing independence

Can accountability, revision lineage and reconstruction be specified without making append-only Event history or exact replay universal requirements?

### Q3 — Bounded memory

Which obligations can survive finite storage, lossy compaction, forgetting or partial retention? Which cannot?

### Q4 — Identity

Does the identity model depend on stable bytes, hashes, global IDs or exact state continuity more than the blueprint admits?

### Q5 — Time and ordering

Are occurrence, observation, write, causal and semantic-precedence distinctions sufficient and non-circular? Is any total order being smuggled in through current machinery?

### Q6 — Epistemic separation

Can Source, Evidence, Provenance and Authority remain distinct in a radically different realization, or do some distinctions depend on the present data model?

### Q7 — Conflict and uncertainty

Does the model preserve unresolved plurality without requiring a universal winner or scalar confidence? Are there cases where `Conflict ≠ Contradiction` becomes ambiguous?

### Q8 — Deletion and forgetting

Are logical erasure, physical erasure, cryptographic erasure, restriction and forgetting operationally distinguishable enough to support falsifiable claims?

### Q9 — Conformance

Can A8 conformance be tested without reproducing current representation choices? Where are the preservation criteria too vague to falsify?

### Q10 — Reference-laboratory capture

Which current P1–C5 mechanisms are most likely to recapture Canon by inertia despite A9?

### Q11 — Independent realization

What would a genuinely cross-lineage implementation need to avoid reusing so that a later experiment is not merely a port of the current Python model?

### Q12 — Refutation conditions

Name at least three observations that should force the project to weaken or refute a major current architecture claim rather than reinterpret the test until it passes.

## 6. Finding format

Every material finding must use a stable review-local identifier:

```text
IAR-F01
IAR-F02
...
```

Required fields:

```yaml
finding_id: IAR-FNN
severity: BLOCKING | MATERIAL | MODERATE | MINOR
status: OPEN | RESOLVED
affected_slices: [A1, ...]
claim_or_obligation: <exact subject>
finding: <what appears wrong or under-justified>
counterexample_or_reasoning: <specific challenge>
implementation_capture_risk: NONE | LOW | MEDIUM | HIGH
falsifiability_impact: NONE | LOW | MEDIUM | HIGH
recommended_disposition: REMOVE | WEAKEN | SPLIT | CLARIFY | TEST | RETAIN
bpv1_dependency: BLOCKS | SHOULD_INFORM | NONE
reconciliation_record: <required when status=RESOLVED>
```

A finding is not closed merely because the current authors disagree. Reconciliation must state the rationale and evidence boundary. Assigning a recommended disposition is not the same as resolving a finding.

## 7. Severity rules

### `BLOCKING`

Use when the finding would make BPV-1 self-confirming, architecture-incoherent, or incapable of distinguishing success from failure.

Examples:

- a supposedly substrate-neutral obligation secretly requires the current Event/reducer model;
- the proposed experiment cannot falsify the claim it is meant to test;
- two core obligations are mutually incompatible for the declared scope.

An unresolved `BLOCKING` finding **always blocks BPV-1**. While it remains `OPEN`, its `bpv1_dependency` must be `BLOCKS`. `TEST`, `RETAIN`, or any other recommended disposition alone cannot bypass this gate.

### `MATERIAL`

Use when the finding could substantially alter Canon candidates or experiment design but does not make the entire validation phase invalid.

### `MODERATE`

Use for significant ambiguity or incomplete boundary that can be resolved without redesigning the central architecture.

### `MINOR`

Use for wording/indexing clarity that does not materially change semantic claims.

## 8. Mandatory anti-confirmation rules

The reviewer must not:

- treat current passing tests as proof that the architecture is correct;
- infer architectural necessity from existing code structure;
- require identical bytes as proof of semantic equivalence unless byte identity is the claim under test;
- upgrade `NOT_TESTED` to support;
- convert lack of a counterexample into universal proof;
- resolve open philosophical questions by definition alone;
- assume a future substrate must resemble a conventional database or event log;
- assume a different programming language alone establishes cross-lineage independence.

## 9. Review outcomes

The review itself has one of these process outcomes:

```text
QUALIFYING_REVIEW_COMPLETE
BLOCKED_NO_QUALIFYING_REVIEWER
INCOMPLETE_REVIEW
REVIEW_INVALIDATED_BY_INDEPENDENCE_FAILURE
```

These are review-process statuses, not A10 hypothesis outcomes.

A qualifying review must produce:

- reviewer identity and independence basis;
- reviewed commit SHA;
- input packet identity/list;
- findings register;
- explicit answers to Q1–Q12;
- list of claims considered stable candidates;
- list of claims that should remain provisional;
- list of blocking/material findings that must shape BPV-1;
- explicit statement that product runtime remains frozen.

`QUALIFYING_REVIEW_COMPLETE` means the review process completed under this protocol. It does **not** imply that its findings have been reconciled or that BPV-1 is admitted.

## 10. Reconciliation gate before BPV-1

BPV-1 remains `BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION` until:

- the review is qualifying;
- every `BLOCKING` finding has `status: RESOLVED` with a concrete reconciliation record;
- every unresolved `BLOCKING` finding, if any exists, retains `bpv1_dependency: BLOCKS` and therefore keeps BPV-1 blocked;
- every `MATERIAL` finding is either reconciled or explicitly carried into the experiment as a falsification dependency;
- experiment success/failure criteria are written before implementation;
- no current runtime component is silently promoted into the experiment's oracle.

There is no exception that allows an open `BLOCKING` finding to be carried into BPV-1 as merely a test target. The blocker must first be resolved sufficiently to make the experiment non-self-confirming, architecture-coherent, and capable of distinguishing success from failure.

## 11. What completion proves

A completed qualifying review proves only that the architecture was subjected to a documented independent adversarial challenge under this protocol.

It does **not** prove:

- that A1–A10 is correct;
- that the architecture is universally portable;
- that any substrate can implement it;
- that BPV-1 will succeed;
- that runtime may thaw;
- that Canon may be finalized;
- production readiness.