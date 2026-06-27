#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT/'shared/Shared-Machine-Readable-Companion-Rules.md').read_text(encoding='utf-8').lower()
required=['yaml','json','csv','human-readable','handoff','traceability','decision']
missing=[r for r in required if r not in text]
if missing:
    print('Validation failed:', missing); sys.exit(1)
print('Machine-readable companion validation passed.')
