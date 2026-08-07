# Current Status

> **Verified:** 2026-08-07  
> **Last verified public `main`:** `db6d65f69f7fc0c42861e5ab45869ec9c2f3d8ad`  
> **P4 implementation:** PR #56 / merge `db6d65f69f7fc0c42861e5ab45869ec9c2f3d8ad`  
> **Repository status:** `RESEARCH / P4 PARTIAL ASSERTION CONFORMANCE / NOT PRODUCTION-READY`

## Current profile

```text
Profile ID:       native-kernel/postgresql-reference
Profile version:  0.4-p4
Evidence lineage: clean/postgresql-reference/0.1
P1:               MERGED / REPOSITORY-TESTED
P2:               MERGED / REPOSITORY-INTEGRATION-TESTED
P3:               MERGED / REPOSITORY-INTEGRATION-TESTED
P4:               MERGED / PARTIAL / C2 REPOSITORY-REPRODUCED
P5:               NOT AUTHORIZED
```

PostgreSQL, Psycopg, Python, SQL layouts, locks and current processors remain replaceable profile technologies, not Architecture Canon.

## Assertion-scoped result map

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
TOTAL:       72
support_state: PARTIAL
```

C2 applies only to the 41 `SUPPORTED` results. All `NK-EPI-001…008` remain `UNSUPPORTED` and `PROPOSED`.

```text
P4 C2 ≠ support for all 72
P4 C2 ≠ C3
P4 C2 ≠ truth/authenticity
P4 C2 ≠ physical deletion
P4 C2 ≠ production readiness
```

## Final PR-head evidence

```text
PR #56 final head: 0e7adf71475d37d5c096718762cbc08086c5e465
P4 run:            31177071487 — PASS
P3 run:            31177072239 — PASS
P2 run:            31177071499 — PASS
P1 run:            31177071518 — PASS
Fixture run:       31177071508 — PASS
AI-context run:    31177071481 — PASS
Artifacts:         4 retained JSON reports
```

## Exact main-push evidence

```text
main:          db6d65f69f7fc0c42861e5ab45869ec9c2f3d8ad
P4 push run:   31177335611 — PASS
P3 push run:   31177335146 — PASS
P2 push run:   31177335749 — PASS
P1 push run:   31177335898 — PASS
Fixture run:   31177335864 — PASS
AI-context:    31177335964 — PASS
```

P4 push matrix passed Python 3.11/3.12 × PostgreSQL 16/18 and retained four `main`-bound JSON artifacts for 30 days.

Main-bound artifact digests:

```text
py3.11/pg16 sha256:aad734cc2c1e5e76f8949c07d8a757a4b952788e35ba572148867bf0c221ea6c
py3.11/pg18 sha256:4057790b9abba3f7375b0ed6a56bc9dad58db47f093db66b4007c96322b458fd
py3.12/pg16 sha256:6021a26ff70734f5caa208a04bb50d6b7faf1ab91942d6378f4e0ca5b590dc65
py3.12/pg18 sha256:0661e2640f5d80898a4ba6e041f889d69179d07ad8ba8eab69d0e19caae166ae
```

## Implemented route

```text
P1 semantic identity / authority / reducer
→ P2 PostgreSQL append / idempotency / writer fencing
→ P3 verified replay / projections / bounded Receipts
→ P4 complete 72-ID evidence adapter / strict report validator
```

P4 evaluates and reports bounded behavior. It does not fill unsupported subsystems through documentation.

## Explicitly absent

- P5 independent SQLite profile;
- C3 cross-profile equivalence;
- complete conflict representation/resolution;
- physical or cryptographic deletion execution;
- restore-before-visibility enforcement;
- cross-project authority adapter;
- truth/signature/notarization certification;
- network API;
- C4/C5 and production guarantees;
- Titan, Mentaury or Crystal runtime wiring;
- historical `v0.1.2.1` recovery;
- package publication decision under Issue #18.

## Issue #1 boundary

```text
clean/postgresql-reference/0.1
≠ recovered v0.1.2.1
≠ original 44-test evidence
```

Issue #1 remains active and independent. `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.

## Next gate

P5 and any C3 claim require a new explicit operator GO, a materially independent SQLite profile and retained equivalence-comparison evidence.
