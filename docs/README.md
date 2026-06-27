# Documentation Index

This directory contains practical operating documentation for **DecisionComplete Prompt Pipeline**.

## Recommended reading order

| Order | Document | Purpose |
|---:|---|---|
| 1 | [Quick-Start.md](Quick-Start.md) | Start a new project with the recommended default path. |
| 2 | [Usage-Guide.md](Usage-Guide.md) | Understand the full operating workflow. |
| 3 | [Prompt-Mode-Selection-Guide.md](Prompt-Mode-Selection-Guide.md) | Choose no-questions, low-, medium-, or high-stakes modes. |
| 4 | [Artifact-Handoff-Guide.md](Artifact-Handoff-Guide.md) | Copy each stage artifact into the next stage correctly. |
| 5 | [Configuration-Profile-Selection-Guide.md](Configuration-Profile-Selection-Guide.md) | Select default, Unity, web application, or shared library profiles. |
| 6 | [Decision-Ledger-Comparison-Guide.md](Decision-Ledger-Comparison-Guide.md) | Compare multiple pipeline runs side by side. |
| 7 | [Complete-Miniature-Run-Guide.md](Complete-Miniature-Run-Guide.md) | Read the complete Todo web app and Unity button-click prototype examples. |
| 8 | [Example-Scenario-Guide.md](Example-Scenario-Guide.md) | Use the scenario packet examples. |
| 9 | [Repository-Layout.md](Repository-Layout.md) | Understand the repository structure. |
| 10 | [Validation-Scope-and-Guarantees.md](Validation-Scope-and-Guarantees.md) | Understand what the validation tools do and do not guarantee. |
| 11 | [GitHub-Publishing-Checklist.md](GitHub-Publishing-Checklist.md) | Prepare the package for public GitHub publication. |
| 12 | [Troubleshooting.md](Troubleshooting.md) | Resolve common problems. |
| 13 | [FAQ.md](FAQ.md) | Quick answers to common questions. |

## Maintainer and release documentation

```text
Validation-Tools.md
Quality-Assurance-Process.md
Repository-Maintenance.md
Versioning-Policy.md
Release-Process.md
Final-Release-Checklist.md
Final-Publication-Cut.md
Final-v1.0.0-Publication-Recut.md
Post-Publish-Smoke-Test.md
Repository-Launch-Guide.md
Public-Repository-Setup.md
```

## Profile and schema documentation

```text
Profile-Family-Roadmap.md
Profile-Authoring-Guide.md
Web-Application-Profile-Deep-Dive.md
Shared-Library-SDK-Profile-Deep-Dive.md
Schema-Configuration-Alignment.md
Semantic-Validation-Guide.md
Validation-Guarantee-Matrix.md
Validator-Implementation-Notes.md
```

## Core operating rule

The pipeline is strict about stage authority:

```text
Stage 1 controls design.
Stage 2 controls execution planning.
Stage 3 controls fabricated outputs.
Stage 4 controls validation, repair classification, packaging, and final handoff.
```

When in doubt, do not silently change an upstream decision in a downstream stage. Rerun the proper upstream stage instead.

- [Final-v1.0.0-Publication-Recut.md](./Final-v1.0.0-Publication-Recut.md)

- [Post-Publish-Smoke-Test.md](./Post-Publish-Smoke-Test.md)
