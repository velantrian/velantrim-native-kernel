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
14. affected Canon, contracts, ADRs, source, tests, workflows and evidence records
15. current GitHub PRs, issues, Actions and review threads
16. corresponding Notion current-state pages

Do not begin with random repository search. Verify live state first.

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
  ACTIVE / IAR-1-RECONCILED / BPV1 D5 COMPLETE / D5-R1 QUALIFIED / D6 NEXT
```

Never collapse these tracks.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
research proposal ≠ accepted contract ≠ runtime
reference laboratory ≠ final architecture
```

## Active operator-approved priority

ADR-0025 established **Architecture Re-foundation / Blueprint-first**. A1–A10 and the integrated review remain provisional architecture work.

ADR-0026 records the operator-selected post-blueprint **Option D**:

```text
A1-A10 provisional blueprint
→ independent architecture review            COMPLETE / IAR-1 / QUALIFYING
→ review finding reconciliation              COMPLETE / IAR-1-R1
→ BPV1 plan and preregistration              COMPLETE / PR #110
→ BPV1 execution admission                   COMPLETE / PR #112 + #113
→ BPV1-001 subject implementation/execution  COMPLETE / PR #114
→ D5-R1 evidence qualification               COMPLETE / PR #115 / QUALIFIED
→ A10 hypothesis classification              NEXT / D6 / NOT STARTED
→ integrated re-review                       D7
→ consolidated authoritative sync            D8
→ separate later operator Canon/runtime decision
```

The active gate is `D6_A10_HYPOTHESIS_CLASSIFICATION`.

```text
qualifying independent review ≠ architecture proof
operator approval ≠ independent validation
SUPPORTED_FOR_SCOPE ≠ universal portability proof
D5 result ≠ D6 hypothesis classification
BPV-1 ≠ product runtime
BPV-1 outcome ≠ automatic Canon promotion
```

IAR-1 is `QUALIFYING_REVIEW_COMPLETE`. IAR-1-R1 reconciliation is `COMPLETE`. All ten review findings have explicit reconciliation records; source review evidence remains preserved.

BPV-1 plan `BPV1-001-cross-lineage-bounded-accountability-v1` remains bound to authoritative plan merge `a538d7f1e28858a88b9ee777ac7d6e05b85943db` and frozen digest `7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0`.

Execution admission remains a separate authorization lane: `ADMITTED_FOR_EXPERIMENT_ONLY`, bounded strictly to BPV1-001 subject implementation/execution. Product runtime integration is not authorized.

D5 historical execution merged via PR #114 at `a191e9c868c14af34a269dcdfae44406f1013bda`. D5-R1 qualification merged via PR #115 at `3856740570620fb2243e2f0da76359281ec4068f` and records:

```text
external qualification: QUALIFIED
frozen evaluator: SUPPORTED_FOR_SCOPE
mandatory fixtures: 12 / 12 PASS
mutations: 512
checkpoints: 128 / 256 / 512
D6: NOT_STARTED
```

### Allowed during the freeze

- D6 A10 hypothesis classification;
- D7 integrated re-review;
- D8 authoritative GitHub↔Notion synchronization;
- architecture and ontology research that does not mutate frozen experiment authority;
- integrity, security, reproducibility, provenance and truth-surface fixes;
- evidence preservation;
- historical recovery.

### Not authorized during the freeze

- product runtime integration of the BPV1-001 subject;
- changes to preregistered normative fields, fixture expected outcomes, thresholds, scenario identity or HR01-HR10 under the same experiment identity;
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

## D6 discipline

D6 must classify the preregistered target hypotheses using the frozen plan plus authoritative qualified D5 evidence. Allowed A10 outcomes are exactly:

```text
SUPPORTED_FOR_SCOPE
WEAKENED
REFUTED
INDETERMINATE
NOT_TESTED
```

Do not assign `SUPPORTED_FOR_SCOPE` mechanically to every hypothesis because the aggregate fixture run passed. Respect the preregistered target map:

- primary: `A10-H02`, `A10-H05`;
- secondary: `A10-H01`, `A10-H04`, `A10-H07`, `A10-H12`;
- informative, not adjudicated: `A10-H03`, `A10-H10`;
- not tested: `A10-H06`, `A10-H08`, `A10-H09`, `A10-H11`.

D6 is classification/evidence work only; it does not change the experiment or authorize runtime expansion.

## Required architecture discipline

```text
Problem-level purpose and candidate semantic obligations
→ Preregistered scope / observables / applicability / failure thresholds
→ Explicit grounding and threat model
→ Frozen external fixture/oracle package
→ Independently derived bounded state/change/history realization
→ External evidence qualification
→ Frozen oracle evaluation
→ Explicit A10 outcome classification
→ Integrated re-review
→ Authoritative synchronization
→ Separate operator decision
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
D5 evidence ≠ D6 classification
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

GitHub must remain technically sufficient without Notion. The current Option D plan deliberately defers D5/D5-R1/D6 Notion synchronization to consolidated D8; until then live Notion may lag at D4.5 without overriding GitHub technical authority. Do not create new Notion pages without operator permission.
