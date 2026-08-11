# GitHub Copilot instructions for Velantrim Native Kernel

## Mandatory orientation

Read in order before suggesting or editing code:

1. `../README.md`
2. `../STATUS.md`
3. `../project-state.json`
4. `../AGENTS.md`
5. `../docs/ai/README.md`
6. `../docs/ai/CURRENT_STATE.md`
7. `../docs/ai/KNOWN_RISKS.md`
8. `../ROADMAP.md`
9. `../docs/ARCHITECTURE_REFOUNDATION.md`
10. `../docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md`
11. `../docs/reviews/IAR-1_RESULT.json`
12. `../docs/reviews/IAR-1_RECONCILIATION.json`
13. `../docs/research/BPV1_PREREGISTRATION.json`
14. relevant Canon, contracts, ADRs, source, tests, workflows, evidence and live GitHub/Notion state

Verify live branch/PR SHA, issue state, workflow runs, review threads, and artifact identities before carrying a claim forward.

## Current status

```text
RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
clean_runtime_support:       PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false
assertions:                 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:                    0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
runtime expansion:          FROZEN
```

`project-state.json` uses `nk-project-state/2`. Resolve live HEAD through Git/GitHub; do not expect a committed manifest to contain the SHA of its own future merge.

## Track boundary

```text
H historical recovery: BLOCKED / independent
C clean implementation: PRESERVED / PARTIAL / BOUNDED REFERENCE LABORATORY
R post-blueprint validation: ACTIVE / BPV1-PREREGISTERED / EXECUTION-ADMISSION-NEXT
```

Do not collapse them.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
reference laboratory ≠ final architecture
blueprint documentation ≠ runtime evidence
operator approval ≠ independent validation
qualifying review ≠ architecture proof
preregistered plan ≠ execution authorization
falsification instrument ≠ product runtime
```

## Active gate — ADR-0026 / BPV1_EXECUTION_ADMISSION

ADR-0025 established blueprint-before-runtime. ADR-0026 records Option D. IAR-1 completed the qualifying independent review, IAR-1-R1 completed reconciliation, and PR #110 made `BPV1-001-cross-lineage-bounded-accountability-v1` authoritative as a preregistered plan.

```text
A1–A10 provisional blueprint
→ integrated review                         COMPLETE / PROVISIONAL
→ operator post-blueprint decision          COMPLETE / ADR-0026
→ INDEPENDENT_ARCHITECTURE_REVIEW           COMPLETE / IAR-1 / QUALIFYING
→ REVIEW_FINDING_RECONCILIATION             COMPLETE / IAR-1-R1
→ BPV1_PLAN_AND_PREREGISTRATION             COMPLETE / PR #110
→ BPV1_EXECUTION_ADMISSION                  NEXT GATE
→ BPV-1 bounded cross-lineage falsification BLOCKED_PENDING_EXECUTION_ADMISSION
→ A10 outcome classification
→ integrated re-review
→ separate later operator Canon/runtime decision
```

Current exact boundary:

```text
BPV-1 plan: BPV1-001-cross-lineage-bounded-accountability-v1 / PREREGISTERED / EXECUTION_NOT_AUTHORIZED
plan merge: a538d7f1e28858a88b9ee777ac7d6e05b85943db
BPV-1 execution: BLOCKED_PENDING_EXECUTION_ADMISSION
product runtime thaw: NO
reducer v2: NOT AUTHORIZED
new semantic Event verbs: NOT AUTHORIZED
new product DB/language/runtime profiles: NOT AUTHORIZED
NK-EPI runtime: NOT AUTHORIZED
Final Canon: NOT AUTHORIZED
production: false
```

### Execution-admission rule

Before any BPV-1 subject implementation/execution, admission must bind:

- the frozen preregistration and digest;
- machine-readable fixtures derived only from it;
- a standalone evaluator whose tests pass before subject execution;
- pinned Rust toolchain and experimental source boundary;
- static no-product-integration scope audit.

The subject implementation cannot define its own expected outcomes. Post-execution normative rescoping requires a new scenario identity.

Rust is `EXPERIMENTAL_INSTRUMENT_NOT_CANON`; different language does not establish independent team/custody or independent computation model.

### Allowed

- architecture research;
- BPV-1 execution-admission packaging derived from the frozen plan;
- integrity/security/reproducibility/provenance/validator/evidence fixes;
- historical recovery;
- later isolated BPV-1 execution only after separate authoritative admission.

### Not authorized

- BPV-1 subject implementation/execution before admission;
- product runtime thaw;
- reducer v2 or new semantic Event verbs;
- new product databases, language/runtime profiles, LLM/vector adapters, or integrations;
- executable NK-EPI, Temporal, full Admission, operational deletion;
- Final Canon, maturity, or production promotion.

## Architecture discipline

- Preserve `purpose/ontology → semantic obligations → preregistered oracle → admission → bounded falsification instrument → fixtures → evidence → A10 outcome → review`.
- Do not force BPV-1 to reproduce A3/A6/Event/reducer/Receipt shape merely because current laboratory does.
- Python, Rust, PostgreSQL, SQLite, JSON, SHA-256, graphs, vectors, LLMs, and hardware remain replaceable instruments.
- Event history is authoritative about recorded history, not automatically truth or universal architecture.
- Receipts, reports, hashes, and retained archives are bounded evidence, not certification.

## Pending decisions remain pending

```text
Issue #18 — license/publication
  PENDING_OPERATOR

Issue #74 / ADR-0024
  PROPOSED / PENDING_OPERATOR
  reducer-v2 NOT AUTHORIZED

Track H source admission
  operator-controlled
```

Do not choose a license, accept ADR-0024, or admit Track H sources for the operator.

## Historical immutability

Do not rewrite reducer-v1 history, Events, Receipts, fixtures, evidence ZIPs, historical checkpoint identities, A1–A10 first drafts, integrated review, IAR-1 findings, or IAR-1-R1 publication-time gate language.

## Verification

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

The SQLite profile fails closed below linked SQLite `3.51.3`.

## Review discipline

Distinguish bot notices, automated findings, human reviews, qualifying independent architecture reviews, operator decisions, and evidence. A Codex quota notice is not review approval.

## Required non-equivalences

```text
Claim ≠ truth
Unknown ≠ False
C5 PASS ≠ production readiness
PostgreSQL + SQLite ≠ full substrate neutrality
hash chain ≠ complete authenticity
logical ERASED ≠ physical deletion
runtime implementation ≠ evidence
evidence ≠ operator authorization
public repository ≠ open-source license
future-facing design ≠ demonstrated future substrate support
```

## Documentation synchronization

Material changes update relevant current-state documents, machine state, risks, roadmap, public English/Russian docs, and Notion. GitHub must remain technically sufficient without Notion.
