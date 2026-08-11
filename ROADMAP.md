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
→ BPV1_PLAN_AND_PREREGISTRATION            NEXT GATE
→ BPV-1 CROSS-LINEAGE FALSIFICATION        BLOCKED BY PREREGISTERED PLAN
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
- review result: [human](docs/reviews/IAR-1_RESULT.md) / [machine](docs/reviews/IAR-1_RESULT.json);
- reconciliation: [human](docs/reviews/IAR-1_RECONCILIATION.md) / [machine](docs/reviews/IAR-1_RECONCILIATION.json);
- operator post-blueprint choice: `OPTION D / ADR-0026 / APPROVED`;
- next gate: `BPV1_PLAN_AND_PREREGISTRATION`;
- BPV-1 execution: `BLOCKED_PENDING_PREREGISTERED_PLAN`;
- runtime expansion: `FROZEN`;
- P1–C5: `BOUNDED_REFERENCE_LABORATORY`;
- production: `false`.

## Reconciled architecture boundary

IAR-1 established that the architecture was still too shaped by its laboratory lineage even after literal Python/SQL/Event disclaimers. The reconciliation therefore narrows the minimum Kernel.

### Candidate minimum obligations

1. representation/Claim is not silently equated with reality/truth;
2. scope, Context, warrant/provenance and Authority assumptions are explicit where materially relevant;
3. Unknown, uncertainty and unsupported states remain explicit;
4. change, revision, supersession, retention and loss are accountable for declared scope;
5. equivalence, capability, degradation and loss are judged against preregistered observables and failure conditions.

### Reference taxonomy, not universal implementation shape

The complete A2 inventory, A3 transition/outcome catalogue, A5 identity/time inventory, A6 lifecycle graph, Receipt-shaped accountability and Event-log-shaped history remain useful analysis/reference mappings, but a later cross-lineage realization is not required to reproduce them as its native shape.

Exact replay/reconstruction, permanent predecessor visibility and global total order are not universal requirements. Local conformance does not imply composition/federation conformance.

## BPV-1 preregistration gate

Before any BPV-1 implementation/execution, the plan must freeze:

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

Post-execution changes to mandatory obligations, applicability, equivalence predicates or failure thresholds invalidate the run for the claimed scope. A changed experiment receives a new identity; the previous outcome is retained.

The plan must include the hard refutation observations from `IAR-1-R1`, including the rule that a non-event realization preserving the minimum purpose weakens over-strong A3/A6 claims rather than being rejected merely for not exposing those taxonomies.

## Runtime freeze

Allowed: architecture research, BPV-1 planning/preregistration, integrity/security/reproducibility/provenance repair, evidence preservation, truth/validator repair, historical recovery, and later isolated falsification execution only after the preregistered plan is authoritative.

Not authorized without a later explicit operator decision: product runtime thaw, reducer-v2, new semantic/conflict Event verbs, product database/language/model/integration profiles, executable NK-EPI/Temporal/full Admission, operational deletion expansion, maturity promotion, production authorization, or other product semantic/runtime expansion.

## Independent pending decisions

- **Issue #18** — license/publication: `PENDING_OPERATOR`; selected option remains null.
- **Issue #74 / ADR-0024** — `PROPOSED / PENDING_OPERATOR`; reducer-v2 remains unauthorized.
- **ADR-0003** — `PROPOSED / NOT_STARTED`.
- **Track H source admission** — operator-controlled.

## Contract and laboratory boundary

Accepted/versioned current contracts remain usable and historically valid within their scope. IAR-1-R1 does not rewrite their history and does not convert the reconciled minimum architecture into a new runtime contract.

```text
accepted current mechanism
→ retain scope and evidence identity
→ compare against preregistered problem-level obligations
→ later map as PRESERVED / PARTIAL / LOSSY / UNSUPPORTED / INDETERMINATE
≠ automatic architecture requirement
≠ retroactive evidence rewrite
```

## Hard stop

```text
qualifying review complete ≠ architecture proof
reconciliation complete ≠ BPV-1 execution authorization
BPV-1 plan ≠ product runtime
BPV-1 outcome ≠ automatic Canon promotion
A1-A10 drafted/reconciled ≠ Final Canon
C5 PASS ≠ production readiness
public repository ≠ open-source license
```

The only current next gate is `BPV1_PLAN_AND_PREREGISTRATION`.