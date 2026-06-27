
# Validator Implementation Notes

The validation tools in `tools/` are intentionally lightweight, deterministic repository checks. They are designed for public repository maintenance, not for proving that every future AI-generated artifact is correct.

## Validator categories

```text
- structure validators;
- prompt consistency validators;
- artifact boundary validators;
- configuration/profile validators;
- schema-guide validators;
- example validators;
- decision ledger validators;
- machine-readable companion validators;
- Markdown link validators;
- GitHub readiness validators;
- publication polish validators;
- release readiness validators.
```

## Batch 12 additions

Batch 12 adds:

```text
tools/validate-profile-depth.py
tools/validate-validation-scope.py
tools/validate-semantic-consistency.py
```

These validators improve the repository's public credibility by checking profile specificity and preventing validation overclaiming.

## Determinism

Generated manifests should be deterministic. Avoid generated timestamps in source-controlled manifests unless they are fixed release metadata or explicitly excluded from CI diff checks.
