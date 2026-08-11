# Roadmap

```yaml
document_role: ACTIVE_ROADMAP
status_as_of: 2026-08-11
authoritative_machine_source: project-state.json
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
publication_checkpoint: 10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c
blueprint_decision: ADR-0025
post_blueprint_decision: ADR-0026
active_architecture_issue: 88
bpv1_plan_merge: a538d7f1e28858a88b9ee777ac7d6e05b85943db
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
→ BPV1_EXECUTION_ADMISSION                 NEXT GATE
→ BPV-1 CROSS-LINEAGE FALSIFICATION        BLOCKED BY EXECUTION ADMISSION
→ A10 OUTCOME CLASSIFICATION               BLOCKED BY BPV-1
→ INTEGRATED RE-REVIEW                     BLOCKED BY OUTCOMES
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
- next gate: `BPV1_EXECUTION_ADMISSION`;
- BPV-1 execution: `BLOCKED_PENDING_EXECUTION_ADMISSION`;
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

## BPV-1 plan — authoritative, execution still blocked

PR #110 published the immutable preregistration identity `BPV1-001-cross-lineage-bounded-accountability-v1`. The plan freezes before execution:

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

The plan also fixes the bounded workload and independence limitations. Rust is an experimental cross-language instrument only; independent team/custody and independent computation model remain `NOT_ESTABLISHED`. Post-execution changes to normative fields invalidate the run and require a new scenario identity.

## BPV1_EXECUTION_ADMISSION — next gate

Execution admission is a separate fail-closed checkpoint. Before any subject implementation/execution it must bind:

- the authoritative plan and a frozen preregistration digest;
- machine-readable fixtures derived only from the preregistered plan;
- a standalone evaluator/oracle whose tests pass before subject execution;
- a pinned Rust toolchain and experimental source boundary;
- a static scope audit proving no product runtime/profile integration.

Until that checkpoint is authoritative:

```text
BPV-1 execution: BLOCKED_PENDING_EXECUTION_ADMISSION
runtime expansion: FROZEN
product runtime thaw: NO
production: false
```

## Runtime freeze

Allowed: architecture research, execution-admission packaging, integrity/security/reproducibility/provenance repair, evidence preservation, truth/validator repair, historical recovery, and later isolated falsification execution only after explicit admission.

Not authorized: product runtime thaw, reducer-v2, new semantic/conflict Event verbs, product database/language/model/integration profiles, executable NK-EPI/Temporal/full Admission, operational deletion expansion, Final Canon, maturity or production promotion.

## Independent pending decisions

- **Issue #18** — license/publication: `PENDING_OPERATOR`.
- **Issue #74 / ADR-0024** — `PROPOSED / PENDING_OPERATOR`; reducer-v2 unauthorized.
- **ADR-0003** — `PROPOSED / NOT_STARTED`.
- **Track H source admission** — operator-controlled.

## Hard stop

```text
qualifying review complete ≠ architecture proof
reconciliation complete ≠ BPV-1 execution authorization
preregistered plan ≠ execution authorization
BPV-1 ≠ product runtime
BPV-1 outcome ≠ automatic Canon promotion
A1-A10 drafted/reconciled ≠ Final Canon
C5 PASS ≠ production readiness
public repository ≠ open-source license
```

The only current next gate is `BPV1_EXECUTION_ADMISSION`.
