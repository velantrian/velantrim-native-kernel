# 🤖 Velantrim Native Kernel repository guidance

This file is the mandatory entry point for AI coding agents, auditors, reviewers and automated contributors.

## 1. Required reading order

1. [`README.md`](README.md) — public purpose and maturity.
2. [`STATUS.md`](STATUS.md) — authoritative implementation/evidence boundary.
3. [`docs/ai/README.md`](docs/ai/README.md) — context-pack map.
4. [`docs/ai/DOCUMENTATION_SYNC_PROTOCOL.md`](docs/ai/DOCUMENTATION_SYNC_PROTOCOL.md).
5. [`docs/ai/CURRENT_STATE.md`](docs/ai/CURRENT_STATE.md).
6. [`docs/ai/C4_IMPLEMENTATION_RECORD.md`](docs/ai/C4_IMPLEMENTATION_RECORD.md) for offline shadow work.
7. [`docs/ai/P5_IMPLEMENTATION_RECORD.md`](docs/ai/P5_IMPLEMENTATION_RECORD.md) for SQLite/C3 prerequisites.
8. [`docs/ai/P4_IMPLEMENTATION_RECORD.md`](docs/ai/P4_IMPLEMENTATION_RECORD.md) for PostgreSQL C2 foundation.
9. Relevant section of [`docs/ai/COMPONENT_MAP.md`](docs/ai/COMPONENT_MAP.md).
10. Relevant entries in [`docs/ai/KNOWN_RISKS.md`](docs/ai/KNOWN_RISKS.md).
11. Recent entries in [`docs/ai/WORK_LOG.md`](docs/ai/WORK_LOG.md).
12. [`docs/ai/AUDIT_PLAYBOOK.md`](docs/ai/AUDIT_PLAYBOOK.md) for audits.

Then inspect only affected contracts, source, tests, manifests, workflows, RFCs, ADRs, PRs and issues. Documentation is orientation, not self-proving evidence.

## 2. Source-of-truth order

1. executable code, committed tests and approved dataset bytes at the exact SHA;
2. exact-SHA CI jobs, logs and retained artifacts;
3. `STATUS.md` and current-state records;
4. accepted ADRs and normative contracts;
5. current RFCs/research with explicit statuses;
6. PRs, issues and work logs;
7. historical chats, audits and external reports.

Never treat an open PR, Notion page, approval, detailed design or generated JSON file as behaviour already present in `main`.

## 3. Required distinctions

```text
Decision status
≠ Implementation status
≠ Evidence level
≠ Operator approval

C1 ≠ C2 ≠ C3 ≠ C4
C4 offline shadow ≠ live shadowing
Shadow observation ≠ authority promotion
```

Distinguish documented, proposed, accepted, implemented, tested, wired, enabled, observed and promoted.

## 4. Architecture discipline

- Preserve `Architecture Canon → Abstract Contracts → Replaceable Implementation Profiles → Bounded Evidence Layers`.
- PostgreSQL, SQLite, Python, Psycopg, SQL layouts, files, JSON protocols, CI runners, LLMs, embeddings, graphs, CPUs/GPUs and future substrates are replaceable instruments, not Canon.
- Event history is authoritative about recorded history, not automatically truth.
- Relevance, recency, utility, repetition, write order, model confidence or shadow agreement do not independently establish truth.
- A Receipt, evidence report, equivalence report or Shadow Receipt proves only its declared operation, inputs, checks and limitations.
- Operator approval is authority, not empirical evidence.

## 5. Current C4 boundary

Current branch maturity:

```text
RESEARCH / C4 PARTIAL OFFLINE SHADOW EVALUATION / NOT PRODUCTION-READY
```

Profiles and evidence layer:

```text
native-kernel/postgresql-reference@0.4-p4
native-kernel/sqlite-embedded@0.5-p5
native-kernel/c4-offline-shadow-v1
```

Result maps:

```text
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
Offline C4 scope:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
support_state:     PARTIAL
```

C4 applies only to the existing 45 C3-supported assertions and the exact approved dataset.

```text
C4 ≠ support for all 72
C4 ≠ live production shadowing
C4 ≠ authority promotion or candidate approval
C4 ≠ PostgreSQL/SQLite operational equivalence
C4 ≠ exhaustive state-space equivalence
C4 ≠ truth/authenticity
C4 ≠ physical deletion
C4 ≠ C5
C4 ≠ production readiness
```

All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

## 6. C4 dataset and authority rules

Approved dataset:

```text
dataset_id:     native-kernel/c4-offline-shadow-v1
protocol:       nk-shadow-workload/1
sha256:         15fb81d8858dcc4e349ffe87c257b25450db026473614582faa7817f90249da3
cases:          15
assertion scope:45 / 45 C3-supported assertions
```

Mandatory authority boundary:

```text
mode:                  SHADOW_ONLY
authority promotion:   FORBIDDEN
authoritative writes:  FORBIDDEN
side effects:           FORBIDDEN
promotion decision:    NOT_AUTHORIZED
```

Dataset changes require a new immutable version, digest, approval record, manifest update, tests and exact repository evidence. Never edit approved thresholds or observations in place while retaining the old dataset ID/version.

The evaluator must not call append, mutate projections, change authoritative history, invoke external tools, approve a candidate or wire itself into Titan, Mentaury or Crystal.

## 7. Profile independence

The SQLite profile must remain materially independent:

- no calls into PostgreSQL append/replay/projection/Receipt adapters;
- own migrations, schema, transaction/fencing and persistence code;
- shared profile-neutral contracts and fixtures are allowed;
- cross-profile comparison must operate on observable contract outcomes, not schema similarity.

Allowed differences must be declared. Payload, order, state, outcome, integrity and Receipt differences must never be hidden by normalization.

## 8. Issue #1 and Issue #18 boundaries

The clean P1–P5 implementation and C4 dataset are not recovered historical `v0.1.2.1` and not the original 44-test suite.

- Do not label newly written code, tests, datasets or reports as recovered history.
- `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.
- Issue #1 recovery remains independent.
- Issue #18 licensing/publication remains independent.
- C4 introduces no new external runtime dependency and publishes no package.

## 9. Cross-project boundaries

- Native Kernel owns neutral semantic memory/Event/evidence contracts and bounded profiles/evidence protocols.
- Titan owns cognition, retrieval, tools and orchestration.
- Mentaury Soul owns digital individuality and continuity.
- Crystal owns verifiable-memory, evidence and product boundaries.

No identity, authority, credential, runtime, storage, C4 observation or conformance status is inherited automatically across projects.

## 10. Verification routes

### C4 local guards

```bash
python -m unittest discover -s tests -p 'test_c4_shadow_evaluation.py' -v
python -m unittest discover -s tests -p 'test_c4_report_validator.py' -v
python -m unittest discover -s tests -p 'test_c4_manifest.py' -v
python tools/profiles/validate_c4_manifest.py
python -m unittest discover -s tests -p 'test_ai_context_validator.py' -v
python tools/ai_context/validate_context.py --repo .
```

Local tests establish implementation checks only. They do not establish repository C4.

### Repository C4 evidence

Repository evidence requires:

- all four Python/PostgreSQL matrix jobs PASS;
- SQLite version recorded;
- exact PostgreSQL P4, SQLite P5 and C3 prerequisite reports;
- exact C4 report validated with repository metadata;
- four retained artifacts, each containing all four reports;
- exact head/run/environment/artifact traceability;
- 15/15 cases and Receipts;
- zero semantic/critical divergences and zero missing Receipts;
- exact `45/10/17/0` map;
- final-head re-run after documentation changes.

Do not claim:

- C4 from local tests alone;
- C4 from a JSON report without retained repository evidence;
- live shadowing from offline recorded data;
- authority promotion from shadow agreement;
- full support from top-level C4;
- operational equivalence from semantic comparison;
- truth, authenticity or physical erasure from hashes/Receipts/reports;
- production safety/privacy/security without C5 and operational proof.

## 11. Documentation and Notion synchronization

Material changes must update relevant GitHub documents:

- `STATUS.md`;
- `docs/ai/CURRENT_STATE.md`;
- `docs/ai/C4_IMPLEMENTATION_RECORD.md`;
- `docs/ai/P5_IMPLEMENTATION_RECORD.md` when prerequisites change;
- `docs/ai/KNOWN_RISKS.md`;
- `docs/ai/COMPONENT_MAP.md`;
- `docs/ai/WORK_LOG.md`;
- relevant ADR/status/profile/contract/tool/public documents.

Classify impact as `NONE`, `GITHUB_ONLY` or `GITHUB_AND_NOTION`.

GitHub must contain enough technical/evidence context to continue without Notion. When Notion is available, synchronize motivation, exact reality, dataset digest, evidence, limitations, PR and merge SHA in the same cycle.

## 12. Change discipline

1. establish exact base/head and phase scope;
2. identify whether a claim concerns `main`, an open PR or future work;
3. inspect affected contracts/tests/downstream documents;
4. make the smallest coherent change;
5. validate it;
6. update GitHub and Notion records;
7. open/update a PR with exact evidence and limitations;
8. inspect final diff, checks, artifacts, reviews and unresolved threads;
9. merge only with expected head SHA.

Do not combine C4 finalization with C5, live shadowing, production deployment, deletion execution, source recovery or ecosystem wiring.
