# 🤖 Velantrim Native Kernel repository guidance

## Required reading order

Before searching code, creating a branch, or proposing architecture changes, read:

1. `README.md`
2. `STATUS.md`
3. `project-state.json`
4. `docs/ai/README.md`
5. `docs/ai/CURRENT_STATE.md`
6. `docs/ai/KNOWN_RISKS.md`
7. `ROADMAP.md`
8. `docs/ARCHITECTURE_REFOUNDATION.md`
9. `docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md`
10. `docs/reviews/IAR-1_RESULT.md` and `docs/reviews/IAR-1_RESULT.json`
11. `docs/reviews/IAR-1_RECONCILIATION.md` and `docs/reviews/IAR-1_RECONCILIATION.json`
12. `docs/research/BPV1_PREREGISTRATION.md` and `docs/research/BPV1_PREREGISTRATION.json`
13. affected Canon, contracts, and ADRs
14. affected source, tests, workflows, and evidence records
15. current GitHub PRs, issues, Actions, and review threads
16. corresponding Notion current-state pages

Do not begin with random repository search. Verify live state first.

## Current maturity

```text
RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
clean_runtime_support:       PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false

assertions: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:    0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
```

Machine-readable truth uses `project-state.json` protocol `nk-project-state/2`. Live HEAD must be resolved through Git or GitHub; committed checkpoint metadata does not attempt to contain its own future merge SHA.

## Three independent tracks

```text
H — Historical Recovery
  authentic v0.1.2.1 + original 44-test suite
  OPEN / BLOCKED / independent

C — Clean Reference Implementation
  P1–P5 + C4 + C5
  PRESERVED / PARTIAL / bounded reference laboratory

R — Architecture Re-foundation and Post-Blueprint Validation
  ACTIVE / IAR-1-RECONCILED / BPV1-PREREGISTERED / EXECUTION-ADMISSION-NEXT
```

Never collapse these tracks.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
research proposal ≠ accepted contract ≠ runtime
reference laboratory ≠ final architecture
```

## Active operator-approved priority

ADR-0025 established **Architecture Re-foundation / Blueprint-first**. A1–A10 and the first integrated review remain provisional architecture work.

ADR-0026 records the operator-selected post-blueprint **Option D**:

```text
A1-A10 provisional blueprint
→ independent architecture review            COMPLETE / IAR-1 / QUALIFYING
→ review finding reconciliation              COMPLETE / IAR-1-R1
→ BPV1 plan and preregistration              COMPLETE / PR #110
→ BPV1 execution admission                   NEXT
→ one bounded cross-lineage falsification instrument (BPV-1)
→ A10 outcome classification
→ integrated re-review
→ separate later operator Canon/runtime decision
```

The active gate is `BPV1_EXECUTION_ADMISSION`.

```text
qualifying independent review ≠ architecture proof
review reconciliation ≠ BPV-1 execution authorization
preregistered plan ≠ BPV-1 execution authorization
operator approval ≠ independent validation
BPV-1 ≠ product runtime
BPV-1 outcome ≠ automatic Canon promotion
```

IAR-1 is `QUALIFYING_REVIEW_COMPLETE`. IAR-1-R1 reconciliation is `COMPLETE`. All ten review findings have explicit reconciliation records; source review evidence remains preserved.

BPV-1 plan `BPV1-001-cross-lineage-bounded-accountability-v1` is `PREREGISTERED / EXECUTION_NOT_AUTHORIZED` at authoritative plan merge `a538d7f1e28858a88b9ee777ac7d6e05b85943db`. BPV-1 execution is `BLOCKED_PENDING_EXECUTION_ADMISSION`.

### Allowed during the freeze

- architecture and ontology research;
- BPV-1 execution-admission packaging derived from the frozen plan;
- integrity, security, reproducibility, and provenance fixes;
- evidence preservation;
- validator and truth-surface repairs;
- historical recovery;
- later isolated BPV-1 execution only after a separate authoritative execution-admission checkpoint.

### Not authorized during the freeze

- BPV-1 subject implementation/execution before execution admission;
- changes to preregistered normative fields under the same scenario identity;
- product runtime thaw;
- reducer v2 or new Event semantics;
- new product databases, language/runtime profiles, LLM/vector adapters, or ecosystem integrations;
- executable NK-EPI, Temporal, full Admission, or operational deletion;
- performance-driven semantic changes;
- Final Canon promotion;
- maturity or production promotion.

Rust in BPV-1 is an experimental cross-language instrument only. It is not a product profile and not a Canon requirement. Independent team/custody and independent computation model remain `NOT_ESTABLISHED` for BPV1-001.

## Independent-review, reconciliation, and preregistration discipline

IAR-1 followed `nk-independent-architecture-review/1` and recorded a concrete independence basis. The qualifying review produced 10 findings: 7 `BLOCKING` and 3 `MATERIAL`. `IAR-1-R1` reconciles all ten without rewriting the original review evidence.

Do not reinterpret a resolved GitHub thread as deletion of the source finding. `docs/reviews/IAR-1_RESULT.json` preserves the review-local source status; `docs/reviews/IAR-1_RECONCILIATION.json` records the later disposition.

Do not self-certify future independent gates. The current assistant lineage, integrated review, CI, tests, Notion read-back, operator approval, or automated review alone do not prove the architecture correct.

The central IAR-1 result is that changing implementation language is insufficient if the experiment merely ports the existing conceptual structure. BPV1-001 therefore requires an independently derived bounded state/change/history realization and forbids reuse of the current Python domain model, Event envelope, reducer, or Receipt shape as its semantic oracle.

The preregistered plan freezes before execution exactly:

```text
scenario_id
purpose_scope
mandatory_obligations
applicability_rules
mandatory_observables
equivalence_predicates
allowed_declared_losses
failure_thresholds
hard_refutation_observations
grounding_mode
threat_model
oracle_authority
```

Post-execution normative rescoping cannot rescue an old run; it invalidates the run for the claimed scope and requires a new scenario identity.

## BPV1_EXECUTION_ADMISSION requirements

Before any subject implementation/execution, the admission checkpoint must bind:

1. authoritative plan `BPV1-001-cross-lineage-bounded-accountability-v1` and its frozen digest;
2. machine-readable fixture/oracle package derived only from that plan;
3. standalone evaluator tests passing before subject execution;
4. pinned Rust toolchain and experimental source boundary;
5. static scope audit proving no product runtime/profile integration;
6. explicit continued `runtime_expansion: FROZEN`, `product_runtime_thaw: NO`, `production_authorized: false`.

Admission may authorize only the bounded falsification instrument. It may not authorize product runtime, reducer-v2, Event semantics, NK-EPI runtime, Final Canon, production, Issue #18, Issue #74/ADR-0024, or Track H admission.

## Required architecture discipline

```text
Problem-level purpose and candidate semantic obligations
→ Preregistered scope / observables / applicability / failure thresholds
→ Explicit grounding and threat model
→ Frozen external fixture/oracle package
→ Independently derived bounded state/change/history realization
→ Positive and adversarial negative fixtures
→ Cross-lineage semantic comparison
→ Explicit PRESERVED / PARTIAL / LOSSY / UNSUPPORTED / INDETERMINATE mapping
→ Exact evidence
→ A10 outcome classification
→ Status update
→ Notion synchronization
```

Do not implement new semantics first and write the architecture afterward. Do not force a future realization to reproduce the A3 transition catalogue, A6 lifecycle graph, Event/reducer/Receipt structures, exact replay, or the current identity/time inventory as its native shape merely because those taxonomies already exist.

Python, PostgreSQL, SQLite, JSON, SHA-256, graphs, vectors, LLMs, event sourcing, exact replay, Rust, and current hardware are replaceable profiles or research instruments, not permanent Canon unless a later evidence-backed decision establishes otherwise.

## Pending decisions remain separate

```text
Issue #18 — license/publication
  PENDING_OPERATOR

Issue #74 / ADR-0024 — reducer referential semantics
  PROPOSED / PENDING_OPERATOR
  reducer-v2 NOT AUTHORIZED

Track H source admission
  operator-controlled
```

No AI agent may choose a license, accept ADR-0024, or admit Track H sources for the operator.

## Historical immutability

Do not reinterpret or rewrite published reducer-v1 histories, Event histories, Receipts, P1–C5 evidence, ZIP archives, historical checkpoint identities, fixture outputs, A1–A10 first-draft history, the first integrated-review record, IAR-1 source findings, or IAR-1-R1 publication-time gate language.

## Required distinctions

```text
Claim ≠ truth
admission ≠ objective truth
Unknown ≠ False
Architecture Canon ≠ implementation profile
reference implementation ≠ architectural authority
blueprint documentation ≠ implementation evidence
operator approval ≠ independent validation
qualifying independent review ≠ architecture proof
review reconciliation ≠ experiment execution authorization
preregistered plan ≠ execution authorization
falsification instrument ≠ product runtime
C2 ≠ C3 ≠ C4 ≠ C5
C5 operational rehearsal ≠ semantic assertion promotion
synthetic CI ≠ live production
logical Event export ≠ physical backup or disaster recovery
logical ERASED ≠ physical deletion
physical erasure ≠ cryptographic erasure
forgetting/loss ≠ deliberate erasure
bounded accountability ≠ exact reconstruction
history visibility ≠ mandatory Event sourcing
local scoped conformance ≠ composition/federation conformance
hash chain ≠ complete authenticity
Receipt/report/archive ≠ truth, compliance, or deletion proof
runtime implementation ≠ evidence
evidence ≠ operator authorization
public repository ≠ open-source license
future-facing design ≠ demonstrated future substrate support
substrate-independent specification ≠ universal portability proof
```

## Evidence discipline

Historical C5 evidence remains immutable. Future BPV-1 evidence must receive its own identity and use A10 outcomes exactly:

```text
SUPPORTED_FOR_SCOPE
WEAKENED
REFUTED
INDETERMINATE
NOT_TESTED
```

`NOT_TESTED ≠ SUPPORTED`.

## Verification

The SQLite WAL profile fails closed below linked SQLite `3.51.3`.

Minimum integrity commands:

```bash
python tools/evidence/verify_bundle.py evidence/c5/2026-08-07/manifest.json
python tools/evidence/verify_bundle.py evidence/c5/2026-08-08-adr0023/manifest.json
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_architecture_freeze.py --repo .
python tools/ai_context/validate_bpv1_preregistration.py --repo .
python tools/ai_context/validate_context.py --repo .
python tools/docs/validate_bilingual_parity.py --repo .
python -m unittest discover -s tests -p 'test_project_state.py' -v
python -m unittest discover -s tests -p 'test_architecture_freeze.py' -v
python -m unittest discover -s tests -p 'test_bpv1_preregistration.py' -v
python -m unittest discover -s tests -p 'test_ai_context_validator.py' -v
python -m unittest discover -s tests -p 'test_bilingual_parity_validator.py' -v
```

A skipped test is not PASS. An unavailable environment is `NOT_EXECUTED`.

## Review discipline

Distinguish `BOT_NOTICE`, `AUTOMATED_FINDING`, `HUMAN_REVIEW`, `QUALIFYING_INDEPENDENT_ARCHITECTURE_REVIEW`, `OPERATOR_DECISION`, and `EVIDENCE`.

A Codex quota notice is not review approval. Reproduce every actionable finding, fix or reject it with rationale, add a regression test where applicable, close the thread, and record post-merge state.

## Documentation synchronization

Material work must update relevant current-state, roadmap, risks, architecture, public English/Russian documentation, and Notion pages. GitHub must remain technically sufficient without Notion. Notion may preserve strategy, decisions, and history but must not silently contradict GitHub code, contracts, evidence, or live issue state.
