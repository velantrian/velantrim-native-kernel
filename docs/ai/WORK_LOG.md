# 🧾 Native Kernel AI Engineering Work Log

This is a concise chronology and hand-off surface. Re-verify exact SHAs, runs and artifacts before treating an entry as present reality.

---

## 2026-08-07 — C4 offline shadow implementation merged; main evidence reproduced

```text
Status:            MERGED / C4 PARTIAL / OFFLINE RECORDED-WORKLOAD SHADOW
Issue / PR:        #61 / #62
Base main:         b10be105743355a04e58611639a9d28faf7ea514
Final PR head:     b7786c088ef2cfd203c02625a5e0c40129cbf148
Merge/main:        07bf1cc955307783f8eaa3becbaa924087b8b325
ADR:               ADR-0020
C5 / production:   NOT AUTHORIZED / NOT ESTABLISHED
Notion impact:     GITHUB_AND_NOTION AFTER CHECKPOINT MERGE
```

Authorized boundary:

```text
OFFLINE_RECORDED_WORKLOAD_ONLY
SHADOW_ONLY
NO AUTHORITY PROMOTION
NO AUTHORITATIVE WRITES
NO SIDE EFFECTS
NO C5 / PRODUCTION / ECOSYSTEM WIRING
```

Implemented:

- approved `nk-shadow-workload/1` dataset;
- exact dataset SHA-256 binding;
- authority-free offline evaluator;
- `nk-shadow-report/1` protocol;
- per-case bounded `nk-shadow-receipt/1`;
- semantic, behavioural, integrity and proof-boundary comparison;
- explicit allowed operational differences;
- fail-closed critical and semantic divergence gates;
- complete 72-ID report with C4 limited to 45 C3-supported assertions;
- strict validators and anti-overclaim tests;
- 4× C4 matrix producing P4, P5, C3 and C4 reports;
- P1–P5 regressions in every C4 job;
- C4-aware public, AI continuity, governance, contract, profile and tooling documentation.

Approved dataset:

```text
dataset_id:      native-kernel/c4-offline-shadow-v1
sha256:          15fb81d8858dcc4e349ffe87c257b25450db026473614582faa7817f90249da3
cases:           15
assertion scope: 45 / 45 C3-supported assertions
```

### Delivery and defect evidence

The first monolithic connector payload was truncated and failed with `base64: invalid input`; no source evidence was claimed from that run.

The payload was replaced by six individually hashed parts plus final archive digest `c7895b487762853f3236e30cff5c69db1f9482a5ef360f7d29f2b5ce582e5066`. Bootstrap run `31187117717` passed all hashes, 19 C4 tests, manifest validation, compileall and source publication. Temporary bootstrap files/workflow were removed before review.

The first genuine matrix run `31187288110` exposed a test that inherited CI evidence environment variables. The test was isolated without weakening evaluator or validator requirements.

A stale root package marker still claimed P3 and was corrected to `0.6.0-c4`.

### Exact final-head evidence

```text
Final head:    b7786c088ef2cfd203c02625a5e0c40129cbf148
C4 run:        31189149796 — PASS
P5/C3 run:     31189149627 — PASS
P4 run:        31189149839 — PASS
P1 run:        31189149436 — PASS
Fixtures:      31189149449 — PASS
AI context:    31189149274 — PASS
```

### Exact implementation-main evidence

```text
Main:          07bf1cc955307783f8eaa3becbaa924087b8b325
C4 run:        31189474449 — PASS
P5/C3 run:     31189474409 — PASS
P4 run:        31189474739 — PASS
P1 run:        31189474300 — PASS
Fixtures:      31189474351 — PASS
AI context:    31189474423 — PASS
```

Matrix:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Main-bound artifact digests:

```text
py3.11/pg16 sha256:3e58a0ea73445d99a94c1e6b7c637640b9852e20b0a71a47f243a14e49995e44
py3.11/pg18 sha256:14cd00c605d247873ff4ae58b3e8d884b6a3e986f13c1f47e0665eee5e33cb9e
py3.12/pg16 sha256:08e1ecccc2679a7ce7bc8fadf43a9586794696b08f8f549f9350d8c658cc160f
py3.12/pg18 sha256:4f890220eb7b1aed36aab74e4aedf4b6e6a4bd71dcc81534a6fe546ae9c75fd6
```

One main-bound artifact was downloaded and inspected:

```text
15 / 15 cases matched
15 Shadow Receipts
45 / 45 C3-supported assertions covered
0 semantic divergences
0 critical divergences
0 missing Receipts
30 allowed operational differences
72 assertion results
status: PASS
support_state: PARTIAL
```

Its inspected Receipt recorded no authority promotion, authoritative write or side effect.

```text
C4 PASS for one approved recorded dataset
≠ live production shadowing
≠ authority promotion
≠ candidate approval
≠ exhaustive equivalence
≠ all 72 supported
≠ C5
≠ production readiness
```

Remaining publication work: merge the docs-only checkpoint, reproduce checkpoint/main evidence, synchronize Notion and close Issue #61.

---

## 2026-08-07 — P5 SQLite and assertion-scoped C3 merged

```text
Issue / PR:      #58 / #59
Final PR head:   6483c9a229aea7d49929745b7652e67f1c39949c
Merge:           a8bb0ae232b977856730a1a4f21f977c1f69ca0a
Checkpoint main: b10be105743355a04e58611639a9d28faf7ea514
```

```text
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
support_state:     PARTIAL
```

Implemented a materially independent stdlib SQLite profile, complete profile reports and a separate `nk-equivalence-report/1` comparator. All `NK-EPI-001…008` remained proposed and unsupported.

---

## Earlier implementation phases

```text
P4 / PR #56 / merge db6d65f69f7fc0c42861e5ab45869ec9c2f3d8ad / ADR-0018
P3 / PR #50 / merge 4af642930e18752f8f8b0bce75df355f76100d6f / ADR-0017
P2 / PR #47 / merge 113452a365890bf6c143d76657b810be59530ed4 / ADR-0016
P1 / PR #44 / merge 9fd608f3f1d2915b961644015eb6b5e1a93e84d3 / ADR-0015
```

---

## Continuing rule

Record exact PR/SHA, dataset ID/digest, support counts, evidence level, artifacts, thresholds, authority boundary, limitations, Notion state and next action. Never infer complete support, truth, authenticity, physical deletion, operational equivalence or production readiness from C2/C3/C4 evidence.
