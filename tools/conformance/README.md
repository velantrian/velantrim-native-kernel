# Conformance tooling

This directory contains three distinct layers:

```text
fixture integrity
≠ single-profile evidence adapters
≠ cross-profile equivalence comparator
```

## Fixture-integrity layer

```bash
python tools/conformance/runner.py validate
python -m unittest discover -s tests -p 'test_conformance_runner.py' -v
```

It validates registry IDs, identity vectors, Event/hash fixtures, idempotency, deletion transitions, `NK-EPI` fixture coverage and base report structure.

The built-in fixture reader deliberately emits every assertion as `UNSUPPORTED`. Fixture PASS is not Kernel runtime conformance.

## PostgreSQL P4 adapter

```text
tools/conformance/postgresql_profile_adapter.py
```

It executes semantic and real PostgreSQL checks and emits `nk-evidence-report/1` for all 72 assertions.

```bash
export NK_TEST_POSTGRES_DSN='postgresql://postgres:postgres@127.0.0.1/native_kernel_test'
export NK_CONFORMANCE_LEVEL=C1
export NK_EVIDENCE_LEVEL=LOCALLY_TESTED

python tools/conformance/runner.py adapter \
  --output postgresql-p4-report.json \
  -- python tools/conformance/postgresql_profile_adapter.py

python tools/conformance/validate_p4_report.py postgresql-p4-report.json
```

## SQLite P5 adapter

```text
tools/conformance/sqlite_profile_adapter.py
```

It executes the independent stdlib-`sqlite3` profile and emits `nk-evidence-report/1` for all 72 assertions.

```bash
export NK_TEST_SQLITE_PATH='./p5-test.db'
export NK_CONFORMANCE_LEVEL=C1
export NK_EVIDENCE_LEVEL=LOCALLY_TESTED

python tools/conformance/runner.py adapter \
  --output sqlite-p5-report.json \
  -- python tools/conformance/sqlite_profile_adapter.py

python tools/conformance/validate_p5_report.py sqlite sqlite-p5-report.json
```

PostgreSQL and SQLite single-profile maps are guarded as:

```text
41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
```

## Cross-profile C3 comparator

```text
tools/conformance/cross_profile_comparator.py
```

The comparator uses a distinct protocol, `nk-equivalence-report/1`. It must not be routed through the generic single-profile evidence runner.

```bash
export NK_TEST_POSTGRES_DSN='postgresql://postgres:postgres@127.0.0.1/native_kernel_test'
export NK_TEST_SQLITE_PATH='./p5-c3.db'
export NK_EVIDENCE_LEVEL=LOCALLY_TESTED

python tools/conformance/cross_profile_comparator.py \
  contracts/fixture-pack.json \
  > c3-equivalence-report.json

python tools/conformance/validate_p5_report.py c3 c3-equivalence-report.json
```

Repository C3 metadata additionally requires:

```text
NK_EVIDENCE_LEVEL=REPOSITORY_REPRODUCED
NK_EVIDENCE_COMMIT=<exact head>
NK_EVIDENCE_RUN_ID=<exact Actions run>
NK_PYTHON_VERSION=<matrix Python>
NK_POSTGRESQL_VERSION=<matrix PostgreSQL>
NK_SQLITE_VERSION=<runtime SQLite>
```

The comparator executes declared BYTE, STRUCTURAL, SEMANTIC and BEHAVIOURAL checks and emits:

```text
45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
support_state: PARTIAL
```

Promoted only by cross-profile evidence:

```text
NK-SEM-008
NK-ID-008
NK-EQV-002
NK-EQV-003
```

All `NK-EPI-001…008` remain unsupported.

## Strict validation

`validate_p4_report.py` guards the PostgreSQL C2 report.

`validate_p5_report.py sqlite` rejects:

- incomplete/duplicate/unknown assertion results;
- wrong `41/13/18/0` map;
- missing or failed evidence references;
- missing limitations;
- `NK-EPI` promotion;
- fake repository C2 metadata;
- missing truth/deletion/C3 boundaries.

`validate_p5_report.py c3` rejects:

- wrong equivalence protocol/profile IDs;
- wrong `45/10/17/0` map;
- unknown/failed cross-profile checks;
- untraceable supported/partial results;
- missing allowed/forbidden difference declarations;
- false C3 with local/placeholder metadata;
- operational-equivalence, truth, deletion or production overclaim.

## P5 test route

```bash
python -m unittest discover -s tests -p 'test_sqlite_profile_unit.py' -v
python -m unittest discover -s tests -p 'test_p5_sqlite_integration.py' -v
python -m unittest discover -s tests -p 'test_p5_report_validator.py' -v
python -m unittest discover -s tests -p 'test_p5_manifest.py' -v
python tools/profiles/validate_p5_manifest.py

NK_TEST_POSTGRES_DSN='postgresql://...' \
  python -m unittest discover -s tests -p 'test_p5_cross_profile_integration.py' -v
```

## Repository workflow

`.github/workflows/p5-sqlite-c3.yml` runs:

```text
Python 3.11/3.12 × PostgreSQL 16/18
+ runner SQLite version
+ P1–P4 regressions
+ 3 reports per artifact
```

Each matrix artifact contains:

```text
postgresql-p4-report.json
sqlite-p5-report.json
c3-equivalence-report.json
```

A self-generated JSON file is not sufficient C2/C3 evidence. Verify the external exact run, head, jobs and retained artifact.

## Boundaries

```text
C2 ≠ C3
C3 ≠ all 72 supported
C3 semantic equivalence ≠ operational equivalence
C3 ≠ truth/authenticity
C3 ≠ physical deletion
C3 ≠ C4/C5
C3 ≠ production certification
```
