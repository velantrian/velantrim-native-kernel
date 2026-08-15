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

## Validator

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

## Tests

```bash
python -m unittest discover -s tests -p 'test_ai_context_validator.py' -v
```

The tests cover valid current/authority surfaces, missing required files, broken links, repository-escape links, required current markers and rejection of stale current-looking markers.

## CI boundary

`.github/workflows/ai-context.yml` runs read-only on relevant pull requests, pushes to `main`, and manual dispatches.

Passing this guard proves continuity/routing constraints only. It does not prove the reconciled architecture universally correct, qualify H11 independence, execute H11, thaw runtime or authorize production.
