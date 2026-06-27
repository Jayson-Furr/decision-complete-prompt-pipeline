# Public GitHub Publication Checklist

Use this checklist before pushing DecisionComplete Prompt Pipeline to a public GitHub repository.

## Repository setup

```text
[ ] Create repository named decision-complete-prompt-pipeline.
[ ] Set repository description from repository-metadata.yaml.
[ ] Add repository topics from repository-metadata.yaml.
[ ] Upload or commit the package contents at repository root.
[ ] Confirm VERSION is 1.0.0.
[ ] Confirm LICENSE is acceptable for the intended public release.
[ ] Replace placeholder owner values in CITATION.cff and .github/CODEOWNERS.
```

## Validation

```text
[ ] Run python tools/run-all-checks.py.
[ ] Run python tools/build-manifest.py.
[ ] Run python tools/build-release-manifest.py.
[ ] Confirm manifests/validation-report.json reports passed.
[ ] Confirm package-manifest.generated.json is current.
[ ] Confirm no generated manifest diff remains before publishing.
```

## Documentation

```text
[ ] Review README.md.
[ ] Review RELEASE.md.
[ ] Review ROADMAP.md.
[ ] Review docs/Quick-Start.md.
[ ] Review docs/GitHub-Publishing-Checklist.md.
[ ] Review SECURITY.md.
[ ] Review CONTRIBUTING.md.
[ ] Review CODE_OF_CONDUCT.md.
```

## Safety review

```text
[ ] Confirm no credentials or secrets are included.
[ ] Confirm examples do not contain private data.
[ ] Confirm no unsupported approval, certification, release, deployment, or rights-clearance claims are made.
[ ] Confirm high-stakes handling is documented as review-gated or authorization-gated.
```

## Release

```text
[ ] Commit files.
[ ] Push to GitHub.
[ ] Confirm GitHub Actions validation passes.
[ ] Create tag v1.0.0.
[ ] Create GitHub release titled DecisionComplete Prompt Pipeline v1.0.0.
[ ] Use RELEASE.md as the release body or link to it.
```


Repository URL: `https://github.com/Jayson-Furr/decision-complete-prompt-pipeline`
