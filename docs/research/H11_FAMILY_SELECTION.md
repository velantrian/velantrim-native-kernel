# A10-H11 Family Selection Candidate

Status: `CANDIDATE_SELECTION / PREREGISTRATION_NOT_YET_AUTHORIZED`

Protocol: `nk-residual-family-selection/1`  
Selection ID: `RFS-001-a10-h11-preregistration-selection-v1`  
Source current-truth checkpoint: `eeddda7382558f939f9bddb19ab80dd8dfbdbee4`  
Source plan: `RAVP-001-residual-a10-validation-plan-v1` / merge `edc0501d71a827462aafd1ac4497920a719a4519`

## Selected family

`A10-H11` / `RAVP-H11-LAB-CANON-SEPARATION`

> Laboratory mechanisms can remain reproducible without becoming Architecture Canon.

This candidate selects H11 for the **next preregistration gate only**. It does not preregister H11, implement an experiment, execute an experiment, change an A10 outcome, promote Final Canon, or thaw runtime.

## Why H11 first

RAVP-001 ranks H11 first because it has the lowest execution burden and protects all later residual families from profile-to-Canon leakage. That rationale is accepted as the bounded selection basis here. The order is not evidence that H11 is supported.

H11 is strategically first because later H03/H10/H06/H09/H08 work may introduce new migration, storage, computation, erasure, probabilistic, or physical mechanisms. The H11 boundary must prevent those laboratory/profile mechanisms from silently becoming universal Architecture obligations merely because they are required to reproduce a particular experiment.

## Exact H11 question preserved from RAVP-001

Can exact reproduction of accepted laboratory evidence depend on profile-specific Python/SQL/JSON/hash/Event/reducer details while the Architecture specification and conformance oracle remain meaning-level and do not mandate those mechanisms universally?

Required independence axis: `INDEPENDENT_SEMANTIC_ORACLE`.

Strengthening axes:

- `INDEPENDENT_TEAM`
- `INDEPENDENT_CUSTODY`
- `INDEPENDENT_IMPLEMENTATION_STRUCTURE`

## Mandatory preregistration content

A later, separate H11 preregistration must freeze at least:

- experiment identity;
- historical laboratory checkpoint and evidence identity;
- exact laboratory reproduction manifest;
- Architecture obligation inventory;
- mechanism dependency graph;
- frozen mechanism-leakage rubric;
- externally visible observables;
- equivalence predicate and allowed losses;
- failure conditions and hard refutation;
- grounding mode and threat/trust model;
- semantic-oracle authority;
- reviewer/reproducer independence basis;
- reproduction requirements;
- allowed A10 outcome vocabulary.

## Fail-closed authority boundary

```text
family selection ≠ family preregistration
family preregistration ≠ execution admission
execution admission ≠ execution
laboratory reproducibility ≠ Architecture Canon
A10-H11 ≠ composition/federation
```

This candidate package self-declares:

```text
preregistration_authorized_by_this_package: false
experiment_implementation_authorized: false
experiment_execution_authorized: false
runtime_expansion: FROZEN
product_runtime_thaw: false
Final Canon: DEFERRED / NOT_AUTHORIZED
production_authorized: false
```

Composition/federation remains the separate D7-F08 capability class. H03/H06/H08/H09/H10 remain unselected and `NOT_TESTED`.

If this candidate is accepted and bound into a later current-truth checkpoint, the next gate becomes `A10_H11_FAMILY_PREREGISTRATION`. That later gate must remain preregistration-only until a further separate execution-admission decision.
