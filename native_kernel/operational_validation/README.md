# Native Kernel C5 operational validation

This package builds and validates bounded C5 rehearsal reports.

It is standard-library-only and profile-neutral. Actual scenarios are executed by `tools/operations/c5_rehearsal.py` through the existing PostgreSQL and SQLite profile APIs.

Protocols:

```text
nk-operational-plan/1
nk-operational-report/1
nk-operational-receipt/1
```

Boundary:

```text
C5_BOUNDED_REHEARSAL
≠ production deployment
≠ live traffic
≠ cloud IAM / network security certification
≠ physical deletion
≠ semantic promotion beyond C4 45/10/17
```
