# Stage 3 Shared Rules

These shared rules apply to every Stage 3 prompt in **DecisionComplete Prompt Pipeline** version `1.0.0`.

## Authority

```text
Stage 1 controls design.
Stage 2 controls execution planning.
Stage 3 controls fabricated outputs.
Stage 4 controls validation, repair classification, packaging, and final handoff.
```

Stage 3 must preserve the Stage 1 design lock and Stage 2 execution lock.

## Required behaviors

```text
- Execute every ready Stage 2 work package that can be safely executed.
- Create a Fabrication Result Packet for every Stage 2 work package.
- Provide complete text-based file contents when claiming a text file is fabricated.
- Accurately classify binary or tool-dependent assets.
- Preserve placeholders and review-gated items.
- Record defects, deviations, blockers, and external-tool-required items.
- Include preliminary validation without pretending it is final Stage 4 validation.
- Maintain the Canonical Fabrication Decision State Register.
- Maintain the Standardized Fabrication Decision Ledger according to prompt mode.
- Complete the Hidden Fabrication Decision Scan.
- Produce the Stage 4 Handoff Contract.
```

## Prohibited behaviors

```text
- Do not redesign the product.
- Do not re-plan execution.
- Do not change required outputs.
- Do not replace placeholders with guesses.
- Do not resolve review-gated items without authorization.
- Do not pretend unsupported binary assets exist.
- Do not claim tests, builds, imports, or external validations passed unless actually run.
- Do not deploy, publish, submit, use credentials, or perform destructive operations.
```

## Completion standard

Stage 3 is complete only when every Stage 2 work package has been fabricated, partially fabricated, blocked, review-gated, placeholder-complete, external-tool-required, excluded, or marked not applicable with full traceability and Stage 4 instructions.
