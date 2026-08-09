# 📚 Native Kernel Documentation

**[English](./README.md) · [Русский](./README.ru.md)**

> **Current boundary:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`

## Start here

| Document | Role |
|---|---|
| [`../STATUS.md`](../STATUS.md) | authoritative human current state and checkpoint roles |
| [`../project-state.json`](../project-state.json) | authoritative committed machine status (`nk-project-state/2`) |
| [`../ROADMAP.md`](../ROADMAP.md) | active gate sequence and authorization boundaries |
| [`QUICKSTART.md`](./QUICKSTART.md) | setup, safe SQLite floor and first tests |
| [`GLOSSARY.md`](./GLOSSARY.md) | terminology and required non-equivalences |
| [`../AGENTS.md`](../AGENTS.md) | mandatory repository instructions |
| [`ai/CURRENT_STATE.md`](./ai/CURRENT_STATE.md) | compact AI continuity checkpoint |
| [`ai/KNOWN_RISKS.md`](./ai/KNOWN_RISKS.md) | active, mitigated and closed risks |
| [`../evidence/c5/README.md`](../evidence/c5/README.md) | immutable evidence identities and proof boundaries |
| [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md) | C0–C5 and assertion boundaries |
| [`adr/README.md`](./adr/README.md) | accepted and proposed decisions |
| [`research/POST_C5_RESEARCH_BACKLOG.md`](./research/POST_C5_RESEARCH_BACKLOG.md) | proposed research only |
| [`INTEGRATION_BOUNDARIES.md`](./INTEGRATION_BOUNDARIES.md) | ecosystem authority boundaries |

## Current map

```text
H historical recovery: OPEN / BLOCKED / independent
C clean implementation: P1–P5 + C4 + C5 / ACTIVE / PARTIAL
R long-horizon research: PROPOSED / BOUNDED / NO AUTOMATIC PROMOTION

kernel_runtime_conformance: C4
operational_validation: C5_BOUNDED_REHEARSAL
assertions: 45 / 10 / 17 / 0
NK-EPI: 0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
production: NOT AUTHORIZED
```

## Truth roles

```text
CURRENT STATE
  STATUS.md
  project-state.json
  docs/ai/CURRENT_STATE.md

ACTIVE ROADMAP
  ROADMAP.md

ACTIVE RISKS
  docs/ai/KNOWN_RISKS.md

HISTORICAL RECORD
  implementation records
  accepted ADRs
  immutable evidence manifests
  Git history and checkpoint permalinks

PROPOSAL
  proposed ADRs
  research backlog
  unaccepted contract drafts
```

Do not treat historical reports, proposals or old Notion chronology as the authoritative current state.

## Reading order

```text
STATUS + project-state
→ ROADMAP
→ QUICKSTART + GLOSSARY
→ AGENTS + AI context
→ contracts + conformance model
→ implementation and tests
→ evidence manifests and records
→ ADR history
→ research only when future direction is relevant
```

## Current authorized sequence

```text
human-readable truth reconciliation
→ Issues #14–#17 and Notion reconciliation
→ license decision options
→ ADR-0024 decision options
→ NK-SAM and named equivalence profiles
→ Event/history commitment
→ only then reducer-v2 runtime
```

Executable NK-EPI, Temporal, full Admission, operational deletion, full independent implementation and ecosystem integration remain outside the current reconciliation slice.

## Central distinctions

```text
Architecture Canon
≠ Abstract Contract
≠ Accepted Decision
≠ Implementation Profile
≠ Evidence Layer
≠ Assertion Result
≠ Operator Authorization
≠ Production Evidence
```

```text
PostgreSQL + SQLite ≠ full substrate neutrality
C5 PASS ≠ production readiness
Unknown ≠ False
admission ≠ truth
logical ERASED ≠ physical deletion
public repository ≠ open-source license
```

PostgreSQL, SQLite, Python, JSON, graphs, vectors, LLMs and hardware are instruments or profiles, not Canon.