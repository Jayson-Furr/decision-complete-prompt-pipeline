# Complete Miniature Runs

This document introduces the complete miniature examples included with DecisionComplete Prompt Pipeline.

The examples are intentionally small. Their purpose is not to showcase product complexity. Their purpose is to show what the four-stage artifact chain looks like when populated end to end.

## Included miniature runs

| Example | Product Type | Purpose | Final Handoff Shape |
|---|---|---|---|
| Todo Web App | Web application | Demonstrates a complete local-only web app pipeline with fabricated React/TypeScript files. | Ready with Warnings because build and browser testing are external validation steps. |
| Unity Button Click Prototype | Unity game | Demonstrates a tiny Unity UI Toolkit prototype with C# and UI files plus Unity Editor validation requirements. | External Validation Required because Unity Editor import, compilation, Play Mode testing, and build were not run. |

## Why these examples exist

The repository contains detailed prompts and configuration profiles. These examples show how those rules become concrete outputs:

```text
Stage 1 artifact → Stage 2 artifact → Stage 3 artifact → Stage 4 artifact
```

They also demonstrate:

```text
- artifact boundary markers;
- decision ledgers;
- traceability matrices;
- fabricated file manifests;
- external validation classification;
- final handoff packet shape;
- Ready with Warnings versus External Validation Required.
```

## Example locations

```text
examples/minimal-complete-run/todo-web-app/
examples/minimal-complete-run/unity-button-click-prototype/
```

Each example contains:

```text
00-source-input/
01-stage-1-design-specification/
02-stage-2-execution-planning/
03-stage-3-fabrication/
04-stage-4-validation-packaging/
05-side-by-side-review/
```

## Validation scope

The examples are documentation fixtures. They are designed to illustrate the repository format and are validated for structure, boundary markers, decision ledger headers, and traceability links. They are not claims that a production application has been built, deployed, security-certified, rights-cleared, or externally validated.
