# 🧾 Native Kernel AI Engineering Work Log

Re-verify exact SHAs, live issue state, runs and artifacts before treating an entry as current reality.

---

## 2026-08-08 — Post-merge Codex integrity review follow-up in progress

```text
Reviewed main:            d8fe6c9f6e1233eb29ade630a85771e581c2813e
Source reviews:           PR #69 + PR #70 / 4 unresolved actionable threads
Classification:           Contract + Implementation Profile + Evidence + Governance
Candidate status:         LOCAL FOCUSED TESTS PASS / PR AND REPOSITORY CI PENDING
Assertion map / NK-EPI:   UNCHANGED
```

Reproduced and corrected in the candidate tree:

- JSON `true` versus `1` type confusion in stored Event envelope comparison;
- absent `tools/sqlite/**` pull/push triggers in P5/C3, C4 and C5;
- undeclared ADR-0023 fields in `evidence-bundle-v1.schema.json`;
- associated P5/C3 and C4 run IDs accepted as arbitrary positive integers.

Historical and ADR-0023 ZIPs remain byte-identical and keep their original evidence scope. Final PR/main runs and synchronization must be appended after merge; no maturity, production, assertion or NK-EPI promotion is authorized.

## 2026-08-08 — SQLite integrity and WAL safety remediation completed

```text
PR:                     #69 SQUASH-MERGED
Runtime main:           675aa4b398a2fc0181dc71d38904a2d33a09f5f8
Decision:               ADR-0023 ACCEPTED / APPROVED
Repository evidence:    PR-HEAD + FINAL-MAIN PASS / ADDITIVE BUNDLE CAPTURED
Assertion map / NK-EPI: UNCHANGED
```

Completed:

- strict SQLite Event Envelope equality for contract, time, nested payload and exact fields;
- exact field-set parity in the PostgreSQL stored Event verifier;
- stored JSON failures normalized to `StoredEventCorrupt`;
- fail-closed linked SQLite 3.51.3 WAL minimum;
- pinned official SQLite source archive with SHA-256 verification in P5/C3/C4/C5 CI;
- evidence metadata must match the actually linked SQLite version;
- atomic migration execution without `executescript()` implicit commit;
- `timeout_seconds` now controls `PRAGMA busy_timeout`;
- regression tests for previously accepted malformed envelopes and failure paths.

Repository P5/C3, C4 and C5 matrices passed at PR head `ab7a203c…` and final main `675aa4b3…`. Eight exact new C5 archives are preserved under `evidence/c5/2026-08-08-adr0023/`; the 2026-08-07 bytes remain unchanged. Re-adjudication preserved 45/10/17/0 and NK-EPI 0/8. Reducer dangling/self/cycle semantics remain a separate contract-first slice because current accepted fixtures do not define the proposed rejection rule.

Evidence publication PR #70 final head `c9d3944627b40619002428d2a37b8621b2cbfe3b` squash-merged as `f13e0c8a948789d8d4e93e95fd95b61324478528`. Exact evidence payload commit `65d3375dbb5506540ba6d2d41e5508ea9c5dabc5` has tree `da5dfd59dbdcc75e930898a8a79ddd67fa7aec68`. All post-merge checks passed, and the five canonical Notion surfaces contain the final publication record.

## 2026-08-07 — C5 evidence preserved; state surfaces reconciled

```text
Verified source checkpoint: 3d56912260ea41b5b501b65477bff1642dfc2d58
Implementation checkpoint:  296981ae84ad5bdab5dabbec9b7b9ebb43af63d7
Issue #64:                 CLOSED / COMPLETED
Status:                    C5 PARTIAL / NOT PRODUCTION-READY
```

Completed:

- downloaded and preserved four implementation-main C5 ZIPs;
- downloaded and preserved four final-main C5 ZIPs;
- verified all eight archive SHA-256 values against GitHub digests;
- recorded exact six-file inventories and file-level hashes;
- added `nk-evidence-bundle/1` manifest and strict verifier;
- added `nk-project-state/1` snapshot and validator;
- separated historical recovery, clean implementation and long-horizon research;
- corrected stale Issue #64 and checkpoint language;
- moved post-C5 proposals into a research-only backlog;
- preserved `NK-EPI 0/8` and all production/non-authority boundaries.

```text
retained bytes
≠ broader evidence than the producing runs
project-state snapshot
≠ self-updating remote truth
research backlog
≠ implementation authorization
```

Remaining:

- repository CI and review for this reconciliation;
- Notion synchronization in the same work cycle;
- separate authorization for any NK-EPI implementation.

---

## 2026-08-07 — C5 bounded operational rehearsal implemented

```text
Issue / PR / ADR: #64 / #65 / ADR-0021
Base main:        d1dd4986a8496cd9ca3e353d33ca422038c65d40
Implementation:   296981ae84ad5bdab5dabbec9b7b9ebb43af63d7
Final checkpoint: 3d56912260ea41b5b501b65477bff1642dfc2d58
```

Implemented an immutable 18-scenario plan, operational report/Receipt/backup protocols, PostgreSQL/SQLite rehearsal, rollback, replay, quarantine restore, corruption/incident checks, privacy canaries, bounded load, strict validators and four-environment evidence.

---

## Previous milestones

```text
C4 / PR #62 + checkpoint #63
P5/C3 / PR #59 + checkpoint #60
P4 / PR #56
P3 / PR #50
P2 / PR #47
P1 / PR #44
```
