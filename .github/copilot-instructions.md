# GitHub Copilot instructions for Velantrim Native Kernel

## Mandatory orientation

`docs/ai/README.md` owns the canonical AI reading order. Before suggesting or editing code:

1. resolve live GitHub branch/PR SHA, issue state, workflow runs and review threads;
2. read `../docs/ai/README.md`;
3. follow its required reading order;
4. apply the operating constraints in `../AGENTS.md`.

Do not reconstruct current truth from a historical checkpoint, README summary, handoff or stale `NEXT` marker.

## Current status

```text
RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
clean_runtime_support:      PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false
assertions:                 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:                     0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
P1–C5:                      BOUNDED_REFERENCE_LABORATORY
selected family:            A10-H11
current gate:               A10_H11_EXECUTION_ADMISSION
admission:                  BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER
reviewer/reproducer:        NOT_ESTABLISHED
H11:                        NOT_TESTED
runtime expansion:          FROZEN
Final Canon:                DEFERRED / NOT AUTHORIZED
production:                 false
```

`project-state.json` uses `nk-project-state/2`. Resolve live HEAD through Git/GitHub; a committed state/checkpoint file never predicts its own future merge SHA.

## Formal Architecture authority

Resolve architecture meaning through the complete accepted chain:

```text
ARCHITECTURE.md
→ A1–A10 first-draft provenance
→ Integrated A1–A10 Review
→ IAR-1 qualifying challenge
→ IAR-1-R1 reconciliation
→ later accepted ADR / operator decisions for their explicit scope
```

Where first-draft wording conflicts with IAR-1-R1, the reconciliation is the current provisional interpretation unless later accepted authority explicitly supersedes that scope. Final Canon remains deferred.

Do not force future profiles to reproduce A2/A3/A5/A6/Event/reducer/Receipt/exact-replay shape merely because the current laboratory or first drafts do so.

## Track boundary

```text
H historical recovery: BLOCKED / independent / operator-controlled source admission
C clean implementation: PRESERVED / PARTIAL / BOUNDED_REFERENCE_LABORATORY
R post-blueprint validation: ACTIVE / H11 EXECUTION ADMISSION BLOCKED
```

Do not collapse them.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
reference laboratory ≠ architecture authority
operator approval ≠ independent validation
qualifying review ≠ universal architecture proof
preregistration ≠ execution admission
blocked admission ≠ INDETERMINATE
falsification instrument ≠ product runtime
```

## Active gate — A10_H11_EXECUTION_ADMISSION

The selected residual family is `A10-H11 / RAVP-H11-LAB-CANON-SEPARATION`. Its frozen plan is `H11-001-c5-lab-canon-separation-v1`, SHA-256 `60da649e675b79b3e70bf8a61cf03cb4d57bb989f4934b65ab8d50c925b19914`.

```text
selection: COMPLETE
preregistration: COMPLETE / EXECUTION_NOT_AUTHORIZED
execution admission: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER
qualifying reviewer/reproducer: NOT_ESTABLISHED
H11 outcome: NOT_TESTED
implementation: NOT AUTHORIZED
execution: NOT AUTHORIZED
dependency-graph execution: NOT AUTHORIZED
semantic adjudication: NOT AUTHORIZED
runtime expansion: FROZEN
production: false
```

PR #131 is the open repository-visible external review surface. Do not merge it merely because CI is green or the PR is mergeable.

### Independence rule

H11 requires `INDEPENDENT_SEMANTIC_ORACLE` evidence. These are not substitutes:

- repository-owner/self review;
- CI success;
- automated validators;
- Codex/LLM agreement;
- model or session change;
- same-agent relabeling;
- Notion read-back.

The existing Codex review is useful technical review but its qualification remains `NOT_ESTABLISHED`. A future qualifying reviewer/reproducer still requires a separate admission reassessment before execution.

## Architecture discipline

- Preserve meaning/profile/evidence/authority separation.
- Treat P1–C5 as a bounded laboratory, not architecture authority.
- Do not turn Python, Rust, PostgreSQL, SQLite, SQL, JSON, SHA-256, Events, reducers, Receipts, graphs, vectors, LLMs or current hardware into universal obligations without governed evidence/decision.
- Event history is authoritative about recorded laboratory history, not automatically truth or universal architecture.
- Logical `ERASED` does not establish physical deletion, cryptographic erasure or global forgetting.
- PostgreSQL↔SQLite is bounded same-lineage profile evidence, not arbitrary-substrate proof.
- Cross-language evidence does not establish independent team, custody or computation model by itself.
- Local scoped conformance does not imply composition/federation conformance.

## Allowed while runtime is frozen

- architecture/truth-surface documentation repair;
- integrity, security, reproducibility and provenance fixes;
- evidence preservation;
- reviewer/reproducer qualification evidence work that does not execute H11;
- historical recovery work that does not admit operator-controlled sources.

## Not authorized

- H11 implementation/execution while admission is blocked;
- H11 dependency-graph execution or semantic adjudication;
- preregistration/execution of H03/H06/H08/H09/H10 without their future gates;
- product runtime thaw;
- reducer v2 or new semantic Event verbs;
- new product database/language/model/hardware profiles;
- executable NK-EPI/Temporal/deletion expansion;
- Final Canon, maturity or production promotion.

## Pending decisions remain pending

```text
Issue #18 — license/publication/contribution regime
  PENDING_OPERATOR

Issue #74 / ADR-0024 — future reducer referential semantics
  PROPOSED / PENDING_OPERATOR
  reducer-v2 NOT AUTHORIZED

Track H source admission
  OPERATOR-CONTROLLED
```

Do not choose a license, accept ADR-0024, admit Track H sources, thaw runtime, promote Final Canon or authorize production for the operator.

## Historical immutability

Do not rewrite reducer-v1 history, Events, Receipts, fixtures, evidence ZIPs, historical checkpoint identities, A1–A10 first drafts, integrated-review history, IAR-1 findings or IAR-1-R1 publication-time gate language.

Historical `NEXT`/`NOT_STARTED` values remain provenance in designated history/research surfaces. Do not copy them back into current-only AI instructions as if they were present state.

## Verification

```bash
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_architecture_freeze.py --repo .
python tools/ai_context/validate_residual_a10_plan.py --repo .
python tools/ai_context/validate_h11_family_selection.py --repo .
python tools/ai_context/validate_h11_preregistration.py --repo .
python tools/ai_context/validate_h11_execution_admission.py --repo .
python tools/ai_context/validate_reconciliation.py --repo .
python tools/ai_context/validate_context.py --repo .
python tools/docs/validate_bilingual_parity.py --repo .
python -m unittest discover -s tests -p 'test_ai_context_validator.py' -v
```

The SQLite profile fails closed below linked SQLite `3.51.3`; an unsafe local SQLite environment is `NOT_EXECUTED` for affected profile tests, not a reason to lower the safety floor.

## Review discipline

Distinguish bot notices, automated findings, human reviews, qualifying independent architecture reviews, qualifying H11 reviewer/reproducer evidence, operator decisions and evidence. A Codex quota notice is not review approval.

## Documentation synchronization

Classify changes using Documentation Standard v5. Update only affected GitHub/Notion representations for their declared roles; do not duplicate volatile live SHA or identical current-state blocks across every human surface. GitHub must remain technically sufficient without Notion.
