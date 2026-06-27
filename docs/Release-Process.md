# Release Process

1. Confirm `VERSION` is correct.
2. Run `python tools/run-all-checks.py`.
3. Run `python tools/build-manifest.py`.
4. Run `python tools/build-release-manifest.py`.
5. Review `CHANGELOG.md`, `README.md`, and `docs/Public-Repository-Release-Notes.md`.
6. Commit generated manifests.
7. Tag the release as `v1.0.0` for the first public release.

## Batch 13 Final Publication Recut Validation

Batch 13 adds `tools/validate-final-publication-recut.py`, which checks final v1.0.0 publication metadata, repository ownership, final recut documentation, validation-scope wording, complete miniature example availability, and absence of public-facing sandbox path or owner-placeholder leakage.
