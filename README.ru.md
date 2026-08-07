# 🧬 Velantrim Native Kernel

### Технологически нейтральные контракты семантической памяти, заменяемые профили и ограниченные доказательства

> **Текущее состояние:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`

Native Kernel исследует сохранение semantic identity, Event history, deterministic replay и bounded evidence при смене баз данных, языков, моделей и вычислительных субстратов.

```text
Architecture Canon
→ abstract contracts
→ replaceable PostgreSQL / SQLite profiles
→ C2 profile evidence
→ C3 cross-profile comparison
→ C4 offline shadow evaluation
→ C5 bounded synthetic operational rehearsal
```

PostgreSQL, SQLite, Python, JSON, CI, LLM, vectors и hardware — заменяемые инструменты, а не Canon.

## Текущая карта evidence

```text
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
Offline C4 scope:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
C5 assertion map:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
support_state: PARTIAL
```

```text
kernel_runtime_conformance: C4
operational_validation: C5_BOUNDED_REHEARSAL
```

## C5 bounded operational rehearsal

```text
plan: native-kernel/c5-bounded-rehearsal-v1
protocol: nk-operational-plan/1
sha256: 4ed680ff4e83ac9d1aca6c1ab8a435ecb19af4a5badf1be8202bc842f964b098
scenarios: 18
deployment: CI_EPHEMERAL_SYNTHETIC
```

Rehearsal использует реальные PostgreSQL/SQLite APIs для authority denial, writer fencing, idempotency, rollback, replay, quarantined restore, corruption detection, incident timeline, privacy canary redaction и bounded load.

Первое полное repository evidence:

```text
head 260922de9f2a62b28697db3237b5ebfc7558edec
run 31202900408 — PASS
Python 3.11/3.12 × PostgreSQL 16/18 × SQLite 3.45.1
```

```text
18/18 scenarios PASS
18 Receipts
0 canary leaks
0 recovery failures
0 uncontained incidents
p95 append 11.484 ms
total rehearsal 975.163 ms
```

## Точная граница

```text
C5 bounded rehearsal
≠ production readiness
≠ live user traffic
≠ cloud IAM / multi-region HA
≠ compliance certification
≠ physical backup или deletion
≠ operational equivalence
≠ authority promotion
≠ ecosystem wiring
```

## Читать дальше

- [`STATUS.md`](STATUS.md)
- [`AGENTS.md`](AGENTS.md)
- [`docs/ai/C5_IMPLEMENTATION_RECORD.md`](docs/ai/C5_IMPLEMENTATION_RECORD.md)
- [`docs/adr/0021-authorize-c5-bounded-operational-rehearsal.md`](docs/adr/0021-authorize-c5-bounded-operational-rehearsal.md)
- [`contracts/operational-plan-v1.json`](contracts/operational-plan-v1.json)
