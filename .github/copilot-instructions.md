# GitHub Copilot instructions for Velantrim Native Kernel

## Project status discipline

- Treat this repository as `RESEARCH / DOCUMENTED_ONLY / NOT PRODUCTION-READY` until `STATUS.md` is explicitly changed by a reviewed implementation PR.
- Do not describe the project as runnable, production-ready, secure, complete, generally linear, sufficient, conscious, autonomous, or truth-authoritative unless repository evidence supports the claim.
- Use the repository status vocabulary consistently:
  - `DOCUMENTED_ONLY` — specification exists, no runtime claim;
  - `EXPERIMENTAL` — runnable or testable mechanism under evaluation;
  - `PROPOSED` — suggested change without approval;
  - `APPROVED` — accepted only after explicit maintainer/operator decision.

## Architecture terminology

- Preserve the distinction between Claim, Event, projection, epistemic state, charge, context selection, and Receipt.
- Treat the append-only event history as the intended authority and SQLite, graph, FTS, and vector stores as replaceable projections.
- Keep truth status separate from relevance, utility, frequency, and task selection.
- Use `evidence grip` in lowercase. Do not claim genuine sufficiency or global minimality for lexical proxy ablation.
- Distinguish candidate conflicts from canonical conflicts and detection from resolution.

## Titan and Crystal boundary

- Native Kernel is an independent research project.
- Titan is a future evaluation environment, not an active integration target by default.
- Crystal is an independent grant-facing product and must not be described as dependent on Native Kernel.
- Do not introduce direct Native Kernel writes into Crystal Canon.
- Any transfer to Crystal requires a separate RFC, threat model, tests, reproducible evaluation, review, and explicit maintainer approval.

## Documentation style

- Keep technical meaning exact and avoid hype.
- Use clear visual hierarchy in public-facing Markdown: concise headings, selective emojis, tables, Mermaid or ASCII diagrams where they improve comprehension, and direct navigation links.
- Do not remove status warnings or maturity boundaries for visual polish.
- Prefer one canonical term over near-synonyms across README, STATUS, ROADMAP, and CONTRIBUTING.
- Benchmark claims must state whether results are external, locally reproduced, or reproduced in repository CI.

## Change discipline

- Keep controlled prototype import separate from semantic redesign.
- Do not silently rewrite the `v0.1.2.1` baseline during import.
- Update `STATUS.md` only after the corresponding code, tests, commands, and CI evidence exist in the repository.
- Operator or maintainer approval is required before a proposal is represented as accepted architecture.
