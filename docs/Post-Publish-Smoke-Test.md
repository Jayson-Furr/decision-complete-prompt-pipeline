# Post-Publish Smoke Test

Use this checklist after publishing `Jayson-Furr/decision-complete-prompt-pipeline` to GitHub.

## Repository page checks

```text
- Repository URL opens: https://github.com/Jayson-Furr/decision-complete-prompt-pipeline
- README renders correctly.
- License is detected by GitHub.
- GitHub Actions workflow is visible.
- Issue templates are visible.
- Pull request template is visible.
- CODEOWNERS file is present.
```

## Local clone checks

```bash
git clone https://github.com/Jayson-Furr/decision-complete-prompt-pipeline.git
cd decision-complete-prompt-pipeline
python tools/run-all-checks.py
```

Expected result:

```text
All repository structure and consistency validation checks pass.
```

## Validation boundary reminder

The smoke test confirms repository publication and repository structure and consistency validation. It does not prove deep semantic correctness, downstream generated artifact correctness, legal approval, security certification, compliance approval, production readiness, deployment success, public release success, or app store approval.
