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
9. `docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md` when working in the post-blueprint validation phase
10. `docs/reviews/IAR-1_RESULT.md` and `docs/reviews/IAR-1_RESULT.json`
11. `docs/reviews/IAR-1_RECONCILIATION.md` and `docs/reviews/IAR-1_RECONCILIATION.json`
12. affected Canon, contracts, and ADRs
13. affected source, tests, workflows, and evidence records
14. current GitHub PRs, issues, Actions, and review threads
15. corresponding Notion current-state pages

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
  ACTIVE / IAR-1-RECONCILED / BPV1-PLAN-NEXT / no automatic promotion
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
→ BPV1 plan and preregistration              NEXT
→ one bounded cross-lineage falsification instrument (BPV-1)
→ A10 outcome classification
→ integrated re-review
→ separate later operator Canon/runtime decision
```

The active gate is `BPV1_PLAN_AND_PREREGISTRATION`.

```text
qualifying independent review ≠ architecture proof
review reconciliation ≠ BPV-1 execution authorization
operator approval ≠ independent validation
BPV-1 ≠ product runtime
BPV-1 outcome ≠ automatic Canon promotion
```

IAR-1 is `QUALIFYING_REVIEW_COMPLETE`. IAR-1-R1 reconciliation is `COMPLETE`. All ten review findings have explicit reconciliation records; source review evidence remains preserved. BPV-1 execution is `BLOCKED_PENDING_PREREGISTERED_PLAN`.

### Allowed during the freeze

- architecture and ontology research;
- BPV-1 plan and preregistration work;
- integrity, security, reproducibility, and provenance fixes;
- evidence preservation;
- validator and truth-surface repairs;
- historical recovery;
- later isolated experiments explicitly admitted under ADR-0026 after their preregistered plan is authoritative, solely to test or falsify blueprint assumptions without runtime promotion.

### Not authorized during the freeze

- BPV-1 execution before an authoritative preregistered plan;
- product runtime thaw;
- reducer v2 or new Event semantics;
- new product databases, language/runtime profiles, LLM/vector adapters, or ecosystem integrations;
- executable NK-EPI, Temporal, full Admission, or operational deletion;
- performance-driven semantic changes;
- Final Canon promotion;
- maturity or production promotion.

A different language or non-event-sourced realization may later be used as a falsification instrument, but neither becomes a product profile or Canon requirement merely because BPV-1 uses it.

## Independent-review and reconciliation discipline

IAR-1 followed `nk-independent-architecture-review/1` and recorded a concrete independence basis. The qualifying review produced 10 findings: 7 `BLOCKING` and 3 `MATERIAL`. `IAR-1-R1` reconciles all ten through separate records without rewriting the original review evidence.

Do not reinterpret a resolved GitHub thread as deletion of the source finding. `docs/reviews/IAR-1_RESULT.json` preserves the review-local source status; `docs/reviews/IAR-1_RECONCILIATION.json` records the later disposition.

Do not self-certify future independent gates. The current assistant lineage, integrated review, CI, tests, Notion read-back, operator approval, or automated review alone do not prove the architecture correct.

The central IAR-1 result is that changing implementation language is insufficient if the experiment merely ports the existing conceptual structure. A later BPV-1 must independently derive its state/change/history model from the preregistered problem-level obligations.

## Required architecture discipline

```text
Problem-level purpose and candidate semantic obligations
→ Preregistered scope / observables / applicability / failure thresholds
→ Explicit grounding and threat model
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

Python, PostgreSQL, SQLite, JSON, SHA-256, graphs, vectors, LLMs, event sourcing, exact replay, and hardware are replaceable profiles or research instruments, not permanent Canon unless a later evidence-backed decision establishes otherwise.

## Pending decisions remain separate

```text
Issue #18 — license/publication
  PENDING_OPERATOR
  blocks open contribution and package publication

Issue #74 / ADR-0024 — reducer referential semantics
  PROPOSED / PENDING_OPERATOR
  blocks reducer-v2 work

Track H source admission
  operator-controlled
```

Post-blueprint validation may proceed without silently deciding any of these. No AI agent may choose a license, accept ADR-0024, or admit Track H sources for the operator.

## Historical immutability

Do not reinterpret or rewrite published:

- reducer-v1 histories;
- Event histories;
- Receipts;
- P1–C5 evidence;
- ZIP archives;
- historical checkpoint identities;
- fixture outputs;
- A1–A10 first-draft history or the first integrated-review record;
- IAR-1 source findings.

New semantics require a new contract/reducer/Event version where applicable, a migration boundary, a new evidence identity, and separate authorization.

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
falsification instrument ≠ product runtime
C2 ≠ C3 ≠ C4 ≠ C5
C5 operational rehearsal ≠ semantic assertion promotion
synthetic CI ≠ live production
logical Event export ≠ physical backup or disaster recovery
logical ERASED ≠ physical deletion
physical erasure ≠ cryptographic erasure
physical/cryptographic erasure assertion ≠ independently verified substrate condition
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

```text
plan: native-kernel/c5-bounded-rehearsal-v1
sha256: 4ed680ff4e83ac9d1aca6c1ab8a435ecb19af4a5badf1be8202bc842f964b098
scenarios: 18
deployment: CI_EPHEMERAL_SYNTHETIC
historical bundle: evidence/c5/2026-08-07/manifest.json
ADR-0023 bundle: evidence/c5/2026-08-08-adr0023/manifest.json
```

Never alter plan scenarios or thresholds under the same identity/digest. Never rewrite archived ZIPs or expand their proof boundary.

Future BPV-1 evidence must receive its own identity and use A10 outcomes exactly:

```text
SUPPORTED_FOR_SCOPE
WEAKENED
REFUTED
INDETERMINATE
NOT_TESTED
```

`NOT_TESTED ≠ SUPPORTED`.

The BPV-1 plan must freeze, before execution, its `scenario_id`, purpose scope, mandatory obligations, applicability rules, observables, equivalence predicates, allowed losses, failure thresholds, hard refutation observations, grounding mode, threat model, and oracle Authority. Post-execution changes to these fields cannot rescue an old run; they require a new experiment identity.

## Verification

The SQLite WAL profile fails closed below linked SQLite `3.51.3`. On Linux, build the pinned library before SQLite/P5/C3/C4/C5 checks:

```bash
tools/sqlite/build_safe_sqlite.sh /tmp/native-kernel-sqlite-3.51.3 /usr/bin/python3
export LD_LIBRARY_PATH=/tmp/native-kernel-sqlite-3.51.3/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
python -c 'from native_kernel.sqlite_profile import linked_sqlite_version; print(linked_sqlite_version())'
```

Minimum integrity commands:

```bash
python tools/evidence/verify_bundle.py evidence/c5/2026-08-07/manifest.json
python tools/evidence/verify_bundle.py evidence/c5/2026-08-08-adr0023/manifest.json
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_architecture_freeze.py --repo .
python tools/ai_context/validate_context.py --repo .
python tools/docs/validate_bilingual_parity.py --repo .
python -m unittest discover -s tests -p 'test_project_state.py' -v
python -m unittest discover -s tests -p 'test_architecture_freeze.py' -v
python -m unittest discover -s tests -p 'test_independent_architecture_review_protocol.py' -v
python -m unittest discover -s tests -p 'test_ai_context_validator.py' -v
python -m unittest discover -s tests -p 'test_bilingual_parity_validator.py' -v
```

A skipped test is not PASS. An unavailable environment is `NOT_EXECUTED`.

## Review discipline

Distinguish:

```text
BOT_NOTICE
AUTOMATED_FINDING
HUMAN_REVIEW
QUALIFYING_INDEPENDENT_ARCHITECTURE_REVIEW
OPERATOR_DECISION
EVIDENCE
```

A Codex quota notice is not review approval. Reproduce every actionable finding, fix or reject it with rationale, add a regression test where applicable, close the thread, and record post-merge state.

## Documentation synchronization

Material work must update the relevant current-state, roadmap, risks, architecture, public English/Russian documentation, and Notion pages.

GitHub must remain technically sufficient without Notion. Notion may preserve strategy, decisions, and history but must not silently contradict GitHub code, contracts, evidence, or live issue state.