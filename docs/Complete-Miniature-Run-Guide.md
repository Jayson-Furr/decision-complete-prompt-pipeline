# Complete Miniature Run Guide

## Purpose

This guide explains the complete miniature examples in `examples/minimal-complete-run/`.

These examples are different from the scenario packets elsewhere in `examples/`. Scenario packets show how to start a pipeline run. Complete miniature runs show what the completed Stage 1 through Stage 4 artifact chain can look like.

## Included miniature runs

| Example | Product Type | Final Handoff Status | Why It Exists |
|---|---|---|---|
| `examples/minimal-complete-run/todo-web-app/` | Web application | Ready with Warnings | Demonstrates a tiny browser app with fabricated text files and external build validation warning. |
| `examples/minimal-complete-run/unity-button-click-prototype/` | Unity game prototype | External Validation Required | Demonstrates Unity text artifacts, external-tool scene creation, and honest Unity Editor validation limits. |

## What each miniature run contains

```text
00-source-input/
  user-input.md
  pipeline.configuration.yaml
01-stage-1-design-specification/
  stage-1-artifact.example.md
  stage-1-decision-ledger.example.csv
  stage-1-traceability-matrix.example.csv
02-stage-2-execution-planning/
  stage-2-artifact.example.md
  stage-2-work-package-registry.example.json
  stage-2-decision-ledger.example.csv
  stage-2-traceability-matrix.example.csv
03-stage-3-fabrication/
  stage-3-artifact.example.md
  fabricated-files/
  stage-3-fabricated-artifact-manifest.example.json
  stage-3-decision-ledger.example.csv
04-stage-4-validation-packaging/
  stage-4-artifact.example.md
  final-artifact-manifest.example.json
  validation-report.example.csv
  repair-log.example.csv
  final-handoff-packet.example.yaml
05-side-by-side-review/
  decision-ledger-comparison-notes.md
  traceability-walkthrough.md
```

## How to inspect one example

1. Read `00-source-input/user-input.md`.
2. Open the Stage 1 artifact and confirm it defines the design authority.
3. Open the Stage 2 artifact and confirm it decomposes the design into work packages.
4. Open the Stage 3 artifact and inspect the fabricated files.
5. Open the Stage 4 artifact and confirm final validation classifications.
6. Review the side-by-side notes and traceability walkthrough.

## Why the examples are intentionally small

The goal is not to ship a production Todo app or production Unity project. The goal is to show the artifact chain clearly:

```text
Source input
→ Stage 1 design authority
→ Stage 2 execution plan
→ Stage 3 fabricated files / records
→ Stage 4 validation and final handoff
```

The examples avoid accounts, payments, analytics, production deployment, live services, and real credentials.

## Validation honesty

The Todo web app example does not claim that `npm install`, `npm run build`, or browser runtime testing occurred.

The Unity example does not claim Unity Editor import, C# compilation, Edit Mode tests, Play Mode tests, scene creation, or player build validation occurred.

Those checks are explicitly marked as warnings, external-tool-required items, or external-validation-required items.
