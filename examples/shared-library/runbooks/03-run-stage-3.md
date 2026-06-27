# Runbook — Stage 3 for ConfigWeave

## Prompt file

```text
stage-3-fabrication/prompts/Stage-3-Prompt-3-Medium-Stakes-Fabrication-Interview.md
```

## Configuration profile

```text
configuration-examples/stage-3-shared-library.configuration.yaml
```

## Required input

```text
the full Stage 2 artifact including boundary markers
```

## Expected output

```text
100% Fabrication-Complete Deliverable Package Suite
```

## Procedure

1. Open the prompt file listed above.
2. Paste or attach the required input.
3. Include the configuration profile or project-specific override if supported by your AI environment.
4. Run the prompt.
5. Save the full output artifact, including boundary markers.
6. Check the completion gate.
7. Use the resulting artifact as the input to the next stage.

## Quality checks before continuing

```text
- Artifact boundary markers are present.
- Artifact header is present.
- Artifact status is explicit.
- Decision register is present.
- Decision ledger or below-threshold summary is present.
- Placeholders are registered.
- Review-gated items are registered.
- Traceability is present.
- Handoff packet is present.
- Completion gate is present.
```

## Stop conditions

Stop before the next stage if the artifact is marked blocked, malformed, or missing required source authority. Rerun the current stage or provide the missing input before proceeding.
