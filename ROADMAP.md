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
- `A5 — Identity, Time, and Change`: [English](docs/A5_IDENTITY_TIME_AND_CHANGE.md) · [Русский](docs/A5_IDENTITY_TIME_AND_CHANGE.ru.md).

A1–A5 remain pending independent review and integrated blueprint review with A6–A10. The next bounded content slice is `A6 — Knowledge Lifecycle`.

```text
A1 Purpose and Non-goals                         DRAFTED / PROVISIONAL
→ A2 Knowledge and Memory Ontology              DRAFTED / PROVISIONAL
→ A3 Abstract Native Kernel Machine             DRAFTED / PROVISIONAL
→ A4 Semantic Laws and Invariants               DRAFTED / PROVISIONAL
→ A5 Identity / Time / Change                   DRAFTED / PROVISIONAL
→ A6 Knowledge Lifecycle                        NEXT BOUNDED SLICE
→ A7 Conflict / Uncertainty / Revision
→ A8 Substrate-independence Contract
→ A9 Reference Laboratory Boundary
→ A10 Open Questions / Falsification
→ integrated blueprint review
→ operator decision on reopening runtime work
```

### A5 contribution

A5 candidate `nk-identity-time-change/A5-draft-1` treats identity as a typed/scoped relation rather than one universal identifier. It distinguishes referent, semantic-content, Claim-position, Record, lineage-continuity, occurrence and substrate-local identity; preserves `UNRESOLVED` identity; separates multiple temporal dimensions and ordering relations; and classifies correction, Revision, Supersession, restriction, erasure and forgetting without collapsing them.

A5 explicitly reconciles existing contracts without silently superseding them:

- `nk-id/1.0` remains a versioned current reference encoding; JSON/NFC/SHA-256 is not universalized;
- `global_seq` / `stream_seq` remain reference-laboratory write/order mechanisms, not occurrence/causal Canon;
- the current deletion state machine remains a bounded profile mechanism;
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

`PROPOSED / PENDING_OPERATOR / RUNTIME NOT AUTHORIZED`. Reducer v1 remains immutable; A5 does not decide successor topology or reducer-v2 semantics.

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
A1-A5 drafted ≠ independent approval or integrated blueprint approval
A5 draft ≠ accepted universal identity/time theory
A5 draft ≠ runtime Temporal implementation
A5 draft ≠ supersession of nk-id/1.0, nk-event/1.0, or nk-deletion/1.0
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
