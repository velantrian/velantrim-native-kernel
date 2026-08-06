# 📚 Native Kernel Documentation

**[English](./README.md) · [Русский](./README.ru.md)**

This directory separates project purpose, architecture, conformance, research proposals, integration boundaries, durable decisions, and AI/human continuity records.

> [!IMPORTANT]
> Read status labels carefully. A documented or accepted architecture decision is not automatically implemented runtime behaviour.

## Start here

| Document | Purpose | Status |
|---|---|---|
| [`../AGENTS.md`](../AGENTS.md) | Mandatory first-read rules for AI agents, auditors and reviewers | active repository guidance |
| [`ai/README.md`](./ai/README.md) | AI context-pack manifest: current state, component map, risks, audit method, work log and GitHub↔Notion protocol | active continuity layer |
| [`FOUNDATIONAL_INTENT.md`](./FOUNDATIONAL_INTENT.md) · [Русский](./FOUNDATIONAL_INTENT.ru.md) | Deep explanation of why Native Kernel exists as a separate system, what problem it studies, and what success would mean | architectural intent |
| [`FOUNDATIONAL_CONTRACT_SKELETON.md`](./FOUNDATIONAL_CONTRACT_SKELETON.md) · [Русский](./FOUNDATIONAL_CONTRACT_SKELETON.ru.md) | Six-family skeleton for semantic roles, identity, events, authority, conflict/unknowns, and semantic equivalence | accepted abstract-contract map; not implemented |
| [`contracts/NORMATIVE_CONTRACTS_V1.md`](./contracts/NORMATIVE_CONTRACTS_V1.md) · [Русский](./contracts/NORMATIVE_CONTRACTS_V1.ru.md) | Proposed exact v1 contracts for identity, single-writer append/replay, deletion/restriction and executable fixtures | proposed; fixture tooling locally tested; Kernel runtime not implemented |
| [`LONG_HORIZON_VISION.md`](./LONG_HORIZON_VISION.md) | Architecture Canon, contracts, profiles, and future substrates | research vision |
| [`STORAGE_AND_EXECUTION_PROFILES.md`](./STORAGE_AND_EXECUTION_PROFILES.md) · [Русский](./STORAGE_AND_EXECUTION_PROFILES.ru.md) | PostgreSQL as the primary full contemporary profile, SQLite as an optional embedded profile, offline local-model operation, profile selection, and migration boundaries | accepted implementation-profile direction; not implemented |
| [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md) | How an implementation can demonstrate compatibility | proposed documentation contract; fixture-integrity tooling exists |
| [`DECISION_PROCESS.md`](./DECISION_PROCESS.md) | How decisions, evidence, implementation, AI input, and operator approval remain separate | governance process |
| [`adr/README.md`](./adr/README.md) | Architecture Decision Record index | active governance |
| [`VELANTRIM_ECOSYSTEM.md`](./VELANTRIM_ECOSYSTEM.md) | Roles and links for Native Kernel, Mentaury Soul, Titan and Crystal | navigation/boundary map |
| [`INTEGRATION_BOUNDARIES.md`](./INTEGRATION_BOUNDARIES.md) | Technical boundaries between Native Kernel, Titan, Mentaury and Crystal | documented boundary |
| [`BENCHMARKS.md`](./BENCHMARKS.md) | Benchmark methodology and evidence rules | research policy |
| [`research/BIO_INSPIRED_COMPUTATION_AND_KITARA.md`](./research/BIO_INSPIRED_COMPUTATION_AND_KITARA.md) · [Русский](./research/BIO_INSPIRED_COMPUTATION_AND_KITARA.ru.md) | Optional bio-inspired and Kitara research boundary | proposed / experimental / not implemented |
| [`research/PHYSARUM_ROUTING_EXPERIMENT.md`](./research/PHYSARUM_ROUTING_EXPERIMENT.md) · [Русский](./research/PHYSARUM_ROUTING_EXPERIMENT.ru.md) | Bounded adaptive-flow routing experiment | proposed / not implemented |

## Reading order

```text
1. AGENTS.md + STATUS.md
        ↓
2. docs/ai context pack
        ↓
3. FOUNDATIONAL_INTENT
        ↓
4. FOUNDATIONAL_CONTRACT_SKELETON
        ↓
5. NORMATIVE_CONTRACTS_V1 + ADR-0011…0014
        ↓
6. LONG_HORIZON_VISION
        ↓
7. STORAGE_AND_EXECUTION_PROFILES
        ↓
8. ARCHITECTURE.md in repository root
        ↓
9. CONFORMANCE_MODEL + contracts/ fixture pack
        ↓
10. DECISION_PROCESS + ADRs
        ↓
11. ROADMAP + optional research notes
```

## The central distinction

```text
Architecture Canon
≠ Abstract Contract
≠ Proposed exact contract
≠ Fixture-integrity tooling
≠ Implementation Profile
≠ Implemented Kernel Runtime
≠ Production Evidence
```

Modern tools are used as laboratories. They do not automatically define permanent architecture.

## The deeper rationale

Native Kernel exists because contemporary memory systems often allow the current database, graph engine, vector index, model API, runtime, or processor assumptions to define what memory means.

This project reverses that order:

```text
meaning and invariants first
        ↓
abstract contracts second
        ↓
replaceable technology profiles third
```

The deeper explanation is maintained in:

- [`FOUNDATIONAL_INTENT.md`](./FOUNDATIONAL_INTENT.md)
- [`FOUNDATIONAL_INTENT.ru.md`](./FOUNDATIONAL_INTENT.ru.md)
- [`FOUNDATIONAL_CONTRACT_SKELETON.md`](./FOUNDATIONAL_CONTRACT_SKELETON.md)
- [`FOUNDATIONAL_CONTRACT_SKELETON.ru.md`](./FOUNDATIONAL_CONTRACT_SKELETON.ru.md)
- [`contracts/NORMATIVE_CONTRACTS_V1.md`](./contracts/NORMATIVE_CONTRACTS_V1.md)
- [`contracts/NORMATIVE_CONTRACTS_V1.ru.md`](./contracts/NORMATIVE_CONTRACTS_V1.ru.md)

## Executable fixture boundary

The repository may include schemas, golden/invalid vectors and a standard-library fixture validator before any Kernel runtime exists.

```text
fixture pack PASS
≠ Kernel runtime implemented
≠ C2 repository conformance
≠ C3 cross-profile equivalence
≠ production deletion guarantee
```

Use [`../tools/conformance/README.md`](../tools/conformance/README.md) and inspect `contracts/registry.json`, `contracts/schema-bundle.json` and `contracts/fixture-pack.json`.

## Optional experimental research

Some source materials contain useful ideas that are not part of Native Kernel Canon. They are preserved as explicitly bounded research notes.

The bio-inspired track currently records:

```text
peripheral event processing
adaptive gain
procedural / motor memory
sensorimotor loops
distributed network adaptation
Physarum-like routing
```

These mechanisms may be tested as replaceable profiles. They must not determine truth, bypass policy, become runtime claims, or expand Issue #1.

## For AI reviewers

Start with [`../AGENTS.md`](../AGENTS.md) and [`ai/README.md`](./ai/README.md).
Before proposing a change:

1. verify the exact repository/PR SHA;
2. check `STATUS.md` and the last verified current-state checkpoint;
3. identify the architectural layer;
4. preserve Native Kernel / Titan / Mentaury / Crystal boundaries;
5. separate proposal, acceptance, evidence, implementation and approval;
6. create or update an ADR for durable decisions;
7. do not expand Issue #1 with redesign;
8. do not turn current technology, biological metaphor or adaptive routing into permanent Canon or epistemic authority;
9. update the AI context pack and GitHub↔Notion synchronization record when material facts change.
