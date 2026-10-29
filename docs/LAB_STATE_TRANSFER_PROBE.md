# Draft read-only v1 state-export comparison probe

Proposed bounded tool based on `c9048bc75e0507babeabcfa8a5489a8ab780153d`.
Status: LAB_ONLY / NOT_CANON / NOT_RUNTIME. Owner requested experimental Draft PRs
on 2026-10-29. This proposal does not execute or adjudicate any A10 family.

`tools/lab/state_transfer_probe.py` reads two local JSON exports and validates them
with the existing `nk-p1-semantic-state/1` codec. Equal validated states report PASS;
different represented fields report FAIL with field names only. Unreadable,
unsupported or malformed input reports BLOCKED. No inputs are rewritten.

The tool checks represented last_global_seq, stream offsets, admitted claim IDs,
links, utilization counts, supersession and erased-claim IDs. Seven unittest methods
include a dedicated same/changed/invalid last_global_seq control, one loss case for
each of the other six fields, malformed and duplicate-key JSON, non-finite constants,
invalid UTF-8, excessive nesting, the 4 MiB input limit, unsupported exports,
content-light reports and CLI exit codes. The initial 20 semantic-core tests and
six probe methods passed locally (Python 3.12.14); the added regression is included
in the focused Python 3.11/3.12 GitHub Actions suite.

The focused `lab-state-transfer-probe.yml` workflow registers this test module on
Python 3.11/3.12 with explicit path triggers. Existing discovery/integrity gates
are preserved; no H11 experiment or new profile is executed by this workflow.

```bash
python -m tools.lab.state_transfer_probe source-state.json target-state.json
python -m unittest discover -s tests -p test_lab_state_transfer_probe.py -v
python -m unittest discover -s tests -p test_semantic_core.py -v
```

Exit codes: PASS=0, FAIL=1, BLOCKED=2. These are local diagnostic results, not
architecture qualifications or H11 outcomes.

**Limits:** equality of v1 exports cannot establish preservation of source payloads,
uncertainty or provenance not represented in this state format; it cannot verify a
database migration, physical erasure, an arbitrary substrate, permissions or truth.
A migration could produce two equally incomplete exports. There is no new database
profile, writer, runtime integration, semantic verb or acceptance threshold.
H11 admission remains blocked, H11 NOT_TESTED, runtime expansion FROZEN, Final Canon
deferred and production false. No frozen evidence or historical outcome changed.

Research context: Agent Memory Atlas's persistence/correction test ideas, pinned to
`da21abdef437812925c8332a8f6ff9bd90093faa`. This probe is an original local diagnostic;
no donor code was copied and the Atlas is not a Kernel authority or oracle.
