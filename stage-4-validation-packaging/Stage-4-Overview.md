# Stage 4 Overview — Validation, Repair, Packaging, and Final Handoff

Stage 4 is the finalization stage of **DecisionComplete Prompt Pipeline** version `1.0.0`.

Stage 4 consumes the Stage 3 artifact:

```text
100% Fabrication-Complete Deliverable Package Suite
```

and produces:

```text
100% Validation-Complete Final Handoff Package Suite
```

## Stage 4 responsibility

Stage 4 validates fabricated deliverables, repairs only within approved scope, classifies every artifact, records unresolved items, prepares final package manifests, produces approval packets, and creates final handoff instructions.

Stage 4 controls validation status, repair classification, package inclusion, warnings, unresolved items, and final handoff readiness.

Stage 4 must not redesign the product, re-plan execution, silently change Stage 3 outputs beyond approved repair scope, deploy, publish, submit, use credentials, perform destructive operations, or claim approval unless explicitly authorized and actually performed.

## Prompt set

| Prompt | Mode | Use When |
|---|---|---|
| Stage-4-Prompt-1-No-Questions-Full-AI-Validation-Packaging.md | No Questions | Maximum speed; validates and packages with safe defaults. |
| Stage-4-Prompt-2-Low-Stakes-Finalization-Interview.md | Low-Stakes Interview | Maximum finalization control. |
| Stage-4-Prompt-3-Medium-Stakes-Finalization-Interview.md | Medium-Stakes Interview | Recommended default. |
| Stage-4-Prompt-4-High-Stakes-Finalization-Interview.md | High-Stakes Interview | Fast operation with high-stakes interruptions only. |

## Required output

Every Stage 4 run should produce a bounded artifact:

```text
<<<BEGIN STAGE 4 ARTIFACT: 100% VALIDATION-COMPLETE FINAL HANDOFF PACKAGE SUITE>>>
...
<<<END STAGE 4 ARTIFACT>>>
```

The final handoff status must be one of:

```text
Ready
Ready with Warnings
Review-Gated
Blocked
External Validation Required
```
