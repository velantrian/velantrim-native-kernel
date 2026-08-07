# GitHub Copilot instructions for Velantrim Native Kernel

## Mandatory orientation

Read in order:

1. `../README.md`
2. `../STATUS.md`
3. `../project-state.json`
4. `../AGENTS.md`
5. `../docs/ai/README.md`
6. `../docs/ai/CURRENT_STATE.md`
7. `../docs/ai/C5_IMPLEMENTATION_RECORD.md`
8. `../evidence/c5/README.md`
9. relevant source/contracts/tests/workflows/risks

Verify the actual branch/PR SHA, live issue state, plan digest, workflow and artifact bytes before carrying a claim forward.

## Current status

```text
RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
kernel_runtime_conformance: C4
operational_validation: C5_BOUNDED_REHEARSAL
support_state: PARTIAL
assertions: 45 / 10 / 17 / 0
NK-EPI: 0 / 8 SUPPORTED
```

## Three tracks

```text
H historical recovery: BLOCKED / independent
C clean implementation: ACTIVE / PARTIAL
R long-horizon research: PROPOSED / bounded
```

Do not collapse them.

## Architecture discipline

- Preserve `Architecture Canon → Abstract Contracts → Replaceable Profiles → Bounded Evidence`.
- Python, PostgreSQL, SQLite, JSON, graphs, vectors, LLMs and hardware are replaceable.
- Event history is authoritative about recorded history, not automatically truth.
- Storage presence, relevance, repetition, confidence, utility and model output do not imply admission.
- Receipts, reports, hashes and retained archives are bounded evidence, not certification.
- Operator approval is authority, not empirical evidence.
- Research notes are not runtime or Canon.

## C5 discipline

```text
plan: native-kernel/c5-bounded-rehearsal-v1
sha256: 4ed680ff4e83ac9d1aca6c1ab8a435ecb19af4a5badf1be8202bc842f964b098
scenarios: 18
durable archive: evidence/c5/2026-08-07/manifest.json
```

Do not rewrite archived ZIPs or expand their proof boundary.

## Verification

```bash
python tools/evidence/verify_bundle.py evidence/c5/2026-08-07/manifest.json
python tools/ai_context/validate_project_state.py --repo .
python -m unittest discover -s tests -p 'test_evidence_bundle.py' -v
python -m unittest discover -s tests -p 'test_project_state.py' -v
python tools/profiles/validate_c5_manifest.py
python tools/ai_context/validate_context.py --repo .
```

## Source recovery and research

- Clean work is not recovered `v0.1.2.1`.
- `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.
- `NK-EPI-001…008` remain proposed/unsupported.
- Keep future ideas in `docs/research/` until separately accepted and evidenced.
- Do not begin production, live traffic, physical deletion, NK-EPI promotion or ecosystem wiring without separate authorization.

## Documentation synchronization

Material changes update current-state documents, project state, risks, component map, work log, ADRs, public READMEs and Notion. GitHub must remain sufficient without Notion.
