# Tools

This directory contains lightweight repository tooling for **DecisionComplete Prompt Pipeline**.

The tools are intentionally standard-library-only except for optional YAML parsing in `validate-configurations.py`, which uses PyYAML when available in the execution environment.

## Run all checks

```bash
python -m pip install -r requirements.txt
python tools/run-all-checks.py
```

## Rebuild manifests

```bash
python tools/build-manifest.py
python tools/build-release-manifest.py
```

Generated manifests are deterministic and exclude generated manifest outputs from their input sets to avoid self-referential CI diffs.

## Tool inventory

```text
_deterministic.py
build-manifest.py
build-release-manifest.py
run-all-checks.py
validate-artifact-boundaries.py
validate-configurations.py
validate-controlled-vocabularies.py
validate-decision-ledgers.py
validate-examples.py
validate-github-readiness.py
validate-machine-readable-companions.py
validate-markdown-links.py
validate-package-structure.py
validate-prompt-files.py
validate-publication-polish.py
validate-release-readiness.py
validate-schemas.py
```

## Validation scope

These tools validate repository structure, prompt presence, boundary markers, configuration parseability, schema-guide alignment, examples, release readiness, and public publication polish. They do not replace human review of project-specific outputs, high-stakes claims, rights, privacy, security, deployment, or professional-review items.

## Batch 12 Validation-Scope Tooling

`validate-validation-scope.py` checks that public validation claims are accurately scoped as repository structure and consistency validation. It also checks that the repository does not imply legal, security, privacy, deployment, or downstream artifact correctness guarantees.


## Batch 12 validators

Batch 12 adds validators that improve public repository credibility without overclaiming semantic guarantees:

```text
validate-profile-depth.py
validate-validation-scope.py
validate-semantic-consistency.py
```

These validators check profile-depth balance, validation-scope wording, and stage/mode/authority consistency across the package.

<!-- batch-12-tools -->

## Batch 12 validators

```text
validate-profile-depth.py
validate-validation-scope.py
validate-semantic-consistency.py
```

These checks strengthen the repository's structure and consistency validation. They do not prove downstream generated artifact correctness.

## Batch 13 Final Publication Recut Validation

Batch 13 adds `tools/validate-final-publication-recut.py`, which checks final v1.0.0 publication metadata, repository ownership, final recut documentation, validation-scope wording, complete miniature example availability, and absence of public-facing sandbox path or owner-placeholder leakage.
