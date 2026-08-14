# H11-001 — Independent Boundary Review Request

**Request identity:** `nk-h11-independent-review/H11-001-request-v1`  
**Request revision:** `2026-08-14-external-reviewer-generalization`  
**Frozen H11 plan:** `H11-001-c5-lab-canon-separation-v1`  
**Frozen plan SHA-256:** `60da649e675b79b3e70bf8a61cf03cb4d57bb989f4934b65ab8d50c925b19914`  
**Immutable review subject:** `e36b7f45410d74b8a65406bff6fdd6d070fa96b0`  
**Requested reviewer/reproducer:** external authenticated candidate; not preselected  
**Requested role:** `REVIEWER` or `REVIEWER_AND_REPRODUCER`  
**Current H11 outcome:** `NOT_TESTED`  
**Current execution admission:** `BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER`  
**Runtime:** `FROZEN`

> [!IMPORTANT]
> This file creates a review/qualification surface only. It is not H11 execution, not a qualification result, not semantic adjudication, and not evidence that independence is established. The immutable review subject is the base commit above, not this request-file diff.

## 1. Why this request exists

H11 is preregistered to test whether exact laboratory reproducibility can remain separate from Architecture Canon. PR #129 created the fail-closed admission package, and PR #130 bound the current machine truth. Execution remains blocked because no qualifying independent reviewer/reproducer has been established.

A substantive GitHub Codex review was already attempted on this request surface. It produced useful technical findings, later remediated through PR #134, but the Codex reviewer explicitly concluded `NOT_ESTABLISHED_FOR_H11_REVIEW_ROLE` because material self-review / organizational-independence concerns remained. That review therefore does **not** qualify or unblock H11.

The repository also previously completed IAR-1 with a substantive Codex review. Historical IAR-1 qualification **must not be inherited**: every H11 candidate must establish its own H11-specific evidence.

This PR is now generalized to any genuinely external, authenticated reviewer/reproducer who can independently disclose identity, authorship relation, custody relation, conflicts, frozen-input use, and private-state boundary.

## 2. Candidate separation facts — verify, do not assume

At this request revision, repository-visible state shows:

- collaborators snapshot: only `velantrian`;
- contributors snapshot: only `velantrian`;
- no repository-internal human candidate is currently available;
- current `main` has advanced beyond the immutable review subject through technical/documentation maintenance only; the H11 review subject remains intentionally frozen at `e36b7f45410d74b8a65406bff6fdd6d070fa96b0`;
- H11 preregistration, its frozen leakage rubric, admission package and machine-truth binding all exist before this request revision;
- the prior Codex review is technically useful but non-qualifying for H11 independence;
- CI success, owner/self-review, local Git identities, automated validators, LLM agreement, usage-limit notices, and prior IAR-1 qualification do **not** establish H11 independence.

These are only repository-visible context facts. A reviewer/reproducer must independently state whether its own separation basis is sufficient for H11 and disclose any material dependence or uncertainty that makes it insufficient.

## 3. Mandatory frozen packet

Review the following from exactly `e36b7f45410d74b8a65406bff6fdd6d070fa96b0`:

1. `AGENTS.md`
2. `docs/ai/README.md`
3. `docs/ai/CURRENT_STATE.md`
4. `docs/ai/KNOWN_RISKS.md`
5. `project-state.json`
6. `docs/A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md`
7. `docs/A9_REFERENCE_LABORATORY_BOUNDARY.md`
8. `docs/A10_OPEN_QUESTIONS_AND_FALSIFICATION.md`
9. `docs/research/RESIDUAL_A10_VALIDATION_PLAN.json`
10. `docs/research/H11_FAMILY_SELECTION.json`
11. `docs/research/H11_PREREGISTRATION.json`
12. `docs/research/H11_DEPENDENCY_GRAPH_SCHEMA.json`
13. `docs/research/H11_RAW_OBSERVATION_SCHEMA.json`
14. `docs/research/H11_SEMANTIC_ADJUDICATION_SCHEMA.json`
15. `docs/research/H11_REVIEWER_REPRODUCER_QUALIFICATION_SCHEMA.json`
16. `docs/research/H11_REVIEWER_REPRODUCER_QUALIFICATION.json`
17. `docs/research/H11_EXECUTION_ADMISSION.json`
18. `tools/ai_context/validate_h11_execution_admission.py`
19. `tests/test_h11_execution_admission.py`
20. `evidence/c5/2026-08-08-adr0023/manifest.json` as laboratory identity/context only; do not run H11 or derive an A10 result in this review.

The frozen H11 plan digest must remain exactly:

`60da649e675b79b3e70bf8a61cf03cb4d57bb989f4934b65ab8d50c925b19914`

## 4. Qualification questions

Answer each explicitly:

### Q1 — Identity and authenticated role
What reviewer/reproducer identity is making this review, what role is claimed, and what externally authenticated repository-visible evidence binds that identity to the review?

### Q2 — H11 authorship relation
Did the reviewer/reproducer author `H11_PREREGISTRATION.json` or its frozen leakage rubric? If yes, H11 independence fails.

### Q3 — Custody / material dependence
What concrete custody, organizational, tooling, model, implementation, profile, laboratory, or other dependence is relevant to the boundary under review? Disclose shared custody or uncertainty rather than hiding it.

### Q4 — Conflicts
List any conflict or material relationship that could make this self-review for H11.

### Q5 — Input boundary
Can the review/reproduction be performed entirely from repository-visible frozen inputs without implementation-private state or current profile bytes being treated as Architecture truth?

Explicitly state:

`private_implementation_state_used = false`

if and only if that is true.

### Q6 — Qualification conclusion
Is the candidate independence basis sufficient for H11's declared review role? Return exactly one of:

- `QUALIFIED_FOR_H11_REVIEW_ROLE`
- `NOT_ESTABLISHED_FOR_H11_REVIEW_ROLE`
- `DISQUALIFIED_FOR_H11_REVIEW_ROLE`

Explain the conclusion. Do not convert the conclusion into an H11 A10 outcome.

## 5. Boundary-review mandate

If and only if the reviewer considers its H11 review-role independence established, review the **admission boundary**, not the H11 experimental result. Try to find ways the package could still permit self-certification or profile→Canon capture before execution.

At minimum challenge:

- whether all 12 mandatory profile mechanisms remain explicitly auditable;
- whether `INDETERMINATE` has been kept out of the frozen leakage-class vocabulary;
- whether raw observations are structurally separated from semantic adjudication;
- whether a future `QUALIFIED` reviewer record can be fabricated without externally authenticated evidence;
- whether CI/bot notices/self-review can be smuggled in as `INDEPENDENT_SEMANTIC_ORACLE`;
- whether the hard refutation or `UNJUSTIFIED_CANON_DEPENDENCY` can be weakened post hoc;
- whether private implementation state or current profile bytes can become required Architecture truth;
- whether blocked admission can be mislabeled as `INDETERMINATE` instead of keeping H11 `NOT_TESTED`.

A finding against the admission package is not an H11 experimental finding. Do not construct the dependency graph, classify H11 edges, calculate `mandatory_profile_leakage_count`, or adjudicate H11.

## 6. Required response

Return a repository-visible substantive review containing:

```text
review_request: nk-h11-independent-review/H11-001-request-v1
reviewed_commit: e36b7f45410d74b8a65406bff6fdd6d070fa96b0
reviewer_identity:
reviewer_role: REVIEWER | REVIEWER_AND_REPRODUCER
authenticated_identity_evidence:
authorship_relation:
custody_relation:
conflicts:
repository_visible_frozen_inputs_only: YES | NO
private_implementation_state_used: false | true
independence_basis:
input_packet_read:
qualification_conclusion:
admission_boundary_findings:
execution_authorized_by_this_review: NO
H11_outcome: NOT_TESTED
runtime: FROZEN
```

If the reviewer cannot complete the packet, cannot substantiate an independence basis, or cannot bind the review to an external authenticated identity, the qualifying result remains `NOT_ESTABLISHED` and execution remains blocked.

## 7. Non-authorizations

This request does **not** authorize:

- H11 implementation or execution;
- dependency-graph construction/execution;
- leakage-edge classification or `mandatory_profile_leakage_count` calculation;
- semantic adjudication or any H11 outcome other than the pre-existing `NOT_TESTED` state;
- A10-H03/H06/H08/H09/H10 work;
- composition/federation work;
- runtime thaw or product-runtime integration;
- Final Canon or production;
- Issue #18 license decision;
- Issue #74 / ADR-0024 reducer-v2 decision;
- Track H recovered-source admission.

Until a new H11-specific qualifying review record exists, the authoritative state remains:

`A10_H11_EXECUTION_ADMISSION = BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER`.