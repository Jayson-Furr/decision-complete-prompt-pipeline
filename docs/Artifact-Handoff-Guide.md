# Artifact Handoff Guide

Each stage artifact is copied into the next stage prompt. The handoff works only if the full artifact is preserved.

## Required boundary markers

### Stage 1 to Stage 2

```text
<<<BEGIN STAGE 1 ARTIFACT: 100% DECISION-COMPLETE DIGITAL PRODUCT DESIGN SPECIFICATION SUITE>>>

[Stage 1 artifact]

<<<END STAGE 1 ARTIFACT>>>
```

### Stage 2 to Stage 3

```text
<<<BEGIN STAGE 2 ARTIFACT: 100% EXECUTION-READY FABRICATION PACKAGE SUITE>>>

[Stage 2 artifact]

<<<END STAGE 2 ARTIFACT>>>
```

### Stage 3 to Stage 4

```text
<<<BEGIN STAGE 3 ARTIFACT: 100% FABRICATION-COMPLETE DELIVERABLE PACKAGE SUITE>>>

[Stage 3 artifact]

<<<END STAGE 3 ARTIFACT>>>
```

### Final Stage 4 artifact

```text
<<<BEGIN STAGE 4 ARTIFACT: 100% VALIDATION-COMPLETE FINAL HANDOFF PACKAGE SUITE>>>

[Stage 4 artifact]

<<<END STAGE 4 ARTIFACT>>>
```

## Copying rule

Copy the complete artifact, including:

```text
- begin marker;
- artifact header;
- root index;
- all document sections;
- decision registers;
- decision ledgers;
- placeholders;
- review gates;
- machine-readable companion data;
- handoff packet;
- completion gate;
- end marker.
```

Do not copy only the summary.

## Multiple artifacts

If you provide multiple prior-stage artifacts, the immediate prior stage is primary.

| Current Stage | Primary Input | Optional Reference |
|---|---|---|
| Stage 2 | Stage 1 artifact | Configuration files |
| Stage 3 | Stage 2 artifact | Stage 1 artifact, environment notes |
| Stage 4 | Stage 3 artifact | Stage 2 and Stage 1 artifacts |

## Partial or malformed artifacts

If a boundary marker is missing, the next stage should classify the artifact as malformed or partial. It may still proceed if enough content exists, but it must register the issue.

## Do not nest artifacts casually

A later-stage artifact should not include the full raw prior-stage artifact unless it is explicitly placed in an appendix. Handoffs should rely on source IDs, traceability matrices, and handoff packets.

## Handoff packet role

Every stage includes a handoff packet. The handoff packet tells the next stage:

```text
- what upstream authority controls;
- which registers are critical;
- which placeholders remain;
- which items are review-gated;
- which blockers remain;
- which external tools or validation are required.
```

The handoff packet does not replace the full artifact. It makes the full artifact easier to ingest.
