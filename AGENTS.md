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
9. affected Canon, contracts, and ADRs
10. affected source, tests, workflows, and evidence records
11. current GitHub PRs, issues, Actions, and review threads
12. corresponding Notion current-state pages

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

R — Architecture Re-foundation and Long-Horizon Research
  ACTIVE / BLUEPRINT-FIRST / no automatic runtime promotion
```

Never collapse these tracks.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
research proposal ≠ accepted contract ≠ runtime
reference laboratory ≠ final architecture
```

## Active operator-approved priority

ADR-0025 places Native Kernel in an **Architecture Re-foundation / Blueprint-first** phase.

```text
Purpose and Non-goals
→ Knowledge and Memory Ontology
→ Abstract Native Kernel Machine
→ Semantic Laws and Invariants
→ Identity / Time / Change
→ Knowledge Lifecycle
→ Conflict / Uncertainty / Revision
→ Substrate-independence Contract
→ Reference Laboratory Boundary
→ Open Questions / Falsification
→ integrated blueprint review
→ separate operator decision before runtime expansion
```

No new semantic/runtime expansion is authorized before the blueprint completion gate.

### Allowed during the freeze

- architecture and ontology research;
- integrity, security, reproducibility, and provenance fixes;
- evidence preservation;
- validator and truth-surface repairs;
- historical recovery;
- isolated experiments explicitly designed to test or falsify a blueprint assumption without runtime promotion.

### Not authorized during the freeze

- reducer v2 or new Event semantics;
- new databases, language ports, LLM/vector adapters, or ecosystem integrations;
- executable NK-EPI, Temporal, full Admission, or operational deletion;
- performance-driven semantic changes;
- maturity or production promotion.

## Required architecture discipline

```text
Architecture purpose and ontology
→ Abstract Kernel Machine
→ Semantic Laws
→ Versioned Abstract Contract
→ Failure and Threat Model
→ Explicit Decision
→ Replaceable Runtime Profile
→ Positive and Negative Fixtures
→ Cross-profile Comparison
→ Exact Evidence
→ Status Update
→ Notion Synchronization
```

Do not implement new semantics first and write the architecture afterward.

Python, PostgreSQL, SQLite, JSON, SHA-256, graphs, vectors, LLMs, and hardware are replaceable profiles or instruments, not permanent Canon.

## Pending decisions remain separate

```text
Issue #18 — license/publication
  PENDING_OPERATOR
  blocks open contribution and package publication

Issue #74 / ADR-0024 — reducer referential semantics
  PROPOSED / PENDING_OPERATOR
  blocks reducer-v2 work
```

Architecture Re-foundation may proceed without silently deciding either one. No AI agent may choose a license or accept ADR-0024 for the operator.

## Historical immutability

Do not reinterpret or rewrite published:

- reducer-v1 histories;
- Event histories;
- Receipts;
- P1–C5 evidence;
- ZIP archives;
- historical checkpoint identities;
- fixture outputs.

New semantics require a new contract/reducer/Event version where applicable, a migration boundary, a new evidence identity, and a post-blueprint authorization.

## Required distinctions

```text
Claim ≠ truth
admission ≠ objective truth
Unknown ≠ False
Architecture Canon ≠ implementation profile
reference implementation ≠ architectural authority
blueprint documentation ≠ implementation evidence
C2 ≠ C3 ≠ C4 ≠ C5
C5 operational rehearsal ≠ semantic assertion promotion
synthetic CI ≠ live production
logical Event export ≠ physical backup or disaster recovery
logical ERASED ≠ physical deletion
hash chain ≠ complete authenticity
Receipt/report/archive ≠ truth, compliance, or deletion proof
runtime implementation ≠ evidence
evidence ≠ operator authorization
public repository ≠ open-source license
future-facing design ≠ demonstrated future substrate support
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
python tools/ai_context/validate_context.py --repo .
python tools/docs/validate_bilingual_parity.py --repo .
python -m unittest discover -s tests -p 'test_project_state.py' -v
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
OPERATOR_DECISION
EVIDENCE
```

A Codex quota notice is not review approval. Reproduce every actionable finding, fix or reject it with rationale, add a regression test where applicable, close the thread, and record post-merge state.

## Documentation synchronization

Material work must update the relevant current-state, roadmap, risks, architecture, public English/Russian documentation, and Notion pages.

GitHub must remain technically sufficient without Notion. Notion may preserve strategy, decisions, and history but must not silently contradict GitHub code, contracts, evidence, or live issue state.
