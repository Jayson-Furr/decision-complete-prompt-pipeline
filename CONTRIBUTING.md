# Contributing

Thank you for considering a contribution to `decision-complete-prompt-pipeline`.

This repository is a prompt-package repository. Contributions should preserve the pipeline’s operating model:

```text
Stage 1 controls design.
Stage 2 controls execution planning.
Stage 3 controls fabricated outputs.
Stage 4 controls validation, repair classification, packaging, and final handoff.
```

## Contribution types

Useful contributions include:

- clearer prompt wording;
- additional product-type configuration profiles;
- schema improvements;
- validation scripts;
- examples;
- documentation corrections;
- controlled vocabulary refinements;
- traceability or decision-ledger improvements.

## Requirements for pull requests

A contribution should:

1. Preserve stage authority.
2. Preserve stable ID conventions.
3. Preserve artifact boundary markers.
4. Avoid removing required completion gates.
5. Avoid weakening high-stakes logging, review gates, placeholder handling, or safety rules.
6. Avoid adding claims of compliance, certification, approval, deployment, or legal status.
7. Update documentation when changing file names, schemas, prompt modes, or configuration values.

## Style

Use Markdown for human-readable documentation, YAML for configuration and handoff packets, JSON for manifests and registries, and CSV for ledgers and matrices.

Use controlled vocabulary values from `shared/Shared-Controlled-Vocabularies.md` once that file is populated.

## Reporting issues

When opening an issue, include:

- the affected file;
- the observed problem;
- the expected behavior;
- whether the issue affects safety, traceability, prompt output, configuration, or documentation.
