#!/usr/bin/env python3
"""Build deterministic release-oriented file indexes, checksums, and repository tree listings."""
from pathlib import Path
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
MAN = ROOT / 'manifests'
MAN.mkdir(exist_ok=True)
GENERATED = {
    'package-manifest.generated.json',
    'manifests/public-repository-file-index.csv',
    'manifests/release-artifact-manifest.json',
    'manifests/repository-tree.txt',
    'manifests/validation-report.json',
    'manifests/checksums.sha256.json',
    'manifests/checksums.sha256.txt',
    'manifests/final-package-inventory.json',
}

def digest(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()

files = []
for path in sorted(ROOT.rglob('*')):
    if not path.is_file():
        continue
    rel = path.relative_to(ROOT)
    rel_text = rel.as_posix()
    if '.git' in rel.parts or '__pycache__' in rel.parts or path.suffix == '.pyc' or rel_text in GENERATED:
        continue
    files.append({'path': rel_text, 'category': rel.parts[0] if len(rel.parts) > 1 else 'root', 'bytes': path.stat().st_size, 'sha256': digest(path)})

with (MAN / 'public-repository-file-index.csv').open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['path', 'category', 'bytes', 'sha256'])
    writer.writeheader()
    writer.writerows(files)

release_package = {
    'name': 'DecisionComplete Prompt Pipeline',
    'repository': 'decision-complete-prompt-pipeline',
    'repository_full_name': 'Jayson-Furr/decision-complete-prompt-pipeline',
    'repository_url': 'https://github.com/Jayson-Furr/decision-complete-prompt-pipeline',
    'version': (ROOT / 'VERSION').read_text(encoding='utf-8').strip(),
    'manifest_generation': 'deterministic',
    'generation_policy': 'Indexes source-controlled package files and excludes generated manifest outputs to avoid self-referential diffs.',
}
release_manifest = {'package': release_package, 'file_count': len(files), 'files': files}
(MAN / 'release-artifact-manifest.json').write_text(json.dumps(release_manifest, indent=2, sort_keys=True) + '\n', encoding='utf-8')

inventory = {
    'package': {**release_package, 'completion_percent': 100},
    'file_count': len(files),
    'excludes': sorted(GENERATED),
    'files': [{'path': f['path'], 'size_bytes': f['bytes'], 'sha256': f['sha256']} for f in files],
}
(MAN / 'final-package-inventory.json').write_text(json.dumps(inventory, indent=2, sort_keys=True) + '\n', encoding='utf-8')
(MAN / 'checksums.sha256.txt').write_text(''.join(f"{f['sha256']}  {f['path']}\n" for f in files), encoding='utf-8')
(MAN / 'checksums.sha256.json').write_text(json.dumps({'algorithm': 'sha256', 'files': [{'path': f['path'], 'sha256': f['sha256']} for f in files]}, indent=2, sort_keys=True) + '\n', encoding='utf-8')

lines = []
for path in sorted(ROOT.rglob('*')):
    rel = path.relative_to(ROOT)
    rel_text = rel.as_posix()
    if '.git' in rel.parts or '__pycache__' in rel.parts or path.suffix == '.pyc' or rel_text in GENERATED:
        continue
    lines.append('  ' * (len(rel.parts) - 1) + rel.name + ('/' if path.is_dir() else ''))
(MAN / 'repository-tree.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(f'Wrote deterministic release manifests for {len(files)} files.')
