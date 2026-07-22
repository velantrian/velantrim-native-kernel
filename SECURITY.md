# Security Policy

## Research-stage warning

Velantrim Native Kernel is an experimental research project. It has not received a production security audit and must not be used to store sensitive, regulated, safety-critical, or irreplaceable data.

Known security limitations include:

- incomplete event-envelope integrity;
- no complete multi-writer threat model;
- no production authentication or authorization layer;
- no encrypted storage layer;
- incomplete command idempotency;
- no production backup and recovery contract;
- append-only research semantics that require further work for legal erasure and restriction;
- no guarantee that current selection heuristics expose all relevant conflicts or omissions.

## Reporting

Do not disclose exploitable security issues publicly before maintainers have had a reasonable opportunity to investigate. Use GitHub's private security advisory mechanism when available, or contact the repository owner privately.

A useful report should include:

- affected commit;
- reproduction steps;
- expected and observed behaviour;
- impact;
- proposed mitigation, when known.

## Supported versions

No version is currently production-supported. Security fixes may be applied only to the latest research branch or `main`.

## Scope boundary

This repository is not a security authority for Titan or Crystal. Any future integration requires a separate threat model, privacy analysis, rollback design, and implementation review in the target repository.