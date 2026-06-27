# Shared Machine-Readable Companion Rules

## Core rule

The human-readable document suite is canonical. If machine-readable companion data conflicts with the human-readable suite, the human-readable suite controls.

## Preferred formats

| Data Type | Preferred Format |
|---|---|
| Configuration | YAML |
| Handoff Packet | YAML |
| Manifest | JSON or CSV |
| Registry | JSON or CSV |
| Decision Ledger | CSV |
| Decision State Register | JSON or CSV |
| Traceability Matrix | CSV |
| Dependency Graph | JSON |
| Validation Report | CSV |
| Repair Log | CSV |
| Link Graph | JSON |

## Required principles

1. Companion data mirrors human-readable documents.
2. Companion data uses canonical stable IDs.
3. Companion data introduces no decisions absent from human-readable documents.
4. Companion data uses controlled vocabulary.
5. Companion data exposes no secrets or credentials.
6. Companion data distinguishes expected, fabricated, external-tool-required, and final artifacts.

## Validation terms

Machine-readable companion data must preserve every handoff packet and traceability record that appears in the human-readable suite.

The handoff packet must use stable IDs, and traceability data must mirror the human-readable traceability matrix.
