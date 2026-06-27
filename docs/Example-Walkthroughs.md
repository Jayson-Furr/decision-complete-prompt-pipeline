# Example Walkthroughs

## Purpose

This document explains how to use the example project packages included in `examples/`.

The examples demonstrate how to start from a project brief, select a configuration profile, run Stage 1, and continue through the pipeline.

---

## Included example scenario packets

```text
examples/unity-game/
examples/web-application/
examples/shared-library/
```

## Included complete miniature runs

```text
examples/minimal-complete-run/todo-web-app/
examples/minimal-complete-run/unity-button-click-prototype/
```

Each example contains:

```text
README.md
project-brief.md
stage-1-input.md
configuration-overrides.yaml
runbook.md
source-context/
stage-artifact-stubs/
```

---

## Example 1 — Unity game

Use this example when you want to see how the pipeline handles a game project with engine-specific concerns.

Start with:

```text
examples/unity-game/stage-1-input.md
examples/unity-game/configuration-overrides.yaml
```

Recommended Stage 1 prompt:

```text
stage-1-design-specification/prompts/Stage-1-Prompt-3-Medium-Stakes-Design-Interview.md
```

Expected focus areas:

```text
- Unity version;
- render pipeline;
- UI framework;
- input system;
- scenes;
- assets;
- external-tool-required binary assets;
- Unity Editor validation requirements.
```

---

## Example 2 — Web application

Use this example for a browser-based product with authentication, API, data, and privacy considerations.

Start with:

```text
examples/web-application/stage-1-input.md
examples/web-application/configuration-overrides.yaml
```

Recommended Stage 1 prompt:

```text
stage-1-design-specification/prompts/Stage-1-Prompt-3-Medium-Stakes-Design-Interview.md
```

Expected focus areas:

```text
- user roles;
- screens;
- API surface;
- data model;
- authentication;
- privacy;
- deployment assumptions;
- external validation.
```

---

## Example 3 — Shared library / SDK

Use this example for a developer-facing package.

Start with:

```text
examples/shared-library/stage-1-input.md
examples/shared-library/configuration-overrides.yaml
```

Recommended Stage 1 prompt:

```text
stage-1-design-specification/prompts/Stage-1-Prompt-3-Medium-Stakes-Design-Interview.md
```

Expected focus areas:

```text
- API design;
- versioning;
- compatibility;
- package publishing;
- documentation;
- examples;
- tests;
- license and dependency review.
```

---

## Artifact stubs

Each example includes `stage-artifact-stubs/`.

These files are not complete generated artifacts. They are small structural examples showing:

```text
- correct boundary markers;
- artifact header pattern;
- completion gate pattern;
- handoff flow;
- placeholder and review-gated status examples.
```

Use them as shape references only.

Do not treat them as real Stage 1, Stage 2, Stage 3, or Stage 4 outputs.

---

## Running an example end to end

1. Open the example `stage-1-input.md`.
2. Open the recommended Stage 1 prompt.
3. Paste the prompt and then the example input.
4. Include the example `configuration-overrides.yaml` as additional context.
5. Save the Stage 1 artifact.
6. Paste the Stage 1 artifact into Stage 2.
7. Continue through Stage 3 and Stage 4.
8. Compare your output to the artifact stubs for structure only.

---

## Using example configurations

Example-specific configuration files are intentionally small override files.

They should be used together with the broader configuration examples in:

```text
configuration-examples/
```

For example, the Unity game example can be run with:

```text
configuration-examples/stage-1-unity-game.configuration.yaml
examples/unity-game/configuration-overrides.yaml
```

The stage prompt should normalize the effective configuration inside the stage artifact.


## Miniature complete run walkthrough

For a complete artifact-chain example, open `examples/minimal-complete-run/todo-web-app/` or `examples/minimal-complete-run/unity-button-click-prototype/` and read the numbered directories in order. These examples show populated artifacts rather than skeletons.
