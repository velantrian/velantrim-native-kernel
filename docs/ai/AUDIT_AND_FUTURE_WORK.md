# Velantrim Native Kernel — Audit & Future Work Ledger

> This ledger is an orientation and future-work surface. It does not authorize implementation.
>
> `future-work entry != implementation authorization`
>
> `priority != authorization`
>
> `research finding != runtime capability`
>
> `open issue != permission to implement`

## 0. How AI must use this document

This document is a durable audit/handoff surface for future maintainers and AI agents. It is subordinate to live repository state and repository-local authority routing.

Before selecting any work:

1. resolve live `main`, open PRs/issues, reviews and Actions;
2. read `project-state.json` and current H11 machine records;
3. follow the mandatory reading order in `docs/ai/README.md` and constraints in `AGENTS.md`;
4. reconcile every item below against live evidence;
5. classify it as still current, stale, blocked, not authorized, or requiring a new decision;
6. propose exactly one bounded next scope only after authority and authorization are explicit.

**DO NOT AUTO-SELECT NEXT MILESTONE.** This ledger preserves future work; it does not choose it.

Repository-local authority routing overrides any generic source-of-truth hierarchy. Live code wins over stale documentation for implementation facts, but bounded laboratory behavior does not automatically override accepted architecture authority for semantic meaning.

## 1. Status vocabulary

- `OPEN` — confirmed unfinished work with a current bounded objective.
- `INVESTIGATE` — evidence gathering/reproduction is required before selecting a fix or experiment.
- `CANDIDATE` — possible direction; not selected.
- `DEFERRED` — intentionally postponed.
- `BLOCKED` — a concrete dependency prevents progress.
- `NOT_AUTHORIZED` — implementation/execution is currently forbidden or lacks required approval.
- `DONE` — completion is supported by current evidence for the declared scope.
- `STALE` — historical item no longer matches current truth.
- `NEEDS_REPRODUCTION` — suspected defect/result must first be reproduced.
- `NEEDS_ARCHITECTURE_DECISION` — code would be premature until a decision/contract/acceptance criteria exist.

Priority labels, when used, are triage only: `P0/P1/P2/P3 != authorization`.

## 2. Current stop boundary

Current research routing is fail-closed:

```text
selected family: A10-H11
gate: A10_H11_EXECUTION_ADMISSION
admission: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER
reviewer/reproducer: NOT_ESTABLISHED
H11: NOT_TESTED
implementation/execution: NOT AUTHORIZED
dependency-graph execution: NOT AUTHORIZED
semantic adjudication: NOT AUTHORIZED
runtime: FROZEN
product runtime thaw: false
Final Canon: DEFERRED / NOT AUTHORIZED
production: false
```

The current H11 plan is `H11-001-c5-lab-canon-separation-v1`, SHA-256 `60da649e675b79b3e70bf8a61cf03cb4d57bb989f4934b65ab8d50c925b19914`. The immutable H11 review subject is `e36b7f45410d74b8a65406bff6fdd6d070fa96b0`.

PR #131 is the repository-visible external review surface. It must not be merged or treated as qualification merely because it exists, is green, or receives owner/AI activity.

## 3. Current stable checkpoint

This ledger does not own a durable live-HEAD value. Resolve live `main` at read time.

At ledger creation, the verified live checkpoint was PR #147 / `6811b54749425210104296fdeb14a8750a60f674`, which hardened outreach-evidence and residual-order reporting without changing H11, runtime, Canon, reducer semantics, issue outcomes, or machine state.

The committed H11 state-binding checkpoint remains PR #130 / `e36b7f45410d74b8a65406bff6fdd6d070fa96b0`; later documentation descendants do not redefine the frozen H11 subject.

## 4. Concrete open work

### NK-FW-001 — Establish an independent H11 reviewer/reproducer

**State:** `BLOCKED`  
**Priority:** `P1`  
**Implementation authorized:** `NO`  
**Runtime capability change:** `NO`  
**Known issue / surface:** Issue #88, PR #131  
**Last verified:** ledger creation checkpoint; re-resolve live evidence before use.

#### Question
Can a genuinely external authenticated reviewer/reproducer satisfy the existing H11 qualification contract without self-review, shared custody, hidden private state, or repository-local self-assertion being mistaken for independence?

#### Why it matters
This is the current explicit execution-admission blocker for H11.

#### Existing evidence
- `docs/research/H11_REVIEWER_REPRODUCER_QUALIFICATION_SCHEMA.json`
- `docs/research/H11_REVIEWER_REPRODUCER_QUALIFICATION.json`
- `docs/research/H11_EXECUTION_ADMISSION.json`
- `tools/ai_context/validate_h11_execution_admission.py`
- PR #131 and `docs/reviews/H11-001_INDEPENDENT_REVIEW_REQUEST.md`

Current Codex/AI evidence is non-qualifying for H11 independence. External outreach/contact/reply is not qualification by itself.

#### Files / components to inspect
The frozen PR #131 packet and the qualification/admission machine contract above.

#### Required audit
Evaluate authenticated identity/role, authorship independence, custody independence, conflicts/material dependence/self-review, frozen-input boundary, repository visibility and private-state exclusion.

#### Required experiment / reproduction
None before qualification. H11 execution remains prohibited while admission is blocked.

#### Preconditions
A distinct external candidate supplies repository-visible authenticated evidence suitable for the existing qualification contract.

#### Non-goals
Do not invent a reviewer, relax the contract, qualify owner/AI/CI, execute H11, or create a competing review surface.

#### Authority boundaries
Qualification does not itself authorize execution. A separate `A10_H11_EXECUTION_ADMISSION` reassessment is required.

#### Exit criteria
A repository-visible machine-evaluable qualification result is established under the canonical contract, followed by a separate admission decision.

#### Possible outcomes
- `DONE`
- `STILL_OPEN`
- `BLOCKED`
- `NOT_AUTHORIZED`

### NK-FW-002 — H11 lab / Canon separation experiment

**State:** `NOT_AUTHORIZED`  
**Priority:** `P1`  
**Implementation authorized:** `NO`  
**Runtime capability change:** `NO`

#### Question
Can exact laboratory mechanisms remain reproducible without being elevated into universal Architecture Canon?

#### Why it matters
This is the selected A10-H11 falsification boundary, not a proof of universal portability or the whole architecture.

#### Existing evidence
Frozen H11 preregistration, dependency/raw/adjudication schemas, qualification contract, execution-admission record and C5 laboratory bundle.

#### Required audit
Before any execution, re-validate that all frozen controls remain unchanged and that an independent reviewer/reproducer has qualified through externally authenticated evidence.

#### Required experiment / reproduction
Only the preregistered H11 experiment, and only after separate admission authorizes it.

#### Preconditions
`QUALIFIED` reviewer/reproducer plus separate execution-admission reassessment.

#### Non-goals
No post-hoc rubric changes; no composition/federation claim; no universal substrate proof; no runtime thaw; no Final Canon promotion.

#### Authority boundaries
`reference laboratory != Architecture authority`; `SUPPORTED_FOR_SCOPE != universal proof`.

#### Exit criteria
One allowed A10 outcome produced under the frozen contract after qualifying execution/adjudication.

#### Possible outcomes
- `DONE`
- `STILL_OPEN`
- `NEEDS_REPRODUCTION`
- `NOT_AUTHORIZED`

## 5. Investigation queue

### NK-FW-003 — Historical v0.1.2.1 / original 44-test recovery

**State:** `BLOCKED`  
**Priority:** `P2`  
**Implementation authorized:** `NO` for reconstructed authenticity claims  
**Known issue:** #1

#### Question
Do operator-controlled local sources/backups contain the authentic v0.1.2.1 source and original 44-test suite?

#### Existing evidence
Current evidence state is `NOT_FOUND_IN_ACCESSIBLE_SOURCES`, not globally lost.

#### Required audit
Search only authorized sources. Distinguish absence from accessible sources from global loss.

#### Non-goals
Never reconstruct approximate code/tests and label them authentic.

#### Exit criteria
Authentic artifacts are admitted with provenance, or the operator makes an explicit decision about the failure branch.

### NK-FW-004 — Reducer referential semantics / ADR-0024 boundary

**State:** `NEEDS_ARCHITECTURE_DECISION`  
**Priority:** `P1`  
**Implementation authorized:** `NO`  
**Known issue:** #74

#### Question
Should a future reducer/policy version add stricter referential validation, and under what versioned semantic contract?

#### Existing evidence
Reducer v1 intentionally remains historical evidence and must not be modified in place.

#### Required audit
Reproduce the exact current referential gap, preserve v1 semantics, and identify candidate version/policy boundaries.

#### Non-goals
No in-place reducer-v1 semantic rewrite.

#### Exit criteria
Explicit operator architecture/policy decision with acceptance criteria before implementation.

### NK-FW-005 — License / contribution regime

**State:** `NEEDS_ARCHITECTURE_DECISION`  
**Priority:** `P1`  
**Implementation authorized:** `NO`  
**Known issue:** #18

Public repository visibility does not imply an open-source license. License/publication/contribution regime is operator-reserved.

### NK-FW-006 — Logical forgetting / deletion / erasure evidence boundaries

**State:** `INVESTIGATE`  
**Priority:** `P1`  
**Known issue:** #16

Preserve the distinctions among logical disposition, physical deletion, cryptographic erasure, forgetting/loss and epistemic accessibility. Strong physical/crypto claims require threat-scoped external evidence; unavailable evidence yields `INDETERMINATE`, not a stronger claim.

### NK-FW-007 — Identity/serialization/hash profile boundaries

**State:** `OPEN` for issue-level reconciliation only; implementation is separately gated  
**Priority:** `P2`  
**Known issue:** #14

Architecture identity/continuity remains semantic/profile-neutral; concrete serialization/hash shapes are profile/version concerns. Re-audit live issue acceptance before selecting any work.

### NK-FW-008 — Event integrity profile boundary

**State:** `OPEN` for issue-level reconciliation only; implementation is separately gated  
**Priority:** `P2`  
**Known issue:** #15

Event-chain mechanisms are profile-specific evidence, not a universal state/change shape. Re-audit live issue acceptance before selecting any change.

### NK-FW-009 — Neutral scoped semantic conformance

**State:** `OPEN` for issue-level reconciliation only; implementation is separately gated  
**Priority:** `P2`  
**Known issue:** #17

Maintain separation between neutral scoped semantic conformance and current Event/reducer/Claim fixtures.

## 6. Research candidates

Residual A10 research targets remain:

- `A10-H03` — representation migration continuity;
- `A10-H10` — storage × computation independence;
- `A10-H06` — logical / cryptographic / physical erasure lanes;
- `A10-H09` — probabilistic bounded statistical conformance;
- `A10-H08` — non-address-based physical continuity with anti-shadow controls.

**State for all five:** `NOT_AUTHORIZED` for implementation/execution unless separately selected, preregistered and admitted.

RAVP-001 records the recommended research order:

`H11 → H03 → H10 → H06 → H09 → H08`

This is planning guidance only. Completion of one family does not authorize the next.

For each future research family, require at minimum:

- hypothesis;
- current evidence;
- alternative explanations;
- bounded experiment;
- falsification/refutation condition;
- non-goals;
- decision rule;
- explicit independence requirements;
- separate preregistration/admission/authorization as applicable.

## 7. Deferred work

- Final Canon selection/freeze — `DEFERRED`, operator decision.
- Runtime thaw — `DEFERRED`, separate operator decision after relevant evidence/Canon decisions; never automatic.
- Production authorization — `DEFERRED`, separate decision; never inferred from research completion.
- Composition/federation conformance — separate capability class; not H11.
- Quantum/non-classical substrate claims — open research question; no compatibility claim is presumed.

## 8. Blocked work

- H11 execution — blocked on a qualifying independent reviewer/reproducer and subsequent separate admission reassessment.
- Track H authentic historical recovery — blocked on operator-controlled source availability/admission.

Do not relabel blocked pre-execution H11 as `INDETERMINATE`; the current outcome is `NOT_TESTED`.

## 9. Explicitly non-authorized directions

Unless live authority changes explicitly, do not start:

- H11 implementation/execution or semantic adjudication while admission is blocked;
- H03/H10/H06/H09/H08 implementation/execution merely because they are listed here;
- reducer-v2/new semantic Event verbs without operator decision;
- new product DB/language/model/hardware profile as an architecture conclusion;
- new runtime integration;
- Final Canon promotion;
- runtime thaw;
- production authorization;
- license selection;
- Track H source admission;
- physical/cryptographic erasure claims unsupported by their required evidence.

## 10. Known risks / technical debt

- Treating reference-laboratory mechanisms as universal architecture.
- Conflating `Claim` with truth, or Unknown with False.
- Treating CI/AI/owner review as independent qualification.
- Treating outreach `SENT` as delivery, response or qualification.
- Rewriting historical reducer semantics instead of versioning a future policy.
- Overclaiming deletion/erasure beyond observable threat-scoped evidence.
- Treating public repository visibility as a license decision.
- Treating recommended research order as automatic execution routing.
- Treating residual-family completion as predetermined Final Canon.

## 11. Governance / operational work

Routine documentation, provenance, integrity, evidence preservation and truth-surface maintenance may be allowed while runtime is frozen, but every write must follow the current `AGENTS.md` write-authorization gate.

Before any repository/Notion mutation, establish exact source evidence, challenged wording/state, controlling authority, smallest proposed change set, why it is maintenance rather than a reserved semantic decision, validation/read-back plan and explicit operator approval for the exact bounded set.

## 12. Suggested audit order

For a future fresh audit, use this order without treating it as work authorization:

1. live `main`, signature, PRs, reviews, issues and Actions;
2. `project-state.json` and current machine gate;
3. H11 qualification/admission contract and PR #131;
4. current architecture authority route through IAR-1-R1;
5. open issues #1, #14, #15, #16, #17, #18, #74, #88;
6. RAVP-001 residual targets and whether any state/authorization changed;
7. existing Notion surfaces only when synchronization/reconciliation is in scope.

## 13. Handoff protocol

When an external H11 response arrives:

```text
response received
→ classify as contact/interest/candidate evidence
→ bind authenticated identity and declarations to repository-visible evidence
→ evaluate the existing machine qualification contract
→ if QUALIFIED, separately reassess execution admission
→ only if admitted, execute the frozen H11 scope
```

Do not create a new H11 procedure unless the existing contract is proven defective and an exact bounded governance change is separately authorized.

For general future work:

```text
fresh live audit
→ reconcile this ledger
→ classify item
→ reproduce suspected defects before selecting fixes
→ resolve architecture decisions before code
→ obtain exact authorization
→ execute one bounded scope
→ validate/read back
→ update this ledger only if durable orientation changed
```

## 14. Historical DONE items

For orientation only; verify Git history if exact evidence is needed:

- A1–A10 first-draft architecture documents drafted: `10/10`; this does not mean Final Canon.
- Integrated A1–A10 review, IAR-1 and IAR-1-R1 reconciliation completed for their declared scope.
- BPV-1 and its recorded follow-up review/synchronization stages completed for bounded scope.
- RAVP-001 planning completed; experiment execution was not authorized by planning.
- A10-H11 selected and preregistered.
- H11 admission package implemented fail-closed and current state bound as blocked.
- H11 contract technical remediation completed while preserving the frozen subject.
- Bounded internal truth-surface/governance remediation through PR #147 completed.

## 15. Update rules

Update this ledger only when durable orientation changes. Do not use it as a volatile live-HEAD log.

For each future item update, preserve:

- state;
- priority if useful;
- implementation authorization separately;
- runtime capability impact separately;
- last-verified evidence/checkpoint;
- question and evidence;
- required audit/reproduction/experiment;
- authority boundaries;
- exit criteria;
- allowed outcomes.

If live evidence contradicts this ledger, live repository truth and the repository's authority routing win. Mark the ledger entry stale and update it only through the current write-authorization process.
