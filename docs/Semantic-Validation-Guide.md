
# Semantic Validation Guide

DecisionComplete Prompt Pipeline includes validation tools, but their guarantee is deliberately narrow and honest.

The validation suite performs **repository structure and consistency validation**. It does not prove deep semantic correctness of generated product artifacts.

## What repository validation checks

```text
- Required public repository files exist.
- Sixteen core prompt files exist.
- Prompt files contain the expected stage, prompt-mode, artifact-boundary, decision-ledger, hidden-scan, and completion-gate language.
- Artifact boundary markers are canonical.
- Configuration examples parse as YAML.
- Product-specific profiles declare inheritance and stage metadata.
- Web application and shared library / SDK profiles contain product-specific depth sections.
- Shared vocabulary and schema guide files are present.
- Complete miniature examples contain stage artifacts, fabricated files, decision ledgers, and traceability matrices.
- Markdown links resolve for repository-internal links where feasible.
- Release metadata is complete for v1.0.0.
```

## What repository validation does not prove

```text
- It does not prove that an AI-generated Stage 1 design is the best design.
- It does not prove that an AI-generated Stage 2 plan is optimal.
- It does not prove that Stage 3 fabricated code compiles or runs unless actual build/test evidence is provided.
- It does not prove that Stage 4 final artifacts are legally approved, rights-cleared, secure, compliant, production-ready, deployed, or publicly released.
- It does not replace user review, professional review, external validation, or authorized execution.
```

## How to describe the validation suite publicly

Preferred wording:

```text
The validation tools check repository structure and consistency. They do not constitute deep semantic validation of generated product artifacts, legal approval, security certification, compliance approval, production readiness, deployment, or public release.
```

## Future semantic validation opportunities

Possible future improvements include:

```text
- formal JSON Schema validation for configuration files;
- AST-level checks for prompt required sections;
- generated artifact fixture validation;
- richer cross-reference graph validation;
- schema-to-example conformance tests;
- optional linting for generated code examples;
- snapshot tests for complete miniature runs.
```

<!-- batch-12-validation-scope -->

## Batch 12 clarification

This repository does not claim deep semantic validation of generated downstream artifacts. The phrase used for this repository's validation suite is:

```text
Repository structure and consistency validation
```

The semantic consistency checks added in Batch 12 verify scoped claims, profile-depth coverage, complete example chains, and decision-ledger headers. They do **not** prove that generated designs, plans, code, assets, tests, packages, releases, or deployments are correct or approved.


Note: downstream artifacts that cannot be validated in the current environment must be marked `External Validation Required`; this repository validation suite does not remove that requirement.

## External Validation Required

Repository validation may mark downstream product checks as external validation required. This means the repository can document the needed check, but the external tool, compiler, runtime, legal reviewer, security reviewer, privacy reviewer, app store, or production environment must perform that validation before any release claim is made.


## Validation guarantee scope

The validation tools perform repository structure and consistency validation; does not prove deep semantic correctness, legal approval, rights clearance, privacy compliance, security certification, deployment success, app store approval, compliance approval, production readiness, or public release success.
