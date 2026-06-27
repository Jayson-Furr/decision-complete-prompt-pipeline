# Quick Start

This quick start gives the shortest reliable path for using DecisionComplete Prompt Pipeline.

## 1. Pick the default path

Use the medium-stakes prompts unless you have a specific reason to use a different mode.

```text
Stage 1: stage-1-design-specification/prompts/Stage-1-Prompt-3-Medium-Stakes-Design-Interview.md
Stage 2: stage-2-execution-planning/prompts/Stage-2-Prompt-3-Medium-Stakes-Execution-Interview.md
Stage 3: stage-3-fabrication/prompts/Stage-3-Prompt-3-Medium-Stakes-Fabrication-Interview.md
Stage 4: stage-4-validation-packaging/prompts/Stage-4-Prompt-3-Medium-Stakes-Finalization-Interview.md
```

Medium-stakes mode lets the AI resolve routine low-stakes details while interviewing for decisions that materially affect scope, quality, implementation, validation, security, privacy, rights, release, or final handoff.

## 2. Start Stage 1

Open the Stage 1 medium-stakes prompt and provide all available project input.

You can provide minimal input such as:

```text
Game name: Starfall Cartographer
Type: Unity 2D puzzle game
Description: The player restores constellations by rotating star clusters and solving spatial puzzles.
Preferences: Unity 6000.4.11f1, UI Toolkit, 2D Renderer, desktop first.
```

You may also attach markdown design notes, screenshots, mockups, concept art, identity images, or a Stage 1 configuration file.

## 3. Save the Stage 1 artifact

Stage 1 should output an artifact wrapped like this:

```text
<<<BEGIN STAGE 1 ARTIFACT: 100% DECISION-COMPLETE DIGITAL PRODUCT DESIGN SPECIFICATION SUITE>>>

[Stage 1 artifact]

<<<END STAGE 1 ARTIFACT>>>
```

Copy the entire artifact, including boundary markers.

## 4. Run Stage 2

Open the Stage 2 medium-stakes prompt and paste the full Stage 1 artifact into the required input section.

Stage 2 will produce:

```text
100% Execution-Ready Fabrication Package Suite
```

This contains work packages, Stage 3 prompts, contractor briefs, dependencies, expected artifacts, QA matrices, and a Stage 3 handoff contract.

## 5. Run Stage 3

Open the Stage 3 medium-stakes prompt and paste the full Stage 2 artifact.

Stage 3 will produce:

```text
100% Fabrication-Complete Deliverable Package Suite
```

This contains fabricated text-based files where possible, artifact records, external-tool-required asset packets, preliminary validation, and Stage 4 handoff instructions.

## 6. Run Stage 4

Open the Stage 4 medium-stakes prompt and paste the full Stage 3 artifact.

Stage 4 will produce:

```text
100% Validation-Complete Final Handoff Package Suite
```

The final handoff status will be one of:

```text
Ready
Ready with Warnings
Review-Gated
Blocked
External Validation Required
```

## 7. Use configuration profiles when helpful

Use these profiles for common project types:

```text
configuration-examples/stage-1-unity-game.configuration.yaml
configuration-examples/stage-1-web-application.configuration.yaml
configuration-examples/stage-1-shared-library.configuration.yaml
```

Each product-type profile has Stage 1 through Stage 4 variants.

## 8. Validate the repository package

From the repository root:

```bash
python tools/validate-package-structure.py
python tools/build-manifest.py
```

These scripts validate expected files and generate `package-manifest.generated.json`.

## 9. Inspect a complete miniature run

To see compact completed artifacts before running your own project, open:

```text
examples/minimal-complete-run/todo-web-app/
examples/minimal-complete-run/unity-button-click-prototype/
```

These examples show what Stage 1 through Stage 4 outputs can look like after a full pass.
