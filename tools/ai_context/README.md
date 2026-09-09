# 🤖 AI context validation tools

These standard-library utilities validate the repository's AI orientation, Formal Authority routing and current-state surfaces.

They are support/governance tooling only.

```text
AI-context guard PASS
≠ Native Kernel runtime PASS
≠ architecture correctness
≠ H11 reviewer qualification
≠ Notion synchronization proof
≠ authentic v0.1.2.1 recovery
```

## Static validator

Run from the repository root:

```bash
python tools/ai_context/validate_context.py --repo .
```

The validator checks that:

- mandatory AI-context, architecture and governance files exist;
- selected first-read Markdown files have valid repository-relative links and do not escape the repository;
- `ARCHITECTURE.md` routes through the Integrated A1–A10 Review and IAR-1 reconciliation rather than treating the first drafts as the final interpretation;
- `docs/ai/project_manifest.yaml` exposes the same Formal Authority routing;
- `docs/ai/CURRENT_STATE.md` and `docs/ai/README.md` contain the current blocked H11 boundary;
- obsolete D6/post-D8 current-looking markers are rejected from those current-only agent surfaces.

Historical chronology is not required to remain duplicated inside current-only agent documents. It remains preserved in `STATUS.md`, `ROADMAP.md`, `docs/research/**`, `docs/reviews/**`, evidence records, work logs/reconciliation records where applicable, and Git history.

Machine checkpoint integrity is validated by the dedicated `validate_project_state.py`, H11 validators and reconciliation validators. `validate_context.py` does not create a second checkpoint authority.

## Live GitHub surface freshness guard

Run from the repository root when live GitHub access is available:

```bash
python tools/ai_context/validate_live_github_surface.py --repo .
```

The live guard does not invent a second current-surface registry. It reads the existing machine-readable binding from `docs/ai/CURRENT_STATE.md`:

```text
open_review_surface: Issue #178
```

and the repository identity/current Issue state from `project-state.json`, then resolves that exact Issue or PR through the GitHub API.

Because the field is explicitly named `open_review_surface`, the referenced live object must be `OPEN`. A merged/closed PR or closed Issue is a validation failure. If GitHub cannot be reached, the live state is `UNKNOWN` and the validator fails closed instead of treating unavailable evidence as a pass.

This guard is specifically intended to catch the class of drift where a current-state document still routes to a PR after that PR has merged/closed. It checks routing freshness only:

```text
live surface guard PASS
≠ reviewer qualification
≠ H11 admission
≠ H11 execution
≠ runtime thaw
≠ Final Canon
≠ production authorization
```

The CI job supplies a read-only GitHub token and runs the live check once on Python 3.12 after the offline/unit guards have passed.

## Tests

```bash
python -m unittest discover -s tests -p 'test_ai_context_validator.py' -v
python -m unittest discover -s tests -p 'test_live_github_surface_validator.py' -v
```

The static-validator tests cover valid current/authority surfaces, missing required files, broken links, repository-escape links, required current markers and rejection of stale current-looking markers.

The live-surface tests use an injected offline fetcher and cover:

- current open Issue passes;
- the historical stale `PR #131 -> MERGED` routing class fails;
- a closed Issue fails;
- unavailable live GitHub state fails closed as `UNKNOWN`;
- missing or non-open machine state for a current Issue fails;
- a mismatched live object number fails closed;
- duplicate current-surface bindings are rejected.

## CI boundary

`.github/workflows/ai-context.yml` runs read-only on relevant pull requests, pushes to `main`, and manual dispatches. The live GitHub step has read-only `contents`, `issues` and `pull-requests` permissions.

Passing these guards proves continuity/routing constraints only. It does not prove the reconciled architecture universally correct, qualify H11 independence, execute H11, thaw runtime or authorize production.
