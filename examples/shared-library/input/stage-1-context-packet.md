# Stage 1 Context Packet — ConfigWeave

Use this packet as input for Stage 1.

## Product seed

```text
Product Name: ConfigWeave
Product Type: Shared library / SDK
Description: A TypeScript shared library for merging layered configuration files with predictable precedence, validation hooks, and audit-friendly conflict reporting.
```

## Preferences and constraints

- TypeScript
- ESM and CJS outputs
- No runtime dependencies unless justified
- Vitest-style tests
- Public API stability emphasized
- Package publication review-gated

## Candidate features

- Layered merge engine
- Conflict reporter
- Schema hook interface
- Default resolver
- Typed result model
- CLI example
- README usage examples
- Test fixtures

## Known review areas

- Open-source license choice
- Package registry publication
- Dependency licensing
- Security implications of loading config files

## Requested Stage 1 behavior

Use the recommended medium-stakes design interview. Resolve low-stakes design details automatically. Interview for medium- and high-stakes decisions. Produce a 100% decision-complete design specification suite with asset packets, positive and negative design prompts, requirements, acceptance criteria, traceability, placeholders, review gates, and Stage 2 handoff contract.

## Configuration to use

```text
configuration-examples/stage-1-shared-library.configuration.yaml
pipeline.configuration.yaml
```
