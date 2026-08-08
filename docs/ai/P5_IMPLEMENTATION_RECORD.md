# 🧩 P5 SQLite & Cross-Profile C3 Implementation Record

**Recorded:** 2026-08-07  
**Implementation base:** `1dc493e9d23b99ee4bbf6015348599cd56f6cb56`  
**Verified implementation main:** `a8bb0ae232b977856730a1a4f21f977c1f69ca0a`  
**Issue / PR / ADR:** #58 / #59 / ADR-0019 `ACCEPTED / APPROVED`

> **2026-08-08 integrity amendment:** ADR-0023 introduces strict Event Envelope verification and a fail-closed linked SQLite 3.51.3 WAL floor. The matrices below remain historical 3.45.1 evidence and are under bounded integrity revalidation; they are not rewritten. Assertion arithmetic and NK-EPI status remain unchanged pending new repository evidence.

## Profiles and lineages

```text
PostgreSQL: native-kernel/postgresql-reference@0.4-p4
Lineage:    clean/postgresql-reference/0.1

SQLite:     native-kernel/sqlite-embedded@0.5-p5
Lineage:    clean/sqlite-embedded/0.1
```

SQLite is materially independent and uses Python standard-library `sqlite3`; it does not call PostgreSQL append, replay, projection or Receipt adapters.

## Final maturity

```text
P1–P4:                 MERGED / REPOSITORY-REPRODUCED
P5 SQLite profile:     MERGED / PARTIAL / C2 REPOSITORY-REPRODUCED
Cross-profile C3:      MERGED / PARTIAL / REPOSITORY-REPRODUCED
support_state:         PARTIAL
C4/C5:                 NOT ESTABLISHED / NOT AUTHORIZED
Production readiness: NOT CLAIMED
```

## Result maps

```text
SQLite C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
C3:        45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
```

C3 promotes exactly `NK-SEM-008`, `NK-ID-008`, `NK-EQV-002` and `NK-EQV-003`. All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

## Independent SQLite route

```text
stdlib sqlite3
→ linked SQLite >= 3.51.3 WAL guard
→ migration ledger + digest drift guard
→ atomic statement-by-statement migrations
→ Kernel-instance registration
→ BEGIN IMMEDIATE single-writer transaction
→ owner / epoch / expiry fence
→ durable idempotency + rollback-safe sequence allocation
→ canonical Event commitments + hash chain
→ persisted replay + disposable projections
→ bounded operational Receipts
→ exact PostgreSQL authoritative-history import
```

## Cross-profile route

```text
same registry + fixture pack
→ independent PostgreSQL workload
→ independent SQLite workload
→ normalized append/Event outcomes
→ replay/projection/Receipt comparison
→ exact PostgreSQL Event import into SQLite
→ BYTE / STRUCTURAL / SEMANTIC / BEHAVIOURAL checks
→ nk-equivalence-report/1
```

Allowed differences include SQL/layout, server versus file topology, row locks versus `BEGIN IMMEDIATE`, independently generated Event IDs/timestamps and operational IAM/network/failover/concurrency capabilities.

Forbidden differences include canonical identity, Command digest, payload/order semantics, hash-chain validity, reducer/projection canonical state, rejection outcomes, Receipt proof fields and exact imported Event bytes/hashes.

## PR-head evidence

```text
Final head: 6483c9a229aea7d49929745b7652e67f1c39949c
P5/C3:      31182711376 — PASS
P4:         31182710450 — PASS
P1:         31182711652 — PASS
Fixtures:   31182710461 — PASS
AI context: 31182710710 — PASS
```

Final-head artifacts:

| Environment | Digest |
|---|---|
| Python 3.11 / PostgreSQL 16 | `sha256:ca1c1266b7b0d9307978bd1a4beadf95139a55c1b8facca4ab641c1d7d502c9c` |
| Python 3.11 / PostgreSQL 18 | `sha256:1ffcd7248ba74ffdcdd15dbfb9c86289c9f0357fd151e0d74187b30f740ace8a` |
| Python 3.12 / PostgreSQL 16 | `sha256:33b022cc9dda1a03e44bce0ca6e0e7622bcddb898764ddb11d010b348b6ea441` |
| Python 3.12 / PostgreSQL 18 | `sha256:d10647dec21c84edd1e4fc94425c048aa63d6c77b8f4952337dc5096a624ccde` |

## Implementation merge and main evidence

```text
PR #59 merge/main: a8bb0ae232b977856730a1a4f21f977c1f69ca0a
P5/C3 main run:    31183074126 — PASS
P4 main run:       31183074048 — PASS
P1 main run:       31183073948 — PASS
Fixtures:          31183073969 — PASS
AI context:        31183073997 — PASS
```

Main matrix:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Each artifact contains:

```text
postgresql-p4-report.json
sqlite-p5-report.json
c3-equivalence-report.json
```

Main-bound artifact digests:

| Environment | Digest |
|---|---|
| Python 3.11 / PostgreSQL 16 | `sha256:ca509f6fe9c1bb56c904399e7e6b60e2c743682aa8af21b006b1d1d5bcb6ea4c` |
| Python 3.11 / PostgreSQL 18 | `sha256:728bcb72a414b3c342e4ed03309593db5c0322e145a7dfc4c5d1834650fa422c` |
| Python 3.12 / PostgreSQL 16 | `sha256:a0c99b14a27f241dba7b6f37e45e80c592d25e0fae42934fab654a6430fc2d35` |
| Python 3.12 / PostgreSQL 18 | `sha256:2264682a85720db3c0512fa75466016466b54abb1e0a99274b9f2f99dc2274fb` |

Artifacts expire on 2026-09-06. A main-bound archive was downloaded and inspected; it contained all three reports. The C3 report named exact main/run/Python/PostgreSQL/SQLite metadata, contained 72 assertion results with `45/10/17/0`, and all eight comparison checks were `PASS`.

## Negative evidence and fixes

1. Three tests initially referenced a non-existent nested fixture path; corrected to committed `contracts/fixture-pack.json`.
2. The generic single-profile runner rejected `nk-equivalence-report/1`; C3 now uses the dedicated comparator and equivalence validator without weakening either protocol.
3. Bot-authored commits produced `action_required` nested workflows; those statuses were never counted as evidence.
4. Temporary bootstrap archives and workflows were removed before review.

## Exact boundary

```text
C3 for 45 SUPPORTED assertions
≠ support for all 72
≠ PostgreSQL and SQLite operational equivalence
≠ truth/authenticity
≠ physical or cryptographic deletion
≠ complete conflict subsystem
≠ C4/C5
≠ production readiness
```

## Remaining risks

- comparison scenarios are bounded, not exhaustive;
- concurrency, failover, backup/restore and managed-provider behavior are not equivalent;
- complete conflict representation/resolution remains absent;
- physical deletion and restore-before-visibility remain absent;
- artifacts expire;
- future contract/profile changes require renewed C3 evidence;
- historical SQLite 3.45.1 evidence requires ADR-0023 safe-version reproduction;
- Issue #18 publication/licensing remains unresolved.

## Publication completion

The implementation and main-push evidence are complete. Remaining work in this cycle is the docs-only checkpoint, Notion synchronization and Issue #58 closure. Later phases require a new explicit operator GO.
