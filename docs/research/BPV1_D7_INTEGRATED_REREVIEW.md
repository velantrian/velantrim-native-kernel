# BPV1-001 D7 — Integrated Re-review

**State:** `CANDIDATE / AUTHORITATIVE AFTER MERGE`  
**Protocol:** `nk-integrated-post-bpv1-rereview/1`  
**Review ID:** `BPV1-001-D7-integrated-rereview-v1`  
**Input checkpoint:** `030d0a0585bd061b27329a38e29708c11304701a`  
**Review kind:** `INTEGRATED_RE_REVIEW / NOT_INDEPENDENT_VALIDATION`  
**Runtime expansion:** `FROZEN`

## Purpose

D7 re-reads the provisional Native Kernel architecture after the full Option D evidence chain now available in GitHub:

```text
A1–A10 provisional blueprint
→ integrated review IR-F01..IR-F07
→ IAR-1 independent challenge
→ IAR-1-R1 reconciliation
→ frozen BPV1-001 plan and admission
→ D5 execution
→ D5-R1 external evidence qualification
→ D6 A10 hypothesis classification
→ this D7 integrated re-review
```

This is an integrated project review, not an independent validation event. It cannot promote Final Canon, thaw product runtime, authorize production, decide Issue #18, decide Issue #74/ADR-0024, or admit Track H sources.

## Evidence position entering D7

D6 classified all twelve A10 hypotheses without propagating the aggregate evaluator result mechanically:

```text
SUPPORTED_FOR_SCOPE
  H01 H02 H04 H05 H07 H12

NOT_TESTED
  H03 H06 H08 H09 H10 H11

WEAKENED      0
REFUTED       0
INDETERMINATE 0
```

The underlying D5-R1 evidence remains `QUALIFIED`; the unchanged frozen evaluator returned `SUPPORTED_FOR_SCOPE` with 12/12 mandatory fixtures PASS.

## Integrated conclusion

The architecture is **stronger than it was before BPV1-001**, but it is still provisional.

The strongest justified statement is:

> Selected semantic obligations survived one materially different, bounded, conventional-digital realization under a frozen external evaluation protocol.

This is materially stronger than merely showing PostgreSQL↔SQLite variation inside one Python lineage. It is still much narrower than arbitrary-substrate portability.

## Findings

### D7-F01 — Evidence-backed semantic core strengthened

**Status:** `CONFIRMED_FOR_SCOPE`.

H01, H02, H04, H05, H07 and H12 survived the qualified BPV1-001 run. In particular, the realization did not require the current Event/reducer/Receipt/SQL shape as its semantic form, preserved Unknown/plurality/scoped uncertainty, preserved bounded revision accountability, and supported loss-aware conformance.

**Effect:** retain these obligations in the provisional architecture, but keep the evidence qualifier `SUPPORTED_FOR_SCOPE`.

### D7-F02 — Representation migration continuity remains open

**Basis:** `A10-H03 = NOT_TESTED`.

BPV1-001 did not perform a source→target representation migration whose identity and continuation relations were adjudicated across the migration.

**Effect:** no claim that arbitrary representation migration preserves semantic identity.

### D7-F03 — Physical and cryptographic erasure remain open

**Basis:** `A10-H06 = NOT_TESTED`.

Physical and cryptographic erasure were outside BPV1-001 applicability. Logical loss, compaction and retained-scope witnesses are not substitutes for physical-residue or key-destruction evidence.

**Effect:** preserve separate erasure claims and their evidence boundaries.

### D7-F04 — Analog/neuromorphic/probabilistic substrate classes remain untested

**Basis:** `A10-H08 = NOT_TESTED`, `A10-H09 = NOT_TESTED`.

BPV1-001 is conventional digital computation. It says nothing conclusive about non-address-based dynamical continuity or statistical conformance on probabilistic substrates.

**Effect:** future-substrate language remains a research hypothesis, not demonstrated support.

### D7-F05 — Storage and computation independence were not isolated

**Basis:** `A10-H10 = NOT_TESTED`.

The BPV1 realization varied language, history model and representation together. That is useful cross-lineage evidence but does not isolate storage and computation axes independently.

**Effect:** do not infer independent substitutability of those axes from this run.

### D7-F06 — Laboratory/Canon governance boundary preserved, but not experimentally adjudicated by BPV1

**Basis:** `A10-H11 = NOT_TESTED` plus the continuing `BOUNDED_REFERENCE_LABORATORY` role.

The project continues to keep P1–C5 and the Rust experiment outside Canon. That governance discipline is real repository evidence, but BPV1-001 did not preregister H11 as a falsification target.

**Effect:** preserve prior governance evidence without calling it BPV1 substrate evidence.

### D7-F07 — H07 support is not independent implementation validation

The Rust subject is a different implementation language/history model, but it remains same-repository custody and was not produced by an independent implementation team. The computation model remains conventional digital.

**Effect:** H07 remains `SUPPORTED_FOR_SCOPE`; independent team, custody and computation-model validation remain `NOT_ESTABLISHED`.

### D7-F08 — Composition/federation remains a separate capability class

BPV1-001 was single-node. IAR-1-R1 already established that local conformance does not imply composition/federation conformance.

**Effect:** no BPV1 result may be promoted to federated/composed conformance.

### D7-F09 — No automatic Canon or runtime authority

D5 and D6 strengthened research evidence only.

```text
P1-C5 role:             BOUNDED_REFERENCE_LABORATORY
Rust subject role:      FALSIFICATION_INSTRUMENT_ONLY
runtime expansion:      FROZEN
product runtime thaw:   NO
production:             false
Final Canon:            NOT AUTHORIZED
```

### D7-F10 — Refined provisional substrate-independence statement

D7 adopts the following wording for D8 synchronization:

> Native Kernel now has qualified evidence that selected semantic obligations can survive one materially different bounded conventional-digital realization without adopting the current reference laboratory's native Event/reducer/Receipt/SQL form. Six A10 hypotheses remain not tested, so arbitrary future-substrate portability remains unproved.

This wording is stronger than the pre-BPV evidence position and weaker than a universal claim.

## Architecture assessment after D7

```text
internal semantic coherence:               no known blocking contradiction in reviewed evidence-backed scope
selected semantic obligations:             strengthened for BPV1 scope
A1-A10 status:                              PROVISIONAL
Final Canon:                                NO
universal substrate independence:          NOT PROVEN
independent implementation validation:     NOT ESTABLISHED
independent computation-model evidence:    NOT ESTABLISHED
composition/federation conformance:         NOT TESTED
physical/cryptographic erasure:             NOT TESTED by BPV1
runtime thaw:                               NO
production:                                 false
```

## What D7 does not rewrite

D7 does not edit or reinterpret the bytes of:

- A1–A10 first drafts;
- the first integrated review;
- IAR-1 source findings;
- IAR-1-R1 publication-time reconciliation;
- the frozen BPV1 plan/oracle/thresholds/HR01-HR10;
- D5/D5-R1 evidence;
- D6 classification.

Those remain separate provenance layers.

## Next gate

The appropriate next bounded gate is:

```text
D8_CONSOLIDATED_AUTHORITATIVE_SYNC
```

D8 may synchronize the confirmed Option D result into the existing Native Kernel Notion surfaces and current GitHub truth surfaces. It must preserve GitHub as technical authority, keep historical checkpoints distinct, and record both the strengthened evidence and the six untested A10 hypotheses.

A later Canon/runtime decision remains a **separate operator decision after D8**. D7 does not make that decision.
