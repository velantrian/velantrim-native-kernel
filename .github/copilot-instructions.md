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
9. relevant Canon, contracts, ADRs, source, tests, workflows and evidence

Verify live branch/PR SHA, issue state, workflow runs, review threads and artifact identities before carrying a claim forward.

## Current status

```text
RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
clean_runtime_support:       PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false
assertions:                 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:                    0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
```

`project-state.json` uses `nk-project-state/2`. Resolve live HEAD through Git/GitHub; do not expect a committed manifest to contain the SHA of its own commit.

## Three tracks

```text
H historical recovery: BLOCKED / independent
C clean implementation: ACTIVE / PARTIAL
R long-horizon research: PROPOSED / bounded / no automatic promotion
```

Do not collapse them.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
research proposal ≠ accepted contract ≠ runtime
```

## Architecture discipline

- Preserve `Canon → versioned contract → failure/threat model → decision → runtime → fixtures → evidence → status`.
- Do not implement new semantics before an accepted contract.
- Python, PostgreSQL, SQLite, JSON, SHA-256, graphs, vectors, LLMs and hardware are replaceable.
- Event history is authoritative about recorded history, not automatically truth.
- Storage presence, relevance, repetition, confidence, utility and model output do not imply admission.
- Receipts, reports, hashes and retained archives are bounded evidence, not certification.
- Operator approval is authority, not empirical evidence.
- Research notes are not runtime or Canon.

## Current gate

```text
human-readable truth reconciliation
→ Issues #14–#17 and Notion reconciliation
→ license/publication operator decision
→ ADR-0024 operator decision
→ NK-SAM and named equivalence profiles
→ Event/history commitment
→ only then reducer-v2 runtime
```

Do not start executable NK-EPI, Temporal, full Admission, operational deletion, full independent Rust/Go implementation, ecosystem integration or production promotion inside this slice.

Do not choose a license or accept ADR-0024 for the operator.

## Historical immutability

Do not rewrite reducer-v1 history, Events, Receipts, fixtures, evidence ZIPs or historical checkpoint identities. New semantics require new versions, migration boundaries and evidence identities.

## Evidence discipline

```text
plan: native-kernel/c5-bounded-rehearsal-v1
sha256: 4ed680ff4e83ac9d1aca6c1ab8a435ecb19af4a5badf1be8202bc842f964b098
scenarios: 18
historical archive: evidence/c5/2026-08-07/manifest.json
ADR-0023 archive: evidence/c5/2026-08-08-adr0023/manifest.json
```

Do not rewrite archived ZIPs or expand their proof boundary.

## Verification

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

The SQLite profile fails closed below linked SQLite `3.51.3`.

## Review discipline

Distinguish bot notices, automated findings, human reviews, operator decisions and evidence. A Codex quota notice is not independent approval.

Every actionable finding must be reproduced, classified, fixed or rejected with rationale, covered by a regression test where applicable and closed in the review thread.

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
```

## Documentation synchronization

Material changes update relevant current-state documents, machine state, risks, roadmap, implementation/evidence records, public English/Russian docs and Notion.

GitHub must remain technically sufficient without Notion.