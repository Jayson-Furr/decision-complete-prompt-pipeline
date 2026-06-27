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

required = [
"README.md","LICENSE","NOTICE.md","CHANGELOG.md","CONTRIBUTING.md","CODE_OF_CONDUCT.md","SECURITY.md","MANIFEST.md","VERSION","repository-metadata.yaml","Pipeline-Overview.md","Pipeline-Controller-Prompt.md","Pipeline-Configuration-Guide.md","pipeline.configuration.yaml","PACKAGE-BUILD-STATUS.md",
"shared/Shared-Definitions.md","shared/Shared-Controlled-Vocabularies.md","shared/Shared-ID-Namespace.md","shared/Shared-Document-Header-Template.md","shared/Shared-Artifact-Boundary-Markup.md","shared/Shared-Configuration-Priority-Rules.md","shared/Shared-Traceability-Rules.md","shared/Shared-Decision-Ledger-Schema.md","shared/Shared-Hidden-Decision-Scan-Schema.md","shared/Shared-Machine-Readable-Companion-Rules.md",
"schemas/stage-1-configuration.schema.yaml","schemas/stage-2-configuration.schema.yaml","schemas/stage-3-configuration.schema.yaml","schemas/stage-4-configuration.schema.yaml","schemas/decision-ledger.schema.md","schemas/document-tree.schema.md","schemas/traceability-matrix.schema.md","schemas/artifact-manifest.schema.md","schemas/handoff-packet.schema.md","schemas/machine-readable-companion.schema.md",
"docs/Quick-Start.md","docs/Usage-Guide.md","docs/Prompt-Mode-Selection-Guide.md","docs/Repository-Layout.md","docs/Artifact-Handoff-Guide.md","docs/Configuration-Profile-Selection-Guide.md","docs/Decision-Ledger-Comparison-Guide.md","docs/Example-Scenario-Guide.md","docs/GitHub-Publishing-Checklist.md","docs/Troubleshooting.md","docs/FAQ.md","docs/Public-Repository-Release-Notes.md","docs/Validation-Tools.md","docs/Quality-Assurance-Process.md","docs/Repository-Maintenance.md","docs/Versioning-Policy.md","docs/Release-Process.md",
".github/workflows/validate.yml","tools/run-all-checks.py","tools/build-manifest.py","tools/build-release-manifest.py","docs/Profile-Family-Roadmap.md","docs/Schema-Configuration-Alignment.md","docs/Semantic-Validation-Guide.md","docs/Complete-Miniature-Examples.md","docs/Profile-Depth-Balance-Report.md","docs/Complete-Miniature-Run-Guide.md","configuration-examples/profile-family-roadmap.yaml","examples/minimal-complete-run/README.md","examples/minimal-complete-run/todo-web-app/README.md","examples/minimal-complete-run/unity-button-click-prototype/README.md",".github/PULL_REQUEST_TEMPLATE.md","docs/Profile-Authoring-Guide.md","docs/Web-Application-Profile-Deep-Dive.md","docs/Shared-Library-SDK-Profile-Deep-Dive.md","docs/Validation-Scope-and-Guarantees.md",
"docs/Final-Publication-Cut.md","docs/Validation-Guarantee-Matrix.md","docs/Validator-Implementation-Notes.md","tools/validate-profile-depth.py","tools/validate-validation-scope.py","tools/validate-semantic-consistency.py",] + PROMPTS + CONFIGS
errors=[f"Missing required file: {r}" for r in required if not (ROOT/r).is_file()]
for d in ["docs","shared","schemas","configuration-examples","examples","tools","manifests",".github/workflows"]:
    if not (ROOT/d).is_dir(): errors.append(f"Missing required directory: {d}")
for rel in ["README.md","MANIFEST.md","repository-metadata.yaml","Pipeline-Overview.md"]:
    text=(ROOT/rel).read_text(encoding='utf-8') if (ROOT/rel).exists() else ''
    if 'DecisionComplete Prompt Pipeline' not in text: errors.append(f"Repository identity missing from {rel}")
    if 'decision-complete-prompt-pipeline' not in text: errors.append(f"Repository name missing from {rel}")
if (ROOT/'VERSION').read_text(encoding='utf-8').strip() != '1.0.0': errors.append('VERSION must be 1.0.0')
fail(errors)
print(f"Package structure validation passed. Validated {len(required)} required files, {len(PROMPTS)} prompt files, and {len(CONFIGS)} configuration examples.")
