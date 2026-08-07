# 🪞 C4 Offline Shadow Evaluation Implementation Record

**Date:** 2026-08-07  
**Issue / PR / ADR:** #61 / #62 / ADR-0020  
**Base main:** `b10be105743355a04e58611639a9d28faf7ea514`  
**Implementation merge/main:** `07bf1cc955307783f8eaa3becbaa924087b8b325`  
**Status:** `MERGED / C4 PARTIAL / OFFLINE RECORDED-WORKLOAD SHADOW / NOT PRODUCTION-READY`

## Authorization and boundary

```text
C4: AUTHORIZED / MERGED
mode: OFFLINE_RECORDED_WORKLOAD_ONLY
authority promotion: FORBIDDEN
authoritative writes: FORBIDDEN
side effects: FORBIDDEN
C5 / production / ecosystem wiring: NOT AUTHORIZED
```

C4 adds an evidence layer, not a third storage profile, command path or deployment runtime.

## Dataset

```text
dataset_id:      native-kernel/c4-offline-shadow-v1
protocol:        nk-shadow-workload/1
sha256:          15fb81d8858dcc4e349ffe87c257b25450db026473614582faa7817f90249da3
cases:           15
assertion scope: 45 / 45 C3-supported assertions
approval:        ADR-0020 / Issue #61 / APPROVED
```

The dataset contains synthetic recorded repository observations, not captured production traffic.

## Evaluation pipeline

```text
approved dataset bytes
+ exact C3 prerequisite report
→ dataset/protocol/digest validation
→ authority-boundary validation
→ declared-field comparison
→ allowed-difference separation
→ semantic/critical divergence metrics
→ one bounded Receipt per case
→ complete 72-ID C4 report
→ strict repository validator
```

## Assertion boundary

```text
SUPPORTED / C4 evaluated: 45
PARTIAL:                   10
UNSUPPORTED:               17
FAILED:                     0
TOTAL:                     72
support_state:             PARTIAL
```

No assertion outside the existing C3-supported set can receive C4. All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

## Thresholds

```text
critical divergences max:      0
semantic divergence rate max:  0.0
missing Receipts max:          0
C3-supported coverage min:     1.0
latency ratio max:              2.0 (informational operational field)
```

Threshold changes require a new dataset/version and evidence cycle.

## Shadow Receipt proof boundary

Each `nk-shadow-receipt/1` records the case ID, dataset/comparison digests, assertion scope, matched/divergence result, `OBSERVE_ONLY` decision, no authority promotion, no authoritative write, no side effects and explicit non-proofs for truth, authenticity, deletion and production safety.

A Receipt proves only that the declared recorded case was compared by this evaluator.

## Publication lineage

```text
PR #62 final head: b7786c088ef2cfd203c02625a5e0c40129cbf148
PR #62 merge/main: 07bf1cc955307783f8eaa3becbaa924087b8b325
```

## Exact final-PR-head evidence

```text
C4 run:        31189149796 — PASS
P5/C3 run:     31189149627 — PASS
P4 run:        31189149839 — PASS
P1 run:        31189149436 — PASS
Fixtures:      31189149449 — PASS
AI context:    31189149274 — PASS
```

Final-head artifact digests:

```text
py3.11/pg16 sha256:04fe9a56055a06f3814d8bf3ac30e40ee65af51bb79f0a4609d042871b34a6a8
py3.11/pg18 sha256:c78bc9486600e77054396d01b2bc8b6a076c3d8df153d5a40596b5332cc10da2
py3.12/pg16 sha256:9f04bbed641e9c3f68db3cc88260ec0a476cd7644279f5b89037a8929b606528
py3.12/pg18 sha256:43fd58e2d966c1e77ab8cbf12a55b44fb4b9a95f25d682d73a7023255a8e2a5b
```

## Exact implementation-main evidence

```text
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

Each artifact contains P4, P5, C3 and C4 reports. A main-bound archive was downloaded and inspected:

```text
15 / 15 matched cases
15 Shadow Receipts
45 / 45 assertion coverage
0 semantic divergences
0 critical divergences
0 missing Receipts
30 allowed operational differences
72 assertion results
status PASS / support_state PARTIAL
```

Its first Receipt explicitly recorded `authority_promoted: false`, `authoritative_write_performed: false` and `side_effects_executed: false`.

Artifacts are retained until 2026-09-06.

## Defect evidence

1. A one-file base64 bootstrap payload was truncated. The failing run was not used as evidence.
2. Delivery was replaced by six individually hashed parts plus a final archive checksum; bootstrap run `31187117717` passed.
3. The first genuine matrix exposed an environment-isolation defect in a test. The test was corrected without weakening evaluator or validator requirements.
4. Temporary bootstrap files and workflow were removed before review.
5. A stale root package marker still claimed P3 and was corrected to `0.6.0-c4`.

## Non-claims

```text
C4 PASS
≠ live production shadowing
≠ authority promotion
≠ candidate approval
≠ exhaustive equivalence proof
≠ operational equivalence
≠ all 72 assertions supported
≠ truth or external authenticity
≠ physical or cryptographic deletion
≠ C5
≠ production readiness
```

## Remaining publication gate

Merge the documentation-only checkpoint, repeat bounded evidence on the resulting `main`, synchronize Notion and close Issue #61. C5, live shadowing, production and ecosystem integration remain separately gated.
