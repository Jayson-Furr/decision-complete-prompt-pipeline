#!/usr/bin/env python3
"""Validate that repository validation claims are scoped accurately."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
required_files = [
    'docs/Validation-Scope-and-Guarantees.md',
    'docs/Semantic-Validation-Guide.md',
    'docs/Validation-Tools.md',
    'docs/Validation-Guarantee-Matrix.md',
    'README.md',
    'RELEASE.md',
]
required_phrases = [
    'repository structure and consistency validation',
    'does not prove',
    'semantic',
]
errors = []
for rel in required_files:
    path = ROOT / rel
    if not path.exists():
        errors.append(f'Missing validation-scope file: {rel}')
        continue
    text = path.read_text(encoding='utf-8').lower()
    for phrase in required_phrases:
        if phrase not in text:
            errors.append(f'{rel}: missing validation-scope phrase {phrase!r}')

scope_doc = ROOT / 'docs/Validation-Scope-and-Guarantees.md'
if scope_doc.exists():
    text = scope_doc.read_text(encoding='utf-8').lower()
    for phrase in ['legal approval', 'rights clearance', 'privacy compliance', 'security certification', 'deployment success', 'app store approval']:
        if phrase not in text:
            errors.append(f'docs/Validation-Scope-and-Guarantees.md: missing non-guarantee phrase {phrase!r}')

report = ROOT / 'manifests' / 'validation-report.json'
if report.exists():
    try:
        data = json.loads(report.read_text(encoding='utf-8'))
        scope = data.get('validation_scope')
        valid_scope = False
        if isinstance(scope, str):
            valid_scope = scope == 'repository_structure_and_consistency'
        elif isinstance(scope, dict):
            valid_scope = scope.get('scope_type') == 'repository_structure_and_consistency'
        elif scope is None:
            valid_scope = True
        if not valid_scope:
            errors.append('manifests/validation-report.json: validation_scope is not repository_structure_and_consistency')
        depth = data.get('semantic_validation_depth')
        if depth not in (None, 'limited'):
            errors.append('manifests/validation-report.json: semantic_validation_depth is not limited')
    except Exception as exc:
        errors.append(f'manifests/validation-report.json: not valid JSON: {exc}')

if errors:
    print('Validation-scope validation failed:')
    for error in errors:
        print('-', error)
    sys.exit(1)
print('Validation scope validation passed. Repository validation claims are scoped to structure and consistency, not deep semantic guarantees.')
