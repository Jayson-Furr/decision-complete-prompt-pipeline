# Validation Tools

Run the complete repository validation suite:

```bash
python -m pip install -r requirements.txt
python tools/run-all-checks.py
```

Rebuild generated manifests:

```bash
python tools/build-manifest.py
python tools/build-release-manifest.py
```

## Generated outputs

```text
package-manifest.generated.json
manifests/validation-report.json
manifests/public-repository-file-index.csv
manifests/release-artifact-manifest.json
manifests/repository-tree.txt
manifests/final-package-inventory.json
manifests/checksums.sha256.json
manifests/checksums.sha256.txt
```

The manifest builders are deterministic. They exclude generated manifest outputs from their input sets so that GitHub Actions can rebuild manifests and run `git diff --exit-code` without timestamp or self-reference churn.

## Validation commands

```text
validate-package-structure.py
validate-prompt-files.py
validate-artifact-boundaries.py
validate-configurations.py
validate-controlled-vocabularies.py
validate-schemas.py
validate-examples.py
validate-decision-ledgers.py
validate-machine-readable-companions.py
validate-markdown-links.py
validate-github-readiness.py
validate-publication-polish.py
validate-release-readiness.py
```

## What the tools validate

```text
- Required public repository files exist.
- Sixteen prompt files exist and contain expected stage content.
- Artifact boundary markers are present and exact.
- Configuration examples parse and align with stage schema guides.
- Controlled vocabulary files and schema-guide files exist.
- Example scenarios contain expected runbooks, skeletons, ledgers, and traceability samples.
- Markdown links resolve where feasible.
- Owner-specific GitHub metadata is applied.
- Public-facing sandbox and placeholder strings are absent.
- Release readiness files are present for v1.0.0.
```

## What still requires review

The validation tools do not prove that a future generated product artifact is correct for a specific project. Human or professional review may still be required for legal, financial, medical, safety, privacy, security, rights, licensing, deployment, release, and regulated-domain issues.

## Validation Scope Statement

The validation tools are repository QA tools. They validate structure, consistency, public metadata, profiles, examples, and release hygiene. They do not certify downstream generated artifacts or external product readiness.

The aggregate validation report now records:

```json
{
  "validation_scope": "repository_structure_and_consistency",
  "semantic_validation_depth": "limited"
}
```

See [Validation Scope and Guarantees](Validation-Scope-and-Guarantees.md) for the full distinction.


## Repository Structure and Consistency Validation

The validation suite performs repository structure and consistency validation. It checks the public repository package, not the semantic correctness or external approval status of downstream generated products.


## Batch 12 validation scope clarification

The validation tooling performs **repository structure and consistency validation**. It checks package completeness, prompt file consistency, artifact boundary markers, configuration/profile structure, example completeness, Markdown links, GitHub readiness, and release metadata.

It does not prove deep semantic correctness of downstream generated artifacts, legal approval, security certification, compliance approval, production readiness, deployment, or public release.

Batch 12 adds validators for profile depth and validation-scope wording:

```text
tools/validate-profile-depth.py
tools/validate-validation-scope.py
tools/validate-semantic-consistency.py
```

<!-- batch-12-validation-scope -->

## Validation guarantee boundary

The validation tools perform **repository structure and consistency validation**. They do not prove prompt correctness, downstream artifact correctness, legal approval, security certification, compliance readiness, production readiness, deployment success, or public release authorization.

For downstream artifacts, use the pipeline statuses `External Validation Required`, `Review-Gated`, `Blocked`, and `Ready with Warnings` honestly. Passing this repository's validation suite does not remove the need for target-environment validation.

Additional Batch 12 validators:

```text
tools/validate-profile-depth.py
tools/validate-validation-scope.py
tools/validate-semantic-consistency.py
```


## Validation guarantee scope

The validation tools perform repository structure and consistency validation; does not prove deep semantic correctness, legal approval, rights clearance, privacy compliance, security certification, deployment success, app store approval, compliance approval, production readiness, or public release success.

## Batch 13 Final Publication Recut Validation

Batch 13 adds `tools/validate-final-publication-recut.py`, which checks final v1.0.0 publication metadata, repository ownership, final recut documentation, validation-scope wording, complete miniature example availability, and absence of public-facing sandbox path or owner-placeholder leakage.
