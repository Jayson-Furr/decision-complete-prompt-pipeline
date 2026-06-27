# Security Policy

## Supported version

| Version | Supported |
|---|---|
| 1.0.x | Yes |

## Reporting a vulnerability

Please report security-sensitive issues privately through the repository owner’s preferred contact method.

Do not post secrets, credentials, private data, exploit details, or sensitive production information in public issues.

## Security scope

This repository contains prompt files, configuration examples, documentation, schemas, and lightweight helper scripts. Security issues may include:

- prompt wording that encourages unsafe credential use;
- prompt wording that claims unauthorized deployment, publication, or approval;
- configuration examples that embed secrets;
- validation tools that destructively modify files;
- documentation that weakens privacy, rights, or high-stakes review handling.

## Baseline rules

The package must not encourage:

```text
- unsupported fact fabrication;
- credential exposure;
- unauthorized production deployment;
- unauthorized public release;
- unauthorized destructive operations;
- bypassing rights, security, privacy, legal, medical, financial, or regulatory review.
```
