# 🤖 Velantrim Native Kernel repository guidance

## Canonical reading order

`docs/ai/README.md` owns the mandatory AI/agent reading order.

Before searching code, creating a branch, proposing architecture changes or mutating repository/Notion state:

1. resolve live GitHub state;
2. open [`docs/ai/README.md`](docs/ai/README.md);
3. follow its reading order exactly;
4. then apply the operating constraints in this file.

For durable future-work orientation, use [`docs/ai/AUDIT_AND_FUTURE_WORK.md`](docs/ai/AUDIT_AND_FUTURE_WORK.md) only after reconciling it against live state. It is not an authorization surface and does not auto-select the next milestone.

A handoff, old checkpoint, model memory, README summary, Notion page or historical `NEXT` marker is not a substitute for live repository truth.

## 🟢 START HERE — execution card

1. **Verify live truth first.** Resolve current `main`, signature status, open PRs, relevant reviews/threads, open issues, Actions, `project-state.json`, the active gate, and the existing Native Kernel Notion surfaces when synchronization is in scope.
2. **Follow live state, not the handoff.** If a dated handoff/checkpoint disagrees with live repository evidence, record the divergence and use live state. Never restore old state mechanically.
3. **Keep project scope strict.** Work only on `velantrian/velantrim-native-kernel`. External projects are read-only, cited, non-authoritative references and may be consulted only when Native Kernel evidence cannot answer a concrete scoped question.
4. **Fail closed on H11.** Unless live evidence establishes otherwise, H11 remains blocked at `A10_H11_EXECUTION_ADMISSION`; owner/AI/CI/self-review does not establish independent reviewer/reproducer provenance.
5. **Default to read-only before mutation.** Live verification, evidence gathering, reconciliation matrices and exact proposed patches do not require a branch.
6. **Separate audit from write.** A finding may justify a proposed change without authorizing that change.
7. **Require explicit operator approval for the exact write set.** Branch creation, commits, PRs, Issue/PR metadata changes, Notion edits, runtime/config changes and other repository mutations are writes. Do not perform them until the operator explicitly approves the proposed bounded change set.
8. **Do not advance research implicitly.** Documentation maintenance does not authorize H11 execution, another residual A10 family, Final Canon, runtime thaw, reducer-v2 semantics, licensing or production.

## Write-authorization gate

The pre-write phases are **read-only by default**. Before any mutation, provide or establish all of the following:

1. exact source evidence and live checkpoint;
2. the current wording/state being challenged;
3. the current controlling interpretation/authority;
4. the smallest proposed change set;
5. why the change is maintenance/clarification rather than a new architecture, semantic contract, H11 decision, runtime change or acceptance-criteria change;
6. the expected validation/read-back plan;
7. explicit operator approval for that bounded change set.

Approval applies only to the change set actually described. If scope grows materially, return to read-only mode and obtain fresh approval before continuing.

A branch is permitted only after this gate is satisfied. Read-only audit work should not create a branch merely as a workspace placeholder.

Green CI, mergeability, an automated review, absence of objections, a prior broad handoff, a stale approval for a different change set, or a model's judgment that a patch is "safe" are not substitutes for explicit operator approval.

## Audit closure and drift definitions

For bounded reconciliation/audit work, classify every target with exactly one action result:

- `NO_ACTION` — current wording remains compatible with controlling authority for its declared scope;
- `CLARIFICATION_CANDIDATE` — a minimal scope/authority annotation would remove real drift without changing outcome, acceptance criteria or semantics;
- `OPERATOR_DECISION_REQUIRED` — the proposed change would select or alter architecture, contract, acceptance criteria, policy/version boundary, H11, license, Canon, runtime or another reserved decision.

Use these definitions:

- **Real drift** exists only when current wording both (a) prescribes, requires or evaluates an implementation/profile mechanism as if it were a universal Kernel requirement and (b) conflicts with the current controlling interpretation for the same scope. Mere use of terms such as Event, reducer, JSON, replay, Claim encoding or SQL does not prove drift.
- **Safe clarification** is a dated scope/authority annotation that does not change issue outcome, acceptance condition, priority, ownership, implementation semantics, frozen evidence, H11 status, Final Canon status or runtime authorization.
- **Substantive operator decision** is required when a proposed change selects or changes a universal architecture requirement, semantic contract, acceptance criterion, versioning/policy boundary, reducer semantics, H11 subject/plan/admission, license, Canon, runtime thaw, production status or issue closure based on new acceptance.

Preserve historical issue/document intent. Prefer a clearly separated dated addendum/current-scope overlay over rewriting historical acceptance text when the old wording is useful provenance.

A completed bounded audit should leave an evidence-backed record containing: target, source evidence, old wording/state, current controlling interpretation, drift decision, smallest proposed clarification if any, action class, owner/authority if escalation is required, and validation/read-back result.

## External outreach evidence and research-order reporting

Keep external communication evidence and research authorization separate and fail closed on stronger claims.

- Treat `SENT`, `DELIVERED_OR_PUBLISHED`, `RESPONSE_RECEIVED`, `CANDIDATE_IDENTIFIED`, and `QUALIFIED` as distinct states. Never infer a later state from an earlier one.
- A repository/Notion summary is not primary transport evidence. When reporting an external outreach action as verified, retain or reference the channel/recipient, UTC send time, exact message body or stable hash, Message-ID or public permalink when available, and the observed delivery/bounce/response state. Absence of an observed bounce is not proof of delivery.
- `recommended_order` in RAVP-001 is planning guidance, not execution authorization. Every residual A10 family remains subject to its own bounded planning/admission/authorization requirements; completion of one family does not automatically authorize the next.
- Residual-family evidence feeds a later integrated reassessment. It does not predetermine Final Canon. A later operator decision may freeze a Canon version, keep the architecture provisional, narrow or revise claims, require more evidence, or reject a claim for the relevant scope.
- Do not publish percentage/probability-style readiness or channel-fit scores unless the denominator, weighting and reproducible calculation rule are explicit. Prefer evidence states and countable ratios such as `2/2 sends recorded` or `0/6 residual outcomes complete`.

## H11 qualification evidence rule

The canonical H11 reviewer/reproducer qualification mechanism is the existing machine contract:

- `docs/research/H11_REVIEWER_REPRODUCER_QUALIFICATION_SCHEMA.json`;
- `docs/research/H11_REVIEWER_REPRODUCER_QUALIFICATION.json`;
- `tools/ai_context/validate_h11_execution_admission.py`.

A prose qualification matrix may summarize evidence, but it cannot substitute for the schema/record/validator or weaken their fail-closed rules.

At minimum, qualification evidence must make identity/role, authorship relation, custody relation, conflicts/material dependence/self-review, frozen-input boundary, private-state boundary, repository visibility and externally authenticated independence provenance evaluable. The qualification-facing result must map to `QUALIFIED`, `NOT_ESTABLISHED` or `DISQUALIFIED` under the machine contract.

Do not manually assert `QUALIFIED` because a narrative matrix looks complete. Qualification must satisfy the machine contract and its external-authentication boundary; even then, qualification is not execution admission.

## Current safety boundary

```text
RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
P1–C5: BOUNDED_REFERENCE_LABORATORY
selected family: A10-H11
current gate: A10_H11_EXECUTION_ADMISSION
admission: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER
reviewer/reproducer: NOT_ESTABLISHED
H11: NOT_TESTED
implementation/execution: NOT AUTHORIZED
runtime expansion: FROZEN
product runtime thaw: false
Final Canon: DEFERRED / NOT AUTHORIZED
production: false
Issue #88: OPEN
```

The frozen H11 plan is `H11-001-c5-lab-canon-separation-v1`, SHA-256 `60da649e675b79b3e70bf8a61cf03cb4d57bb989f4934b65ab8d50c925b19914`. PR #131 is the repository-visible external review surface.

The committed H11 state-binding checkpoint is PR #130 / `e36b7f45410d74b8a65406bff6fdd6d070fa96b0`. Live HEAD must always be resolved separately through Git/GitHub; committed checkpoint metadata never predicts its own future merge SHA.

## Architecture authority

Do not treat A1–A10 first-draft wording as Final Canon or as the last interpretation when later reconciliation narrows it.

```text
ARCHITECTURE.md
→ A1–A10 first-draft provenance
→ Integrated A1–A10 Review
→ IAR-1 qualifying challenge
→ IAR-1-R1 reconciliation
→ later accepted ADR / operator decisions for their explicit scope
```

Where first-draft wording conflicts with IAR-1-R1, the reconciliation is the current provisional interpretation unless a later accepted architecture authority explicitly supersedes that scope.

Reference-laboratory mechanisms do not become universal architecture merely because current evidence depends on them.

```text
reference laboratory ≠ Architecture authority
exact lab reproduction ≠ Final Canon
profile-specific mechanism ≠ universal semantic obligation
```

## Independent tracks

Never collapse these tracks:

```text
H — Historical Recovery
  OPEN / BLOCKED / operator-controlled source admission

C — Clean Reference Implementation
  P1–P5 + C4 + C5
  PARTIAL / BOUNDED_REFERENCE_LABORATORY

R — Architecture Re-foundation and post-blueprint research
  A1–A10 first drafts complete / provisional
  integrated review + IAR-1 + IAR-1-R1 complete
  Option D / BPV-1 / D6–D8 complete for their recorded scope
  ADR-0027 accepted
  RAVP-001 complete
  A10-H11 selected and preregistered
  current admission BLOCKED pending genuine independent reviewer/reproducer evidence
```

## H11 fail-closed rules

- Architecture/preregistration authors may not self-certify H11.
- Subject self-PASS is forbidden.
- CI success, owner review, automated validators, LLM agreement, model/session changes or same-agent relabeling are not qualifying independence.
- The existing Codex technical review is useful but remains `NOT_ESTABLISHED_FOR_H11_REVIEW_ROLE`.
- Raw observations and semantic adjudication remain separate.
- Private implementation state is not mandatory semantic-oracle input.
- `UNJUSTIFIED_CANON_DEPENDENCY` remains the frozen hard-failure class.
- Frozen failure conditions, oracle and thresholds may not be changed post hoc to rescue the run.
- Historical evidence/architecture history may not be rewritten to rescue H11.
- `INDETERMINATE` is an A10 outcome available only after qualifying execution/adjudication; blocked pre-execution admission remains `NOT_TESTED`.
- Qualification is not execution admission; a future qualifying reviewer still requires a separate admission reassessment before execution.
- `A10-H11 ≠ composition/federation`.

## Runtime freeze

Allowed while frozen:

- truth-surface, documentation-authority, integrity, security and provenance repairs;
- evidence preservation;
- reviewer/reproducer qualification evidence work that does not execute H11;
- historical recovery work that does not admit operator-controlled sources;
- later research admission/preregistration work only when the active gate explicitly authorizes it.

Not automatically authorized:

- H11 implementation/execution, dependency-graph execution or semantic adjudication while admission is blocked;
- preregistration/execution of A10-H03/H06/H08/H09/H10;
- product runtime integration;
- reducer v2 or new semantic Event verbs;
- new product database/language/model/hardware profile;
- executable NK-EPI/Temporal/deletion expansion;
- Final Canon promotion;
- runtime thaw;
- production authorization.

## Reserved operator decisions

No AI agent may make these decisions without explicit operator authority:

```text
Issue #18 — license/publication/contribution regime
Issue #74 / ADR-0024 — future reducer referential semantics
Track H recovered-source admission
Final Canon
runtime thaw
production authorization
```

Reducer v1 historical semantics must not be rewritten in place. Logical `ERASED` must not be presented as physical or cryptographic erasure without the required evidence boundary.

## Required distinctions

```text
Claim ≠ truth
admission ≠ objective truth
Unknown ≠ False
reference laboratory ≠ architecture authority
operator approval ≠ independent validation
qualifying review ≠ universal architecture proof
falsification instrument ≠ product runtime
logical ERASED ≠ physical deletion
cryptographic erasure ≠ physical erasure
forgetting/loss ≠ deliberate erasure
language difference ≠ computation-model difference
simulation/emulation ≠ physical substrate evidence
local scoped conformance ≠ composition/federation conformance
planning ≠ selection ≠ preregistration ≠ execution admission ≠ execution
blocked admission ≠ INDETERMINATE
public repository ≠ open-source license
SUPPORTED_FOR_SCOPE ≠ universal proof
NOT_TESTED ≠ SUPPORTED
```

## Historical/current discipline

Do not restore obsolete current-looking state into current-only agent surfaces merely to satisfy an old literal-string validator.

Historical D5/D6/D7/D8, ADR-0027, RAVP, family-selection and preregistration checkpoints remain available in `STATUS.md`, `ROADMAP.md`, `docs/research/**`, `docs/reviews/**`, evidence records, work/reconciliation logs and Git history.

If a historical document contains an old `NEXT`, `NOT_STARTED`, merge SHA or Notion checkpoint, preserve it as provenance but do not treat it as a present instruction when machine/current-state authority has advanced.

## Verification

At minimum for current truth / architecture-routing changes:

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

Run additional P4/P5/C3/C4/C5/BPV1 gates when changed-file scope triggers them. A skipped test is not PASS. An unavailable environment is `NOT_EXECUTED`.

## Review discipline

Distinguish `BOT_NOTICE`, `AUTOMATED_FINDING`, `HUMAN_REVIEW`, `QUALIFYING_INDEPENDENT_ARCHITECTURE_REVIEW`, `QUALIFYING_INDEPENDENT_H11_REVIEWER_REPRODUCER`, `OPERATOR_DECISION`, and `EVIDENCE`.

A Codex usage-limit notice is not review approval. Actionable findings must be reproduced and resolved or rejected with evidence. Do not merge PR #131 as a substitute for independent qualification.