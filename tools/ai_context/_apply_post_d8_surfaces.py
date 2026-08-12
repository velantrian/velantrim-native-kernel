#!/usr/bin/env python3
from pathlib import Path
R=Path(__file__).resolve().parents[2]
D='57993f39906ae7266011f6146c9a485d0587d2bf'; N='RESIDUAL_A10_VALIDATION_PLAN'; H='A10-H03, A10-H06, A10-H08, A10-H09, A10-H10, A10-H11'
en=f'''<!-- POST_D8_OPERATOR_DECISION_CURRENT -->\n> [!IMPORTANT]\n> **Current post-D8 operator decision — 2026-08-12.** ADR-0027 / `OD-POST-D8-001` is `ACCEPTED / OPERATOR APPROVED` at `{D}`. A1–A10 remains `STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL`; Final Canon is **deferred**, product runtime remains `FROZEN`, production remains `false`. The only current next gate is `{N}` for {H}, and that gate is **RESEARCH_PLANNING_ONLY** — no residual experiment execution is authorized. Any lower `D6 NEXT`, `D8 IN_PROGRESS`, or `OPERATOR_CANON_RUNTIME_DECISION_REQUIRED` wording is historical chronology, not current truth.\n\n'''
ru=f'''<!-- POST_D8_OPERATOR_DECISION_CURRENT -->\n> [!IMPORTANT]\n> **Текущее решение оператора после D8 — 2026-08-12.** ADR-0027 / `OD-POST-D8-001` имеет статус `ACCEPTED / OPERATOR APPROVED`, merge `{D}`. A1–A10 остаётся `STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL`; Final Canon **отложен**, product runtime остаётся `FROZEN`, production — `false`. Единственный текущий gate — `{N}` для {H}; это только **RESEARCH_PLANNING_ONLY**, выполнение нового residual experiment не разрешено. Нижние `D6 NEXT`, `D8 IN_PROGRESS` и `OPERATOR_CANON_RUNTIME_DECISION_REQUIRED` — историческая хронология.\n\n'''
def add(rel,block):
 p=R/rel; t=p.read_text(); assert 'POST_D8_OPERATOR_DECISION_CURRENT' not in t, rel; p.write_text(block+t)
for rel in ['README.md','STATUS.md','ROADMAP.md','docs/ai/README.md','docs/ai/CURRENT_STATE.md','docs/ai/KNOWN_RISKS.md','docs/ai/NOTION_HANDOFF.md','docs/adr/README.md']: add(rel,en)
add('README.ru.md',ru)
p=R/'docs/adr/README.md'; t=p.read_text(); row='| [`0027`](./0027-retain-provisional-architecture-and-runtime-freeze-after-option-d.md) | Retain provisional architecture and runtime freeze after Option D | `ACCEPTED` | `REPOSITORY_REPRODUCED` | governance complete; residual validation planning only | `APPROVED` |'
if row not in t:
 lines=t.splitlines(); idx=next(i for i,x in enumerate(lines) if x.startswith('| [`0026`]')); lines.insert(idx+1,row); p.write_text('\n'.join(lines)+'\n')
