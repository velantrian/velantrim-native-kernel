# ADR-0023 — Harden SQLite WAL runtime and stored Event integrity

- **Decision status:** `ACCEPTED`
- **Evidence level:** `REPOSITORY_REPRODUCED / EVIDENCE_CAPTURED`
- **Implementation status:** `MERGED VIA PR #69 / POST-MERGE REVIEW FOLLOW-UP IN DRAFT PR #72`
- **Operator approval:** `APPROVED`
- **Date:** `2026-08-08`
- **Decider:** `@velantrian`
- **Track:** `C — Clean Implementation / SQLite Profile Hardening`
- **Related:** ADR-0012, ADR-0019, ADR-0021, Issue #15, Issue #17

## Context

The retained P5/C3/C4/C5 evidence used runner SQLite 3.45.1 and the profile enabled WAL on every connection. SQLite upstream later documented a rare WAL-reset corruption bug affecting 3.7.0 through 3.51.2, fixed in 3.51.3. The failure requires multiple connections plus concurrent write/checkpoint timing, but its consequence can be database corruption.

An audit also reproduced an independent verifier defect: the SQLite profile accepted a canonical and re-hashed Event envelope whose `contract`, `recorded_at`, nested `payload`, or undeclared fields differed from the stored Event. PostgreSQL rejected the first three mismatches, but neither profile required the exact envelope key set.

Additional reproduction showed that SQLite migration use of `executescript()` could leave the explicit transaction and that `timeout_seconds` was overwritten by a fixed 5000 ms busy timeout.

## Decision

### WAL version gate

1. The SQLite WAL profile requires the **actually linked SQLite library** to be at least 3.51.3.
2. The guard runs before opening the database and fails closed with `UnsafeSQLiteVersion`.
3. CI builds official SQLite 3.51.3 from a pinned archive and verifies SHA-256 before compilation.
4. Evidence metadata must equal the linked runtime version; an environment variable cannot silently substitute another version.
5. Branch-specific backports are not accepted implicitly. A future backport requires an explicit allowlist entry and its own reproducible CI job.

### Stored Event verification

Both SQLite and PostgreSQL verifiers require the exact v1 Event envelope field set and equality for:

```text
contract · event_id · command_id · idempotency_key
stream_id · global_seq · stream_seq
actor_ref · authority_ref · recorded_at
event_type · schema_version · payload
prev_global_hash · payload_hash · event_hash
```

SQLite JSON decode failures are normalized to `StoredEventCorrupt`. Canonical payload bytes, nested envelope payload, stored columns and both hashes must agree.

Post-merge review established that Python structural equality is not type-exact for JSON because `True == 1` and `False == 0`. Event field equality therefore compares canonical JSON bytes per field in both profiles. This preserves the JSON type distinction for payloads and sequence fields instead of relying on Python `==`.

### Evidence and workflow follow-up

1. `nk-evidence-bundle/1` is compatibly extended with optional, schema-declared ADR-0023 revalidation fields; the historical bundle remains valid without them.
2. The ADR-0023 bundle verifier binds each checkpoint role to its exact commit and P5/C3, C4 and C5 workflow run IDs. Positive integers alone are insufficient evidence identity.
3. P5/C3, C4 and C5 pull-request and `main` path filters include `tools/sqlite/**`, because all three workflows execute the pinned SQLite builder.

### Transaction and timeout behavior

- SQLite migrations execute statement-by-statement inside the caller-owned transaction; `executescript()` is not used.
- `timeout_seconds` controls both connection timeout and `PRAGMA busy_timeout`.
- WAL activation and required pragmas are checked rather than assumed.

## Evidence impact

The 2026-08-07 C5 ZIPs remain immutable historical evidence of the runs that produced them. They are not deleted, rewritten, or represented as having used a fixed SQLite library.

```text
historical PASS on SQLite 3.45.1
≠ recommendation to continue using 3.45.1
≠ proof that the WAL-reset race could not occur
```

The assertion arithmetic remains `45 / 10 / 17 / 0` and `NK-EPI` remains `0 / 8 SUPPORTED`. P5/C3/C4/C5 was reproduced at PR head `ab7a203c…` and merged main `675aa4b3…` on linked SQLite 3.51.3; the exact C5 ZIPs are separately recorded under `evidence/c5/2026-08-08-adr0023/`. Re-adjudication preserved the existing labels and did not promote or demote assertions by wording alone.

The retained ADR-0023 ZIPs predate the type-exact comparison and verifier/workflow follow-up. Their bytes and producing-run claims remain unchanged; they are not relabelled as evidence of later code. The follow-up requires its own exact PR and `main` CI results before completion can be claimed.

## Rejected alternatives

### Keep SQLite 3.45.1 because the bug is rare

Rejected. Low probability does not justify knowingly retaining a corruption range in a profile centered on durable history and replay evidence.

### Trust `NK_SQLITE_VERSION` without checking the loaded library

Rejected. Evidence metadata must describe the executable runtime, not an unverified declaration.

### Add an unreviewed alternative Python SQLite wrapper

Rejected for this slice. The profile remains standard-library `sqlite3`; CI supplies a safe linked SQLite library.

### Rewrite or discard old evidence

Rejected. New evidence must be additive and must not erase the exact historical bytes or their limitations.

## Boundaries

```text
safe SQLite version + strict envelope verification
≠ complete Event Integrity
≠ privileged-rewrite protection
≠ operational equivalence with PostgreSQL
≠ production readiness
≠ physical deletion
≠ NK-EPI promotion
≠ ecosystem authority
```

Reducer referential rules, `nkc1` admission enforcement, quarantine visibility, deletion semantics, event-ID scope, and independent-language readers remain separate contract/implementation work.

## Verification

```bash
tools/sqlite/build_safe_sqlite.sh /tmp/native-kernel-sqlite-3.51.3 /usr/bin/python3
LD_LIBRARY_PATH=/tmp/native-kernel-sqlite-3.51.3/lib \
  /usr/bin/python3 -m unittest tests.test_sqlite_profile_unit -v
```

Repository completion was established by four-job P5/C3, C4, and C5 matrices at both remediation checkpoints plus a new additive evidence identity. The older archives remain unchanged.
