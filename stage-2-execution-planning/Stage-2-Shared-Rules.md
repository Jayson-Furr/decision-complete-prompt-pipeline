
# Stage 2 Shared Rules

These rules apply to all Stage 2 prompt modes.

## Authority

Stage 2 controls execution planning. It must preserve Stage 1 design authority.

## Required artifact status

```text
100% Execution-Ready
Not Yet Execution-Ready
```

Execution-ready means Stage 3 can fabricate without making execution-planning decisions. It does not mean files, code, assets, builds, or deployments exist.

## Required artifact boundary

```text
<<<BEGIN STAGE 2 ARTIFACT: 100% EXECUTION-READY FABRICATION PACKAGE SUITE>>>
...
<<<END STAGE 2 ARTIFACT>>>
```

## Required ledgers and registers

```text
Canonical Execution Decision State Register
Standardized Execution Decision Ledger
Below-Threshold Execution Decision Summary, where applicable
Execution Assumptions, Constraints, and Blocked Items
Placeholder and Review-Gated Item Handling
Hidden Execution Decision Scan
```

## Non-negotiable standards

```text
Do not redesign Stage 1.
Every work package needs source authority.
Every ready work package needs required outputs.
Every ready work package needs positive and negative execution prompts.
Every ready work package needs acceptance and rejection criteria.
No Stage 3 executor should need to make an execution-planning decision.
```
