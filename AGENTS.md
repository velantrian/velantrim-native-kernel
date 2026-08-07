# 🤖 Velantrim Native Kernel repository guidance

## Required reading

1. `README.md`
2. `STATUS.md`
3. `docs/ai/README.md`
4. `docs/ai/CURRENT_STATE.md`
5. `docs/ai/C5_IMPLEMENTATION_RECORD.md`
6. affected contracts/source/tests/workflows
7. `docs/ai/KNOWN_RISKS.md`

## Current maturity

```text
RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
kernel_runtime_conformance: C4
operational_validation: C5_BOUNDED_REHEARSAL
support_state: PARTIAL
assertions: 45 / 10 / 17 / 0
```

## Required distinctions

```text
Architecture Canon ≠ implementation profile
C2 ≠ C3 ≠ C4 ≠ C5
C5 operational rehearsal ≠ semantic assertion promotion
synthetic CI ≠ live production
logical Event export ≠ physical backup/DR
Receipt/report ≠ truth, compliance or deletion proof
```

## C5 plan boundary

```text
plan: native-kernel/c5-bounded-rehearsal-v1
sha256: 4ed680ff4e83ac9d1aca6c1ab8a435ecb19af4a5badf1be8202bc842f964b098
scenarios: 18
deployment: CI_EPHEMERAL_SYNTHETIC
```

Never change plan scenarios or thresholds under the same plan identity/digest. A material change requires a new version, ADR/manifest update and full evidence cycle.

## Forbidden C5 claims/actions

- production readiness or deployment;
- live user traffic or real personal data;
- cloud IAM, multi-region HA or compliance certification;
- physical/cryptographic deletion;
- automatic authority promotion or external side effects;
- Titan, Mentaury or Crystal wiring;
- support for all 72 assertions;
- historical `v0.1.2.1` recovery.

## Verification

```bash
python -m unittest discover -s tests -p 'test_c5_operational_validation.py' -v
python -m unittest discover -s tests -p 'test_c5_report_validator.py' -v
python -m unittest discover -s tests -p 'test_c5_manifest.py' -v
python tools/profiles/validate_c5_manifest.py
python -m unittest discover -s tests -p 'test_ai_context_validator.py' -v
python tools/ai_context/validate_context.py --repo .
```

Repository C5 additionally requires all four matrix jobs, exact P4/P5/C3/C4 prerequisites, 18/18 scenario PASS, 18 Receipts, zero canary/recovery/incident failures and retained six-report artifacts.

## Documentation synchronization

Material work must update `STATUS.md`, current state, C5 record, risks, component map, work log, public README and Notion. GitHub must remain sufficient without Notion.
