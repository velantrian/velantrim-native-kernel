# 🧬 Velantrim Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

### Technology-neutral architecture for durable knowledge, memory, change, and explanation

> **Current state:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`  
> **Active phase:** `POST-BLUEPRINT VALIDATION / IAR-1 RECONCILED / BPV1 PLAN NEXT / RUNTIME EXPANSION FROZEN`

Velantrim Native Kernel studies what semantic meaning, identity, provenance, time, uncertainty, conflict, revision, and explanation should survive when databases, languages, models, processors, and storage media change.

It is **not** an operating-system kernel, database product, LLM memory plugin, vector store, or Python framework definition.

```text
first define problem-level meaning and candidate obligations
        ↓
preregister scope, observables, threat/grounding assumptions and failure rules
        ↓
derive a replaceable bounded realization independently
        ↓
map it against provisional reference taxonomies
        ↓
test and falsify the architectural claims
```

## Architecture boundary

```text
Problem-level Purpose and Candidate Semantic Obligations
→ Preregistered Conformance / Threat / Grounding Boundary
→ Independently Derived Bounded Realization
→ Replaceable Implementation or Falsification Instrument
→ Positive + Adversarial Negative Fixtures
→ Cross-lineage Semantic Comparison
→ Evidence
→ Outcome / Status / Maturity
```

Python, JSON, SHA-256, PostgreSQL, SQLite, graphs, vectors, LLMs, conventional hardware, event sourcing, exact replay, and CI are replaceable research instruments. They are not permanent Canon.

The current Python/PostgreSQL/SQLite lineage is a **bounded reference laboratory**, not the final definition of Native Kernel. IAR-1 additionally established that the full A3 transition/outcome machine, A6 lifecycle graph, current Event/reducer/Receipt shape, and exact reconstruction are not yet justified as the universal minimum Kernel form.

## Current state

```text
clean_runtime_support:       PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false

assertion map: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:        0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
```

C5 does not promote semantic assertions and does not authorize production.

## Checkpoint model

Machine-readable truth is recorded in [`project-state.json`](project-state.json) under `nk-project-state/2`.

| Role | Checkpoint |
|---|---|
| Machine truth reconciliation | `d9eee591de308a689ace940c2efe58c9e8a137f2` |
| Human truth reconciliation | `07549a0cd952b4e06b61ef24d21b2dcdbc9f861d` |
| Issues and Notion reconciliation record | `cdf559a3a32decd538e4cab3dd7fb591fc6e9322` |
| Publication checkpoint | `10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c` |
| Runtime checkpoint | `675aa4b398a2fc0181dc71d38904a2d33a09f5f8` |
| Runtime integrity checkpoint | `a1cdc6d8f36d67f40f065641809bc6da463c10a4` |
| Evidence-producing checkpoint | `296981ae84ad5bdab5dabbec9b7b9ebb43af63d7` |
| Manifest source / Notion synchronized descendant | `70acd0da61fee19131947aa56125833adb156ced` |

The publication checkpoint remains the PR #83 decision-package identity. The later PR #86 Notion checkpoint does not rewrite or replace it. Live `main` is resolved from GitHub or the checked-out Git ref; committed state does not predict its own future merge SHA.

## Truth reconciliation

```text
machine-readable truth: COMPLETE / PR #80
human-readable truth:   COMPLETE / PR #81
Issues #14–#17:         RECONCILED / OPEN / PR #82
publication checkpoint: PR #83
Notion dashboard:       COMMITTED CHECKPOINT THROUGH PR #86
checkpoint role repair: COMPLETE / PR #87
```

The exact committed Notion checkpoint above is historical. Newer live Notion content must be read directly and is synchronized again after material GitHub merges. Historical reports and proposals remain preserved but do not override current state.

## Current evidence

Two immutable C5 evidence identities are repository-resident:

```text
evidence/c5/2026-08-07/manifest.json
evidence/c5/2026-08-08-adr0023/manifest.json
```

ADR-0023 sets linked SQLite `3.51.3` as the current WAL floor. Historical SQLite `3.45.1` artifacts remain unchanged and version-bound.

```text
repository-resident evidence
≠ independent custody
≠ complete authenticity
≠ live-data safety
≠ physical deletion
≠ production readiness
```

ADR-0025, ADR-0026, IAR-1 and IAR-1-R1 do not expand any existing runtime/evidence proof boundary.

## Three independent tracks

```text
H — Historical Recovery
  authentic v0.1.2.1 and original 44-test suite
  NOT_FOUND_IN_ACCESSIBLE_SOURCES / OPEN / INDEPENDENT

C — Clean Reference Implementation
  P1–P5 + C4 + C5
  PRESERVED / PARTIAL / BOUNDED REFERENCE LABORATORY

R — Post-Blueprint Validation
  A1–A10 + integrated review remain provisional
  IAR-1 QUALIFYING / IAR-1-R1 COMPLETE
  ACTIVE / BPV1 PLAN NEXT / NO AUTOMATIC PROMOTION
```

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
reference laboratory ≠ final architecture
```

## Active architecture phase

ADR-0025 established blueprint-before-runtime. A1–A10 and the first integrated review remain `DRAFTED / PROVISIONAL` architecture work.

ADR-0026 records the operator-approved **Option D** validation route. IAR-1 has now completed the independent challenge and IAR-1-R1 has reconciled all ten findings without promoting Final Canon:

```text
A1–A10 provisional blueprint
→ integrated review                         COMPLETE / PROVISIONAL
→ operator post-blueprint decision          OPTION D / ADR-0026 / APPROVED
→ INDEPENDENT_ARCHITECTURE_REVIEW           COMPLETE / IAR-1 / QUALIFYING
→ REVIEW_FINDING_RECONCILIATION             COMPLETE / IAR-1-R1
→ BPV1_PLAN_AND_PREREGISTRATION             NEXT GATE
→ BPV-1 bounded cross-lineage falsification BLOCKED BY PREREGISTERED PLAN
→ A10 outcome classification
→ integrated re-review
→ separate later operator Canon/runtime decision
```

Current boundaries:

```text
independent architectural validation: IAR-1 QUALIFYING_REVIEW_COMPLETE
IAR-1 findings: 10 total / 7 BLOCKING / 3 MATERIAL
IAR-1-R1: COMPLETE / open blockers 0 / open material 0
BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN
runtime expansion: FROZEN
product runtime thaw: NO
A1-A10 Final Canon: NOT AUTHORIZED
production: false
```

IAR-1 did **not** prove the architecture correct. It materially weakened it. The current candidate minimum is problem-level: non-conflation of representation/Claim with reality/truth; explicit scope/Context/warrant/Authority assumptions where material; explicit Unknown/uncertainty/unsupported states; accountable change/retention/loss for declared scope; and preregistered equivalence/degradation/refutation conditions.

Before BPV-1 execution, its plan must freeze `scenario_id`, purpose scope, mandatory obligations, applicability rules, mandatory observables, equivalence predicates, allowed declared losses, failure thresholds, hard refutation observations, grounding mode, threat model, and oracle Authority. Post-execution changes to those normative fields cannot rescue the run; they require a new experiment identity.

Plan: [English](docs/ARCHITECTURE_REFOUNDATION.md) · [Русский](docs/ARCHITECTURE_REFOUNDATION.ru.md).  
Blueprint decision: [`ADR-0025`](docs/adr/0025-blueprint-before-runtime-expansion.md).  
Post-blueprint decision: [`ADR-0026`](docs/adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md).  
Independent-review protocol: [English](docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md) · [Русский](docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md).  
IAR-1 result: [English](docs/reviews/IAR-1_RESULT.md) · [Русский](docs/reviews/IAR-1_RESULT.ru.md) · [JSON](docs/reviews/IAR-1_RESULT.json).  
IAR-1 reconciliation: [English](docs/reviews/IAR-1_RECONCILIATION.md) · [Русский](docs/reviews/IAR-1_RECONCILIATION.ru.md) · [JSON](docs/reviews/IAR-1_RECONCILIATION.json).  
Tracking: [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88).

During the freeze, architecture research, BPV-1 planning/preregistration, integrity, security, reproducibility, provenance, evidence-preservation, truth-surface, and historical-recovery work remains allowed. BPV-1 execution remains forbidden until its preregistered plan is authoritative. New product semantic/runtime features remain unauthorized.

## Pending decisions

```text
Issue #18 — license/publication
  PENDING_OPERATOR / selected_option: null
  blocks open contributions and package publication

Issue #74 / ADR-0024 — reducer referential semantics
  PROPOSED / PENDING_OPERATOR / selected_option: null
  blocks reducer-v2 work
```

Neither decision is silently decided by ADR-0026 or IAR-1-R1. Track H source admission also remains operator-controlled.

Runtime work may be reconsidered only through a later explicit operator decision after validation. BPV-1 itself is not product runtime and cannot authorize reducer-v2 or any other runtime expansion.

## Human quickstart

The current laboratory requires Python 3.11 or 3.12:

```bash
python -m unittest discover -s tests -p 'test_semantic_core.py' -v
python -m unittest discover -s tests -p 'test_p1_manifest.py' -v
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_architecture_freeze.py --repo .
python tools/ai_context/validate_context.py --repo .
```

> **SQLite profile warning:** P5/C3/C4/C5 fail closed when the Python process is linked against SQLite older than `3.51.3`. Do not treat a system SQLite rejection as a semantic failure. Build/use the pinned safe SQLite library before running those profile checks.

For the pinned-library setup, PostgreSQL DSN, and full P4/P5/C3/C4/C5 commands, use [`docs/QUICKSTART.md`](docs/QUICKSTART.md).