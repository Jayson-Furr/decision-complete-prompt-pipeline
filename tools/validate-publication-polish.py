#!/usr/bin/env python3
"""Validate publication polish for the public GitHub repository package."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
errors = []
public_files = []
for p in ROOT.rglob('*'):
    if not p.is_file():
        continue
    rel = p.relative_to(ROOT)
    if '.git' in rel.parts or '__pycache__' in rel.parts or 'tools' in rel.parts:
        continue
    if rel.suffix.lower() in {'.md','.yaml','.yml','.json','.cff','.txt','.csv'} or rel.name in {'CODEOWNERS'}:
        public_files.append(p)

placeholder_tokens = ['YOUR-USERNAME', 'YOUR-ACCOUNT', 'YOUR-GITHUB-USERNAME', '@YOUR']
for p in public_files:
    rel = p.relative_to(ROOT).as_posix()
    text = p.read_text(encoding='utf-8', errors='ignore')
    if '/mnt/data' in text:
        errors.append(f'{rel}: contains sandbox path /mnt/data')
    for token in placeholder_tokens:
        if token in text:
            errors.append(f'{rel}: contains unresolved owner placeholder {token}')
    if '__pycache__' in text and rel.startswith('manifests/'):
        errors.append(f'{rel}: contains transient __pycache__ reference')
    if 'package-9-file-checksums' in text:
        errors.append(f'{rel}: contains stale package-9 checksum reference')

if not (ROOT/'docs/Profile-Authoring-Guide.md').is_file():
    errors.append('Missing docs/Profile-Authoring-Guide.md')
if not (ROOT/'docs/Validation-Scope-and-Guarantees.md').is_file():
    errors.append('Missing docs/Validation-Scope-and-Guarantees.md')
if not (ROOT/'docs/Profile-Family-Roadmap.md').is_file():
    errors.append('Missing docs/Profile-Family-Roadmap.md')
if not (ROOT/'configuration-examples/profile-family-roadmap.yaml').is_file():
    errors.append('Missing configuration-examples/profile-family-roadmap.yaml')
github_entries = {p.name for p in (ROOT/'.github').iterdir()} if (ROOT/'.github').is_dir() else set()
if 'pull_request_template.md' in github_entries:
    errors.append('Duplicate lower-case pull request template exists')
stale_public_files = ['README.md','RELEASE.md','FINAL-PACKAGE-NOTES.md','PACKAGE-BUILD-STATUS.md','repository-metadata.yaml']
for rel in stale_public_files:
    path = ROOT / rel
    if path.exists():
        text_value = path.read_text(encoding='utf-8', errors='ignore')
        if 'package-12' in text_value or 'package-11.zip' in text_value or 'package-12.zip' in text_value:
            errors.append(f'{rel}: contains stale package directory/archive reference')
if not (ROOT/'package-manifest.generated.json').is_file():
    errors.append('package-manifest.generated.json should be present in the public release')
if 'package-manifest.generated.json' in (ROOT/'.gitignore').read_text(encoding='utf-8'):
    errors.append('.gitignore excludes package-manifest.generated.json even though it is committed')
codeowners = (ROOT/'.github/CODEOWNERS').read_text(encoding='utf-8') if (ROOT/'.github/CODEOWNERS').exists() else ''
if '@Jayson-Furr' not in codeowners:
    errors.append('CODEOWNERS does not reference @Jayson-Furr')
if errors:
    print('Publication polish validation failed:')
    for error in errors:
        print('-', error)
    sys.exit(1)
print(f'Publication polish validation passed. Checked {len(public_files)} public text files.')
