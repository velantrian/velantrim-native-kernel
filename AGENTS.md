# 🤖 Velantrim Native Kernel repository guidance

This file is the mandatory entry point for AI coding agents, auditors, reviewers and automated contributors.

## 1. Required reading order

1. [`README.md`](README.md) — public purpose and maturity.
2. [`STATUS.md`](STATUS.md) — authoritative implementation/evidence boundary.
3. [`docs/ai/README.md`](docs/ai/README.md) — context-pack map.
4. [`docs/ai/DOCUMENTATION_SYNC_PROTOCOL.md`](docs/ai/DOCUMENTATION_SYNC_PROTOCOL.md).
5. [`docs/ai/CURRENT_STATE.md`](docs/ai/CURRENT_STATE.md).
6. Relevant section of [`docs/ai/COMPONENT_MAP.md`](docs/ai/COMPONENT_MAP.md).
7. Relevant entries in [`docs/ai/KNOWN_RISKS.md`](docs/ai/KNOWN_RISKS.md).
8. Recent entries in [`docs/ai/WORK_LOG.md`](docs/ai/WORK_LOG.md).
9. [`docs/ai/P4_IMPLEMENTATION_RECORD.md`](docs/ai/P4_IMPLEMENTATION_RECORD.md) for conformance work.
10. [`docs/ai/AUDIT_PLAYBOOK.md`](docs/ai/AUDIT_PLAYBOOK.md) for audits.

Then inspect only affected contracts, source, tests, manifests, workflows, RFCs, ADRs, PRs and issues. Documentation is orientation, not self-proving evidence.

## 2. Source-of-truth order

1. executable code and committed tests at the exact SHA;
2. exact-SHA CI jobs, logs and artifacts;
3. `STATUS.md` and current-state records;
4. accepted ADRs and normative contracts;
5. current RFCs and research documents with explicit statuses;
6. PRs, issues and work logs;
7. historical chats, audits and external reports.

Never treat an open PR, Notion page, approval or detailed design as behavior already present in `main`.

## 3. Required status distinctions

Distinguish:

- documented;
- proposed;
- accepted;
- implemented;
- tested;
- wired;
- enabled;
- observed.

Preserve:

```text
Decision status
≠ Implementation status
≠ Evidence level
≠ Operator approval
```

## 4. Architecture discipline

- Preserve `Architecture Canon → Abstract Contracts → Replaceable Implementation Profiles`.
- PostgreSQL, SQLite, Python, Psycopg, SQL layouts, LLMs, embeddings, graphs, CPUs/GPUs and future substrates are replaceable instruments, not Canon.
- Event history is authoritative about recorded history, not automatically truth.
- Relevance, recency, utility, repetition, write order and model confidence do not independently establish truth.
- A Receipt or evidence report proves only its declared operation, checks and limitations.
- Operator approval is authority, not empirical evidence.

## 5. Current P4 boundary

Current branch maturity:

```text
RESEARCH / P4 PARTIAL ASSERTION CONFORMANCE / NOT PRODUCTION-READY
```

Clean lineage:

```text
clean/postgresql-reference/0.1
```

Current assertion map:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
TOTAL:       72
```

Repository C2 applies only to the 41 `SUPPORTED` results in the exact evidence report.

```text
P4 C2 ≠ support for all 72
P4 C2 ≠ C3
P4 C2 ≠ truth/authenticity
P4 C2 ≠ physical deletion
P4 C2 ≠ production readiness
```

All `NK-EPI-001…008` remain `UNSUPPORTED` because their registry decision is `PROPOSED`.

P5/SQLite/C3 requires a separate explicit operator GO.

## 6. Issue #1 boundary

The clean P1–P4 implementation is not recovered historical `v0.1.2.1` and not the original 44-test suite.

- Do not reconstruct an approximation and label it recovered history.
- Do not call newly written tests the original suite.
- `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.
- Issue #1 source recovery remains independent.
- Issue #18 licensing/publication remains independent.

## 7. Cross-project boundaries

- Native Kernel owns neutral semantic memory/Event/evidence contracts and bounded profiles.
- Titan owns cognition, retrieval, tools and orchestration.
- Mentaury Soul owns digital individuality and continuity.
- Crystal owns verifiable-memory, evidence and product boundaries.

No identity, authority, credential, runtime, storage or conformance status is inherited automatically across projects.

## 8. Verification routes

Use the narrowest relevant checks first.

### P1

```bash
python -m unittest discover -s tests -p 'test_semantic_core.py' -v
python -m unittest discover -s tests -p 'test_p1_manifest.py' -v
python tools/profiles/validate_p1_manifest.py
```

### P2

Run unit/manifest checks, then PostgreSQL integration with an explicit DSN.

### P3

Run semantic/manifest checks, PostgreSQL replay/projection integration and P2 regressions.

### P4

```bash
python -m unittest discover -s tests -p 'test_p4_conformance_unit.py' -v
python -m unittest discover -s tests -p 'test_p4_manifest.py' -v
python tools/profiles/validate_p4_manifest.py

NK_TEST_POSTGRES_DSN='postgresql://...' \
  python -m unittest discover -s tests -p 'test_p4_postgresql_integration.py' -v
```

For C2, inspect the exact P4 workflow run, all four matrix jobs, generated JSON reports and artifact metadata. A JSON file with self-declared CI metadata is not sufficient evidence by itself.

Do not claim:

- Kernel CI when only utility CI ran;
- integration when tests were skipped;
- C2 without exact repository run/artifact traceability;
- C3 from Python/PostgreSQL version diversity;
- truth, authenticity or physical erasure from hashes, Receipts or reports;
- production safety/privacy/security without operational proof.

## 9. Documentation and Notion synchronization

Material changes to architecture, implementation, evidence, risks, contracts or phase gates must update relevant GitHub documentation:

- `STATUS.md`;
- `docs/ai/CURRENT_STATE.md`;
- `docs/ai/KNOWN_RISKS.md`;
- `docs/ai/COMPONENT_MAP.md`;
- `docs/ai/WORK_LOG.md`;
- relevant ADR/RFC/profile/package documents.

Classify documentation impact as `NONE`, `GITHUB_ONLY` or `GITHUB_AND_NOTION`.

GitHub must contain enough technical and evidence context to continue work without Notion. When Notion is available, synchronize motivation, decision, exact reality, evidence, limitations, PR and final merge SHA in the same cycle.

## 10. Change discipline

1. establish exact base/head and phase scope;
2. identify whether a claim concerns `main`, an open PR or future work;
3. inspect affected contracts/tests/downstream documents;
4. make the smallest coherent change;
5. validate it;
6. update GitHub and Notion records;
7. open or update a PR with exact evidence and limitations;
8. inspect final diff, checks, artifacts, reviews and unresolved threads;
9. merge only with expected head SHA.

Do not combine P4 finalization with P5, deletion execution, production deployment, source recovery or ecosystem wiring.
