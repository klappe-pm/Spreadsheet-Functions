---
domain: Spreadsheet Functions
category: Diagrams
subcategory: Information
purpose:
  - Function Relationships
use-case:
  - Checking Data Types
  - Detecting Errors
  - Reading Cell and Sheet Details
related:
  - AVERAGE
  - CELL
  - ERROR.TYPE
  - FIELDVALUE
  - GET.CELL
  - GET.WORKBOOK
  - IF
  - IFERROR
  - INFO
  - ISBLANK
  - ISERR
  - ISERROR
  - ISEVEN
  - ISFORMULA
  - ISLOGICAL
  - ISNA
  - ISNONTEXT
  - ISNUMBER
  - ISODD
  - ISTEXT
  - "N"
  - NA
  - SHEET
  - SHEETS
  - SUM
  - TYPE
level: 2
source:
  - https://support.microsoft.com/en-us/office/excel-functions-by-category-5f91f4e9-7b42-46d2-9bd1-63f26a86c0eb
  - https://support.google.com/docs/table/25273
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - diagrams
  - data-types
  - error-checking
  - information
  - reference-info
---

# Information Functions Relationship Diagram

This diagram shows the relationships between functions in the Information category and their connections to commonly used functions. It shows 21 of the 26 Information functions. FIELDVALUE belongs to Lookup & Reference.

```mermaid
graph TD
    classDef Information fill:#5F27CD,stroke:#333,stroke-width:2px,color:#000
    ISBLANK["ISBLANK<br/>Tests whether a cell is empty"]
    GET_WORKBOOK["GET.WORKBOOK<br/>Legacy Excel 4.0 macro function for workbook details"]
    FIELDVALUE["FIELDVALUE<br/>Returns a field from a linked data type in Excel"]
    ISNUMBER["ISNUMBER<br/>Tests whether a value is a number"]
    SHEET["SHEET<br/>Returns the sheet number of a reference"]
    ISLOGICAL["ISLOGICAL<br/>Tests whether a value is TRUE or FALSE"]
    ISFORMULA["ISFORMULA<br/>Tests whether a cell contains a formula"]
    ISTEXT["ISTEXT<br/>Tests whether a value is text"]
    ISNA["ISNA<br/>Tests whether a value is the #N/A error"]
    INFO["INFO<br/>Returns information about the operating environment"]
    N["N<br/>Converts a value to a number"]
    NA["NA<br/>Returns the #N/A error value"]
    ERROR_TYPE["ERROR.TYPE<br/>Returns a number that identifies an error type"]
    ISNONTEXT["ISNONTEXT<br/>Tests whether a value is not text"]
    SHEETS["SHEETS<br/>Returns the number of sheets in a reference"]
    GET_CELL["GET.CELL<br/>Legacy Excel 4.0 macro function for cell details"]
    ISERR["ISERR<br/>Tests whether a value is an error other than #N/A"]
    ISERROR["ISERROR<br/>Tests whether a value is any error, including #N/A"]
    ISEVEN["ISEVEN<br/>Tests whether a number is even"]
    ISODD["ISODD<br/>Tests whether a number is odd"]
    TYPE["TYPE<br/>Returns a number that identifies a value's data type"]
    CELL["CELL<br/>Returns information about a cell's format, location or contents"]
    IF["IF<br/>External Function"]
    ISBLANK --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ISBLANK --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ISBLANK --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ISBLANK -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ISBLANK -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    GET_WORKBOOK --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    GET_WORKBOOK --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    GET_WORKBOOK --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    GET_WORKBOOK -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    GET_WORKBOOK -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FIELDVALUE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FIELDVALUE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    FIELDVALUE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    FIELDVALUE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    FIELDVALUE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ISNUMBER --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ISNUMBER --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ISNUMBER --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ISNUMBER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ISNUMBER -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SHEET --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SHEET --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    SHEET --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SHEET -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SHEET -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ISLOGICAL --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ISLOGICAL --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ISLOGICAL --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ISLOGICAL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ISLOGICAL -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ISFORMULA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ISFORMULA --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ISFORMULA --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ISFORMULA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ISFORMULA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ISTEXT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ISTEXT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ISTEXT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ISTEXT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ISTEXT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ISNA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ISNA --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ISNA --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ISNA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ISNA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    INFO --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    INFO --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    INFO --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    INFO -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    INFO -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    N --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    N --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    N --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    N -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    N -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    NA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    NA --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    NA --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    NA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    NA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ERROR_TYPE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ERROR_TYPE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ERROR_TYPE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ERROR_TYPE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ERROR_TYPE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ISNONTEXT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ISNONTEXT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ISNONTEXT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ISNONTEXT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ISNONTEXT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SHEETS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SHEETS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    SHEETS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    SHEETS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    SHEETS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    GET_CELL --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    GET_CELL --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    GET_CELL --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    GET_CELL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    GET_CELL -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ISERR --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ISERR --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ISERR --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ISERR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ISERR -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ISERROR --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ISERROR --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ISERROR --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ISERROR -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ISERROR -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ISEVEN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ISEVEN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ISEVEN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ISEVEN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ISEVEN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ISODD --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ISODD --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ISODD --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    ISODD -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    ISODD -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TYPE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TYPE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TYPE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    TYPE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    TYPE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CELL --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CELL --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CELL --> AVERAGE
    class AVERAGE external
    IF["IF<br/>Related Function"]
    CELL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>Related Function"]
    CELL -.-> IFERROR
    class IFERROR external
    class ISBLANK Information
    class GET_WORKBOOK Information
    class FIELDVALUE Information
    class ISNUMBER Information
    class SHEET Information
    class ISLOGICAL Information
    class ISFORMULA Information
    class ISTEXT Information
    class ISNA Information
    class INFO Information
    class N Information
    class NA Information
    class ERROR_TYPE Information
    class ISNONTEXT Information
    class SHEETS Information
    class GET_CELL Information
    class ISERR Information
    class ISERROR Information
    class ISEVEN Information
    class ISODD Information
    class TYPE Information
    class CELL Information
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```

## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows** (`-.->`): "Similar functions" relationships
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in This Category: 26
