#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
checks={
'schemas/stage-1-configuration.schema.yaml':['schema_metadata','stage'],
'schemas/stage-2-configuration.schema.yaml':['schema_metadata','stage'],
'schemas/stage-3-configuration.schema.yaml':['schema_metadata','stage'],
'schemas/stage-4-configuration.schema.yaml':['schema_metadata','stage'],
'schemas/decision-ledger.schema.md':['decision ledger','decision key'],
'schemas/document-tree.schema.md':['document tree','document'],
'schemas/traceability-matrix.schema.md':['traceability','stage 1'],
'schemas/artifact-manifest.schema.md':['artifact manifest','artifact'],
'schemas/handoff-packet.schema.md':['handoff packet','critical'],
'schemas/machine-readable-companion.schema.md':['machine-readable','companion'],
}
errors=[]
for rel,terms in checks.items():
    p=ROOT/rel
    if not p.exists(): errors.append(f"Missing schema: {rel}"); continue
    text=p.read_text(encoding='utf-8').lower().replace('_',' ')
    for t in terms:
        if t.lower().replace('_',' ') not in text: errors.append(f"{rel}: missing {t!r}")
if errors:
    print('Validation failed:'); [print('-',e) for e in errors]; sys.exit(1)
print(f"Schema validation passed. Checked {len(checks)} files.")
