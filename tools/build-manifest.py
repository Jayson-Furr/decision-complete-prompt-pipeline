#!/usr/bin/env python3
"""Build deterministic package-manifest.generated.json.

Generated manifest outputs are excluded from the manifest input set to avoid self-referential
hash churn in CI.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
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
total = 0
exts = {}
for path in sorted(ROOT.rglob('*')):
    if not path.is_file():
        continue
    rel = path.relative_to(ROOT)
    rel_text = rel.as_posix()
    if '.git' in rel.parts or '__pycache__' in rel.parts or path.suffix == '.pyc' or rel_text in GENERATED:
        continue
    size = path.stat().st_size
    total += size
    ext = path.suffix.lower() or '[none]'
    exts[ext] = exts.get(ext, 0) + 1
    files.append({'path': rel_text, 'bytes': size, 'sha256': digest(path)})

data = {
    'package': {
        'name': 'DecisionComplete Prompt Pipeline',
        'repository': 'decision-complete-prompt-pipeline',
        'repository_full_name': 'Jayson-Furr/decision-complete-prompt-pipeline',
        'repository_url': 'https://github.com/Jayson-Furr/decision-complete-prompt-pipeline',
        'version': (ROOT / 'VERSION').read_text(encoding='utf-8').strip(),
        'manifest_generation': 'deterministic',
        'generation_policy': 'Indexes source-controlled package files and excludes generated manifest outputs to avoid self-referential diffs.',
    },
    'summary': {'file_count': len(files), 'total_bytes': total, 'extensions': dict(sorted(exts.items()))},
    'files': files,
}
(ROOT / 'package-manifest.generated.json').write_text(json.dumps(data, indent=2, sort_keys=True) + '\n', encoding='utf-8')
print(f"Wrote package-manifest.generated.json with {len(files)} files.")
