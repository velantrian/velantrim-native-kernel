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
13. `docs/research/BPV1_D5_R1_QUALIFICATION.md`
14. `docs/research/BPV1_D6_A10_CLASSIFICATION.md` and `docs/research/BPV1_D6_A10_CLASSIFICATION.json`
15. `docs/research/BPV1_D7_INTEGRATED_REREVIEW.md` and `docs/research/BPV1_D7_INTEGRATED_REREVIEW.json`
16. `docs/research/BPV1_D8_CONSOLIDATED_SYNC.md` and `docs/research/BPV1_D8_CONSOLIDATED_SYNC.json`
17. `docs/adr/0027-post-d8-residual-validation-planning.md`
18. affected Canon, contracts, ADRs, source, tests, workflows and evidence records
19. current GitHub PRs, issues, Actions and review threads
20. corresponding Notion current-state pages

Do not begin with random repository search. Verify live state first. When a lower historical section conflicts with the current ADR-0027 overlay or `project-state.json`, preserve the historical record and follow the newer current-truth layer.

## Current maturity

```text
RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
clean_runtime_support:      PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false

assertions: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:    0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
runtime expansion: FROZEN
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
  ACTIVE / OPTION D COMPLETE / ADR-0027 ACCEPTED
  RESIDUAL A10 VALIDATION PLANNING ONLY
```

Never collapse these tracks.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
research proposal ≠ accepted contract ≠ runtime
reference laboratory ≠ final architecture
```

## Active operator-approved priority

ADR-0025 established **Architecture Re-foundation / Blueprint-first**. ADR-0026 selected Option D. Option D is now complete through D8, and ADR-0027 records the separate post-D8 operator decision.

```text
A1-A10 provisional blueprint                         COMPLETE / PROVISIONAL
→ independent architecture review                    COMPLETE / IAR-1 / QUALIFYING
→ review finding reconciliation                      COMPLETE / IAR-1-R1
→ BPV1 plan and preregistration                      COMPLETE / PR #110
→ BPV1 execution admission                           COMPLETE / PR #112 + #113
→ BPV1-001 subject implementation/execution          COMPLETE / PR #114
→ D5-R1 evidence qualification                       COMPLETE / PR #115 / QUALIFIED
→ D6 A10 hypothesis classification                  COMPLETE / PR #117
→ D7 integrated re-review                           COMPLETE / PR #118
→ D8 consolidated authoritative synchronization     COMPLETE / PR #119 / 7/7
→ separate post-D8 operator decision                COMPLETE / ADR-0027
→ ADR-0027 Notion synchronization/read-back          COMPLETE / 7/7 VERIFIED
→ residual A10 validation planning                  CURRENT / RESEARCH_PLANNING_ONLY
```

The active gate is `RESIDUAL_A10_VALIDATION_PLAN`.

```text
scope: RESEARCH_PLANNING_ONLY
residual targets: A10-H03 / H06 / H08 / H09 / H10 / H11
residual experiment execution: NOT AUTHORIZED
architecture: STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL
Final Canon: DEFERRED / NOT AUTHORIZED
runtime expansion: FROZEN
product runtime thaw: NO
production: false
```

Do not infer execution authorization from planning authorization.

```text
qualifying independent review ≠ architecture proof
operator approval ≠ independent validation
SUPPORTED_FOR_SCOPE ≠ universal portability proof
NOT_TESTED ≠ SUPPORTED
planning authorization ≠ experiment execution authorization
BPV-1 ≠ product runtime
BPV-1 outcome ≠ automatic Canon promotion
```

IAR-1 is `QUALIFYING_REVIEW_COMPLETE`. IAR-1-R1 reconciliation is `COMPLETE`. All ten review findings have explicit reconciliation records; source review evidence remains preserved.

BPV-1 plan `BPV1-001-cross-lineage-bounded-accountability-v1` remains bound to authoritative plan merge `a538d7f1e28858a88b9ee777ac7d6e05b85943db` and frozen digest `7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0`.

Execution admission for BPV1-001 is a historical bounded authorization lane. It did not authorize product runtime integration, and it does not authorize any residual experiment under ADR-0027.

D5 historical execution merged via PR #114 at `a191e9c868c14af34a269dcdfae44406f1013bda`. D5-R1 qualification merged via PR #115 at `3856740570620fb2243e2f0da76359281ec4068f` and records:

```text
external qualification: QUALIFIED
frozen evaluator: SUPPORTED_FOR_SCOPE
mandatory fixtures: 12 / 12 PASS
mutations: 512
checkpoints: 128 / 256 / 512
```

D6 classified exactly:

```text
SUPPORTED_FOR_SCOPE:
  A10-H01 / A10-H02 / A10-H04 / A10-H05 / A10-H07 / A10-H12

NOT_TESTED:
  A10-H03 / A10-H06 / A10-H08 / A10-H09 / A10-H10 / A10-H11
```

Do not change any `NOT_TESTED` outcome without new qualifying evidence.

### Allowed during the freeze

- `RESIDUAL_A10_VALIDATION_PLAN` research planning for the six `NOT_TESTED` hypotheses;
- architecture and ontology research that does not mutate frozen experiment authority;
- preregistration design only after the planning artifact establishes a bounded family and a later gate authorizes that work;
- integrity, security, reproducibility, provenance and truth-surface fixes;
- evidence preservation;
- historical recovery.

### Not authorized during the freeze

- residual experiment implementation or execution without separate preregistration/admission authority;
- product runtime integration of any falsification subject;
- changes to BPV1-001 preregistered normative fields, fixture expected outcomes, thresholds, scenario identity or HR01-HR10 under the same experiment identity;
- product runtime thaw;
- reducer v2 or new Event semantics;
- new product databases, language/runtime profiles, LLM/vector adapters or ecosystem integrations;
- executable NK-EPI, Temporal, full Admission or operational deletion;
- performance-driven semantic changes;
- Final Canon promotion;
- maturity or production promotion.

Rust in BPV-1 is an experimental cross-language instrument only. It is not a product profile and not a Canon requirement. Independent team/custody and independent computation model remain `NOT_ESTABLISHED` for BPV1-001.

## D5-R1 qualification discipline

PR #115 corrected three evidence-quality weaknesses without rewriting PR #114 history:

1. the Rust subject now emits raw facts instead of structural oracle-facing PASS booleans;
2. an external qualifier derives implementation-neutral observations without reading frozen fixture expectations or private runtime state; if a required fact cannot be established, it is omitted so the unchanged evaluator can become `INDETERMINATE`;
3. semantic corruption coverage includes evidence and epistemic position, and retained loss-witness storage is internally bounded with bounded rollup.

The historical D5 evidence remains immutable; D5-R1 has a separate repository evidence identity under `experiments/bpv1/BPV1-001/results/d5-r1/`.

The specific HR10 subject-self-report adjudication path is removed for this evidence path. Do **not** reinterpret that as independent-team, independent-custody or independent-computation-model validation.

## D6 classification discipline — historical complete gate

D6 used the frozen plan plus authoritative qualified D5 evidence and only the allowed A10 outcomes:

```text
SUPPORTED_FOR_SCOPE
WEAKENED
REFUTED
INDETERMINATE
NOT_TESTED
```

Its result is immutable classification evidence for that checkpoint. Residual planning starts from the six `NOT_TESTED` hypotheses; it must not reinterpret the six supported hypotheses or broaden their scope.

## Required architecture discipline

```text
Problem-level purpose and candidate semantic obligations
→ Preregistered scope / observables / applicability / failure thresholds
→ Explicit grounding and threat model
→ Frozen external fixture/oracle package
→ Independently derived bounded realization
→ External evidence qualification
→ Frozen oracle evaluation
→ Explicit A10 outcome classification
→ Integrated re-review
→ Authoritative synchronization
→ Separate operator decision
→ Residual research planning for remaining NOT_TESTED hypotheses
→ Separate preregistration and execution-admission chain before any new execution
```

Do not implement new product semantics first and write architecture afterward. Do not force future realizations to reproduce the A3 transition catalogue, A6 lifecycle graph, Event/reducer/Receipt structures, exact replay, or current identity/time inventory merely because those taxonomies exist.

Python, PostgreSQL, SQLite, JSON, SHA-256, graphs, vectors, LLMs, event sourcing, exact replay, Rust and current hardware are replaceable profiles or research instruments, not permanent Canon unless a later evidence-backed operator decision establishes otherwise.

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

Do not reinterpret or rewrite published reducer-v1 histories, Event histories, Receipts, P1–C5 evidence, ZIP archives, historical checkpoint identities, fixture outputs, A1–A10 first-draft history, the integrated-review record, IAR-1 source findings, IAR-1-R1 publication-time gate language, frozen BPV1 preregistration/oracle or historical PR #114 D5 evidence.

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
falsification instrument ≠ product runtime
C2 ≠ C3 ≠ C4 ≠ C5
C5 operational rehearsal ≠ semantic assertion promotion
synthetic CI ≠ live production
logical ERASED ≠ physical deletion
physical erasure ≠ cryptographic erasure
forgetting/loss ≠ deliberate erasure
bounded accountability ≠ exact reconstruction
history visibility ≠ mandatory Event sourcing
local scoped conformance ≠ composition/federation conformance
runtime implementation ≠ evidence
evidence ≠ operator authorization
public repository ≠ open-source license
future-facing design ≠ demonstrated future substrate support
substrate-independent specification ≠ universal portability proof
SUPPORTED_FOR_SCOPE ≠ universal proof
NOT_TESTED ≠ SUPPORTED
planning ≠ execution
```

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
python -m unittest discover -s tests -p 'test_bpv1_subject.py' -v
```

A skipped test is not PASS. An unavailable environment is `NOT_EXECUTED`.

## Review discipline

Distinguish `BOT_NOTICE`, `AUTOMATED_FINDING`, `HUMAN_REVIEW`, `QUALIFYING_INDEPENDENT_ARCHITECTURE_REVIEW`, `OPERATOR_DECISION`, and `EVIDENCE`.

A Codex quota notice is not review approval. Reproduce every actionable finding, fix or reject it with rationale, add a regression test where applicable, close the thread, and record post-merge state.

## Documentation synchronization

GitHub remains technically sufficient without Notion. ADR-0027 orientation has now been synchronized across the seven existing Native Kernel Notion surfaces and read back `7/7 VERIFIED`; zero new pages were created. This documentation convergence is not architecture proof, evidence promotion, runtime thaw, production authorization, or residual experiment admission.
