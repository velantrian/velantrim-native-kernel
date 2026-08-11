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
10. `../docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md` during post-blueprint validation
11. relevant Canon, contracts, ADRs, source, tests, workflows, and evidence

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
R post-blueprint validation: ACTIVE / OPTION D / INDEPENDENT-REVIEW-FIRST
```

Do not collapse them.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
reference laboratory ≠ final architecture
blueprint documentation ≠ runtime evidence
operator approval ≠ independent validation
independent review protocol ≠ completed independent review
falsification instrument ≠ product runtime
```

## Active gate — ADR-0026

ADR-0025 established blueprint-before-runtime. A1–A10 and the first integrated review are complete only as provisional architecture work.

ADR-0026 records the operator-approved Option D sequence:

```text
A1–A10 provisional blueprint
→ integrated review                         COMPLETE / PROVISIONAL
→ operator post-blueprint decision          OPTION D / ADR-0026 / APPROVED
→ INDEPENDENT_ARCHITECTURE_REVIEW           NEXT GATE
→ REVIEW_FINDING_RECONCILIATION
→ BPV-1 bounded cross-lineage falsification
→ A10 outcome classification
→ integrated re-review
→ separate later operator Canon/runtime decision
```

Current exact boundary:

```text
independent architectural validation: NOT ESTABLISHED
BPV-1: BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION
product runtime thaw: NO
reducer v2: NOT AUTHORIZED
new semantic Event verbs: NOT AUTHORIZED
new product DB/language/runtime profiles: NOT AUTHORIZED
NK-EPI runtime: NOT AUTHORIZED
Final Canon: NOT AUTHORIZED
production: false
```

A qualifying independent review must follow `nk-independent-architecture-review/1` and state a concrete independence basis. Do not self-certify. If no qualifying reviewer exists, record `BLOCKED_NO_QUALIFYING_REVIEWER` and stop before BPV-1.

An unresolved `BLOCKING` review finding always blocks BPV-1. Assigning `TEST`, `RETAIN`, or another recommended disposition is not resolution.

### Allowed

- architecture and ontology research;
- qualifying independent architecture review and review reconciliation;
- integrity, security, reproducibility, provenance, validator, and evidence-preservation fixes;
- historical recovery;
- a later isolated BPV-1 experiment only after the ADR-0026 review/reconciliation gate and without runtime promotion.

### Not authorized

- product runtime thaw;
- reducer v2 or new semantic Event verbs;
- new product databases, language/runtime profiles, LLM/vector adapters, or ecosystem integrations;
- executable NK-EPI, Temporal, full Admission, or operational deletion;
- performance-driven semantic changes;
- Final Canon, maturity, or production promotion.

## Architecture discipline

- Preserve `purpose/ontology → abstract machine → semantic laws → versioned contract → failure/threat model → decision → bounded implementation/falsification instrument → fixtures → evidence → status`.
- Do not implement new product semantics before an accepted architecture/contract boundary and explicit authorization.
- Python, PostgreSQL, SQLite, JSON, SHA-256, graphs, vectors, LLMs, and hardware are replaceable instruments.
- Event history is authoritative about recorded history, not automatically truth.
- Storage presence, relevance, repetition, confidence, utility, and model output do not imply admission.
- Receipts, reports, hashes, and retained archives are bounded evidence, not certification.
- Operator approval is authority, not empirical evidence or independent validation.
- Research notes and BPV-1 results are not runtime or Final Canon.

## Pending decisions remain pending

```text
Issue #18 — license/publication
  PENDING_OPERATOR
  blocks open contribution/package publication

Issue #74 / ADR-0024
  PROPOSED / PENDING_OPERATOR
  blocks reducer-v2 work

Track H source admission
  operator-controlled
```

Architecture validation may proceed without deciding any of these. Do not choose a license, accept ADR-0024, or admit Track H sources for the operator.

## Historical immutability

Do not rewrite reducer-v1 history, Events, Receipts, fixtures, evidence ZIPs, historical checkpoint identities, or A1–A10 first-draft/integrated-review history. New semantics require new versions, migration boundaries, evidence identities, and explicit authorization.

## Verification

```bash
python tools/evidence/verify_bundle.py evidence/c5/2026-08-07/manifest.json
python tools/evidence/verify_bundle.py evidence/c5/2026-08-08-adr0023/manifest.json
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_architecture_freeze.py --repo .
python tools/ai_context/validate_context.py --repo .
python tools/docs/validate_bilingual_parity.py --repo .
python -m unittest discover -s tests -p 'test_project_state.py' -v
python -m unittest discover -s tests -p 'test_independent_architecture_review_protocol.py' -v
python -m unittest discover -s tests -p 'test_ai_context_validator.py' -v
python -m unittest discover -s tests -p 'test_bilingual_parity_validator.py' -v
```

The SQLite profile fails closed below linked SQLite `3.51.3`.

## Review discipline

Distinguish bot notices, automated findings, human reviews, qualifying independent architecture reviews, operator decisions, and evidence. Codex code-review feedback is actionable review input when specific, but it is not automatically the qualifying independent architectural review required by ADR-0026.

Every actionable finding must be reproduced, classified, fixed or rejected with rationale, covered by a regression test where applicable, and closed in the review thread.

## Required non-equivalences

```text
Claim ≠ truth
Unknown ≠ False
admission ≠ objective truth
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

Material changes update relevant current-state documents, machine state, risks, roadmap, public English/Russian docs, and Notion.

GitHub must remain technically sufficient without Notion.