# Minimal Complete Runs

This directory contains small, complete example pipeline runs for **DecisionComplete Prompt Pipeline**.

Unlike the scenario folders in `examples/unity-game/`, `examples/web-application/`, and `examples/shared-library/`, these examples include compact but complete Stage 1 through Stage 4 artifacts, sample ledgers, traceability matrices, fabricated text files, and final handoff records.

## Included complete runs

| Example | Product Type | Purpose |
|---|---|---|
| [todo-web-app](todo-web-app/) | Web application | Demonstrates a simple non-deployed local Todo app with React/TypeScript-style fabricated files. |
| [unity-button-click-prototype](unity-button-click-prototype/) | Unity game prototype | Demonstrates Unity-specific text artifact fabrication, external-tool-required Unity Editor assets, and external validation handling. |

## How to use these examples

1. Open the example README.
2. Review `00-source-input/`.
3. Read each stage artifact in order.
4. Compare the decision ledgers and traceability matrices to the artifacts.
5. Inspect Stage 3 fabricated files.
6. Review the Stage 4 final handoff packet to understand package classification.

## Important scope note

These examples are intentionally small. They are not production applications. Their purpose is to show what completed pipeline artifacts look like and how IDs, ledgers, traceability, blockers, external-validation items, and final handoff status connect across all four stages.
