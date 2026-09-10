# Native Kernel reproducibility

Operational guide for a new developer, AI reviewer, CI job, or local checkout. This is not an architecture document.

Environment readiness is not semantic proof, H11 qualification, runtime thaw, Final Canon, or production authorization. The bounded laboratory remains a research profile.

```text
research lab ≠ production
env ready ≠ semantically proven
env ready ≠ H11 executed
env ready ≠ runtime authorized
env ready ≠ Final Canon
```

Current authority (unchanged by this guide): H11 `NOT_TESTED`; reviewer/reproducer `NOT_ESTABLISHED`; admission `BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER`; runtime expansion `FROZEN`; Final Canon `DEFERRED / NOT AUTHORIZED`; production `false`.

Read-only environment probe:

```bash
python tools/environment_doctor.py --repo .
```

**Default exit contract:** exit `0` without `--strict` means only `CORE` readiness (validated Python minor plus usable Git repository/HEAD). It does **not** mean SQLite/WAL, PostgreSQL, Rust/BPV1, complete Git history, or `FULL_SUITE` readiness. Always read the named status lines. `--strict` exits non-zero unless the full optional matrix (SQLite WAL floor, PostgreSQL DSN + driver, pinned Rust, complete git history) is ready.

## Python

CI workflows currently exercise **Python 3.11 and 3.12** only. No other minor version is validated here.

Python version is not the linked SQLite version. A valid 3.11/3.12 interpreter may still load an unsafe SQLite library.

## SQLite

WAL profile code checks the **actually linked** C library:

```bash
python -c 'import sqlite3; print(sqlite3.sqlite_version)'
```

Authoritative floor: `MINIMUM_WAL_SAFE_SQLITE = "3.51.3"` in [`native_kernel/sqlite_profile/runtime.py`](../native_kernel/sqlite_profile/runtime.py). Versions below that floor are not SQLite/WAL integration-ready and must never be inferred ready from the default doctor exit code.

## PostgreSQL

DSN environment variable used by tests and workflows: **`NK_TEST_POSTGRES_DSN`**.

Driver range installed by CI: `psycopg[binary]>=3.3,<3.4` from [`profiles/postgresql-reference-v0/requirements-p2-ci.txt`](../profiles/postgresql-reference-v0/requirements-p2-ci.txt). CI PostgreSQL images: **16 and 18**.

Absent DSN means relevant integration modules SKIP; it is not a PostgreSQL semantic pass.

## Rust

Evidence-backed pin only: [`experiments/bpv1/BPV1-001/rust-toolchain.toml`](../experiments/bpv1/BPV1-001/rust-toolchain.toml) channel **`1.97.1`**, profile `minimal`.

## Git history

CI continuity jobs check out with `fetch-depth: 0`. Git-bound checkpoint tests SKIP on a shallow clone. `environment_doctor.py` reports shallow vs complete history; shallow is not a core Python failure.

## Quick validation

```bash
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_architecture_freeze.py --repo .
python tools/ai_context/validate_reconciliation.py --repo .
python tools/ai_context/validate_context.py --repo .
python tools/ai_context/validate_h11_execution_admission.py --repo .
```

These prove routing and declared boundaries. They do not qualify an H11 reviewer, execute H11, or thaw runtime.

## Targeted tests and discovery guard

Do not assume a file is in CI merely because it matches `test*.py`.

`tools/ci/check_test_discovery.py` is a **bounded static coverage heuristic**. It inventories repository test modules against supported explicit unittest command forms and pull-request path filters. It does **not** execute workflow jobs and does **not** prove runtime reachability, matrix-condition execution, reusable-workflow expansion, shell-branch reachability, or arbitrary YAML semantics.

A green discovery guard therefore means only: within its documented supported syntax, each discovered test module has a matching declared unittest invocation and a matching pull-request path trigger.

## Full suite

```bash
python -m unittest discover -s tests -v
```

A local result is environment-scoped evidence, not repository CI evidence. Numeric totals from prior local runs are historical snapshots, not repository invariants, and should always be interpreted with their SHA, date, Python, SQLite, PostgreSQL DSN, Rust, and Git-history context.

## Result classification

Use unittest/validator outcomes as written. Do not convert environment gaps into semantic PASS.

| Class | Meaning |
|---|---|
| **PASS** | Assertions/validators succeeded |
| **FAILURE** | Assertion or validator rejected a claim/state |
| **ERROR** | Exception during test execution, including fail-closed environment preconditions such as unsafe linked SQLite |
| **SKIP** | Declared precondition absent |
| **ENVIRONMENT PRECONDITION FAILURE** | Environment cannot honestly execute that suite; not a Kernel semantic result |

`environment_doctor.py` separates `CORE`, `SQLITE_INTEGRATION`, `POSTGRES_INTEGRATION`, `BPV1_EXECUTION`, `GIT_HISTORY`, and `FULL_SUITE`; those statuses must be read independently.