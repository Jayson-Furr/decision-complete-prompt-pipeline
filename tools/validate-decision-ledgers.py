#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT/'shared/Shared-Decision-Ledger-Schema.md').read_text(encoding='utf-8')
required=['Artifact ID','Prompt Mode','Logging Level','Decision Key','Decision Category','Affected Item','Decision Question','Selected Option Text','Selection Reason','Comparison Notes']
missing=[r for r in required if r not in text]
if missing:
    print('Validation failed:', missing); sys.exit(1)
print('Decision ledger schema validation passed.')
