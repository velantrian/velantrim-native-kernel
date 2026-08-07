# 🧾 Native Kernel AI Engineering Work Log

This is a concise chronology and hand-off surface. Re-verify exact SHAs, runs and artifacts before treating an entry as present reality.

---

## 2026-08-07 — P4 assertion-scoped conformance merged and reproduced on main

```text
Status:        MERGED / P4 PARTIAL / ASSERTION-SCOPED C2
Issue / PR:    #55 / #56
Base main:     4f8cb0a8b7d9ca678a8578cf005b118fd6dff150
Final PR head: 0e7adf71475d37d5c096718762cbc08086c5e465
Merge/main:    db6d65f69f7fc0c42861e5ab45869ec9c2f3d8ad
Profile:       native-kernel/postgresql-reference@0.4-p4
Evidence line: clean/postgresql-reference/0.1
ADR:           ADR-0018
P5 / C3:       NOT AUTHORIZED / NOT ESTABLISHED
```

Support map:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
support_state: PARTIAL
```

Implemented:

- complete 72-ID PostgreSQL evidence adapter;
- semantic, identity, authority, Receipt, reducer and deletion checks;
- migration, fencing, append, rollback, replay, projection, stale-head and corruption checks;
- strict assertion-to-passed-check traceability;
- mandatory limitations and proposed `NK-EPI` non-promotion;
- C1/C2 metadata boundary;
- strict report and manifest validators;
- Python 3.11/3.12 × PostgreSQL 16/18 workflow;
- one retained JSON artifact per matrix job;
- P1/P2/P3 regressions in every P4 job;
- synchronized public, RFC, ADR, profile, package and AI documentation.

Initial defect evidence:

```text
run 31175593261 — FAILURE
```

All unit/manifest/full C1 checks passed, but direct CLI execution lacked repository-root bootstrap. The bootstrap was corrected without weakening checks, statuses or validation.

Final PR-head evidence:

```text
P4 31177071487 — PASS
P3 31177072239 — PASS
P2 31177071499 — PASS
P1 31177071518 — PASS
Fixtures 31177071508 — PASS
AI context 31177071481 — PASS
4 P4 artifacts retained
```

Exact main-push evidence:

```text
P4 31177335611 — PASS
P3 31177335146 — PASS
P2 31177335749 — PASS
P1 31177335898 — PASS
Fixtures 31177335864 — PASS
AI context 31177335964 — PASS
4 main-bound P4 artifacts retained
```

One final-head artifact was opened and verified to contain 72 results, 18 passed checks, exact run/head/environment metadata and the guarded `41/13/18/0` map.

```text
P4 C2 for SUPPORTED assertions
≠ all 72 supported
≠ C3
≠ accepted NK-EPI
≠ truth/authenticity
≠ physical deletion
≠ production readiness
```

---

## 2026-08-07 — P3 replay, projections and bounded Receipts merged

```text
Issue / PR:  #49 / #50
Final head:  7e615bc633cbf966211d3b2815f51b8ff9eb9716
Merge:       4af642930e18752f8f8b0bce75df355f76100d6f
Checkpoint:  4f8cb0a8b7d9ca678a8578cf005b118fd6dff150
ADR:         ADR-0017
```

Implemented verified persisted replay, deterministic upcasting, disposable projection rebuild, stale-head rejection and bounded operational Receipts. Final P3 matrix passed PostgreSQL 16/18 × Python 3.11/3.12.

---

## 2026-08-07 — P2 PostgreSQL append/idempotency merged

```text
Issue / PR:  #46 / #47
Final head:  36ddb1d0342914f0c06fe7f31171bac06565ee72
Merge:       113452a365890bf6c143d76657b810be59530ed4
Checkpoint:  4e6be77196c633c25dd3896660335c1448b2baf5
ADR:         ADR-0016
```

Implemented checksum-locked migrations, writer epoch fencing, atomic Event/idempotency persistence, rollback-safe ordering and canonical Event commitments.

---

## 2026-08-06 — P1 semantic core merged

```text
Issue / PR:  #43 / #44
Final head:  273d9369e624d8e4c4033dc7842ebbcc46642668
Merge:       9fd608f3f1d2915b961644015eb6b5e1a93e84d3
Checkpoint:  bb94835ad612f45e2629655bc9add872d8981357
ADR:         ADR-0015
```

Implemented canonical identity, immutable semantic objects, explicit authority, deterministic reduction, semantic deletion transitions and Receipt overclaim guards.

---

## 2026-08-06 — Clean PostgreSQL profile and exact contracts

RFC-0002 established `clean/postgresql-reference/0.1`, independently from Issue #1 and historical `v0.1.2.1`.

ADR-0011…0014 accepted `nk-id/1.0`, `nk-event/1.0`, `nk-deletion/1.0` and `nk-fixtures/1.0`. Registry `nk-contract-registry/1.1.0` contains 72 stable assertion IDs; `NK-EPI-001…008` remains proposed.

---

## Continuing rule

Record exact PR/SHA, support counts, evidence level, artifacts, limitations, Notion state and next action. Never infer C3, truth, authenticity, physical deletion or production readiness from P4 C2 evidence.
