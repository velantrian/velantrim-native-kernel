# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-07  
**Last verified public `main`:** `4f8cb0a8b7d9ca678a8578cf005b118fd6dff150`  
**Active branch / PR / issue:** `agent/p4-conformance-adapter` / #56 / #55  
**Repository status:** `RESEARCH / P4 PARTIAL ASSERTION CONFORMANCE / NOT PRODUCTION-READY`

> Context checkpoint ≠ automatically current main. Re-check the branch ref, final PR head, workflows, artifact state, reviews and merge SHA.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
P4 C2 ≠ C3
C2 SUPPORTED ASSERTIONS ≠ SUPPORT FOR ALL 72
ASSERTION EVIDENCE ≠ TRUTH / AUTHENTICITY / PHYSICAL ERASURE
C1 ≠ C2 ≠ C3
```

## Operator gate

```text
RFC-0002:              ACCEPTED / APPROVED
P1 semantic core:      MERGED / REPOSITORY-TESTED
P2 PostgreSQL adapter: MERGED / REPOSITORY-INTEGRATION-TESTED
P3 replay/projections: MERGED / REPOSITORY-INTEGRATION-TESTED
P4 conformance:        AUTHORIZED / PARTIAL / C2 PREVIOUS-HEAD EVIDENCE
P5 / C3:               REQUIRE SEPARATE GO
Issue #1 / #18:        ACTIVE / INDEPENDENT
```

Decision and implementation records: Issue #55, ADR-0018, PR #56 and `P4_IMPLEMENTATION_RECORD.md`.

## P4 route

```text
contract registry 1.1.0
→ P1 semantic/identity/authority checks
→ P2 PostgreSQL append/fencing checks
→ P3 replay/projection/Receipt checks
→ 72 explicit assertion results
→ passed-check traceability + limitations
→ strict report validation
→ per-matrix JSON evidence artifacts
```

## Assertion map

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
TOTAL:       72
```

All `NK-EPI-001…008` results remain `UNSUPPORTED` because their registry decision remains `PROPOSED`.

## Initial exact C2 evidence

Executable/evidence head:

```text
93710131fffdea7d9a586cc05e7f258c07fae707
```

```text
P4 run 31175767586 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
P1 run 31175767587 — PASS
P2 run 31175767636 — PASS
P3 run 31175768175 — PASS
Fixture run 31175767614 — PASS
Artifacts: 4 retained JSON reports
```

Each matrix job generated and strictly validated a C2 report, then passed P1–P3 regressions and compileall.

The first P4 workflow run `31175593261` failed only because the standalone adapter did not bootstrap repository root. Full C1 integration passed in that run. The CLI path was corrected without weakening checks, statuses or validation.

## Evidence meaning

```text
support_state: PARTIAL
C2:            REPOSITORY_REPRODUCED for 41 SUPPORTED assertions
C3:            NOT_ESTABLISHED
C4/C5:         NOT_ESTABLISHED
```

C2 does not apply to the 13 `PARTIAL` or 18 `UNSUPPORTED` results. One PostgreSQL profile cannot establish cross-profile equivalence.

## Explicitly absent

- P5 independent SQLite profile;
- C3 cross-profile equivalence;
- complete conflict subsystem;
- physical/cryptographic deletion execution;
- restore-before-visibility enforcement;
- cross-project authority adapter;
- network API;
- truth/signature/notarization certification;
- C4/C5 or production guarantees;
- Titan, Mentaury or Crystal runtime wiring;
- historical `v0.1.2.1` recovery.

## Current finalization gates

1. complete GitHub and Notion documentation synchronization;
2. repeat P4, P1, P2, P3, fixture and AI-context checks on one final exact PR head;
3. verify four final-head artifacts;
4. inspect full diff, comments, reviews and unresolved threads;
5. merge only with P5/C3/deletion/production/ecosystem scope absent;
6. close Issue #55 after final publication evidence;
7. require separate operator GO before P5/C3.
