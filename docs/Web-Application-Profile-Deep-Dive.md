
# Web Application Profile Deep Dive

The web application profile family is intended for browser-based applications with user interfaces, client-side state, optional backend APIs, optional persistence, and optional deployment.

Batch 12 deepens this profile so it is closer to the Unity profile in specificity.

## Stage 1 design depth

The Stage 1 web application profile now emphasizes:

```text
- frontend framework decision;
- routing strategy;
- state management strategy;
- styling strategy;
- form and validation behavior;
- accessibility and responsive design;
- data model and API boundary;
- authentication and authorization review gates;
- personal data and privacy review;
- deployment and hosting assumptions.
```

## Stage 2 execution depth

The Stage 2 web profile now emphasizes work packages for:

```text
- frontend scaffold;
- route and page implementation;
- component library;
- form validation;
- state management;
- API client contracts;
- backend service stubs where applicable;
- database schema or not-applicable decisions;
- test planning;
- build and deployment preparation.
```

## Stage 3 fabrication depth

The Stage 3 web profile now distinguishes:

```text
- text-based files that can be fabricated, such as TypeScript, CSS, JSON, tests, and docs;
- external validation required for package install, build, browser runtime, accessibility tooling, and deployment;
- high-stakes handling for authentication, personal data, secrets, payments, analytics, and production hosting.
```

## Stage 4 finalization depth

The Stage 4 web profile now clarifies:

```text
- build validation versus source review;
- browser smoke testing versus not-run classification;
- accessibility validation limits;
- deployment not performed statement;
- secret exposure checks;
- final artifact inclusion rules;
- production release authorization requirements.
```
