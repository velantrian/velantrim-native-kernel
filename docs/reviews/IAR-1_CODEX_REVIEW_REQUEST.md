# IAR-1 — Independent Architecture Review Request

**Request identity:** `nk-independent-architecture-review/IAR-1-request`  
**Protocol:** `nk-independent-architecture-review/1`  
**Governing decision:** `ADR-0026`  
**Architecture tracking:** `Issue #88`  
**Immutable reviewed commit:** `2dd51723e30d5f3c5e86268365bf4cf7639b5e9a`  
**Requested reviewer:** GitHub Codex review agent  
**Review mode:** `ADVERSARIAL_FALSIFICATION`  
**Product runtime:** `FROZEN`

> [!IMPORTANT]
> This file is a review request, not a review result and not evidence that independence is established. The PR containing this request exists only to provide a review surface for a separate review agent. The architecture subject is the immutable base commit above, not the request-file diff itself.

## 1. Proposed independence basis to verify, not assume

The requested reviewer may qualify only if the review record can support all of the following:

```yaml
reviewer_identity: github-codex-review-agent
reviewer_kind: AGENT
reviewed_commit: 2dd51723e30d5f3c5e86268365bf4cf7639b5e9a
prior_authorship_of_A1_A10: false
prior_authorship_of_integrated_review: false
review_mode: ADVERSARIAL_FALSIFICATION
current_runtime_used_as_architectural_oracle: false
```

Repository-visible separation at request time:

- GitHub collaborators endpoint lists only `velantrian` as a repository collaborator;
- GitHub contributors endpoint lists only `velantrian` as a contributor;
- PR #103 and PR #104 had no formal qualifying review and their Codex activity was quota/bot notice, not architectural authorship or validation;
- the requested Codex agent is being invoked only after A1–A10, the integrated review, ADR-0026, and the review protocol already exist on immutable `main`;
- the agent is explicitly instructed to attack the blueprint rather than preserve the current authorship lineage's conclusions.

These facts are a proposed concrete independence basis. **They do not automatically make the review qualifying.** If the agent cannot substantively review the full packet or cannot satisfy the required output, the correct outcome is `INCOMPLETE_REVIEW` or `BLOCKED_NO_QUALIFYING_REVIEWER`, not self-certification.

## 2. Mandatory reading packet

Review the content at exactly `2dd51723e30d5f3c5e86268365bf4cf7639b5e9a`, following this order:

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
17. `docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md`
18. enough P1–C5 contracts/evidence/runtime context to detect implementation capture without treating current implementation as architecture authority.

Do not use this request file as a substitute for reading the packet.

## 3. Adversarial mandate

Your objective is **not approval**. Try to invalidate, shrink, weaken, split, or expose hidden assumptions in the provisional architecture.

Specifically search for:

- Python, SQL, event-sourcing, reducer, exact-replay, JSON, SHA-256, current-ID, or conventional-digital assumptions smuggled into Canon candidates;
- concepts that are implementation conveniences rather than architecture obligations;
- circular or non-falsifiable definitions;
- obligations stronger than necessary;
- contradictions or unresolved tensions across A1–A10 missed by the integrated review;
- requirements that secretly assume unbounded memory, permanent identifiers, a global order, exact history, or lossless representation;
- inability to distinguish Source, Evidence, Provenance, Authority, Claim, Truth, Unknown, False, Conflict, Contradiction, Resolution, Revision, Supersession, Erasure, and Forgetting on a radically different realization;
- conformance rules too vague to fail;
- cases where current P1–C5 evidence is being used as architecture proof;
- reasons BPV-1 would become self-confirming.

Passing current tests is not a reason to accept the architecture.

## 4. Required Q1–Q12 answers

Answer every question. If there is no finding for a question, state `NO_FINDING_FOR_SCOPE` and explain the scope checked.

### Q1 — Minimal kernel

What is the smallest set of obligations that still deserves the name Native Kernel? Which A1–A10 concepts are useful taxonomy but not architectural necessities?

### Q2 — Event-sourcing independence

Can accountability, revision lineage, and reconstruction be specified without making append-only Event history or exact replay universal requirements?

### Q3 — Bounded memory

Which obligations can survive finite storage, lossy compaction, forgetting, or partial retention? Which cannot?

### Q4 — Identity

Does the identity model depend on stable bytes, hashes, global IDs, or exact state continuity more than the blueprint admits?

### Q5 — Time and ordering

Are occurrence, observation, write, causal, and semantic-precedence distinctions sufficient and non-circular? Is any total order smuggled in through current machinery?

### Q6 — Epistemic separation

Can Source, Evidence, Provenance, and Authority remain distinct in a radically different realization, or do some distinctions depend on the present data model?

### Q7 — Conflict and uncertainty

Does the model preserve unresolved plurality without a universal winner or scalar confidence? Where could `Conflict ≠ Contradiction` become ambiguous?

### Q8 — Deletion and forgetting

Are logical erasure, physical erasure, cryptographic erasure, restriction, and forgetting operationally distinguishable enough for falsifiable claims?

### Q9 — Conformance

Can A8 conformance be tested without reproducing current representation choices? Which preservation criteria are too vague to falsify?

### Q10 — Reference-laboratory capture

Which P1–C5 mechanisms are most likely to recapture Canon by inertia despite A9?

### Q11 — Independent realization

What must a genuinely cross-lineage implementation deliberately avoid reusing so BPV-1 is not merely a port of the Python model?

### Q12 — Refutation conditions

Name at least three concrete observations that should force the project to weaken or refute a major architecture claim rather than reinterpret the test until it passes.

## 5. Required finding register

Use `IAR-F01`, `IAR-F02`, ... for every material finding.

For each finding provide:

```yaml
finding_id: IAR-FNN
severity: BLOCKING | MATERIAL | MODERATE | MINOR
status: OPEN
affected_slices: [A1, ...]
claim_or_obligation: <exact subject>
finding: <specific problem>
counterexample_or_reasoning: <specific challenge>
implementation_capture_risk: NONE | LOW | MEDIUM | HIGH
falsifiability_impact: NONE | LOW | MEDIUM | HIGH
recommended_disposition: REMOVE | WEAKEN | SPLIT | CLARIFY | TEST | RETAIN
bpv1_dependency: BLOCKS | SHOULD_INFORM | NONE
```

Any unresolved `BLOCKING` finding must use `bpv1_dependency: BLOCKS`.

## 6. Mandatory end-of-review summary

Return all of the following:

```text
review_process_outcome:
  QUALIFYING_REVIEW_COMPLETE |
  INCOMPLETE_REVIEW |
  REVIEW_INVALIDATED_BY_INDEPENDENCE_FAILURE |
  BLOCKED_NO_QUALIFYING_REVIEWER

reviewer_identity:
independence_basis:
reviewed_commit: 2dd51723e30d5f3c5e86268365bf4cf7639b5e9a
input_packet_read:
Q1-Q12_complete: YES | NO
finding_count:
blocking_findings:
material_findings:
stable_candidate_claims:
claims_that_must_remain_provisional:
BPV1_status_recommendation:
product_runtime_status: FROZEN
```

Also state explicitly whether the proposed independence basis is sufficient in your view and why.

## 7. Non-authorizations

This review request does not authorize:

- product runtime thaw;
- reducer v2;
- Issue #74 / ADR-0024 acceptance;
- Issue #18 license choice;
- Track H source admission;
- new Event verbs;
- NK-EPI runtime;
- Final Canon;
- production promotion;
- universal substrate-independence claims;
- BPV-1 execution.

BPV-1 remains blocked until a qualifying review is captured and its blocking/material findings are reconciled under ADR-0026.