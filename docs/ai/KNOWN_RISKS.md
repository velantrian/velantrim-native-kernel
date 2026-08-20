<!-- H11_EXECUTION_ADMISSION_BLOCKED_CURRENT -->
# ⚠️ Native Kernel Known Risks and Required Proof

This file is the **active-risk register**. Historical defect chronology remains in its original reviews, research/evidence records, `STATUS.md`, `ROADMAP.md`, work/reconciliation logs and Git history; current risks must not be lost merely to make the document shorter.

```yaml
document_role: ACTIVE_RISKS
status_as_of: 2026-08-15
authoritative_machine_source: ../../project-state.json
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
selected_family: A10-H11
current_gate: A10_H11_EXECUTION_ADMISSION
admission: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER
reviewer_reproducer: NOT_ESTABLISHED
h11_outcome: NOT_TESTED
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
```

PR #131 remains the external review surface. A future qualifying reviewer/reproducer still requires a separate `A10_H11_EXECUTION_ADMISSION` reassessment before execution.

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

**State:** `OPEN / ISSUE #74 / ADR-0024 PENDING / RUNTIME FROZEN`.

Reducer v1 historically permits referential cases a stricter future policy may reject, including dangling/unknown references and insufficiently constrained supersession relations.

Do **not** repair reducer v1 in place; that would reinterpret historical P1–C5 evidence. Any stricter semantics must use the existing operator-controlled versioning/ADR path.

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

## 🟠 P1 — H11 qualification evidence must be operationally bindable

**State:** `OPEN / PRE-EXECUTION OPERATIONAL RISK`.

The fail-closed qualification contract correctly prevents repository-local self-certification. When a genuine external reviewer/reproducer appears, externally authenticated identity/evidence must be bindable into the **existing** qualification record without weakening frozen criteria.

Current machine nuance:

- the existing qualification vocabulary already contains `QUALIFIED`, `NOT_ESTABLISHED`, and `DISQUALIFIED`, with structural requirements for a qualifying record;
- repository-local Git identities or locally generated keys are still insufficient to establish externally authenticated independence;
- the current top-level H11 admission validator validates the present Codex / `NOT_ESTABLISHED` / `BLOCKED` package, not a generic future positive-candidate path;
- no external-authentication binding, sufficient-evidence policy, issuer/profile choice, generic evaluator, or positive qualification-transition behavior is selected or implemented by the current repository state.

```text
authenticated account/action ≠ real-world identity
real-world identity ≠ organizational independence
organizational independence ≠ independent evidence custody
qualification ≠ execution admission
execution admission ≠ H11 execution
```

Any future positive qualification path requires a separate operator-approved, versioned, candidate-neutral design before implementation, followed by a separate `A10_H11_EXECUTION_ADMISSION` reassessment. Until then, `NOT_ESTABLISHED / BLOCKED / NOT_TESTED` remains the authoritative boundary.

This is not permission to invent a substitute reviewer, protocol or gate. It keeps the existing PR #131 → qualification record → admission reassessment path executable.

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
GitHub Sync Log → PR/SHA/CI synchronization chronology
```

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
```

## Update rule

For every risk transition record exact governing contract/decision, exact evidence identity, residual risk, proof boundary and whether operator approval is required. Do not convert a bounded PASS, closed defect, accepted research priority, operator approval, qualifying review, reconciliation, preregistration or scoped experiment result into production, truth, compliance, deletion, Final Canon, universal neutrality, future-substrate support or ecosystem-authority claims.