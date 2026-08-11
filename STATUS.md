# Current Status

```yaml
document_role: CURRENT_STATE
status_as_of: 2026-08-11
authoritative_machine_source: project-state.json (nk-project-state/2)
live_head_source: GitHub API or checked-out Git ref
machine_truth_reconciliation_merge: d9eee591de308a689ace940c2efe58c9e8a137f2
human_truth_reconciliation_merge: 07549a0cd952b4e06b61ef24d21b2dcdbc9f861d
issues_notion_reconciliation_merge: cdf559a3a32decd538e4cab3dd7fb591fc6e9322
publication_checkpoint: 10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c
runtime_checkpoint: 675aa4b398a2fc0181dc71d38904a2d33a09f5f8
runtime_integrity_checkpoint: a1cdc6d8f36d67f40f065641809bc6da463c10a4
evidence_producing_checkpoint: 296981ae84ad5bdab5dabbec9b7b9ebb43af63d7
manifest_generated_from: 70acd0da61fee19131947aa56125833adb156ced
notion_synchronized_through: 70acd0da61fee19131947aa56125833adb156ced
blueprint_decision: ADR-0025
post_blueprint_decision: ADR-0026
active_architecture_issue: 88
architecture_phase: POST_BLUEPRINT_VALIDATION_BPV1_PLAN_NEXT
```

> **Repository status:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`  
> **Architecture state:** `A1-A10 DRAFTED / PROVISIONAL · INTEGRATED REVIEW COMPLETE / PROVISIONAL · IAR-1 QUALIFYING REVIEW COMPLETE · IAR-1-R1 RECONCILIATION COMPLETE · BPV-1 PLAN NEXT`.

Committed checkpoint SHAs above remain historical role identities, not automatic live HEAD. Resolve live `main` through GitHub/Git.

## Current implementation boundary

```text
clean_runtime_support:      PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false
assertion map: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:        0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
runtime expansion: FROZEN
P1-C5 role: BOUNDED_REFERENCE_LABORATORY
```

## Architecture Re-foundation and validation

Blueprint decision: [ADR-0025](docs/adr/0025-blueprint-before-runtime-expansion.md).  
Post-blueprint decision: [ADR-0026](docs/adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md).  
Plan: [English](docs/ARCHITECTURE_REFOUNDATION.md) · [Русский](docs/ARCHITECTURE_REFOUNDATION.ru.md).  
Integrated review: [English](docs/INTEGRATED_A1_A10_REVIEW.md) · [Русский](docs/INTEGRATED_A1_A10_REVIEW.ru.md).  
Independent-review protocol: [English](docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md) · [Русский](docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md).  
IAR-1 result: [human](docs/reviews/IAR-1_RESULT.md) · [machine](docs/reviews/IAR-1_RESULT.json).  
IAR-1 reconciliation: [human](docs/reviews/IAR-1_RECONCILIATION.md) · [machine](docs/reviews/IAR-1_RECONCILIATION.json).  
Tracking: [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88).

```text
blueprint content: A1-A10 DRAFTED / PROVISIONAL / RECONCILED BY OVERLAY
integrated review: COMPLETED / PROVISIONAL
operator post-blueprint decision: OPTION D / ADR-0026 / APPROVED
IAR-1: QUALIFYING_REVIEW_COMPLETE
IAR-1 findings: 10 total / 7 BLOCKING / 3 MATERIAL
IAR-1-R1 reconciliation: COMPLETE
open BLOCKING findings: 0
open MATERIAL findings: 0
next content gate: BPV1_PLAN_AND_PREREGISTRATION
BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN
runtime expansion: FROZEN
```

IAR-1 materially weakened the provisional architecture. In particular, the complete A3 transition/outcome machine, A6 lifecycle graph, full A5 identity/time inventory, Receipt-shaped accountability and Event-log-shaped history are no longer treated as the universal minimum Kernel form.

The current provisional minimum is problem-level: non-conflation of representation/Claim with reality/truth, explicit scope/Context/warrant/Authority assumptions where material, explicit Unknown/uncertainty/unsupported states, accountable change/retention/loss for the declared scope, and preregistered equivalence/degradation/refutation conditions.

Exact reconstructability, exact replay, permanent predecessor visibility, global total order and distributed-composition semantics are **not** universal requirements.

## BPV-1 planning gate

BPV-1 implementation/execution is still forbidden. A plan must first preregister:

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

Changing those after execution invalidates the run for the claimed scope and requires a new experiment identity.

The BPV-1 plan must independently derive its state/change/history model instead of importing the current A3/A6/Event/reducer/Receipt shape as an oracle.

## Required non-equivalences

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
reference laboratory ≠ final architecture
blueprint documentation ≠ runtime evidence
operator approval ≠ independent validation
qualifying independent review ≠ architecture proof
review reconciliation ≠ BPV-1 execution authorization
falsification instrument ≠ product runtime
representation ≠ represented reality
Observation ≠ Claim
Claim ≠ Truth
Evidence ≠ Source
Unknown ≠ False
Unsupported ≠ False
Conflict ≠ necessarily Contradiction
Detection ≠ Resolution
Resolution-for-scope ≠ Objective Truth
Uncertainty ≠ one universal confidence scalar
confidence score ≠ Evidence
semantic identity ≠ storage identity
write order ≠ occurrence order ≠ causal order ≠ semantic precedence
Revision ≠ overwrite
Supersession ≠ deletion or falsity
restriction ≠ logical erase ≠ physical deletion ≠ cryptographic erasure ≠ forgetting
PHYSICALLY_ERASED ≠ CRYPTOGRAPHICALLY_ERASED
transition taxonomy ≠ mandatory implementation shape
history visibility ≠ mandatory Event sourcing
bounded accountability ≠ exact reconstruction
local conformance ≠ composition/federation conformance
profile conformance ≠ production authorization
substrate-independent specification ≠ universal portability proof
existing mechanism ≠ architecture requirement
NOT_TESTED ≠ SUPPORTED
```

## Independent pending decisions

- Issue #18 license/publication: `PENDING_OPERATOR`; no selection made.
- Issue #74 / ADR-0024: `PROPOSED / PENDING_OPERATOR`; reducer-v2 unauthorized.
- ADR-0003: `PROPOSED / NOT_STARTED`.
- Track H source admission remains operator-controlled.

## Hard stop

The next gate is `BPV1_PLAN_AND_PREREGISTRATION`. It authorizes only experiment design/preregistration. It is not A11, not BPV-1 execution, not runtime thaw and not Canon promotion. A1–A10 remain provisional and reconciled by overlay; production authorization remains `false`.