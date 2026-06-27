# Shared Decision Ledger Schema

## Universal ledger columns

```text
| Artifact ID | Prompt Mode | Logging Level | Decision Key | Decision Category | Affected Item | Decision Question | Stakes Level | Logging Treatment | Option A | Option B | Option C | Option D | Other Options Considered | Selected Option Code | Selected Option Text | Decision Source | Selection Reason | Assumption Used? | Placeholder Used? | Review Requirement | Decision Status | Comparison Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

## CSV header

```csv
Artifact ID,Prompt Mode,Logging Level,Decision Key,Decision Category,Affected Item,Decision Question,Stakes Level,Logging Treatment,Option A,Option B,Option C,Option D,Other Options Considered,Selected Option Code,Selected Option Text,Decision Source,Selection Reason,Assumption Used?,Placeholder Used?,Review Requirement,Decision Status,Comparison Notes
```

## Logging threshold rules

| Prompt Mode | Line-Item Logged | Below-Threshold Summary |
|---|---|---|
| No Questions | Low, Medium, High | None |
| Low-Stakes Interview | Low, Medium, High | None |
| Medium-Stakes Interview | Medium, High | Low |
| High-Stakes Interview | High | Low, Medium |

## Canonical decision state register schema

```text
| Decision Key | Decision Category | Applies To | Decision Question | Final Resolution | Resolution Type | Constraint Strength | Source Basis | Downstream Instruction | Status |
|---|---|---|---|---|---|---|---|---|---|
```
