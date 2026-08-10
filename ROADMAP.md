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
- `A7 — Conflict, Uncertainty, and Revision`: [English](docs/A7_CONFLICT_UNCERTAINTY_AND_REVISION.md) · [Русский](docs/A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md).

A1–A7 remain pending independent review and integrated blueprint review with A8–A10. The next bounded content slice is `A8 — Substrate-independence Contract`.

```text
A1 Purpose and Non-goals                         DRAFTED / PROVISIONAL
→ A2 Knowledge and Memory Ontology              DRAFTED / PROVISIONAL
→ A3 Abstract Native Kernel Machine             DRAFTED / PROVISIONAL
→ A4 Semantic Laws and Invariants               DRAFTED / PROVISIONAL
→ A5 Identity / Time / Change                   DRAFTED / PROVISIONAL
→ A6 Knowledge Lifecycle                        DRAFTED / PROVISIONAL
→ A7 Conflict / Uncertainty / Revision          DRAFTED / PROVISIONAL
→ A8 Substrate-independence Contract            NEXT BOUNDED SLICE
→ A9 Reference Laboratory Boundary
→ A10 Open Questions / Falsification
→ integrated blueprint review
→ operator decision on reopening runtime work
```

### A7 contribution

A7 candidate `nk-conflict-uncertainty-revision/A7-draft-1` refines conflict, uncertainty, and revision as substrate-neutral meaning-level obligations without selecting a universal winner algorithm or accepting proposed runtime mechanisms.

It establishes three independent axes:

```text
tension kind ≠ assessment status ≠ resolution status
```

Assessment distinguishes `CANDIDATE`, `ESTABLISHED`, `NOT_A_CONFLICT`, and `UNRESOLVED_ASSESSMENT`; resolution distinguishes `UNRESOLVED`, `DEFERRED`, `RESOLVED_FOR_SCOPE`, and `REOPENED`. A resolved-for-scope decision remains scoped/accountable and is not converted into objective truth.

A7 refines the accepted `NK-CFL` family with a provisional taxonomy covering technical and semantic tensions, typed `UNCERTAINTY_POSITION`, a `TENSION_POSITION` / Conflict Set semantic pattern, Authority boundaries, scoped resolution modes, explicit `EPISTEMIC_REVISION`, reversibility/reopening, and the ability to remain undecided. It preserves A4-L21/L22/L24, A5 lineage, and A6 lifecycle semantics.

A7 explicitly reconciles existing boundaries without silently deciding them:

- ADR-0003 remains `PROPOSED / NOT_STARTED`; A7 does not accept its proposed Event lifecycle;
- `CONFLICT_OPENED`, `CONFLICT_REVIEWED`, `CONFLICT_RESOLVED`, and `CONFLICT_REOPENED` are not authorized Event verbs;
- Issue #74 / ADR-0024 remains `PROPOSED / PENDING_OPERATOR`; A7 does not decide one/multi-successor topology, self-supersession, cycles, or reducer-v2 migration;
- P1–C5 remains a bounded reference laboratory and does not gain A7 runtime-conformance evidence;
- Issue #14/#15/#16/#17, Issue #18 and Track H retain their scopes.

### A6 contribution

A6 candidate `nk-knowledge-lifecycle/A6-draft-1` models the knowledge lifecycle as a labeled directed graph of nine recurring phases (`ENCOUNTERED`, `RETAINED`, `POSITIONED`, `EPISTEMICALLY_WEIGHED`, `RELATIONALLY_INTEGRATED`, `IN_TENSION`, `REVISED_OR_SUPERSEDED`, `DISPOSED`, `ACCOUNTED`) rather than a linear pipeline, each mapped to one or more of A3's thirteen transition families. A7 refines the conflict/uncertainty/revision semantics around those phases without changing the phase inventory.

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

`PROPOSED / PENDING_OPERATOR / RUNTIME NOT AUTHORIZED`. Reducer v1 remains immutable; A7 does not decide successor topology, reducer-v2 semantics, or `REVISED_OR_SUPERSEDED` successor/cycle rules.

### Semantic-conflict ADR — ADR-0003

`PROPOSED / NOT_STARTED`. A7 refines compatible blueprint semantics but does not change ADR-0003's decision status or promote its proposed conflict Event vocabulary.

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
A1-A7 drafted ≠ independent approval or integrated blueprint approval
A7 draft ≠ accepted universal conflict/truth engine
A7 draft ≠ acceptance of ADR-0003
A7 draft ≠ conflict Event runtime
A7 draft ≠ universal confidence/probability algebra
A7 draft ≠ ADR-0024/reducer-v2 decision
blueprint documentation ≠ implementation evidence
reference laboratory ≠ final architecture
future-facing design ≠ demonstrated future substrate support
semantic identity ≠ storage identity
write order ≠ semantic precedence
Conflict detection ≠ conflict resolution
resolution-for-scope ≠ objective truth
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