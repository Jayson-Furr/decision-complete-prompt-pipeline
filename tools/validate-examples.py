#!/usr/bin/env python3

from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]
MARKERS = {
    1: ("<<<BEGIN STAGE 1 ARTIFACT: 100% DECISION-COMPLETE DIGITAL PRODUCT DESIGN SPECIFICATION SUITE>>>", "<<<END STAGE 1 ARTIFACT>>>"),
    2: ("<<<BEGIN STAGE 2 ARTIFACT: 100% EXECUTION-READY FABRICATION PACKAGE SUITE>>>", "<<<END STAGE 2 ARTIFACT>>>"),
    3: ("<<<BEGIN STAGE 3 ARTIFACT: 100% FABRICATION-COMPLETE DELIVERABLE PACKAGE SUITE>>>", "<<<END STAGE 3 ARTIFACT>>>"),
    4: ("<<<BEGIN STAGE 4 ARTIFACT: 100% VALIDATION-COMPLETE FINAL HANDOFF PACKAGE SUITE>>>", "<<<END STAGE 4 ARTIFACT>>>"),
}
LEDGER_HEADER = [
    "Artifact ID", "Prompt Mode", "Logging Level", "Decision Key", "Decision Category", "Affected Item",
    "Decision Question", "Stakes Level", "Logging Treatment", "Option A", "Option B", "Option C", "Option D",
    "Other Options Considered", "Selected Option Code", "Selected Option Text", "Decision Source", "Selection Reason",
    "Assumption Used?", "Placeholder Used?", "Review Requirement", "Decision Status", "Comparison Notes",
]
errors = []

def require_file(path: Path):
    if not path.is_file():
        errors.append(f"Missing {path.relative_to(ROOT)}")

def require_marker(path: Path, stage: int):
    require_file(path)
    if path.is_file():
        text = path.read_text(encoding="utf-8")
        begin, end = MARKERS[stage]
        if begin not in text or end not in text:
            errors.append(f"{path.relative_to(ROOT)} missing Stage {stage} artifact markers")

def require_ledger(path: Path):
    require_file(path)
    if path.is_file():
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, [])
        if header != LEDGER_HEADER:
            errors.append(f"{path.relative_to(ROOT)} does not use the standardized decision ledger header")

def require_csv_has_header(path: Path, required_columns):
    require_file(path)
    if path.is_file():
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, [])
        for col in required_columns:
            if col not in header:
                errors.append(f"{path.relative_to(ROOT)} missing required column {col!r}")

scenario_required = [
    "input/project-brief.md",
    "input/stage-1-context-packet.md",
    "configuration/pipeline.override.yaml",
    "runbooks/01-run-stage-1.md",
    "runbooks/02-run-stage-2.md",
    "runbooks/03-run-stage-3.md",
    "runbooks/04-run-stage-4.md",
    "artifact-skeletons/stage-1-artifact-skeleton.md",
    "artifact-skeletons/stage-2-artifact-skeleton.md",
    "artifact-skeletons/stage-3-artifact-skeleton.md",
    "artifact-skeletons/stage-4-artifact-skeleton.md",
    "checklists/stage-4-validation-checklist.md",
    "decision-ledger-comparison/sample-decision-ledger.csv",
    "traceability/sample-traceability-matrix.csv",
]
for scenario in ["unity-game", "web-application", "shared-library"]:
    for rel in scenario_required:
        require_file(ROOT / "examples" / scenario / rel)

complete_runs = {
    "todo-web-app": {
        "stage3_files": [
            "03-stage-3-fabrication/fabricated-files/package.json",
            "03-stage-3-fabrication/fabricated-files/index.html",
            "03-stage-3-fabrication/fabricated-files/src/main.tsx",
            "03-stage-3-fabrication/fabricated-files/src/App.tsx",
            "03-stage-3-fabrication/fabricated-files/src/App.css",
            "03-stage-3-fabrication/fabricated-files/src/types.ts",
            "03-stage-3-fabrication/fabricated-files/src/App.test.tsx",
            "03-stage-3-fabrication/fabricated-files/README.generated.md",
        ]
    },
    "unity-button-click-prototype": {
        "stage3_files": [
            "03-stage-3-fabrication/fabricated-files/Assets/_Project/Scripts/Runtime/ButtonClickCounter.cs",
            "03-stage-3-fabrication/fabricated-files/Assets/_Project/Scripts/UI/ClickButtonPresenter.cs",
            "03-stage-3-fabrication/fabricated-files/Assets/_Project/UI/UXML/ClickButtonScreen.uxml",
            "03-stage-3-fabrication/fabricated-files/Assets/_Project/UI/USS/ClickButtonScreen.uss",
            "03-stage-3-fabrication/fabricated-files/Assets/Tests/EditMode/ButtonClickCounterTests.cs",
            "03-stage-3-fabrication/fabricated-files/ExternalToolPackets/UnitySceneCreationPacket.md",
            "03-stage-3-fabrication/fabricated-files/ExternalValidation/UnityEditorValidationChecklist.md",
        ]
    },
}

for example_name, config in complete_runs.items():
    base = ROOT / "examples" / "minimal-complete-run" / example_name
    require_file(base / "README.md")
    require_file(base / "00-source-input/user-input.md")
    require_file(base / "00-source-input/pipeline.configuration.yaml")
    for stage in [1, 2, 3, 4]:
        folder = ["", "01-stage-1-design-specification", "02-stage-2-execution-planning", "03-stage-3-fabrication", "04-stage-4-validation-packaging"][stage]
        require_marker(base / folder / f"stage-{stage}-artifact.example.md", stage)
    for ledger in base.rglob("*decision-ledger*.csv"):
        require_ledger(ledger)
    for trace in base.rglob("*traceability-matrix*.csv"):
        require_csv_has_header(trace, ["Trace ID"] if "final" in trace.name else ["Stage 1 Entity ID"])
    for rel in config["stage3_files"]:
        require_file(base / rel)

if errors:
    print("Example validation failed:")
    for error in errors:
        print("-", error)
    sys.exit(1)

print("Example validation passed. Checked 3 scenario packets and 2 complete miniature runs.")
