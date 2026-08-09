# 🧬 Velantrim Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

### Technology-neutral semantic memory architecture, versioned contracts and bounded evidence

> **Current state:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`

Velantrim Native Kernel studies how different implementations and future compute substrates can preserve declared semantic meaning, identity, provenance, history, uncertainty and proof boundaries without silently changing them.

It is **not** an operating-system kernel, database product, LLM memory plugin, vector store or Python framework definition.

```text
same declared meaning
        ↓
different physical mechanisms
        ↓
named observable equivalence
```

## Architecture boundary

```text
Architecture Canon
→ Versioned Abstract Contracts
→ Replaceable Implementation Profiles
→ Fixtures and Tests
→ Evidence
→ Status and Maturity
```

The Canon defines durable semantic requirements. Python, JSON, SHA-256, PostgreSQL, SQLite, UTF-8, LLMs, vectors, conventional binary hardware and CI are replaceable profiles or instruments, not permanent Canon.

Current Python, PostgreSQL and SQLite code is a bounded reference implementation. It is not the final definition of Native Kernel.

## Current state

```text
clean_runtime_support:       PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false

assertion map: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:        0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
```

```text
P1–P5: merged
C4:     merged / partial / offline shadow evidence
C5:     merged / partial / bounded synthetic operational rehearsal
```

C5 does not promote semantic assertions and does not authorize production.

## Checkpoint model

Machine-readable truth is recorded in [`project-state.json`](project-state.json) under `nk-project-state/2`.

| Role | Checkpoint |
|---|---|
| Machine truth reconciliation merge | `d9eee591de308a689ace940c2efe58c9e8a137f2` |
| Runtime checkpoint | `675aa4b398a2fc0181dc71d38904a2d33a09f5f8` |
| Runtime integrity checkpoint | `a1cdc6d8f36d67f40f065641809bc6da463c10a4` |
| Evidence-producing checkpoint | `296981ae84ad5bdab5dabbec9b7b9ebb43af63d7` |
| Notion synchronized through | `626f34e6328b455258f2dd5fcf2145ec4db64a60` |

Live `main` is resolved from GitHub or the checked-out Git ref. A committed manifest records verified checkpoints and their expected relationship to HEAD; it does not attempt to contain its own commit SHA.

## Current evidence

Two immutable C5 evidence identities are repository-resident:

```text
evidence/c5/2026-08-07/manifest.json
evidence/c5/2026-08-08-adr0023/manifest.json
```

ADR-0023 sets linked SQLite `3.51.3` as the current WAL floor. Historical SQLite `3.45.1` artifacts remain unchanged and version-bound.

Evidence proves only its declared code, environment, fixtures, workflow runs and bounded outputs.

```text
repository-resident evidence
≠ independent custody
≠ complete authenticity
≠ live-data safety
≠ physical deletion
≠ production readiness
```

## Three independent tracks

```text
H — Historical Recovery
  authentic v0.1.2.1 and original 44-test suite
  NOT_FOUND_IN_ACCESSIBLE_SOURCES / OPEN / INDEPENDENT

C — Clean Implementation
  P1–P5 + C4 + C5
  ACTIVE / PARTIAL

R — Long-Horizon Research
  PROPOSED / BOUNDED / NO AUTOMATIC PROMOTION
```

Clean implementation does not claim recovery of `v0.1.2.1`. Historical recovery does not block the clean lineage. Research prose does not become Canon or runtime automatically.

## Current gates

```text
human-readable truth reconciliation
→ Issues #14–#17 and Notion reconciliation
→ license/publication operator decision — Issue #18
→ ADR-0024 operator decision — Issue #74
→ NK-SAM and named equivalence profiles
→ Event/history commitment contract
→ only then reducer-v2 runtime
```

Not yet authorized in the current slice:

- reducer-v2 runtime;
- executable NK-EPI;
- Temporal runtime;
- full Admission lifecycle;
- operational deletion;
- full independent Rust/Go implementation;
- Titan, Crystal or Mentaury integration;
- production promotion.

## Human quickstart

The smallest semantic-core check requires Python 3.11 or 3.12:

```bash
python -m unittest discover -s tests -p 'test_semantic_core.py' -v
python -m unittest discover -s tests -p 'test_p1_manifest.py' -v
```

Machine-state integrity:

```bash
python tools/ai_context/validate_project_state.py --repo .
```

The SQLite profile fails closed when Python links SQLite older than `3.51.3`. PostgreSQL setup, expected skips and full commands are in [`docs/QUICKSTART.md`](docs/QUICKSTART.md).

## Explicit non-equivalences

```text
Claim ≠ truth
admission ≠ objective truth
Unknown ≠ False
runtime implementation ≠ evidence
evidence ≠ operator authorization
C5 PASS ≠ production readiness
PostgreSQL + SQLite ≠ full substrate neutrality
hash chain ≠ complete authenticity
logical ERASED ≠ physical deletion
public repository ≠ open-source license
```

## Read next

- [`STATUS.md`](STATUS.md) — authoritative human current-state surface
- [`project-state.json`](project-state.json) — authoritative committed machine status
- [`ROADMAP.md`](ROADMAP.md) — active gate sequence
- [`docs/QUICKSTART.md`](docs/QUICKSTART.md) — setup and tests
- [`docs/GLOSSARY.md`](docs/GLOSSARY.md) — terminology and non-equivalences
- [`AGENTS.md`](AGENTS.md) — mandatory repository instructions
- [`docs/ai/CURRENT_STATE.md`](docs/ai/CURRENT_STATE.md) — AI continuity checkpoint
- [`docs/ai/KNOWN_RISKS.md`](docs/ai/KNOWN_RISKS.md) — active and closed risks
- [`evidence/c5/README.md`](evidence/c5/README.md) — retained evidence identities
- [`docs/CONFORMANCE_MODEL.md`](docs/CONFORMANCE_MODEL.md) — conformance levels and proof boundaries
- [`docs/research/POST_C5_RESEARCH_BACKLOG.md`](docs/research/POST_C5_RESEARCH_BACKLOG.md) — proposed research only

Historical status and review chronology remains available in Git history and version-bound implementation/evidence records.