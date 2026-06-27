# FAQ

## Is this a code generator?

It can be used to generate code during Stage 3, but the full package is broader than code generation. It is a traceable prompt pipeline for design, planning, fabrication, validation, packaging, and handoff.

## Does Stage 1 create code?

No. Stage 1 decides the design.

## Does Stage 2 create deliverables?

No. Stage 2 creates the execution-ready fabrication plan, work packages, Stage 3 prompts, contractor briefs, expected artifacts, dependencies, and QA matrix.

## Does Stage 3 do final validation?

No. Stage 3 may perform preliminary validation, but Stage 4 performs final validation and packaging.

## Does Stage 4 deploy or publish?

No. Stage 4 prepares final handoff, approval packets, release-candidate notes, and package classifications. Deployment, public release, store submission, credential use, and destructive actions require explicit authorization and are not performed by default.

## Why are there four prompt modes?

Different workflows need different interruption levels. Some users want speed, some want full control, and most want a balanced default.

## What does “100% complete” mean?

It means every required item is accounted for. It does not mean every item passed cleanly or that no warnings remain.

## What if information is missing?

Missing information should become a controlled placeholder, review gate, blocker, exclusion, external requirement, or not-applicable determination. The pipeline should not use vague `TBD` values.

## Can I use this for non-game products?

Yes. The pipeline supports websites, web applications, web services, desktop apps, mobile apps, shared libraries, SDKs, and hybrid systems. Product-specific configuration examples currently include Unity games, web applications, and shared libraries.

## Can I add my own product profile?

Yes. Copy a stage-specific configuration profile and create a new profile under `configuration-examples/` or in your own project repository.

## Can this be used with human contractors?

Yes. Stage 2 can create contractor briefs and execution packets that are intended for humans as well as AI agents.

## Why does the pipeline care about rights and source provenance?

Public use of images, audio, fonts, brands, third-party code, and reference materials can create rights or licensing issues. The pipeline records provenance and preserves review gates instead of assuming permissions.
