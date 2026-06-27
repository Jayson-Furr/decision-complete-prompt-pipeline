# Shared Configuration Priority Rules

## Universal priority order

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

## Stage authority overlay

```text
Stage 1 controls design.
Stage 2 controls execution planning.
Stage 3 controls fabricated outputs.
Stage 4 controls validation, repair classification, packaging, and final handoff.
```

## Configuration may not override

```text
safety rules
non-deception rules
prior-stage authority
placeholder preservation
review-gated preservation
high-stakes authorization requirements
no-unauthorized-deployment rules
no-unauthorized-credential-use rules
no-unauthorized-destructive-operation rules
```

## Conflict log format

| Conflict ID | Sources in Conflict | Conflict Summary | Stakes Level | Priority Resolution | Final Handling | Review Needed? |
|---|---|---|---|---|---|---|

## Normalized active configuration skeleton

```yaml
configuration_metadata:
  config_name: "normalized-active-stage-configuration"
  config_version: "1.0.0"
  pipeline_name: "DecisionComplete Prompt Pipeline"
configuration_sources: {}
effective_prompt_mode: {}
authority_constraints:
  stage_1_controls_design: true
  stage_2_controls_execution_plan: true
  stage_3_controls_fabricated_artifact_record: true
  stage_4_controls_validation_packaging_and_handoff: true
safety_constraints:
  no_unsupported_fact_fabrication: true
  no_unauthorized_deployment: true
  no_unauthorized_publishing: true
  no_unauthorized_credential_use: true
  no_unauthorized_destructive_operations: true
applied_defaults: []
overridden_values: []
ignored_values: []
conflict_resolutions: []
status:
  normalized_configuration_complete: true
```
