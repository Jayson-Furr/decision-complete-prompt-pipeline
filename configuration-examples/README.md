# Configuration Examples

This directory contains reusable YAML configuration profiles for `decision-complete-prompt-pipeline` version `1.0.0`.

The configuration files are examples and defaults. A stage prompt treats a configuration file as active only when you attach it, paste it, or explicitly name it as the configuration for that run.

## Files

### Stage defaults

```text
stage-1-default.configuration.yaml
stage-2-default.configuration.yaml
stage-3-default.configuration.yaml
stage-4-default.configuration.yaml
```

### Unity game profiles

```text
stage-1-unity-game.configuration.yaml
stage-2-unity-game.configuration.yaml
stage-3-unity-game.configuration.yaml
stage-4-unity-game.configuration.yaml
```

### Web application profiles

```text
stage-1-web-application.configuration.yaml
stage-2-web-application.configuration.yaml
stage-3-web-application.configuration.yaml
stage-4-web-application.configuration.yaml
```

### Shared library / SDK profiles

```text
stage-1-shared-library.configuration.yaml
stage-2-shared-library.configuration.yaml
stage-3-shared-library.configuration.yaml
stage-4-shared-library.configuration.yaml
```

### Index

```text
configuration-index.yaml
```

## How to use

Use the global `pipeline.configuration.yaml` for repository-wide defaults, then add a stage-specific configuration when running a stage. For example, for a Unity game Stage 1 run, paste or attach:

```text
pipeline.configuration.yaml
configuration-examples/stage-1-unity-game.configuration.yaml
```

The active prompt file still controls the prompt mode unless you explicitly instruct the agent to switch modes.

## Safety and authority rules

Configuration files may guide process, output structure, and defaults. They may not override safety rules or prior-stage authority.

```text
Stage 1 controls design.
Stage 2 controls execution planning.
Stage 3 controls fabricated outputs.
Stage 4 controls validation, repair classification, packaging, and final handoff.
```

Configuration must not authorize deployment, public release, app store submission, credential use, destructive operations, rights clearance, compliance claims, or professional approvals by implication.

## Profile roadmap

`profile-family-roadmap.yaml` lists included and recommended future configuration profile families.
