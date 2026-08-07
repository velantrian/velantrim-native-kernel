# 📚 Native Kernel Documentation

**[English](./README.md) · [Русский](./README.ru.md)**

This directory separates purpose, architecture, contracts, implementation profiles, evidence, research, integration boundaries and continuity records.

> [!IMPORTANT]
> Current branch maturity is `RESEARCH / P5 PARTIAL CROSS-PROFILE CONFORMANCE / NOT PRODUCTION-READY`. Acceptance, implementation, C2/C3 evidence and operational readiness remain separate.

## Start here

| Document | Purpose | Current boundary |
|---|---|---|
| [`../AGENTS.md`](../AGENTS.md) | Mandatory repository guidance | P5/C3 and non-claim rules |
| [`../STATUS.md`](../STATUS.md) | Authoritative current implementation/evidence state | C3 45/10/17; support partial |
| [`ai/README.md`](./ai/README.md) | AI/human continuity map | active context pack |
| [`ai/P5_IMPLEMENTATION_RECORD.md`](./ai/P5_IMPLEMENTATION_RECORD.md) | SQLite/C3 checks, runs, artifacts and limitations | previous-head C2/C3 evidence |
| [`ai/P4_IMPLEMENTATION_RECORD.md`](./ai/P4_IMPLEMENTATION_RECORD.md) | PostgreSQL C2 foundation | historical prerequisite |
| [`FOUNDATIONAL_INTENT.md`](./FOUNDATIONAL_INTENT.md) · [Русский](./FOUNDATIONAL_INTENT.ru.md) | Why Native Kernel exists | architectural intent |
| [`contracts/NORMATIVE_CONTRACTS_V1.md`](./contracts/NORMATIVE_CONTRACTS_V1.md) · [Русский](./contracts/NORMATIVE_CONTRACTS_V1.ru.md) | Exact v1 contracts | accepted; profile support partial |
| [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md) | Assertion states and C0–C5 model | P5 C3 implemented partially |
| [`STORAGE_AND_EXECUTION_PROFILES.md`](./STORAGE_AND_EXECUTION_PROFILES.md) · [Русский](./STORAGE_AND_EXECUTION_PROFILES.ru.md) | PostgreSQL/SQLite roles | both implemented; operational envelopes differ |
| [`rfc/0002-postgresql-reference-profile-v0.md`](./rfc/0002-postgresql-reference-profile-v0.md) | Clean profile lifecycle | P1–P5 |
| [`adr/0019-authorize-p5-sqlite-and-c3-equivalence.md`](./adr/0019-authorize-p5-sqlite-and-c3-equivalence.md) | P5/C3 decision | accepted/approved |
| [`adr/README.md`](./adr/README.md) | Durable decision index | ADR-0019 current |
| [`VELANTRIM_ECOSYSTEM.md`](./VELANTRIM_ECOSYSTEM.md) | Project roles | navigation/boundary map |
| [`INTEGRATION_BOUNDARIES.md`](./INTEGRATION_BOUNDARIES.md) | Cross-project technical boundaries | no active runtime inheritance |
| [`DECISION_PROCESS.md`](./DECISION_PROCESS.md) | Decision/evidence/approval separation | governance process |

## Reading order

```text
AGENTS + STATUS
→ AI context pack + P5 implementation record
→ foundational intent/contracts
→ Architecture Canon
→ ADR-0019 + RFC-0002
→ PostgreSQL and SQLite source/tests/manifests/workflows
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
≠ Operational Equivalence
≠ Production Evidence
```

Current maps:

```text
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
support_state:     PARTIAL
```

```text
C2 ≠ C3
C3 ≠ all 72 supported
C3 semantic equivalence ≠ operational equivalence
C3 ≠ truth/authenticity/physical deletion/production
```

## Executable evidence layers

### Fixture integrity

The standard-library reader validates registry/schema/fixture consistency. Fixture PASS alone is not profile runtime conformance.

### Single-profile C2

PostgreSQL and SQLite adapters each emit a complete `nk-evidence-report/1` with all 72 IDs and guarded `41/13/18/0` map.

### Cross-profile C3

The dedicated comparator emits `nk-equivalence-report/1` after independent PostgreSQL and SQLite execution, normalized outcome comparison and exact authoritative-history import.

Initial P5 evidence:

```text
head d43a6ed28232e9fc8b62f84d9025386fb8bce6f7
run 31181341275 — PASS
Python 3.11/3.12 × PostgreSQL 16/18 × SQLite 3.45.1 — PASS
4 artifacts × 3 JSON reports
```

C2/C3 is credible only with externally visible exact run/head/artifact evidence.

## Technology neutrality

```text
meaning and invariants first
→ abstract contracts second
→ independent replaceable profiles third
→ comparison evidence scoped to exact assertions
```

PostgreSQL, SQLite, Python, graphs, vectors, LLMs and hardware are instruments, not Canon.

## Current missing areas

- exhaustive cross-profile equivalence proof;
- operational equivalence;
- complete conflict subsystem;
- physical/cryptographic deletion execution;
- restore-before-visibility enforcement;
- cross-project authority adapter;
- C4/C5 and production operation;
- historical `v0.1.2.1` recovery.

## For AI reviewers

1. verify exact SHA and whether the claim concerns `main` or an open PR;
2. trace C2/C3 claims from assertion ID to result, check IDs and artifact;
3. preserve `support_state: PARTIAL` and exact counts;
4. preserve semantic-versus-operational equivalence;
5. preserve Issue #1, Issue #18 and ecosystem boundaries;
6. update GitHub and Notion continuity records for material changes;
7. do not begin C4/C5/production/deletion/integration without separate authorization.
