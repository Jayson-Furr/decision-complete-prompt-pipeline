# Public Repository Setup

This guide explains how to publish the package to GitHub.

## Recommended repository settings

```text
Repository name: decision-complete-prompt-pipeline
Visibility: Public
License: MIT
Default branch: main
Issues: Enabled
Discussions: Optional
Wiki: Optional
Projects: Optional
```

## Suggested topics

```text
prompt-engineering
ai-workflows
product-design
software-planning
documentation
traceability
requirements
unity
web-application
sdk
```

## First commit sequence

```bash
git init
git add .
git commit -m "Release DecisionComplete Prompt Pipeline v1.0.0"
git branch -M main
git remote add origin git@github.com:Jayson-Furr/decision-complete-prompt-pipeline.git
git push -u origin main
```

## Tagging

```bash
git tag v1.0.0
git push origin v1.0.0
```

## After publishing

The repository owner metadata is already set to `Jayson-Furr`. Review [CITATION.cff](../CITATION.cff) only if you want to change citation authorship or release metadata.
