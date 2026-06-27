# Examples

This directory contains practical example scenarios for DecisionComplete Prompt Pipeline.

The examples are designed to show how to prepare input and run the four-stage prompt chain. They are intentionally smaller than full generated stage artifacts.

## Included scenarios

| Example | Product Type | Recommended Configuration Family |
|---|---|---|
| [unity-game](unity-game/) | Unity 2D game | `stage-N-unity-game.configuration.yaml` |
| [web-application](web-application/) | Web application | `stage-N-web-application.configuration.yaml` |
| [shared-library](shared-library/) | Shared library / SDK | `stage-N-shared-library.configuration.yaml` |
| [minimal-complete-run/todo-web-app](minimal-complete-run/todo-web-app/) | Web application | `stage-N-web-application.configuration.yaml` |
| [minimal-complete-run/unity-button-click-prototype](minimal-complete-run/unity-button-click-prototype/) | Unity game prototype | `stage-N-unity-game.configuration.yaml` |

## Included complete miniature runs

| Complete Run | Product Type | Demonstrates |
|---|---|---|
| [minimal-complete-run/todo-web-app](minimal-complete-run/todo-web-app/) | Web application | Complete four-stage artifact chain plus fabricated React/TypeScript files. |
| [minimal-complete-run/unity-button-click-prototype](minimal-complete-run/unity-button-click-prototype/) | Unity game prototype | Complete four-stage artifact chain plus UI Toolkit text artifacts and external Unity validation handling. |

## What each example contains

```text
input/
  project-brief.md
  stage-1-context-packet.md
configuration/
  pipeline.override.yaml
runbooks/
  01-run-stage-1.md
  02-run-stage-2.md
  03-run-stage-3.md
  04-run-stage-4.md
artifact-skeletons/
  stage-1-artifact-skeleton.md
  stage-2-artifact-skeleton.md
  stage-3-artifact-skeleton.md
  stage-4-artifact-skeleton.md
checklists/
  stage-4-validation-checklist.md
decision-ledger-comparison/
  sample-decision-ledger.csv
traceability/
  sample-traceability-matrix.csv
```

## How to use

1. Choose the example closest to your product type.
2. Open `input/stage-1-context-packet.md`.
3. Paste it into the Stage 1 prompt with the matching configuration profile.
4. Run Stage 1 through Stage 4 using the runbooks.
5. Use the skeletons, checklists, and sample CSV files as formatting references.

## Important note

The scenario artifact skeletons are structural references. The `minimal-complete-run/` examples include compact completed artifacts and fabricated text files so readers can inspect a full Stage 1 through Stage 4 chain.


## Complete miniature runs

The `minimal-complete-run/` directory contains two complete, compact end-to-end examples:

```text
minimal-complete-run/todo-web-app/
minimal-complete-run/unity-button-click-prototype/
```

Use these to see how the pipeline artifacts look when populated across all four stages.


## Complete miniature runs

Complete miniature runs contain compact completed Stage 1 through Stage 4 artifacts. Use them when you want to see what generated artifacts, ledgers, traceability matrices, fabricated files, validation reports, and handoff packets look like after a full pass.
