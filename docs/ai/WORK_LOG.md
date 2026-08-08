# 🧾 Native Kernel AI Engineering Work Log

Re-verify exact SHAs, live issue state, runs and artifacts before treating an entry as current reality.

---

## 2026-08-08 — SQLite integrity and WAL safety remediation opened

```text
Base main:              20b80a40b360670c1231865b020a3fa62208c471
Branch:                 agent/sqlite-integrity-wal-safety
Decision:               ADR-0023 ACCEPTED / APPROVED
Repository evidence:    PENDING
Assertion map / NK-EPI: UNCHANGED
```

Implemented in the candidate:

- strict SQLite Event Envelope equality for contract, time, nested payload and exact fields;
- exact field-set parity in the PostgreSQL stored Event verifier;
- stored JSON failures normalized to `StoredEventCorrupt`;
- fail-closed linked SQLite 3.51.3 WAL minimum;
- pinned official SQLite source archive with SHA-256 verification in P5/C3/C4/C5 CI;
- evidence metadata must match the actually linked SQLite version;
- atomic migration execution without `executescript()` implicit commit;
- `timeout_seconds` now controls `PRAGMA busy_timeout`;
- regression tests for previously accepted malformed envelopes and failure paths.

```text
local tests on linked SQLite 3.51.3
≠ repository reproduction
≠ re-adjudicated assertion status
≠ replacement of historical C5 evidence
```

Next: exact-head matrices, additive artifact capture, review, merge, final state/Notion synchronization. Reducer dangling/self/cycle semantics remain a separate contract-first slice because current accepted fixtures do not define the proposed rejection rule.

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
