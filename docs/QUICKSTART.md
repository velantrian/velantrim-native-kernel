# 🚀 Native Kernel Quickstart

**[English](./QUICKSTART.md) · [Русский](./QUICKSTART.ru.md)**

> **Boundary:** this is a research repository. Running tests does not authorize production use, broaden the assertion map, or prove substrate neutrality.

## 1. Prerequisites

- Python 3.11 or 3.12;
- Bash;
- for the pinned SQLite build: `curl`, `sha256sum`, `tar`, a C compiler, `make`, and standard build tools;
- optional PostgreSQL 16 or 18 plus a Psycopg installation for integration tests.

The repository is currently run from its checkout root with `PYTHONPATH=.` semantics. There is no published Python package or supported `pip install` contract yet.

## 2. Fast semantic-core check

From the repository root:

```bash
python -m unittest discover -s tests -p 'test_semantic_core.py' -v
python -m unittest discover -s tests -p 'test_p1_manifest.py' -v
python -m compileall -q native_kernel
```

These checks exercise the technology-neutral semantic core and P1 manifest. They do not exercise PostgreSQL, SQLite WAL operation, C3 equivalence, C4 shadow evaluation, or C5 rehearsal.

## 3. Why the system SQLite may be rejected

The SQLite profile opens WAL only when the **actually linked** Python `sqlite3` library is SQLite 3.51.3 or later. Older versions fail closed by design because ADR-0023 does not accept them for the current safe-runtime profile.

Check the version loaded by Python:

```bash
python -c 'import sqlite3; print(sqlite3.sqlite_version)'
```

A failure caused by an older linked SQLite is not a skipped safety check and should not be converted into a pass.

## 4. Build the pinned SQLite 3.51.3 profile dependency

```bash
tools/sqlite/build_safe_sqlite.sh \
  /tmp/native-kernel-sqlite-3.51.3 \
  "$(command -v python)"
```

Run Python with that shared library:

```bash
export LD_LIBRARY_PATH="/tmp/native-kernel-sqlite-3.51.3/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
python -c 'from native_kernel.sqlite_profile import linked_sqlite_version; print(linked_sqlite_version())'
```

Expected output:

```text
3.51.3
```

The build script downloads the official source archive, verifies its pinned SHA-256 before extraction, builds under an explicit non-root prefix, and verifies what Python actually loads. See [`../tools/sqlite/README.md`](../tools/sqlite/README.md).

## 5. SQLite unit checks

After exporting `LD_LIBRARY_PATH`:

```bash
python -m unittest discover -s tests -p 'test_sqlite_profile_unit.py' -v
python -m unittest discover -s tests -p 'test_p5_manifest.py' -v
python tools/profiles/validate_p5_manifest.py
```

Some integration tests require PostgreSQL and the environment variables below.

## 6. PostgreSQL integration setup

Install the current CI driver range:

```bash
python -m pip install -r profiles/postgresql-reference-v0/requirements-p2-ci.txt
```

Provide a disposable PostgreSQL database and set:

```bash
export NK_TEST_POSTGRES_DSN='postgresql://postgres:postgres@127.0.0.1:5432/native_kernel_test'
```

Then run the relevant integration suites:

```bash
python -m unittest discover -s tests -p 'test_p2_postgresql_integration.py' -v
python -m unittest discover -s tests -p 'test_p5_cross_profile_integration.py' -v
```

Use a test database only. The repository does not provide production IAM, backup, HA, compliance, or deployment policy.

## 7. Full local discovery

```bash
python -m unittest discover -s tests -v
```

Interpret results carefully:

- PostgreSQL-only tests may skip when `NK_TEST_POSTGRES_DSN` is absent;
- SQLite profile tests should fail closed when Python links an unsupported SQLite version;
- a local pass is not equivalent to repository CI evidence;
- repository CI evidence is scoped to its exact commit, workflow, matrix, and retained artifacts.

## 8. Read before changing code

1. [`../AGENTS.md`](../AGENTS.md)
2. [`../STATUS.md`](../STATUS.md)
3. [`ai/README.md`](./ai/README.md)
4. [`GLOSSARY.md`](./GLOSSARY.md)
5. relevant ADRs and profile documents

For contribution and synchronization rules, see [`../CONTRIBUTING.md`](../CONTRIBUTING.md).
