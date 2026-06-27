# Shared Definitions

## Purpose

This file defines shared terminology used across DecisionComplete Prompt Pipeline.

## Stage authority baseline

```text
Stage 1 controls design.
Stage 2 controls execution planning.
Stage 3 controls fabricated outputs.
Stage 4 controls validation, repair classification, packaging, and final handoff.
```

## 1. Pipeline

A structured four-stage prompt workflow that transforms rough user input into a validated final handoff package.

## 2. Stage

A discrete pipeline phase with a responsibility, authority boundary, input artifact, and output artifact.

## 3. Stage 1

The design specification stage; it decides product design and produces the decision-complete design suite.

## 4. Stage 2

The execution-planning stage; it converts the locked Stage 1 design into an execution-ready fabrication package.

## 5. Stage 3

The fabrication stage; it executes locked Stage 2 work packages and records fabricated outputs.

## 6. Stage 4

The validation, repair, packaging, and handoff stage; it prepares the final validation-complete package.

## 7. Artifact

A bounded stage output intended as input for the next stage or final handoff.

## 8. Document Suite

A human-readable, tree-structured, internally linked set of documents inside a stage artifact.

## 9. Human-Readable First

The rule that the primary artifact must be understandable without parsing companion data.

## 10. Machine-Readable Companion Data

Structured YAML, JSON, CSV, or similar data that mirrors the human-readable suite.

## 11. Prompt Mode

A stage-specific operating mode controlling interview threshold and decision logging level.

## 12. Low-Stakes Decision

A routine reversible decision unlikely to affect scope, safety, legality, privacy, rights, release status, or downstream execution materially.

## 13. Medium-Stakes Decision

A decision affecting usefulness, scope, quality, maintainability, implementation complexity, user experience, validation depth, or handoff quality.

## 14. High-Stakes Decision

A decision involving safety, security, privacy, rights, legal status, financial consequences, medical claims, regulated content, credentials, deployment, public release, destructive actions, or professional review.

## 15. Decision-Complete

A Stage 1 state where every meaningful downstream-relevant design decision has final resolution or controlled handling.

## 16. Execution-Ready

A Stage 2 state where work packages, dependencies, expected artifacts, prompts, briefs, QA items, and handoff instructions are sufficient for Stage 3.

## 17. Fabrication-Complete

A Stage 3 state where every Stage 2 work package has been fabricated, partially fabricated, blocked, review-gated, placeholder-complete, external-tool-required, or marked not applicable.

## 18. Validation-Complete

A Stage 4 state where every Stage 3 artifact has been validated, repaired where permitted, classified, included, excluded, blocked, review-gated, externally required, or marked not applicable.

## 19. Canonical Decision State Register

A stage-specific register that records final resolved state for all important decisions regardless of logging threshold.

## 20. Standardized Decision Ledger

A stage-specific audit table that records how decisions were made according to the active logging threshold.

## 21. Placeholder

A controlled token used when information is missing, unsafe to fabricate, or unavailable.

## 22. Placeholder-Complete

A status meaning missing information has been converted into controlled placeholder handling with downstream instructions.

## 23. Review-Gated

A status meaning user, professional, external, or authorized review is required before finalization or release.

## 24. Repair-Gated

A Stage 4 status meaning a repair is identified but cannot be applied automatically without review or authorization.

## 25. Blocked

A status meaning an item cannot proceed until a blocking issue is resolved.

## 26. External-Tool-Required

A status meaning the requested output requires a tool or environment not available in the current stage.

## 27. External Validation Required

A status meaning validation must occur outside the current AI environment.

## 28. Source Authority

The upstream source that authorizes a decision, requirement, artifact, validation, repair, or handoff item.

## 29. Traceability

The ability to follow a downstream item back to the upstream source that authorized it.

## 30. Hidden Decision

A decision downstream users would have to infer because it was not explicitly resolved, logged, summarized, placeholder-complete, review-gated, blocked, excluded, deferred, or marked not applicable.

## 31. Work Package

A Stage 2 execution unit that tells Stage 3 exactly what to fabricate.

## 32. Fabrication Result Packet

A Stage 3 packet recording the outcome of executing a Stage 2 work package.

## 33. Final Artifact

A Stage 4 artifact included, excluded, blocked, review-gated, or otherwise classified in final handoff.

## 34. Release Authorization

Explicit user authorization to release, deploy, publish, submit, or make a product public or operational.

## 35. No Unauthorized Side Effects

A pipeline-wide rule prohibiting effects on external systems, accounts, data, credentials, production environments, or public availability without explicit authorization.

## 36. No Unsupported Fact Fabrication

A rule prohibiting invention of facts that require verification.


For fixed allowed values, see `Shared-Controlled-Vocabularies.md`.
