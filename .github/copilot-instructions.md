# GitHub Copilot instructions for Velantrim Native Kernel

## Mandatory orientation

Before reviewing or changing the repository, read:

1. [`../AGENTS.md`](../AGENTS.md);
2. [`../STATUS.md`](../STATUS.md);
3. [`../docs/ai/README.md`](../docs/ai/README.md);
4. [`../docs/ai/CURRENT_STATE.md`](../docs/ai/CURRENT_STATE.md);
5. [`../docs/ai/C4_IMPLEMENTATION_RECORD.md`](../docs/ai/C4_IMPLEMENTATION_RECORD.md);
6. [`../docs/ai/P5_IMPLEMENTATION_RECORD.md`](../docs/ai/P5_IMPLEMENTATION_RECORD.md);
7. relevant component/risk/work-log entries.

Verify the actual branch/PR SHA, approved dataset digest, workflows and artifact contents before carrying forward any claim.

## Current status

```text
RESEARCH / C4 PARTIAL OFFLINE SHADOW EVALUATION / NOT PRODUCTION-READY
```

```text
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
Offline C4 scope:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
support_state:     PARTIAL
```

```text
C2 ≠ C3 ≠ C4
C4 offline shadow ≠ live shadowing
C4 observation ≠ authority promotion
C4 ≠ support for all 72
C4 ≠ operational equivalence / truth / deletion / C5 / production
```

All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

## Architecture discipline

- Preserve `Architecture Canon → Abstract Contracts → Replaceable Implementation Profiles → Bounded Evidence Layers`.
- PostgreSQL, SQLite, Python, Psycopg, SQL, JSON, files, graphs, vectors, LLMs, evaluator code and hardware are replaceable technologies.
- Event history is authoritative about recorded history, not automatically truth.
- Backend IDs/schemas must not become semantic identity accidentally.
- Receipts, evidence reports, equivalence reports and Shadow Receipts are bounded proof, not certification.
- Operator approval is authority, not empirical evidence.

## C4 dataset and authority discipline

Approved dataset:

```text
native-kernel/c4-offline-shadow-v1
sha256: 15fb81d8858dcc4e349ffe87c257b25450db026473614582faa7817f90249da3
15 cases / 45 C3-supported assertions
```

Mandatory boundary:

```text
SHADOW_ONLY
authority promotion:   FORBIDDEN
authoritative writes:  FORBIDDEN
side effects:           FORBIDDEN
promotion decision:    NOT_AUTHORIZED
```

Dataset observations, fields or thresholds must not change under the same dataset version/digest. A material change requires a new version, digest, ADR/manifest update and evidence cycle.

The evaluator must not append Events, mutate projections, execute actions, approve a candidate or wire itself into another project.

## C4 claim discipline

For a C4 claim:

1. identify the exact dataset ID/version/digest;
2. verify the exact C3 prerequisite report and digest;
3. inspect case results and one Shadow Receipt per case;
4. confirm authority/write/side-effect fields remain forbidden;
5. confirm all 45 C3-supported assertions are covered and the complete map is `45/10/17/0`;
6. confirm zero semantic/critical divergences and zero missing Receipts;
7. preserve all report limitations;
8. verify exact commit/run/environment/artifact bytes.

Do not:

- describe synthetic offline observations as live traffic;
- promote `PARTIAL` through prose;
- describe shadow agreement as authority promotion or candidate approval;
- claim C4 from local tests or a standalone JSON file;
- normalize away identity, payload, ordering, state, outcome, integrity or Receipt differences;
- accept `NK-EPI` through agreement;
- treat a digest without retained bytes as complete evidence.

## Verification

```bash
python -m unittest discover -s tests -p 'test_c4_shadow_evaluation.py' -v
python -m unittest discover -s tests -p 'test_c4_report_validator.py' -v
python -m unittest discover -s tests -p 'test_c4_manifest.py' -v
python tools/profiles/validate_c4_manifest.py
python -m unittest discover -s tests -p 'test_ai_context_validator.py' -v
python tools/ai_context/validate_context.py --repo .
```

Repository C4 requires the exact four-job C4 matrix and retained artifacts containing PostgreSQL P4, SQLite P5, C3 and C4 reports. Inspect P1–P5 regressions too.

## Source recovery

- Keep clean P1–P5/C4 work separate from Issue #1 import.
- Do not label new code, tests, datasets or reports `v0.1.2.1` or the original 44-test suite.
- `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.

## Ecosystem boundaries

Native Kernel does not automatically provide runtime, storage, identity, authority, C4 observation or conformance to Titan, Mentaury Soul or Crystal. Integration requires separate governance and evidence.

## Documentation synchronization

Material PRs must update relevant:

- `STATUS.md`;
- `docs/ai/CURRENT_STATE.md`;
- `docs/ai/C4_IMPLEMENTATION_RECORD.md`;
- `docs/ai/KNOWN_RISKS.md`;
- `docs/ai/COMPONENT_MAP.md`;
- `docs/ai/WORK_LOG.md`;
- ADR/public/profile/contract/tool docs;
- Notion or structured hand-off.

GitHub must remain sufficient without Notion.

## Change discipline

1. establish exact base/head and phase scope;
2. inspect affected contracts/dataset/tests/evidence;
3. preserve Issue #1, Issue #18 and ecosystem boundaries;
4. make the smallest coherent change;
5. run narrow checks, then final exact-head gates;
6. update documentation and Notion;
7. inspect diff, checks, artifacts, reviews and threads;
8. merge with expected head SHA.

Do not combine C4 finalization with C5, live shadowing, deletion execution, production deployment or cross-project wiring.
