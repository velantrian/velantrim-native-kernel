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

Historical reconciliation binding remains unchanged: publication checkpoint `10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c`; manifest source / previously committed Notion-synchronized descendant `70acd0da61fee19131947aa56125833adb156ced`. The later Notion synchronization checkpoint does not rewrite or replace the earlier publication checkpoint.

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
preregistered plan ≠ BPV-1 execution permission
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
BPV-1 plan: PREREGISTERED / EXECUTION_NOT_AUTHORIZED
authoritative BPV-1 plan merge: a538d7f1e28858a88b9ee777ac7d6e05b85943db
BPV-1 execution-admission package merge: 6027eec73f11c4626be5553de7e79f827be2c81d
next bounded gate: BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION
BPV-1 execution: ADMITTED_FOR_EXPERIMENT_ONLY
runtime expansion: FROZEN
```

Integrated review: [EN](../INTEGRATED_A1_A10_REVIEW.md) / [RU](../INTEGRATED_A1_A10_REVIEW.ru.md).  
Independent-review protocol: [EN](../INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md) / [RU](../INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md).  
IAR-1 result: [human](../reviews/IAR-1_RESULT.md) / [machine](../reviews/IAR-1_RESULT.json).  
IAR-1 reconciliation: [human](../reviews/IAR-1_RECONCILIATION.md) / [machine](../reviews/IAR-1_RECONCILIATION.json).  
BPV-1 preregistration: [EN](../research/BPV1_PREREGISTRATION.md) / [RU](../research/BPV1_PREREGISTRATION.ru.md) / [machine](../research/BPV1_PREREGISTRATION.json).

## BPV-1 preregistration effect

Scenario `BPV1-001-cross-lineage-bounded-accountability-v1` is now an authoritative preregistered falsification plan. PR #110 merged it as `a538d7f1e28858a88b9ee777ac7d6e05b85943db`, with exact-head and post-merge validation green.

The plan freezes before execution all twelve normative fields required by IAR-1-R1:

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

It fixes one single-node, non-composed, conventional-digital cross-language instrument. Rust is `EXPERIMENTAL_INSTRUMENT_NOT_CANON`; independent team/custody and independent computation model remain `NOT_ESTABLISHED`. The subject may not reuse current Python domain models, Event envelopes, reducer logic, Receipt shape, or SQL profile as its semantic oracle.

Post-execution normative rescoping invalidates the run and requires a new scenario identity.

## BPV1_EXECUTION_ADMISSION — complete

The separate execution-admission checkpoint is now authoritative. PR #112 merged the candidate package at `6027eec73f11c4626be5553de7e79f827be2c81d`, binding:

- the authoritative preregistration and frozen digest (corrected to `7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0` after independent verification found the originally recorded digest did not match the unmodified preregistration file's actual bytes);
- machine-readable fixtures/oracle package derived only from the plan;
- standalone evaluator tests passing before subject execution;
- pinned Rust toolchain and experimental source boundary;
- static scope audit proving no product runtime/profile integration.

Admission authorizes only BPV1-001 subject implementation/execution. It is not A11, product runtime thaw, Final Canon or production authorization. The implementation under test cannot define expected semantic outcomes after execution begins.

```text
BPV-1 execution: ADMITTED_FOR_EXPERIMENT_ONLY
subject implementation: AUTHORIZED_FOR_BPV1-001_ONLY
subject execution: AUTHORIZED_FOR_BPV1-001_ONLY
product runtime integration: NOT AUTHORIZED
runtime expansion: FROZEN
product runtime thaw: NO
production_authorized: false
```

## Current integrated/reconciled distinctions

```text
PHYSICALLY_ERASED ≠ CRYPTOGRAPHICALLY_ERASED
FORGOTTEN_OR_LOST ≠ deliberate erasure claim
physical/crypto erasure assertion ≠ verified substrate condition
uncertainty ≠ one universal confidence scalar
Conflict ≠ necessarily Contradiction
A6 lifecycle positions ≠ mandatory pipeline or universal shape
A3 transition catalogue ≠ mandatory Kernel machine shape
bounded accountability ≠ exact reconstruction
history visibility ≠ mandatory Event sourcing
local conformance ≠ composition/federation conformance
A10 outcomes = SUPPORTED_FOR_SCOPE / WEAKENED / REFUTED / INDETERMINATE / NOT_TESTED
NOT_TESTED ≠ SUPPORTED
reference laboratory ≠ final architecture
existing mechanism ≠ architecture requirement
substrate-independent specification ≠ universal portability proof
```

## Runtime/operator boundary

No AI agent may select the license or accept ADR-0024. Track H source admission also remains operator-controlled.

Not authorized automatically: BPV-1 execution before admission, product runtime thaw, reducer v2, new semantic/conflict Event verbs, new product database/language/model/integration profiles, executable NK-EPI/Temporal/full Admission, operational deletion expansion, Final Canon, maturity promotion or production authorization.

```text
Issue #18: PENDING_OPERATOR
Issue #74 / ADR-0024: PROPOSED / PENDING_OPERATOR
ADR-0003: PROPOSED / NOT_STARTED
Track H source admission: operator-controlled
```

## Current known gaps

- BPV1-001 subject implementation has not yet been written or executed;
- no cross-lineage BPV-1 subject realization has been executed;
- P5/C3 is not independent-language or arbitrary-substrate evidence;
- no bounded-memory run has yet tested the refined accountability boundary;
- composition/federation remains a separate capability class;
- no arbitrary future-substrate support is demonstrated;
- A10 major hypotheses remain unproved across independent computation models;
- physical/cryptographic erasure execution and production operations remain absent.

## Hard stop

The only current next gate is `BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION`. BPV-1 execution is `ADMITTED_FOR_EXPERIMENT_ONLY`, bounded strictly to the BPV1-001 subject; it is not A11, product runtime permission, Final Canon or production authorization. Product runtime integration remains not authorized and runtime expansion remains `FROZEN`.
