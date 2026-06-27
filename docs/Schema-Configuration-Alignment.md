# Schema and Configuration Alignment

The configuration examples use an inheritance model.

Default stage profiles are complete base configurations:

```text
stage-1-default.configuration.yaml
stage-2-default.configuration.yaml
stage-3-default.configuration.yaml
stage-4-default.configuration.yaml
```

Product-specific profiles extend those base files:

```yaml
configuration_metadata:
  extends: "stage-1-default.configuration.yaml"
```

A product-specific profile may omit inherited sections when the matching default configuration supplies them. Validators should therefore distinguish between:

```text
- explicitly required keys that must appear in every file; and
- inherited keys that may be supplied by the referenced default profile.
```

## Publication rule

The repository treats these schema files as human-readable YAML schema guides for v1.0.0. They are not strict JSON Schema documents. Future releases may add enforceable JSON Schema files if desired.
