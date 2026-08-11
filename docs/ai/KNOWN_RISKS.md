# ⚠️ Native Kernel Known Risks and Required Proof

```yaml
document_role: ACTIVE_RISKS
status_as_of: 2026-08-11
authoritative_machine_source: ../../project-state.json
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
blueprint_decision: ADR-0025
post_blueprint_decision: ADR-0026
independent_review: IAR-1 / QUALIFYING_REVIEW_COMPLETE
review_reconciliation: IAR-1-R1 / COMPLETE
bpv1_plan: BPV1-001-cross-lineage-bounded-accountability-v1 / PREREGISTERED
bpv1_plan_merge: a538d7f1e28858a88b9ee777ac7d6e05b85943db
bpv1_execution_admission_package_merge: 6027eec73f11c4626be5553de7e79f827be2c81d
next_gate: BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION
bpv1_execution: ADMITTED_FOR_EXPERIMENT_ONLY
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
ephemeral CI + synthetic C5 scenarios
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

Operational success cannot promote unsupported or partial semantic assertions.

## P0 — Reference implementation may capture the Canon

**State:** `MITIGATED BY ADR-0025 + ADR-0026 + IAR-1-R1 + BPV1-001 PREREGISTRATION / RESIDUAL OPEN`.

The current P1–C5 lineage was implemented before the complete blueprint. IAR-1 showed that capture risk existed not only in Python/SQL/Event choices but also in higher-level A3 transition/outcome, A6 lifecycle and Receipt/reconstruction structures.

Current controls:

- P1–C5 remains `BOUNDED_REFERENCE_LABORATORY`;
- A1–A10 remain provisional;
- IAR-1 completed as a qualifying adversarial review;
- IAR-1-R1 demoted over-shaped taxonomies from universal minimum to reference structures;
- BPV1-001 forbids reuse of current Python domain models, Event envelope, reducer and Receipt shape as the semantic oracle;
- BPV1-001 uses Rust only as an experimental cross-language instrument, not Canon/product profile;
- runtime remains frozen.

Residual risk: a later subject implementation can still imitate the same conceptual architecture under different syntax. Execution admission must therefore freeze the evaluator before the subject exists/runs.

## P0 — False independence / self-confirming validation

**State:** `MITIGATED FOR IAR-1 / RESIDUAL OPEN FOR EXPERIMENT`.

IAR-1 recorded a concrete reviewer identity and separation basis. It satisfies its review-process gate but does not prove architecture correctness.

BPV1-001 declares:

```text
independent language: APPLICABLE / RUST
same repository custody: DECLARED_LIMITATION
independent team: NOT_ESTABLISHED
independent computation model: NOT_ESTABLISHED / CONVENTIONAL_DIGITAL
```

No later report may call BPV1-001 fully independent merely because the implementation language differs.

## P0 — Execution-admission oracle leakage

**State:** `MITIGATED / SUBJECT IMPLEMENTATION NOW ADMITTED FOR BPV1-001 ONLY`.

The preregistration is authoritative, and the machine-readable fixtures and standalone evaluator are now admitted (PR #112, merge `6027eec73f11c4626be5553de7e79f827be2c81d`, frozen digest corrected to `7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0`). The immediate risk was translating the plan into executable expectations in a way that secretly incorporates subject behavior or current implementation assumptions; the fixtures/evaluator were authored and self-tested before any subject source existed, closing that specific leakage path for this admission.

`BPV1_EXECUTION_ADMISSION` bound before any subject implementation/execution:

- authoritative plan `BPV1-001-cross-lineage-bounded-accountability-v1`;
- frozen digest of normative preregistration;
- machine-readable fixtures derived only from the preregistered plan;
- standalone evaluator tests passing before subject execution;
- pinned Rust toolchain and experimental source boundary;
- static no-product-integration audit.

The evaluator cannot be changed after observing subject results under the same scenario identity except for non-normative bug repair that forces a new admitted evidence identity where meaning could change. Residual risk: the source-boundary audit must be re-verified once the BPV1-001 subject actually exists, to confirm no hidden Native Kernel reuse crept in during implementation.

```text
preregistered plan ≠ execution authorization
fixture package ≠ subject implementation
implementation self-report ≠ oracle Authority
```

## P0 — Post-hoc rescoping

**State:** `MITIGATED BY FROZEN PLAN / MUST REMAIN FAIL-CLOSED`.

The twelve normative fields are frozen before execution:

```text
scenario_id
purpose_scope
mandatory_obligations
applicability_rules
mandatory_observables
equivalence_predicates
allowed_declared_losses
failure_thresholds
hard_refutation_observations
grounding_mode
threat_model
oracle_authority
```

Changing them after results are observed invalidates the run for its claimed scope and requires a new scenario identity. A failed experiment may not be rescued by silently changing applicability or thresholds.

## P0 — Bounded accountability boundary is untested

**State:** `OPEN / PREREGISTERED / NOT YET EXECUTED`.

IAR-1-R1 separates current accountability from exact reconstruction/replay. BPV1-001 preregisters bounded current accountability, explicit retention scope and loss witnesses while allowing compaction outside retained detail.

Risk: the proposed loss-witness boundary may be too weak to prevent silent overwrite or too strong for genuinely bounded realizations. Such an observation must weaken/refute the claim rather than force an Event-log equivalent by definition.

## P0 — Bounded-state thresholds may be misleading

**State:** `OPEN / PREREGISTERED THRESHOLDS / EMPIRICAL RESULT PENDING`.

BPV1-001 fixes:

```text
scripted_mutations: 512
durable_state_byte_cap: 262144
retained_detailed_predecessor_cap: 64
loss_witness_cap: 32
growth_rule: durable_bytes_at_512 <= durable_bytes_at_256 * 1.25 + 4096
```

These are experiment thresholds, not universal architecture constants or performance targets. Passing them cannot be generalized to arbitrary workloads/hardware.

## P0 — Threat/authenticity boundary is provisional

**State:** `OPEN / NEGATIVE TESTS PREREGISTERED / EXECUTION PENDING`.

Relevant adversarial cases include forgery, truncation, rollback, equivocation, withheld counterevidence and unavailable/forged Authority. No one cryptographic mechanism is architecture Canon.

## P0 — Context/Provenance/Authority grounding can hide assumptions

**State:** `OPEN / FINITE GROUNDING PREREGISTERED / EXECUTION PENDING`.

Context/Provenance/Authority chains require an explicit finite grounding mode. Matching visible outputs with materially different hidden roots cannot count as full semantic equivalence.

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

Reducer v1 must not be rewritten in place. Option D and BPV-1 do not accept ADR-0024 or authorize reducer v2.

## P0 — Event/history commitment is not complete authenticity

**State:** `OPEN`.

```text
hash chain ≠ complete authenticity
signature over incomplete commitment ≠ complete integrity
history visibility ≠ mandatory Event sourcing
```

BPV1-001 specifically tests a non-event-sourced authoritative history model; success or failure is scoped evidence, not a universal conclusion by itself.

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

Qualifying review, reconciliation, preregistration, execution admission, experimental PASS, or A10 outcome classification do not automatically create Final Canon, product runtime behavior, production authority, or universal substrate claims.

## P1 — Independent implementation evidence remains absent

**State:** `OPEN / BPV1-001 TARGETS A STRONGER CLASS BUT HAS NOT EXECUTED`.

Current PostgreSQL and SQLite profiles share a Python semantic lineage. BPV1-001 plans cross-language + non-event-sourced + bounded-memory evidence, but independent team/custody and independent computation-model evidence remain absent.

Still absent after preregistration:

- an executed independent-language realization;
- executed non-event-sourced cross-lineage evidence;
- executed bounded-memory evidence;
- independent implementation team/custody;
- probabilistic/neuromorphic/analog/non-classical implementation evidence.

## P1 — Composition/federation remains outside base conformance

**State:** `OPEN / SEPARATE CAPABILITY CLASS`.

```text
local conformance ≠ federation/composition conformance
```

BPV1-001 is explicitly single-node/non-composed and cannot be generalized to federation.

## P1 — Operational equivalence remains absent

**State:** `OPEN`.

PostgreSQL and SQLite bounded semantic comparison is not full operational equivalence. BPV1-001 does not attempt to prove operational parity either.

## P1 — Durable evidence lacks independent custody

**State:** `MITIGATED / RESIDUAL OPEN`.

Repository-resident ZIPs and future BPV-1 artifacts are not independent third-party custody, signed timestamping, or disaster recovery.

## P1 — Synthetic privacy checks are not privacy compliance

**State:** `OPEN`.

Synthetic artifact inspection does not prove real personal-data handling or legal compliance.

## P1 — Logical export is not disaster recovery

**State:** `OPEN`.

Logical export/import evidence is not physical DB backup, WAL recovery, PITR, cross-region restore or restore-under-load proof.

## P1 — Scale and environment scope are narrow

**State:** `OPEN`.

Passing C5 or BPV1-001 thresholds is not a capacity, SLO, cost, architecture, hardware-portability or universal substrate claim.

## P1 — Current-state surfaces can drift

**State:** `MITIGATED / RESIDUAL LIVE-STATE RISK OPEN`.

GitHub refs, issue states, Actions and Notion can change after committed snapshots. Live state requires GitHub verification; Notion requires separate post-merge synchronization/read-back.

## Closed/historical boundaries

Historical Event-comparison, evidence-schema, workflow-trigger and SQLite-version defects remain closed/version-bound in their original PR/evidence histories. They are not reopened by BPV-1 and are not rewritten here.

## Update rule

For every risk transition record exact contract/decision, exact SHA/workflow runs, affected evidence identity, residual risk, proof boundary, and whether operator approval is required.

Never convert a bounded PASS, retained archive, closed bug, accepted research priority, operator approval, qualifying independent review, reconciliation, preregistration or future BPV-1 result into production, truth, compliance, deletion, Final Canon, universal neutrality, future-substrate support or ecosystem-authority claims.
