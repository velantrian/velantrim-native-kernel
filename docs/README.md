# 📚 Native Kernel Documentation

**[English](./README.md) · [Русский](./README.ru.md)**

> **Current boundary:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`

## Start here

| Document | Purpose |
|---|---|
| [`QUICKSTART.md`](./QUICKSTART.md) | human setup, pinned SQLite and first test commands |
| [`GLOSSARY.md`](./GLOSSARY.md) | compact terminology and required non-equivalences |
| [`../STATUS.md`](../STATUS.md) | current implementation/evidence boundary |
| [`../project-state.json`](../project-state.json) | machine-readable state snapshot |
| [`../AGENTS.md`](../AGENTS.md) | mandatory repository guidance |
| [`ai/README.md`](./ai/README.md) | continuity map |
| [`ai/C5_IMPLEMENTATION_RECORD.md`](./ai/C5_IMPLEMENTATION_RECORD.md) | C5 implementation and preservation evidence |
| [`../evidence/c5/README.md`](../evidence/c5/README.md) | exact retained ZIP archive |
| [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md) | C0–C5 and assertion boundaries |
| [`adr/README.md`](./adr/README.md) | decision index |
| [`research/POST_C5_RESEARCH_BACKLOG.md`](./research/POST_C5_RESEARCH_BACKLOG.md) | proposed post-C5 work only |
| [`INTEGRATION_BOUNDARIES.md`](./INTEGRATION_BOUNDARIES.md) | ecosystem authority boundaries |

## Current map

```text
H historical recovery: OPEN / BLOCKED / independent
C clean implementation: P1–P5 + C4 + C5 / ACTIVE / PARTIAL
R long-horizon research: PROPOSED / BOUNDED

kernel_runtime_conformance: C4
operational_validation: C5_BOUNDED_REHEARSAL
assertions: 45 / 10 / 17 / 0
NK-EPI: 0 / 8 SUPPORTED
production: NOT AUTHORIZED
```

## Reading order

```text
QUICKSTART + GLOSSARY
→ STATUS + project-state
→ AGENTS + AI context
→ C5 implementation/evidence archive
→ contracts + conformance model
→ ADRs
→ source/tests/workflows
→ research only when future direction is relevant
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

PostgreSQL, SQLite, Python, JSON, graphs, vectors, LLMs and hardware are instruments, not Canon.
