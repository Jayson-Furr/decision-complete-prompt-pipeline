# Pipeline Overview

Repository: `decision-complete-prompt-pipeline`

## DecisionComplete Prompt Pipeline

DecisionComplete Prompt Pipeline is a four-stage prompt pipeline for turning rough digital product input into a validated final handoff package.

The four stages are:

```text
Stage 1: Decide the design.
Stage 2: Decide the fabrication plan.
Stage 3: Fabricate the deliverables.
Stage 4: Validate, repair, package, and prepare final handoff.
```

## Stage model

| Stage | Purpose | Output |
|---|---|---|
| Stage 1 | Convert user context into a complete design specification | 100% Decision-Complete Digital Product Design Specification Suite |
| Stage 2 | Convert the locked design into execution-ready work packages | 100% Execution-Ready Fabrication Package Suite |
| Stage 3 | Execute work packages and create deliverables where possible | 100% Fabrication-Complete Deliverable Package Suite |
| Stage 4 | Validate, repair within scope, package, and prepare final handoff | 100% Validation-Complete Final Handoff Package Suite |

## Authority model

```text
Stage 1 controls design.
Stage 2 controls execution planning.
Stage 3 controls fabricated outputs.
Stage 4 controls validation, repair classification, packaging, and final handoff.
```

Later stages must preserve earlier-stage authority. They may classify, preserve, block, review-gate, or externalize unresolved items, but must not silently rewrite upstream decisions.

## Prompt modes

Each stage provides four prompt modes:

```text
Prompt 1: No Questions
Prompt 2: Low-Stakes Interview
Prompt 3: Medium-Stakes Interview
Prompt 4: High-Stakes Interview
```

The recommended default is Prompt 3 for each stage.

## Artifact handoff

Each stage artifact is copied into the next stage prompt using exact boundary markers.

```text
Stage 1 artifact → Stage 2 prompt
Stage 2 artifact → Stage 3 prompt
Stage 3 artifact → Stage 4 prompt
```

## Final output

The final output is a Stage 4 artifact with one of these final handoff statuses:

```text
Ready
Ready with Warnings
Review-Gated
Blocked
External Validation Required
```

`Validation-Complete` means every item is accounted for. It does not necessarily mean defect-free, deployed, published, certified, approved, or rights-cleared.
