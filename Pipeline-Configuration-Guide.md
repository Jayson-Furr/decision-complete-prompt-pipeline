# Pipeline Configuration Guide

## Purpose

Configuration files control process defaults for the Four-Stage Digital Product Fabrication Prompt Pipeline.

Configuration files are optional. If no configuration is provided, each prompt uses safe built-in defaults.

## Configuration files

```text
pipeline.configuration.yaml
stage-1-design-specification.configuration.yaml
stage-2-execution-planning.configuration.yaml
stage-3-fabrication.configuration.yaml
stage-4-validation-packaging.configuration.yaml
```

## Priority rule

When inputs conflict, use this priority order:

```text
1. Safety, integrity, non-deception, and no-unauthorized-side-effect rules.
2. Active stage prompt required operating rules.
3. User latest direct instruction.
4. Active stage configuration file.
5. Pipeline configuration file.
6. Prior-stage artifact according to authority scope.
7. Other user-provided context.
8. AI defaults.
```

## What configuration may control

```text
- default prompt modes;
- output structure;
- decision logging;
- traceability requirements;
- work package strategy;
- validation depth;
- repair policy;
- machine-readable companion data;
- file naming conventions.
```

## What configuration may not override

```text
- safety rules;
- non-deception rules;
- prior-stage authority;
- placeholder preservation;
- review-gated item preservation;
- high-stakes authorization requirements;
- no-unauthorized-deployment rules;
- no-unauthorized-publishing rules;
- no-unauthorized-credential-use rules;
- no-unauthorized-destructive-operation rules.
```

## Recommended default modes

```yaml
default_prompt_modes:
  stage_1: "medium_stakes_design_interview"
  stage_2: "medium_stakes_execution_interview"
  stage_3: "medium_stakes_fabrication_interview"
  stage_4: "medium_stakes_finalization_interview"
```

## Configuration examples

Stage-specific and product-type-specific examples are stored in `configuration-examples/`.

## Normalized active configuration

Each stage should output a normalized active configuration showing which values were applied, defaulted, overridden, or ignored.


## Version 1.0.0 Configuration Profile Set

The public repository distribution includes these active examples:

| Profile Family | Stage 1 | Stage 2 | Stage 3 | Stage 4 |
|---|---|---|---|---|
| Default | `stage-1-default.configuration.yaml` | `stage-2-default.configuration.yaml` | `stage-3-default.configuration.yaml` | `stage-4-default.configuration.yaml` |
| Unity game | `stage-1-unity-game.configuration.yaml` | `stage-2-unity-game.configuration.yaml` | `stage-3-unity-game.configuration.yaml` | `stage-4-unity-game.configuration.yaml` |
| Web application | `stage-1-web-application.configuration.yaml` | `stage-2-web-application.configuration.yaml` | `stage-3-web-application.configuration.yaml` | `stage-4-web-application.configuration.yaml` |
| Shared library / SDK | `stage-1-shared-library.configuration.yaml` | `stage-2-shared-library.configuration.yaml` | `stage-3-shared-library.configuration.yaml` | `stage-4-shared-library.configuration.yaml` |

Each product-type profile extends the corresponding stage default and keeps the same safety, authority, placeholder, review-gated, traceability, and machine-readable companion requirements.

## Authority model statement

```text
Stage 1 controls design.
Stage 2 controls execution planning.
Stage 3 controls fabricated outputs.
Stage 4 controls validation, repair classification, packaging, and final handoff.
```
