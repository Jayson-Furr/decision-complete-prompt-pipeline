# Project Brief — ConfigWeave

## Product summary

A TypeScript shared library for merging layered configuration files with predictable precedence, validation hooks, and audit-friendly conflict reporting.

## Product type

```text
Shared library / SDK
```

## Design preferences

- TypeScript
- ESM and CJS outputs
- No runtime dependencies unless justified
- Vitest-style tests
- Public API stability emphasized
- Package publication review-gated

## Initial feature candidates

- Layered merge engine
- Conflict reporter
- Schema hook interface
- Default resolver
- Typed result model
- CLI example
- README usage examples
- Test fixtures

## Known high-stakes or review-gated topics

- Open-source license choice
- Package registry publication
- Dependency licensing
- Security implications of loading config files

## Validation focus

- API surface review
- Type declaration review
- Unit test coverage
- Package manifest validation
- License and publication review

## Notes for Stage 1

This brief is intentionally incomplete. Stage 1 should produce a decision-complete design specification by interviewing for medium- and high-stakes decisions, creating controlled placeholders where needed, preserving review-gated issues, and avoiding unsupported facts.
