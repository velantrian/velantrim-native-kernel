"""Velantrim Native Kernel clean implementation lineage.

P1 semantic core, bounded P2 PostgreSQL append/idempotency, bounded P3
replay/projection/Receipt mechanisms, P4 assertion-scoped PostgreSQL C2, P5
independent SQLite/C3 and C4 authority-free offline shadow evaluation exist.
The implementation remains partial and not production-ready; C5, live shadowing,
physical deletion, ecosystem wiring and production claims remain out of scope.
"""

__version__ = "0.6.0-c4"
