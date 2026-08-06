# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-06  
**Verified baseline before AI context-pack change:** `18ee09c870f7416932de29a2b2f5de53202fcb2e`

A detailed document, accepted ADR or passing support-tool test does not close a runtime risk.
Closure requires evidence in the declared scope.

## P0 — Authentic source recovery remains unresolved

- The reported `v0.1.2.1` source and original 44-test suite are not present in `main`.
- Connected accessible-source search found no authentic candidate bytes.
- Operator-controlled local devices, backups and inaccessible archives remain outside connector evidence.
- Reconstruction must not be mislabelled as recovery.

Required proof: authentic archive/location, lineage, hashes, original test inventory and explicit operator GO.

## P0 — Documentation/implementation confusion

The repository is architecture-rich but runtime-empty.
High-quality diagrams, ADRs and status text can be mistaken for implemented behavior.

Required controls:

- preserve status labels in every summary;
- update `STATUS.md` only with committed implementation evidence;
- distinguish source-recovery utility CI from Kernel CI;
- keep accepted decisions separate from implementation status.

## P0 — AI and documentation continuity drift

Without a mandatory entry point and context pack, AI actors may:

- read historical audits as current truth;
- miss recent ADRs or PRs;
- repeat rejected proposals;
- omit Notion synchronization;
- leave important findings only in chat;
- update one language while the paired document remains stale.

This context pack reduces the risk but does not remove it. Every actor must compare the recorded checkpoint with the actual SHA.

## P1 — GitHub ↔ Notion drift

Notion carries deeper rationale and history; GitHub carries the complete public technical/evidence package.
Manual synchronization can drift.

Required proof for closure:

- each material PR classifies documentation impact;
- GitHub remains sufficient without Notion;
- Notion record contains verified PR/merge SHA and exact status;
- connectorless work creates a structured hand-off rather than a false sync claim.

## P1 — Cross-project semantic confusion

Native Kernel, Mentaury, Titan and Crystal have complementary roles but independent Canons and authority boundaries.
Risks include treating:

- Kernel events as Mentaury personal identity;
- Titan tool output as admitted belief;
- Crystal TruthGate as a Kernel dependency;
- ecosystem links as runtime wiring;
- shared terminology as proven semantic equivalence.

Required proof before any integration claim: scoped RFC/ADR, mapping contract, tests, threat/privacy review, rollback and explicit approvals.

## P1 — Storage neutrality is unproven

ADR-0009 selects PostgreSQL as preferred full profile and SQLite as optional embedded profile, but no Kernel adapters or cross-profile conformance evidence exist.

Required proof:

- normative event/identity encoding;
- shared golden histories;
- adapters with declared capability profiles;
- replay/equivalence tests;
- migration, interruption, corruption and rollback evidence.

## P1 — Executable conformance is absent

C0–C5 remains a documentation model.
No committed normative schemas, golden event vectors, invalid corpora, expected reducer outputs or cross-profile runner currently prove compatibility.

## P1 — Deletion and restriction contract is incomplete

`ERASED` as an event concept does not by itself define deletion/restriction for payloads, projections, vectors, exports, Receipts, backups or Shadow data.
A separate threat model and verifiable lifecycle remain required.

## P1 — Claim identity and canonical bytes are not normative

Stable identity is required, but exact canonical encoding, Unicode policy, hash domains, collision handling and migration rules are not yet committed as executable contract evidence.

## P1 — Context sufficiency remains unproven

Lexical activation and proxy ablation may support research, but:

```text
selected context ≠ sufficient evidence
minimal changed answer ≠ globally minimal Grip
stable answer ≠ correct answer
```

Any future claim requires task obligations, evidence coverage, contradiction coverage, omissions and structured Receipts.

## P1 — Future-substrate claims can become hype

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
