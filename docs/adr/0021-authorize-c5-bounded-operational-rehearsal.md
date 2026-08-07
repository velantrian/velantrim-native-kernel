# ADR-0021 — Authorize C5 bounded operational validation rehearsal

- **Status:** ACCEPTED
- **Operator approval:** APPROVED
- **Date:** 2026-08-07
- **Issue:** #64
- **Base main:** `d1dd4986a8496cd9ca3e353d33ca422038c65d40`

## Context

P1–P5 and C4 now provide two partial implementation profiles, assertion-scoped C2/C3 evidence and an authority-free offline shadow evaluation. They do not establish operational behaviour under a deployment envelope.

The next evidence question is deliberately narrower than production readiness:

```text
Can the current profiles execute a controlled synthetic operational rehearsal
with explicit security, privacy, rollback, recovery, incident and bounded-load evidence
without changing semantic assertion support or granting production authority?
```

## Decision

Authorize C5 only as a **bounded operational rehearsal** in ephemeral CI.

Accepted evidence protocols:

```text
nk-operational-plan/1
nk-operational-report/1
nk-operational-receipt/1
```

Approved plan:

```text
plan_id: native-kernel/c5-bounded-rehearsal-v1
deployment_class: CI_EPHEMERAL_SYNTHETIC
scenarios: 18
prerequisite: exact passing nk-shadow-report/1
```

C5 must preserve the existing semantic boundary:

```text
operational_validation: C5_BOUNDED_REHEARSAL
kernel_runtime_conformance: C4
support_state: PARTIAL
assertion map: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
```

## Required operational categories

- application-level authority denial and writer fencing;
- idempotent retry and bounded synthetic load;
- transaction rollback after injected faults;
- deterministic replay and disposable projection rebuild;
- application-level logical backup, quarantined restore and replay verification;
- stored-corruption detection and bounded incident timeline;
- synthetic-only enforcement and canary redaction.

## Mandatory boundary

```text
live_user_data: false
production_traffic: false
network_api_exposed: false
authority_promotion: false
authoritative_external_side_effects: false
ecosystem_wiring: false
physical_deletion_claimed: false
compliance_certification_claimed: false
```

## Consequences

A passing C5 report means only that the exact approved synthetic plan passed in the exact recorded ephemeral environments.

It does not establish:

- production readiness or live-traffic safety;
- cloud IAM or network perimeter security;
- multi-region HA, managed-provider DR or exhaustive scale;
- operational equivalence between PostgreSQL and SQLite;
- physical or cryptographic deletion;
- privacy/security/compliance certification;
- truth, external authenticity or Byzantine protection;
- automatic authority promotion or ecosystem wiring.

Any production, live-data, physical-deletion or ecosystem phase requires a new explicit operator decision.
