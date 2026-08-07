from __future__ import annotations

import json
from pathlib import Path

SUPPORTED = {
    'NK-AUT-001','NK-AUT-002','NK-AUT-003','NK-AUT-005','NK-AUT-007','NK-AUT-008','NK-AUT-009','NK-AUT-012',
    'NK-CFL-006','NK-EQV-001','NK-EQV-002','NK-EQV-003','NK-EQV-004','NK-EQV-005','NK-EQV-006','NK-EQV-007','NK-EQV-008','NK-EQV-009','NK-EQV-010',
    'NK-EVT-003','NK-EVT-004','NK-EVT-006','NK-EVT-007','NK-EVT-008','NK-EVT-011','NK-EVT-012','NK-EVT-013','NK-EVT-014',
    'NK-ID-001','NK-ID-002','NK-ID-003','NK-ID-004','NK-ID-005','NK-ID-008','NK-ID-009','NK-ID-010','NK-ID-011','NK-ID-012',
    'NK-SEM-001','NK-SEM-003','NK-SEM-004','NK-SEM-005','NK-SEM-006','NK-SEM-007','NK-SEM-008',
}
PARTIAL = {'NK-AUT-004','NK-AUT-010','NK-CFL-003','NK-EVT-001','NK-EVT-002','NK-EVT-005','NK-EVT-009','NK-EVT-010','NK-ID-006','NK-SEM-002'}
UNSUPPORTED = {'NK-AUT-006','NK-AUT-011','NK-CFL-001','NK-CFL-002','NK-CFL-004','NK-CFL-005','NK-CFL-007','NK-CFL-008','NK-EPI-001','NK-EPI-002','NK-EPI-003','NK-EPI-004','NK-EPI-005','NK-EPI-006','NK-EPI-007','NK-EPI-008','NK-ID-007'}


def assertion_ids(root: Path) -> list[str]:
    path = root / 'contracts' / 'registry.json'
    try:
        registry = json.loads(path.read_text(encoding='utf-8'))
        ids = [a['assertion_id'] for f in registry['families'] for a in f['assertions']]
        if ids:
            return ids
    except (OSError, json.JSONDecodeError, KeyError, TypeError):
        pass
    return sorted(SUPPORTED | PARTIAL | UNSUPPORTED)


def make_c3_report(root: Path) -> dict:
    ids = assertion_ids(root)
    assert len(ids) == 72
    assert set(ids) == SUPPORTED | PARTIAL | UNSUPPORTED
    rows = []
    for assertion_id in ids:
        status = 'SUPPORTED' if assertion_id in SUPPORTED else 'PARTIAL' if assertion_id in PARTIAL else 'UNSUPPORTED'
        rows.append({'assertion_id': assertion_id, 'status': status, 'evidence': ['test.c3'], 'limitations': ['bounded test prerequisite']})
    return {
        'report_version': 'nk-equivalence-report/1',
        'comparison_id': 'test/postgresql-sqlite-c3',
        'kernel_runtime_conformance': 'C3',
        'support_state': 'PARTIAL',
        'assertion_results': rows,
    }
