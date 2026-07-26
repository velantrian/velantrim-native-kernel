# Source Recovery Utilities

These standard-library Python tools help inventory and verify a recovered-source candidate for Issue #1.

They do **not** authenticate a candidate.

```text
byte consistency
≠ historical provenance
≠ operator authenticity decision
```

## Safety boundary

Run the tools only after preserving the original candidate archive read-only and computing its hash. Do not execute recovered Python code on a trusted host merely to inspect it.

The tools:

- refuse symlinks in the candidate tree;
- refuse path traversal and duplicate manifest paths;
- hash files with SHA-256;
- record byte sizes;
- optionally hash the original archive;
- optionally hash a normalized test node-ID artifact;
- always generate `UNVERIFIED_CANDIDATE` status;
- never promote authenticity automatically.

They do not unpack archives, import candidate modules, install dependencies, or run the recovered test suite.

## 1. Preserve the archive

Example:

```bash
sha256sum /read-only/source/velantrim-native-kernel-v0.1.2.1.tar.zst
```

Record the original filename, size, hash, source location, date, and chain-of-custody notes before extraction.

## 2. Extract in isolation

Use a disposable environment and inspect archive entries before extraction. Reject absolute paths, `..`, symlinks, device files, and unexpected installers.

The extracted directory passed to the generator must contain regular files only.

## 3. Collect test node IDs

Only after the candidate has been quarantined and its environment is understood, collect test identities in an isolated environment. Store one node ID per line:

```text
tests/test_kernel.py::test_replay
tests/test_kernel.py::test_candidate_conflict
```

The manifest tool normalizes line endings and surrounding whitespace, preserves order, rejects duplicates, and hashes the final newline-terminated UTF-8 list.

## 4. Generate an unverified manifest

```bash
python tools/source_recovery/generate_manifest.py \
  /quarantine/extracted-v0.1.2.1 \
  --archive /read-only/source/velantrim-native-kernel-v0.1.2.1.tar.zst \
  --output /quarantine/v0.1.2.1.candidate.json \
  --recovered-from "encrypted backup / path / device" \
  --recovered-by "operator name" \
  --test-node-ids /quarantine/node_ids.txt \
  --original-test-command "python -m pytest -q"
```

The generated manifest remains:

```json
{
  "snapshot_status": "UNVERIFIED_CANDIDATE",
  "authenticity": {"decision": "PENDING"}
}
```

## 5. Verify bytes against the manifest

```bash
python tools/source_recovery/verify_manifest.py \
  /quarantine/v0.1.2.1.candidate.json \
  /quarantine/extracted-v0.1.2.1 \
  --archive /read-only/source/velantrim-native-kernel-v0.1.2.1.tar.zst \
  --test-node-ids /quarantine/node_ids.txt
```

Machine-readable result:

```bash
python tools/source_recovery/verify_manifest.py \
  manifest.json extracted/ \
  --archive original.tar.zst \
  --test-node-ids node_ids.txt \
  --json
```

A successful result contains:

```json
{
  "ok": true,
  "authenticity_proven": false
}
```

That `false` value is intentional.

## 6. Provenance review

Before an operator may mark a candidate `AUTHENTIC_RECOVERED`, review at least:

- original archive/container hash and timestamp context;
- source location and chain of custody;
- complete file inventory;
- version labels in code, tests, Receipts, and metadata;
- original test node IDs, fixtures, skips, and expected failures;
- dependency and Python environment;
- historical benchmark identifiers and workload definitions;
- correspondence with contemporaneous notes rather than later derived documentation;
- absence of reconstruction or silent semantic redesign.

## Tests

Utility tests run on Python 3.11 and 3.12 through `.github/workflows/source-recovery-tools.yml`.

This workflow validates only the recovery utilities. It is not Native Kernel runtime CI and does not reproduce the reported 44-test checkpoint.
