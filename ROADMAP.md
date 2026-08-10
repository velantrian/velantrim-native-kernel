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
- `A9 — Reference Laboratory Boundary`: [English](docs/A9_REFERENCE_LABORATORY_BOUNDARY.md) · [Русский](docs/A9_REFERENCE_LABORATORY_BOUNDARY.ru.md);
- `A10 — Open Questions and Falsification`: [English](docs/A10_OPEN_QUESTIONS_AND_FALSIFICATION.md) · [Русский](docs/A10_OPEN_QUESTIONS_AND_FALSIFICATION.ru.md).

A1–A10 remain pending independent review and integrated blueprint review. The next bounded gate is `INTEGRATED_A1_A10_REVIEW`.

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
→ A10 Open Questions and Falsification           DRAFTED / PROVISIONAL
→ integrated A1-A10 review                     NEXT GATE
→ operator decision on reopening runtime work
```

### A10 contribution

A10 candidate `nk-open-questions-falsification/A10-draft-1` converts the remaining uncertainty into a falsifiable research boundary instead of silently treating unknowns as success.

It defines five research outcomes — `SUPPORTED_FOR_SCOPE`, `WEAKENED`, `REFUTED`, `INDETERMINATE`, `NOT_TESTED` — with the explicit rule `NOT_TESTED ≠ SUPPORTED`.

A10 records twelve major provisional hypotheses with weakening/refutation conditions and eighteen open questions covering minimum explicit history, reconstruction without exact replay, lossy identity, independent-language evidence, analog/neuromorphic continuity, probabilistic conformance, forgetting and physical deletion observability, bounded memory, causal order without global sequence, decentralized Authority, derived-state boundaries, semantic-equivalence observables, contract reclassification, non-classical computation, self-modification and evidence independence.

Contrasting thought experiments cover eventless archives, distributed neuromorphic memory, lossy bounded-memory agents, probabilistic realizations and independent-language digital profiles. These are falsification aids, not implementation commitments.

A10 also defines explicit stop conditions: contradictions across A1–A9, non-falsifiable tests, reproducible counterexamples inside claimed scope, or runtime work needed only to make an architecture claim appear true require reopening assumptions rather than silent promotion.

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

`PROPOSED / PENDING_OPERATOR / RUNTIME NOT AUTHORIZED`. Reducer v1 remains immutable; A10 does not decide successor topology, reducer-v2 semantics, cycles, self-supersession, or migration.

### Semantic-conflict ADR — ADR-0003

`PROPOSED / NOT_STARTED`. A7–A10 preserve compatible blueprint semantics but do not promote its proposed conflict Event vocabulary.

## Downstream contract work

Existing accepted/versioned contracts remain historical and usable within their scope. Integrated review must reconcile them under the drafted blueprint rather than silently promote current mechanisms.

```text
A1–A10 drafted blueprint
→ integrated A1-A10 review
→ reconcile accepted contract families
→ define named semantic/substrate equivalence if warranted
→ decide portable history commitment if required
→ resolve ADR-0024 only if reducer work resumes
→ separate operator decision before runtime expansion
```

## Blueprint completion gate

The draft inventory now contains all ten deliverables. The architecture phase is still not accepted until:
- terminology is reconciled across A1–A10;
- contradictions/unknowns remain explicit;
- implementation-specific assumptions remain labelled;
- falsification criteria cover major hypotheses;
- existing contracts/runtime are mapped without automatic authority;
- contrasting substrate thought experiments are reviewed;
- critical integrated review is recorded;
- operator separately approves the next phase.

## Explicit non-claims

```text
A1-A10 drafted ≠ independent approval or integrated blueprint approval
A10 falsification inventory ≠ proof of its hypotheses
PostgreSQL + SQLite C3 ≠ independent-language equivalence ≠ arbitrary-substrate portability proof
A8 substrate-independence ≠ universal portability proof
blueprint documentation ≠ implementation evidence
reference laboratory ≠ final architecture
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
