#!/usr/bin/env python3
"""Perform higher-level repository consistency checks without claiming deep semantic validation."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

# Confirm no public docs overclaim validation.
for rel in ['README.md', 'docs/Validation-Tools.md', 'docs/Semantic-Validation-Guide.md']:
    path = ROOT / rel
    text = path.read_text(encoding='utf-8').lower() if path.exists() else ''
    forbidden = ['proof of prompt correctness', 'proof of generated artifact correctness', 'deep semantic validation passed']
    for phrase in forbidden:
        if phrase in text:
            errors.append(f'{rel}: contains overbroad validation claim {phrase!r}')

# Confirm core authority model is visible in core docs.
for rel in ['README.md', 'Pipeline-Overview.md', 'Pipeline-Configuration-Guide.md']:
    path = ROOT / rel
    text = path.read_text(encoding='utf-8') if path.exists() else ''
    for fragment in ['Stage 1 controls design', 'Stage 2 controls execution', 'Stage 3 controls fabricated', 'Stage 4 controls validation']:
        if fragment not in text:
            errors.append(f'{rel}: missing authority statement fragment {fragment!r}')

# Confirm complete miniature examples have full four-stage chain and ledgers.
for example in ['todo-web-app', 'unity-button-click-prototype']:
    base = ROOT / 'examples' / 'minimal-complete-run' / example
    required = [
        '01-stage-1-design-specification/stage-1-artifact.example.md',
        '02-stage-2-execution-planning/stage-2-artifact.example.md',
        '03-stage-3-fabrication/stage-3-artifact.example.md',
        '04-stage-4-validation-packaging/stage-4-artifact.example.md',
        '01-stage-1-design-specification/stage-1-decision-ledger.example.csv',
        '02-stage-2-execution-planning/stage-2-decision-ledger.example.csv',
        '03-stage-3-fabrication/stage-3-decision-ledger.example.csv',
        '04-stage-4-validation-packaging/stage-4-decision-ledger.example.csv',
    ]
    for rel in required:
        if not (base / rel).exists():
            errors.append(f'examples/minimal-complete-run/{example}: missing {rel}')
    combined_parts = []
    if base.exists():
        for p in base.rglob('*'):
            if p.is_file() and p.suffix.lower() in {'.md', '.csv', '.json', '.yaml', '.yml', '.tsx', '.ts', '.css', '.cs', '.uxml', '.uss'}:
                combined_parts.append(p.read_text(encoding='utf-8', errors='ignore'))
    combined = ''.join(combined_parts)
    for token in ['S1-', 'S2-', 'S3-', 'S4-']:
        if token not in combined:
            errors.append(f'examples/minimal-complete-run/{example}: missing cross-stage token {token}')

# Confirm decision ledger examples use the canonical header prefix.
expected_prefix = 'Artifact ID,Prompt Mode,Logging Level,Decision Key,Decision Category,Affected Item,Decision Question,Stakes Level,Logging Treatment'
for path in ROOT.rglob('*decision-ledger*.csv'):
    if '.git' in path.parts:
        continue
    lines = path.read_text(encoding='utf-8').splitlines()
    if not lines:
        errors.append(f'{path.relative_to(ROOT)}: empty decision ledger')
        continue
    if not lines[0].strip().startswith(expected_prefix):
        errors.append(f'{path.relative_to(ROOT)}: decision ledger header does not match canonical prefix')

if errors:
    print('Semantic consistency validation failed:')
    for error in errors:
        print('-', error)
    sys.exit(1)
print('Semantic consistency validation passed. Checked scoped validation language, authority model, complete miniature example chains, and decision ledger headers.')
