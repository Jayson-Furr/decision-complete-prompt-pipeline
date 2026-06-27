# Profile Family Roadmap

DecisionComplete Prompt Pipeline v1.0.0 ships with four profile families:

```text
default
unity_game
web_application
shared_library
```

This roadmap identifies recommended future profile families. These are enhancement candidates, not v1.0.0 requirements.

## Recommended next profile families

| Priority | Profile Family | Recommended Repository Slug | Rationale | Suggested Stage Files |
|---:|---|---|---|---|
| 1 | Godot Game | `godot-game` | Completes another major game-engine path and complements the Unity profile. | Stage 1-4 configs |
| 2 | Unreal Game | `unreal-game` | Covers high-fidelity game and simulation projects with strong external-tool constraints. | Stage 1-4 configs |
| 3 | Web Service / API | `web-service` | Covers backend APIs, service contracts, auth, data, deployment review, and external validation. | Stage 1-4 configs |
| 4 | Mobile Application | `mobile-application` | Covers app UX, platform policies, privacy, app-store review, device validation, and mobile release gates. | Stage 1-4 configs |
| 5 | Desktop Application | `desktop-application` | Covers installable desktop UX, packaging, update strategy, OS compatibility, and code-signing review. | Stage 1-4 configs |
| 6 | Website / Documentation Site | `website` | Covers public content, information architecture, accessibility, SEO, content review, and publishing gates. | Stage 1-4 configs |
| 7 | Desktop Service | `desktop-service` | Covers background services, local permissions, OS integration, logging, installation, and safety review. | Stage 1-4 configs |
| 8 | Mobile Service | `mobile-service` | Covers mobile backend services, push notifications, account systems, privacy, and external API constraints. | Stage 1-4 configs |
| 9 | SDK | `sdk` | Separates SDK concerns from shared libraries, including examples, API stability, versioning, and publishing. | Stage 1-4 configs |
| 10 | CLI / Developer Tool | `cli-developer-tool` | Covers command design, scripting, local file safety, packaging, and developer documentation. | Stage 1-4 configs |

## Future AI-oriented profile candidates

| Profile Family | Repository Slug | Notes |
|---|---|---|
| AI Agent Application | `ai-agent-application` | Should emphasize tool authorization, external API boundaries, logging, review gates, and safety constraints. |
| LLM-Powered Web Application | `llm-powered-web-application` | Should emphasize prompt/data boundaries, privacy, retrieval sources, evals, and model/version configuration. |
| Data Pipeline | `data-pipeline` | Should emphasize schemas, provenance, transformations, privacy, validation, and destructive-operation guards. |
| Developer Platform | `developer-platform` | Should emphasize APIs, SDKs, docs, examples, authentication, and release compatibility. |
| Design System / UI Kit | `design-system-ui-kit` | Should emphasize tokens, components, accessibility, versioning, and visual regression validation. |

## Profile family standard

Every new profile family should include:

```text
configuration-examples/stage-1-[profile].configuration.yaml
configuration-examples/stage-2-[profile].configuration.yaml
configuration-examples/stage-3-[profile].configuration.yaml
configuration-examples/stage-4-[profile].configuration.yaml
```

Each profile family should preserve:

```text
- stage authority rules;
- prompt mode behavior;
- decision ledger schema;
- controlled vocabulary alignment;
- artifact boundary markers;
- placeholder and review-gated handling;
- external-tool and external-validation honesty;
- no-unauthorized-side-effect rules.
```

## v1.0.0 Profile Depth Balance

Batch 12 deepens the web application and shared library / SDK profile families so they are closer to the specificity of the Unity profile.

The intended maturity model is:

| Profile Family | v1.0.0 Status | Depth Target |
|---|---|---|
| Unity game | Deep | Engine, scene, prefab, UI, asset import, validation, and release concerns |
| Web application | Deepened in Batch 12 | Frontend, backend, API, database, auth, privacy, deployment, testing |
| Shared library / SDK | Deepened in Batch 12 | Public API, semver, packaging, compatibility, docs, tests, publishing |
| Godot game | Planned | Engine scene/resource/export validation profile |
| Unreal game | Planned | Blueprint/C++/asset/map/package validation profile |
| Web service | Planned | API, database, auth, observability, deployment validation profile |
| Mobile application | Planned | iOS/Android, store, privacy, device testing, release profile |
| Desktop application | Planned | installer, OS integration, signing, update, accessibility profile |

The repository should continue adding profile families without weakening the stage authority model.


## Batch 12 profile balance update

Batch 12 deepens the included web application and shared library / SDK profile families so they are closer to the Unity profile in stage-specific specificity.

The goal is not to make every profile as engine-specific as Unity. The goal is to ensure every shipped profile family has:

```text
- product-specific Stage 1 design surfaces;
- product-specific Stage 2 work package decomposition;
- product-specific Stage 3 fabrication and external-validation rules;
- product-specific Stage 4 validation, final package, and approval rules;
- explicit high-stakes review domains;
- clear external-tool and external-validation handling.
```

The `profile-family-roadmap.yaml` file now records profile depth status for shipped families.

<!-- batch-12-depth-update -->

## Batch 12 profile-depth update

The web application and shared library / SDK profile families were deepened to better match the specificity of the Unity game profile. The repository now treats these three product families as v1.0.0 complete profile families:

```text
unity_game
web_application
shared_library
```

The next recommended families are:

```text
godot_game
unreal_game
web_service
mobile_application
desktop_application
sdk
cli_developer_tool
ai_agent_application
```

Use `docs/Profile-Authoring-Guide.md` when creating additional profile families.
