# Shared Document Header Template

## Universal document header

```yaml
---
Document ID: "[STAGE-DOC-ID]"
Document Title: "[Document Title]"
Document Type: "[Index / Specification / Register / Ledger / Manifest / Matrix / Report / Packet / Appendix / Artifact / Configuration / Schema / Guide / Overview / Contract / Brief / Library / Checklist / Instructions / Other]"
Stage: "[Stage 1 / Stage 2 / Stage 3 / Stage 4]"
Parent Document: "[Parent Document ID and Link / None for root document]"
Child Documents:
  - "[Child Document ID and Link / None]"
Related Documents:
  - "[Related Document ID and Link / None]"
Source Authority:
  - "[Relevant upstream IDs, configuration IDs, decision IDs, artifact IDs, validation IDs, repair IDs, or approval IDs]"
Status: "[Stage-Specific Status]"
Human-Readable: "Yes"
Machine-Readable Companion: "[None / JSON / YAML / CSV / Markdown / XML / TOML / Structured Text / Other]"
Downstream Use: "[How this document should be used by the next stage or final recipient]"
---
```

## Root index header template

```yaml
---
Document ID: "[S#-DOC-000]"
Document Title: "[Stage-Specific Root Index Title]"
Document Type: "Index"
Stage: "[Stage 1 / Stage 2 / Stage 3 / Stage 4]"
Parent Document: "None — root document"
Child Documents:
  - "[Child Document ID and Link]"
Related Documents:
  - "[Related Document ID and Link]"
Source Authority:
  - "Active stage artifact structure"
  - "Active stage prompt requirements"
Status: "[Stage-Specific Complete Status]"
Human-Readable: "Yes"
Machine-Readable Companion: "None"
Downstream Use: "[Stage-specific index usage]"
---
```

## Header validation checklist

| Check | Pass / Fail | Notes |
|---|---|---|
| Document ID is present | [Pass / Fail] | [Notes] |
| Document ID uses correct stage prefix | [Pass / Fail] | [Notes] |
| Document type uses controlled vocabulary | [Pass / Fail] | [Notes] |
| Parent document is identified or root status is stated | [Pass / Fail] | [Notes] |
| Source authority is listed | [Pass / Fail] | [Notes] |
| Status uses stage-specific vocabulary | [Pass / Fail] | [Notes] |
| Human-Readable is set to Yes | [Pass / Fail] | [Notes] |
| Downstream Use is populated | [Pass / Fail] | [Notes] |
```
