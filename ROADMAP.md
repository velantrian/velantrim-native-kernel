# Roadmap

```yaml
document_role: ACTIVE_ROADMAP
status_as_of: 2026-08-09
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

Their status, evidence, and authority must never be collapsed.

## Governing sequence

```text
Architecture purpose and ontology
→ abstract Kernel machine
→ semantic laws and invariants
→ versioned abstract contracts
→ failure and threat models
→ explicit decisions
→ replaceable implementation profiles
→ positive and negative fixtures
→ cross-profile comparison
→ exact evidence
→ status update
→ Notion synchronization
```

Runtime must not define new semantics before the blueprint and contract. Evidence must not be relabelled after the fact. Maturity does not rise automatically because more tests passed.

## Active priority — Architecture Re-foundation

**State:** `ACTIVE / BLUEPRINT-FIRST / RUNTIME EXPANSION FROZEN`.

Decision: [`ADR-0025`](docs/adr/0025-blueprint-before-runtime-expansion.md).  
Plan: [English](docs/ARCHITECTURE_REFOUNDATION.md) · [Русский](docs/ARCHITECTURE_REFOUNDATION.ru.md).  
Issue: [#88](https://github.com/velantrian/velantrim-native-kernel/issues/88).

The project now completes the architecture blueprint before further semantic/runtime expansion. `A1` is drafted: [English](docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.md) · [Русский](docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md), pending independent review and integrated blueprint review with `A2`–`A10`. The next bounded content slice is `A2 — Knowledge and Memory Ontology`.

```text
A1 Purpose and Non-goals
→ A2 Knowledge and Memory Ontology
→ A3 Abstract Native Kernel Machine
→ A4 Semantic Laws and Invariants
→ A5 Identity / Time / Change
→ A6 Knowledge Lifecycle
→ A7 Conflict / Uncertainty / Revision
→ A8 Substrate-independence Contract
→ A9 Reference Laboratory Boundary
→ A10 Open Questions / Falsification
→ integrated blueprint review
→ operator decision on reopening runtime work
```

### Runtime freeze

The existing P1–C5 lineage is preserved as a bounded reference laboratory. It is not the final definition of Native Kernel.

Allowed during the freeze:

- architecture and ontology research;
- integrity, security, reproducibility, and provenance fixes;
- evidence preservation;
- validator and current-truth repairs;
- historical recovery;
- isolated experiments that test or falsify a blueprint assumption without runtime promotion.

Not authorized without a separate explicit operator decision:

- reducer v2;
- new semantic Event verbs;
- new databases, language ports, model adapters, or ecosystem integrations;
- executable NK-EPI, Temporal, full Admission, or operational deletion;
- performance-driven semantic changes;
- maturity or production promotion.

## Track H — Historical Recovery

**Status:** `BLOCKED / ACTIVE EVIDENCE-RECOVERY / INDEPENDENT`.

Purpose: recover authentic `v0.1.2.1` source and the original 44-test suite from permitted sources.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
clean reconstruction ≠ authentic historical recovery
```

A candidate must be preserved read-only, hashed before extraction, inspected in isolation, recorded as `UNVERIFIED_CANDIDATE`, reviewed for provenance, and accepted only by an explicit operator decision.

## Track C — Clean Reference Implementation

**Status:** `PRESERVED / ACTIVE FOR MAINTENANCE / PARTIAL / NOT PRODUCTION-READY`.

```text
P1 semantic core                         MERGED / REPOSITORY-TESTED
P2 PostgreSQL append                     MERGED / REPOSITORY-INTEGRATION-TESTED
P3 replay / projections / Receipts       MERGED / REPOSITORY-INTEGRATION-TESTED
P4 PostgreSQL assertion conformance      MERGED / PARTIAL / C2
P5 SQLite + cross-profile comparison     MERGED / PARTIAL / C2 + C3
C4 offline shadow evaluation             MERGED / PARTIAL
C5 bounded operational rehearsal         MERGED / PARTIAL / SYNTHETIC

kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
assertion map:              45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:                     0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
production_authorized:      false
```

The clean implementation may receive maintenance and integrity fixes under ADR-0025. It may not expand semantic scope while the blueprint gate remains open.

## Completed reconciliation phases

```text
0A machine-readable truth              COMPLETE / PR #80
0B human-readable truth                COMPLETE / PR #81
0C Issues and publication              COMPLETE / PR #82 + PR #83
0D Notion descendant synchronization   COMPLETE / PR #86
0E checkpoint-role validator repair    COMPLETE / PR #87
```

Live `main` is resolved through GitHub or a checked-out ref. Committed checkpoint records remain non-self-referential.

## Independent pending decisions

### License and publication — Issue #18

**State:** `PACKAGE PREPARED / PENDING_OPERATOR / selected_option: null`.

Until explicit selection:

```text
license change: NO
external contributions: NOT ACCEPTED
package publication: NOT AUTHORIZED
```

This decision does not block architecture research. It blocks an open contribution/publication regime.

### Reducer referential semantics — Issue #74 / ADR-0024

**State:** `PROPOSED / PENDING_OPERATOR / RUNTIME NOT AUTHORIZED`.

Reducer v1 remains immutable. ADR-0024 is required only before a reducer-v2 path is reopened; Architecture Re-foundation does not accept, reject, or bypass it.

## Downstream contract work

NK-SAM, named equivalence profiles, and Event/history commitment remain required. Their final forms must derive from the integrated blueprint rather than from current Python/SQL convenience.

```text
complete blueprint
→ reconcile accepted contract families
→ define NK-SAM and named equivalence
→ define portable Event/history commitment
→ decide ADR-0024 outcome when reducer work resumes
→ only then reducer-v2 runtime
```

## Blueprint completion gate

The phase is complete only when:

- all ten deliverables are present and linked;
- terminology is reconciled;
- contradictions and unknowns remain explicit;
- implementation-specific assumptions are labelled;
- falsification criteria are recorded;
- existing contracts and runtime are mapped without automatic authority;
- at least two contrasting substrate thought experiments are documented;
- critical review is recorded;
- the operator approves the next phase separately.

## Explicit non-claims

```text
blueprint documentation ≠ implementation evidence
reference laboratory ≠ final architecture
future-facing design ≠ future substrate support
C5 PASS ≠ production readiness
PostgreSQL + SQLite ≠ full substrate neutrality
public repository ≠ open-source license
```

## Promotion rule

```text
research question
→ ontology and semantic law
→ abstract machine / contract
→ failure and falsification cases
→ explicit decision
→ bounded implementation profile
→ reproducible evidence
→ separate promotion decision
```

The pre-refoundation roadmap remains available through Git history. It is historical context, not the active sequence.
