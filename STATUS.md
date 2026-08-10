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
8. [A8 — Substrate-Independence Contract](docs/A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md) · [RU](docs/A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md);
9. [A9 — Reference Laboratory Boundary](docs/A9_REFERENCE_LABORATORY_BOUNDARY.md) · [RU](docs/A9_REFERENCE_LABORATORY_BOUNDARY.ru.md).

Current progress:

```text
ADR-0025 decision: ACCEPTED / OPERATOR APPROVED
blueprint plan: PRESENT
blueprint content: A1-A9 DRAFTED / PROVISIONAL; A10 INCOMPLETE
next content slice: A10 — OPEN QUESTIONS AND FALSIFICATION
runtime expansion: FROZEN
```

A1–A9 are still pending independent review and integrated A1–A10 review. Drafting a slice is not Canon promotion.

### A9 candidate model

A9 introduces provisional `nk-reference-laboratory-boundary/A9-draft-1`. It classifies current P1–C5 mechanisms against A1–A8 while preserving the implementation/evidence lineage and preventing implementation capture of Canon.

A9 role labels are:

```text
ARCHITECTURE_PRESERVING_EVIDENCE
PROFILE_SPECIFIC_REALIZATION
PARTIAL_ARCHITECTURE_COVERAGE
FALSIFICATION_INSTRUMENT
LABORATORY_ONLY_CONSTRAINT
NOT_ARCHITECTURE_EVIDENCE
```

A mechanism can carry more than one role. PostgreSQL, SQLite, Python, current Event vocabulary, reducer v1, exact byte encodings, sequence counters, hash chains and CI mechanisms remain valid where their accepted profile contracts require them, but their existence does not make them universal architecture requirements.

P5/C3 provides real but narrow evidence that selected meaning-level behavior survives a PostgreSQL↔SQLite storage-profile change inside a shared Python/conventional-digital lineage. It does not establish independent-language, independent-computation-model or arbitrary-substrate equivalence. Exact imported-history bytes remain a valid laboratory constraint where explicitly required; at architecture level A8 still controls: different bytes may preserve meaning, and equal bytes alone do not prove semantic equivalence.

C4 and C5 are predominantly falsification/bounded-evidence instruments. C5 remains synthetic and ephemeral, not production security, privacy, HA, compliance, independent custody or universal conformance evidence.

A9 preservation rule:

```text
profile-specific
→ label correctly
→ preserve reproducibility
→ keep evidence lineage
→ prevent silent Canon promotion
≠ delete or rewrite automatically
```

A10, not A9, owns the remaining open questions and falsification criteria.

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
existing mechanism ≠ architecture requirement
useful evidence ≠ universal substrate proof
```

## Independent tracks and decisions

| Boundary | State | Effect |
|---|---|---|
| Track H historical recovery | `BLOCKED / ACTIVE EVIDENCE-RECOVERY` | operator-controlled source admission; A9 does not alter it |
| Issue #18 license/publication | `PENDING_OPERATOR / selected_option: null` | no license change; external contribution/publication regime remains unauthorized |
| Issue #74 / ADR-0024 | `PROPOSED / PENDING_OPERATOR / selected_option: null` | reducer v1 remains immutable; reducer-v2 remains unauthorized |
| ADR-0003 semantic conflicts | `PROPOSED / NOT_STARTED` | A7–A9 preserve semantic boundaries but do not accept the ADR or authorize Event vocabulary |

Issue #14, #15, #16 and #17 retain their existing accepted/versioned contract or conformance scopes and remaining work. A9 does not close or silently redefine them.

## Runtime freeze

Allowed under ADR-0025: architecture research, integrity/security/reproducibility/provenance fixes, evidence preservation, truth-surface/validator repairs, historical recovery, and isolated blueprint-falsification experiments without promotion.

Not authorized: reducer-v2 runtime, new semantic/conflict Event verbs, executable NK-EPI, Temporal runtime, full Admission lifecycle, operational deletion expansion, new databases/language profiles/model adapters/ecosystem integrations, maturity promotion, or production authorization.

## Evidence boundary

Repository evidence remains version-bound under its original identities:

```text
evidence/c5/2026-08-07/manifest.json
evidence/c5/2026-08-08-adr0023/manifest.json
```

A9 documentation does not create new runtime evidence, change assertion arithmetic, promote NK-EPI, prove arbitrary future-substrate support, or establish production readiness.

## Explicit non-claims

```text
Architecture Re-foundation ≠ completed blueprint
A1-A9 drafted ≠ independent approval or integrated blueprint approval
A9 classification ≠ acceptance of current mechanisms as universal Canon
PostgreSQL↔SQLite C3 ≠ independent-language equivalence ≠ arbitrary-substrate portability proof
profile-specific ≠ delete/rewrite automatically
C5 PASS ≠ production readiness
public repository ≠ open-source license
```

Historical implementation records, accepted ADRs, immutable evidence manifests and Git history remain inspectable but do not override this current blueprint state.
