# 📚 Документация Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

> **Текущая граница:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`

## Начать здесь

| Документ | Роль |
|---|---|
| [`../STATUS.md`](../STATUS.md) | authoritative human current state и роли checkpoints |
| [`../project-state.json`](../project-state.json) | authoritative committed machine status (`nk-project-state/2`) |
| [`../ROADMAP.md`](../ROADMAP.md) | active gate sequence и границы authorization |
| [`QUICKSTART.ru.md`](./QUICKSTART.ru.md) | setup, безопасный SQLite floor и первые tests |
| [`GLOSSARY.ru.md`](./GLOSSARY.ru.md) | terminology и обязательные non-equivalences |
| [`../AGENTS.md`](../AGENTS.md) | обязательные инструкции репозитория |
| [`ai/CURRENT_STATE.md`](./ai/CURRENT_STATE.md) | компактный AI continuity checkpoint |
| [`ai/KNOWN_RISKS.md`](./ai/KNOWN_RISKS.md) | active, mitigated и closed risks |
| [`../evidence/c5/README.md`](../evidence/c5/README.md) | неизменяемые evidence identities и proof boundaries |
| [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md) | C0–C5 и границы assertions |
| [`adr/README.md`](./adr/README.md) | accepted и proposed decisions |
| [`research/POST_C5_RESEARCH_BACKLOG.md`](./research/POST_C5_RESEARCH_BACKLOG.md) | только proposed research |
| [`INTEGRATION_BOUNDARIES.md`](./INTEGRATION_BOUNDARIES.md) | границы ecosystem authority |

## Текущая карта

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

## Роли правды

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
  Git history и checkpoint permalinks

PROPOSAL
  proposed ADRs
  research backlog
  unaccepted contract drafts
```

Historical reports, proposals и старая Notion chronology не являются authoritative current state.

## Порядок чтения

```text
STATUS + project-state
→ ROADMAP
→ QUICKSTART + GLOSSARY
→ AGENTS + AI context
→ contracts + conformance model
→ implementation и tests
→ evidence manifests и records
→ ADR history
→ research только когда важно будущее направление
```

## Текущая разрешённая последовательность

```text
human-readable truth reconciliation
→ reconciliation Issues #14–#17 и Notion
→ license decision options
→ ADR-0024 decision options
→ NK-SAM и именованные equivalence profiles
→ Event/history commitment
→ только затем reducer-v2 runtime
```

Executable NK-EPI, Temporal, полный Admission, operational deletion, полная independent implementation и ecosystem integration остаются за пределами текущего reconciliation slice.

## Центральные различия

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

PostgreSQL, SQLite, Python, JSON, graphs, vectors, LLM и hardware — инструменты или profiles, а не Canon.