# Complete Miniature Examples

The repository includes two small, complete pipeline runs under `examples/minimal-complete-run/`:

```text
examples/minimal-complete-run/todo-web-app/
examples/minimal-complete-run/unity-button-click-prototype/
```

These examples are designed to answer a practical question:

```text
What does a completed Stage 1 → Stage 2 → Stage 3 → Stage 4 pipeline run look like?
```

## Todo web app

The Todo web app example demonstrates a simple web application with no backend, no authentication, no payments, no analytics, and no deployment. It includes:

```text
- Stage 1 design specification artifact;
- Stage 2 execution package artifact;
- Stage 3 fabricated deliverable artifact;
- Stage 3 fabricated React/TypeScript-style text files;
- Stage 4 final validation and handoff artifact;
- decision ledger CSV files;
- traceability matrix CSV files;
- final handoff packet YAML.
```

## Unity button-click prototype

The Unity button-click prototype demonstrates a small Unity game prototype with a UI button that increments a counter. It includes:

```text
- Unity-specific Stage 1 design artifact;
- Unity-specific Stage 2 execution package artifact;
- Stage 3 fabricated C#, UXML, USS, documentation, and external Unity Editor packets;
- Stage 4 final handoff artifact that honestly marks Unity Editor validation as external-validation-required;
- decision ledger CSV files;
- traceability matrix CSV files;
- final handoff packet YAML.
```

## Why both examples exist

The Todo app demonstrates the generic/web flow in a low-risk application. The Unity prototype demonstrates the package's strongest product-specific profile and shows how to handle artifacts that cannot honestly be claimed as created without a Unity Editor environment.

## How to read them

Start with each example's `README.md`, then read:

```text
00-source-input/user-input.md
01-stage-1-design-specification/stage-1-artifact.example.md
02-stage-2-execution-planning/stage-2-artifact.example.md
03-stage-3-fabrication/stage-3-artifact.example.md
04-stage-4-validation-packaging/stage-4-artifact.example.md
05-side-by-side-review/traceability-walkthrough.md
```

The examples are intentionally concise, but their artifact boundary markers, stable IDs, ledgers, traceability, statuses, and handoff logic follow the same conventions as full-scale package runs.
