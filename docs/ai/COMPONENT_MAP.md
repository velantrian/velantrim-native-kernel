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
| `tools/ai_context/` + `.github/workflows/ai-context.yml` | Context-pack integrity checks | Support/governance tooling, not Kernel runtime evidence |

## Architecture and intent

| Question | First read | Supporting records |
|---|---|---|
| Why does Kernel exist? | `docs/FOUNDATIONAL_INTENT*` | `docs/LONG_HORIZON_VISION.md` |
| What meaning must survive? | `ARCHITECTURE.md` | ADR-0001, conformance model |
| How are the foundational responsibilities separated? | `docs/FOUNDATIONAL_CONTRACT_SKELETON*` | accepted ADR-0010, Issues #14–#17 |
| What is not Canon? | `ARCHITECTURE.md`, Copilot instructions | profile docs, Anti-Canon statements |
| How are decisions accepted? | `docs/DECISION_PROCESS.md` | ADR-0007, ADR template/index |
| How is compatibility demonstrated? | `docs/CONFORMANCE_MODEL.md` | ADR-0004, benchmarks |

## Foundational contract skeleton

Start with:

- `docs/FOUNDATIONAL_CONTRACT_SKELETON.md`;
- `docs/FOUNDATIONAL_CONTRACT_SKELETON.ru.md`;
- ADR-0010;
- Issues #14, #15, #16 and #17;
- `docs/WORLD_AND_EPISTEMIC_BOUNDARIES.md` and ADR-0008.

Accepted family map:

```text
NK-SEM — semantic roles
NK-ID  — identity and canonical encoding
NK-EVT — event, observation and recorded change
NK-AUT — authority and admission
NK-CFL — conflict and explicit unknowns
NK-EQV — conformance and semantic equivalence
```

Authority boundary:

```text
accepted assertion namespace
≠ executable schema
≠ implemented runtime
≠ conformance evidence
≠ proven portability
```

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

## AI context integrity tooling

Start with:

- `tools/ai_context/README.md`;
- `tools/ai_context/validate_context.py`;
- `tests/test_ai_context_validator.py`;
- `.github/workflows/ai-context.yml`.

The guard verifies required context files, selected repository-relative links, checkpoint syntax, commit existence, checkpoint ancestry and status-boundary markers.

```text
AI-context guard PASS
→ repository orientation package is structurally coherent

AI-context guard PASS
≠ every statement is semantically current
≠ Notion is synchronized
≠ Architecture Canon is correct
≠ Kernel runtime exists or works
```

An ancestor checkpoint is valid by design. Human or AI review still decides whether intervening material changes require a new semantic checkpoint.

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
| Foundational semantic/identity/authority change | foundational skeleton → relevant ADR/issue → conformance model |
| Source candidate | Issue #1 spec → source-recovery README/tooling → provenance manifest |
| AI-context integrity | AI-context README → validator/tests → workflow result → affected context file |
| New profile | profile docs → conformance model → ADR → evidence plan |
| New event or Claim semantics | foundational skeleton → Architecture → decision process → ADR → conformance fixtures |
| Cross-project reference | ecosystem map → integration boundaries → affected project docs |
| Documentation-only polish | paired language files → status check → link validation |
| Notion unavailable | complete GitHub → `NOTION_HANDOFF.md` |
