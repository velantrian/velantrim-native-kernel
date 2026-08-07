# Conformance and shadow-evidence tooling

This directory contains four distinct layers:

```text
fixture integrity
≠ single-profile evidence adapters
≠ cross-profile equivalence comparator
≠ authority-free offline shadow evaluator
```

## Fixture-integrity layer

```bash
python tools/conformance/runner.py validate
python -m unittest discover -s tests -p 'test_conformance_runner.py' -v
```

It validates registry IDs, identity vectors, Event/hash fixtures, idempotency, deletion transitions, `NK-EPI` fixture coverage and base report structure.

The built-in fixture reader deliberately emits every assertion as `UNSUPPORTED`. Fixture PASS is not Kernel runtime conformance.

## PostgreSQL P4 adapter

`postgresql_profile_adapter.py` executes semantic and real PostgreSQL checks and emits `nk-evidence-report/1` for all 72 assertions.

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

`sqlite_profile_adapter.py` executes the independent stdlib-`sqlite3` profile and emits `nk-evidence-report/1` for all 72 assertions.

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

`cross_profile_comparator.py` uses a distinct protocol, `nk-equivalence-report/1`. It must not be routed through the generic single-profile evidence runner.

```bash
export NK_TEST_POSTGRES_DSN='postgresql://postgres:postgres@127.0.0.1/native_kernel_test'
export NK_TEST_SQLITE_PATH='./p5-c3.db'
export NK_EVIDENCE_LEVEL=LOCALLY_TESTED

python tools/conformance/cross_profile_comparator.py \
  contracts/fixture-pack.json \
  > c3-equivalence-report.json

python tools/conformance/validate_p5_report.py c3 c3-equivalence-report.json
```

The comparator executes declared BYTE, STRUCTURAL, SEMANTIC and BEHAVIOURAL checks and emits:

```text
45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
support_state: PARTIAL
```

All `NK-EPI-001…008` remain unsupported.

## C4 offline shadow evaluator

`offline_shadow_evaluator.py` consumes:

```text
1. exact approved nk-shadow-workload/1 dataset bytes
2. exact validated nk-equivalence-report/1 prerequisite
```

Local generation:

```bash
export NK_EVIDENCE_LEVEL=LOCALLY_TESTED

python tools/conformance/offline_shadow_evaluator.py \
  contracts/shadow-workload-v1.json \
  c3-equivalence-report.json \
  > c4-shadow-report.json

python tools/conformance/validate_c4_report.py c4-shadow-report.json
```

Repository metadata requires:

```text
NK_EVIDENCE_LEVEL=REPOSITORY_REPRODUCED_OFFLINE_SHADOW
NK_EVIDENCE_COMMIT=<exact head>
NK_EVIDENCE_RUN_ID=<exact Actions run>
NK_PYTHON_VERSION=<matrix Python>
NK_POSTGRESQL_VERSION=<matrix PostgreSQL>
NK_SQLITE_VERSION=<runtime SQLite>
```

Approved dataset:

```text
dataset_id:      native-kernel/c4-offline-shadow-v1
sha256:          15fb81d8858dcc4e349ffe87c257b25450db026473614582faa7817f90249da3
cases:           15
assertion scope: 45 / 45 C3-supported assertions
```

The evaluator emits `nk-shadow-report/1` and one bounded `nk-shadow-receipt/1` per case.

Mandatory authority boundary:

```text
mode:                  SHADOW_ONLY
authority promotion:   FORBIDDEN
authoritative writes:  FORBIDDEN
side effects:           FORBIDDEN
promotion decision:    NOT_AUTHORIZED
```

## Strict validation

`validate_p4_report.py` guards the PostgreSQL C2 report.

`validate_p5_report.py` guards SQLite C2 and cross-profile C3 maps, traceability, proposed-family non-promotion, difference declarations, repository metadata and non-claims.

`validate_c4_report.py` rejects:

- wrong shadow protocol, dataset identity or dataset digest;
- wrong/missing C3 prerequisite binding;
- missing, duplicate or unknown case IDs;
- missing/duplicate Shadow Receipts;
- unsafe authority, write, side-effect or promotion fields;
- incomplete 45-assertion C3-supported coverage;
- wrong complete `45/10/17/0` assertion map;
- semantic or critical divergence above zero thresholds;
- missing limitations;
- false repository C4 metadata;
- live-shadow, authority-promotion, truth, deletion, C5 or production overclaim.

## C4 test route

```bash
python -m unittest discover -s tests -p 'test_c4_shadow_evaluation.py' -v
python -m unittest discover -s tests -p 'test_c4_report_validator.py' -v
python -m unittest discover -s tests -p 'test_c4_manifest.py' -v
python tools/profiles/validate_c4_manifest.py
```

P1–P5 prerequisite tests must also remain green.

## Repository workflow

`.github/workflows/c4-offline-shadow.yml` runs:

```text
Python 3.11/3.12 × PostgreSQL 16/18
+ runner SQLite version
+ C4 unit/manifest/report guards
+ exact P4/P5/C3 prerequisite report generation
+ exact C4 evaluation
+ P1–P5 regressions
+ 4 reports per artifact
```

Each matrix artifact contains:

```text
postgresql-p4-report.json
sqlite-p5-report.json
c3-equivalence-report.json
c4-shadow-report.json
```

A self-generated JSON file is not sufficient C2/C3/C4 evidence. Verify the external exact run, head, jobs and retained artifact bytes.

## Boundaries

```text
C2 ≠ C3 ≠ C4
C4 ≠ all 72 supported
C4 offline shadow ≠ live shadowing
C4 observation ≠ authority promotion
C4 ≠ exhaustive or operational equivalence
C4 ≠ truth/authenticity
C4 ≠ physical deletion
C4 ≠ C5 / production certification
```
