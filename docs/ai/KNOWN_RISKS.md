<!-- H11_EXECUTION_ADMISSION_BLOCKED_CURRENT -->
> [!IMPORTANT]
> **Current authoritative risk overlay — 2026-08-13.** Current selected family is `A10-H11`; current gate is `A10_H11_EXECUTION_ADMISSION`; admission remains `BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER`; reviewer/reproducer remains `NOT_ESTABLISHED`; H11 remains `NOT_TESTED`; PR #131 is the open review surface. The immediate P0 research risk is false independence/self-certification: CI success, owner/self review, automated validators, Codex quota `BOT_NOTICE`, LLM agreement, or same-agent relabeling are not qualifying `INDEPENDENT_SEMANTIC_ORACLE` evidence. H11 implementation/execution, dependency-graph execution, and semantic adjudication remain `NOT AUTHORIZED`. Runtime expansion remains `FROZEN`; Final Canon `DEFERRED / NOT_AUTHORIZED`; production `false`; Issue #88 OPEN. PR #129 remains immutable admission evidence; PR #130 (`e36b7f45410d74b8a65406bff6fdd6d070fa96b0`) is the separate machine-truth / verified 7-of-7 Notion synchronization checkpoint. Lower D5/D6/D8/RAVP risk snapshots are historical chronology only.

> [!WARNING]
> **New P1 evidence-chain risk set.** PR #131's substantive Codex review found six open validation weaknesses: mechanism coverage could be claimed without graph evidence; self-review could be self-declared qualified; support was not a conditional invariant; input artifacts were arbitrary strings; private/non-repository observations could enter adjudication; and raw payloads could carry semantic verdict self-reports. The current bounded candidate hardens these paths and adds negative fixtures, but is not yet merged. Codex itself remains non-qualifying for H11 because organizational/self-review independence is not established.

> [!WARNING]
> **PR #134 second-round P1 set remains review-stage until exact-head evidence.** Codex found seven further bypasses in the first hardening candidate: records were not applied to their declared schemas, worktree-only evidence could appear repository-visible, hard-failure edge semantics trusted a label, semantic paraphrases bypassed a token blacklist, CI could stand in for independence, support could omit exact bundle verification or retain gaps, and conditional schemas could be rendered unreachable. A bounded follow-up candidate closes these paths without modifying the frozen plan, but it is not authoritative `main` state until protected merge and post-merge reconciliation. Codex's useful technical review still does not qualify it for H11 independence.

<!-- POST_D8_OPERATOR_DECISION_CURRENT -->
> [!IMPORTANT]
> **Current post-D8 operator decision — 2026-08-12.** ADR-0027 / `OD-POST-D8-001` is `ACCEPTED / OPERATOR APPROVED` at `57993f39906ae7266011f6146c9a485d0587d2bf`. A1–A10 remains `STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL`; Final Canon is **deferred**, product runtime remains `FROZEN`, production remains `false`. The only current next gate is `RESIDUAL_A10_VALIDATION_PLAN` for A10-H03, A10-H06, A10-H08, A10-H09, A10-H10, A10-H11, and that gate is **RESEARCH_PLANNING_ONLY** — no residual experiment execution is authorized. Any lower `D6 NEXT`, `D8 IN_PROGRESS`, or `OPERATOR_CANON_RUNTIME_DECISION_REQUIRED` wording is historical chronology, not current truth.

# ⚠️ Native Kernel Known Risks and Required Proof

```yaml
document_role: ACTIVE_RISKS
status_as_of: 2026-08-12
authoritative_machine_source: ../../project-state.json
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
blueprint_decision: ADR-0025
post_blueprint_decision: ADR-0026
independent_review: IAR-1 / QUALIFYING_REVIEW_COMPLETE
review_reconciliation: IAR-1-R1 / COMPLETE
bpv1_plan: BPV1-001-cross-lineage-bounded-accountability-v1 / PREREGISTERED
bpv1_plan_merge: a538d7f1e28858a88b9ee777ac7d6e05b85943db
bpv1_d5_merge: a191e9c868c14af34a269dcdfae44406f1013bda
bpv1_d5_r1_qualification_merge: 3856740570620fb2243e2f0da76359281ec4068f
bpv1_qualified_outcome: SUPPORTED_FOR_SCOPE
next_gate: D6_A10_HYPOTHESIS_CLASSIFICATION
D6: NOT_STARTED
bpv1_execution_authorization_lane: ADMITTED_FOR_EXPERIMENT_ONLY
```

This page lists current risks. Historical defects and prior gate states remain available through Git history and their original evidence/review records; they are not rewritten as current truth.

## Risk-state vocabulary

```text
OPEN                 unresolved technical, governance or evidence risk
MITIGATED            bounded control exists; residual risk remains
CLOSED               exact finding corrected and repository-verified
HISTORICAL_BOUNDARY  retained evidence remains valid only for original version/scope
PROPOSED             research or decision work, not runtime protection
```

## P0 — Production overclaim

**State:** `OPEN / PRIMARY COMMUNICATION AND GOVERNANCE RISK`.

```text
C5 + BPV1-001 scoped evidence
≠ production deployment
≠ live user traffic
≠ sustained operations
```

Production authorization remains `false`.

## P0 — Semantic assertion overclaim

**State:** `OPEN`.

```text
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
assertion map:              45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:                     0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
```

Operational success and BPV1-001 `SUPPORTED_FOR_SCOPE` cannot promote unsupported semantic assertions or silently classify A10 hypotheses.

## P0 — Reference implementation may capture the Canon

**State:** `MITIGATED BY ADR-0025 + ADR-0026 + IAR-1-R1 + BPV1-001 D5/D5-R1 / RESIDUAL OPEN`.

Current controls:

- P1–C5 remains `BOUNDED_REFERENCE_LABORATORY`;
- A1–A10 remain provisional;
- IAR-1 completed as a qualifying adversarial review;
- IAR-1-R1 demoted over-shaped taxonomies from universal minimum to reference structures;
- BPV1-001 forbids current Python/Event/reducer/Receipt/SQL forms as semantic oracle;
- Rust subject was derived as a separate bounded experimental realization;
- D5-R1 externally qualifies structural evidence rather than accepting subject self-report;
- runtime remains frozen.

Residual risk: one Rust realization can still share conceptual assumptions with the repository authors. D6/D7 must preserve this limitation rather than presenting one cross-language success as universal architectural proof.

## P0 — False independence / self-confirming validation

**State:** `MITIGATED FOR IAR-1 AND D5-R1 SELF-REPORT PATH / RESIDUAL OPEN`.

BPV1-001 still declares:

```text
independent language: APPLICABLE / RUST
same repository custody: DECLARED_LIMITATION
independent team: NOT_ESTABLISHED
independent computation model: NOT_ESTABLISHED / CONVENTIONAL_DIGITAL
```

PR #115 removed the specific HR10 problem found after D5: the Rust subject no longer supplies structural oracle-facing PASS booleans. The external qualifier derives structural facts without reading frozen fixture expectations or private runtime state; if it cannot establish a required fact, the unchanged evaluator can become `INDETERMINATE`.

This fixes that adjudication path, but it does **not** establish independent team, custody or computation-model evidence.

## P0 — Oracle leakage / post-hoc rescoping

**State:** `MITIGATED / MUST REMAIN FAIL-CLOSED`.

The frozen preregistration, machine-readable fixture/oracle package and evaluator remain unchanged across D5 and D5-R1. The twelve normative fields, scenario identity, expected fixture semantics, thresholds and HR01-HR10 cannot be changed to rescue a result under the same scenario identity.

D5-R1 has a dedicated scope guard that rejects changes to:

```text
docs/research/BPV1_PREREGISTRATION.*
experiments/bpv1/BPV1-001/admission/**
tools/bpv1/evaluate.py
```

A semantic change there requires a new admitted evidence identity or new scenario identity as applicable.

## P0 — Bounded accountability boundary

**State:** `MITIGATED FOR BPV1-001 FIXED SCOPE / RESIDUAL OPEN OUTSIDE SCOPE`.

The fixed 512-mutation BPV1-001 run preserves current accountability, explicit retention scope and valid loss witnesses while remaining within the preregistered state bounds. D5-R1 also fixes the earlier implementation weakness where witness storage itself could grow without an internal cap.

A separate 96-cycle engineering stress test verifies retained witness records remain bounded and older witness detail folds into a bounded per-slot rollup rather than silently disappearing or becoming an unbounded replacement log.

Residual risk: this is not a proof of bounded behavior for arbitrary workloads, data distributions or future substrates.

## P0 — Bounded-state thresholds may be misleading

**State:** `MITIGATED FOR FIXED BPV1-001 / RESIDUAL OPEN`.

Observed qualified run:

```text
scripted_mutations: 512
durable_state_byte_cap: 262144
durable_bytes_at_512: 42276
retained_detailed_predecessor_cap: 64
retained_detailed_predecessors: 52
loss_witness_cap: 32
retained_loss_witness_records: 13
growth_rule: PASS
```

These are experiment thresholds, not universal architecture constants, capacity claims or performance targets.

## P0 — Semantic corruption coverage

**State:** `MITIGATED FOR BPV1-001 CLAIM FIELDS / RESIDUAL OPEN`.

The original D5 content digest omitted `evidence` and `epistemic_position`; D5-R1 corrected this and added adversarial tests that mutate each without recomputing the digest and require corruption detection.

Residual risk: this local digest is an experiment corruption detector, not a cryptographic authenticity scheme or universal storage-integrity architecture.

## P0 — Threat/authenticity boundary is provisional

**State:** `MITIGATED FOR PREREGISTERED NEGATIVE FIXTURES / RESIDUAL OPEN`.

BPV1-001 executed its scoped negative fixtures for truncation/corruption, forged Authority and withheld counterevidence. This is not a cybersecurity benchmark and does not establish OS security, distributed consensus, production key management, cryptographic authenticity or arbitrary adversarial resilience.

## P0 — Context/Provenance/Authority grounding can hide assumptions

**State:** `OPEN / SCOPED BPV1 EVIDENCE ONLY`.

BPV1-001 preserves the material Context/Source/Evidence/Authority distinctions required by its fixtures and detects hidden semantic divergence despite matching visible final values. It does not exhaust grounding problems across all knowledge systems or substrates.

## P0 — Historical and clean lineages may be collapsed

**State:** `OPEN / GOVERNANCE BOUNDARY`.

```text
clean P1–P5 + C4 + C5
≠ recovered v0.1.2.1
≠ original 44-test evidence
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
```

Issue #1 remains independent.

## P0 — Reducer referential semantics are incomplete

**State:** `OPEN / ISSUE #74 / ADR-0024 PENDING / RUNTIME FROZEN`.

Reducer v1 must not be rewritten in place. Option D, D5 and D5-R1 do not accept ADR-0024 or authorize reducer v2.

## P0 — Event/history commitment is not complete authenticity

**State:** `OPEN`.

```text
hash chain ≠ complete authenticity
signature over incomplete commitment ≠ complete integrity
history visibility ≠ mandatory Event sourcing
```

BPV1-001 produced scoped evidence that current accountability can survive without a canonical per-operation Event log or exact replay in this one realization. D6 must decide what that supports or weakens among the preregistered hypotheses; no universal conclusion is automatic.

## P0 — Physical deletion remains absent

**State:** `OPEN / OUTSIDE BPV1-001 SCOPE`.

Logical `ERASED`, restriction and Receipts must not be represented as global physical deletion. Physical/cryptographic erasure remains outside BPV1-001 because independent physical substrate observability is absent.

## P0 — License and contribution rights are unresolved

**State:** `OPEN / ISSUE #18 / OPERATOR DECISION REQUIRED`.

```text
publicly readable source ≠ permission to copy, modify or redistribute
```

BPV-1 work does not select a license or contribution regime.

## P0 — Research may be mistaken for authorization

**State:** `OPEN / GOVERNANCE BOUNDARY`.

Qualifying review, reconciliation, preregistration, execution admission, D5/D5-R1 `SUPPORTED_FOR_SCOPE`, or later A10 outcome classification do not automatically create Final Canon, product runtime behavior, production authority, or universal substrate claims.

## P1 — Independent implementation evidence remains limited

**State:** `PARTIAL / CROSS-LANGUAGE EVIDENCE EXISTS / BROADER INDEPENDENCE ABSENT`.

BPV1-001 now provides one executed Rust, non-event-sourced, bounded-memory realization. This is materially stronger than PostgreSQL↔SQLite storage-profile evidence, but still lacks:

- independent implementation team/custody;
- independent computation model;
- probabilistic/neuromorphic/analog/non-classical implementation evidence;
- composition/federation evidence.

Do not call it fully independent merely because the language differs.

## P1 — Composition/federation remains outside base conformance

**State:** `OPEN / SEPARATE CAPABILITY CLASS`.

```text
local conformance ≠ federation/composition conformance
```

BPV1-001 is explicitly single-node/non-composed and cannot be generalized to federation.

## P1 — Operational equivalence remains absent

**State:** `OPEN`.

PostgreSQL and SQLite bounded semantic comparison is not full operational equivalence. BPV1-001 does not attempt to prove operational parity or performance superiority.

## P1 — Durable evidence lacks independent custody

**State:** `MITIGATED / RESIDUAL OPEN`.

Repository-resident C5 and BPV1 artifacts are not independent third-party custody, signed timestamping, or disaster recovery.

## P1 — Scale and environment scope are narrow

**State:** `OPEN`.

Passing C5 or BPV1-001 thresholds is not a capacity, SLO, cost, architecture, hardware-portability or universal substrate claim.

## P1 — Current-state surfaces can drift

**State:** `MITIGATED / RESIDUAL LIVE-STATE RISK OPEN`.

GitHub refs, issue states, Actions and Notion can change after committed snapshots. Live state requires GitHub verification. Notion currently remains at D4.5 by deliberate Option D synchronization policy; D5/D5-R1/D6 are deferred to D8.

## P1 — Repository governance enforcement

**State:** `OPEN / SEPARATE FROM BPV1 SEMANTICS`.

Live repository inspection has shown the main branch as protected while enforcement/settings may still be disabled. This is a repository governance risk, not evidence that BPV1 semantics failed. It must not be conflated with D5/D5-R1 qualification.

## Closed/historical boundaries

Historical Event-comparison, evidence-schema, workflow-trigger, SQLite-version, D5 subject-self-report, semantic-digest coverage and unbounded witness-retention defects remain preserved in their original PR/evidence histories. D5-R1 corrects the latter three in a new evidence identity rather than rewriting PR #114 evidence.

## Update rule

For every risk transition record exact contract/decision, exact SHA/workflow runs, affected evidence identity, residual risk, proof boundary, and whether operator approval is required.

Never convert a bounded PASS, retained archive, closed bug, accepted research priority, operator approval, qualifying independent review, reconciliation, preregistration or BPV1 result into production, truth, compliance, deletion, Final Canon, universal neutrality, future-substrate support or ecosystem-authority claims.
