# 🤖 Velantrim Native Kernel repository guidance

This file is the mandatory entry point for AI coding agents, auditors, reviewers and automated contributors.

## 1. Required reading order

1. [`README.md`](README.md) — public purpose and maturity.
2. [`STATUS.md`](STATUS.md) — authoritative implementation/evidence boundary.
3. [`docs/ai/README.md`](docs/ai/README.md) — context-pack map.
4. [`docs/ai/DOCUMENTATION_SYNC_PROTOCOL.md`](docs/ai/DOCUMENTATION_SYNC_PROTOCOL.md).
5. [`docs/ai/CURRENT_STATE.md`](docs/ai/CURRENT_STATE.md).
6. [`docs/ai/P5_IMPLEMENTATION_RECORD.md`](docs/ai/P5_IMPLEMENTATION_RECORD.md) for SQLite/C3 work.
7. [`docs/ai/P4_IMPLEMENTATION_RECORD.md`](docs/ai/P4_IMPLEMENTATION_RECORD.md) for PostgreSQL C2 foundation.
8. Relevant section of [`docs/ai/COMPONENT_MAP.md`](docs/ai/COMPONENT_MAP.md).
9. Relevant entries in [`docs/ai/KNOWN_RISKS.md`](docs/ai/KNOWN_RISKS.md).
10. Recent entries in [`docs/ai/WORK_LOG.md`](docs/ai/WORK_LOG.md).
11. [`docs/ai/AUDIT_PLAYBOOK.md`](docs/ai/AUDIT_PLAYBOOK.md) for audits.

Then inspect only affected contracts, source, tests, manifests, workflows, RFCs, ADRs, PRs and issues. Documentation is orientation, not self-proving evidence.

## 2. Source-of-truth order

1. executable code and committed tests at the exact SHA;
2. exact-SHA CI jobs, logs and artifacts;
3. `STATUS.md` and current-state records;
4. accepted ADRs and normative contracts;
5. current RFCs/research with explicit statuses;
6. PRs, issues and work logs;
7. historical chats, audits and external reports.

Never treat an open PR, Notion page, approval or detailed design as behaviour already present in `main`.

## 3. Required distinctions

```text
Decision status
≠ Implementation status
≠ Evidence level
≠ Operator approval

C1 ≠ C2 ≠ C3
C3 semantic equivalence ≠ operational equivalence
```

Distinguish documented, proposed, accepted, implemented, tested, wired, enabled and observed.

## 4. Architecture discipline

- Preserve `Architecture Canon → Abstract Contracts → Replaceable Implementation Profiles`.
- PostgreSQL, SQLite, Python, Psycopg, SQL layouts, files, LLMs, embeddings, graphs, CPUs/GPUs and future substrates are replaceable instruments, not Canon.
- Event history is authoritative about recorded history, not automatically truth.
- Relevance, recency, utility, repetition, write order and model confidence do not independently establish truth.
- A Receipt, evidence report or equivalence report proves only its declared operation, checks and limitations.
- Operator approval is authority, not empirical evidence.

## 5. Current P5 boundary

Current branch maturity:

```text
RESEARCH / P5 PARTIAL CROSS-PROFILE CONFORMANCE / NOT PRODUCTION-READY
```

Profiles:

```text
native-kernel/postgresql-reference@0.4-p4
native-kernel/sqlite-embedded@0.5-p5
```

Single-profile C2 map:

```text
41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
```

Cross-profile C3 map:

```text
45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
support_state: PARTIAL
```

Repository C3 applies only to the 45 `SUPPORTED` results in the exact comparison report.

```text
C3 ≠ support for all 72
C3 ≠ PostgreSQL/SQLite operational equivalence
C3 ≠ truth/authenticity
C3 ≠ physical deletion
C3 ≠ C4/C5
C3 ≠ production readiness
```

Cross-profile evidence promotes only `NK-SEM-008`, `NK-ID-008`, `NK-EQV-002`, `NK-EQV-003`. All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

## 6. Profile independence

The SQLite profile must remain materially independent:

- no calls into PostgreSQL append/replay/projection/Receipt adapters;
- own migrations, schema, transaction/fencing and persistence code;
- shared profile-neutral contracts and fixtures are allowed;
- cross-profile comparison must operate on observable contract outcomes, not schema similarity.

Allowed differences must be declared. Payload/order/state/Receipt differences must never be hidden by normalization.

## 7. Issue #1 boundary

The clean P1–P5 implementation is not recovered historical `v0.1.2.1` and not the original 44-test suite.

- Do not label newly written code/tests as recovered history.
- `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.
- Issue #1 recovery remains independent.
- Issue #18 licensing/publication remains independent.

## 8. Cross-project boundaries

- Native Kernel owns neutral semantic memory/Event/evidence contracts and bounded profiles.
- Titan owns cognition, retrieval, tools and orchestration.
- Mentaury Soul owns digital individuality and continuity.
- Crystal owns verifiable-memory, evidence and product boundaries.

No identity, authority, credential, runtime, storage or conformance status is inherited automatically across projects.

## 9. Verification routes

### P1–P4 prerequisite checks

Run the narrow affected suites and inspect exact repository runs. P5 workflow also runs P1–P4 regressions.

### P5 SQLite/C3

```bash
python -m unittest discover -s tests -p 'test_sqlite_profile_unit.py' -v
python -m unittest discover -s tests -p 'test_p5_sqlite_integration.py' -v
python -m unittest discover -s tests -p 'test_p5_report_validator.py' -v
python -m unittest discover -s tests -p 'test_p5_manifest.py' -v
python tools/profiles/validate_p5_manifest.py

NK_TEST_POSTGRES_DSN='postgresql://...' \
  python -m unittest discover -s tests -p 'test_p5_cross_profile_integration.py' -v
```

Repository evidence requires:

- all four Python/PostgreSQL matrix jobs PASS;
- SQLite version recorded;
- PostgreSQL P4, SQLite P5 and C3 reports generated and validated;
- four retained artifacts, each containing all three reports;
- exact head/run/artifact traceability;
- final-head re-run after documentation changes.

Do not claim:

- C2/C3 from local tests alone;
- C3 from environment-version diversity;
- full support from top-level C3;
- operational equivalence from semantic comparison;
- truth, authenticity or physical erasure from hashes/Receipts/reports;
- production safety/privacy/security without operational proof.

## 10. Documentation and Notion synchronization

Material changes must update relevant GitHub documents:

- `STATUS.md`;
- `docs/ai/CURRENT_STATE.md`;
- `docs/ai/P5_IMPLEMENTATION_RECORD.md`;
- `docs/ai/KNOWN_RISKS.md`;
- `docs/ai/COMPONENT_MAP.md`;
- `docs/ai/WORK_LOG.md`;
- relevant ADR/RFC/profile/package documents.

Classify impact as `NONE`, `GITHUB_ONLY` or `GITHUB_AND_NOTION`.

GitHub must contain enough technical/evidence context to continue without Notion. When Notion is available, synchronize motivation, exact reality, evidence, limitations, PR and merge SHA in the same cycle.

## 11. Change discipline

1. establish exact base/head and phase scope;
2. identify whether a claim concerns `main`, an open PR or future work;
3. inspect affected contracts/tests/downstream documents;
4. make the smallest coherent change;
5. validate it;
6. update GitHub and Notion records;
7. open/update a PR with exact evidence and limitations;
8. inspect final diff, checks, artifacts, reviews and unresolved threads;
9. merge only with expected head SHA.

Do not combine P5 finalization with C4/C5, deletion execution, production deployment, source recovery or ecosystem wiring.
