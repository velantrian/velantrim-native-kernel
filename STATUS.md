# Current Status

```yaml
document_role: CURRENT_STATE
status_as_of: 2026-08-12
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
architecture_phase: POST_BLUEPRINT_VALIDATION_D6_A10_HYPOTHESIS_CLASSIFICATION_NEXT
bpv1_plan_merge: a538d7f1e28858a88b9ee777ac7d6e05b85943db
bpv1_execution_admission_package_merge: 6027eec73f11c4626be5553de7e79f827be2c81d
bpv1_d5_merge: a191e9c868c14af34a269dcdfae44406f1013bda
bpv1_d5_r1_qualification_merge: 3856740570620fb2243e2f0da76359281ec4068f
```

> **Repository status:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`  
> **Architecture state:** `A1-A10 DRAFTED / PROVISIONAL · INTEGRATED REVIEW COMPLETE / PROVISIONAL · IAR-1 QUALIFYING REVIEW COMPLETE · IAR-1-R1 COMPLETE · BPV-1 PLAN PREREGISTERED · EXECUTION ADMISSION COMPLETE · D5 EXECUTION COMPLETE · D5-R1 QUALIFIED / SUPPORTED_FOR_SCOPE · D6 NOT STARTED`.

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
BPV-1 preregistration: [English](docs/research/BPV1_PREREGISTRATION.md) · [Русский](docs/research/BPV1_PREREGISTRATION.ru.md) · [JSON](docs/research/BPV1_PREREGISTRATION.json).  
D5-R1 qualification: [English](docs/research/BPV1_D5_R1_QUALIFICATION.md) · [Русский](docs/research/BPV1_D5_R1_QUALIFICATION.ru.md).  
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
BPV-1 plan: PREREGISTERED / EXECUTION_NOT_AUTHORIZED
authoritative BPV-1 plan merge: a538d7f1e28858a88b9ee777ac7d6e05b85943db
BPV-1 execution-admission package merge: 6027eec73f11c4626be5553de7e79f827be2c81d
BPV-1 D5 execution: COMPLETE / historical merge a191e9c868c14af34a269dcdfae44406f1013bda
BPV-1 D5-R1 qualification: COMPLETE / QUALIFIED / merge 3856740570620fb2243e2f0da76359281ec4068f
BPV-1 qualified outcome: SUPPORTED_FOR_SCOPE / 12-of-12 mandatory fixtures PASS
next content gate: D6_A10_HYPOTHESIS_CLASSIFICATION
D6: NOT_STARTED
BPV-1 execution authorization lane: ADMITTED_FOR_EXPERIMENT_ONLY
runtime expansion: FROZEN
```

IAR-1 materially weakened the provisional architecture. The complete A3 transition/outcome machine, A6 lifecycle graph, full A5 identity/time inventory, Receipt-shaped accountability and Event-log-shaped history are reference taxonomies/capabilities rather than universal minimum Kernel form.

The current provisional minimum remains problem-level: non-conflation of representation/Claim with reality/truth; explicit scope/Context/warrant/Authority assumptions where material; explicit Unknown/uncertainty/unsupported states; accountable change/retention/loss for the declared scope; and preregistered equivalence/degradation/refutation conditions.

Exact reconstructability, exact replay, permanent predecessor visibility, global total order and distributed-composition semantics are **not** universal requirements.

## BPV-1 preregistered plan

Scenario: `BPV1-001-cross-lineage-bounded-accountability-v1`.

The authoritative preregistration remains byte-frozen under plan merge `a538d7f1e28858a88b9ee777ac7d6e05b85943db` and SHA-256 `7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0`. Its twelve normative fields, fixture semantics, failure thresholds, target hypotheses and HR01-HR10 were not changed by D5 or D5-R1.

Rust remains a single-node conventional-digital `EXPERIMENTAL_INSTRUMENT_NOT_CANON`; independent team/custody and independent computation model remain `NOT_ESTABLISHED`.

## D5 execution and D5-R1 qualification

PR #114 executed the preregistered BPV1-001 workload and produced the historical D5 evidence. PR #115 then corrected evidence-quality weaknesses without changing the frozen plan/oracle:

- subject output is raw facts rather than oracle-facing structural self-report;
- external qualifier derives implementation-neutral observations without reading fixture expectations or private runtime state;
- the unchanged frozen evaluator returns `SUPPORTED_FOR_SCOPE` with all 12 mandatory fixtures PASS;
- the 512-mutation workload and checkpoints 128/256/512 are unchanged;
- semantic corruption coverage now includes `evidence` and epistemic position;
- retained loss-witness storage is intrinsically bounded, with bounded rollup rather than silent loss or an unbounded replacement log;
- the specific HR10 subject-self-report adjudication path is removed.

The D5-R1 repository evidence is under `experiments/bpv1/BPV1-001/results/d5-r1/`. Historical PR #114 evidence remains preserved unchanged.

`SUPPORTED_FOR_SCOPE` is scoped evidence only. It does **not** establish Final Canon, universal substrate portability, production readiness, independent custody/team, an independent computation model, analog/neuromorphic/probabilistic/quantum support, or product runtime suitability.

## Required non-equivalences

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
reference laboratory ≠ final architecture
blueprint documentation ≠ runtime evidence
operator approval ≠ independent validation
qualifying independent review ≠ architecture proof
review reconciliation ≠ BPV-1 execution authorization
preregistered plan ≠ execution authorization
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
transition taxonomy ≠ mandatory implementation shape
history visibility ≠ mandatory Event sourcing
bounded accountability ≠ exact reconstruction
local conformance ≠ composition/federation conformance
profile conformance ≠ production authorization
substrate-independent specification ≠ universal portability proof
existing mechanism ≠ architecture requirement
NOT_TESTED ≠ SUPPORTED
SUPPORTED_FOR_SCOPE ≠ universal proof
D5 outcome ≠ D6 hypothesis classification
```

## Independent pending decisions

- Issue #18 license/publication: `PENDING_OPERATOR`; no selection made.
- Issue #74 / ADR-0024: `PROPOSED / PENDING_OPERATOR`; reducer-v2 unauthorized.
- ADR-0003: `PROPOSED / NOT_STARTED`.
- Track H source admission remains operator-controlled.

## Notion synchronization boundary

Live Notion remains synchronized through the earlier D4.5 admission checkpoint. D5/D5-R1/D6 evidence is intentionally deferred to the consolidated Option D D8 synchronization unless live governance changes that rule. GitHub is authoritative for current technical state in the meantime.

## Hard stop

The current next gate is `D6_A10_HYPOTHESIS_CLASSIFICATION`. D5 execution and D5-R1 qualification are complete; D6 is **NOT_STARTED** and must classify the preregistered target hypotheses without silently generalizing `SUPPORTED_FOR_SCOPE`. Product runtime integration remains unauthorized, runtime expansion remains `FROZEN`, product runtime thaw remains `NO`, Final Canon remains unauthorized and production authorization remains `false`.
