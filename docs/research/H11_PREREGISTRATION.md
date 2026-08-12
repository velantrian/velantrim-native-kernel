# A10-H11 Preregistration — Laboratory / Canon Separation

**Protocol:** `nk-h11-preregistration/1`  
**Plan ID:** `H11-001-c5-lab-canon-separation-v1`  
**State:** `PREREGISTERED / EXECUTION_NOT_AUTHORIZED`  
**Target:** `A10-H11` / `RAVP-H11-LAB-CANON-SEPARATION`  
**Selection merge:** `bcd3b3f6c9d898315c93e5d24b5d0e02c95508cc` / PR #126  
**Runtime:** `FROZEN`

## Question

Can exact reproduction of accepted laboratory evidence depend on profile-specific Python/SQL/JSON/hash/Event/reducer details while the Architecture specification and semantic oracle remain meaning-level and do not mandate those mechanisms universally?

This preregistration does not claim that H11 is supported. `A10-H11` remains `NOT_TESTED` until a separately admitted execution and independent semantic adjudication complete.

## Frozen laboratory subject

The exact laboratory artifact is the repository-resident ADR-0023 C5 evidence bundle:

```text
bundle_id: native-kernel/c5/2026-08-08-adr0023
manifest: evidence/c5/2026-08-08-adr0023/manifest.json
protocol: nk-evidence-bundle/1
plan: native-kernel/c5-bounded-rehearsal-v1
checkpoints: 2
artifacts: 8 ZIPs
SQLite evidence floor: 3.51.3
```

The existing fail-closed verifier is:

```text
python tools/evidence/verify_bundle.py evidence/c5/2026-08-08-adr0023/manifest.json --repo .
```

Exact bytes, ZIP inventories, sizes, SHA-256 digests, environment snapshots, metrics and checkpoint identities are **laboratory reproduction requirements only**. Their exactness does not make Python, PostgreSQL, SQLite, SQL, JSON, ZIP, SHA-256, Event, reducer, Receipt, integer sequences or current report schemas Architecture Canon.

## Frozen H11 obligations

- `H11-O01` — laboratory evidence/profile mechanisms remain distinguishable from Architecture authority.
- `H11-O02` — semantic obligations remain separable from their current realization mechanisms.
- `H11-O03` — historical evidence identity remains reproducible without rewriting Architecture history or prior evidence scope.
- `H11-O04` — Architecture falsification/conformance remains expressible at meaning level without current profile bytes becoming mandatory oracle input solely because the historical lab needs them.

## Dependency graph and leakage rubric

The execution must construct a complete graph containing Architecture obligations, laboratory evidence, profile mechanisms and validator/oracle nodes. Concrete dependencies are classified as:

- `LAB_ONLY` — required only to reproduce the named historical lab artifact;
- `PROFILE_SPECIFIC` — valid profile realization, not Architecture authority;
- `MEANING_LEVEL_JUSTIFIED` — requirement is expressed independently of a concrete mechanism;
- `UNJUSTIFIED_CANON_DEPENDENCY` — a concrete lab/profile mechanism becomes mandatory Architecture solely because historical lab reproduction requires it.

`UNJUSTIFIED_CANON_DEPENDENCY` is the hard failure class. Support requires `mandatory_profile_leakage_count == 0` and mechanism-neutral Architecture obligations/falsifiers.

## Independence gate

H11 requires `INDEPENDENT_SEMANTIC_ORACLE`. Architecture/preregistration authors may **not self-certify H11**.

Before execution admission, a qualifying reviewer/reproducer must have a concrete, disclosed independence basis and must not have authored this preregistration or its frozen leakage rubric. If no qualifying reviewer/reproducer is available, the correct gate result is:

`BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER`

That blocker is not an H11 refutation and must not be converted into fabricated validation.

## Frozen adjudication

- `SUPPORTED_FOR_SCOPE` — exact lab verification succeeds, qualifying independence is established, leakage count is zero, Architecture stays meaning-level and history is unchanged.
- `WEAKENED` — no hard refutation, but some Architecture wording requires narrowing/profile scoping; no post-hoc rescue under the same experiment ID.
- `REFUTED` — the preregistered hard refutation occurs.
- `INDETERMINATE` — evidence/dependency visibility/independence is insufficient.
- `NOT_TESTED` — no qualifying execution/adjudication has occurred.

Hard refutation:

> Within this scope, a necessary accepted Architecture obligation cannot remain reproducible/testable unless a profile-specific C5 laboratory mechanism is elevated into universal Architecture solely because historical C5 evidence reproduction depends on that mechanism.

## Authority boundary

```text
H11 preregistration ≠ H11 execution admission
execution admission ≠ execution
exact laboratory reproduction ≠ Architecture Canon
A10-H11 ≠ composition/federation
NOT_TESTED ≠ SUPPORTED
```

This plan self-declares:

```text
implementation_authorized_by_this_plan: false
execution_authorized_by_this_plan: false
runtime_expansion: FROZEN
product_runtime_thaw: false
Final Canon: DEFERRED / NOT_AUTHORIZED
production_authorized: false
```

The next gate after authoritative preregistration is `A10_H11_EXECUTION_ADMISSION`, which must freeze the plan digest, machine-readable dependency-graph format, raw-observation/adjudication separation and qualifying reviewer/reproducer evidence before any execution.