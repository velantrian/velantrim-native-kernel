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
clean_runtime_support:       PARTIAL
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
7. [A7 — Conflict, Uncertainty, and Revision](docs/A7_CONFLICT_UNCERTAINTY_AND_REVISION.md) · [RU](docs/A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md).

Current progress:

```text
ADR-0025 decision: ACCEPTED / OPERATOR APPROVED
blueprint plan: PRESENT
blueprint content: A1-A7 DRAFTED / PROVISIONAL; A8-A10 INCOMPLETE
next content slice: A8 — SUBSTRATE-INDEPENDENCE CONTRACT
runtime expansion: FROZEN
```

A1–A7 are still pending independent review and integrated A1–A10 review. Drafting a slice is not Canon promotion.

### A7 candidate model

A7 introduces provisional `nk-conflict-uncertainty-revision/A7-draft-1` and refines the accepted `NK-CFL` semantic boundary without accepting proposed ADR-0003 or changing runtime.

It keeps three axes independent:

```text
tension kind
≠ assessment status
≠ resolution status
```

Assessment status distinguishes `CANDIDATE`, `ESTABLISHED`, `NOT_A_CONFLICT`, and `UNRESOLVED_ASSESSMENT`. Resolution status distinguishes `UNRESOLVED`, `DEFERRED`, `RESOLVED_FOR_SCOPE`, and `REOPENED`. Resolution-for-scope is an accountable scoped decision, not a truth oracle.

A7 defines a provisional taxonomy covering technical and semantic tensions including duplicate delivery, write-version race, divergent history, semantic contradiction, temporal/scope mismatch, provenance conflict, measurement disagreement, Authority/policy conflict, epistemic disagreement, projection drift, and unclassified tension. Strict contradiction requires materially adequate alignment of interpretation, Context/scope, time, modality, assumptions, identity, Authority, and known uncertainty.

Uncertainty is represented as typed positions such as Evidence, provenance, Context, temporal, identity, interpretation, Authority, capability, dependency, or measurement gaps. A7 explicitly rejects one mandatory confidence scalar or universal uncertainty-combination algebra. A probability, interval, qualitative judgment, physical distribution, or model score can only be a declared profile-specific representation with explicit meaning and dependencies.

A7 permits `UNRESOLVED` and long-lived plurality. It distinguishes detection Authority from resolution, epistemic-assessment, operational-disposition, and architecture/governance Authority. It supports scoped resolution, revision, Supersession, deferral, and reopening while preserving A5 lineage and A6 lifecycle history.

A7 does not change A6's phase inventory. `IN_TENSION` remains the lifecycle position for unresolved tension; a scoped resolution without semantic revision need not enter `REVISED_OR_SUPERSEDED`, while actual revision/supersession must preserve A5 predecessor/successor lineage.

A7 also does not decide Issue #74 / ADR-0024 successor topology, self-supersession, cycles, reducer-v2 dispatch/migration, or create `CONFLICT_OPENED` / `CONFLICT_RESOLVED` Event verbs.

## Required non-equivalences

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
reference laboratory ≠ final architecture
blueprint documentation ≠ runtime evidence
Observation ≠ Claim
Claim ≠ Truth
Evidence ≠ Source
Repetition ≠ Evidence
Belief ≠ Knowledge
Memory ≠ merely a stored Record
retrieval relevance ≠ epistemic validity
Conflict ≠ necessarily Contradiction
candidate tension ≠ established tension
established tension ≠ resolved tension
detection ≠ resolution
resolution-for-scope ≠ objective truth
uncertainty ≠ one universal confidence scalar
confidence score ≠ Evidence
newer ≠ more correct
majority ≠ truth
Unknown ≠ False
Event usage in P1-C5 ≠ Event as universal primitive
State ≠ necessarily reducer output
Knowledge ≠ LLM / embeddings / SQL / JSON / specific processor
abstract machine ≠ runtime implementation
transition ≠ Event envelope
transition relation ≠ reducer
history visibility ≠ mandatory Event sourcing
admission ≠ truth
semantic identity ≠ storage identity
equal bytes/hash/text ≠ universal semantic identity
write order ≠ represented-world or causal order
Revision ≠ silent overwrite
Supersession ≠ deletion or falsity
restriction ≠ logical erase ≠ physical deletion ≠ cryptographic erasure ≠ forgetting
Receipt/accountability ≠ correctness or truth
profile conformance ≠ production authorization
lifecycle phase ≠ storage status column
closure ≠ deletion of history
one Event ≠ one lifecycle transition
```

## Independent tracks and decisions

| Boundary | State | Effect |
|---|---|---|
| Track H historical recovery | `BLOCKED / ACTIVE EVIDENCE-RECOVERY` | operator-controlled source admission; A7 does not alter it |
| Issue #18 license/publication | `PENDING_OPERATOR / selected_option: null` | no license change; external contribution/publication regime remains unauthorized |
| Issue #74 / ADR-0024 | `PROPOSED / PENDING_OPERATOR / selected_option: null` | reducer v1 remains immutable; reducer-v2 remains unauthorized |
| ADR-0003 semantic conflicts | `PROPOSED / NOT_STARTED` | A7 refines compatible semantic concepts but does not accept the ADR or its proposed Event lifecycle |

Issue #14, #15, #16 and #17 retain their existing accepted/versioned contract or conformance scopes and remaining work. A7 does not close or silently redefine them.

## Runtime freeze

Allowed under ADR-0025: architecture research, integrity/security/reproducibility/provenance fixes, evidence preservation, truth-surface/validator repairs, historical recovery, and isolated blueprint-falsification experiments without promotion.

Not authorized: reducer-v2 runtime, new semantic/conflict Event verbs, executable NK-EPI, Temporal runtime, full Admission lifecycle, operational deletion expansion, new databases/language profiles/model adapters/ecosystem integrations, maturity promotion, or production authorization.

## Evidence boundary

Repository evidence remains version-bound under its original identities:

```text
evidence/c5/2026-08-07/manifest.json
evidence/c5/2026-08-08-adr0023/manifest.json
```

A7 documentation does not create new runtime evidence, change assertion arithmetic, promote `NK-CFL` executable support, or prove arbitrary future-substrate support.

## Explicit non-claims

```text
Architecture Re-foundation ≠ completed blueprint
A1-A7 DRAFTED ≠ independent approval ≠ integrated blueprint approval ≠ Canon promotion
A7 model ≠ universal truth/conflict engine
A7 model ≠ acceptance of ADR-0003
A7 model ≠ conflict Event runtime
A7 model ≠ universal probability/confidence algebra
A7 model ≠ reducer-v2 / ADR-0024 decision
C5 PASS ≠ production readiness
public repository ≠ open-source license
```

Historical implementation records, accepted ADRs, immutable evidence manifests and Git history remain inspectable but do not override this current blueprint state.