# Source Recovery Records

> **Status:** `ACTIVE / STAGE 0.5 / AUTHENTIC SOURCE NOT LOCATED`  
> **Scope:** recovery of the reported external `v0.1.2.1` checkpoint and original 44-test suite  
> **Authority:** these records document search evidence; they do not authenticate a candidate by themselves

## Purpose

This directory preserves the source-recovery process for Issue #1.

The recovery objective is narrow:

```text
identify authentic source or immutable archive
→ preserve it read-only
→ record lineage and archive hash
→ verify the original test inventory
→ operator provenance decision
→ exact controlled import
```

A detailed architecture description, matching behaviour, matching file names, or a replacement suite containing 44 tests is not proof that an artifact is the externally reported `v0.1.2.1` snapshot.

## Current evidence boundary

The connected and accessible sources searched so far contain only derived documentation and historical claims. No authentic source archive, original `kernel.py`, original test suite, original benchmark harness, or complete original environment has been located.

This supports the statement:

```text
NOT LOCATED IN THE DECLARED ACCESSIBLE SOURCES
```

It does not yet support the stronger statement:

```text
GLOBALLY LOST
```

The stronger state requires an explicit operator decision after locally controlled devices, backups, removable media, private archives, and any inaccessible historical environments have been checked.

## Required search record

Each sweep must record:

- stable `search_id`;
- date and actor;
- scope and access limitations;
- exact locations or source surfaces checked;
- queries or identifiers used;
- candidate artifacts discovered;
- hashes where bytes were accessible;
- false positives and why they were rejected;
- conclusion and remaining inaccessible surfaces.

## Candidate handling

Any candidate artifact must be handled as untrusted and read-only.

1. Do not execute it on a trusted host.
2. Do not edit, normalize, rename, or unpack destructively before hashing the original container.
3. Record archive-level SHA-256 and byte size first.
4. Extract into an isolated directory without overwriting the original.
5. Refuse symlinks, path traversal, device files, and unexpected executable installers during initial inspection.
6. Generate a candidate manifest with status `UNVERIFIED_CANDIDATE`.
7. Compare provenance, file inventory, test identity, version labels, environment metadata, and historical references.
8. Only the operator may promote a candidate to `AUTHENTIC_RECOVERED`.

## Tooling

Repository utilities under `tools/source_recovery/` can:

- generate a deterministic candidate file inventory;
- compute archive and per-file SHA-256 values;
- hash normalized test node IDs;
- verify a manifest against recovered bytes;
- reject path traversal, duplicate paths, symlinks, missing files, size drift, and hash drift.

These tools verify byte consistency. They do not prove historical authenticity.

## Records

- [`2026-07-26-accessible-sources-sweep.md`](./2026-07-26-accessible-sources-sweep.md) — connected GitHub, Notion, ChatGPT Library, and conversation-file sweep.
- [`2026-08-09-bootstrap-branch-resweep.md`](./2026-08-09-bootstrap-branch-resweep.md) — full lineage and tree inspection of the retained `bootstrap/research-kernel-v0.1.2.1` docs branch, plus GitHub and Notion resweep.

## Decision outcomes

### Authentic candidate accepted

```text
UNVERIFIED_CANDIDATE
→ provenance review
→ OPERATOR APPROVED
→ AUTHENTIC_RECOVERED
→ Stage 1 import PR
```

### No authentic source recoverable

```text
declared local and connected-source search completed
→ operator records checkpoint as
  LOST / NON-REPRODUCIBLE EXTERNAL CHECKPOINT
→ new clean implementation receives
  a new version and independent evidence lineage
```

No reconstructed implementation may inherit the reported `v0.1.2.1` evidence state.
