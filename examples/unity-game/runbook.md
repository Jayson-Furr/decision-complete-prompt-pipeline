# Runbook — Unity Game Example

## Stage 1

Prompt:

```text
stage-1-design-specification/prompts/Stage-1-Prompt-3-Medium-Stakes-Design-Interview.md
```

Inputs:

```text
examples/unity-game/stage-1-input.md
examples/unity-game/configuration-overrides.yaml
configuration-examples/stage-1-unity-game.configuration.yaml
```

Expected result:

```text
Stage 1 artifact with Unity game design, asset packets, requirements, acceptance criteria, placeholders, review flags, and Stage 2 handoff contract.
```

## Stage 2

Prompt:

```text
stage-2-execution-planning/prompts/Stage-2-Prompt-3-Medium-Stakes-Execution-Interview.md
```

Input:

```text
Full Stage 1 artifact.
```

Expected result:

```text
Unity work packages, expected artifact manifest, generated Stage 3 prompts, dependency graph, QA matrix, and Stage 3 handoff contract.
```

## Stage 3

Prompt:

```text
stage-3-fabrication/prompts/Stage-3-Prompt-3-Medium-Stakes-Fabrication-Interview.md
```

Input:

```text
Full Stage 2 artifact.
```

Expected result:

```text
Fabricated C#, UXML, USS, JSON, YAML, Markdown, and external-tool-ready packets where possible. Unity Editor artifacts should be accurately marked external-tool-required or external-validation-required when not actually created or validated.
```

## Stage 4

Prompt:

```text
stage-4-validation-packaging/prompts/Stage-4-Prompt-3-Medium-Stakes-Finalization-Interview.md
```

Input:

```text
Full Stage 3 artifact.
```

Expected result:

```text
Final handoff package with Unity validation status, external validation register, repair log, final artifact manifest, approval packet, and release-not-performed statement.
```
