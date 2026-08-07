# GitHub Copilot instructions for Velantrim Native Kernel

## Mandatory orientation

Before reviewing or changing the repository, read:

1. [`../AGENTS.md`](../AGENTS.md);
2. [`../STATUS.md`](../STATUS.md);
3. [`../docs/ai/README.md`](../docs/ai/README.md);
4. [`../docs/ai/CURRENT_STATE.md`](../docs/ai/CURRENT_STATE.md);
5. [`../docs/ai/P4_IMPLEMENTATION_RECORD.md`](../docs/ai/P4_IMPLEMENTATION_RECORD.md);
6. relevant component/risk/work-log entries.

Verify the actual branch/PR SHA, workflows and artifacts before carrying forward any claim.

## Current status

```text
RESEARCH / P4 PARTIAL ASSERTION CONFORMANCE / NOT PRODUCTION-READY
```

Current guarded P4 map:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
support_state: PARTIAL
```

Repository C2 applies only to `SUPPORTED` results.

```text
P4 C2 ≠ all 72 supported
P4 C2 ≠ C3
P4 C2 ≠ truth/authenticity
P4 C2 ≠ physical deletion
P4 C2 ≠ production readiness
```

P5/SQLite/C3 requires a separate operator GO. All `NK-EPI-001…008` remain `UNSUPPORTED` and `PROPOSED`.

## Architecture discipline

- Preserve `Architecture Canon → Abstract Contracts → Replaceable Implementation Profiles`.
- PostgreSQL, SQLite, Python, Psycopg, SQL, graphs, vectors, LLMs and hardware are replaceable profile technologies.
- Event history is authoritative about recorded history, not automatically truth.
- Backend IDs, schemas, embeddings, graph nodes or processor assumptions must not become semantic identity by accident.
- Relevance, utility, frequency, freshness and write order do not independently establish truth.
- Receipts and evidence reports are bounded proof, not certification.
- Operator approval is authority, not empirical evidence.

## Source recovery

- Keep clean implementation separate from Issue #1 controlled import.
- Do not label reconstructed/new code `v0.1.2.1`.
- Do not call new tests the original 44-test suite.
- `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.
- Clean lineage is `clean/postgresql-reference/0.1`.

## P4 conformance discipline

For a support claim:

1. identify the assertion ID;
2. inspect the exact P4 result status;
3. inspect referenced check IDs;
4. verify those checks passed in the same report;
5. preserve stated limitations;
6. verify exact commit/run/artifact for C2.

Do not:

- omit unsupported assertions;
- promote `PARTIAL` to `SUPPORTED` through prose;
- turn a failed required check into unsupported;
- claim C2 from a locally generated JSON report alone;
- infer C3 from Python/PostgreSQL matrix diversity;
- accept `NK-EPI` through fixture execution.

## Verification

P4 local checks:

```bash
python -m unittest discover -s tests -p 'test_p4_conformance_unit.py' -v
python -m unittest discover -s tests -p 'test_p4_manifest.py' -v
python tools/profiles/validate_p4_manifest.py

NK_TEST_POSTGRES_DSN='postgresql://...' \
  python -m unittest discover -s tests -p 'test_p4_postgresql_integration.py' -v
```

C2 requires exact repository matrix jobs and retained JSON artifacts. Also inspect P1/P2/P3 regressions.

## Ecosystem boundaries

- Native Kernel owns neutral semantic memory/Event/evidence contracts and bounded profiles.
- Titan owns cognition/retrieval/tools/orchestration.
- Mentaury Soul owns digital individuality and continuity.
- Crystal owns verifiable-memory/evidence/product boundaries.

No runtime, storage, identity, authority or conformance status is inherited automatically.

## Governance vocabulary

Keep separate:

```text
Decision status
≠ Evidence level
≠ Implementation status
≠ Operator approval
```

An accepted ADR does not mean complete implementation. A completed workflow does not establish claims beyond its exact checks.

## Documentation synchronization

Material PRs must update relevant:

- `STATUS.md`;
- `docs/ai/CURRENT_STATE.md`;
- `docs/ai/P4_IMPLEMENTATION_RECORD.md`;
- `docs/ai/KNOWN_RISKS.md`;
- `docs/ai/COMPONENT_MAP.md`;
- `docs/ai/WORK_LOG.md`;
- ADR/RFC/public/profile/package docs;
- Notion or structured hand-off.

GitHub must remain sufficient without Notion.

## Change discipline

1. establish exact base/head and phase scope;
2. inspect affected contracts/tests/evidence;
3. preserve Issue #1, Issue #18 and ecosystem boundaries;
4. make the smallest coherent change;
5. run narrow checks, then final exact-head gates;
6. update documentation and Notion;
7. inspect diff, checks, artifacts, reviews and threads;
8. merge with expected head SHA.

Do not combine P4 finalization with P5, deletion execution, production deployment or cross-project wiring.
