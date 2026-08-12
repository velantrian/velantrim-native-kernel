<!-- POST_D8_OPERATOR_DECISION_CURRENT -->
> [!IMPORTANT]
> **Current post-D8 operator decision — 2026-08-12.** ADR-0027 / `OD-POST-D8-001` is `ACCEPTED / OPERATOR APPROVED` at `57993f39906ae7266011f6146c9a485d0587d2bf`. A1–A10 remains `STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL`; Final Canon is **deferred**, product runtime remains `FROZEN`, production remains `false`. The only current next gate is `RESIDUAL_A10_VALIDATION_PLAN` for A10-H03, A10-H06, A10-H08, A10-H09, A10-H10, A10-H11, and that gate is **RESEARCH_PLANNING_ONLY** — no residual experiment execution is authorized. Any lower `D6 NEXT`, `D8 IN_PROGRESS`, or `OPERATOR_CANON_RUNTIME_DECISION_REQUIRED` wording is historical chronology, not current truth.

# Roadmap

```yaml
document_role: ACTIVE_ROADMAP
status_as_of: 2026-08-12
authoritative_machine_source: project-state.json
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
publication_checkpoint: 10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c
blueprint_decision: ADR-0025
post_blueprint_decision: ADR-0026
active_architecture_issue: 88
bpv1_plan_merge: a538d7f1e28858a88b9ee777ac7d6e05b85943db
bpv1_execution_admission_package_merge: 6027eec73f11c4626be5553de7e79f827be2c81d
bpv1_d5_merge: a191e9c868c14af34a269dcdfae44406f1013bda
bpv1_d5_r1_qualification_merge: 3856740570620fb2243e2f0da76359281ec4068f
```

Native Kernel keeps three independent tracks:

```text
H — Historical Recovery
C — Clean Reference Implementation
R — Architecture Re-foundation and Post-Blueprint Validation
```

## Governing sequence

```text
A1 purpose
→ A2 ontology
→ A3 abstract machine
→ A4 semantic laws
→ A5 identity / time / change
→ A6 lifecycle
→ A7 conflict / uncertainty / revision
→ A8 substrate-independence contract
→ A9 reference-laboratory boundary
→ A10 open questions / falsification
→ integrated A1-A10 review                 COMPLETE / PROVISIONAL
→ OPERATOR_POST_BLUEPRINT_DECISION         COMPLETE / OPTION D / ADR-0026
→ INDEPENDENT_ARCHITECTURE_REVIEW          COMPLETE / IAR-1 / QUALIFYING
→ REVIEW_FINDING_RECONCILIATION            COMPLETE / IAR-1-R1
→ BPV1_PLAN_AND_PREREGISTRATION            COMPLETE / PR #110
→ BPV1_EXECUTION_ADMISSION                 COMPLETE / PR #112 + PR #113 checkpoint
→ BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION COMPLETE / PR #114
→ D5_R1_EVIDENCE_QUALIFICATION             COMPLETE / PR #115 / QUALIFIED
→ A10 OUTCOME CLASSIFICATION               NEXT / D6 / NOT STARTED
→ INTEGRATED RE-REVIEW                     BLOCKED BY D6
→ FINAL AUTHORITATIVE SYNC                 BLOCKED BY D7
→ separate operator Canon/runtime decision BLOCKED BY RE-REVIEW
```

## Current architecture checkpoint

- A1–A10: `DRAFTED / PROVISIONAL / RECONCILED BY OVERLAY`;
- integrated review: [EN](docs/INTEGRATED_A1_A10_REVIEW.md) / [RU](docs/INTEGRATED_A1_A10_REVIEW.ru.md);
- independent review: `IAR-1 / QUALIFYING_REVIEW_COMPLETE`;
- IAR-1 findings: `10 total / 7 BLOCKING / 3 MATERIAL`;
- reconciliation: `IAR-1-R1 / COMPLETE / open blockers 0 / open material 0`;
- BPV-1 plan: `BPV1-001-cross-lineage-bounded-accountability-v1 / PREREGISTERED / EXECUTION_NOT_AUTHORIZED`;
- authoritative plan merge: `a538d7f1e28858a88b9ee777ac7d6e05b85943db`;
- execution-admission package merge: `6027eec73f11c4626be5553de7e79f827be2c81d`;
- D5 execution merge: `a191e9c868c14af34a269dcdfae44406f1013bda`;
- D5-R1 qualification merge: `3856740570620fb2243e2f0da76359281ec4068f`;
- D5-R1 qualification: `QUALIFIED`;
- frozen-oracle result: `SUPPORTED_FOR_SCOPE / 12-of-12 mandatory fixtures PASS`;
- next gate: `D6_A10_HYPOTHESIS_CLASSIFICATION`;
- D6: `NOT_STARTED`;
- BPV-1 execution authorization lane: `ADMITTED_FOR_EXPERIMENT_ONLY`;
- runtime expansion: `FROZEN`;
- P1–C5: `BOUNDED_REFERENCE_LABORATORY`;
- production: `false`.

## Reconciled architecture boundary

The candidate minimum remains problem-level:

1. representation/Claim is not silently equated with reality/truth;
2. scope, Context, warrant/provenance and Authority assumptions are explicit where materially relevant;
3. Unknown, uncertainty and unsupported states remain explicit;
4. change, revision, supersession, retention and loss are accountable for declared scope;
5. equivalence, capability, degradation and loss are judged against preregistered observables and failure conditions.

The complete A2 inventory, A3 transition/outcome catalogue, A5 identity/time inventory, A6 lifecycle graph, Receipt-shaped accountability and Event-log-shaped history remain useful reference taxonomies, not universal implementation shape. Exact replay/reconstruction, permanent predecessor visibility and global total order are not universal requirements. Local conformance does not imply composition/federation conformance.

## BPV-1 execution and qualification

The frozen plan and oracle were not modified by D5 or D5-R1. PR #114 executed the exact preregistered workload. PR #115 added an external qualification layer so oracle-facing structural facts are derived outside the Rust subject rather than accepted as subject self-report, strengthened semantic corruption coverage, and made retained loss-witness storage intrinsically bounded.

The exact frozen BPV1-001 scenario remains:

```text
active claim slots: 32
revision cycles: 16
scripted mutations: 512
checkpoints: 128 / 256 / 512
durable-state cap: 262144 bytes
retained detailed predecessor cap: 64
loss-witness retained-record cap: 32
```

Qualified result:

```text
external qualification: QUALIFIED
frozen evaluator: SUPPORTED_FOR_SCOPE
mandatory fixtures: 12 / 12 PASS
durable bytes @512: 42276
retained detailed predecessors: 52
retained witness records: 13
growth rule: PASS
```

This result is evidence for BPV1-001 only. It does not prove universal substrate independence, independent team/custody, independent computation model, Final Canon, production readiness, or product runtime suitability.

## D6 — next bounded stage

D6 must classify the A10 target hypotheses using only the authoritative frozen plan plus qualified D5 evidence. Allowed classifications remain:

```text
SUPPORTED_FOR_SCOPE
WEAKENED
REFUTED
INDETERMINATE
NOT_TESTED
```

D6 must not treat aggregate `SUPPORTED_FOR_SCOPE` as automatic support for every A10 hypothesis. Informative-not-adjudicated and not-tested hypotheses remain distinct, and `NOT_TESTED ≠ SUPPORTED`.

D6 is documentation/evidence classification only. It does not thaw runtime, promote Final Canon, change the experiment, or authorize implementation expansion.

## Runtime freeze

Allowed: architecture research, integrity/security/reproducibility/provenance repair, evidence preservation, truth/validator repair, historical recovery, D6 classification, D7 integrated re-review, and D8 synchronization.

Not authorized: product runtime thaw, reducer-v2, new semantic/conflict Event verbs, product database/language/model/integration profiles, executable NK-EPI/Temporal/full Admission, operational deletion expansion, Final Canon, maturity or production promotion.

## Independent pending decisions

- **Issue #18** — license/publication: `PENDING_OPERATOR`.
- **Issue #74 / ADR-0024** — `PROPOSED / PENDING_OPERATOR`; reducer-v2 unauthorized.
- **ADR-0003** — `PROPOSED / NOT_STARTED`.
- **Track H source admission** — operator-controlled.

## Notion synchronization

Live Notion remains at the earlier D4.5 admission checkpoint. D5/D5-R1/D6 evidence is intentionally deferred to the consolidated Option D D8 synchronization unless live governance changes that rule. This lag is explicit and must not be interpreted as a contradiction in GitHub technical authority.

## Hard stop

```text
qualifying review complete ≠ architecture proof
preregistered plan ≠ execution authorization
SUPPORTED_FOR_SCOPE ≠ universal portability proof
D5 result ≠ D6 classification
BPV-1 ≠ product runtime
BPV-1 outcome ≠ automatic Canon promotion
A1-A10 drafted/reconciled ≠ Final Canon
C5 PASS ≠ production readiness
public repository ≠ open-source license
```

The only current next gate is `D6_A10_HYPOTHESIS_CLASSIFICATION`; D6 is not started.
