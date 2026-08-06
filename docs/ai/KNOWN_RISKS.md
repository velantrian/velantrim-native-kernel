# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-06  
**Last verified public `main`:** `2a03c871e5f7250c917c060cc112a9ea1497e9c4`

A detailed document, accepted ADR or passing support-tool test does not close a runtime risk.
Closure requires evidence in the declared scope.

## P0 — Authentic source recovery remains unresolved

**State:** `OPEN`

- The reported `v0.1.2.1` source and original 44-test suite are not present in `main`.
- Connected accessible-source search found no authentic candidate bytes.
- Operator-controlled local devices, backups and inaccessible archives remain outside connector evidence.
- Reconstruction must not be mislabelled as recovery.

Required proof: authentic archive/location, lineage, hashes, original test inventory and explicit operator GO.

## P0 — Documentation/implementation confusion

**State:** `OPEN`

The repository is architecture-rich but runtime-empty.
High-quality diagrams, ADRs and status text can be mistaken for implemented behavior.

Required controls:

- preserve status labels in every summary;
- update `STATUS.md` only with committed implementation evidence;
- distinguish source-recovery utility CI from Kernel CI;
- keep accepted decisions separate from implementation status.

## P0 — AI and documentation continuity drift

**State:** `NARROWED`, not closed  
**Evidence:** PR #26 → `099ae235ff935948348f2101804eb53ac9eeae1a`; exact-head run `31105098991`; main-push run `31105237368`.

The mandatory entry point and context pack reduce the chance that AI actors read historical audits as current truth, miss recent decisions, omit a hand-off, or silently break first-read navigation.

PR #26 adds repository-reproduced structural controls on Python 3.11 and 3.12:

- mandatory AI-context/governance files must exist;
- selected repository-relative Markdown links must resolve;
- relative links may not escape the repository;
- `CURRENT_STATE.md` must contain an exact checkpoint SHA;
- the checkpoint commit must exist and be an ancestor of the reviewed commit;
- core maturity and epistemic boundary markers must remain present.

Residual risk:

```text
structural guard PASS
≠ every statement is semantically current
≠ every material change updated the correct context file
≠ English/Russian meaning is automatically equivalent
≠ Notion synchronization proof
```

Required next controls:

- reviewers still classify documentation impact;
- material PRs update the affected context records;
- checkpoint ancestry remains a floor, not semantic freshness proof;
- broader link/language checks require separate bounded design and tests;
- branch protection remains a repository governance setting, not a property of the workflow itself.

## P1 — GitHub ↔ Notion drift

**State:** `OPEN`

Notion carries deeper rationale and history; GitHub carries the complete public technical/evidence package.
Manual synchronization can drift.

Required proof for closure:

- each material PR classifies documentation impact;
- GitHub remains sufficient without Notion;
- Notion record contains verified PR/merge SHA and exact status;
- connectorless work creates a structured hand-off rather than a false sync claim.

The AI-context validator does not call the Notion API and must not be cited as proof that Notion is synchronized.

## P1 — Cross-project semantic confusion

**State:** `OPEN`

Native Kernel, Mentaury, Titan and Crystal have complementary roles but independent Canons and authority boundaries.
Risks include treating:

- Kernel events as Mentaury personal identity;
- Titan tool output as admitted belief;
- Crystal TruthGate as a Kernel dependency;
- ecosystem links as runtime wiring;
- shared terminology as proven semantic equivalence.

Required proof before any integration claim: scoped RFC/ADR, mapping contract, tests, threat/privacy review, rollback and explicit approvals.

## P1 — Foundational contract responsibilities can be silently collapsed

**State:** `NARROWED BY ACCEPTED ADR-0010`, not closed

The architecture previously named Claims, Events, provenance, admission, conflicts, unknowns, Receipts and conformance without one accepted ownership map. A profile could therefore collapse:

```text
semantic content
= source assertion
= observation
= evidence
= admitted knowledge
= storage record
```

ADR-0010 and the bilingual `foundational-skeleton/1.0` contract now accept six separate families:

- `NK-SEM` — semantic roles;
- `NK-ID` — identity and canonical encoding;
- `NK-EVT` — event, observation and recorded change;
- `NK-AUT` — authority and admission;
- `NK-CFL` — conflict and explicit unknowns;
- `NK-EQV` — conformance and semantic equivalence.

This closes the missing architecture-ownership map only. It does not establish schemas, fixtures, runtime behaviour, deletion guarantees or cross-profile evidence.

Residual proof required:

- exact versioned contracts for identity, events, authority, conflict and equivalence;
- valid and invalid fixtures;
- profile mappings and evidence records;
- no silent skip of unsupported assertions;
- at least two materially different profiles before C3 claims.

## P1 — Storage neutrality is unproven

**State:** `OPEN`

ADR-0009 selects PostgreSQL as preferred full profile and SQLite as optional embedded profile, but no Kernel adapters or cross-profile conformance evidence exist.

Required proof:

- normative event/identity encoding;
- shared golden histories;
- adapters with declared capability profiles;
- replay/equivalence tests;
- migration, interruption, corruption and rollback evidence.

## P1 — Executable conformance is absent

**State:** `OPEN`

C0–C5 remains a documentation model.
No committed normative schemas, golden event vectors, invalid corpora, expected reducer outputs or cross-profile runner currently prove compatibility.

## P1 — Deletion and restriction contract is incomplete

**State:** `OPEN`

`ERASED` as an event concept does not by itself define deletion/restriction for payloads, projections, vectors, exports, Receipts, backups or Shadow data.
A separate threat model and verifiable lifecycle remain required.

## P1 — Claim identity and canonical bytes are not normative

**State:** `OPEN`

Stable identity is required, but exact canonical encoding, Unicode policy, hash domains, collision handling and migration rules are not yet committed as executable contract evidence.

## P1 — Context sufficiency remains unproven

**State:** `OPEN`

Lexical activation and proxy ablation may support research, but:

```text
selected context ≠ sufficient evidence
minimal changed answer ≠ globally minimal Grip
stable answer ≠ correct answer
```

Any future claim requires task obligations, evidence coverage, contradiction coverage, omissions and structured Receipts.

## P1 — Future-substrate claims can become hype

**State:** `OPEN`

Neuromorphic, photonic, analog, probabilistic, non-binary and other substrates are valid research possibilities.
They are not evidence of portability, superiority or implementation.

## Update rule

For every risk, record:

- state: `OPEN`, `NARROWED`, `CLOSED`, `ACCEPTED`, or `DEFERRED`;
- exact evidence and SHA;
- what remains unproven;
- owning issue/ADR/PR;
- required next action.

Do not close a risk through wording alone.
