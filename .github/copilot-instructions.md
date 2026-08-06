# GitHub Copilot instructions for Velantrim Native Kernel

## Mandatory orientation

Before auditing, reviewing or changing this repository, read:

1. [`../AGENTS.md`](../AGENTS.md) — repository-wide mandatory AI guidance;
2. [`../STATUS.md`](../STATUS.md) — authoritative implementation/evidence boundary;
3. [`../docs/ai/README.md`](../docs/ai/README.md) — AI context-pack manifest;
4. [`../docs/ai/DOCUMENTATION_SYNC_PROTOCOL.md`](../docs/ai/DOCUMENTATION_SYNC_PROTOCOL.md);
5. [`../docs/ai/CURRENT_STATE.md`](../docs/ai/CURRENT_STATE.md);
6. relevant component, risk and recent work-log entries under `docs/ai/`.

Treat these as orientation checkpoints, not automatic proof. Verify the actual branch/PR SHA before carrying forward any status, test count or implementation claim.

## Project identity

- Treat Native Kernel as an independent, personal, long-horizon architecture research project.
- It is separate from Crystal, Titan and Mentaury implementation tracks.
- The project may study ideas from those repositories, academic work and external systems, but adoption is selective and must preserve Native Kernel's own architecture, lineage and evidence gates.
- Current technologies are research instruments and implementation profiles, not the permanent definition of the system.

## Project status discipline

- Treat this repository as `RESEARCH / DOCUMENTED_ONLY / NOT PRODUCTION-READY` until `STATUS.md` is explicitly changed by a reviewed implementation PR.
- No runnable Native Kernel or original 44-test suite is currently present in `main`.
- Source-recovery tooling is support tooling, not Kernel runtime evidence.
- `NOT_FOUND_IN_ACCESSIBLE_SOURCES` must not be rewritten as `GLOBALLY_LOST`.
- Do not describe the project as runnable, production-ready, secure, complete, generally linear, sufficient, conscious, autonomous, truth-authoritative, or portable across arbitrary future hardware unless repository evidence supports the claim.

Use status vocabulary consistently:

- `DOCUMENTED_ONLY` — specification exists, no runtime claim;
- `PROPOSED` — suggested change without approval;
- `ACCEPTED` — operator-approved decision; implementation may still be absent;
- `EXPERIMENTAL` — runnable/testable mechanism under evaluation;
- `IMPLEMENTED` — code exists in the declared scope;
- `TESTED` — committed tests exist and their result is known;
- `WIRED` — a real runtime caller exists;
- `ENABLED` — selected configuration activates it;
- `OBSERVED` — a running instance produced operational evidence.

## Architecture terminology

- Preserve the distinction between Architecture Canon, Abstract Contracts and Implementation Profiles.
- Preserve the distinction between Claim, Event, projection, epistemic state, charge, context selection and Receipt.
- Treat append-only event history as authoritative about recorded history, not automatically equivalent to truth.
- Treat PostgreSQL, SQLite, graph, FTS, vector stores, Python, model APIs and conventional hardware as replaceable implementation choices.
- Do not allow backend-generated identifiers, schemas, embeddings, graph nodes, APIs, runtimes or processor assumptions to become semantic identity by accident.
- Keep truth separate from relevance, utility, frequency, freshness, write order and task selection.
- Use `evidence grip` in lowercase. Do not claim genuine sufficiency or global minimality for lexical proxy ablation.
- Distinguish candidate conflicts from established conflicts and detection from resolution.
- Treat future neuromorphic, photonic, analog, non-binary or other substrates as research possibilities, not implementation evidence.

## Issue #1 source-recovery discipline

- Keep controlled prototype import separate from semantic redesign.
- Do not reconstruct, regenerate or approximate an implementation and label it `v0.1.2.1`.
- Do not replace the original suite with new tests and call the original evidence recovered.
- Do not silently rewrite the reported baseline during import.
- Authenticity requires provenance, preserved bytes, original test inventory and explicit operator GO.
- If recovery ultimately fails, a clean implementation requires a new version and evidence lineage after an explicit operator decision.

## State Checkpoints and conflicts

- Treat State Checkpoints as `PROPOSED` and `NOT IMPLEMENTED` unless repository code/tests prove otherwise.
- Distinguish State Checkpoint, Read Snapshot, Evaluation Snapshot, Claim freshness and replay completeness.
- Do not prescribe checkpoint frequency, retention, SQLite schema or Claim-per-stream as Architecture Canon.
- Do not describe OCC, durable command idempotency, CRDT policy, multi-writer merge or a conflict-resolution API as implemented.
- Preserve the principle that write order may define deterministic order but must not independently determine semantic truth.
- Do not add new conflict event verbs to controlled import.

## Architecture Decision Records

- Major Canon, contract, event-vocabulary, checkpoint, conflict, portability and integration-boundary changes require an ADR.
- Keep four dimensions separate:
  - decision status: `PROPOSED | ACCEPTED | REJECTED | DEPRECATED | SUPERSEDED`;
  - evidence level: `DOCUMENTED | EXTERNALLY_OBSERVED | LOCALLY_TESTED | REPOSITORY_REPRODUCED | SHADOW_EVALUATED | OPERATIONALLY_VALIDATED`;
  - implementation status: `NOT_STARTED | PARTIAL | COMPLETE | REMOVED`;
  - operator approval: `NOT_REQUESTED | PENDING | APPROVED | WITHDRAWN`.
- An accepted ADR does not mean runtime code exists.
- Multi-model agreement may be listed as input, never as evidence or approval.

## Ecosystem boundaries

- Native Kernel is independent and is not a universal Velantrim truth authority.
- Titan is a cognition/retrieval/tools/orchestration environment, not Kernel's mandatory parent or storage owner.
- Mentaury Soul owns digital-individuality, identity-continuity, relationship and commitment semantics in its own project; Kernel events do not establish personal identity by themselves.
- Crystal is an independent verifiable-memory and grant-facing product; it must not be described as dependent on Kernel.
- Do not introduce direct Kernel writes into another project's Canon.
- Do not insert Crystal TruthGate or Titan/Mentaury domain policy as a Kernel dependency during controlled import.
- Any transfer requires a separate RFC/ADR, semantic mapping, threat/privacy review, tests, rollback and explicit approvals.

## Bilingual documentation

- `README.md` is English and `README.ru.md` is Russian.
- Keep visible language selectors and semantic alignment.
- Translation may adapt wording but must preserve status, maturity, evidence, benchmark, security, ADR and ecosystem claims.
- Update paired substantive sections in the same PR or explicitly record the temporary gap.

## Documentation synchronization

Every PR must follow [`../docs/ai/DOCUMENTATION_SYNC_PROTOCOL.md`](../docs/ai/DOCUMENTATION_SYNC_PROTOCOL.md) and classify impact as `NONE`, `GITHUB_ONLY` or `GITHUB_AND_NOTION`.

For material work, update as applicable:

- `STATUS.md` and `docs/ai/CURRENT_STATE.md`;
- `docs/ai/KNOWN_RISKS.md`;
- `docs/ai/COMPONENT_MAP.md`;
- `docs/ai/WORK_LOG.md`;
- relevant ADR/RFC and public documentation;
- Notion directly or `docs/ai/NOTION_HANDOFF.md`.

GitHub must contain enough public technical and audit context to continue without Notion. Do not leave material decisions, evidence, risks or next actions only in chat.

## Documentation style

- Keep technical meaning exact and avoid hype.
- Use clear visual hierarchy: concise headings, selective emojis, tables, Mermaid/ASCII where useful, and direct links.
- Do not remove status warnings for visual polish.
- Prefer one canonical term across README, STATUS, ROADMAP, ARCHITECTURE, ADRs and context files.
- Benchmark claims must state whether evidence is external, local or repository-reproduced.
- Make clear that technology independence does not mean rejecting current systems.

## Change discipline

Before writing:

1. establish exact base/head SHA and scope;
2. distinguish `main`, open PR, external checkpoint, proposal and implemented state;
3. inspect affected contracts, ADRs, tests and documentation;
4. preserve Issue #1 and ecosystem boundaries;
5. make the smallest coherent change;
6. validate it;
7. update GitHub continuity records and Notion or create a hand-off;
8. open a PR with evidence and remaining limitations.

Do not silently combine unrelated cleanup, source recovery, redesign, runtime implementation, profile activation or cross-project integration.
