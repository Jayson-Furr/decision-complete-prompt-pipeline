# Runbook — Web Application Example

## Stage 1

Use:

```text
stage-1-design-specification/prompts/Stage-1-Prompt-3-Medium-Stakes-Design-Interview.md
```

Input:

```text
examples/web-application/stage-1-input.md
examples/web-application/configuration-overrides.yaml
```

## Stage 2

Use the Stage 2 Medium-Stakes prompt with the Stage 1 artifact.

Expected Stage 2 focus:

```text
- frontend work packages;
- API work packages;
- schema and data packages;
- authentication review-gated packages;
- privacy review-gated packages;
- QA and accessibility packages.
```

## Stage 3

Use the Stage 3 Medium-Stakes prompt with the Stage 2 artifact.

Expected Stage 3 focus:

```text
- text-based React, TypeScript, schema, test, and documentation files where possible;
- blocked or review-gated handling for high-stakes auth/privacy concerns;
- no production deployment.
```

## Stage 4

Use the Stage 4 Medium-Stakes prompt with the Stage 3 artifact.

Expected Stage 4 focus:

```text
- final validation;
- repair log;
- security and privacy review flags;
- deployment-not-performed statement;
- final handoff readiness.
```
