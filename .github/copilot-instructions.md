# GitHub Copilot instructions for Velantrim Native Kernel

## Mandatory orientation

Before reviewing or changing the repository, read:

1. [`../AGENTS.md`](../AGENTS.md);
2. [`../STATUS.md`](../STATUS.md);
3. [`../docs/ai/README.md`](../docs/ai/README.md);
4. [`../docs/ai/CURRENT_STATE.md`](../docs/ai/CURRENT_STATE.md);
5. [`../docs/ai/P5_IMPLEMENTATION_RECORD.md`](../docs/ai/P5_IMPLEMENTATION_RECORD.md);
6. [`../docs/ai/P4_IMPLEMENTATION_RECORD.md`](../docs/ai/P4_IMPLEMENTATION_RECORD.md);
7. relevant component/risk/work-log entries.

Verify the actual branch/PR SHA, workflows and artifacts before carrying forward any claim.

## Current status

```text
RESEARCH / P5 PARTIAL CROSS-PROFILE CONFORMANCE / NOT PRODUCTION-READY
```

```text
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
support_state:     PARTIAL
```

```text
C2 ≠ C3
C3 ≠ support for all 72
C3 semantic equivalence ≠ operational equivalence
C3 ≠ truth/authenticity
C3 ≠ physical deletion
C3 ≠ C4/C5 or production readiness
```

All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

## Architecture discipline

- Preserve `Architecture Canon → Abstract Contracts → Replaceable Implementation Profiles`.
- PostgreSQL, SQLite, Python, Psycopg, SQL, files, graphs, vectors, LLMs and hardware are replaceable technologies.
- Event history is authoritative about recorded history, not automatically truth.
- Backend IDs/schemas must not become semantic identity accidentally.
- Receipts, evidence reports and equivalence reports are bounded proof, not certification.
- Operator approval is authority, not empirical evidence.

## P5 profile independence

- SQLite must not call PostgreSQL append/replay/projection/Receipt adapters.
- Shared accepted contracts and profile-neutral fixtures are allowed.
- Compare observable contract outcomes, not SQL/table similarity.
- Declare allowed differences explicitly.
- Never normalize away payload, ordering, state, outcome or Receipt differences.

## C3 claim discipline

For a C3 support claim:

1. identify the assertion ID;
2. inspect the exact C3 result status;
3. inspect referenced cross-profile check IDs;
4. verify those checks passed in the same report;
5. preserve result/report limitations;
6. verify exact commit/run/environment/artifact;
7. confirm the result is in the guarded `45/10/17/0` map.

Do not:

- omit unsupported assertions;
- promote `PARTIAL` through prose;
- claim C3 from local tests or environment diversity;
- describe semantic comparison as operational equivalence;
- accept `NK-EPI` through fixture/profile agreement;
- treat a digest without retained bytes as complete evidence.

## Verification

```bash
python -m unittest discover -s tests -p 'test_sqlite_profile_unit.py' -v
python -m unittest discover -s tests -p 'test_p5_sqlite_integration.py' -v
python -m unittest discover -s tests -p 'test_p5_report_validator.py' -v
python -m unittest discover -s tests -p 'test_p5_manifest.py' -v
python tools/profiles/validate_p5_manifest.py

NK_TEST_POSTGRES_DSN='postgresql://...' \
  python -m unittest discover -s tests -p 'test_p5_cross_profile_integration.py' -v
```

Repository C2/C3 requires the exact four-job P5 matrix and retained artifacts containing PostgreSQL, SQLite and C3 reports. Inspect P1–P4 regressions too.

## Source recovery

- Keep clean P1–P5 implementation separate from Issue #1 import.
- Do not label new code/tests `v0.1.2.1` or the original 44-test suite.
- `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.

## Ecosystem boundaries

Native Kernel does not automatically provide runtime/storage/identity/authority/conformance to Titan, Mentaury Soul or Crystal. Integration requires separate governance and evidence.

## Documentation synchronization

Material PRs must update relevant:

- `STATUS.md`;
- `docs/ai/CURRENT_STATE.md`;
- `docs/ai/P5_IMPLEMENTATION_RECORD.md`;
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

Do not combine P5 finalization with C4/C5, deletion execution, production deployment or cross-project wiring.
