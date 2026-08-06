# 🗺️ Native Kernel Document, Contract and Authority Map

Use exact SHAs, statuses and evidence. Document presence is not runtime wiring.

## Primary orientation surfaces

| Surface | Role | Authority / caution |
|---|---|---|
| `README.md` / `README.ru.md` | Public overview and ecosystem navigation | Must match maturity boundary |
| `STATUS.md` | Current implementation and evidence boundary | Authoritative for public status claims |
| `ARCHITECTURE.md` | Canon shape, invariants and portability target | Architecture, not runtime proof |
| `docs/FOUNDATIONAL_CONTRACT_SKELETON*` | Accepted six-family ownership map | ADR-0010 accepted; runtime absent |
| `docs/contracts/NORMATIVE_CONTRACTS_V1*` | Proposed exact v1 identity/event/deletion/fixture contracts | ADR-0011…0014 pending operator decision |
| `contracts/*.json` | Registry, schema bundle and executable fixture corpus | Machine-readable proposal/evidence surface, not runtime |
| `tools/conformance/` | Fixture-integrity reader and adapter protocol | Support tooling; reports Kernel runtime as `UNSUPPORTED` |
| `docs/ai/*` | Current orientation, risks, logs and sync protocol | Last-verified operational context |
| `tools/ai_context/` | Context-pack integrity checks | Governance tooling, not Kernel runtime evidence |

## Architecture and exact-contract route

```text
ARCHITECTURE.md
        ↓
FOUNDATIONAL_CONTRACT_SKELETON (accepted ownership map)
        ↓
NORMATIVE_CONTRACTS_V1 (proposed exact contracts)
        ↓
contracts/registry + schemas + fixtures
        ↓
tools/conformance fixture-integrity evidence
        ↓
future implementation profiles
```

### Stable families

```text
NK-SEM — semantic roles
NK-ID  — identity and canonical encoding
NK-EVT — event, observation and recorded change
NK-AUT — authority and admission
NK-CFL — conflict and explicit unknowns
NK-EQV — conformance and semantic equivalence
NK-EPI — proposed epistemic fixture family
```

### Issues #14–#17 ownership

| Issue | Owning proposal | Machine-readable evidence |
|---|---|---|
| #14 identity/canonical encoding | ADR-0011 + identity section of `NORMATIVE_CONTRACTS_V1` | `registry.json`, identity golden/invalid fixtures, reference canonicalizer |
| #15 append/idempotency/order/replay | ADR-0012 + event section | command/event schemas and event-chain scenarios |
| #16 deletion/restriction/retention | ADR-0013 + deletion section | deletion Receipt schema and state-machine scenarios |
| #17 executable conformance | ADR-0014 + fixture protocol section | registry, schema/fixture bundles, runner, tests and workflow |

Authority boundary:

```text
proposed exact contract
+ locally passing fixture tooling
≠ operator-accepted architecture
≠ implemented Kernel runtime
≠ C2 repository conformance until exact CI evidence
≠ C3 cross-profile equivalence
```

## Conformance tooling route

Start with:

- `docs/contracts/NORMATIVE_CONTRACTS_V1.md` or `.ru.md`;
- ADR-0011 through ADR-0014;
- `contracts/registry.json`;
- `contracts/schema-bundle.json`;
- `contracts/fixture-pack.json`;
- `tools/conformance/README.md`;
- `tools/conformance/runner.py`;
- `tests/test_conformance_runner.py`;
- `.github/workflows/conformance-fixtures.yml`.

The runner validates assertion uniqueness, identity vectors, event chains, deletion transitions and positive/negative `NK-EPI-001…008` coverage. Its evidence report deliberately states:

```text
support_state: SUPPORTED
kernel_runtime_conformance: UNSUPPORTED
```

## Source recovery boundary

Start with `STATUS.md`, Issue #1, import specs, `docs/source-recovery/`, `tools/source_recovery/` and its isolated workflow.

```text
Issues #14–#17 proposal lineage
≠ controlled v0.1.2.1 import
≠ recovered original tests
≠ historical reproduction evidence
```

## AI context integrity tooling

Start with `tools/ai_context/README.md`, validator, tests and workflow. A structural PASS does not prove semantic freshness, Notion synchronization, architecture correctness or Kernel runtime behaviour.

## Storage and execution profiles

PostgreSQL preferred full profile and SQLite optional profile are accepted documentation direction under ADR-0009. No adapters or storage-neutrality evidence currently exist.

## World and epistemic boundaries

Preserve:

```text
representation ≠ represented reality
observation ≠ explanation
transformation ≠ origin
unknown ≠ false
missing provenance ≠ permission to invent provenance
retrieval/model output ≠ admitted knowledge
```

ADR-0008 and `NK-EPI-001…008` remain proposed until explicit operator acceptance. Executable fixtures improve reviewability but do not promote them automatically.

## Ecosystem boundaries

- Native Kernel — substrate-neutral memory/event/replay contract research;
- Mentaury Soul — digital individuality and continuity research;
- Titan — cognition, retrieval, tools, agents and orchestration;
- Crystal — verifiable memory, evidence, trust and audit.

Cross-links do not authorize runtime integration, shared storage, shared Canon or inherited authority.

## Decision ownership

- Architecture acceptance: operator/maintainer through ADR process.
- Fixture/tool evidence: exact code, tests, commands and CI at a named SHA.
- Kernel implementation evidence: future committed runtime profiles, not fixture tooling.
- Source authenticity: provenance evidence plus explicit Issue #1 operator gate.
- C3 claim: two materially independent profiles and declared equivalence.
- Notion: rationale/history surface; never overrides GitHub implementation evidence.

## Task routes

| Task | Minimum route |
|---|---|
| General audit | `AGENTS` → `STATUS` → AI pack → affected documents |
| Identity contract | skeleton → ADR-0011 → normative contract → identity fixtures |
| Event/replay contract | skeleton → ADR-0012 → schemas/scenarios → threat boundary |
| Deletion contract | ADR-0013 → location inventory/state machine/Receipt fixtures |
| Conformance evidence | ADR-0014 → registry/schema/fixture pack → runner/tests/CI |
| Source candidate | Issue #1 spec → source-recovery tooling → provenance manifest |
| New implementation profile | profile docs → exact contracts → conformance model → separate ADR/evidence plan |
| Cross-project reference | ecosystem map → integration boundaries → affected project docs |
| Notion unavailable | complete GitHub → `NOTION_HANDOFF.md` |
