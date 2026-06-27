# Shared Controlled Vocabularies

## Purpose

This file defines controlled values used across the pipeline for consistency, auditability, traceability, machine-readable companion data, and side-by-side comparison.

## 1. Stage IDs

```text
stage_1
stage_2
stage_3
stage_4
```

## 2. Prompt Mode Families

```text
No Questions
Low-Stakes Interview
Medium-Stakes Interview
High-Stakes Interview
```

## 3. Stakes Levels

```text
Low
Medium
High
```

## 4. Logging Treatments

```text
Line-Item Logged
Below-Threshold Summary
Elevated for Materiality
Deferred
Placeholder
Professional Review
Review-Gated
Repair-Gated
Blocked
External Tool Required
External Validation Required
Not Applicable
```

## 5. Decision Sources

```text
AI-Selected
Configuration-Selected
User-Provided
User-Selected
Stage-1-Required
Stage-2-Required
Stage-3-Required
Auto-Repaired
Placeholder
Professional Review
Not Applicable
```

## 6. Review Requirements

```text
None
User Review Suggested
User Review Required
Professional Review Required
External Authorization Required
External Validation Required
```

## 7. Decision Status Values

```text
Selected
Deferred
Placeholder
Review-Gated
Repair-Gated
Blocked
External-Tool-Required
External-Validation-Required
Excluded
Not Applicable
Not Used
```

## 8. Constraint Strength Values

```text
Hard Constraint
Strong Preference
Soft Preference
Default Assumption
Placeholder Constraint
Review-Gated Constraint
Repair-Gated Constraint
Blocked Constraint
External-Tool Constraint
External-Validation Constraint
```

## 9. Artifact Status Values

```text
100% Decision-Complete
Not Yet Decision-Complete
100% Execution-Ready
Not Yet Execution-Ready
100% Fabrication-Complete
Not Yet Fabrication-Complete
100% Validation-Complete
Not Yet Validation-Complete
```

## 10. Final Handoff Status Values

```text
Ready
Ready with Warnings
Review-Gated
Blocked
External Validation Required
```

## 11. Validation Status Values

```text
Passed
Failed
Partially Passed
Not Run
Not Applicable
```

## 12. Repair Status Values

```text
No Repair Needed
Auto-Repaired
Repair Proposed
Repair-Gated
Not Repairable
Blocked
Not Applicable
```

## 13. Traceability Status Values

```text
Fully Traced
Partially Traced
Traceability Gap
Mapped
Partially Mapped
Blocked
Review-Gated
Deferred
External Validation Required
Placeholder-Complete
External-Tool-Required
Not Applicable
```

## 14. Product Type Values

```text
Unity game
Unreal game
Godot game
Game prototype
Shared library
SDK
Desktop application
Desktop service
Mobile application
Mobile service
Website
Web application
Web service
Web platform
Web solution
Hybrid software system
Multi-component digital product
Unknown
```

## 15. Machine-Friendly Product Type Values

```text
unity_game
unreal_game
godot_game
game_prototype
shared_library
sdk
desktop_application
desktop_service
mobile_application
mobile_service
website
web_application
web_service
web_platform
web_solution
hybrid_software_system
multi_component_digital_product
auto_detect
unknown
```

## 16. Scope Tier Values

```text
Prototype
Vertical Slice
MVP
Version 1.0
Full Product Concept
Future Expansion
```

## 17. Document Type Values

```text
Index
Specification
Register
Ledger
Manifest
Matrix
Report
Packet
Appendix
Artifact
Configuration
Schema
Guide
Overview
Contract
Brief
Library
Checklist
Instructions
Other
Not Applicable
```

## 18. Asset Type Values

```text
Visual
UI
Icon
Illustration
Sprite
Texture
Model
Material
Animation
VFX
Audio
Sound Effect
Music
Voice
Video
Cinematic
Text
Copy
Documentation
Diagram
Data
Schema
Configuration
Technical
Code Example
Sample Project
API Example
Other
Not Applicable
```

## 19. Work Package Type Values

```text
Feature
Asset
Screen
View
Page
Code Module
Service
API
Integration
Data
Configuration
QA
Documentation
Audio
Video
Animation
Build / Packaging Preparation
Deployment Preparation
Prompt
Contractor Brief
External Tool Preparation
Other
Not Applicable
```

## 20. Artifact Type Values

```text
Source Code File
Configuration File
Schema File
Scene File
Prefab Specification
Sprite
Texture
Icon
Illustration
Sound Effect
Music Loop
Animation Clip
Video
Markdown Document
JSON File
YAML File
CSV File
XML File
TOML File
Test File
Build Script
Deployment Manifest
Prompt File
Contractor Brief
Documentation File
Data File
External Tool Packet
Binary Asset
Compiled Artifact
Package
Other
Not Applicable
```

## 21. Fabrication Status Values

```text
Fabricated
Partially Fabricated
Blocked
Review-Gated
Placeholder-Complete
External-Tool-Required
Not Applicable
```

## 22. Final Artifact Status Values

```text
Included
Included with Warning
Excluded
Blocked
Review-Gated
External-Tool-Required
External Validation Required
Placeholder-Complete
Not Applicable
```

## 23. Rights / Ownership Status Values

```text
User-Provided; Ownership Not Verified
User-Provided; Rights Claimed by User
User-Provided; Rights Confirmed by User
Third-Party; Rights Not Confirmed
Third-Party; License Provided
Generated; Rights Status Not Determined
Public Domain Claimed; Not Verified
Open License Claimed; Not Verified
Not Applicable
Unknown
```


## Machine-readable prompt mode values

```yaml
stage_1:
  - no_questions_full_ai_design_fabrication
  - low_stakes_design_interview
  - medium_stakes_design_interview
  - high_stakes_design_interview
stage_2:
  - no_questions_full_ai_execution_planning
  - low_stakes_execution_interview
  - medium_stakes_execution_interview
  - high_stakes_execution_interview
stage_3:
  - no_questions_full_ai_fabrication
  - low_stakes_fabrication_interview
  - medium_stakes_fabrication_interview
  - high_stakes_fabrication_interview
stage_4:
  - no_questions_full_ai_validation_packaging
  - low_stakes_finalization_interview
  - medium_stakes_finalization_interview
  - high_stakes_finalization_interview
```
