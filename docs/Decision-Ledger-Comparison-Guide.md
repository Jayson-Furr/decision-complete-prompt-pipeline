# Decision Ledger Comparison Guide

Decision ledgers are designed for side-by-side comparison across pipeline runs.

## Why compare ledgers

Use ledger comparison when you want to know:

```text
- why two designs differ;
- why two execution plans decomposed work differently;
- why two fabrications produced different files;
- why one final package is Ready and another is Ready with Warnings;
- which decisions came from the user, configuration, upstream authority, or AI;
- which assumptions changed between runs.
```

## Standard ledger columns

Every standardized decision ledger uses the same column order:

```csv
Artifact ID,Prompt Mode,Logging Level,Decision Key,Decision Category,Affected Item,Decision Question,Stakes Level,Logging Treatment,Option A,Option B,Option C,Option D,Other Options Considered,Selected Option Code,Selected Option Text,Decision Source,Selection Reason,Assumption Used?,Placeholder Used?,Review Requirement,Decision Status,Comparison Notes
```

## Recommended comparison process

1. Export or copy the decision ledgers from two or more runs.
2. Align rows by `Decision Category`, `Affected Item`, and `Decision Question`.
3. Compare `Selected Option Text`.
4. Compare `Decision Source`.
5. Compare `Assumption Used?` and `Placeholder Used?`.
6. Inspect `Review Requirement` and `Decision Status`.
7. Use `Comparison Notes` to understand intentional differences.

## Most useful fields

| Field | Why It Matters |
|---|---|
| Prompt Mode | Explains interview threshold differences. |
| Logging Level | Explains why some decisions are summarized rather than row-level logged. |
| Decision Category | Groups comparable decisions. |
| Affected Item | Shows what was changed. |
| Selected Option Text | Shows the actual decision. |
| Decision Source | Shows who or what made the decision. |
| Selection Reason | Explains why. |
| Review Requirement | Highlights unresolved sensitive decisions. |
| Decision Status | Shows whether the decision is selected, blocked, review-gated, or not applicable. |

## Interpreting prompt-mode differences

A medium-stakes run may summarize low-stakes decisions that a low-stakes run logs line by line. This is expected.

A high-stakes run may summarize both low- and medium-stakes decisions. Any low- or medium-stakes decision that materially affects a high-stakes issue should still be elevated and logged.

## Example comparison question

```text
Why did Run A create one work package per screen, while Run B used hybrid work packages?
```

Check:

```text
Decision Category: Work Package Granularity
Affected Item: S2-DOC-006 or S2-WP registry
Selected Option Text
Selection Reason
Decision Source
Comparison Notes
```

## Example red flags

Investigate when:

```text
- high-stakes decisions are missing from the ledger;
- a decision source is AI-Selected when it should be Stage-1-Required;
- a placeholder was used but no placeholder registry row exists;
- a review requirement is present but no review-gated register item exists;
- selected option differs across runs but comparison notes are blank.
```
