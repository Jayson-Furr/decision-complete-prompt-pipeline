# Profile Authoring Guide

## Purpose

This guide explains how to create new product-type profile families for the DecisionComplete Prompt Pipeline.

A profile family is a set of four stage configuration files that specialize the pipeline for one product type while preserving the shared stage authority model.

Example profile family:

```text
configuration-examples/stage-1-web-application.configuration.yaml
configuration-examples/stage-2-web-application.configuration.yaml
configuration-examples/stage-3-web-application.configuration.yaml
configuration-examples/stage-4-web-application.configuration.yaml
```

## Profile family rule

Every public profile family should include all four stages:

```text
Stage 1 profile: design-specific decisions and design-surface coverage.
Stage 2 profile: execution-planning decomposition, expected artifacts, QA planning, and Stage 3 prompt context.
Stage 3 profile: fabrication behavior, external-tool handling, preliminary validation, and Stage 4 handoff notes.
Stage 4 profile: final validation, repair policy, package classification, final handoff, approval, and release handling.
```

A profile must not override the pipeline authority model:

```text
Stage 1 controls design.
Stage 2 controls execution planning.
Stage 3 controls fabricated outputs.
Stage 4 controls validation, repair classification, packaging, and final handoff.
```

## Minimum profile metadata

Each configuration file should include:

```yaml
configuration_metadata:
  config_name: "stage-1-example-profile"
  config_version: "1.0.0"
  pipeline_name: "DecisionComplete Prompt Pipeline"
  repository_name: "decision-complete-prompt-pipeline"
  applies_to_stage: "stage_1"
  configuration_scope: "product_type_specific"
  extends: "stage-1-default.configuration.yaml"
  product_type_profile: "example_profile"
```

Use the matching default extension for the stage:

```text
stage-1-default.configuration.yaml
stage-2-default.configuration.yaml
stage-3-default.configuration.yaml
stage-4-default.configuration.yaml
```

## Required safety baseline

Every profile must preserve safety and non-deception rules:

```yaml
safety_and_integrity:
  preserve_placeholders: true
  preserve_review_gated_items: true
  no_public_release_without_explicit_authorization: true
  no_production_deployment_without_explicit_authorization: true
  no_credentials_or_private_data_use_without_explicit_authorization: true
  no_destructive_operations_without_explicit_authorization: true
```

Profiles may add more safety rules. They must not remove or weaken the baseline.

## Required profile-depth areas

A useful profile should define product-specific behavior in at least these areas:

| Stage | Recommended profile-specific areas |
|---|---|
| Stage 1 | product classification, design surfaces, product-specific assets, data, security/privacy, accessibility, release constraints |
| Stage 2 | product-specific work packages, dependency planning, expected artifacts, QA matrix, external validation planning |
| Stage 3 | product-specific fabricatable files, external-tool items, preliminary validation, artifact manifests, test fabrication |
| Stage 4 | product-specific validation methods, repair policy, package inclusion, external validation, approval/release handling |

## Recommended profile families

The repository currently includes:

```text
default
unity_game
web_application
shared_library
```

Recommended future profile families:

```text
unreal_game
godot_game
web_service
mobile_application
desktop_application
website
mobile_service
desktop_service
sdk
cli_developer_tool
ai_agent_application
data_pipeline
design_system_ui_kit
documentation_site
```

## Naming convention

Use this file naming pattern:

```text
stage-1-[profile-family].configuration.yaml
stage-2-[profile-family].configuration.yaml
stage-3-[profile-family].configuration.yaml
stage-4-[profile-family].configuration.yaml
```

Use machine-readable profile IDs in snake case:

```text
web_application
shared_library
unity_game
mobile_application
```

Use file names in kebab case:

```text
web-application
shared-library
unity-game
mobile-application
```

## Profile authoring checklist

```text
| Check | Pass / Fail | Notes |
|---|---|---|
| All four stage profiles exist | [Pass / Fail] | [Notes] |
| Each profile declares configuration_metadata.extends | [Pass / Fail] | [Notes] |
| Each profile uses the correct applies_to_stage value | [Pass / Fail] | [Notes] |
| Each profile preserves stage authority | [Pass / Fail] | [Notes] |
| Each profile preserves safety and integrity rules | [Pass / Fail] | [Notes] |
| Each profile includes product-specific Stage 1 design surfaces | [Pass / Fail] | [Notes] |
| Each profile includes product-specific Stage 2 work package strategy | [Pass / Fail] | [Notes] |
| Each profile includes product-specific Stage 3 fabrication rules | [Pass / Fail] | [Notes] |
| Each profile includes product-specific Stage 4 validation/finalization rules | [Pass / Fail] | [Notes] |
| External-tool-required items are handled honestly | [Pass / Fail] | [Notes] |
| External-validation-required items are handled honestly | [Pass / Fail] | [Notes] |
| Public release, deployment, publishing, and credential use require explicit authorization | [Pass / Fail] | [Notes] |
```

## Profile validation

Run:

```bash
python tools/validate-profile-depth.py
python tools/validate-configurations.py
python tools/run-all-checks.py
```

These tools check repository/profile structure and consistency. They do not prove that a downstream generated product is semantically correct, secure, compliant, legally approved, or production-ready.
