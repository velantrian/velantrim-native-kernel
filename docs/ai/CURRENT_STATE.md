# 📍 Native Kernel Current State

```yaml
document_role: CURRENT_STATE
status_as_of: 2026-08-11
authoritative_machine_source: ../../project-state.json
machine_protocol: nk-project-state/2
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
live_head_source: GitHub API or checked-out Git ref
machine_truth_reconciliation_merge: d9eee591de308a689ace940c2efe58c9e8a137f2
publication_checkpoint: 10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c
runtime_checkpoint: 675aa4b398a2fc0181dc71d38904a2d33a09f5f8
runtime_integrity_checkpoint: a1cdc6d8f36d67f40f065641809bc6da463c10a4
evidence_producing_checkpoint: 296981ae84ad5bdab5dabbec9b7b9ebb43af63d7
manifest_generated_from: 70acd0da61fee19131947aa56125833adb156ced
notion_synchronized_through: 70acd0da61fee19131947aa56125833adb156ced
blueprint_decision: ADR-0025
post_blueprint_decision: ADR-0026
active_architecture_issue: 88
```

This file must not predict its own future merge SHA. GitHub live refs remain authoritative for `main`, PR heads, Actions, reviews and merge state.

Historical reconciliation binding: publication checkpoint `10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c`; manifest source / previously Notion-synchronized descendant `70acd0da61fee19131947aa56125833adb156ced`. The descendant synchronization identity does not rewrite or replace the publication checkpoint.

The later Notion synchronization checkpoint does not rewrite or replace the earlier publication checkpoint.

## Current boundary

```text
RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
clean_runtime_support:      PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false
assertion map: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:        0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
runtime expansion: FROZEN
P1-C5: BOUNDED REFERENCE LABORATORY
```

```text
C5 bounded rehearsal ≠ production readiness
repository-resident evidence ≠ independent custody
logical ERASED ≠ physical deletion
public repository ≠ open-source license
operator approval ≠ independent validation
qualifying review ≠ architecture proof
review reconciliation ≠ BPV-1 execution permission
```

## Architecture state

Architecture Re-foundation: `BLUEPRINT COMPLETE / PROVISIONAL / VALIDATION ACTIVE`.

```text
blueprint content A1-A10: DRAFTED / PROVISIONAL / RECONCILED BY OVERLAY
integrated review: COMPLETED / PROVISIONAL
operator post-blueprint choice: OPTION D / ADR-0026 / APPROVED
IAR-1: QUALIFYING_REVIEW_COMPLETE
IAR-1 findings: 10 total / 7 BLOCKING / 3 MATERIAL
IAR-1-R1 reconciliation: COMPLETE
open BLOCKING findings: 0
open MATERIAL findings: 0
next bounded gate: BPV1_PLAN_AND_PREREGISTRATION
BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN
runtime expansion: FROZEN
```

Integrated review: [EN](../INTEGRATED_A1_A10_REVIEW.md) / [RU](../INTEGRATED_A1_A10_REVIEW.ru.md). Identity: `nk-integrated-blueprint-review/A1-A10-review-1`.

Independent-review protocol: [EN](../INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md) / [RU](../INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md). Identity: `nk-independent-architecture-review/1`.

IAR-1 result: [human](../reviews/IAR-1_RESULT.md) / [machine](../reviews/IAR-1_RESULT.json).  
IAR-1 reconciliation: [human](../reviews/IAR-1_RECONCILIATION.md) / [machine](../reviews/IAR-1_RECONCILIATION.json).

## IAR-1 architectural effect

IAR-1 found ten substantive issues and completed as a qualifying adversarial review. The reconciliation deliberately shrinks the provisional Kernel rather than preserving every A1–A10 structure.

Current minimum candidate obligations are:

```text
representation / Claim are not silently reality / truth
scope / Context / warrant-provenance / Authority assumptions explicit where material
Unknown / uncertainty / unsupported remain explicit
change / revision / supersession / retention / loss accountable for declared scope
equivalence / degradation / loss judged against preregistered observables and failure rules
```

The complete A2 inventory, A3 transition/outcome machine, A5 seven-identity/eight-time inventory, A6 lifecycle graph, Receipt-shaped accountability and Event-log-shaped history are **reference taxonomies**, not mandatory universal implementation shape.

```text
bounded accountability ≠ exact reconstruction
history visibility ≠ mandatory Event sourcing
exact replay ≠ universal architecture requirement
local conformance ≠ composition/federation conformance
```

Physical/cryptographic erasure requires threat-scoped evidence beyond unverified self-assertion. Context/Provenance/Authority evaluation must terminate through an explicit grounding mode rather than infinite recursive metadata.

## BPV-1 preregistration boundary

Before implementation/execution, the BPV-1 plan must freeze:

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

Post-execution changes to mandatory obligations, applicability, equivalence predicates or failure thresholds invalidate the run for the claimed scope and require a new experiment identity.

The implementation under test must not serve as its own semantic oracle. The plan must derive its state/change/history model from problem-level obligations and must not import A3/A6/Event/reducer/Receipt structures merely because they already exist.

## Current integrated/reconciled distinctions

```text
PHYSICALLY_ERASED ≠ CRYPTOGRAPHICALLY_ERASED
FORGOTTEN_OR_LOST ≠ deliberate erasure claim
physical/crypto erasure assertion ≠ verified substrate condition
uncertainty ≠ one universal confidence scalar
Conflict ≠ necessarily Contradiction
A6 lifecycle positions ≠ mandatory pipeline or universal shape
A3 transition catalogue ≠ mandatory Kernel machine shape
A10 outcomes = SUPPORTED_FOR_SCOPE / WEAKENED / REFUTED / INDETERMINATE / NOT_TESTED
NOT_TESTED ≠ SUPPORTED
reference laboratory ≠ final architecture
existing mechanism ≠ architecture requirement
substrate-independent specification ≠ universal portability proof
```

## Runtime/operator boundary

No AI agent may select the license or accept ADR-0024. Track H source admission also remains operator-controlled.

Not authorized automatically: BPV-1 execution before an authoritative preregistered plan, product runtime thaw, reducer v2, new semantic/conflict Event verbs, new product database/language/model/integration profiles, executable NK-EPI/Temporal/full Admission, operational deletion expansion, Final Canon, maturity promotion or production authorization.

```text
Issue #18: PENDING_OPERATOR
Issue #74 / ADR-0024: PROPOSED / PENDING_OPERATOR
ADR-0003: PROPOSED / NOT_STARTED
Track H source admission: operator-controlled
```

## Current known gaps

- BPV-1 plan/preregistration is not yet authoritative;
- no cross-lineage BPV-1 realization exists;
- P5/C3 is not independent-language or arbitrary-substrate evidence;
- no bounded-memory realization has yet tested the refined accountability boundary;
- composition/federation semantics are intentionally outside base conformance and remain separate research;
- no arbitrary future-substrate support is demonstrated;
- A10 major hypotheses remain unproved across independent computation models;
- physical/cryptographic erasure execution and production operations remain absent.

## Hard stop

The only current next gate is `BPV1_PLAN_AND_PREREGISTRATION`. It authorizes design/preregistration only. It is not A11, BPV-1 execution, Canon promotion, runtime permission or production authorization.