# Final Release Checklist

Use this checklist before publishing `decision-complete-prompt-pipeline` to GitHub.

## Repository Identity

| Check | Status |
|---|---|
| Repository name is `decision-complete-prompt-pipeline` | Complete |
| Project name is `DecisionComplete Prompt Pipeline` | Complete |
| Version is `1.0.0` | Complete |
| Repository description is present | Complete |
| License file is present | Complete |

## Required Content

| Area | Status |
|---|---|
| Root README | Complete |
| Pipeline overview | Complete |
| Pipeline controller prompt | Complete |
| Configuration guide | Complete |
| Global configuration | Complete |
| Shared standards | Complete |
| Stage 1 prompt library | Complete |
| Stage 2 prompt library | Complete |
| Stage 3 prompt library | Complete |
| Stage 4 prompt library | Complete |
| Configuration examples | Complete |
| Schemas | Complete |
| Example scenario packets | Complete |
| Validation tools | Complete |
| Manifests | Complete |
| GitHub templates | Complete |

## Validation

Run:

```bash
python tools/run-all-checks.py
python tools/build-manifest.py
python tools/build-release-manifest.py
```

Expected result: all checks pass.

## Manual Publishing Steps

1. Create a new GitHub repository named `decision-complete-prompt-pipeline`.
2. Copy the contents of this package directory into the repository root.
3. Review `LICENSE`, `.github/CODEOWNERS`, and issue template contact links.
4. Commit with a message such as `Release v1.0.0`.
5. Create a GitHub release named `v1.0.0`.
6. Attach the ZIP archive if desired.

## Batch 13 Final Publication Recut Validation

Batch 13 adds `tools/validate-final-publication-recut.py`, which checks final v1.0.0 publication metadata, repository ownership, final recut documentation, validation-scope wording, complete miniature example availability, and absence of public-facing sandbox path or owner-placeholder leakage.
