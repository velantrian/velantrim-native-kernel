# Conformance tooling

This directory contains two distinct layers:

```text
fixture-integrity tooling
≠ PostgreSQL P4 runtime adapter
```

## Fixture-integrity layer

```bash
python tools/conformance/runner.py validate
python -m unittest discover -s tests -p 'test_conformance_runner.py' -v
```

It validates:

- unique registry assertion IDs;
- identity golden/invalid vectors;
- Event commitments and hash-chain fixtures;
- idempotency scenarios;
- deletion state transitions and Receipt limits;
- positive/negative `NK-EPI` fixture coverage;
- base evidence-report structure and exact assertion coverage.

The built-in fixture reader deliberately emits every assertion as `UNSUPPORTED`. Its `support_state: SUPPORTED` means only that the fixture reader completed. It is not Kernel runtime conformance.

## P4 PostgreSQL adapter

The runner-compatible adapter is:

```text
tools/conformance/postgresql_profile_adapter.py
```

It executes semantic and real PostgreSQL checks, then emits `nk-evidence-report/1` for all 72 assertions.

Local C1 example:

```bash
export NK_TEST_POSTGRES_DSN='postgresql://postgres:postgres@127.0.0.1/native_kernel_test'
export NK_CONFORMANCE_LEVEL=C1
export NK_EVIDENCE_LEVEL=LOCALLY_TESTED

python tools/conformance/runner.py adapter \
  --output p4-report.json \
  -- python tools/conformance/postgresql_profile_adapter.py

python tools/conformance/validate_p4_report.py p4-report.json
```

Repository C2 example uses the same adapter with exact CI metadata:

```text
NK_CONFORMANCE_LEVEL=C2
NK_EVIDENCE_LEVEL=REPOSITORY_REPRODUCED
NK_EVIDENCE_COMMIT=<exact PR head>
NK_EVIDENCE_RUN_ID=<GitHub Actions run ID>
NK_PYTHON_VERSION=<matrix Python>
NK_POSTGRESQL_VERSION=<matrix PostgreSQL>
```

A self-generated JSON file is not sufficient C2 evidence. Verify the external GitHub run, exact head and retained artifact.

## Current P4 support map

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
support_state: PARTIAL
```

C2 applies only to the `SUPPORTED` results. All `NK-EPI-001…008` remain `UNSUPPORTED` because the family remains `PROPOSED`.

## Strict validation

`validate_p4_report.py` rejects:

- missing/duplicate/unknown assertion IDs;
- wrong support counts;
- supported/partial results without evidence;
- unknown or failed referenced checks;
- missing limitations;
- proposed `NK-EPI` promotion;
- C2 reports with `LOCAL` metadata;
- missing C3/truth/deletion boundaries.

## Tests

```bash
python -m unittest discover -s tests -p 'test_p4_conformance_unit.py' -v
python -m unittest discover -s tests -p 'test_p4_manifest.py' -v
python tools/profiles/validate_p4_manifest.py

NK_TEST_POSTGRES_DSN='postgresql://...' \
  python -m unittest discover -s tests -p 'test_p4_postgresql_integration.py' -v
```

## Boundaries

```text
P4 C2 ≠ all 72 supported
P4 C2 ≠ C3
P4 C2 ≠ truth/authenticity
P4 C2 ≠ physical deletion
P4 C2 ≠ production certification
```

P5/C3 requires a separate explicit operator GO and a materially independent profile.
