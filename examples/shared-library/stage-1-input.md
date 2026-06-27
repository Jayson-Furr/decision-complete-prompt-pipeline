# Stage 1 Input Packet — Shared Library Example

## Product name

```text
ConfigWeave
```

## Product type

```text
Shared library / SDK
```

## Short description

A TypeScript library for loading, merging, validating, and normalizing layered YAML/JSON configuration files.

## Preferred toolchain

```text
Language: TypeScript
Runtime: Node.js LTS
Package manager: npm
Test framework: Vitest
Build output: ESM and CJS if feasible
Documentation: Markdown
```

## API goals

```text
- loadConfig(files, options)
- validateConfig(config, schema)
- normalizeConfig(config, defaults)
- createConfigReport(result)
```

## Non-goals

```text
- no remote config fetching in v1;
- no secret manager integration in v1;
- no package publishing authorization in this example.
```

## Review-gated notes

```text
- Publishing to npm requires explicit authorization.
- License compatibility must be reviewed before public package release.
- Do not include real secrets in examples or test fixtures.
```
