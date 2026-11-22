---
domain: Spreadsheet Functions
category: Diagrams
subcategory: Cube
purpose:
  - Function Relationships
use-case:
  - Querying OLAP Cubes
  - Building KPI Reports
related:
  - AVERAGE
  - CUBEKPIMEMBER
  - CUBEMEMBER
  - CUBEMEMBERPROPERTY
  - CUBERANKEDMEMBER
  - CUBESET
  - CUBESETCOUNT
  - CUBEVALUE
  - IF
  - IFERROR
  - SUM
level: 4
source:
  - https://support.microsoft.com/en-us/office/excel-functions-by-category-5f91f4e9-7b42-46d2-9bd1-63f26a86c0eb
  - https://support.google.com/docs/table/25273
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - diagrams
  - cube
  - olap
---

# Cube Functions Relationship Diagram

This diagram shows the relationships between functions in the Cube category and their connections to commonly used functions.

```mermaid
graph TD
    classDef Cube fill:#E17055,stroke:#333,stroke-width:2px,color:#000
    CUBERANKEDMEMBER["CUBERANKEDMEMBER<br/>Returns the nth ranked member in a set"]
    CUBEMEMBER["CUBEMEMBER<br/>Returns a member or tuple from a cube hierarchy"]
    CUBESET["CUBESET<br/>Defines a calculated set of members or tuples"]
    CUBESETCOUNT["CUBESETCOUNT<br/>Returns the number of items in a set"]
    CUBEKPIMEMBER["CUBEKPIMEMBER<br/>Returns a KPI name, property and measure from a cube"]
    CUBEVALUE["CUBEVALUE<br/>Returns an aggregated value from a cube"]
    CUBEMEMBERPROPERTY["CUBEMEMBERPROPERTY<br/>Returns the value of a member property from a cube"]
    IF["IF<br/>External Function"]
    CUBERANKEDMEMBER --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CUBERANKEDMEMBER --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CUBERANKEDMEMBER --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    CUBERANKEDMEMBER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    CUBERANKEDMEMBER -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CUBEMEMBER --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CUBEMEMBER --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CUBEMEMBER --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    CUBEMEMBER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    CUBEMEMBER -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CUBESET --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CUBESET --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CUBESET --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    CUBESET -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    CUBESET -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CUBESETCOUNT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CUBESETCOUNT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CUBESETCOUNT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    CUBESETCOUNT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    CUBESETCOUNT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CUBEKPIMEMBER --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CUBEKPIMEMBER --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CUBEKPIMEMBER --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    CUBEKPIMEMBER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    CUBEKPIMEMBER -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CUBEVALUE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CUBEVALUE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CUBEVALUE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    CUBEVALUE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    CUBEVALUE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CUBEMEMBERPROPERTY --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CUBEMEMBERPROPERTY --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CUBEMEMBERPROPERTY --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    CUBEMEMBERPROPERTY -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    CUBEMEMBERPROPERTY -.-> IFERROR
    class IFERROR external
    class CUBERANKEDMEMBER Cube
    class CUBEMEMBER Cube
    class CUBESET Cube
    class CUBESETCOUNT Cube
    class CUBEKPIMEMBER Cube
    class CUBEVALUE Cube
    class CUBEMEMBERPROPERTY Cube
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```


## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (`-.->`)**: "Similar functions" relationships
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in This Category: 7
