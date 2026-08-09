# 🤖 Velantrim Native Kernel repository guidance

## Required reading order

Before searching code, creating a branch or proposing architecture changes, read:

1. `README.md`
2. `STATUS.md`
3. `project-state.json`
4. `docs/ai/README.md`
5. `docs/ai/CURRENT_STATE.md`
6. `docs/ai/KNOWN_RISKS.md`
7. `ROADMAP.md`
8. affected Canon, contracts and ADRs
9. affected source, tests, workflows and evidence records
10. current GitHub PRs, issues, Actions and review threads
11. corresponding Notion current-state pages

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

Machine-readable truth uses `project-state.json` protocol `nk-project-state/2`. Live HEAD must be resolved through Git or GitHub; committed checkpoint metadata does not attempt to contain its own commit SHA.

## Three independent tracks

```text
H — historical recovery
  authentic v0.1.2.1 + original 44-test suite
  OPEN / BLOCKED / independent

C — clean implementation
  P1–P5 + C4 + C5
  ACTIVE / PARTIAL

R — long-horizon research
  PROPOSED / BOUNDED / no automatic promotion
```

Never collapse these tracks.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
research proposal ≠ accepted contract ≠ runtime
```

## Required architecture discipline

```text
Architecture Canon
→ Versioned Abstract Contract
→ Failure and Threat Model
→ Explicit Decision
→ Runtime Implementation
→ Positive and Negative Fixtures
→ Cross-profile Comparison
→ Exact Evidence
→ Status Update
→ Notion Synchronization
```

Do not implement new semantics first and write the contract afterward.

Python, PostgreSQL, SQLite, JSON, SHA-256, graphs, vectors, LLMs and hardware are replaceable profiles or instruments, not permanent Canon.

## Historical immutability

Do not reinterpret or rewrite published:

- reducer-v1 histories;
- Event histories;
- Receipts;
- P1–C5 evidence;
- ZIP archives;
- historical checkpoint identities;
- fixture outputs.

New semantics require a new contract/reducer/Event version where applicable, a migration boundary and a new evidence identity.

## Current authorized sequence

```text
human-readable truth reconciliation
→ Issues #14–#17 and Notion reconciliation
→ license/publication operator decision — Issue #18
→ ADR-0024 operator decision — Issue #74
→ NK-SAM and named equivalence profiles
→ Event/history commitment contract
→ only then reducer-v2 runtime
```

No AI agent may choose a license or accept ADR-0024 for the operator.

Do not begin inside the current slice:

- reducer-v2 runtime;
- executable NK-EPI;
- Temporal runtime;
- full Admission lifecycle;
- operational deletion;
- full independent Rust/Go implementation;
- Titan, Crystal or Mentaury integration;
- distributed multi-writer work;
- production promotion.

## Required distinctions

```text
Claim ≠ truth
admission ≠ objective truth
Unknown ≠ False
Architecture Canon ≠ implementation profile
C2 ≠ C3 ≠ C4 ≠ C5
C5 operational rehearsal ≠ semantic assertion promotion
synthetic CI ≠ live production
logical Event export ≠ physical backup or disaster recovery
logical ERASED ≠ physical deletion
hash chain ≠ complete authenticity
Receipt/report/archive ≠ truth, compliance or deletion proof
runtime implementation ≠ evidence
evidence ≠ operator authorization
public repository ≠ open-source license
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

Runtime PRs require their targeted unit/integration matrices and exact-head CI. A skipped test is not PASS. An unavailable environment is `NOT_EXECUTED`.

## Review discipline

Distinguish:

```text
BOT_NOTICE
AUTOMATED_FINDING
HUMAN_REVIEW
OPERATOR_DECISION
EVIDENCE
```

A Codex quota notice is not review approval. Reproduce every actionable finding, fix or reject it with rationale, add a regression test where applicable, close the thread and record post-merge state.

## Documentation synchronization

Material work must update the relevant current-state, status, roadmap, risks, implementation/evidence records, public English/Russian documentation and Notion.

GitHub must remain technically sufficient without Notion. Notion may preserve strategy, decisions and history but must not silently contradict GitHub code, contracts, evidence or live issue state.