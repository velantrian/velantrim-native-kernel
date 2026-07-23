# 📚 Native Kernel Documentation

**[English](./README.md) · [Русский](./README.ru.md)**

This directory separates project purpose, architecture, conformance, research proposals, integration boundaries, and durable decisions.

> [!IMPORTANT]
> Read status labels carefully. A documented or accepted architecture decision is not automatically implemented runtime behaviour.

## Start here

| Document | Purpose | Status |
|---|---|---|
| [`FOUNDATIONAL_INTENT.md`](./FOUNDATIONAL_INTENT.md) | Why Native Kernel exists as a separate system | architectural intent |
| [`LONG_HORIZON_VISION.md`](./LONG_HORIZON_VISION.md) | Architecture Canon, contracts, profiles, and future substrates | research vision |
| [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md) | How an implementation can demonstrate compatibility | proposed documentation contract |
| [`DECISION_PROCESS.md`](./DECISION_PROCESS.md) | How decisions, evidence, implementation, AI input, and operator approval remain separate | governance process |
| [`adr/README.md`](./adr/README.md) | Architecture Decision Record index | active governance |
| [`INTEGRATION_BOUNDARIES.md`](./INTEGRATION_BOUNDARIES.md) | Native Kernel, Titan, and Crystal boundaries | documented boundary |
| [`BENCHMARKS.md`](./BENCHMARKS.md) | Benchmark methodology and evidence rules | research policy |

## Reading order

```text
1. FOUNDATIONAL_INTENT
        ↓
2. LONG_HORIZON_VISION
        ↓
3. ARCHITECTURE.md in repository root
        ↓
4. CONFORMANCE_MODEL
        ↓
5. DECISION_PROCESS + ADRs
        ↓
6. STATUS.md and ROADMAP.md
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

## For AI reviewers

Before proposing a change:

1. verify the repository state;
2. identify the architectural layer;
3. preserve Native Kernel / Titan / Crystal boundaries;
4. separate proposal, evidence, implementation, and approval;
5. create or update an ADR for durable architectural decisions;
6. do not expand Issue #1 with redesign.
