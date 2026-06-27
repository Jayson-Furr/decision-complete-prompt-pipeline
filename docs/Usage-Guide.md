# Usage Guide

This guide explains how to use DecisionComplete Prompt Pipeline for a complete digital product workflow.

## What the pipeline does

The pipeline converts rough input into four increasingly concrete artifacts:

| Stage | Output | Main Question Answered |
|---|---|---|
| Stage 1 | 100% Decision-Complete Digital Product Design Specification Suite | What is the product? |
| Stage 2 | 100% Execution-Ready Fabrication Package Suite | How should it be fabricated? |
| Stage 3 | 100% Fabrication-Complete Deliverable Package Suite | What deliverables were fabricated? |
| Stage 4 | 100% Validation-Complete Final Handoff Package Suite | What is validated, repaired, included, blocked, or ready? |

The artifacts are designed to be copied directly from one stage into the next stage.

## Standard operating workflow

1. Collect project input.
2. Select a prompt mode.
3. Run Stage 1.
4. Copy the entire Stage 1 artifact, including boundary markers.
5. Run Stage 2 with the Stage 1 artifact.
6. Copy the entire Stage 2 artifact, including boundary markers.
7. Run Stage 3 with the Stage 2 artifact.
8. Copy the entire Stage 3 artifact, including boundary markers.
9. Run Stage 4 with the Stage 3 artifact.
10. Use the Stage 4 final handoff package as the authoritative final delivery record.

## What input can be provided to Stage 1

Stage 1 accepts rough or polished input:

```text
- a one-sentence idea;
- project name;
- app, game, service, or library description;
- markdown design notes;
- screenshots or mockups;
- concept art or identity images;
- technical preferences;
- platform preferences;
- configuration files;
- feature lists;
- workflow notes;
- user stories;
- source provenance notes.
```

Minimal input is allowed. Missing values become controlled placeholders, not vague `TBD` values.

## What input is required by later stages

| Stage | Required Input |
|---|---|
| Stage 2 | Full Stage 1 artifact |
| Stage 3 | Full Stage 2 artifact |
| Stage 4 | Full Stage 3 artifact |

Later stages may accept prior artifacts as reference, but the immediate prior stage is the primary required input.

## Choosing a prompt mode

The recommended default is medium-stakes mode.

| Mode | Best For |
|---|---|
| No Questions | Fast internal drafts and rapid prototypes. |
| Low-Stakes Interview | Maximum user control. |
| Medium-Stakes Interview | Most production planning and balanced usage. |
| High-Stakes Interview | Fast flow with safety interruptions only. |

## Using configuration files

Configuration files are optional. Use them when you want consistent behavior across runs.

```text
pipeline.configuration.yaml
configuration-examples/stage-1-default.configuration.yaml
configuration-examples/stage-1-unity-game.configuration.yaml
configuration-examples/stage-1-web-application.configuration.yaml
configuration-examples/stage-1-shared-library.configuration.yaml
```

Stage-specific configuration controls process. It may not override safety rules or locked upstream authority.

## How to rerun a stage

Rerun the earliest stage affected by the change.

| You Want To Change | Rerun |
|---|---|
| Product concept, scope, feature design, screens, assets | Stage 1, then downstream stages |
| Work package boundaries, dependencies, generated Stage 3 prompts | Stage 2, then downstream stages |
| Fabricated files, code, asset prompt packets | Stage 3, then Stage 4 |
| Validation depth, repair policy, package inclusion, final warnings | Stage 4 |

## What “complete” means

Completion means every item is accounted for, not that every item passed cleanly.

Examples:

```text
Decision-Complete: every design decision is resolved, placeholder-complete, review-gated, excluded, or not applicable.
Execution-Ready: every work package is ready, blocked, review-gated, placeholder-complete, deferred, or not applicable.
Fabrication-Complete: every work package was executed, blocked, review-gated, external-tool-required, placeholder-complete, partially fabricated, or not applicable.
Validation-Complete: every artifact was validated, repaired, classified, blocked, review-gated, excluded, external-validation-required, or not applicable.
```

## Non-negotiable safety rules

The pipeline must not invent:

```text
- approvals;
- licenses;
- credentials;
- rights clearance;
- legal status;
- certification;
- compliance status;
- production deployment status;
- successful release status;
- app store approval.
```

It must not perform deployment, publishing, credential use, destructive operations, or external API actions without explicit authorization.
