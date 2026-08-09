# Bootstrap `v0.1.2.1` Documentation-Lineage Manifest

> **Manifest ID:** `NK-SRC-LINEAGE-20260809-001`  
> **Purpose:** preserve the exact inspected lineage behind recovery record `NK-SRC-RECOVERY-20260809-004`  
> **Original mutable ref:** `bootstrap/research-kernel-v0.1.2.1`  
> **Archived reachability ref:** `archive/bootstrap-v0.1.2.1-docs-lineage`  
> **Exact head:** `d64855afc4b34bcfb0ed8f1c3766925d287b07c6`  
> **Exact head tree:** `fc1549531990badde0a5f67fa140f9e143bbbaa0`  
> **Classification:** `MERGED_DOCS_BOOTSTRAP_BRANCH / SOURCE_BEARING_FALSE`

## Evidence boundary

This manifest preserves the commit chain, tree identities, changed-path inventory, and exact head-tree inventory used to classify the retained bootstrap branch as documentation-only.

It does not authenticate or recover the reported external `v0.1.2.1` runtime. It does not prove that the historical source is globally lost.

The archival branch is an additional reachability anchor. The repository-resident manifest is the durable review record; no claim is made that a GitHub ref is cryptographically undeletable.

## Complete reachable commit chain

The chain is single-parent and contains 14 commits. The first commit added only `.gitignore` and `README.md`. Every later commit added or modified only the Markdown paths listed below. No commit added, deleted, renamed, or modified a runtime source file, test file, benchmark executable, dependency lock, environment export, source archive, or CI workflow.

| # | Commit | Tree | Parent | Timestamp (UTC) | Message | Changed paths |
|---:|---|---|---|---|---|---|
| 1 | `636781fbaff98d3c331ae5948e5ad10e797d60c6` | `2137fef1cea20366f5b5b335590d15b56b28886b` | none | `2026-07-22T16:46:50Z` | Initial commit | `.gitignore` added; `README.md` added |
| 2 | `92bf1309cf8ac3db6a866011134ee438226dfdfc` | `4ee3f4ed758386c0b4b31ac82b847bf1aa6e5907` | `636781fbaff98d3c331ae5948e5ad10e797d60c6` | `2026-07-22T16:56:11Z` | docs: establish Native Kernel research overview | `README.md` modified |
| 3 | `8e6b009f1ef449859ad588cf1de02f6943b3b2b5` | `3647748d0852be0cda05a18985ef34e6648338cb` | `92bf1309cf8ac3db6a866011134ee438226dfdfc` | `2026-07-22T16:56:48Z` | docs: define exact repository status boundary | `STATUS.md` added |
| 4 | `c95ab689bbaca9bc3f5077a0116e7b153168c93c` | `119c49ed60a9c9ca4e43809439502504fff46d8a` | `8e6b009f1ef449859ad588cf1de02f6943b3b2b5` | `2026-07-22T16:57:28Z` | docs: add Native Kernel architecture and invariants | `ARCHITECTURE.md` added |
| 5 | `41c75de3e9fd2976500489eb732f80bea929fa54` | `d84351119426094e0c38f95bf2957530489e15c4` | `c95ab689bbaca9bc3f5077a0116e7b153168c93c` | `2026-07-22T16:58:21Z` | docs: add staged Native Kernel roadmap | `ROADMAP.md` added |
| 6 | `a3d24f314d06f77404a88001230da7ae066288cd` | `2bbfbf4897b4a0d3d76482ede3be5a7c18b76e30` | `41c75de3e9fd2976500489eb732f80bea929fa54` | `2026-07-22T16:59:05Z` | docs: add benchmark methodology and evidence boundary | `docs/BENCHMARKS.md` added |
| 7 | `59caf04e9fe0eacdc3ff830a85d6bce5cef2c651` | `117ee16032a48f5827b8baf60bd661874b80fc49` | `a3d24f314d06f77404a88001230da7ae066288cd` | `2026-07-22T16:59:50Z` | docs: define Titan and Crystal integration boundaries | `docs/INTEGRATION_BOUNDARIES.md` added |
| 8 | `e029cff4361e849b27fc60417904257cf8542503` | `7e1555272335f4cdf5f141b193e71ee365078286` | `59caf04e9fe0eacdc3ff830a85d6bce5cef2c651` | `2026-07-22T17:00:15Z` | docs: add research-stage security policy | `SECURITY.md` added |
| 9 | `e3f325447c19271cf1c03299f7d1c0ac1c0ac468` | `47d9d66c05e4dfecee622e6c3f4c71efc2ae82d2` | `e029cff4361e849b27fc60417904257cf8542503` | `2026-07-22T17:00:45Z` | docs: add contribution and status discipline | `CONTRIBUTING.md` added |
| 10 | `5d5f496e0929be3062e9376cfc4d0911229612ce` | `1af879d28103a8fa2e189af78aae19e2c56880a0` | `e3f325447c19271cf1c03299f7d1c0ac1c0ac468` | `2026-07-22T17:01:16Z` | docs: add controlled prototype import plan | `prototype/README.md` added |
| 11 | `b3e942db3b24a7db7f0cbc5008dd760a95662d3a` | `f1ca6e5d9d433b4fc9afa878ca0f146ca75cce27` | `5d5f496e0929be3062e9376cfc4d0911229612ce` | `2026-07-22T19:55:45Z` | docs: align repository maturity terminology | `README.md` modified |
| 12 | `da5d019d85d2c6e00abd58af8e228e4279f42be9` | `670158b8b624cdf38ef8812f471a4f44124044e3` | `b3e942db3b24a7db7f0cbc5008dd760a95662d3a` | `2026-07-22T19:56:12Z` | docs: standardize documented-only status | `STATUS.md` modified |
| 13 | `c85d3da51997b2e388ab45e85ffc5639ef667178` | `e2c8aa3f1babdb4486ae17f04b8fcd13b0834daa` | `da5d019d85d2c6e00abd58af8e228e4279f42be9` | `2026-07-22T19:56:37Z` | docs: align prototype import status terminology | `prototype/README.md` modified |
| 14 | `d64855afc4b34bcfb0ed8f1c3766925d287b07c6` | `fc1549531990badde0a5f67fa140f9e143bbbaa0` | `c85d3da51997b2e388ab45e85ffc5639ef667178` | `2026-07-22T19:57:12Z` | docs: standardize evidence grip terminology | `ARCHITECTURE.md` modified |

## Exact head-tree inventory

The recursive head tree was not truncated.

| Path | Type | Mode | Git object SHA | Bytes |
|---|---|---|---|---:|
| `.gitignore` | blob | `100644` | `83972fadc2724842e111d0d3e2829a59ae3d3f45` | 4628 |
| `ARCHITECTURE.md` | blob | `100644` | `f81d4d16a2b069c7fbb3240649d0156f0222aee7` | 6062 |
| `CONTRIBUTING.md` | blob | `100644` | `29c4005eed155ffcffa4a390571f88920c5bf823` | 1940 |
| `README.md` | blob | `100644` | `0fd652fa668f4f42bf8f1b465184ea5732318d2f` | 4182 |
| `ROADMAP.md` | blob | `100644` | `725ddb2b4ee0cf8a7b54261f67ea1dd99dea0a52` | 4140 |
| `SECURITY.md` | blob | `100644` | `3708ab6ac99feb7e26d4744c0e3cf0dc2eeb2414` | 1492 |
| `STATUS.md` | blob | `100644` | `da27a07f14c723a71f67591d3d7867002ee564af` | 3099 |
| `docs/BENCHMARKS.md` | blob | `100644` | `9394ebdeec0730c47e10ec5ba393f21cc87ad11f` | 2475 |
| `docs/INTEGRATION_BOUNDARIES.md` | blob | `100644` | `af6c9ac4289cb72fddc4ec86abd342b011d54566` | 2207 |
| `prototype/README.md` | blob | `100644` | `7d95bb3f491ee1ac1cbfd8b84fd8722e984da938` | 1767 |

Directory tree objects:

- `docs` — `180964db3d04fb944dd85a3a1ebda010b2da3f59`;
- `prototype` — `7d0fd76a5095530466a0db1055187f5197aa4931`.

## Reproduction rule

A reviewer may verify the record by resolving either retained ref to `d64855afc4b34bcfb0ed8f1c3766925d287b07c6`, walking the single-parent chain, comparing each commit/tree identity above, and confirming the changed-path and final-tree inventories.

If both GitHub refs later become unavailable, this committed manifest still preserves the exact lineage and object identities used for the bounded classification, but it is not a byte-complete Git bundle and must not be represented as one.
