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

errors=[]
shared=(ROOT/'shared/Shared-Artifact-Boundary-Markup.md').read_text(encoding='utf-8')
for stage,(begin,end,_) in MARKERS.items():
    if begin not in shared or end not in shared: errors.append(f"Shared boundary doc missing Stage {stage} markers")
for rel in PROMPTS:
    text=(ROOT/rel).read_text(encoding='utf-8'); stage=int(rel.split('Stage-',1)[1][0]); begin,end,_=MARKERS[stage]
    if begin not in text or end not in text: errors.append(f"{rel}: missing own stage artifact markers")
for scenario in ['unity-game','web-application','shared-library']:
    for stage,(begin,end,_) in MARKERS.items():
        p=ROOT/'examples'/scenario/'artifact-skeletons'/f'stage-{stage}-artifact-skeleton.md'
        if p.exists():
            t=p.read_text(encoding='utf-8')
            if begin not in t or end not in t: errors.append(f"{p.relative_to(ROOT)} missing markers")
for example in ['todo-web-app','unity-button-click-prototype']:
    for stage,(begin,end,_) in MARKERS.items():
        folder={1:'01-stage-1-design-specification',2:'02-stage-2-execution-planning',3:'03-stage-3-fabrication',4:'04-stage-4-validation-packaging'}[stage]
        p=ROOT/'examples'/'minimal-complete-run'/example/folder/f'stage-{stage}-artifact.example.md'
        if p.exists():
            t=p.read_text(encoding='utf-8')
            if begin not in t or end not in t: errors.append(f"{p.relative_to(ROOT)} missing markers")

for run in ['todo-web-app','unity-button-click-prototype']:
    run_root = ROOT/'examples'/'minimal-complete-run'/run
    for stage,(begin,end,_) in MARKERS.items():
        matches = list(run_root.glob(f'0{stage}-stage-*/stage-{stage}-artifact.example.md'))
        if matches:
            t = matches[0].read_text(encoding='utf-8')
            if begin not in t or end not in t:
                errors.append(f"{matches[0].relative_to(ROOT)} missing markers")
        else:
            errors.append(f"Missing complete run Stage {stage} artifact for {run}")

fail(errors)
print('Artifact boundary validation passed.')
