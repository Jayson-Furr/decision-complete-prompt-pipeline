# Stage 4 Shared Rules

These shared rules apply to every Stage 4 prompt in **DecisionComplete Prompt Pipeline** version `1.0.0`.

## Authority

```text
Stage 1 controls design.
Stage 2 controls execution planning.
Stage 3 controls fabricated outputs.
Stage 4 controls validation, repair classification, packaging, and final handoff.
```

Stage 4 must preserve the Stage 1 design lock, Stage 2 execution lock, and Stage 3 fabrication record.

## Required behaviors

```text
- Inventory the Stage 3 artifact.
- Validate every fabricated artifact that can be validated.
- Mark unrun checks as Not Run or External Validation Required.
- Perform only allowed repairs.
- Log every repair.
- Classify every Stage 3 artifact in the final artifact manifest.
- Preserve placeholders and review-gated items.
- Identify external-tool-required and external-validation-required items.
- Produce final QA, traceability, unresolved item, readiness, and approval reports.
- Maintain the Canonical Finalization Decision State Register.
- Maintain the Standardized Finalization Decision Ledger according to prompt mode.
- Complete the Hidden Finalization Decision Scan.
- Produce the final handoff packet.
```

## Prohibited behaviors

```text
- Do not redesign the product.
- Do not re-plan execution.
- Do not silently alter Stage 3 fabricated outputs.
- Do not change acceptance criteria.
- Do not replace placeholders with guesses.
- Do not resolve review-gated items without authorization.
- Do not claim tests, builds, imports, approvals, certifications, deployment, or release occurred unless actually performed and authorized.
- Do not deploy, publish, submit, use credentials, or perform destructive operations.
```

## Completion standard

Stage 4 is complete when every Stage 3 artifact has been validated, repaired where permitted, classified, included, excluded, blocked, review-gated, external-tool-required, external-validation-required, placeholder-complete, or marked not applicable with full traceability and final handoff status.
