# 🗺️ Native Kernel Document, Contract and Authority Map

Use exact SHAs, statuses and evidence. Document presence is not runtime wiring.

## Primary orientation surfaces

| Surface | Role | Authority / caution |
|---|---|---|
| `README.md` / `README.ru.md` | Public overview and ecosystem navigation | Must match maturity boundary |
| `STATUS.md` | Current implementation and evidence boundary | Authoritative for public status claims |
| `ARCHITECTURE.md` | Canon shape, invariants and portability target | Architecture, not runtime proof |
| `ROADMAP.md` | Stage gates and future work | Planned sequence, not implementation |
| `AGENTS.md` | Mandatory AI/reviewer rules | Repository-wide guidance |
| `docs/ai/*` | Current orientation, risks, logs and sync protocol | Last-verified operational context |

## Architecture and intent

| Question | First read | Supporting records |
|---|---|---|
| Why does Kernel exist? | `docs/FOUNDATIONAL_INTENT*` | `docs/LONG_HORIZON_VISION.md` |
| What meaning must survive? | `ARCHITECTURE.md` | ADR-0001, conformance model |
| What is not Canon? | `ARCHITECTURE.md`, Copilot instructions | profile docs, Anti-Canon statements |
| How are decisions accepted? | `docs/DECISION_PROCESS.md` | ADR-0007, ADR template/index |
| How is compatibility demonstrated? | `docs/CONFORMANCE_MODEL.md` | ADR-0004, benchmarks |

## Source recovery and executable evidence

Start with:

- `STATUS.md`;
- `docs/ISSUE_1_IMPORT_SPEC.md` and `.ru.md`;
- `prototype/README.md`;
- `docs/source-recovery/README.md`;
- `docs/source-recovery/2026-07-26-accessible-sources-sweep.md`;
- `tools/source_recovery/`;
- `.github/workflows/source-recovery-tools.yml`;
- GitHub Issue #1.

Authority boundary:

```text
source-recovery tooling
→ inventories and verifies candidate bytes
→ does not authenticate historical provenance
→ does not execute Kernel runtime
→ does not reproduce the external 44-test checkpoint
```

## Storage and execution profiles

Start with:

- `docs/STORAGE_AND_EXECUTION_PROFILES.md`;
- `docs/STORAGE_AND_EXECUTION_PROFILES.ru.md`;
- ADR-0009;
- `docs/CONFORMANCE_MODEL.md`.

Decision boundary:

```text
PostgreSQL preferred full profile
+ SQLite optional embedded profile
= accepted documentation direction
≠ implemented adapters
≠ storage-neutrality evidence
```

## Curiosity, causality and optional research

| Area | First read | Current state |
|---|---|---|
| Curiosity Core | RFC-0001 + ADR-0005 | proposed, docs-only, non-authoritative |
| Causal relations | ADR-0006 + related research notes | accepted placement, not implemented |
| Bio-inspired/Kitara | `docs/research/*` | optional research, not Canon |
| Physarum routing | dedicated experiment note | proposed, bounded, not implemented |

## World and epistemic boundaries

Start with:

- `docs/WORLD_AND_EPISTEMIC_BOUNDARIES.md`;
- ADR-0008;
- Architecture invariants 23–30.

Preserve:

```text
representation ≠ represented reality
observation ≠ explanation
transformation ≠ origin
unknown ≠ false
missing provenance ≠ permission to invent provenance
```

## Ecosystem boundaries

Start with:

- `docs/VELANTRIM_ECOSYSTEM.md`;
- `docs/INTEGRATION_BOUNDARIES.md`;
- ecosystem section in both READMEs.

Roles:

- Native Kernel — substrate-neutral memory/event/replay contract research;
- Mentaury Soul — digital individuality and continuity research;
- Titan — cognition, retrieval, tools, agents and orchestration;
- Crystal — verifiable memory, evidence, trust and audit.

Cross-links do not authorize runtime integration, shared storage, shared Canon or inherited authority.

## Decision ownership

- Architecture acceptance: operator/maintainer through ADR process.
- Implementation evidence: committed code, tests and exact repository evidence.
- Source authenticity: provenance evidence plus explicit operator gate.
- Runtime activation: no accepted Native Kernel runtime owner exists in current `main`.
- Cross-project integration: separate project owners plus bounded RFC/ADR, tests, rollback and explicit approval.
- Notion: rationale/history surface; never overrides GitHub implementation evidence.

## Task routes

| Task | Minimum route |
|---|---|
| General audit | `AGENTS` → `STATUS` → AI pack → affected documents |
| Source candidate | Issue #1 spec → source-recovery README/tooling → provenance manifest |
| New profile | profile docs → conformance model → ADR → evidence plan |
| New event or Claim semantics | Architecture → decision process → ADR → conformance fixtures |
| Cross-project reference | ecosystem map → integration boundaries → affected project docs |
| Documentation-only polish | paired language files → status check → link validation |
| Notion unavailable | complete GitHub → `NOTION_HANDOFF.md` |
