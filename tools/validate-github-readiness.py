#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
required = [
    'README.md','LICENSE','CHANGELOG.md','CONTRIBUTING.md','CODE_OF_CONDUCT.md','SECURITY.md','SUPPORT.md','RELEASE.md','ROADMAP.md','PUBLICATION-CHECKLIST.md','CITATION.cff',
    '.github/workflows/validate.yml','.github/PULL_REQUEST_TEMPLATE.md','.github/ISSUE_TEMPLATE/bug_report.md','.github/ISSUE_TEMPLATE/feature_request.md','docs/Public-Repository-Setup.md','docs/GitHub-Repository-Administration.md','docs/Final-Publication-Cut.md','GOVERNANCE.md','MAINTAINERS.md','ADOPTERS.md'
]
errors = [f'Missing file: {r}' for r in required if not (ROOT / r).is_file()]
github_entries = {p.name for p in (ROOT / '.github').iterdir()} if (ROOT / '.github').is_dir() else set()
if 'pull_request_template.md' in github_entries:
    errors.append('Duplicate lowercase .github/pull_request_template.md should not exist; use .github/PULL_REQUEST_TEMPLATE.md')
metadata = (ROOT / 'repository-metadata.yaml').read_text(encoding='utf-8') if (ROOT / 'repository-metadata.yaml').exists() else ''
for token in ['Jayson-Furr/decision-complete-prompt-pipeline','https://github.com/Jayson-Furr/decision-complete-prompt-pipeline','DecisionComplete Prompt Pipeline','1.0.0']:
    if token not in metadata:
        errors.append(f'Metadata missing {token!r}')
codeowners = (ROOT / '.github/CODEOWNERS').read_text(encoding='utf-8') if (ROOT / '.github/CODEOWNERS').exists() else ''
if '@Jayson-Furr' not in codeowners:
    errors.append('CODEOWNERS does not reference @Jayson-Furr')
if errors:
    print('GitHub readiness validation failed:')
    for error in errors:
        print('-', error)
    sys.exit(1)
print(f'GitHub readiness validation passed. Checked {len(required)} required files and owner metadata.')
