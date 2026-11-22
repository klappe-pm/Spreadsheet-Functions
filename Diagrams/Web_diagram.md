---
domain: Spreadsheet Functions
category: Diagrams
subcategory: Web
purpose:
  - Function Relationships
use-case:
  - Importing Web Data
  - Summarizing Imported Data
related:
  - AVERAGE
  - IF
  - IFERROR
  - IMPORTJSON
  - SUM
level: 2
source:
  - https://support.microsoft.com/en-us/office/excel-functions-by-category-5f91f4e9-7b42-46d2-9bd1-63f26a86c0eb
  - https://support.google.com/docs/table/25273
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - diagrams
  - data-import
  - web
---

# Web Functions Relationship Diagram

This diagram shows the relationships between functions in the Web category and their connections to commonly used functions. It shows 1 of the 12 Web functions.

```mermaid
graph TD
    classDef Web fill:#00B894,stroke:#333,stroke-width:2px,color:#000
    IMPORTJSON["IMPORTJSON<br/>Apps Script custom function (not built in)"]
    IF["IF<br/>External Function"]
    IMPORTJSON --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    IMPORTJSON --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    IMPORTJSON --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    IMPORTJSON -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    IMPORTJSON -.-> IFERROR
    class IFERROR external
    class IMPORTJSON Web
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```

## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows** (`-.->`): "Similar functions" relationships
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in This Category: 12
