---
domain: Spreadsheet Functions
category: Diagrams
subcategory: Database
purpose:
  - Function Relationships
use-case:
  - Summarizing Records With Criteria
  - Choosing a Database Function
related:
  - AVERAGE
  - DAVERAGE
  - DCOUNT
  - DCOUNTA
  - DGET
  - DMAX
  - DMIN
  - DPRODUCT
  - DSTDEV
  - DSTDEVP
  - DSUM
  - DVAR
  - DVARP
  - IF
  - IFERROR
  - SUM
level: 3
source:
  - https://support.microsoft.com/en-us/office/excel-functions-by-category-5f91f4e9-7b42-46d2-9bd1-63f26a86c0eb
  - https://support.google.com/docs/table/25273
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - diagrams
  - database
  - aggregation
  - criteria
---

# Database Functions Relationship Diagram

This diagram shows the relationships between functions in the Database category and their connections to commonly used functions.

```mermaid
graph TD
    classDef Database fill:#00D2D3,stroke:#333,stroke-width:2px,color:#000
    DSTDEVP["DSTDEVP<br/>Standard deviation of an entire population of matching records"]
    DPRODUCT["DPRODUCT<br/>Multiplies field values in records that match criteria"]
    DCOUNT["DCOUNT<br/>Counts numeric field values in records that match criteria"]
    DCOUNTA["DCOUNTA<br/>Counts nonblank field values in records that match criteria"]
    DAVERAGE["DAVERAGE<br/>Averages field values in records that match criteria"]
    DMAX["DMAX<br/>Largest field value in records that match criteria"]
    DVARP["DVARP<br/>Variance of an entire population of matching records"]
    DGET["DGET<br/>Returns the single field value of the one matching record"]
    DSUM["DSUM<br/>Adds field values in records that match criteria"]
    DSTDEV["DSTDEV<br/>Estimates standard deviation from a sample of matching records"]
    DMIN["DMIN<br/>Smallest field value in records that match criteria"]
    DVAR["DVAR<br/>Estimates variance from a sample of matching records"]
    IF["IF<br/>External Function"]
    DSTDEVP --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DSTDEVP --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DSTDEVP --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DSTDEVP -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DSTDEVP -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DPRODUCT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DPRODUCT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DPRODUCT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DPRODUCT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DPRODUCT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DCOUNT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DCOUNT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DCOUNT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DCOUNT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DCOUNT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DCOUNTA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DCOUNTA --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DCOUNTA --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DCOUNTA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DCOUNTA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DAVERAGE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DAVERAGE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DAVERAGE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DAVERAGE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DAVERAGE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DMAX --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DMAX --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DMAX --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DMAX -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DMAX -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DVARP --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DVARP --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DVARP --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DVARP -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DVARP -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DGET --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DGET --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DGET --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DGET -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DGET -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DSUM --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DSUM --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DSUM --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DSUM -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DSUM -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DSTDEV --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DSTDEV --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DSTDEV --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DSTDEV -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DSTDEV -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DMIN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DMIN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DMIN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DMIN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DMIN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DVAR --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DVAR --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DVAR --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    DVAR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    DVAR -.-> IFERROR
    class IFERROR external
    class DSTDEVP Database
    class DPRODUCT Database
    class DCOUNT Database
    class DCOUNTA Database
    class DAVERAGE Database
    class DMAX Database
    class DVARP Database
    class DGET Database
    class DSUM Database
    class DSTDEV Database
    class DMIN Database
    class DVAR Database
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```


## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (-.->)**: "Similar functions" relationships  
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions In This Category: 13
