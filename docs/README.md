# 📚 Native Kernel Documentation

**[English](./README.md) · [Русский](./README.ru.md)**

This directory separates purpose, architecture, contracts, implementation profiles, bounded evidence, research, integration boundaries and continuity records.

> [!IMPORTANT]
> Current branch maturity is `RESEARCH / C4 PARTIAL OFFLINE SHADOW EVALUATION / NOT PRODUCTION-READY`. Acceptance, implementation, C2/C3/C4 evidence, authority and operational readiness remain separate.

## Start here

| Document | Purpose | Current boundary |
|---|---|---|
| [`../AGENTS.md`](../AGENTS.md) | Mandatory repository guidance | C4 offline/no-promotion rules |
| [`../STATUS.md`](../STATUS.md) | Authoritative current implementation/evidence state | C4 45/10/17; support partial |
| [`ai/README.md`](./ai/README.md) | AI/human continuity map | active context pack |
| [`ai/C4_IMPLEMENTATION_RECORD.md`](./ai/C4_IMPLEMENTATION_RECORD.md) | Dataset, evaluator, Shadow Receipts, runs, artifacts and limits | exact C4 evidence route |
| [`ai/P5_IMPLEMENTATION_RECORD.md`](./ai/P5_IMPLEMENTATION_RECORD.md) | SQLite/C3 prerequisite evidence | merged prerequisite |
| [`FOUNDATIONAL_INTENT.md`](./FOUNDATIONAL_INTENT.md) · [Русский](./FOUNDATIONAL_INTENT.ru.md) | Why Native Kernel exists | architectural intent |
| [`contracts/NORMATIVE_CONTRACTS_V1.md`](./contracts/NORMATIVE_CONTRACTS_V1.md) · [Русский](./contracts/NORMATIVE_CONTRACTS_V1.ru.md) | Exact v1 contracts | accepted; profile support partial |
| [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md) | Assertion states and C0–C5 model | C4 implemented partially |
| [`STORAGE_AND_EXECUTION_PROFILES.md`](./STORAGE_AND_EXECUTION_PROFILES.md) · [Русский](./STORAGE_AND_EXECUTION_PROFILES.ru.md) | PostgreSQL/SQLite roles | profiles differ operationally |
| [`adr/0020-authorize-c4-offline-shadow-evaluation.md`](./adr/0020-authorize-c4-offline-shadow-evaluation.md) | C4 decision | accepted/approved; offline only |
| [`implementation/c4-offline-shadow-evaluation.md`](./implementation/c4-offline-shadow-evaluation.md) | C4 implementation details | no authority or side effects |
| [`adr/README.md`](./adr/README.md) | Durable decision index | ADR-0020 current |
| [`VELANTRIM_ECOSYSTEM.md`](./VELANTRIM_ECOSYSTEM.md) | Project roles | navigation/boundary map |
| [`INTEGRATION_BOUNDARIES.md`](./INTEGRATION_BOUNDARIES.md) | Cross-project technical boundaries | no active runtime inheritance |

## Reading order

```text
AGENTS + STATUS
→ AI context pack + C4 implementation record
→ foundational intent/contracts
→ Architecture Canon + conformance model
→ ADR-0020 + approved dataset
→ evaluator/validators/tests/workflow
→ exact run/jobs/artifacts
```

## Central distinction

```text
Architecture Canon
≠ Abstract Contract
≠ Accepted Decision
≠ Implementation Profile
≠ Evidence Layer
≠ Assertion Result
≠ Authority Promotion
≠ Production Evidence
```

Current maps:

```text
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
Offline C4 scope:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
support_state:     PARTIAL
```

```text
C2 ≠ C3 ≠ C4
C4 offline shadow ≠ live shadowing
C4 observation ≠ authority promotion
C4 ≠ all 72 supported
C4 ≠ operational equivalence / truth / deletion / C5 / production
```

## Executable evidence layers

### Fixture integrity

The standard-library reader validates registry/schema/fixture consistency. Fixture PASS alone is not profile runtime conformance.

### Single-profile C2

PostgreSQL and SQLite adapters each emit complete `nk-evidence-report/1` reports with all 72 IDs and guarded `41/13/18/0` maps.

### Cross-profile C3

The dedicated comparator emits `nk-equivalence-report/1` after independent PostgreSQL and SQLite execution, normalized outcome comparison and exact authoritative-history import.

### Offline C4

The authority-free evaluator consumes an exact validated C3 report and the approved immutable `nk-shadow-workload/1` dataset. It emits `nk-shadow-report/1` plus one bounded `nk-shadow-receipt/1` per case.

```text
dataset: native-kernel/c4-offline-shadow-v1
sha256:  15fb81d8858dcc4e349ffe87c257b25450db026473614582faa7817f90249da3
cases:   15
scope:   45 / 45 C3-supported assertions
```

First C4 repository evidence:

```text
head 97abce685a68e24aec9afab451c009df5783b96b
run 31187532364 — PASS
Python 3.11/3.12 × PostgreSQL 16/18 × SQLite 3.45.1 — PASS
4 artifacts × 4 JSON reports
15/15 matched cases · 15 Receipts · 0 semantic/critical divergences
```

C2/C3/C4 is credible only with externally visible exact run/head/artifact evidence.

## Technology neutrality

```text
meaning and invariants first
→ abstract contracts second
→ independent replaceable profiles third
→ bounded evidence layers over declared observations
```

PostgreSQL, SQLite, Python, JSON, graphs, vectors, LLMs and hardware are instruments, not Canon.

## Current missing areas

- live traffic capture or live production shadowing;
- authority promotion or candidate approval;
- exhaustive cross-profile/state-space equivalence;
- operational equivalence;
- complete conflict subsystem;
- physical/cryptographic deletion execution;
- restore-before-visibility enforcement;
- cross-project authority adapter;
- C5 and production operation;
- historical `v0.1.2.1` recovery.

## For AI reviewers

1. verify exact SHA and whether the claim concerns `main` or an open PR;
2. trace C4 from ADR/dataset ID/digest to C3 prerequisite, case results, Receipts and retained artifact;
3. preserve `support_state: PARTIAL` and exact counts;
4. preserve offline-versus-live and observation-versus-authority boundaries;
5. preserve Issue #1, Issue #18 and ecosystem boundaries;
6. update GitHub and Notion continuity records for material changes;
7. do not begin C5/live/production/deletion/integration without separate authorization.
