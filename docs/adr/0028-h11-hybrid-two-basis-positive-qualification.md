# ADR-0028 — H11 hybrid two-basis positive reviewer/reproducer qualification

- **Status:** ACCEPTED / OPERATOR APPROVED
- **Date:** 2026-08-22
- **Issue:** #154
- **Selected option:** `OPTION_C_HYBRID_TWO_BASIS`
- **Implementation:** `NOT_STARTED`
- **H11 reviewer/reproducer:** `NOT_ESTABLISHED`
- **A10_H11_EXECUTION_ADMISSION:** `BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER`
- **H11:** `NOT_TESTED`
- **Runtime:** `FROZEN`
- **Final Canon:** `DEFERRED / NOT AUTHORIZED`
- **Production:** `NOT AUTHORIZED`

## Context

Native Kernel's current H11 qualification machinery intentionally prevents repository-local self-certification. The existing qualification vocabulary and structural checks can represent `QUALIFIED`, `NOT_ESTABLISHED`, and `DISQUALIFIED`, but the current repository state does not define a generic positive-candidate path that can safely bind externally authenticated independence evidence.

A real external candidate therefore cannot become `QUALIFIED` merely by appearing on PR #131 or by providing repository-local assertions. Authentication, real-world identity, organizational separation, independent custody, qualification, execution admission, and H11 execution are distinct claims.

## Decision

Adopt a **hybrid two-basis positive qualification path** for any future H11 reviewer/reproducer candidate.

A positive qualification MAY be considered only when both evidence bases are present and mutually consistent:

1. **Authenticated GitHub basis** — a distinct external candidate acts through an authenticated GitHub account on the repository-visible H11 review surface and provides a structured H11 reviewer/reproducer declaration.
2. **Independent second basis** — a separate repository-visible and independently verifiable evidence basis supports the claimed organizational separation and/or independent evidence custody under a narrow versioned sufficient-evidence policy.

Neither basis is sufficient alone.

```text
GitHub authenticated actor alone
!= qualifying independence

second evidence basis alone
!= qualifying independence

basis 1 + basis 2
+ authorship separation
+ custody separation where required
+ conflict/material-dependence disclosure
+ frozen-input compliance
+ private-state exclusion
+ no contradictory evidence
= candidate eligible for qualification evaluation
```

Eligibility for evaluation is not itself `QUALIFIED`.

## Required positive-qualification contract

Before implementation, the follow-up bounded contract must version and define at minimum:

- accepted forms of authenticated GitHub candidate action;
- the structured reviewer/reproducer declaration fields;
- accepted categories for the second evidence basis;
- what makes that second basis independently verifiable;
- minimum evidence required for authorship independence;
- minimum evidence required for organizational/custody independence;
- treatment of conflicts, shared custody, material dependence, aliases and uncertainty;
- repository-visible evidence-reference and digest/binding rules;
- contradiction handling;
- exact transition conditions for `QUALIFIED`, `NOT_ESTABLISHED`, and `DISQUALIFIED`;
- candidate-neutral evaluation rules;
- fail-closed behavior for missing, ambiguous, unverifiable, stale or contradictory evidence.

The sufficient-evidence policy must remain narrow. Native Kernel must not grow a general identity, KYC, PKI or organization-verification subsystem merely to satisfy H11.

## Minimum fail-closed semantics

A future evaluator must not produce a positive qualification when any of the following is true:

- only owner/self evidence exists;
- the candidate is the author of the frozen H11 preregistration/rubric;
- material implementation/profile/laboratory custody is shared where the accepted policy requires separation;
- unresolved conflicts or material dependence exist;
- evidence is repository-local and self-assertable only;
- either of the two required bases is missing;
- the two bases contradict each other;
- private implementation state was materially used;
- the frozen-input boundary was violated;
- evidence identity or provenance cannot be bound deterministically.

Ambiguity resolves to `NOT_ESTABLISHED`, not `QUALIFIED`.

Evidence establishing disqualifying self-review, prohibited authorship/custody conditions, or materially false/contradictory declarations may resolve to `DISQUALIFIED` under the future versioned policy.

## Authority separation

This ADR establishes only the contract direction for building a future positive qualification path.

It does **not**:

- qualify any current or future candidate;
- make the current Codex review qualifying;
- treat another model/session/agent label as independent;
- change PR #131 into qualification evidence;
- execute H11;
- change `A10_H11_EXECUTION_ADMISSION`;
- authorize dependency-graph execution or semantic adjudication;
- authorize reducer-v2;
- thaw runtime;
- promote Final Canon;
- authorize production;
- decide Issue #18 licensing.

```text
qualification design
!= qualification

qualification
!= execution admission

execution admission
!= H11 execution

H11 outcome
!= Final Canon
```

## Implementation boundary

Implementation is explicitly `NOT_STARTED`.

Any implementation requires a separate bounded PR that:

1. defines the versioned sufficient-evidence policy and positive-candidate schema/evaluator;
2. preserves the current frozen H11 plan and leakage rubric;
3. preserves the current `NOT_ESTABLISHED / BLOCKED / NOT_TESTED` record until real qualifying evidence exists;
4. adds negative/adversarial fixtures proving fail-closed behavior;
5. does not execute H11;
6. does not automatically mutate execution admission after qualification.

## Qualification-to-admission transition

If a future candidate is evaluated as `QUALIFIED`, the repository must stop at that result and perform a **separate** `A10_H11_EXECUTION_ADMISSION` reassessment.

No evaluator or qualification record may automatically authorize H11 execution.

## Alternatives considered

### OPTION A — GitHub-native authenticated review only

Rejected as insufficient by itself because authenticated account control does not prove organizational independence or independent custody.

### OPTION B — external signed attestation only

Not selected because it risks creating unnecessary trust/issuer infrastructure and still requires policy decisions about what the attestation proves.

### OPTION C — hybrid two-basis path

**Selected.** It combines a repository-native authenticated action with a second independently verifiable evidence basis while allowing the sufficient-evidence policy to remain small and purpose-specific.

### OPTION D — remain blocked indefinitely

Not selected as the desired direction. However the actual H11 gate remains blocked until this ADR is implemented and a genuinely qualifying external candidate is established.

## Rollback / supersession

If the selected path proves too weak, too complex or operationally unworkable before H11 execution, a later ADR may supersede this qualification design.

Such supersession must not reinterpret prior non-qualification records as qualification and must not retroactively change the frozen H11 evidence identity.

## Consequences

### Positive

- removes ambiguity about how a future positive candidate should be authenticated and evidenced;
- keeps self-certification fail-closed;
- avoids making GitHub identity the sole independence proof;
- avoids building a general-purpose identity platform;
- preserves the distinction between qualification and execution authority.

### Cost

- a narrow sufficient-evidence policy and positive evaluator still need a separate implementation slice;
- an actual external candidate remains required;
- H11 remains blocked until both are satisfied.

## Current state after this decision

```yaml
issue_154: OPERATOR_OPTION_SELECTED
adr_0028: ACCEPTED / OPTION_C_HYBRID_TWO_BASIS
positive_qualification_implementation: NOT_STARTED
qualifying_reviewer_reproducer: NOT_ESTABLISHED
A10_H11_EXECUTION_ADMISSION: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER
H11: NOT_TESTED
runtime: FROZEN
Final_Canon: DEFERRED / NOT_AUTHORIZED
production: false
```
