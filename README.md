# DecisionComplete Prompt Pipeline

> **v1.0.0 final publication recut:** This repository package is finalized for `Jayson-Furr/decision-complete-prompt-pipeline`. It includes the 16 core prompts, shared standards, default and product-specific configuration profiles, complete miniature Todo web app and Unity button-click prototype runs, deterministic validation tooling, and explicit validation-scope boundaries. The included validators perform repository structure and consistency validation with limited semantic validation depth; this does not prove deep semantic correctness, downstream artifact correctness, legal approval, rights clearance, security, privacy, compliance, deployment, or production readiness.


**Repository:** `Jayson-Furr/decision-complete-prompt-pipeline`  
**Version:** `1.0.0`  
**Status:** v1.0.0 final publication recut  
**License:** MIT

DecisionComplete Prompt Pipeline is a four-stage prompt system for transforming rough digital-product input into decision-complete specifications, execution-ready fabrication plans, fabricated deliverables, and validation-complete final handoff packages.

The package is designed for AI-assisted digital product work where traceability, decision logging, placeholder handling, review gates, and final handoff status matter.

## What this repository provides

```text
Stage 1: Decide the design.
Stage 2: Decide the fabrication plan.
Stage 3: Fabricate the deliverables.
Stage 4: Validate, repair, package, and prepare final handoff.
```

| Stage | Output Artifact | Authority |
|---|---|---|
| Stage 1 | 100% Decision-Complete Digital Product Design Specification Suite | Controls design |
| Stage 2 | 100% Execution-Ready Fabrication Package Suite | Controls execution planning |
| Stage 3 | 100% Fabrication-Complete Deliverable Package Suite | Controls fabricated outputs |
| Stage 4 | 100% Validation-Complete Final Handoff Package Suite | Controls validation, repair classification, packaging, and final handoff |


## Stage authority model

The package uses these exact authority rules across prompts, configuration, examples, and validation docs:

```text
Stage 1 controls design.
Stage 2 controls execution planning.
Stage 3 controls fabricated outputs.
Stage 4 controls validation, repair classification, packaging, and final handoff.
```

Later stages must preserve upstream authority: Stage 2 must not redesign Stage 1; Stage 3 must not redesign Stage 1 or re-plan Stage 2; Stage 4 must not redesign Stage 1, re-plan Stage 2, or silently change Stage 3 fabricated outputs beyond approved repair scope.

## Quick start

Use the recommended medium-stakes path for most projects:

```text
Stage 1: stage-1-design-specification/prompts/Stage-1-Prompt-3-Medium-Stakes-Design-Interview.md
Stage 2: stage-2-execution-planning/prompts/Stage-2-Prompt-3-Medium-Stakes-Execution-Interview.md
Stage 3: stage-3-fabrication/prompts/Stage-3-Prompt-3-Medium-Stakes-Fabrication-Interview.md
Stage 4: stage-4-validation-packaging/prompts/Stage-4-Prompt-3-Medium-Stakes-Finalization-Interview.md
```

Start with [docs/Quick-Start.md](docs/Quick-Start.md), then use [docs/Artifact-Handoff-Guide.md](docs/Artifact-Handoff-Guide.md) when moving from one stage to the next.

## Prompt modes

Each stage includes four prompt modes.

| Mode | Use When | Decision Handling |
|---|---|---|
| No Questions | You want maximum speed | AI proceeds with safe defaults, placeholders, blockers, review gates, and full logging. |
| Low-Stakes Interview | You want maximum control | AI interviews for low-, medium-, and high-stakes decisions. |
| Medium-Stakes Interview | You want the recommended default | AI resolves low-stakes decisions and interviews for medium/high-stakes decisions. |
| High-Stakes Interview | You want speed with safety interruptions | AI resolves low/medium decisions and interviews only for high-stakes decisions. |

## Repository layout

```text
decision-complete-prompt-pipeline/
  README.md
  LICENSE
  CHANGELOG.md
  Pipeline-Overview.md
  Pipeline-Controller-Prompt.md
  Pipeline-Configuration-Guide.md
  pipeline.configuration.yaml
  docs/
  shared/
  stage-1-design-specification/
  stage-2-execution-planning/
  stage-3-fabrication/
  stage-4-validation-packaging/
  configuration-examples/
  schemas/
  examples/
  tools/
  manifests/
```

See [docs/Repository-Layout.md](docs/Repository-Layout.md) for details.

## Prompt libraries

The repository includes all sixteen core prompt files:

```text
stage-1-design-specification/prompts/
stage-2-execution-planning/prompts/
stage-3-fabrication/prompts/
stage-4-validation-packaging/prompts/
```

Each prompt file is ready to copy into an AI agent workflow.

## Configuration profiles

Version 1.0.0 includes four configuration profile families:

```text
Default profiles:        stage-1-default through stage-4-default
Unity game profiles:     stage-1-unity-game through stage-4-unity-game
Web app profiles:        stage-1-web-application through stage-4-web-application
Shared library profiles: stage-1-shared-library through stage-4-shared-library
```

The Unity, web application, and shared library / SDK profiles are intentionally stage-specific. Each family includes Stage 1, Stage 2, Stage 3, and Stage 4 configuration files.

See [docs/Configuration-Profile-Selection-Guide.md](docs/Configuration-Profile-Selection-Guide.md), [docs/Profile-Authoring-Guide.md](docs/Profile-Authoring-Guide.md), and [docs/Profile-Family-Roadmap.md](docs/Profile-Family-Roadmap.md).

## Complete miniature examples

The repository includes two compact complete pipeline runs:

```text
examples/minimal-complete-run/todo-web-app/
examples/minimal-complete-run/unity-button-click-prototype/
```

These examples show completed Stage 1, Stage 2, Stage 3, and Stage 4 artifacts, fabricated text files, decision ledgers, traceability matrices, validation reports, and final handoff packets.

Start with [docs/Complete-Miniature-Run-Guide.md](docs/Complete-Miniature-Run-Guide.md).

## Core guarantees

```text
Human-readable first.
Stable IDs everywhere.
Traceability across every stage.
Decision ledgers for side-by-side comparison.
Controlled placeholders instead of vague TBDs.
Review gates for high-stakes uncertainty.
No unsupported fact fabrication.
No unauthorized deployment, publishing, credential use, or destructive operations.
```

## Validation tools

Run the full repository validation suite:

```bash
python tools/run-all-checks.py
```

Rebuild generated manifests:

```bash
python tools/build-manifest.py
python tools/build-release-manifest.py
```

The validation tools perform **repository structure and consistency validation**. They do not prove downstream generated artifact correctness, legal approval, rights clearance, privacy compliance, security certification, compliance approval, production readiness, deployment success, public release success, or app store approval.

See [docs/Validation-Scope-and-Guarantees.md](docs/Validation-Scope-and-Guarantees.md), [docs/Validation-Tools.md](docs/Validation-Tools.md), and [docs/Quality-Assurance-Process.md](docs/Quality-Assurance-Process.md).

## Public repository publication

This package is finalized as version `1.0.0` for the public GitHub repository:

```text
https://github.com/Jayson-Furr/decision-complete-prompt-pipeline
```

Helpful publication files:

```text
PUBLICATION-CHECKLIST.md
RELEASE.md
ROADMAP.md
SUPPORT.md
CITATION.cff
docs/Final-Release-Checklist.md
docs/Public-Repository-Setup.md
docs/Final-Publication-Cut.md
```

## License

This repository is released under the MIT License. Review `LICENSE`, `NOTICE.md`, and `CITATION.cff` before publication if you prefer different licensing or attribution details.

## Semantic validation note

The included tools include limited semantic consistency checks for repository metadata, profile depth, examples, and validation-scope language, but they do not prove semantic correctness of products generated later with the prompts.

## Validation guarantee boundary

The validation suite performs repository structure and consistency validation. It does not prove semantic correctness of products created later with the prompts, nor does it prove legal approval, rights clearance, privacy compliance, security certification, compliance approval, production readiness, deployment success, public release success, or app store approval.
