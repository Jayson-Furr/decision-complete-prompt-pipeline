# Stage 3 Overview — Fabrication

Stage 3 is the fabrication stage of **DecisionComplete Prompt Pipeline** version `1.0.0`.

Stage 3 consumes the Stage 2 artifact:

```text
100% Execution-Ready Fabrication Package Suite
```

and produces:

```text
100% Fabrication-Complete Deliverable Package Suite
```

## Stage 3 responsibility

Stage 3 executes the locked Stage 2 work packages. It fabricates text-based deliverables where possible, records binary or tool-dependent deliverables accurately, preserves placeholders and review-gated items, performs preliminary validation, and prepares a Stage 4 handoff contract.

Stage 3 may fabricate source code files, configuration files, schemas, tests, documentation, prompts, scripts, asset metadata, UI markup, style files, sample data, and external-tool-ready asset packets.

Stage 3 must not redesign the product, re-plan Stage 2 execution, silently change required outputs, perform final Stage 4 validation, package the final release, deploy, publish, submit, use credentials, or perform destructive operations.

## Prompt set

| Prompt | Mode | Use When |
|---|---|---|
| Stage-3-Prompt-1-No-Questions-Full-AI-Fabrication.md | No Questions | Maximum speed; AI resolves safe fabrication decisions and logs all meaningful decisions. |
| Stage-3-Prompt-2-Low-Stakes-Fabrication-Interview.md | Low-Stakes Interview | Maximum fabrication control; asks for low, medium, and high decisions. |
| Stage-3-Prompt-3-Medium-Stakes-Fabrication-Interview.md | Medium-Stakes Interview | Recommended default; asks for medium and high decisions. |
| Stage-3-Prompt-4-High-Stakes-Fabrication-Interview.md | High-Stakes Interview | Fast operation; asks only for high-stakes decisions. |

## Required output

Every Stage 3 run should produce a bounded artifact:

```text
<<<BEGIN STAGE 3 ARTIFACT: 100% FABRICATION-COMPLETE DELIVERABLE PACKAGE SUITE>>>
...
<<<END STAGE 3 ARTIFACT>>>
```

Stage 4 consumes this artifact for validation, repair, packaging, and final handoff.
