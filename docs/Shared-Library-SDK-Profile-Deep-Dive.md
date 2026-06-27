
# Shared Library / SDK Profile Deep Dive

The shared library / SDK profile family is intended for reusable code packages, public or internal APIs, developer-facing documentation, examples, tests, and package publishing workflows.

Batch 12 deepens this profile so it is closer to the Unity profile in specificity.

## Stage 1 design depth

The Stage 1 shared library profile now emphasizes:

```text
- public API surface;
- API stability level;
- semantic versioning expectations;
- runtime and language compatibility;
- dependency policy;
- error model;
- documentation and example requirements;
- package publishing assumptions;
- license and rights review gates.
```

## Stage 2 execution depth

The Stage 2 shared library profile now emphasizes work packages for:

```text
- package scaffold;
- public API modules;
- type declarations or interface definitions;
- runtime adapters;
- test matrix;
- examples;
- documentation;
- changelog and release notes;
- package publishing preparation.
```

## Stage 3 fabrication depth

The Stage 3 shared library profile now distinguishes:

```text
- source code and type files that can be fabricated;
- tests, examples, README, and API docs;
- package metadata drafts;
- external validation required for install, test, build, bundle, type-check, and package publishing dry runs;
- high-stakes handling for public registry publishing and license claims.
```

## Stage 4 finalization depth

The Stage 4 shared library profile now clarifies:

```text
- API compatibility validation;
- test and type-check status;
- package manifest validation;
- public publishing not performed;
- release authorization requirements;
- license review requirements;
- final package inclusion and warnings.
```
