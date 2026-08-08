# SQLite runtime safety tooling

`build_safe_sqlite.sh` builds the exact SQLite library used by the P5/C3/C4/C5 Linux CI jobs.

```text
SQLite: 3.51.3
source: https://sqlite.org/2026/sqlite-autoconf-3510300.tar.gz
SHA-256: 81f5be397049b0cae1b167f2225af7646fc0f82e4a9b3c48c9ea3a533e21d77a
```

The script downloads into a unique temporary directory, verifies the archive before extraction, builds a shared library under an explicit non-root prefix, and checks the version loaded by Python.

```bash
tools/sqlite/build_safe_sqlite.sh /tmp/native-kernel-sqlite-3.51.3 /usr/bin/python3
LD_LIBRARY_PATH=/tmp/native-kernel-sqlite-3.51.3/lib \
  /usr/bin/python3 -c 'from native_kernel.sqlite_profile import linked_sqlite_version; print(linked_sqlite_version())'
```

This is profile/CI tooling, not Architecture Canon and not a claim that SQLite and PostgreSQL have equivalent operational behavior.
