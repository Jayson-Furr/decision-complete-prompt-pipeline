# Profile Depth Balance Report

## Purpose

This report documents the v1.0.0 profile depth balancing work.

Earlier builds intentionally made the Unity profile very detailed. Batch 12 brings the web application and shared library / SDK profiles closer to the same level of specificity while keeping all profile families governed by the same stage authority, safety, decision-ledger, traceability, and handoff rules.

## Included profile families

| Profile family | Current status | Notes |
|---|---|---|
| default | Complete | Baseline behavior for all stages. |
| unity_game | Complete and deep | Strongest engine-specific profile family. |
| web_application | Complete and deepened | Now includes frontend, backend, routing, state, API, data, auth/privacy, testing, build, and deployment validation rules. |
| shared_library | Complete and deepened | Now includes public API surface, versioning, compatibility, packaging, release, docs, tests, license, and registry-publishing rules. |

## Web application depth additions

The web application family now includes explicit handling for:

```text
frontend framework
routing
state management
forms and validation
API integration
backend/API boundaries
database and persistence
security and privacy
authentication and authorization
accessibility
responsive design
build validation
deployment authorization
static hosting vs server hosting
secrets and environment variables
```

## Shared library / SDK depth additions

The shared library family now includes explicit handling for:

```text
public API surface
API stability level
semantic versioning
breaking-change policy
module formats
package manager
registry publishing
runtime compatibility
dependency policy
test matrix
documentation examples
license review
security advisory handling
release and publish authorization
```

## Remaining planned profile families

Recommended future profile families are listed in:

```text
configuration-examples/profile-family-roadmap.yaml
docs/Profile-Family-Roadmap.md
```

Highest priority candidates:

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

## Depth policy

A profile is considered public-ready when it provides product-specific rules for all four stages:

```text
Stage 1: design surfaces and high-stakes scan areas.
Stage 2: work package decomposition and expected artifact strategy.
Stage 3: fabrication behavior, supported file types, and external-tool handling.
Stage 4: validation, repair classification, external validation, final package, and approval handling.
```
