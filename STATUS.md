# Current Status

```yaml
document_role: CURRENT_STATE
status_as_of: 2026-08-10
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
active_architecture_decision: ADR-0025
active_architecture_issue: 88
architecture_phase: ARCHITECTURE_REFOUNDATION_BLUEPRINT_FIRST
```

> **Repository status:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`  
> **Active research phase:** `ARCHITECTURE RE-FOUNDATION / BLUEPRINT-FIRST / RUNTIME EXPANSION FROZEN`.

Committed checkpoints are role-bearing historical references, not automatic live HEAD. Resolve live `main` through GitHub or the checked-out Git ref. Later documentation does not broaden earlier runtime/evidence proof.

## Current implementation boundary

```text
clean_runtime_support:      PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false

assertion map: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:        0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
```

P1–P5, C4 and C5 remain a **BOUNDED REFERENCE LABORATORY**. They are preserved, useful and testable, but are not the final Native Kernel architecture and may not expand semantic/runtime scope before the blueprint gate.

## Active Architecture Re-foundation

Decision: [ADR-0025](docs/adr/0025-blueprint-before-runtime-expansion.md).  
Plan: [English](docs/ARCHITECTURE_REFOUNDATION.md) · [Русский](docs/ARCHITECTURE_REFOUNDATION.ru.md).  
Tracking: [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88).

Drafted provisional deliverables:

1. [A1 — Kernel Purpose and Non-goals](docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.md) · [RU](docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md);
2. [A2 — Knowledge and Memory Ontology](docs/A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md) · [RU](docs/A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md);
3. [A3 — Abstract Native Kernel Machine](docs/A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md) · [RU](docs/A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md);
4. [A4 — Semantic Laws and Invariants](docs/A4_SEMANTIC_LAWS_AND_INVARIANTS.md) · [RU](docs/A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md);
5. [A5 — Identity, Time, and Change](docs/A5_IDENTITY_TIME_AND_CHANGE.md) · [RU](docs/A5_IDENTITY_TIME_AND_CHANGE.ru.md);
6. [A6 — Knowledge Lifecycle](docs/A6_KNOWLEDGE_LIFECYCLE.md) · [RU](docs/A6_KNOWLEDGE_LIFECYCLE.ru.md);
7. [A7 — Conflict, Uncertainty, and Revision](docs/A7_CONFLICT_UNCERTAINTY_AND_REVISION.md) · [RU](docs/A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md);
8. [A8 — Substrate-Independence Contract](docs/A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md) · [RU](docs/A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md).

Current progress:

```text
ADR-0025 decision: ACCEPTED / OPERATOR APPROVED
blueprint plan: PRESENT
blueprint content: A1-A8 DRAFTED / PROVISIONAL; A9-A10 INCOMPLETE
next content slice: A9 — REFERENCE LABORATORY BOUNDARY
runtime expansion: FROZEN
```

A1–A8 are still pending independent review and integrated A1–A10 review. Drafting a slice is not Canon promotion.

### A8 candidate model

A8 introduces provisional `nk-substrate-independence/A8-draft-1`. It defines substrate independence as preservation of meaning-level obligations through declared mappings rather than physical sameness.

A profile maps architecture obligations through:

```text
SUBSTRATE_MAPPING(
  profile,
  architecture_obligation,
  realization_or_equivalent,
  preservation_state,
  context_and_scope,
  observable_check,
  declared_loss_or_none,
  uncertainty,
  authority_for_claim
)
```

The mapping distinguishes `PRESERVED`, `PARTIAL`, `UNSUPPORTED`, `INDETERMINATE`, and `LOSSY`. These are A8 mapping states, not assertion-map arithmetic. A known inability to preserve a required distinction must weaken or fail the conformance claim rather than silently approximate it.

A8 defines ten preservation obligations (`A8-P01`…`A8-P10`) spanning A2 ontology distinctions, A3 transition semantics, A4 laws, A5 identity/time/order, A6 lifecycle/history, A7 conflict/uncertainty/revision, Context/Provenance/Authority, accountability, and explicit capability/loss declarations.

A8 keeps distinct:

```text
PHYSICAL_IDENTITY
REPRESENTATION_EQUIVALENCE
SEMANTIC_OBLIGATION_EQUIVALENCE
BEHAVIORAL_CONFORMANCE_FOR_SCOPE
LINEAGE_CONTINUITY_EQUIVALENCE
```

Physical identity is neither necessary nor sufficient for semantic equivalence. Same bytes/output do not prove semantic equivalence, and different bytes/IDs/storage layouts do not by themselves prove non-equivalence.

A8 does not require a global clock, total order, SQL, JSON, Event sourcing, reducer, Python, hashes, digital bytes, one uncertainty scalar, or one processor model. A substrate may use a partial order or other time representation as long as materially required temporal/causal relations are preserved and implementation order is not promoted to world order.

A8 defines scoped conformance outcomes `FULL_CONFORMANCE_FOR_SCOPE`, `BOUNDED_CONFORMANCE`, `NON_CONFORMANT_FOR_SCOPE`, and `INDETERMINATE_CONFORMANCE`. It explicitly rejects universal future-substrate portability claims. A9, not A8, owns the detailed mapping and grading of P1–C5 against the blueprint.

## Required non-equivalences

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
reference laboratory ≠ final architecture
blueprint documentation ≠ runtime evidence
Architecture ≠ implementation
representation ≠ represented reality
Observation ≠ Claim
Claim ≠ Truth
Evidence ≠ Source
Repetition ≠ Evidence
Belief ≠ Knowledge
Memory ≠ merely a stored Record
retrieval relevance ≠ epistemic validity
Unknown ≠ False
Unsupported ≠ False
Conflict ≠ necessarily Contradiction
Detection ≠ Resolution
Resolution-for-scope ≠ Objective Truth
Uncertainty ≠ one universal confidence scalar
confidence score ≠ Evidence
newer ≠ more correct
majority ≠ truth
semantic identity ≠ storage identity
equal bytes/hash/text ≠ universal semantic identity
write order ≠ occurrence order ≠ observation order ≠ causal order ≠ semantic precedence
Revision ≠ overwrite
Supersession ≠ deletion or falsity
restriction ≠ logical erase ≠ physical deletion ≠ cryptographic erasure ≠ forgetting
transition ≠ Event envelope
transition relation ≠ reducer
history visibility ≠ mandatory Event sourcing
profile conformance ≠ production authorization
substrate-independent specification ≠ universal portability proof
physical identity ≠ semantic equivalence
same output ≠ full semantic equivalence
```

## Independent tracks and decisions

| Boundary | State | Effect |
|---|---|---|
| Track H historical recovery | `BLOCKED / ACTIVE EVIDENCE-RECOVERY` | operator-controlled source admission; A8 does not alter it |
| Issue #18 license/publication | `PENDING_OPERATOR / selected_option: null` | no license change; external contribution/publication regime remains unauthorized |
| Issue #74 / ADR-0024 | `PROPOSED / PENDING_OPERATOR / selected_option: null` | reducer v1 remains immutable; reducer-v2 remains unauthorized |
| ADR-0003 semantic conflicts | `PROPOSED / NOT_STARTED` | A7/A8 preserve semantic boundaries but do not accept the ADR or authorize Event vocabulary |

Issue #14, #15, #16 and #17 retain their existing accepted/versioned contract or conformance scopes and remaining work. A8 does not close or silently redefine them.

## Runtime freeze

Allowed under ADR-0025: architecture research, integrity/security/reproducibility/provenance fixes, evidence preservation, truth-surface/validator repairs, historical recovery, and isolated blueprint-falsification experiments without promotion.

Not authorized: reducer-v2 runtime, new semantic/conflict Event verbs, executable NK-EPI, Temporal runtime, full Admission lifecycle, operational deletion expansion, new databases/language profiles/model adapters/ecosystem integrations, maturity promotion, or production authorization.

## Evidence boundary

Repository evidence remains version-bound under its original identities:

```text
evidence/c5/2026-08-07/manifest.json
evidence/c5/2026-08-08-adr0023/manifest.json
```

A8 documentation does not create new runtime evidence, change assertion arithmetic, promote NK-EPI, prove arbitrary future-substrate support, or establish a production-ready neuromorphic/analog/quantum implementation.

## Explicit non-claims

```text
Architecture Re-foundation ≠ completed blueprint
A1-A8 DRAFTED ≠ independent approval ≠ integrated blueprint approval ≠ Canon promotion
A8 substrate-independence ≠ universal portability proof
A8 conformance model ≠ proof that every substrate can conform
A8 model ≠ grading of current P1-C5 laboratory
A8 model ≠ future-substrate implementation evidence
C5 PASS ≠ production readiness
public repository ≠ open-source license
```

Historical implementation records, accepted ADRs, immutable evidence manifests and Git history remain inspectable but do not override this current blueprint state.