# Validation Scope and Guarantees

## Purpose

This document defines what the repository validation tools do and do not guarantee.

The validation suite is intentionally conservative. It validates repository structure, naming, required files, prompt/package consistency, configuration/profile consistency, schema-guide alignment, examples, Markdown links, and release metadata.

It does **not** prove that any downstream generated product, game, app, service, library, artifact, deployment, legal claim, security property, or compliance claim is correct or approved.

## Correct validation claim

Use this phrase when describing the tools:

```text
Repository structure and consistency validation
```

Avoid overbroad claims such as:

```text
Deep semantic validation
Proof of prompt correctness
Proof of generated artifact correctness
Proof of legal approval
Proof of security certification
Proof of compliance readiness
Proof of production readiness
```

## What the tools validate

The repository tools validate:

```text
- required repository files;
- public GitHub metadata;
- prompt file inventory;
- artifact boundary marker strings;
- configuration profile structure;
- profile family depth coverage;
- schema-guide alignment with configuration examples;
- controlled vocabulary presence;
- example directory structure;
- complete miniature run structure;
- decision ledger CSV headers;
- machine-readable companion conventions;
- Markdown relative links;
- release-readiness and publication-polish metadata;
- deterministic manifest generation.
```

## What the tools do not validate

The repository tools do not validate:

```text
- whether an AI-generated design is objectively good;
- whether generated code compiles in every target environment;
- whether a Unity project imports successfully unless Unity validation evidence is supplied;
- whether a web app builds unless build evidence is supplied;
- whether a library package publishes successfully unless publish evidence is supplied;
- whether generated artifacts are secure;
- whether generated artifacts are legally compliant;
- whether third-party rights are cleared;
- whether a deployment occurred;
- whether public release is authorized;
- whether medical, legal, financial, safety, or regulatory claims are professionally approved.
```

## Validation result interpretation

When the repository validation suite passes, it means:

```text
The repository package is structurally coherent and internally consistent according to the v1.0.0 validation scripts.
```

It does not mean:

```text
Any downstream product created with the prompts is defect-free, production-ready, legally approved, secure, or deployable.
```

## External validation requirements

Downstream artifacts may still require:

```text
- compiler validation;
- engine import validation;
- unit/integration test execution;
- accessibility testing;
- security review;
- privacy review;
- rights/licensing review;
- legal/professional review;
- platform/store review;
- deployment authorization;
- production environment validation.
```

The pipeline’s Stage 4 prompts explicitly preserve these statuses through `External Validation Required`, `Review-Gated`, `Blocked`, and approval-packet records.

## Recommended language for README and release notes

Use:

```text
The included tools perform repository structure and consistency validation. They check the package layout, prompt inventory, artifact boundary markers, configuration profiles, schema guides, example structure, decision ledger headers, machine-readable companion conventions, Markdown links, and release metadata. They do not provide semantic correctness guarantees for downstream generated artifacts.
```

## Maintainer checklist

Before claiming validation passed, run:

```bash
python tools/run-all-checks.py
python tools/build-manifest.py
python tools/build-release-manifest.py
python tools/run-all-checks.py
```

Running the suite after manifest generation helps verify deterministic metadata behavior.


## Non-guarantee summary

The validation suite does not prove deep semantic correctness, legal approval, security certification, compliance approval, production readiness, deployment, or public release.


## Validation guarantee scope

The validation tools perform repository structure and consistency validation; does not prove deep semantic correctness, legal approval, rights clearance, privacy compliance, security certification, deployment success, app store approval, compliance approval, production readiness, or public release success.
