# Example Scenario Guide

The `examples/` directory contains practical sample scenarios that show how to use the prompt package.

## Included scenario packets

```text
examples/unity-game/
examples/web-application/
examples/shared-library/
examples/minimal-complete-run/todo-web-app/
examples/minimal-complete-run/unity-button-click-prototype/
```

## Included complete miniature runs

```text
examples/minimal-complete-run/todo-web-app/
examples/minimal-complete-run/unity-button-click-prototype/
```

Each example includes:

```text
- input project brief;
- Stage 1 context packet;
- configuration override sample;
- runbooks for Stage 1 through Stage 4;
- artifact skeletons for each stage;
- validation checklist;
- sample decision ledger rows;
- sample traceability matrix rows.
```

## How to use an example

1. Open the example README.
2. Review `input/project-brief.md`.
3. Copy `input/stage-1-context-packet.md` into the recommended Stage 1 prompt.
4. Optionally attach or paste the example configuration override.
5. Follow the runbooks in order.
6. Compare your generated artifacts with the artifact skeletons.
7. Use the sample ledger and traceability files as formatting references.

## Important note

The original scenario folders are input packets and skeletons. The `examples/minimal-complete-run/` folders are compact completed runs with Stage 1 through Stage 4 artifacts, fabricated files, decision ledgers, traceability matrices, and final handoff packets.

## Example selection

| Product Type | Example Folder | Recommended Profiles |
|---|---|---|
| Unity game | `examples/unity-game/` | `stage-N-unity-game.configuration.yaml` |
| Web application | `examples/web-application/` | `stage-N-web-application.configuration.yaml` |
| Shared library / SDK | `examples/shared-library/` | `stage-N-shared-library.configuration.yaml` |
| Complete Todo web app | `examples/minimal-complete-run/todo-web-app/` | `stage-N-web-application.configuration.yaml` |
| Complete Unity button prototype | `examples/minimal-complete-run/unity-button-click-prototype/` | `stage-N-unity-game.configuration.yaml` |

## Converting examples to real runs

Replace the sample project brief with your own project context, then run the same Stage 1 through Stage 4 process.

Do not treat sample artifacts as authoritative for your project. The generated artifacts from your run become your actual authority chain.


## Complete miniature runs

Complete miniature runs are different from scenario packets. They include compact completed Stage 1, Stage 2, Stage 3, and Stage 4 artifact examples. They also include populated decision ledgers, traceability matrices, fabricated files, validation reports, repair logs, and final handoff packets.

Use [Complete-Miniature-Run-Guide.md](Complete-Miniature-Run-Guide.md) when you want to inspect the finished artifact chain directly.
