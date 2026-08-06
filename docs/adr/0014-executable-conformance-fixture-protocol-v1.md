# ADR-0014: Executable conformance fixture protocol v1

- **Decision status:** `PROPOSED`
- **Evidence level:** `LOCALLY_TESTED`
- **Implementation status:** `PARTIAL` fixture tooling implemented; Kernel runtime unsupported
- **Operator approval:** `PENDING`
- **Date:** `2026-08-06`
- **Related:** Issue #17, ADR-0004, ADR-0010

## Context

C0–C5 and assertion families existed only in prose. Missing mappings could be silently skipped and “equivalent” remained too easy to use without a definition.

## Decision proposal

Adopt a machine-readable registry, versioned schemas/fixtures, explicit byte/structural/semantic/behavioural equivalence, positive and negative epistemic scenarios, machine-readable evidence reports and an external adapter protocol. Unsupported assertions and failures must remain visible.

## Evidence boundary

The included Python tool validates fixture integrity only and reports Kernel runtime conformance as `UNSUPPORTED`. It cannot establish C2 until CI reproduces it and cannot establish C3 without two materially independent profiles.

## Consequences

Contract evolution gains executable review surfaces. Runtime conformance remains assertion-scoped and must cite exact commits, commands, environment and limits.
