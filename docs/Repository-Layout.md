# Repository Layout

This repository is organized for public GitHub distribution and direct prompt-package use.

```text
decision-complete-prompt-pipeline/
  README.md
  LICENSE
  CHANGELOG.md
  CONTRIBUTING.md
  CODE_OF_CONDUCT.md
  SECURITY.md
  NOTICE.md
  MANIFEST.md
  VERSION
  repository-metadata.yaml
  Pipeline-Overview.md
  Pipeline-Controller-Prompt.md
  Pipeline-Configuration-Guide.md
  pipeline.configuration.yaml
  docs/
  shared/
  stage-1-design-specification/
  stage-2-execution-planning/
  stage-3-fabrication/
  stage-4-validation-packaging/
  configuration-examples/
  schemas/
  examples/
  tools/
  manifests/
```

## Root files

| File | Purpose |
|---|---|
| `README.md` | Public repository landing page. |
| `LICENSE` | MIT license by default. Replace if desired before publication. |
| `CHANGELOG.md` | Version 1.0.0 release history. |
| `CONTRIBUTING.md` | Contribution workflow. |
| `CODE_OF_CONDUCT.md` | Contributor conduct expectations. |
| `SECURITY.md` | Security reporting and high-stakes safety notes. |
| `Pipeline-Overview.md` | Full conceptual explanation of the four-stage pipeline. |
| `Pipeline-Controller-Prompt.md` | Prompt for selecting the next pipeline stage and mode. |
| `Pipeline-Configuration-Guide.md` | Detailed guide for configuration files. |
| `pipeline.configuration.yaml` | Global default configuration. |
| `MANIFEST.md` | Human-readable repository manifest. |
| `package-manifest.generated.json` | Generated file manifest with checksums. |

## Stage directories

Each stage directory contains:

```text
README.md
Stage-N-Overview.md
Stage-N-Shared-Rules.md
prompts/
companion-data/
```

The prompt files in `prompts/` are the main operational files.

## Shared directory

`shared/` contains the standards used by all stages:

```text
Shared-Definitions.md
Shared-Controlled-Vocabularies.md
Shared-ID-Namespace.md
Shared-Document-Header-Template.md
Shared-Artifact-Boundary-Markup.md
Shared-Configuration-Priority-Rules.md
Shared-Traceability-Rules.md
Shared-Decision-Ledger-Schema.md
Shared-Hidden-Decision-Scan-Schema.md
Shared-Machine-Readable-Companion-Rules.md
```

## Configuration examples

`configuration-examples/` contains reusable YAML profiles:

```text
stage-1-default.configuration.yaml
stage-2-default.configuration.yaml
stage-3-default.configuration.yaml
stage-4-default.configuration.yaml
stage-1-unity-game.configuration.yaml
...
```

## Examples directory

`examples/` contains practical usage scenarios:

```text
examples/unity-game/
examples/web-application/
examples/shared-library/
```

Each example includes input packets, configuration overrides, runbooks, artifact skeletons, traceability samples, and decision ledger samples.

## Tools directory

`tools/` contains helper scripts:

```text
validate-package-structure.py
build-manifest.py
```

The tools are intentionally lightweight and require only Python’s standard library.
