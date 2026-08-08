# 🤖 Velantrim Native Kernel repository guidance

## Required reading

1. `README.md`
2. `STATUS.md`
3. `project-state.json`
4. `docs/ai/README.md`
5. `docs/ai/CURRENT_STATE.md`
6. `docs/ai/C5_IMPLEMENTATION_RECORD.md`
7. `evidence/c5/README.md`
8. affected contracts/source/tests/workflows
9. `docs/ai/KNOWN_RISKS.md`

## Current maturity

```text
RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
kernel_runtime_conformance: C4
operational_validation: C5_BOUNDED_REHEARSAL
support_state: PARTIAL
assertions: 45 / 10 / 17 / 0
NK-EPI: 0 / 8 SUPPORTED
```

## Three independent tracks

```text
H — historical recovery
v0.1.2.1 + original 44-test suite
OPEN / BLOCKED / independent from clean implementation

C — clean implementation
P1–P5 + C4 + C5
ACTIVE / PARTIAL

R — long-horizon research
PROPOSED / BOUNDED / no automatic promotion
```

Never collapse these tracks.

## Required distinctions

```text
Architecture Canon ≠ implementation profile
historical recovery ≠ clean implementation
research proposal ≠ accepted contract ≠ runtime
C2 ≠ C3 ≠ C4 ≠ C5
C5 operational rehearsal ≠ semantic assertion promotion
synthetic CI ≠ live production
logical Event export ≠ physical backup/DR
Receipt/report ≠ truth, compliance or deletion proof
retained artifact bytes ≠ broader proof than the producing run
```

## C5 plan and durable evidence

```text
plan: native-kernel/c5-bounded-rehearsal-v1
sha256: 4ed680ff4e83ac9d1aca6c1ab8a435ecb19af4a5badf1be8202bc842f964b098
scenarios: 18
deployment: CI_EPHEMERAL_SYNTHETIC
durable bundle: evidence/c5/2026-08-07/manifest.json
```

Never change plan scenarios or thresholds under the same plan identity/digest. Never rewrite archived ZIPs under the same evidence bundle identity.

## Forbidden claims/actions

- production readiness or deployment;
- live user traffic or real personal data;
- cloud IAM, multi-region HA or compliance certification;
- physical/cryptographic deletion;
- automatic authority promotion or external side effects;
- Titan, Mentaury or Crystal wiring;
- support for all 72 assertions;
- any `NK-EPI` promotion without executable evidence and a separate decision;
- historical `v0.1.2.1` recovery or global-loss claim;
- promoting a research note into Canon or runtime through wording alone.

## Verification

The SQLite WAL profile fails closed below linked SQLite 3.51.3. On Linux, build the pinned library before SQLite/P5/C3/C4/C5 checks:

```bash
tools/sqlite/build_safe_sqlite.sh /tmp/native-kernel-sqlite-3.51.3 /usr/bin/python3
export LD_LIBRARY_PATH=/tmp/native-kernel-sqlite-3.51.3/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
python -c 'from native_kernel.sqlite_profile import linked_sqlite_version; print(linked_sqlite_version())'
```

```bash
python tools/evidence/verify_bundle.py evidence/c5/2026-08-07/manifest.json
python tools/ai_context/validate_project_state.py --repo .
python -m unittest discover -s tests -p 'test_evidence_bundle.py' -v
python -m unittest discover -s tests -p 'test_project_state.py' -v
python -m unittest discover -s tests -p 'test_c5_operational_validation.py' -v
python -m unittest discover -s tests -p 'test_c5_report_validator.py' -v
python -m unittest discover -s tests -p 'test_c5_manifest.py' -v
python tools/profiles/validate_c5_manifest.py
python -m unittest discover -s tests -p 'test_ai_context_validator.py' -v
python tools/ai_context/validate_context.py --repo .
```

Repository C5 additionally requires the four-job matrix, exact P4/P5/C3/C4 prerequisites, 18/18 scenarios, 18 Receipts and zero canary/recovery/incident failures.

## Documentation synchronization

Material work must update `STATUS.md`, project state, current state, implementation records, risks, component map, work log, public README and Notion. GitHub must remain sufficient without Notion.
