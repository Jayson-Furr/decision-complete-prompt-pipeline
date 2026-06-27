# Project Brief — ConfigWeave

## One-sentence concept

A TypeScript shared library that loads layered configuration files, validates them against a schema, and produces a normalized configuration object with traceable defaults and overrides.

## Target users

```text
- application developers;
- tool authors;
- build pipeline maintainers;
- AI prompt package authors who want structured configuration loading.
```

## Core features

```text
- load multiple YAML or JSON config files;
- merge defaults, profiles, and overrides;
- validate required fields;
- report ignored, overridden, and defaulted values;
- produce a normalized configuration object;
- expose a small typed API;
- provide CLI helper for validation.
```

## High-stakes areas

```text
- package publishing is not authorized by this example;
- license compatibility must be reviewed;
- no secrets should be printed in validation output;
- security-sensitive config values should be redacted.
```
