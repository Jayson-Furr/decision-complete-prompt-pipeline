#!/usr/bin/env python3
"""Run all repository validation checks and write manifests/validation-report.json."""
from __future__ import annotations

from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TOOLS = [
    'validate-package-structure.py',
    'validate-prompt-files.py',
    'validate-artifact-boundaries.py',
    'validate-configurations.py',
    'validate-controlled-vocabularies.py',
    'validate-schemas.py',
    'validate-examples.py',
    'validate-decision-ledgers.py',
    'validate-machine-readable-companions.py',
    'validate-semantic-consistency.py',
    'validate-profile-depth.py',
    'validate-markdown-links.py',
    'validate-github-readiness.py',
    'validate-publication-polish.py',
    'validate-validation-scope.py',
    'validate-final-publication-recut.py',
    'validate-release-readiness.py',
]

results = []
failed = False
for tool in TOOLS:
    print(f'==> {tool}', flush=True)
    tool_path = ROOT / 'tools' / tool
    if not tool_path.exists():
        print(f'Missing tool: {tool}', file=sys.stderr)
        results.append({'tool': tool, 'returncode': 127, 'status': 'failed'})
        failed = True
        continue
    try:
        process = subprocess.run([sys.executable, str(tool_path)], cwd=ROOT, text=True, timeout=90)
        returncode = process.returncode
    except subprocess.TimeoutExpired:
        print(f'Timeout while running {tool}', file=sys.stderr)
        returncode = 124
    results.append({'tool': tool, 'returncode': returncode, 'status': 'passed' if returncode == 0 else 'failed'})
    if returncode != 0:
        failed = True

report = {
    'package': {
        'name': 'DecisionComplete Prompt Pipeline',
        'repository': 'decision-complete-prompt-pipeline',
        'repository_full_name': 'Jayson-Furr/decision-complete-prompt-pipeline',
        'version': (ROOT / 'VERSION').read_text(encoding='utf-8').strip(),
    },
    'status': 'failed' if failed else 'passed',
    'validation_scope': {
        'scope_type': 'repository_structure_and_consistency',
        'semantic_validation_depth': 'limited',
        'description': 'Checks repository structure, required files, prompt/config/example consistency, public metadata, and release-readiness hygiene.',
        'does_not_validate': [
            'downstream generated artifact correctness',
            'legal approval',
            'rights clearance',
            'privacy compliance',
            'security certification',
            'compliance approval',
            'production readiness',
            'deployment success',
            'public release success',
            'app store approval'
        ]
    },
    'semantic_validation_depth': 'limited',
    'does_not_validate': [
        'downstream generated artifact correctness',
        'legal approval',
        'rights clearance',
        'privacy compliance',
        'security certification',
        'compliance approval',
        'production readiness',
        'deployment success',
        'public release success',
        'app store approval'
    ],
    'results': results,
}
(ROOT / 'manifests').mkdir(exist_ok=True)
(ROOT / 'manifests' / 'validation-report.json').write_text(json.dumps(report, indent=2, sort_keys=True) + '\n', encoding='utf-8')
print(f"Wrote manifests/validation-report.json with status: {report['status']}")
if failed:
    raise SystemExit(1)
