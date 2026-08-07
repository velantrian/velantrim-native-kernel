# 🧾 Native Kernel AI Engineering Work Log

This is a concise chronology and hand-off surface. Re-verify exact SHAs, runs and artifacts before treating an entry as present reality.

---

## 2026-08-07 — P4 assertion-scoped conformance under review

```text
Status:          PR OPEN / P4 PARTIAL / C2 PREVIOUS-HEAD EVIDENCE
Issue:           #55
PR:              #56
Base main:       4f8cb0a8b7d9ca678a8578cf005b118fd6dff150
Evidence head:   93710131fffdea7d9a586cc05e7f258c07fae707
Profile:         native-kernel/postgresql-reference@0.4-p4
Evidence line:   clean/postgresql-reference/0.1
ADR:             ADR-0018
P4:              AUTHORIZED
P5 / C3:         NOT AUTHORIZED / NOT ESTABLISHED
Notion impact:   GITHUB_AND_NOTION
```

P4 implements a complete 72-ID evidence adapter, not complete support:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
support_state: PARTIAL
```

All eight proposed `NK-EPI` assertions remain `UNSUPPORTED`.

Architecture/evidence route:

```text
registry + fixture pack
→ P1 semantic checks
→ P2 PostgreSQL append/fencing checks
→ P3 replay/projection/Receipt checks
→ assertion-to-check mapping
→ strict nk-evidence-report/1 validation
→ C1 local / C2 repository metadata
→ per-matrix JSON artifacts
```

Implemented:

- `native_kernel.postgresql_profile.conformance`;
- standalone adapter CLI compatible with the existing conformance runner;
- strict P4 report validator;
- complete assertion result emission with no silent skip;
- check/result traceability and mandatory limitations;
- hard support-count guard;
- explicit proposed-family non-promotion;
- P4 implementation manifest and validator;
- 5 mapping/traceability unit tests;
- 5 manifest anti-overclaim tests;
- full PostgreSQL report integration test;
- Python 3.11/3.12 × PostgreSQL 16/18 workflow;
- one retained JSON evidence artifact per matrix job;
- P1/P2/P3 regressions in every P4 job;
- ADR-0018 and public/AI documentation updates.

Initial failure evidence:

```text
run 31175593261 — FAILURE
```

All unit, manifest and full C1 PostgreSQL report checks passed. The standalone adapter failed with `ModuleNotFoundError` because direct script execution did not include repository root. The CLI bootstrap was fixed without weakening checks, mapping or validator requirements.

Initial successful C2 evidence:

```text
head 93710131fffdea7d9a586cc05e7f258c07fae707
P4 run 31175767586 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
P1 run 31175767587 — PASS
P2 run 31175767636 — PASS
P3 run 31175768175 — PASS
Fixture run 31175767614 — PASS
Artifacts: 4 / retained 30 days
```

Artifact digests are recorded in `P4_IMPLEMENTATION_RECORD.md`.

```text
P4 C2 for SUPPORTED assertions
≠ all 72 supported
≠ C3
≠ truth/authenticity
≠ physical deletion
≠ production readiness
```

Remaining work in this cycle:

1. finish README/RFC/profile/AI/Notion synchronization;
2. repeat P4 and governance checks on one final exact PR head;
3. inspect final diff, comments, reviews and unresolved threads;
4. merge PR #56 with expected head;
5. publish post-merge continuity evidence;
6. close Issue #55;
7. keep P5/C3 blocked pending a separate GO.

---

## 2026-08-07 — P3 replay, projections and bounded Receipts merged

```text
Status:        MERGED / P3 PARTIAL / REPOSITORY-INTEGRATION-TESTED
Issue / PR:    #49 / #50
Base:          4e6be77196c633c25dd3896660335c1448b2baf5
Final head:    7e615bc633cbf966211d3b2815f51b8ff9eb9716
Merge:         4af642930e18752f8f8b0bce75df355f76100d6f
Final main:    4f8cb0a8b7d9ca678a8578cf005b118fd6dff150 after checkpoints
ADR:           ADR-0017
```

Final P3 run `31173133661` passed PostgreSQL 16/18 × Python 3.11/3.12 with 8 unique integration scenarios. P2, P1, fixture and AI-context checks passed on the same final head. P3 added verified persisted replay, deterministic upcasting, disposable projection rebuild, stale-head rejection and bounded operational Receipts.

P3 did not establish assertion-scoped conformance, C1/C2/C3 or physical deletion.

---

## 2026-08-07 — P2 PostgreSQL append/idempotency merged

```text
Status:      MERGED / P2 PARTIAL / REPOSITORY-INTEGRATION-TESTED
Issue / PR:  #46 / #47
Final head:  36ddb1d0342914f0c06fe7f31171bac06565ee72
Merge:       113452a365890bf6c143d76657b810be59530ed4
Checkpoint:  4e6be77196c633c25dd3896660335c1448b2baf5
ADR:         ADR-0016
```

Implemented checksum-locked migrations, instance/history head, writer epoch fencing, atomic Event/idempotency transaction, rollback-safe ordering and canonical Event commitments. Final matrix run `31152380799` passed.

---

## 2026-08-06 — P1 semantic core merged

```text
Status:      MERGED / P1 PARTIAL
Issue / PR:  #43 / #44
Final head:  273d9369e624d8e4c4033dc7842ebbcc46642668
Merge:       9fd608f3f1d2915b961644015eb6b5e1a93e84d3
Checkpoint:  bb94835ad612f45e2629655bc9add872d8981357
ADR:         ADR-0015
```

Implemented canonical identity helpers, immutable semantic objects, explicit authority, deterministic reduction, semantic deletion transitions and Receipt overclaim guards. Initial evidence was local; later P2–P4 workflows retained P1 regression evidence.

---

## 2026-08-06 — Clean PostgreSQL reference profile accepted

RFC-0002 and clean lineage `clean/postgresql-reference/0.1` were published through PRs #41/#42. ADR-0015 accepted the clean profile and separately authorized P1. This lineage remains independent from Issue #1 and historical `v0.1.2.1`.

---

## 2026-08-06 — Exact contracts accepted

ADR-0011…0014 accepted `nk-id/1.0`, `nk-event/1.0`, `nk-deletion/1.0` and `nk-fixtures/1.0`. Registry `nk-contract-registry/1.1.0` contains 72 stable assertion IDs; `NK-EPI-001…008` remains proposed.

---

## Continuing rule

Record exact PR/SHA, support counts, evidence level, artifacts, limitations, Notion state and next action. Never infer C3, truth, authenticity, physical deletion or production readiness from P4 C2 evidence.
