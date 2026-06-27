# Repository Launch Guide

This guide describes how to publish DecisionComplete Prompt Pipeline as a public GitHub repository.

## Recommended Repository Settings

| Setting | Recommended Value |
|---|---|
| Repository name | `decision-complete-prompt-pipeline` |
| Visibility | Public |
| Description | A four-stage prompt pipeline that transforms rough digital-product input into decision-complete specifications, execution-ready fabrication plans, fabricated deliverables, and validation-complete final handoff packages. |
| Topics | prompt-engineering, ai-agents, software-design, documentation, validation, traceability |
| License | MIT |
| Default branch | main |

## Initial Commit

```bash
git init
git add .
git commit -m "Release v1.0.0"
git branch -M main
git remote add origin git@github.com:Jayson-Furr/decision-complete-prompt-pipeline.git
git push -u origin main
```

## First Release

Create a GitHub release:

```text
Tag: v1.0.0
Title: DecisionComplete Prompt Pipeline v1.0.0
```

Use `RELEASE.md` or `docs/Public-Repository-Release-Notes.md` as the release body.

## After Publication

Run GitHub Actions validation or run locally:

```bash
python tools/run-all-checks.py
```

## Batch 12 Launch Note

Before publishing, review `docs/Validation-Scope-and-Guarantees.md` so public users understand that the included validation suite checks the repository package itself and does not certify downstream generated products.
