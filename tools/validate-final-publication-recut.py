#!/usr/bin/env python3
"""Validate final v1.0.0 publication recut metadata and documentation."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
errors = []
required = [
    'README.md', 'RELEASE.md', 'CHANGELOG.md', 'PACKAGE-BUILD-STATUS.md', 'repository-metadata.yaml',
    'docs/Final-v1.0.0-Publication-Recut.md', 'docs/Post-Publish-Smoke-Test.md',
    'docs/Validation-Scope-and-Guarantees.md', 'docs/Profile-Authoring-Guide.md',
    'examples/minimal-complete-run/todo-web-app/README.md',
    'examples/minimal-complete-run/unity-button-click-prototype/README.md',
]
for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f'Missing final publication recut file: {rel}')
expected_tokens = {
    'README.md': ['v1.0.0 final publication recut', 'Jayson-Furr/decision-complete-prompt-pipeline', 'repository structure and consistency validation'],
    'RELEASE.md': ['Final v1.0.0 Publication Recut', 'Jayson-Furr/decision-complete-prompt-pipeline', 'repository structure and consistency validation'],
    'PACKAGE-BUILD-STATUS.md': ['Latest Batch | 13', 'package-13', 'Final v1.0.0 publication recut complete'],
    'repository-metadata.yaml': ['latest_batch: 13', 'v1_0_0_final_publication_recut_complete', 'public_repository_ready: true'],
    'docs/Final-v1.0.0-Publication-Recut.md': ['Final v1.0.0 Publication Recut', 'Ready for GitHub publication', 'Final recut batch: 13'],
}
for rel, tokens in expected_tokens.items():
    p = ROOT / rel
    text = p.read_text(encoding='utf-8') if p.exists() else ''
    for token in tokens:
        if token not in text:
            errors.append(f'{rel}: missing expected token {token!r}')
public_text_exts = {'.md', '.yaml', '.yml', '.json', '.cff', '.txt', '.csv'}
for p in ROOT.rglob('*'):
    if not p.is_file():
        continue
    rel = p.relative_to(ROOT)
    if '.git' in rel.parts or '__pycache__' in rel.parts or 'tools' in rel.parts:
        continue
    if rel.suffix.lower() not in public_text_exts and rel.name != 'CODEOWNERS':
        continue
    text = p.read_text(encoding='utf-8', errors='ignore')
    if '/mnt/data' in text:
        errors.append(f'{rel.as_posix()}: contains sandbox path /mnt/data')
    for placeholder in ['YOUR-USERNAME', 'YOUR-GITHUB-USERNAME', 'YOUR-ACCOUNT', '@YOUR']:
        if placeholder in text:
            errors.append(f'{rel.as_posix()}: contains unresolved owner placeholder {placeholder}')
if errors:
    print('Final publication recut validation failed:')
    for error in errors:
        print('-', error)
    sys.exit(1)
print('Final publication recut validation passed.')
