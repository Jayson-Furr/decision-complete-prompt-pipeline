#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]; pattern=re.compile(r'\[[^\]]+\]\(([^)]+)\)')
for p in ROOT.rglob('*.md'):
    if '.git' in p.parts: continue
    in_fence=False
    for n,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
        if line.strip().startswith('```'):
            in_fence=not in_fence; continue
        if in_fence: continue
        for m in pattern.finditer(line):
            target=m.group(1).strip()
            if not target or target.startswith(('http://','https://','mailto:','#','sandbox:','file:')): continue
            target=target.split('#',1)[0]
            if not target: continue
            q=(p.parent/target).resolve()
            try: q.relative_to(ROOT.resolve())
            except ValueError: errors.append(f'{p.relative_to(ROOT)}:{n} links outside repo: {target}'); continue
            if not q.exists(): errors.append(f'{p.relative_to(ROOT)}:{n} broken link: {target}')
if errors:
    print('Validation failed:'); [print('-',e) for e in errors]; sys.exit(1)
print('Markdown link validation passed.')
