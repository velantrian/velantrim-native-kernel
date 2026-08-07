# 📚 Native Kernel Documentation

**[English](./README.md) · [Русский](./README.ru.md)**

This directory separates purpose, architecture, contracts, implementation profiles, evidence, research, integration boundaries and continuity records.

> [!IMPORTANT]
> Current repository maturity is `RESEARCH / P4 PARTIAL ASSERTION CONFORMANCE / NOT PRODUCTION-READY`. Acceptance, implementation and evidence remain separate.

## Start here

| Document | Purpose | Current boundary |
|---|---|---|
| [`../AGENTS.md`](../AGENTS.md) | Mandatory repository guidance | P4/C2 and phase boundaries |
| [`../STATUS.md`](../STATUS.md) | Authoritative current implementation/evidence state | 41 supported / 13 partial / 18 unsupported |
| [`ai/README.md`](./ai/README.md) | AI/human continuity map | active context pack |
| [`ai/P4_IMPLEMENTATION_RECORD.md`](./ai/P4_IMPLEMENTATION_RECORD.md) | Exact P4 checks, runs, artifacts and limitations | previous-head C2 evidence |
| [`FOUNDATIONAL_INTENT.md`](./FOUNDATIONAL_INTENT.md) · [Русский](./FOUNDATIONAL_INTENT.ru.md) | Why Native Kernel exists | architectural intent |
| [`FOUNDATIONAL_CONTRACT_SKELETON.md`](./FOUNDATIONAL_CONTRACT_SKELETON.md) · [Русский](./FOUNDATIONAL_CONTRACT_SKELETON.ru.md) | Contract-family map | accepted abstraction |
| [`contracts/NORMATIVE_CONTRACTS_V1.md`](./contracts/NORMATIVE_CONTRACTS_V1.md) · [Русский](./contracts/NORMATIVE_CONTRACTS_V1.ru.md) | Exact v1 identity/event/deletion/fixture contracts | accepted; profile support partial |
| [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md) | Assertion result states and C0–C5 model | P4 adapter implemented; C3 absent |
| [`rfc/0002-postgresql-reference-profile-v0.md`](./rfc/0002-postgresql-reference-profile-v0.md) | Clean PostgreSQL profile lifecycle | P1–P4 active lineage |
| [`adr/README.md`](./adr/README.md) | Durable decisions | ADR-0018 accepted |
| [`VELANTRIM_ECOSYSTEM.md`](./VELANTRIM_ECOSYSTEM.md) | Project roles | navigation/boundary map |
| [`INTEGRATION_BOUNDARIES.md`](./INTEGRATION_BOUNDARIES.md) | Cross-project technical boundaries | no active runtime inheritance |
| [`DECISION_PROCESS.md`](./DECISION_PROCESS.md) | Decision/evidence/approval separation | governance process |
| [`BENCHMARKS.md`](./BENCHMARKS.md) | Benchmark methodology | research policy |

## Reading order

```text
AGENTS + STATUS
→ AI context pack + P4 implementation record
→ foundational intent/contracts
→ Architecture Canon
→ RFC-0002 + ADR-0015…0018
→ source/tests/manifests/workflows
→ exact run/jobs/artifacts
```

## Central distinction

```text
Architecture Canon
≠ Abstract Contract
≠ Accepted Decision
≠ Implementation Profile
≠ Assertion Result
≠ Evidence Level
≠ Production Evidence
```

Current P4 map:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
support_state: PARTIAL
```

```text
P4 C2 ≠ all 72 supported
P4 C2 ≠ C3
P4 C2 ≠ truth/authenticity
P4 C2 ≠ physical deletion
```

## Executable evidence layers

### Fixture integrity

The standard-library reader validates registry/schema/fixture consistency and deliberately emits all assertions as unsupported. Fixture PASS is not Kernel runtime conformance.

### PostgreSQL P4 adapter

The P4 adapter executes bounded semantic and PostgreSQL checks and emits one `nk-evidence-report/1` result for every registered assertion.

Use [`../tools/conformance/README.md`](../tools/conformance/README.md) for commands and validation boundaries.

Initial C2 evidence:

```text
head 93710131fffdea7d9a586cc05e7f258c07fae707
run 31175767586 — PASS
Python 3.11/3.12 × PostgreSQL 16/18 — PASS
4 JSON artifacts retained
```

C2 is credible only with an externally visible exact run/head/artifact, not a self-generated JSON report alone.

## Technology neutrality

```text
meaning and invariants first
→ abstract contracts second
→ replaceable profiles third
→ evidence scoped to exact assertions
```

PostgreSQL, SQLite, Python, graphs, vectors, LLMs and hardware are instruments, not Canon.

## Current missing areas

- independent SQLite profile and C3;
- complete conflict subsystem;
- physical/cryptographic deletion execution;
- restore-before-visibility enforcement;
- cross-project authority adapter;
- C4/C5 and production operation;
- historical `v0.1.2.1` recovery.

## For AI reviewers

1. verify exact SHA and whether the claim concerns `main` or an open PR;
2. trace each conformance claim from assertion ID to result, check IDs and artifact;
3. preserve `support_state: PARTIAL` and support counts;
4. preserve Issue #1, Issue #18 and ecosystem boundaries;
5. update GitHub and Notion continuity records for material changes;
6. do not begin P5/C3 without separate operator GO.
