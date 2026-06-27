# Shared ID Namespace

## Purpose

This file defines stable IDs for traceability, links, ledgers, registers, manifests, validation reports, repair logs, and handoff packets.

## Core format

```text
[STAGE]-[ENTITY-TYPE]-[NUMBER]
```

Examples:

```text
S1-DOC-001
S1-FEAT-001
S2-WP-001
S3-ART-001
S4-VAL-001
```

## Stage prefixes

```text
S1 = Stage 1 — Design Specification
S2 = Stage 2 — Execution Planning
S3 = Stage 3 — Fabrication
S4 = Stage 4 — Validation, Repair, Packaging, and Final Handoff
```

## Stage 1 namespace

```text
S1-DOC-001      Stage 1 document
S1-FEAT-001     Feature
S1-REQ-001      Requirement
S1-AC-001       Acceptance criterion
S1-SCR-001      Screen / view / page
S1-FLOW-001     Workflow / user flow
S1-STORY-001    User story
S1-AST-001      Asset
S1-TOK-001      Design token
S1-DATA-001     Data object
S1-API-001      API / interface
S1-STATE-001    State
S1-ANIM-001     Animation
S1-SFX-001      Sound effect
S1-VID-001      Video / cinematic
S1-PH-001       Placeholder
S1-REV-001      Review flag
S1-RISK-001     Risk
S1-DEC-001      Design decision
S1-CONF-001     Conflict
S1-SRC-001      Source context item
S1-PROV-001     Source provenance item
```

## Stage 2 namespace

```text
S2-DOC-001      Stage 2 document
S2-WP-001       Work package
S2-P3-001       Generated Stage 3 prompt
S2-BRIEF-001    Contractor brief
S2-DEP-001      Dependency
S2-ARTEXP-001   Expected artifact
S2-QA-001       QA / validation item
S2-PH-001       Placeholder handling item
S2-REV-001      Review-gated handling item
S2-BLOCK-001    Blocked item
S2-EXEC-001     Execution decision
S2-TRACE-001    Traceability item
S2-CONF-001     Conflict
```

## Stage 3 namespace

```text
S3-DOC-001      Stage 3 document
S3-FR-001       Fabrication result
S3-ART-001      Fabricated artifact
S3-VAL-001      Preliminary validation item
S3-DEF-001      Defect / deviation item
S3-EXT-001      External-tool-required item
S3-PH-001       Preserved placeholder
S3-REV-001      Preserved review-gated item
S3-FAB-001      Fabrication decision
S3-TRACE-001    Traceability item
S3-CONF-001     Conflict
```

## Stage 4 namespace

```text
S4-DOC-001      Stage 4 document
S4-VAL-001      Final validation result
S4-REP-001      Repair item
S4-FINAL-001    Final artifact
S4-QA-001       Final QA item
S4-DEF-001      Final defect / unresolved item
S4-APP-001      Approval item
S4-REL-001      Release / handoff readiness item
S4-FIN-001      Finalization decision
S4-TRACE-001    Traceability item
S4-CONF-001     Conflict
```

## Rules

1. Once assigned, an ID remains stable.
2. Later stages preserve upstream IDs exactly.
3. File paths are not IDs.
4. Lowercase forms are Markdown anchors only.
5. Machine-readable data uses canonical uppercase IDs.

## Traceability example

```text
S1-SCR-001 → S2-WP-001 → S3-ART-001 → S4-FINAL-001
```
