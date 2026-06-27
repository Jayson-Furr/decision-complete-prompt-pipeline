# API Design Notes — Shared Library Example

## Candidate API

```typescript
loadConfig(paths: string[], options?: LoadConfigOptions): Promise<LoadConfigResult>
validateConfig(config: unknown, schema: ConfigSchema): ValidationResult
normalizeConfig(config: unknown, defaults: unknown): NormalizedConfigResult
createConfigReport(result: NormalizedConfigResult): ConfigReport
```

## Candidate package files

```text
src/index.ts
src/loadConfig.ts
src/mergeConfig.ts
src/validateConfig.ts
src/normalizeConfig.ts
src/reporting.ts
src/types.ts
tests/loadConfig.test.ts
tests/mergeConfig.test.ts
README.md
package.json
tsconfig.json
```

## Review-gated areas

```text
- npm publish authorization;
- license compatibility;
- dependency security;
- secret redaction behavior;
- public API stability claims.
```
