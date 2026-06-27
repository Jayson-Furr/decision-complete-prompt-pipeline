
# Validation Guarantee Matrix

This document describes repository structure and consistency validation and separates it from guarantees the repository does not make.

This matrix separates repository validation checks from guarantees the repository does not make.

| Area | Checked by repository tooling? | Guarantee level | Notes |
|---|---:|---|---|
| Required repository files | Yes | Structural | Checks that expected files exist. |
| Sixteen core prompt files | Yes | Structural + consistency | Checks stage/mode terms and artifact markers. |
| Artifact boundary markers | Yes | Consistency | Checks canonical boundary strings. |
| Configuration examples | Yes | Parseability + profile consistency | Checks YAML parseability and key profile contracts. |
| Product profile depth | Yes | Coverage heuristic | Checks that web/shared profiles include stage-specific depth sections and required domains. |
| Schemas | Yes | Documentation consistency | Checks schema guide presence and alignment language. |
| Example packets | Yes | Structure + sample artifact consistency | Checks complete miniature runs, boundaries, ledgers, traceability samples, and fabricated files. |
| Markdown links | Yes | Repository link consistency | Checks internal relative links where feasible. |
| Generated downstream artifacts | No | Not guaranteed | Must be reviewed per stage artifact rules. |
| Real product build/test success | No | Not guaranteed | Requires external tools and actual execution. |
| Security certification | No | Not guaranteed | Requires security review. |
| Legal / rights clearance | No | Not guaranteed | Requires rights and legal review. |
| Compliance approval | No | Not guaranteed | Requires qualified review. |
| Deployment / publication | No | Not performed | Requires explicit authorization and external execution. |


## Non-guarantee summary

The validation suite does not prove deep semantic correctness, downstream artifact correctness, legal approval, security certification, compliance approval, production readiness, deployment, or public release.


## Validation guarantee scope

The validation tools perform repository structure and consistency validation; does not prove deep semantic correctness, legal approval, rights clearance, privacy compliance, security certification, deployment success, app store approval, compliance approval, production readiness, or public release success.
