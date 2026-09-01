# ADR-0028 — H11 hybrid two-basis positive reviewer/reproducer qualification

- **Status:** ACCEPTED / OPERATOR APPROVED
- **Date:** 2026-08-22
- **Issue:** #154
- **Selected option:** `OPTION_C_HYBRID_TWO_BASIS`
- **Implementation at decision time:** `NOT_STARTED`
- **Current bounded implementation:** `IMPLEMENTED / NO_CANDIDATE_EVALUATED` via Issue #163 / PR #164
- **H11 reviewer/reproducer:** `NOT_ESTABLISHED`
- **A10_H11_EXECUTION_ADMISSION:** `BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER`
- **H11:** `NOT_TESTED`
- **Runtime:** `FROZEN`
- **Final Canon:** `DEFERRED / NOT AUTHORIZED`
- **Production:** `NOT AUTHORIZED`

## Current implementation overlay — 2026-08-23

ADR-0028's decision remains unchanged. The bounded follow-up implementation tracked by Issue #163 and PR #164 now materializes the selected design as a pre-admission qualification mechanism:

- sufficient-evidence policy: `nk-h11-positive-qualification-policy/1`;
- evaluation request: `nk-h11-positive-qualification-request/1`;
- candidate-neutral evaluator result: `nk-h11-positive-qualification-evaluation/1`;
- candidate review surface: authenticated GitHub pull-request review on PR #131;
- second basis: separately verifiable organizational-separation and independent-evidence-custody attestations from distinct external public Organization-owned repositories and distinct authenticated organization-associated issuers;
- exact frozen plan/digest, event-ID, freshness, authorship, custody, conflict, frozen-input and private-state checks;
- fail-closed policy-weakening and adversarial tests.

This is a **narrow H11 reviewer-role sufficient-evidence policy**, not KYC, legal-identity proof, employment verification, a general PKI system, execution admission, or H11 execution authority.

No candidate has been evaluated under this implementation. Therefore the authoritative semantic state remains:

```yaml
positive_qualification_implementation: IMPLEMENTED / NO_CANDIDATE_EVALUATED
qualifying_reviewer_reproducer: NOT_ESTABLISHED
A10_H11_EXECUTION_ADMISSION: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER
H11: NOT_TESTED
runtime: FROZEN
Final_Canon: DEFERRED / NOT_AUTHORIZED
production: false
```

A future `QUALIFIED` evaluator result is a mandatory stop condition and can route only to a separate `A10_H11_EXECUTION_ADMISSION` reassessment. It cannot itself execute H11 or change any authority boundary.

## Context

Native Kernel's H11 qualification machinery intentionally prevents repository-local self-certification. The qualification vocabulary and structural checks can represent `QUALIFIED`, `NOT_ESTABLISHED`, and `DISQUALIFIED`, but a positive-candidate path must bind externally authenticated evidence without collapsing authentication, organizational separation, custody independence, qualification, execution admission, or H11 execution into one claim.

A real external candidate therefore cannot become `QUALIFIED` merely by appearing on PR #131 or by providing repository-local assertions. Authentication, real-world identity, organizational separation, independent custody, qualification, execution admission, and H11 execution are distinct claims.

## Decision

Adopt a **hybrid two-basis positive qualification path** for any future H11 reviewer/reproducer candidate.

A positive qualification MAY be considered only when both evidence bases are present and mutually consistent:

1. **Authenticated GitHub basis** — a distinct external candidate acts through an authenticated GitHub account on the repository-visible H11 review surface and provides a structured H11 reviewer/reproducer declaration.
2. **Independent second basis** — a separate repository-visible and independently verifiable evidence basis supports the claimed organizational separation and independent evidence custody under a narrow versioned sufficient-evidence policy.

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

The bounded implementation must version and define at minimum:

- accepted forms of authenticated GitHub candidate action;
- the structured reviewer/reproducer declaration fields;
- accepted categories for the second evidence basis;
- what makes that second basis independently verifiable;
- minimum evidence required for authorship independence;
- minimum evidence required for organizational/custody independence;
- treatment of conflicts, shared custody, material dependence, aliases and uncertainty;
- repository-visible evidence-reference and binding rules;
- contradiction handling;
- exact transition conditions for `QUALIFIED`, `NOT_ESTABLISHED`, and `DISQUALIFIED`;
- candidate-neutral evaluation rules;
- fail-closed behavior for missing, ambiguous, unverifiable, stale or contradictory evidence.

Issue #163 / PR #164 materializes this contract through the three versioned protocols listed in the current implementation overlay. The sufficient-evidence policy remains narrow; Native Kernel does not grow a general identity, KYC, PKI or organization-verification subsystem merely to satisfy H11.

## Minimum fail-closed semantics

The evaluator must not produce a positive qualification when any of the following is true:

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

Evidence establishing disqualifying self-review, prohibited authorship/custody conditions, or materially false/contradictory declarations may resolve to `DISQUALIFIED` under the versioned policy.

## Authority separation

This ADR establishes the contract direction for the positive qualification path. The bounded follow-up implementation does not broaden that authority.

It does **not**:

- qualify any current or future candidate by itself;
- make the current Codex/ChatGPT review qualifying;
- treat another model/session/agent label as independent;
- change PR #131 into qualification evidence by itself;
- execute H11;
- change `A10_H11_EXECUTION_ADMISSION` automatically;
- authorize dependency-graph execution or semantic adjudication;
- authorize reducer-v2;
- thaw runtime;
- promote Final Canon;
- authorize production;
- decide Issue #18 licensing.

```text
qualification design
!= qualification implementation

qualification implementation
!= qualification

qualification
!= execution admission

execution admission
!= H11 execution

H11 outcome
!= Final Canon
```

## Implementation boundary

At ADR acceptance, implementation was explicitly `NOT_STARTED` and required a separate bounded PR.

Issue #163 / PR #164 now implements that bounded slice while preserving all original requirements:

1. the versioned sufficient-evidence policy and positive-candidate schema/evaluator are explicit;
2. the frozen H11 plan and leakage rubric are unchanged;
3. `NOT_ESTABLISHED / BLOCKED / NOT_TESTED` remains authoritative until real qualifying evidence exists;
4. negative/adversarial fixtures prove fail-closed behavior and policy weakening is rejected;
5. H11 is not executed;
6. qualification cannot automatically mutate execution admission.

The implementation status therefore advances to `IMPLEMENTED / NO_CANDIDATE_EVALUATED`, while H11 authority does not advance.

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

Not selected as the desired design direction. The actual H11 gate nevertheless remains blocked until a genuinely qualifying external candidate is evaluated and a later separate execution-admission reassessment authorizes H11.

## Rollback / supersession

If the selected path proves too weak, too complex or operationally unworkable before H11 execution, a later ADR may supersede this qualification design.

Such supersession must not reinterpret prior non-qualification records as qualification and must not retroactively change the frozen H11 evidence identity.

## Consequences

### Positive

- removes ambiguity about how a future positive candidate should be authenticated and evidenced;
- keeps self-certification fail-closed;
- avoids making GitHub identity the sole independence proof;
- avoids building a general-purpose identity platform;
- preserves the distinction between qualification and execution authority;
- after Issue #163 / PR #164, removes the remaining owner-side implementation dependency before a real external candidate can be evaluated.

### Cost

- an actual external candidate and two independent evidence bases remain required;
- live evidence must satisfy the bounded policy at evaluation time;
- H11 remains blocked until qualification and a later separate execution-admission reassessment both succeed.

## Current state

```yaml
issue_154: CLOSED / DECISION COMPLETE
adr_0028: ACCEPTED / OPTION_C_HYBRID_TWO_BASIS
positive_qualification_implementation: IMPLEMENTED / NO_CANDIDATE_EVALUATED
qualifying_reviewer_reproducer: NOT_ESTABLISHED
A10_H11_EXECUTION_ADMISSION: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER
H11: NOT_TESTED
runtime: FROZEN
Final_Canon: DEFERRED / NOT_AUTHORIZED
production: false
next_dependency: ESTABLISH_GENUINELY_EXTERNAL_CANDIDATE_THEN_EVALUATE_ADR0028_QUALIFICATION
```
