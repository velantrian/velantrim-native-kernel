# 🪞 C4 Offline Shadow Evaluation Implementation Record

**Date:** 2026-08-07  
**Issue / PR / ADR:** #61 / #62 / ADR-0020  
**Base public main:** `b10be105743355a04e58611639a9d28faf7ea514`  
**Status:** `C4 PARTIAL / OFFLINE RECORDED-WORKLOAD SHADOW / NOT PRODUCTION-READY`

## Authorization

The operator authorized C4 only as an offline, authority-free evaluation over an explicitly approved recorded workload.

```text
C4: AUTHORIZED
mode: OFFLINE_RECORDED_WORKLOAD_ONLY
authority promotion: FORBIDDEN
authoritative writes: FORBIDDEN
side effects: FORBIDDEN
C5 / production / ecosystem wiring: NOT AUTHORIZED
```

## Scope

C4 adds:

- immutable approved workload bytes with exact SHA-256 binding;
- `nk-shadow-workload/1` dataset protocol;
- `nk-shadow-report/1` evaluation report;
- `nk-shadow-receipt/1` per-case bounded evidence;
- an authority-free evaluator;
- semantic, behavioural, integrity and proof-boundary comparison;
- explicit allowed operational differences;
- fail-closed divergence and threshold handling;
- complete 72-ID output with C4 limited to 45 C3-supported assertions;
- repository CI and retained four-report artifacts.

C4 does not add a third storage profile, a command path or a deployment runtime.

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

Threshold changes require a new dataset/version and evidence cycle; they must not silently rewrite the approved dataset.

## Shadow Receipt proof boundary

Each `nk-shadow-receipt/1` records:

- case ID;
- dataset digest;
- comparison digest;
- matched/divergence result;
- assertion scope;
- `OBSERVE_ONLY` decision;
- no authority promotion;
- no authoritative write;
- no side effects;
- explicit non-proofs for truth, authenticity, deletion and production safety.

A Receipt proves only that the declared recorded case was compared by this evaluator.

## First repository evidence

```text
Evidence head: 97abce685a68e24aec9afab451c009df5783b96b
C4 run:       31187532364 — PASS
P5/C3 run:    31187532391 — PASS
P4 run:       31187532618 — PASS
P1 run:       31187532346 — PASS
Fixtures:     31187532580 — PASS
```

Matrix:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Artifact digests:

```text
py3.11/pg16 sha256:59cf39e6cbd3e8c95157676cc3fd838687d5911676b227681efd6c83a7f36e90
py3.11/pg18 sha256:9d4f828095285e479e1a95b87523fbaa800068f82a75cbbefb5f2d736e952032
py3.12/pg16 sha256:f85e29688a0176c168067fb8ed6f889550342c6faffcb4dc7d391715ea5364d4
py3.12/pg18 sha256:6892bc2ab7232c96124d4d207aacf06385f8b2ff6a3ea91097d1db6c2e834328
```

One archive was downloaded and inspected. It contained P4, P5, C3 and C4 reports. The C4 result was:

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

## Defect evidence

1. A one-file base64 bootstrap payload was truncated. The failing run was not used as evidence.
2. The payload was replaced by six individually hashed parts plus a final archive checksum; bootstrap run `31187117717` passed.
3. The first genuine matrix exposed an environment-isolation defect in a test. The test was corrected without weakening evaluator or validator requirements.
4. Temporary bootstrap files and workflow were removed before the executable PR head.

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

- repeat C4 and prerequisite workflows on the exact final documentation head;
- validate AI context and public links;
- inspect a final-head four-report artifact;
- review and merge PR #62;
- reproduce evidence on `main`;
- publish a docs-only checkpoint;
- synchronize Notion;
- close Issue #61.

C5, live shadowing, production and ecosystem integration remain separately gated.
