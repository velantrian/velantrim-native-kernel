# Roadmap

```yaml
document_role: ACTIVE_ROADMAP
status_as_of: 2026-08-10
authoritative_machine_source: project-state.json
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
publication_checkpoint: 10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c
active_architecture_decision: ADR-0025
active_architecture_issue: 88
```

Velantrim Native Kernel maintains three independent tracks:

```text
H — Historical Recovery
C — Clean Reference Implementation
R — Architecture Re-foundation and Long-Horizon Research
```

Their status, evidence and authority must never be collapsed.

## Governing sequence

```text
purpose/ontology
→ abstract Kernel machine
→ semantic laws
→ identity / time / change
→ knowledge lifecycle
→ conflict / uncertainty / revision
→ substrate-independence
→ reference-laboratory boundary
→ open questions / falsification
→ integrated blueprint review
→ separate operator decision
→ only then possible runtime sequencing
```

Runtime must not define new semantics before the blueprint/contract. Evidence must not be relabelled after the fact. More tests do not automatically increase maturity.

## Active priority — Architecture Re-foundation

**State:** `ACTIVE / BLUEPRINT-FIRST / RUNTIME EXPANSION FROZEN`.

Decision: [`ADR-0025`](docs/adr/0025-blueprint-before-runtime-expansion.md).  
Plan: [English](docs/ARCHITECTURE_REFOUNDATION.md) · [Русский](docs/ARCHITECTURE_REFOUNDATION.ru.md).  
Issue: [#88](https://github.com/velantrian/velantrim-native-kernel/issues/88).

Drafted provisional content:

- `A1 — Kernel Purpose and Non-goals`: [English](docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.md) · [Русский](docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md);
- `A2 — Knowledge and Memory Ontology`: [English](docs/A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md) · [Русский](docs/A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md);
- `A3 — Abstract Native Kernel Machine`: [English](docs/A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md) · [Русский](docs/A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md);
- `A4 — Semantic Laws and Invariants`: [English](docs/A4_SEMANTIC_LAWS_AND_INVARIANTS.md) · [Русский](docs/A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md);
- `A5 — Identity, Time, and Change`: [English](docs/A5_IDENTITY_TIME_AND_CHANGE.md) · [Русский](docs/A5_IDENTITY_TIME_AND_CHANGE.ru.md);
- `A6 — Knowledge Lifecycle`: [English](docs/A6_KNOWLEDGE_LIFECYCLE.md) · [Русский](docs/A6_KNOWLEDGE_LIFECYCLE.ru.md);
- `A7 — Conflict, Uncertainty, and Revision`: [English](docs/A7_CONFLICT_UNCERTAINTY_AND_REVISION.md) · [Русский](docs/A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md);
- `A8 — Substrate-Independence Contract`: [English](docs/A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md) · [Русский](docs/A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md);
- `A9 — Reference Laboratory Boundary`: [English](docs/A9_REFERENCE_LABORATORY_BOUNDARY.md) · [Русский](docs/A9_REFERENCE_LABORATORY_BOUNDARY.ru.md).

A1–A9 remain pending independent review and integrated blueprint review with A10. The next bounded content slice is `A10 — Open Questions and Falsification`.

```text
A1 Purpose and Non-goals                         DRAFTED / PROVISIONAL
→ A2 Knowledge and Memory Ontology              DRAFTED / PROVISIONAL
→ A3 Abstract Native Kernel Machine             DRAFTED / PROVISIONAL
→ A4 Semantic Laws and Invariants               DRAFTED / PROVISIONAL
→ A5 Identity / Time / Change                   DRAFTED / PROVISIONAL
→ A6 Knowledge Lifecycle                        DRAFTED / PROVISIONAL
→ A7 Conflict / Uncertainty / Revision          DRAFTED / PROVISIONAL
→ A8 Substrate-independence Contract            DRAFTED / PROVISIONAL
→ A9 Reference Laboratory Boundary              DRAFTED / PROVISIONAL
→ A10 Open Questions and Falsification           NEXT BOUNDED SLICE
→ integrated blueprint review
→ operator decision on reopening runtime work
```

### A9 contribution

A9 candidate `nk-reference-laboratory-boundary/A9-draft-1` classifies the existing P1–C5 implementation lineage against A1–A8 without promoting laboratory mechanisms into universal Canon.

It uses six scoped role labels: `ARCHITECTURE_PRESERVING_EVIDENCE`, `PROFILE_SPECIFIC_REALIZATION`, `PARTIAL_ARCHITECTURE_COVERAGE`, `FALSIFICATION_INSTRUMENT`, `LABORATORY_ONLY_CONSTRAINT`, and `NOT_ARCHITECTURE_EVIDENCE`. A mechanism may carry multiple roles.

Key result: P5/C3 is genuine but narrow architecture-preserving evidence for a storage-profile change. PostgreSQL and SQLite differ in SQL/layout/locking/topology while selected supported semantic outcomes remain stable. However both profiles share Python, conventional digital execution, the semantic core/reducer model, current Event vocabulary/encodings, related harnesses and repository custody. Therefore:

```text
PostgreSQL ↔ SQLite C3
= useful cross-profile evidence
≠ independent-language equivalence
≠ independent-computation-model equivalence
≠ arbitrary-substrate portability proof
```

Current Event/reducer/sequence/hash/Receipt/CI mechanisms remain binding where their accepted versioned laboratory contracts require them, but they are not automatically substrate-neutral requirements. Exact imported Event bytes may be a valid laboratory constraint while A8 still permits different representations to count as semantically equivalent when meaning is preserved.

P4, C4 and C5 are especially useful as measurement/falsification instruments. C5 remains bounded synthetic operational rehearsal, not production readiness, live-data safety, independent custody, compliance, HA or universal conformance evidence.

A9 preserves profile-specific mechanisms rather than deleting them:

```text
profile-specific
→ label correctly
→ preserve reproducibility
→ keep evidence lineage
→ prevent silent Canon promotion
≠ delete or rewrite automatically
```

A10 owns unresolved questions and explicit falsification criteria before integrated review.

## Runtime freeze

Allowed during the freeze:
- architecture and ontology research;
- integrity/security/reproducibility/provenance fixes;
- evidence preservation;
- validator/current-truth repairs;
- historical recovery;
- isolated falsification experiments with no runtime promotion.

Not authorized without a separate explicit operator decision:
- reducer v2 or new semantic/conflict Event verbs;
- new databases/language ports/model adapters/ecosystem integrations;
- executable NK-EPI, Temporal, full Admission, or operational deletion expansion;
- performance-driven semantic changes;
- maturity/production promotion.

## Track H — Historical Recovery

**Status:** `BLOCKED / ACTIVE EVIDENCE-RECOVERY / INDEPENDENT`.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
clean reconstruction ≠ authentic historical recovery
```

Operator-controlled local sources and source-admission decisions remain outside this bounded architecture work.

## Track C — Clean Reference Implementation

**Status:** `PRESERVED / ACTIVE FOR MAINTENANCE / PARTIAL / NOT PRODUCTION-READY`.

```text
P1–P5 + C4 + C5: preserved bounded reference laboratory
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
assertion map:              45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:                     0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
production_authorized:      false
```

## Independent pending decisions

### License and publication — Issue #18

`PENDING_OPERATOR / selected_option: null`. No license change, open contribution regime or package publication is authorized.

### Reducer referential semantics — Issue #74 / ADR-0024

`PROPOSED / PENDING_OPERATOR / RUNTIME NOT AUTHORIZED`. Reducer v1 remains immutable; A9 does not decide successor topology, reducer-v2 semantics, cycles, self-supersession, or migration.

### Semantic-conflict ADR — ADR-0003

`PROPOSED / NOT_STARTED`. A7–A9 preserve compatible blueprint semantics but do not promote its proposed conflict Event vocabulary.

## Downstream contract work

Existing accepted/versioned contracts remain historical and usable within their scope. Later integrated review must reconcile them under the completed blueprint rather than silently promote current mechanisms.

```text
complete A1–A10 blueprint
→ integrated review
→ reconcile accepted contract families
→ define named semantic/substrate equivalence if warranted
→ decide portable history commitment if required
→ resolve ADR-0024 only if reducer work resumes
→ separate operator decision before runtime expansion
```

## Blueprint completion gate

The phase is complete only when:
- all ten deliverables are present and linked;
- terminology is reconciled;
- contradictions/unknowns remain explicit;
- implementation-specific assumptions are labelled;
- falsification criteria are recorded;
- existing contracts/runtime are mapped without automatic authority;
- contrasting substrate thought experiments exist;
- critical review is recorded;
- operator separately approves the next phase.

## Explicit non-claims

```text
A1-A9 drafted ≠ independent approval or integrated blueprint approval
A9 classification ≠ current mechanisms are universal Canon
PostgreSQL + SQLite C3 ≠ independent-language equivalence ≠ arbitrary-substrate portability proof
profile-specific ≠ architectural defect ≠ automatic deletion
A8 substrate-independence ≠ universal portability proof
blueprint documentation ≠ implementation evidence
reference laboratory ≠ final architecture
write order ≠ semantic precedence
C5 PASS ≠ production readiness
public repository ≠ open-source license
```

## Promotion rule

```text
research question
→ ontology / semantic law
→ abstract machine / contract
→ failure and falsification cases
→ explicit decision
→ bounded implementation profile
→ reproducible evidence
→ separate promotion decision
```

The pre-refoundation roadmap remains in Git history as historical context, not active authority.
