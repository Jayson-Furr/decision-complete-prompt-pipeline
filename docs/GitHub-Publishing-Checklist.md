# GitHub Publishing Checklist

Use this checklist before publishing `decision-complete-prompt-pipeline` as a public GitHub repository.

## Repository identity

```text
Project name: DecisionComplete Prompt Pipeline
Repository name: decision-complete-prompt-pipeline
Version: 1.0.0
```

Recommended repository description:

```text
A four-stage prompt pipeline that transforms rough digital-product input into decision-complete specifications, execution-ready fabrication plans, fabricated deliverables, and validation-complete final handoff packages.
```

## Pre-publication checks

| Check | Status |
|---|---|
| Repository name confirmed | Pending user review |
| License confirmed | Pending user review |
| `README.md` reviewed | Pending user review |
| `SECURITY.md` reviewed | Pending user review |
| No private data included | Pending user review |
| No credentials included | Pending user review |
| Prompt files present | Check with tools |
| Configuration examples present | Check with tools |
| Shared standards present | Check with tools |
| Example folders present | Check with tools |
| File manifest generated | Check with tools |
| ZIP release package created | External to repository |

## Local validation commands

From the repository root:

```bash
python tools/validate-package-structure.py
python tools/build-manifest.py
```

## Suggested Git initialization

```bash
git init
git add .
git commit -m "Release DecisionComplete Prompt Pipeline v1.0.0"
git branch -M main
git remote add origin https://github.com/<your-username>/decision-complete-prompt-pipeline.git
git push -u origin main
```

## Suggested GitHub topics

```text
prompt-engineering
ai-workflow
design-specification
software-planning
traceability
decision-ledger
product-design
game-development
software-delivery
```

## Release checklist

Create a GitHub release named:

```text
v1.0.0
```

Suggested release title:

```text
DecisionComplete Prompt Pipeline v1.0.0
```

Include:

```text
- core sixteen prompts;
- shared standards;
- configuration examples;
- schemas;
- examples and runbooks;
- validation tools;
- generated package manifest.
```

## License note

The package currently uses MIT License. Replace the license before publication if you prefer a different license. This package does not provide legal advice about which license you should use.


Repository URL: `https://github.com/Jayson-Furr/decision-complete-prompt-pipeline`
