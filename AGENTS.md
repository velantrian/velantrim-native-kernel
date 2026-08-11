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
10. affected Canon, contracts, and ADRs
11. affected source, tests, workflows, and evidence records
12. current GitHub PRs, issues, Actions, and review threads
13. corresponding Notion current-state pages

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
  ACTIVE / INDEPENDENT-REVIEW-FIRST / no automatic promotion
```

Never collapse these tracks.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
research proposal ≠ accepted contract ≠ runtime
reference laboratory ≠ final architecture
```

## Active operator-approved priority

ADR-0025 established **Architecture Re-foundation / Blueprint-first**. A1–A10 and the first integrated review are complete only as provisional architecture work.

ADR-0026 records the operator-selected post-blueprint **Option D**:

```text
A1-A10 provisional blueprint
→ independent architecture review
→ review finding reconciliation
→ one bounded cross-lineage falsification instrument (BPV-1)
→ A10 outcome classification
→ integrated re-review
→ separate later operator Canon/runtime decision
```

The active gate is `INDEPENDENT_ARCHITECTURE_REVIEW`.

```text
independent review protocol ≠ completed independent review
operator approval ≠ independent validation
BPV-1 ≠ product runtime
BPV-1 outcome ≠ automatic Canon promotion
```

Independent validation is currently `NOT ESTABLISHED`. BPV-1 is `BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION`.

### Allowed during the freeze

- architecture and ontology research;
- independent architectural review and review reconciliation;
- integrity, security, reproducibility, and provenance fixes;
- evidence preservation;
- validator and truth-surface repairs;
- historical recovery;
- later isolated experiments explicitly admitted under ADR-0026 to test or falsify a blueprint assumption without runtime promotion.

### Not authorized during the freeze

- product runtime thaw;
- reducer v2 or new Event semantics;
- new product databases, language/runtime profiles, LLM/vector adapters, or ecosystem integrations;
- executable NK-EPI, Temporal, full Admission, or operational deletion;
- performance-driven semantic changes;
- Final Canon promotion;
- maturity or production promotion.

A different language or non-event-sourced realization may later be used as a falsification instrument, but neither becomes a product profile or Canon requirement merely because BPV-1 uses it.

## Independent-review discipline

A qualifying independent review must follow `nk-independent-architecture-review/1` and record an actual independence basis.

Do not self-certify independence. The current assistant lineage, the integrated review, CI, tests, Notion read-back, operator approval, or a Codex quota notice do not by themselves satisfy the gate.

The reviewer must be instructed to search for counterexamples, hidden implementation assumptions, unnecessary obligations, circular definitions, non-falsifiable claims, and architecture capture rather than to confirm the current design.

If a qualifying reviewer cannot be established, record `BLOCKED_NO_QUALIFYING_REVIEWER` rather than silently proceeding to BPV-1.

## Required architecture discipline

```text
Architecture purpose and ontology
→ Abstract Kernel Machine
→ Semantic Laws
→ Versioned Abstract Contract
→ Failure and Threat Model
→ Explicit Decision
→ Replaceable Runtime Profile or bounded falsification instrument
→ Positive and Negative Fixtures
→ Cross-profile / cross-lineage Comparison
→ Exact Evidence
→ Status Update
→ Notion Synchronization
```

Do not implement new semantics first and write the architecture afterward.

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
- A1–A10 first-draft history or the first integrated-review record.

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
independent review protocol ≠ completed review
falsification instrument ≠ product runtime
C2 ≠ C3 ≠ C4 ≠ C5
C5 operational rehearsal ≠ semantic assertion promotion
synthetic CI ≠ live production
logical Event export ≠ physical backup or disaster recovery
logical ERASED ≠ physical deletion
physical erasure ≠ cryptographic erasure
forgetting/loss ≠ deliberate erasure
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