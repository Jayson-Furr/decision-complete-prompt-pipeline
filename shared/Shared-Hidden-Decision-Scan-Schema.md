# Shared Hidden Decision Scan Schema

## Universal scan table

```text
| Scan ID | Area Checked | Related IDs | Hidden Decision Found? | Stakes Level | Resolution | Resolution Record ID | Downstream Handling | Notes |
|---|---|---|---|---|---|---|---|---|
```

## Stage scan IDs

```text
S1-HDS-001      Stage 1 hidden design scan item
S2-HES-001      Stage 2 hidden execution scan item
S3-HFS-001      Stage 3 hidden fabrication scan item
S4-HZS-001      Stage 4 hidden finalization scan item
```

## Rule

A stage is not complete unless its hidden-decision scan has been completed and every found hidden decision has been resolved, registered, logged or summarized, and given downstream handling.
