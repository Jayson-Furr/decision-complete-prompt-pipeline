# Configuration Profile Selection Guide

Configuration profiles help you run the same pipeline consistently across different product types.

## Configuration hierarchy

Use configuration in this order:

```text
1. pipeline.configuration.yaml for global defaults.
2. stage-specific default profile for general behavior.
3. product-type-specific profile when the product type is known.
4. project-specific override when you need custom settings.
```

## Default profiles

Use defaults for generic products or mixed products:

```text
configuration-examples/stage-1-default.configuration.yaml
configuration-examples/stage-2-default.configuration.yaml
configuration-examples/stage-3-default.configuration.yaml
configuration-examples/stage-4-default.configuration.yaml
```

## Unity game profiles

Use these when the product is a Unity game or Unity prototype:

```text
configuration-examples/stage-1-unity-game.configuration.yaml
configuration-examples/stage-2-unity-game.configuration.yaml
configuration-examples/stage-3-unity-game.configuration.yaml
configuration-examples/stage-4-unity-game.configuration.yaml
```

These profiles add Unity-specific decisions for scenes, UI Toolkit, uGUI, Input System, packages, ScriptableObjects, prefabs, asset import settings, external Unity Editor validation, builds, and release authorization.

## Web application profiles

Use these when the product is a web application, SaaS application, dashboard, admin tool, or browser-based system:

```text
configuration-examples/stage-1-web-application.configuration.yaml
configuration-examples/stage-2-web-application.configuration.yaml
configuration-examples/stage-3-web-application.configuration.yaml
configuration-examples/stage-4-web-application.configuration.yaml
```

These profiles emphasize routes, pages, components, API contracts, data models, authentication, authorization, privacy, security, environment configuration, tests, deployment preparation, and external validation.

## Shared library / SDK profiles

Use these when the product is a library, SDK, package, module, or developer-facing integration layer:

```text
configuration-examples/stage-1-shared-library.configuration.yaml
configuration-examples/stage-2-shared-library.configuration.yaml
configuration-examples/stage-3-shared-library.configuration.yaml
configuration-examples/stage-4-shared-library.configuration.yaml
```

These profiles emphasize API design, versioning, package formats, examples, documentation, tests, compatibility, licensing, package registry release, and public API stability.

## Project-specific overrides

Create a small project override rather than editing the repository profiles directly.

Example:

```yaml
configuration_metadata:
  config_name: "my-project-stage-1"
  extends: "configuration-examples/stage-1-unity-game.configuration.yaml"
  applies_to_stage: "stage_1"

product:
  product_name: "Starfall Cartographer"
  release_tier: "Vertical Slice"

toolchain:
  unity_version: "Unity 6000.4.11f1"
  ui_framework: "UI Toolkit"
```

## Priority rule

The active prompt file still controls the prompt mode unless the user explicitly switches modes. Configuration controls process defaults, not locked upstream authority.
