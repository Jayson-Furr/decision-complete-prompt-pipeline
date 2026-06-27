# Shared Artifact Boundary Markup

## Canonical stage markers

### Stage 1

```text
<<<BEGIN STAGE 1 ARTIFACT: 100% DECISION-COMPLETE DIGITAL PRODUCT DESIGN SPECIFICATION SUITE>>>

[Stage 1 artifact content]

<<<END STAGE 1 ARTIFACT>>>
```

### Stage 2

```text
<<<BEGIN STAGE 2 ARTIFACT: 100% EXECUTION-READY FABRICATION PACKAGE SUITE>>>

[Stage 2 artifact content]

<<<END STAGE 2 ARTIFACT>>>
```

### Stage 3

```text
<<<BEGIN STAGE 3 ARTIFACT: 100% FABRICATION-COMPLETE DELIVERABLE PACKAGE SUITE>>>

[Stage 3 artifact content]

<<<END STAGE 3 ARTIFACT>>>
```

### Stage 4

```text
<<<BEGIN STAGE 4 ARTIFACT: 100% VALIDATION-COMPLETE FINAL HANDOFF PACKAGE SUITE>>>

[Stage 4 artifact content]

<<<END STAGE 4 ARTIFACT>>>
```

## Rules

1. Artifact headers appear inside markers.
2. Completion gates appear inside markers.
3. Machine-readable companion data appears inside markers unless delivered as separate named files.
4. Prompt files and configuration files are not wrapped in artifact markers.
5. Malformed markers should be repaired only when intended stage and artifact type are unambiguous.
