# BPV1-001 D5-R1 Evidence Qualification

Status: **CANDIDATE / NOT AUTHORITATIVE UNTIL PR MERGE + POST-MERGE CI**  
Scope: BPV1-001 only  
Historical D5 merge: `a191e9c868c14af34a269dcdfae44406f1013bda`  
Frozen plan merge: `a538d7f1e28858a88b9ee777ac7d6e05b85943db`  
Frozen plan SHA-256: `7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0`

## Why D5-R1 exists

PR #114 mechanically completed D5 and produced `SUPPORTED_FOR_SCOPE`, but a post-merge audit found four qualification weaknesses that should be corrected before D6 uses the result to classify A10 hypotheses:

1. repository current-truth surfaces still described BPV1 subject execution as the next gate;
2. several structural oracle-facing booleans were emitted directly by the Rust subject, which created an HR10 self-report concern even though separate static tests existed;
3. the local corruption digest omitted `evidence` and `epistemic_position`;
4. detailed `loss_witnesses` storage had no intrinsic retained-record bound.

D5-R1 is a bounded corrective/qualification pass. It does **not** change the preregistered experiment semantics or reinterpret a failed result.

## Frozen authorities remain unchanged

D5-R1 must not edit:

- `docs/research/BPV1_PREREGISTRATION.{json,md,ru.md}`;
- `experiments/bpv1/BPV1-001/admission/**`;
- `tools/bpv1/evaluate.py`;
- scenario identity, target hypotheses, HR01-HR10, expected fixture outcomes, or thresholds.

The CI scope guard fails closed if these paths change.

## Corrected evidence path

```text
Rust subject
  -> raw implementation-neutral facts
  -> external qualifier (no frozen expected outcomes)
  -> nk-bpv1-observations/1
  -> unchanged frozen evaluator + fixture oracle
  -> outcome
```

The Rust subject no longer emits the structural pass-oriented values used by the oracle for `authoritative_per_operation_append_log`, `exact_replay_required`, or current-lineage reuse. The external qualifier derives those facts from repository source structure and emits them only when established. If the required facts cannot be established, the corresponding frozen observables remain absent and the unchanged evaluator can become `INDETERMINATE` rather than receiving a fabricated `false`.

The qualifier records:

- `oracle_fixture_expectations_read: false`;
- `implementation_private_runtime_state_read: false`;
- `subject_self_report_used_for_structural_oracle_fields: false`.

This removes the specific D5 self-report path that triggered the HR10 qualification concern. It does not create independent-team or independent-custody evidence.

## FX07 integrity strengthening

The subject's local corruption digest now covers the materially relevant claim fields used by this experiment, including the evidence list and epistemic position. Additional Rust tests mutate each of those fields without updating the digest and require corruption detection.

These additional tests strengthen the implementation measurement path. The preregistered FX07 expected semantics are unchanged.

## Bounded loss-witness storage

Retained detailed loss witnesses are bounded to 32 records. If a future run would exceed the retained-record cap, older detailed witnesses are folded into one bounded per-slot rollup containing aggregate count, witness range, per-slot compacted count, and first/last compacted version range. The mechanism does not silently drop the existence or declared boundary of older loss and does not replace the witness list with another per-operation unbounded log.

A separate 96-cycle engineering stress test exercises this mechanism beyond the preregistered 16-cycle workload. The stress test is **not** part of BPV1-001 adjudication and does not alter its frozen workload or thresholds.

## Qualification run before evidence preservation

Exact head `5433ec0e56a2882ddfdd44e1d131cdca1ee1a082` was used to validate the corrected path before preserving the D5-R1 evidence bundle.

- AI context integrity: run `31549755468` — SUCCESS;
- BPV1 execution admission: run `31549755493` — SUCCESS;
- BPV1 subject falsification instrument: run `31549755461` — SUCCESS;
- Python 3.11 job `93969695483` — SUCCESS;
- Python 3.12 job `93969695477` — SUCCESS;
- external qualification: `QUALIFIED`;
- unchanged frozen evaluator: `SUPPORTED_FOR_SCOPE`;
- mandatory fixtures: `12/12 PASS`;
- workload: 512 mutations; checkpoints 128/256/512; 52 retained detailed predecessors; 13 retained witness records; 42,276 durable bytes at mutation 512; growth rule PASS.

An earlier candidate head produced the same `QUALIFIED` / `SUPPORTED_FOR_SCOPE` semantic result but the workflow failed a brittle meta-test that rejected the literal text `evaluate.py` in a documentation string. That test was corrected to inspect actual Python imports/dependencies; no preregistration, oracle, fixture, or experiment semantic was changed.

## Repository evidence identity

The D5-R1 candidate evidence is stored separately under:

`experiments/bpv1/BPV1-001/results/d5-r1/`

The historical PR #114 evidence files remain preserved unchanged.

## Non-claims and next gate

This qualification does not establish Final Canon, production readiness, universal substrate portability, independent team/custody, or an independent computation model. Rust remains `EXPERIMENTAL_INSTRUMENT_NOT_CANON`. Product runtime integration is not authorized; runtime expansion remains `FROZEN`.

D6 A10 hypothesis classification must remain **NOT STARTED** until this D5-R1 package is merged, post-merge CI is green, late review is checked, and a separate current-truth checkpoint binds the authoritative D5-R1 merge.
