# Artifact Lifecycle

## Purpose

This document explains how artifacts move through the DecisionComplete Prompt Pipeline.

The pipeline’s core promise is that each stage produces a bounded, traceable artifact that becomes the input for the next stage.

---

## Lifecycle summary

```text
Rough input
  ↓
Stage 1 artifact: design specification
  ↓
Stage 2 artifact: execution-ready fabrication package
  ↓
Stage 3 artifact: fabricated deliverable package
  ↓
Stage 4 artifact: validation-complete final handoff package
```

---

## Stage 1 artifact

Output:

```text
100% Decision-Complete Digital Product Design Specification Suite
```

Stage 1 decides:

```text
- product type;
- scope;
- features;
- screens;
- workflows;
- user stories;
- assets;
- design system;
- technical constraints;
- requirements;
- acceptance criteria;
- placeholders;
- review gates.
```

Stage 1 does not create work packages or final deliverables.

---

## Stage 2 artifact

Output:

```text
100% Execution-Ready Fabrication Package Suite
```

Stage 2 decides:

```text
- work package boundaries;
- dependencies;
- generated Stage 3 prompts;
- contractor briefs;
- expected artifacts;
- QA plans;
- execution order;
- Stage 3 handoff contract.
```

Stage 2 does not fabricate files or assets.

---

## Stage 3 artifact

Output:

```text
100% Fabrication-Complete Deliverable Package Suite
```

Stage 3 records:

```text
- what was fabricated;
- what files were created;
- what file contents were produced;
- what could not be created;
- what is external-tool-required;
- what is blocked or review-gated;
- preliminary validation results;
- Stage 4 handoff contract.
```

Stage 3 does not perform final validation or final package release.

---

## Stage 4 artifact

Output:

```text
100% Validation-Complete Final Handoff Package Suite
```

Stage 4 records:

```text
- final validation;
- allowed repairs;
- repair log;
- final artifact manifest;
- final QA report;
- unresolved item register;
- approval packet;
- final handoff status.
```

Stage 4 does not deploy, publish, submit, release, or use credentials unless explicitly authorized.

---

## Authority chain

```text
Stage 1 controls design.
Stage 2 controls execution planning.
Stage 3 controls fabricated output records.
Stage 4 controls validation, repair classification, packaging, and final handoff.
```

Later stages must preserve earlier authority.

---

## Artifact boundary markers

Artifacts must be copied with their boundary markers.

The next stage uses those markers to identify the prior-stage source.

If a marker is missing or malformed, the next stage should report an intake issue and classify the artifact as partial, malformed, or blocked if needed.

---

## Completion does not mean perfection

Each stage’s completion status has a precise meaning.

```text
Decision-Complete means decisions are resolved, placeholder-complete, review-gated, excluded, or not applicable.
Execution-Ready means Stage 3 can execute or accurately classify work packages.
Fabrication-Complete means every Stage 2 work package has a result or safe classification.
Validation-Complete means every Stage 3 artifact has been validated, repaired, classified, included, excluded, blocked, or otherwise accounted for.
```

Validation-complete does not mean defect-free.

Ready with Warnings does not mean Ready without warnings.
