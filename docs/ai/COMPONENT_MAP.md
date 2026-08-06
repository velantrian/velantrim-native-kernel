# 🗺️ Native Kernel Document, Contract and Authority Map

Use exact SHAs, statuses and evidence. Document presence is not runtime wiring.

## Primary orientation surfaces

| Surface | Role | Authority / caution |
|---|---|---|
| `README.md` / `README.ru.md` | Public overview and ecosystem navigation | Must match maturity boundary |
| `STATUS.md` | Current implementation and evidence boundary | Authoritative for public status claims |
| `ARCHITECTURE.md` | Canon shape, invariants and portability target | Architecture, not runtime proof |
| `docs/FOUNDATIONAL_CONTRACT_SKELETON*` | Accepted six-family ownership map | ADR-0010 accepted; runtime absent |
| `docs/contracts/NORMATIVE_CONTRACTS_V1*` | Accepted exact v1 identity/event/deletion/fixture contracts | ADR-0011…0014 accepted; runtime absent |
| `contracts/*.json` | Registry, schema bundle and executable fixture corpus | Machine-readable accepted contract/evidence surface, not runtime |
| `docs/rfc/0002-postgresql-reference-profile-v0*` | Proposed first clean PostgreSQL profile plan | Planning only; operator approval and runtime GO pending |
| `profiles/postgresql-reference-v0/profile-manifest.json` | Machine-readable assertion/phase plan | All runtime support remains `UNSUPPORTED` |
| `tools/profiles/` | Planning-manifest validator | Prevents false runtime/recovery promotion |
| `tools/conformance/` | Fixture-integrity reader and adapter protocol | Support tooling; reports Kernel runtime as `UNSUPPORTED` |
| `docs/ai/*` | Current orientation, risks, logs and sync protocol | Last-verified operational context |
| `tools/ai_context/` | Context-pack integrity checks | Governance tooling, not Kernel runtime evidence |

## Architecture, contracts and profile route

```text
ARCHITECTURE.md
        ↓
FOUNDATIONAL_CONTRACT_SKELETON (accepted ownership map)
        ↓
NORMATIVE_CONTRACTS_V1 (accepted exact contracts)
        ↓
contracts/registry + schemas + fixtures
        ↓
RFC-0002 + proposed PostgreSQL profile manifest
        ↓
separate operator runtime GO
        ↓
future implementation PRs and evidence
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

| Issue | Accepted contract | Machine-readable evidence |
|---|---|---|
| #14 identity/canonical encoding | ADR-0011 + `nk-id/1.0` | `registry.json`, identity golden/invalid fixtures, reference canonicalizer |
| #15 append/idempotency/order/replay | ADR-0012 + `nk-event/1.0` | command/event schemas, event-chain and idempotency scenarios |
| #16 deletion/restriction/retention | ADR-0013 + `nk-deletion/1.0` | deletion Receipt schema and state-machine scenarios |
| #17 executable conformance | ADR-0014 + `nk-fixtures/1.0` | registry, schema/fixture bundles, runner, tests and workflow |
| #40 clean PostgreSQL profile planning | RFC-0002 proposal | profile manifest, validator, tests and phased implementation plan |

Authority boundary:

```text
accepted exact contract
+ proposed profile plan
+ locally passing planning validator
≠ accepted runtime implementation
≠ recovered v0.1.2.1
≠ C2 or C3
```

## RFC-0002 route

Read in this order:

1. [Issue #40](https://github.com/velantrian/velantrim-native-kernel/issues/40);
2. `docs/rfc/0002-postgresql-reference-profile-v0.md` or `.ru.md`;
3. `profiles/README.md`;
4. `profiles/postgresql-reference-v0/profile-manifest.json`;
5. `tools/profiles/validate_manifest.py`;
6. `tests/test_profile_manifest.py`;
7. `.github/workflows/conformance-fixtures.yml`.

Profile identity:

```text
profile_id:        native-kernel/postgresql-reference
planning_version:  nk-pg-profile/0.1-proposed
evidence_lineage:  clean/postgresql-reference/0.1
RFC status:        PROPOSED
operator approval: PENDING
implementation:    NOT_STARTED
runtime support:   UNSUPPORTED
```

The proposed manifest maps all 72 registry assertions:

- 64 accepted-family assertions are `PLANNED` for phases P1–P4;
- eight `NK-EPI` assertions remain `DEFERRED_PROPOSED_FAMILY`;
- every assertion reports runtime support as `UNSUPPORTED`;
- historical lineage is null;
- Issue #1 remains independent.

The profile validator rejects missing/duplicate assertions, false runtime support, a historical `v0.1.2.1` lineage claim, and silent promotion of `NK-EPI`.

## Conformance tooling route

Start with:

- `docs/contracts/NORMATIVE_CONTRACTS_V1.md` or `.ru.md`;
- ADR-0011 through ADR-0014;
- `contracts/registry.json`;
- `contracts/schema-bundle.json`;
- `contracts/evidence-report-v1.schema.json`;
- `contracts/fixture-pack.json`;
- `contracts/idempotency-scenarios.json`;
- `tools/conformance/README.md`;
- `tools/conformance/runner.py`;
- `tests/test_conformance_runner.py`;
- `.github/workflows/conformance-fixtures.yml`.

The runner validates assertion uniqueness, identity vectors, event commitments/chains, idempotency cases, deletion transitions and positive/negative `NK-EPI-001…008` coverage. Its evidence report deliberately states:

```text
support_state: SUPPORTED
kernel_runtime_conformance: UNSUPPORTED
```

The expanded workflow can validate both accepted fixtures and the proposed planning manifest on Python 3.11/3.12. A declared workflow is not an executed result.

## Source recovery boundary

Start with `STATUS.md`, Issue #1, import specs, `docs/source-recovery/`, `tools/source_recovery/` and its isolated workflow.

```text
clean/postgresql-reference/0.1
≠ controlled v0.1.2.1 import
≠ recovered original tests
≠ declaration that historical source is globally lost
```

RFC-0002 cannot close or replace Issue #1. Runtime work requires a separate operator decision.

## AI context integrity tooling

Start with `tools/ai_context/README.md`, validator, tests and workflow. A structural PASS does not prove semantic freshness, Notion synchronization, architecture correctness or Kernel runtime behaviour.

## Storage and execution profiles

ADR-0009 accepts PostgreSQL as the preferred full contemporary profile and SQLite as optional. RFC-0002 proposes the first clean PostgreSQL profile lineage but does not implement an adapter or prove storage neutrality.

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

ADR-0008 and `NK-EPI-001…008` remain proposed. Executable fixtures and a planning manifest do not promote them.

## Ecosystem boundaries

- Native Kernel — substrate-neutral memory/event/replay contract research;
- Mentaury Soul — digital individuality and continuity research;
- Titan — cognition, retrieval, tools, agents and orchestration;
- Crystal — verifiable memory, evidence, trust and audit.

Cross-links do not authorize runtime integration, shared storage, shared Canon or inherited authority.

## Decision ownership

- Architecture acceptance: operator/maintainer through ADR process.
- RFC/profile-plan acceptance: separate operator decision.
- Runtime implementation start: separate explicit GO after planning acceptance.
- Fixture/tool evidence: exact code, tests, commands and CI at a named SHA.
- Kernel implementation evidence: future committed runtime profiles, not planning manifests.
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
| PostgreSQL profile plan | Issue #40 → RFC-0002 → manifest → validator/tests |
| Future PostgreSQL implementation | accepted RFC + separate runtime GO → stage-specific PR |
| Source candidate | Issue #1 spec → source-recovery tooling → provenance manifest |
| Cross-project reference | ecosystem map → integration boundaries → affected project docs |
| Notion unavailable | complete GitHub → `NOTION_HANDOFF.md` |
