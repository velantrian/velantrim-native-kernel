# Source Recovery Sweep — 2026-07-26

> **Search ID:** `NK-SRC-RECOVERY-20260726-003`  
> **Result:** `NOT_FOUND_IN_ACCESSIBLE_SOURCES`  
> **Target:** reported external `v0.1.2.1`, original 44-test suite, benchmark harness, and environment metadata  
> **Decision impact:** Issue #1 remains blocked  
> **Global-loss claim:** not made

## 1. Search objective

Locate bytes or a concrete immutable archive that could plausibly be the authentic source of the historical claims:

```text
snapshot: v0.1.2.1
reported tests: 44 deterministic tests
reported engine version: 0.1.2.1
reported selection mode: lexical_proxy_ablation
reported conflict flag: conclusion_frozen
reported indexed helper: _canonical_neighbors
```

Documentation repeating these identifiers was treated as a reference, not as recovered source.

## 2. GitHub scope

### Repositories discovered through the connected GitHub installation

The accessible installation included the following Velantrim-related repositories, among others:

- `velantrian/velantrim-native-kernel`;
- `velantrian/velantrim`;
- `velantrian/Velantrim-ExoCortex-Titan`;
- `velantrian/velantrim-exocortex-crystal`;
- `velantrian/velantrim-core`;
- `velantrian/velantrim-eiti`;
- multiple historical Eiti repositories.

### Code-search queries

The connected code index was searched for:

```text
"v0.1.2.1"
"engine_version" "0.1.2.1"
"lexical_proxy_ablation"
"conclusion_frozen"
"_canonical_neighbors"
```

### Commit-search query

```text
v0.1.2.1
```

### GitHub result

- Exact `v0.1.2.1` matches resolved only to Native Kernel documentation and governance files in current `main`.
- No indexed source file containing the distinctive runtime identifiers was returned.
- No original test file, benchmark harness, source archive, or dependency lock tied to the claimed checkpoint was returned.
- Commit search produced unrelated release/documentation commits from other Velantrim projects and no authentic Native Kernel prototype commit.
- Issue #1 and merged PRs #12–#13 confirm that the public repository has no imported runtime baseline.

### GitHub limitations

- Code search may not index every repository or every historical branch.
- Connected search does not prove the absence of bytes in an inaccessible private repository, deleted fork, unindexed branch, detached local commit, local stash, or local reflog.
- The execution container had no DNS/network route to clone GitHub directly, so the connected GitHub API remained the authoritative accessible interface for this sweep.

## 3. Notion scope

Workspace search used the following queries and distinctive identifiers:

```text
"v0.1.2.1" kernel.py 44 tests source archive benchmark harness
"conclusion_frozen" "lexical_proxy_ablation" "_canonical_neighbors"
"44 / 44 tests green"
"kernel.py" Native Kernel prototype tests benchmark
```

### Notion result

- Results pointed only to the Native Kernel Hub, Prototype Status, Roadmap, and Titan Offline Shadow documentation.
- No page or attachment containing original runtime bytes, a source archive, original test files, or executable benchmark harness was returned.
- Exact searches for the distinctive runtime identifiers returned no source-bearing result.

### Notion limitations

- A deleted page, inaccessible workspace, unshared attachment, external link requiring separate credentials, or local Notion export may remain outside the connected scope.

## 4. ChatGPT Library and conversation files

The connected Library and current-conversation file surface were searched for:

```text
"v0.1.2.1" kernel.py 44 tests Velantrim Native Kernel
"44 / 44 tests green" kernel.py benchmark harness
Velantrim Native Kernel source archive test suite
```

The complete visible Library listing contained:

- `VELANTRIM_NATIVE_KERNEL_TZ_v1.0.md`;
- `Velantrim_v8_Crystal_v802.md`;
- `HYPERIA_FractalMemory_V5_26_ULTIMATE.md`;
- images and unrelated generated artifacts.

### Library result

- `VELANTRIM_NATIVE_KERNEL_TZ_v1.0.md` is a derived external specification, not source.
- The large Crystal and HYPERIA documents describe neighboring systems and contain code examples, but no authenticated Native Kernel `v0.1.2.1` snapshot or original 44-test inventory was identified.
- No `.py`, `.zip`, `.tar`, `.tar.gz`, `.7z`, dependency lock, or archive with a Native Kernel source-bearing title was present in the visible Library listing.

## 5. Candidate artifacts

```yaml
candidate_artifacts: []
```

No byte-level candidate was available to hash, quarantine, inspect, or compare.

## 6. False positives rejected

| Artifact or match | Why rejected |
|---|---|
| Native Kernel README/STATUS/ROADMAP references | derived documentation; no runtime bytes |
| Claude import specification | advisory specification created after the historical checkpoint |
| Notion Prototype Status page | historical claims and benchmark records; no source attachment |
| Crystal/HYPERIA code blocks | neighboring architectures with different contracts and lineage |
| Other Velantrim release commits | unrelated project/version lineage |

## 7. Conclusion

The accessible connected-source sweep found no authentic source or original suite.

Supported conclusion:

```text
The authentic v0.1.2.1 source snapshot and original 44-test suite
were not located in the GitHub, Notion, ChatGPT Library,
and current conversation sources accessible during this sweep.
```

Unsupported conclusion:

```text
The source is globally and permanently lost.
```

## 8. Remaining inaccessible surfaces

The following require operator-controlled local access and cannot be inspected through the current connectors:

- workstation and phone filesystems;
- Downloads, Documents, Desktop, project, temp, and archive directories;
- IDE local history;
- Git stashes, reflogs, worktrees, and unpushed branches on local clones;
- cloud-drive folders not connected to this workspace;
- email attachments;
- removable media;
- system backups and snapshots;
- old virtual machines, containers, or development environments;
- private repositories or organizations not granted to the connector;
- deleted or unshared Notion pages and exports.

## 9. Next gate

If a candidate is found on an inaccessible/local surface:

1. preserve the original archive read-only;
2. compute archive SHA-256 before extraction;
3. use the repository source-recovery tools to generate an `UNVERIFIED_CANDIDATE` manifest;
4. compare version labels, file inventory, test node IDs, environment, historical timestamps, and referenced behaviour;
5. record an operator provenance decision;
6. begin Stage 1 only after `AUTHENTIC_RECOVERED` is explicitly accepted.

If every declared local surface is checked and no candidate is found, create a separate operator decision recording `LOST / NON-REPRODUCIBLE EXTERNAL CHECKPOINT` before starting a new implementation lineage.
