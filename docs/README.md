# 📚 Native Kernel Documentation

**[English](./README.md) · [Русский](./README.ru.md)**

This directory separates project purpose, architecture, conformance, research proposals, integration boundaries, and durable decisions.

> [!IMPORTANT]
> Read status labels carefully. A documented or accepted architecture decision is not automatically implemented runtime behaviour.

## Start here

| Document | Purpose | Status |
|---|---|---|
| [`FOUNDATIONAL_INTENT.md`](./FOUNDATIONAL_INTENT.md) · [Русский](./FOUNDATIONAL_INTENT.ru.md) | Deep explanation of why Native Kernel exists as a separate system, what problem it studies, and what success would mean | architectural intent |
| [`LONG_HORIZON_VISION.md`](./LONG_HORIZON_VISION.md) | Architecture Canon, contracts, profiles, and future substrates | research vision |
| [`STORAGE_AND_EXECUTION_PROFILES.md`](./STORAGE_AND_EXECUTION_PROFILES.md) · [Русский](./STORAGE_AND_EXECUTION_PROFILES.ru.md) | PostgreSQL as the primary full contemporary profile, SQLite as an optional embedded profile, offline local-model operation, profile selection, and migration boundaries | accepted implementation-profile direction; not implemented |
| [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md) | How an implementation can demonstrate compatibility | proposed documentation contract |
| [`DECISION_PROCESS.md`](./DECISION_PROCESS.md) | How decisions, evidence, implementation, AI input, and operator approval remain separate | governance process |
| [`adr/README.md`](./adr/README.md) | Architecture Decision Record index | active governance |
| [`INTEGRATION_BOUNDARIES.md`](./INTEGRATION_BOUNDARIES.md) | Native Kernel, Titan, and Crystal boundaries | documented boundary |
| [`BENCHMARKS.md`](./BENCHMARKS.md) | Benchmark methodology and evidence rules | research policy |
| [`research/BIO_INSPIRED_COMPUTATION_AND_KITARA.md`](./research/BIO_INSPIRED_COMPUTATION_AND_KITARA.md) · [Русский](./research/BIO_INSPIRED_COMPUTATION_AND_KITARA.ru.md) | Optional bio-inspired and Kitara research boundary | proposed / experimental / not implemented |
| [`research/PHYSARUM_ROUTING_EXPERIMENT.md`](./research/PHYSARUM_ROUTING_EXPERIMENT.md) · [Русский](./research/PHYSARUM_ROUTING_EXPERIMENT.ru.md) | Bounded adaptive-flow routing experiment | proposed / not implemented |

## Reading order

```text
1. FOUNDATIONAL_INTENT
        ↓
2. LONG_HORIZON_VISION
        ↓
3. STORAGE_AND_EXECUTION_PROFILES
        ↓
4. ARCHITECTURE.md in repository root
        ↓
5. CONFORMANCE_MODEL
        ↓
6. DECISION_PROCESS + ADRs
        ↓
7. STATUS.md and ROADMAP.md
        ↓
8. Optional experimental research notes
```

## The central distinction

```text
Architecture Canon
≠ Abstract Contract
≠ Implementation Profile
≠ Implemented Runtime
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

The deeper explanation, including the transportation-blueprint analogy, success criteria, research method, and explicit non-claims, is maintained in:

- [`FOUNDATIONAL_INTENT.md`](./FOUNDATIONAL_INTENT.md)
- [`FOUNDATIONAL_INTENT.ru.md`](./FOUNDATIONAL_INTENT.ru.md)

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

Before proposing a change:

1. verify the repository state;
2. identify the architectural layer;
3. preserve Native Kernel / Titan / Crystal boundaries;
4. separate proposal, evidence, implementation, and approval;
5. create or update an ADR for durable architectural decisions;
6. do not expand Issue #1 with redesign;
7. do not turn a current technology into permanent Canon merely because it is useful today;
8. do not promote biological metaphor or adaptive routing into epistemic authority.
