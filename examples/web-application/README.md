# Web Application Example

This example demonstrates how to run DecisionComplete Prompt Pipeline for a **Web application**.

## Example product

```text
Name: Field Notes Hub
Type: Web application
Description: A browser-based research note workspace for organizing field observations, tagged notes, attachments, and lightweight team review workflows.
```

## Recommended prompt path

```text
Stage 1: stage-1-design-specification/prompts/Stage-1-Prompt-3-Medium-Stakes-Design-Interview.md
Stage 2: stage-2-execution-planning/prompts/Stage-2-Prompt-3-Medium-Stakes-Execution-Interview.md
Stage 3: stage-3-fabrication/prompts/Stage-3-Prompt-3-Medium-Stakes-Fabrication-Interview.md
Stage 4: stage-4-validation-packaging/prompts/Stage-4-Prompt-3-Medium-Stakes-Finalization-Interview.md
```

## Recommended configuration profiles

```text
Stage 1: configuration-examples/stage-1-web-application.configuration.yaml
Stage 2: configuration-examples/stage-2-web-application.configuration.yaml
Stage 3: configuration-examples/stage-3-web-application.configuration.yaml
Stage 4: configuration-examples/stage-4-web-application.configuration.yaml
```

## Directory contents

```text
input/project-brief.md
input/stage-1-context-packet.md
configuration/pipeline.override.yaml
runbooks/01-run-stage-1.md
runbooks/02-run-stage-2.md
runbooks/03-run-stage-3.md
runbooks/04-run-stage-4.md
artifact-skeletons/stage-1-artifact-skeleton.md
artifact-skeletons/stage-2-artifact-skeleton.md
artifact-skeletons/stage-3-artifact-skeleton.md
artifact-skeletons/stage-4-artifact-skeleton.md
checklists/stage-4-validation-checklist.md
decision-ledger-comparison/sample-decision-ledger.csv
traceability/sample-traceability-matrix.csv
```

## Key preferences

- TypeScript
- React-style component model
- Server API contract documented before implementation
- Responsive desktop and tablet layout
- Authentication review-gated
- No production deployment in pipeline

## High-stakes considerations

- Authentication
- Authorization
- Personal data handling
- File attachments
- Production deployment authorization

## Validation focus

- Route coverage
- API contract validation
- Schema validation
- Accessibility review
- Security and privacy review

## How to run this example

1. Open `input/stage-1-context-packet.md`.
2. Paste it into the Stage 1 prompt.
3. Include the configuration profile named above, or use `configuration/pipeline.override.yaml` as a small project-specific override.
4. Run the four stage prompts in order.
5. Use the artifact skeletons only as structural references.
6. Use the sample CSV files to verify ledger and traceability formatting.
