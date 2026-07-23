# GitHub Copilot instructions for Velantrim Native Kernel

## Project identity

- Treat Native Kernel as an independent, personal, long-horizon architecture research project.
- It is separate from the Crystal grant-facing product and is not constrained by Crystal delivery milestones.
- The project may study ideas from Titan, Crystal, academic work, and external systems, but adoption is selective and must preserve Native Kernel's own architecture and evidence gates.
- Current technologies are research instruments and implementation profiles, not the permanent definition of the system.

## Project status discipline

- Treat this repository as `RESEARCH / DOCUMENTED_ONLY / NOT PRODUCTION-READY` until `STATUS.md` is explicitly changed by a reviewed implementation PR.
- Do not describe the project as runnable, production-ready, secure, complete, generally linear, sufficient, conscious, autonomous, truth-authoritative, or portable across arbitrary future hardware unless repository evidence supports the claim.
- Use the repository status vocabulary consistently:
  - `DOCUMENTED_ONLY` — specification exists, no runtime claim;
  - `EXPERIMENTAL` — runnable or testable mechanism under evaluation;
  - `PROPOSED` — suggested change without approval;
  - `APPROVED` — accepted only after explicit maintainer/operator decision.

## Architecture terminology

- Preserve the distinction between Architecture Canon, Abstract Contracts, and Implementation Profiles.
- Preserve the distinction between Claim, Event, projection, epistemic state, charge, context selection, and Receipt.
- Treat append-only event history as authoritative about recorded history, not automatically equivalent to truth.
- Treat SQLite, graph, FTS, vector stores, Python, model APIs, and conventional hardware as replaceable implementation choices.
- Do not allow backend-generated identifiers, database schemas, embeddings, graph nodes, model APIs, runtimes, or processor assumptions to become semantic identity by accident.
- Keep truth status separate from relevance, utility, frequency, freshness, write order, and task selection.
- Use `evidence grip` in lowercase. Do not claim genuine sufficiency or global minimality for lexical proxy ablation.
- Distinguish candidate conflicts from established conflicts and detection from resolution.
- Treat future neuromorphic, photonic, analog, non-binary, or other substrates as research possibilities, not implementation evidence.

## State Checkpoints and conflicts

- Treat State Checkpoints as `PROPOSED` and `NOT IMPLEMENTED` unless repository code and tests prove otherwise.
- Distinguish State Checkpoint, Read Snapshot, Evaluation Snapshot, Claim freshness, and replay completeness.
- Do not prescribe checkpoint frequency, retention, SQLite schema, or Claim-per-stream as Architecture Canon.
- Do not describe OCC, durable command idempotency, CRDT policy, multi-writer merge, or a conflict-resolution API as implemented.
- Preserve the principle that write order may define deterministic order but must not independently determine semantic truth.
- Do not add new conflict event verbs to the `v0.1.2.1` controlled import.

## Architecture Decision Records

- Major Canon, contract, event-vocabulary, checkpoint, conflict, portability, and integration-boundary changes require an ADR.
- Keep three dimensions separate:
  - decision status: `PROPOSED | ACCEPTED | REJECTED | DEPRECATED | SUPERSEDED`;
  - evidence level: `DOCUMENTED | EXTERNALLY_OBSERVED | LOCALLY_TESTED | REPOSITORY_REPRODUCED | SHADOW_EVALUATED | OPERATOR_APPROVED`;
  - implementation status: `NOT_STARTED | PARTIAL | COMPLETE`.
- An `ACCEPTED` ADR does not automatically mean runtime code exists.
- A `PROPOSED` ADR must not be summarized as accepted or implemented.
- Multi-model agreement may be listed as an input, never as approval or implementation evidence.

## Titan and Crystal boundary

- Native Kernel is an independent research project.
- Titan is a future evaluation environment, not an active integration target by default and not merely a projection layer.
- Crystal is an independent grant-facing product and must not be described as dependent on Native Kernel.
- Do not introduce direct Native Kernel writes into Crystal Canon.
- Do not insert Crystal TruthGate as a Native Kernel dependency during the controlled import.
- Any transfer to Crystal requires a separate RFC, threat model, tests, reproducible evaluation, review, rollback, and explicit maintainer approval.

## Bilingual documentation

- `README.md` is the English overview and `README.ru.md` is the Russian overview.
- Keep a visible `English · Русский` selector near the top and bottom of both files.
- Keep both READMEs semantically aligned.
- Translation may adapt wording, but must preserve status, maturity, test counts, benchmark boundaries, security limitations, ADR statuses, and Titan/Crystal integration claims.
- When changing a substantive README section, update the corresponding section in the other language in the same PR or explicitly record the temporary translation gap.

## Documentation style

- Keep technical meaning exact and avoid hype.
- Use clear visual hierarchy in public-facing Markdown: concise headings, selective emojis, tables, Mermaid or ASCII diagrams where they improve comprehension, and direct navigation links.
- Do not remove status warnings or maturity boundaries for visual polish.
- Prefer one canonical term over near-synonyms across README, README.ru, STATUS, ROADMAP, ARCHITECTURE, ADRs, and CONTRIBUTING.
- Benchmark claims must state whether results are external, locally reproduced, or reproduced in repository CI.
- Make clear that modern technologies are accepted as laboratory tools; technology independence does not mean rejecting current systems.

## Change discipline

- Keep controlled prototype import separate from semantic redesign.
- Do not silently rewrite the `v0.1.2.1` baseline during import.
- Long-horizon architecture documentation may evolve without changing the imported prototype baseline.
- Update `STATUS.md` implementation claims only after the corresponding code, tests, commands, and CI evidence exist in the repository.
- Operator or maintainer approval is required before a proposal is represented as accepted architecture.
