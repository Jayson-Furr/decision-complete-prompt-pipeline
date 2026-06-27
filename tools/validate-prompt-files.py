#!/usr/bin/env python3

from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
PROMPTS = [
"stage-1-design-specification/prompts/Stage-1-Prompt-1-No-Questions-Full-AI-Design-Fabrication.md",
"stage-1-design-specification/prompts/Stage-1-Prompt-2-Low-Stakes-Design-Interview.md",
"stage-1-design-specification/prompts/Stage-1-Prompt-3-Medium-Stakes-Design-Interview.md",
"stage-1-design-specification/prompts/Stage-1-Prompt-4-High-Stakes-Design-Interview.md",
"stage-2-execution-planning/prompts/Stage-2-Prompt-1-No-Questions-Full-AI-Execution-Planning.md",
"stage-2-execution-planning/prompts/Stage-2-Prompt-2-Low-Stakes-Execution-Interview.md",
"stage-2-execution-planning/prompts/Stage-2-Prompt-3-Medium-Stakes-Execution-Interview.md",
"stage-2-execution-planning/prompts/Stage-2-Prompt-4-High-Stakes-Execution-Interview.md",
"stage-3-fabrication/prompts/Stage-3-Prompt-1-No-Questions-Full-AI-Fabrication.md",
"stage-3-fabrication/prompts/Stage-3-Prompt-2-Low-Stakes-Fabrication-Interview.md",
"stage-3-fabrication/prompts/Stage-3-Prompt-3-Medium-Stakes-Fabrication-Interview.md",
"stage-3-fabrication/prompts/Stage-3-Prompt-4-High-Stakes-Fabrication-Interview.md",
"stage-4-validation-packaging/prompts/Stage-4-Prompt-1-No-Questions-Full-AI-Validation-Packaging.md",
"stage-4-validation-packaging/prompts/Stage-4-Prompt-2-Low-Stakes-Finalization-Interview.md",
"stage-4-validation-packaging/prompts/Stage-4-Prompt-3-Medium-Stakes-Finalization-Interview.md",
"stage-4-validation-packaging/prompts/Stage-4-Prompt-4-High-Stakes-Finalization-Interview.md",
]
CONFIGS = [
"configuration-examples/stage-1-default.configuration.yaml",
"configuration-examples/stage-2-default.configuration.yaml",
"configuration-examples/stage-3-default.configuration.yaml",
"configuration-examples/stage-4-default.configuration.yaml",
"configuration-examples/stage-1-unity-game.configuration.yaml",
"configuration-examples/stage-2-unity-game.configuration.yaml",
"configuration-examples/stage-3-unity-game.configuration.yaml",
"configuration-examples/stage-4-unity-game.configuration.yaml",
"configuration-examples/stage-1-web-application.configuration.yaml",
"configuration-examples/stage-2-web-application.configuration.yaml",
"configuration-examples/stage-3-web-application.configuration.yaml",
"configuration-examples/stage-4-web-application.configuration.yaml",
"configuration-examples/stage-1-shared-library.configuration.yaml",
"configuration-examples/stage-2-shared-library.configuration.yaml",
"configuration-examples/stage-3-shared-library.configuration.yaml",
"configuration-examples/stage-4-shared-library.configuration.yaml",
]
MARKERS = {
1:("<<<BEGIN STAGE 1 ARTIFACT: 100% DECISION-COMPLETE DIGITAL PRODUCT DESIGN SPECIFICATION SUITE>>>","<<<END STAGE 1 ARTIFACT>>>","100% Decision-Complete"),
2:("<<<BEGIN STAGE 2 ARTIFACT: 100% EXECUTION-READY FABRICATION PACKAGE SUITE>>>","<<<END STAGE 2 ARTIFACT>>>","100% Execution-Ready"),
3:("<<<BEGIN STAGE 3 ARTIFACT: 100% FABRICATION-COMPLETE DELIVERABLE PACKAGE SUITE>>>","<<<END STAGE 3 ARTIFACT>>>","100% Fabrication-Complete"),
4:("<<<BEGIN STAGE 4 ARTIFACT: 100% VALIDATION-COMPLETE FINAL HANDOFF PACKAGE SUITE>>>","<<<END STAGE 4 ARTIFACT>>>","100% Validation-Complete"),
}
def fail(errors):
    if errors:
        print('Validation failed:')
        for e in errors: print('-', e)
        raise SystemExit(1)

import re
errors=[]
mode_terms={1:['No Questions','Full AI'],2:['Low-Stakes','Interview'],3:['Medium-Stakes','Interview'],4:['High-Stakes','Interview']}
stage_terms={1:['Design Decision Ledger','Hidden Design Decision Scan','Stage 2 Handoff Contract'],2:['Execution Decision Ledger','Hidden Execution Decision Scan','Stage 3 Handoff Contract'],3:['Fabrication Decision Ledger','Hidden Fabrication Decision Scan','Stage 4 Handoff Contract'],4:['Finalization Decision Ledger','Hidden Finalization Decision Scan','User Approval']}
for rel in PROMPTS:
    p=ROOT/rel; text=p.read_text(encoding='utf-8') if p.exists() else ''
    m=re.search(r'Stage-(\d)-Prompt-(\d)', rel); stage=int(m.group(1)); num=int(m.group(2))
    begin,end,status=MARKERS[stage]
    for term in [f'Stage {stage}', begin, end, status, 'Completion Gate', 'Machine-Readable'] + mode_terms[num] + stage_terms[stage]:
        if term not in text: errors.append(f"{rel}: missing {term!r}")
fail(errors)
print(f"Prompt file validation passed. Validated {len(PROMPTS)} prompt files.")
