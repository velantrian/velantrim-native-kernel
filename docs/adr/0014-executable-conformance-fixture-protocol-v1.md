# ADR-0014: Executable conformance fixture protocol v1

- **Decision status:** `ACCEPTED`
- **Evidence level:** `LOCALLY_TESTED`
- **Implementation status:** `PARTIAL` fixture tooling implemented; Kernel runtime unsupported
- **Operator approval:** `APPROVED`
- **Date:** `2026-08-06`
- **Deciders:** `@velantrian`
- **Track:** `Abstract Contract / NK-EQV`
- **Related:** Issue #17, ADR-0004, ADR-0010

## Context

C0–C5 and assertion families existed only in prose. Missing mappings could be silently skipped and “equivalent” remained too easy to use without a definition.

## Decision

Adopt `nk-fixtures/1.0` with a machine-readable registry, versioned schemas/fixtures, explicit byte/structural/semantic/behavioural equivalence, positive and negative epistemic scenarios, machine-readable evidence reports and an external adapter protocol. Unsupported assertions and failures must remain visible.

The operator approved this architectural contract on 2026-08-06. Approval accepts the fixture/evidence protocol; it does not certify a Kernel implementation or change the evidence level of the existing Python fixture reader.

## Evidence boundary

The included Python tool validates fixture integrity only and reports Kernel runtime conformance as `UNSUPPORTED`. It cannot establish C2 until committed repository execution reproduces the declared scope and cannot establish C3 without two materially independent profiles.

## Consequences

Contract evolution gains an accepted executable review surface. Runtime conformance remains assertion-scoped and must cite exact commits, commands, environments, profile mappings and limitations.

## Evidence and promotion gates

- operator decision: `APPROVED`;
- fixture runner and focused tests: `LOCALLY_TESTED`;
- GitHub Actions workflow definition: active;
- repository workflow execution: not yet recorded;
- Kernel implementation adapter: absent;
- C3 requires two materially independent profiles and comparison evidence.
