<!-- H11_EXECUTION_ADMISSION_BLOCKED_CURRENT -->
# ⚠️ Native Kernel Known Risks and Required Proof

This file is the **active-risk register**. Historical defect chronology remains in its original reviews, research/evidence records, `STATUS.md`, `ROADMAP.md`, work/reconciliation logs and Git history; current risks must not be lost merely to make the document shorter.

```yaml
document_role: ACTIVE_RISKS
status_as_of: 2026-08-23
authoritative_machine_source: ../../project-state.json
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
selected_family: A10-H11
current_gate: A10_H11_EXECUTION_ADMISSION
admission: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER
reviewer_reproducer: NOT_ESTABLISHED
h11_outcome: NOT_TESTED
positive_qualification_design: ADR-0028 / OPTION_C_HYBRID_TWO_BASIS
positive_qualification_implementation: IMPLEMENTED / NO_CANDIDATE_EVALUATED
runtime_expansion: FROZEN
production_authorized: false
```

## Risk-state vocabulary

```text
OPEN                 unresolved technical, governance or evidence risk
MITIGATED            bounded control exists; residual risk remains
CLOSED               exact finding corrected and repository-verified
HISTORICAL_BOUNDARY  retained evidence remains valid only for original version/scope
PROPOSED             research or decision work, not runtime protection
```

## 🔴 P0 — False independence / self-certification

**State:** `OPEN / CURRENT H11 BLOCKER`.

H11 requires a genuinely qualifying `INDEPENDENT_SEMANTIC_ORACLE`. The current Codex qualification record remains `NOT_ESTABLISHED`; shared-custody/self-review and organizational-independence concerns remain material.

```text
CI success ≠ independent review
owner/self review ≠ independent review
LLM agreement / model-session change / same-agent relabeling ≠ independent review
Notion read-back ≠ independent review
implemented evaluator ≠ independent reviewer
```

PR #131 remains the external review surface. ADR-0028 is now operationally materialized by a narrow positive-qualification policy/request/evaluator, but **no candidate has been evaluated** and no external evidence has been established. A future candidate must satisfy both independent evidence bases. Even if the evaluator returns `QUALIFIED`, the repository must stop and separately reassess `A10_H11_EXECUTION_ADMISSION` before any H11 execution.

## 🔴 P0 — Formal Authority misrouting / stale first-draft interpretation

**State:** `MITIGATION IN PROGRESS / MUST REMAIN FAIL-CLOSED`.

A1–A10 are preserved first-draft provenance, while IAR-1-R1 deliberately narrows several first-draft structures. A reading route that stops at A1–A10 can therefore overstate the current provisional architecture.

```text
ARCHITECTURE.md
→ A1–A10 first-draft provenance
→ Integrated A1–A10 Review
→ IAR-1
→ IAR-1-R1 reconciliation
→ later accepted ADR / operator decisions for their explicit scope
```

Where first-draft wording conflicts with IAR-1-R1, the reconciliation is the current provisional interpretation. Final Canon remains deferred.

## 🔴 P0 — Historical/current state confusion

**State:** `MITIGATION IN PROGRESS`.

Historical D5/D6/D7/D8, ADR-0027, RAVP, family-selection and preregistration records contain values that were once current. Requiring those exact literals inside current-only AI surfaces creates a retrieval hazard even when a newer overlay exists.

```text
historical NEXT ≠ current next gate
historical NOT_STARTED ≠ current state
old Notion checkpoint ≠ live GitHub HEAD
```

Current-only surfaces must carry current H11 state; chronology remains in designated history/evidence surfaces.

## 🔴 P0 — Production overclaim

**State:** `OPEN / PRIMARY COMMUNICATION AND GOVERNANCE RISK`.

```text
C5 + BPV1 scoped evidence
≠ production deployment
≠ live user traffic
≠ sustained operations
```

Production authorization remains `false`.

## 🔴 P0 — Semantic assertion overclaim

**State:** `OPEN`.

```text
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
assertion map:              45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:                     0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
```

Operational success and scoped BPV1/A10 evidence cannot promote unsupported assertions or universalize bounded findings.

## 🔴 P0 — Reference implementation may capture architecture authority

**State:** `MITIGATED / RESIDUAL OPEN`.

Controls already present:

- P1–C5 remains `BOUNDED_REFERENCE_LABORATORY`;
- A1–A10 remains provisional first-draft provenance;
- IAR-1-R1 demotes over-shaped taxonomies from universal minimum to reference structures;
- BPV1/H11 separate profile mechanisms from meaning-level obligations;
- runtime remains frozen;
- Final Canon remains deferred.

Residual risk remains because the same repository and conventional-digital machinery dominate most evidence. One cross-language realization is not independent-computation-model proof.

## 🔴 P0 — Oracle leakage / post-hoc rescoping

**State:** `MITIGATED / MUST REMAIN FAIL-CLOSED`.

Frozen preregistration, scenario identity, mandatory obligations, expected fixture semantics, thresholds and hard-refutation conditions cannot be changed post-execution to rescue a result under the same evidence identity. A semantic change requires the appropriate new admitted evidence/scenario identity.

## 🔴 P0 — Bounded accountability boundary

**State:** `MITIGATED FOR BPV1 FIXED SCOPE / RESIDUAL OPEN OUTSIDE SCOPE`.

The fixed 512-mutation BPV1 run preserves current accountability, explicit retention scope and loss witnesses within its preregistered bounds. Additional engineering stress tests exercise bounded witness retention.

This is not proof of bounded behavior for arbitrary workloads, distributions or future substrates.

## 🔴 P0 — Bounded-state thresholds may be misleading

**State:** `MITIGATED FOR FIXED BPV1 SCOPE / RESIDUAL OPEN`.

Recorded BPV1 thresholds and observations are experiment parameters/evidence, not universal architecture constants, capacity/SLO claims or performance targets.

## 🔴 P0 — Semantic corruption coverage is scoped

**State:** `MITIGATED FOR BPV1 CLAIM FIELDS / RESIDUAL OPEN`.

Corrective tests cover corruption of evidence/epistemic-position fields for the bounded BPV1 evidence path. The local digest remains an experiment corruption detector, not a universal cryptographic authenticity scheme.

## 🔴 P0 — Threat/authenticity boundary remains provisional

**State:** `MITIGATED FOR PREREGISTERED NEGATIVE FIXTURES / RESIDUAL OPEN`.

Scoped negative fixtures cover selected corruption, forged-Authority and withheld-counterevidence cases. They do not establish OS security, distributed consensus, key management, independent custody, cryptographic authenticity or arbitrary adversarial resilience.

## 🔴 P0 — Context / Provenance / Authority grounding can hide assumptions

**State:** `OPEN / SCOPED EVIDENCE ONLY`.

The reconciled architecture requires finite/declared grounding where these relations are material. Existing fixtures do not exhaust grounding problems across all knowledge systems or substrates.

## 🔴 P0 — Historical and clean lineages may be collapsed

**State:** `OPEN / GOVERNANCE BOUNDARY`.

```text
clean P1–P5 + C4 + C5
≠ recovered v0.1.2.1
≠ original 44-test evidence
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
```

Issue #1 remains independent. Track H source admission remains operator-controlled.

## 🔴 P0 — Reducer referential semantics remain incomplete

**State:** `OPEN / ISSUE #74 CLOSED / ADR-0024 ACCEPTED / IMPLEMENTATION NOT_STARTED / RUNTIME FROZEN`.

Reducer v1 historically permits referential cases a stricter future policy may reject, including dangling/unknown references and insufficiently constrained supersession relations.

The operator selected `ACCEPT_WITH_CHANGES` on 2026-08-22. ADR-0024 freezes the future versioned referential contract direction while preserving reducer v1 as an immutable historical contract. Issue #74 is complete as a decision gate, but the implementation risk remains open: reducer-v2 implementation is `NOT_STARTED` and reducer-v2 runtime remains `NOT_AUTHORIZED`.

Do **not** repair reducer v1 in place; that would reinterpret historical P1–C5 evidence. Any stricter implementation must use a separately authorized reducer-v2 path and new evidence identity under the accepted ADR-0024 boundary.

### RVT-01 — reducer-v1 evidence-lineage boundary

A bounded read-only trace on 2026-08-21 found that the current C3 support evidence is materially produced under reducer-v1 permissive referential semantics:

```text
27 / 45 SUPPORTED → direct evidence-path coupling to C3 workload/replay containing dangling LINK and/or SUPERSEDED targets
16 / 45 SUPPORTED → indirect artifact-generation coupling through P4/P5 profile-report compatibility
 2 / 45 SUPPORTED → no assertion-level referential-workload dependency
45 / 45 current C3 artifact pipeline → operationally produced with reducer-v1 profile reports
```

This trace did **not** show that any current SUPPORTED assertion is semantically false, did **not** reproduce `Unknown → False`, and does **not** change the `45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED` map. The narrower gap is that referential absence can remain unclassified by reducer v1 rather than being materialized as an explicit `UNKNOWN` / provenance-gap state.

Therefore existing C3/C4/C5 support is **historical reducer-v1-bounded evidence**. It must not be silently reused as proof of a future strict-referential / reducer-v2 policy. A future reducer version requires its own admitted fixtures/evidence cycle.

## 🔴 P0 — Event/history commitment is not complete authenticity

**State:** `OPEN`.

```text
hash chain ≠ complete authenticity
signature over incomplete commitment ≠ complete integrity
history visibility ≠ mandatory Event sourcing
```

The reconciled architecture no longer treats Event-log-shaped history or exact replay as universal minimum requirements. Existing Event-integrity evidence remains profile-scoped.

## 🔴 P0 — Physical / cryptographic erasure is not established

**State:** `OPEN`.

Logical restriction/`ERASED` does not prove physical deletion, cryptographic erasure or global forgetting.

The reconciled architecture distinguishes:

1. logical disposition claim;
2. substrate-condition claim under a threat/observation boundary;
3. epistemic accessibility / forgetting-loss claim.

Do not upgrade one layer into another without required evidence and Authority.

## 🔴 P0 — License and contribution rights are unresolved

**State:** `OPEN / ISSUE #18 / OPERATOR DECISION REQUIRED`.

```text
publicly readable repository ≠ permission to copy, modify or redistribute
```

No AI agent may choose the license, contribution regime, patent/trademark terms or recovered-source rights for the operator.

## 🔴 P0 — Research may be mistaken for authorization

**State:** `OPEN / GOVERNANCE BOUNDARY`.

Qualifying review, reconciliation, preregistration, execution admission, bounded support or later A10 outcomes do not automatically create Final Canon, product runtime behavior, production authority or universal substrate claims.

## 🟠 P1 — H11 positive qualification implementation complete; external evidence remains absent

**State:** `IMPLEMENTED / NO_CANDIDATE_EVALUATED / EXTERNAL DEPENDENCY OPEN`.

ADR-0028, merged via PR #155 at `4a13d2b4ee8001a43f7e3e701dbe9025dbcfd0df`, selected `OPTION_C_HYBRID_TWO_BASIS`. Issue #163 / PR #164 now materializes the bounded pre-admission path as:

- `nk-h11-positive-qualification-policy/1`;
- `nk-h11-positive-qualification-request/1`;
- `nk-h11-positive-qualification-evaluation/1`;
- live GitHub event/repository verification;
- fail-closed adversarial fixtures and policy-weakening guards.

A positive qualification requires both:

1. a distinct authenticated GitHub candidate review/declaration on PR #131; and
2. separate repository-visible organizational-separation and independent-evidence-custody attestations from distinct external public Organization-owned repositories and distinct authenticated organization-associated issuers.

Neither basis is sufficient alone. Missing, stale, malformed, ambiguous, contradictory or non-distinct evidence resolves to `NOT_ESTABLISHED`; prohibited owner/self review, preregistration/rubric authorship, same custody, private-state use or frozen-input violation can resolve to `DISQUALIFIED`.

The implementation is deliberately narrower than KYC or a general identity subsystem. It establishes only whether repository-visible evidence is sufficient for the bounded H11 reviewer/reproducer role under ADR-0028.

```text
authenticated account/action ≠ legal/real-world identity proof
bounded sufficient evidence ≠ universal organizational-independence proof
implementation ≠ qualification
qualification ≠ execution admission
execution admission ≠ H11 execution
```

No candidate has been evaluated. The authoritative reviewer state remains `NOT_ESTABLISHED`; H11 admission remains `BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER`; H11 remains `NOT_TESTED`.

A future `QUALIFIED` result is a hard **STOP**: the evaluator keeps every authority flag false and routes only to `SEPARATE_A10_H11_EXECUTION_ADMISSION_REASSESSMENT`.

## 🟠 P1 — Independent implementation evidence remains limited

**State:** `PARTIAL / CROSS-LANGUAGE EVIDENCE EXISTS / BROADER INDEPENDENCE ABSENT`.

```text
independent team: NOT_ESTABLISHED
independent custody: NOT_ESTABLISHED
independent computation model: NOT_ESTABLISHED / CONVENTIONAL_DIGITAL
```

Cross-language evidence is materially useful but cannot be described as fully independent merely because the language differs.

## 🟠 P1 — Composition/federation remains outside base conformance

**State:** `OPEN / SEPARATE CAPABILITY CLASS`.

```text
local scoped conformance ≠ federation/composition conformance
A10-H11 ≠ composition/federation
```

Do not import composition authority or mechanisms from Titan, Crystal, Mentaury or another project into Native Kernel.

## 🟠 P1 — Operational equivalence remains absent

**State:** `OPEN`.

PostgreSQL↔SQLite bounded semantic comparison is not full operational equivalence. BPV1 does not prove performance/operational parity.

## 🟠 P1 — Durable evidence lacks independent custody

**State:** `MITIGATED / RESIDUAL OPEN`.

Repository-resident C5/BPV1 artifacts are not independent third-party custody, signed timestamping or disaster recovery.

## 🟠 P1 — Scale and environment scope remain narrow

**State:** `OPEN`.

Passing C5/BPV1 bounds is not a capacity, SLO, cost, hardware-portability or universal substrate claim.

## 🟠 P1 — Evidence/checkpoint identity can be misread after squash merges

**State:** `MITIGATED / RESIDUAL PROCESS RISK`.

PR #138 repaired one post-squash evidence anchor. Preserve the distinction:

```text
pre-merge candidate identity: exact PR head
post-merge authoritative repository identity: main-reachable merge/commit + verified bytes/digest
```

A PR-head SHA must not silently become the durable main-reachable evidence anchor after a squash merge.

## 🟠 P1 — Current-state / Notion surfaces can drift

**State:** `OPEN / DOCUMENTATION PROCESS RISK`.

GitHub refs, PRs, Actions and Notion can change after committed snapshots. Notion is a human/navigation projection, not stronger authority than GitHub.

Different Notion pages have different roles; copying one volatile live SHA/gate block across all pages creates churn and stale truth. Use role-specific updates and read-back:

```text
Hub → stable portrait/navigation
Core Architecture → architecture meaning/invariants
Current State → current state projection
Roadmap → active gate/order
Active Risks → active risk register
AI Context → continuation/routing
Decision Ledger → operator/ADR decision projection
GitHub Sync Log → PR/SHA/CI synchronization chronology
```

The ADR-0028 design projection has a previous 8/8 read-back. The positive-qualification implementation requires a new post-merge update/read-back of the same eight existing pages; it must not create a ninth page or reinterpret the frozen H11 state-binding checkpoint.

## 🟠 P1 — Repository governance enforcement can be weaker than methodology

**State:** `OPEN / SEPARATE FROM RESEARCH SEMANTICS`.

The active default-branch ruleset requires PR-based integration and protects destructive/non-fast-forward changes. Required status checks/review/thread-resolution policy may still be weaker than the repository's methodological discipline.

This is governance hardening, not evidence that BPV1/H11 semantics failed.

## 🟡 P2 — Local SQLite environment may be unable to execute P5 safely

**State:** `EXPECTED ENVIRONMENT LIMITATION / NOT A REASON TO LOWER THE SAFETY FLOOR`.

The SQLite profile intentionally fails closed below the evidenced WAL-safe floor. CI builds the pinned safe SQLite version. A local environment with older linked SQLite may be `NOT_EXECUTED` for affected P5 tests rather than a Kernel regression.

Do not weaken the WAL safety floor merely to make an unsafe local environment green.

## Closed / historical boundaries

Historical Event-comparison, evidence-schema, workflow-trigger, SQLite-version, D5 subject-self-report, semantic-digest coverage, witness-retention and H11 validation-bypass defects remain preserved in their original PR/review/evidence histories. Later remediation adds a new evidence/validation identity rather than rewriting old evidence.

## Required non-claims

```text
bounded evidence ≠ universal proof
cross-language ≠ independent computation model
repository-visible ≠ independent custody
logical ERASED ≠ physical deletion
physical deletion ≠ global forgetting
Final Canon deferred ≠ architecture absent
runtime frozen ≠ research stopped
Notion synchronized ≠ H11 qualified
CI green ≠ independent validation
ADR-0028 accepted ≠ reviewer qualified
positive qualification implemented ≠ reviewer qualified
qualification ≠ execution admission
execution admission ≠ H11 execution
```

## Update rule

For every risk transition record exact governing contract/decision, exact evidence identity, residual risk, proof boundary and whether operator approval is required. Do not convert a bounded PASS, closed defect, accepted research priority, operator approval, qualifying review, reconciliation, preregistration or scoped experiment result into production, truth, compliance, deletion, Final Canon, universal neutrality, future-substrate support or ecosystem-authority claims.
