# Troubleshooting

This guide covers common issues when running the pipeline.

## The next stage says the prior artifact is missing

Check whether you copied the full artifact boundary markers.

For Stage 2, the Stage 1 artifact must include:

```text
<<<BEGIN STAGE 1 ARTIFACT: 100% DECISION-COMPLETE DIGITAL PRODUCT DESIGN SPECIFICATION SUITE>>>
...
<<<END STAGE 1 ARTIFACT>>>
```

If the markers are missing, the next stage may classify the input as malformed.

## The artifact is too large to paste

Use continuation handling only when necessary. Save the full artifact as a markdown file if your environment supports attachments. Ensure the file begins and ends with the correct boundary markers.

## Stage 3 marks binary assets as external-tool-required

This is expected when the current environment cannot actually create the binary file. Stage 3 must not pretend that images, audio, video, 3D models, Unity scenes, prefabs, or builds exist unless they were actually created.

## Stage 4 says external validation is required

This is expected when validation requires a tool or environment not available to the AI.

Examples:

```text
- Unity Editor import validation;
- TypeScript build execution;
- browser runtime testing;
- package registry dry-run;
- security testing;
- accessibility audit;
- app store review.
```

## I need to change a feature after Stage 2

Rerun Stage 1 first. Then rerun Stage 2, Stage 3, and Stage 4. Stage 2 may not redesign Stage 1, and later stages must preserve upstream authority.

## I need to change work package boundaries after Stage 3

Rerun Stage 2, then rerun Stage 3 and Stage 4. Stage 3 may not re-plan Stage 2.

## Stage 4 refuses to repair something

Stage 4 can only perform repairs that preserve Stage 1 design, Stage 2 execution plan, and Stage 3 artifact intent. If a repair would change behavior, design, security, privacy, licensing, deployment, or release state, it must be review-gated, blocked, or moved to the correct upstream stage.

## I see `Ready with Warnings`

`Ready with Warnings` means the final package can be handed off, but warnings remain. It does not mean defect-free or release-ready.

## I want fewer questions

Use High-Stakes Interview or No Questions mode.

## I want more control

Use Low-Stakes Interview mode.

## The repository validation tool fails

Run:

```bash
python tools/validate-package-structure.py
```

Read the missing-path message. Restore the missing file or rerun the batch that created it.
