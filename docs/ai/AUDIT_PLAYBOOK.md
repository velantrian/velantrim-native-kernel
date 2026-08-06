# 🔍 Native Kernel AI Audit Playbook

This playbook defines a context-efficient audit method for Native Kernel.
The goal is not to read every file. The goal is to obtain enough verified evidence to make a reliable conclusion without mixing architecture, external history, support tooling and runtime claims.

## 1. Establish the exact object under review

Record:

- repository and default branch;
- exact base commit SHA;
- PR/issue number and exact head SHA, if applicable;
- changed files and current checks;
- whether the claim concerns `main`, an open PR, external `v0.1.2.1`, a proposal, an accepted decision, support tooling or a running implementation.

Never mix an open branch or external report into current `main` reality.

## 2. Read the orientation layer

Read in order:

1. root `README.md`;
2. `STATUS.md`;
3. root `AGENTS.md`;
4. `docs/ai/CURRENT_STATE.md`;
5. relevant section of `COMPONENT_MAP.md`;
6. relevant risks and recent work-log entries.

Stop reading general documentation when the affected architectural layer, evidence boundary and owning record are clear.

## 3. Convert the request into testable claims

Examples:

- “Is Kernel implemented?” → public runtime files, tests, package/install path and exact CI.
- “Is PostgreSQL supported?” → adapter exists, contract tests, replay/equivalence and operational profile—not ADR text alone.
- “Was v0.1.2.1 recovered?” → authentic bytes, lineage, manifest, original tests and operator GO.
- “Is this technology-neutral?” → at least two materially different profiles preserve declared semantics under committed conformance evidence.
- “Is this safe?” → threat model, failure paths, deletion/privacy semantics, rollback and observed evidence.

## 4. Identify the architectural layer

For each claim, classify:

```text
Architecture Canon
Abstract Contract
Implementation Profile
Support / Recovery Tooling
Implemented Runtime
Evidence Artifact
Operator Decision
Production Evidence
```

Flag silent promotion from one layer to another.

## 5. Trace authority and provenance

For every proposed or implemented path, identify:

```text
source
→ identity / canonical encoding
→ admission or authority owner
→ event or state transition
→ authoritative history
→ reducer
→ projection
→ consumer
→ Receipt
→ operator visibility
```

Flag:

- missing provenance converted into invented origin;
- backend IDs becoming semantic identity;
- projection/retrieval becoming truth authority;
- model output becoming admitted knowledge;
- write order becoming semantic correctness;
- cross-project data inheriting authority implicitly.

## 6. Inspect real artifacts and downstream references

Do not rely on a summary alone.

For changed status labels, contracts, event verbs, schemas, ADRs, profile choices and integration boundaries:

1. inspect the exact diff;
2. search all current references;
3. inspect paired English/Russian documents;
4. inspect ADR index and supersession state;
5. inspect tests/workflows when implementation or evidence is claimed;
6. inspect Notion only as rationale/history, never as runtime proof.

## 7. Separate maturity questions

| Question | Evidence |
|---|---|
| Documented? | current specification exists |
| Proposed? | explicit proposal/RFC status |
| Accepted? | operator-approved ADR/decision |
| Implemented? | code exists at exact SHA |
| Tested? | committed tests and exact result |
| Wired? | real caller/runtime path |
| Enabled? | active configuration/profile |
| Observed? | runtime metrics/logs/traces |

Never collapse these into “works”.

## 8. Verify tests and CI honestly

Check:

- exact workflow scope and trigger;
- exact SHA tested;
- Python/runtime versions;
- dependency reproducibility;
- whether checks cover support tooling or Kernel runtime;
- skips, deselections and failure ordering;
- whether an open PR or synthetic merge ref is being mistaken for `main` evidence.

A source-recovery-tool PASS proves only its declared utility contract.

## 9. Audit failure and recovery paths

As applicable, consider:

- duplicate command and idempotency;
- crash before/after append;
- partial batch;
- concurrent writers and ordering;
- corruption/truncation;
- schema evolution;
- projection deletion/rebuild;
- migration interruption/rollback;
- erasure across payloads, projections, exports and backups;
- profile capability mismatch;
- provenance gaps;
- Notion/GitHub documentation drift.

## 10. Produce an evidence table

Use:

| Finding | Evidence | Impact | Confidence | Required action |
|---|---|---|---|---|

Classify each as:

- confirmed defect;
- documentation drift;
- missing evidence;
- design trade-off;
- boundary violation;
- future recommendation.

## 11. Update continuity records

After significant work:

- update `CURRENT_STATE.md` only for verified state changes;
- update `KNOWN_RISKS.md` with exact proof;
- add `WORK_LOG.md` entry;
- update `COMPONENT_MAP.md` if first-read paths or ownership changed;
- add/update ADR for durable decisions;
- synchronize Notion or create a hand-off.

## Audit completion criteria

An audit is complete enough for a decision when it states:

- exact scope and SHA;
- what is documented, accepted, implemented and evidenced;
- highest-impact defects or missing proof;
- source/provenance and authority boundaries;
- checks actually observed;
- documentation freshness caveats;
- prioritized minimal next actions.
