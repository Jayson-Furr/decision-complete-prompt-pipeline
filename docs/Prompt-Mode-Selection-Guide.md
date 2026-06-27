# Prompt Mode Selection Guide

Each stage has four prompt modes. The mode controls how often the AI pauses to interview the user before deciding.

## Mode summary

| Mode | Interview Threshold | Ledger Detail | Recommended Use |
|---|---|---|---|
| No Questions | None | Low, medium, and high decisions line-item logged | Fast drafts and prototype runs. |
| Low-Stakes Interview | Low and above | Low, medium, and high decisions line-item logged | Maximum control. |
| Medium-Stakes Interview | Medium and above | Medium/high line-item logged; low summarized | Default for most work. |
| High-Stakes Interview | High only | High line-item logged; low/medium summarized | Fast runs with sensitive-topic interruptions. |

## Use No Questions mode when

```text
- you want the fastest possible pipeline run;
- you are comfortable with AI-selected defaults;
- you want a first-pass artifact;
- you are prototyping;
- you want everything safe but not repeatedly interviewed.
```

No Questions mode still preserves placeholders, review gates, blockers, external-tool-required items, and high-stakes safety boundaries. It does not authorize deployment, public release, credential use, or destructive operations.

## Use Low-Stakes Interview mode when

```text
- every detail matters;
- the project is client-facing;
- the user wants to compare multiple fabrications precisely;
- small naming, structure, or formatting choices matter;
- you want the most comprehensive decision ledger.
```

This mode is the most controlled and the slowest.

## Use Medium-Stakes Interview mode when

```text
- you want the recommended default;
- routine decisions can be safely handled by AI;
- product, execution, fabrication, or validation decisions still matter;
- you want a good balance of speed, quality, and auditability.
```

This is the best starting point for most repository users.

## Use High-Stakes Interview mode when

```text
- you want speed;
- you only want to be interrupted for legal, privacy, security, release, rights, deployment, credential, safety, or regulated issues;
- low- and medium-stakes decisions can be handled automatically.
```

This mode is fast but still designed to avoid hidden high-stakes decisions.

## Cross-stage examples

| Scenario | Recommended Mode |
|---|---|
| Solo prototype for a game jam | No Questions or High-Stakes Interview |
| New commercial game concept | Medium-Stakes Interview |
| Client UX/product specification | Low-Stakes or Medium-Stakes Interview |
| Web app with accounts and payments | Medium-Stakes or High-Stakes Interview |
| Library intended for public package registry | Medium-Stakes Interview |
| Final validation before public release | High-Stakes or Low-Stakes Finalization Interview |

## Decision escalation rule

A lower-stakes decision must be elevated when it materially affects a higher-stakes outcome.

Example:

```text
A file naming decision is usually low-stakes.
If it changes a deployment path or credential location, it becomes high-stakes and must be line-item logged.
```
