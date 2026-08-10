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
- `A6 — Knowledge Lifecycle`: [English](docs/A6_KNOWLEDGE_LIFECYCLE.md) · [Русский](docs/A6_KNOWLEDGE_LIFECYCLE.ru.md).

A1–A6 remain pending independent review and integrated blueprint review with A7–A10. The next bounded content slice is `A7 — Conflict, Uncertainty, and Revision`.

```text
A1 Purpose and Non-goals                         DRAFTED / PROVISIONAL
→ A2 Knowledge and Memory Ontology              DRAFTED / PROVISIONAL
→ A3 Abstract Native Kernel Machine             DRAFTED / PROVISIONAL
→ A4 Semantic Laws and Invariants               DRAFTED / PROVISIONAL
→ A5 Identity / Time / Change                   DRAFTED / PROVISIONAL
→ A6 Knowledge Lifecycle                        DRAFTED / PROVISIONAL
→ A7 Conflict / Uncertainty / Revision           NEXT BOUNDED SLICE
→ A8 Substrate-independence Contract
→ A9 Reference Laboratory Boundary
→ A10 Open Questions / Falsification
→ integrated blueprint review
→ operator decision on reopening runtime work
```

### A6 contribution

A6 candidate `nk-knowledge-lifecycle/A6-draft-1` models the knowledge lifecycle as a labeled directed graph of nine recurring phases (`ENCOUNTERED`, `RETAINED`, `POSITIONED`, `EPISTEMICALLY_WEIGHED`, `RELATIONALLY_INTEGRATED`, `IN_TENSION`, `REVISED_OR_SUPERSEDED`, `DISPOSED`, `ACCOUNTED`) rather than a linear pipeline, each mapped to one or more of A3's thirteen transition families. It defines a typed `LIFECYCLE_TRANSITION` relation reusing A3's outcome vocabulary; separates `LIFECYCLE_TRANSITION_ORDER` from occurrence/causal/write-commit order; and extends A3's eight dispositions with three closure kinds resolving the erasure/forgetting distinctions A5 deferred.

A6 explicitly reconciles existing contracts without silently superseding them:

- the illustrative P1–C5 Event-to-phase mapping (`ADMIT`/`LINK`/`UTILIZED`/`SUPERSEDED`/`ERASED`) is non-canonical and authorizes no new Event verbs;
- `global_seq` / `stream_seq` remain reference-laboratory ordering mechanisms, not `LIFECYCLE_TRANSITION_ORDER` itself;
- Issue #14/#15/#16 retain their established scopes;
- Issue #74 / ADR-0024 and Issue #18 remain untouched/operator-controlled.

## Runtime freeze

Allowed during the freeze:
- architecture and ontology research;
- integrity/security/reproducibility/provenance fixes;
- evidence preservation;
- validator/current-truth repairs;
- historical recovery;
- isolated falsification experiments with no runtime promotion.

Not authorized without a separate explicit operator decision:
- reducer v2 or new semantic Event verbs;
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

`PROPOSED / PENDING_OPERATOR / RUNTIME NOT AUTHORIZED`. Reducer v1 remains immutable; A6 does not decide successor topology, reducer-v2 semantics, or `REVISED_OR_SUPERSEDED` successor/cycle rules.

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
A1-A6 drafted ≠ independent approval or integrated blueprint approval
A6 draft ≠ accepted universal lifecycle theory
A6 draft ≠ runtime Temporal implementation
A6 draft ≠ supersession of nk-id/1.0, nk-event/1.0, or nk-deletion/1.0
blueprint documentation ≠ implementation evidence
reference laboratory ≠ final architecture
future-facing design ≠ demonstrated future substrate support
semantic identity ≠ storage identity
equal bytes/hash/text ≠ universal semantic identity
write order ≠ represented-world or causal order
Revision ≠ silent overwrite
Supersession ≠ deletion or falsity
C5 PASS ≠ production readiness
PostgreSQL + SQLite ≠ full substrate neutrality
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
