---
domain: Spreadsheet Functions
category: Diagrams
subcategory: Overview
purpose:
  - Function Relationships
use-case:
  - Checking Platform Availability
  - Migrating Excel-Only Formulas
related:
  - ARRAYTOTEXT
  - AVERAGE
  - BYCOL
  - CELL
  - CHOOSECOLS
  - CHOOSEROWS
  - CUMIPMT
  - CUMPRINC
  - DROP
  - ENCODEURL
  - EXPAND
  - FILTERXML
  - FVSCHEDULE
  - IF
  - IFERROR
  - INFO
  - LAMBDA
  - MAKEARRAY
  - MAP
  - PDURATION
  - RANDARRAY
  - REDUCE
  - RRI
  - SCAN
  - SEQUENCE
  - SORT
  - SORTBY
  - STOCKHISTORY
  - SUM
  - TEXTAFTER
  - TEXTBEFORE
  - TEXTJOIN
  - TOCOL
  - TOROW
  - VALUETOTEXT
  - VDB
  - VSTACK
  - WEBSERVICE
  - WRAPCOLS
  - WRAPROWS
level: 3
source:
  - https://support.microsoft.com/en-us/office/excel-functions-by-category-5f91f4e9-7b42-46d2-9bd1-63f26a86c0eb
  - https://support.google.com/docs/table/25273
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - diagrams
  - arrays
  - excel
  - platform-availability
---

# Excel-Specific Functions Relationship Diagram

This diagram groups functions that were once treated as Excel-specific. Each function now lives in its official category, listed in the table below. The grouping is kept here for reference.

| Folder | Functions |
| --- | --- |
| `Functions/Financial` | CUMIPMT, CUMPRINC, FVSCHEDULE, PDURATION, RRI, VDB |
| `Functions/Information` | CELL, INFO, STOCKHISTORY |
| `Functions/Logical` | BYCOL, BYROW, LAMBDA, MAKEARRAY, MAP, REDUCE, SCAN |
| `Functions/Lookup & Reference` | CHOOSECOLS, CHOOSEROWS, DROP, EXPAND, HSTACK, SORT, SORTBY, TOCOL, TOROW, VSTACK, WRAPCOLS, WRAPROWS |
| `Functions/Math & Trig` | RANDARRAY, SEQUENCE |
| `Functions/Text` | ARRAYTOTEXT, TEXTAFTER, TEXTBEFORE, TEXTJOIN, TEXTSPLIT, VALUETOTEXT |
| `Functions/Web` | ENCODEURL, FILTERXML, WEBSERVICE |

27 of the 39 functions also work in Google Sheets. Excel only: ARRAYTOTEXT, DROP, EXPAND, FILTERXML, INFO, SORTBY, STOCKHISTORY, TEXTAFTER, TEXTBEFORE, TEXTSPLIT, VALUETOTEXT, WEBSERVICE.

```mermaid
graph LR
    classDef ExcelSpecific fill:#6C5CE7,stroke:#333,stroke-width:2px,color:#000
    TOCOL["TOCOL<br/>Returns an array or range as a single column"]
    CUMIPMT["CUMIPMT<br/>Returns cumulative interest paid between two periods"]
    FILTERXML["FILTERXML<br/>Returns data from XML content using an XPath"]
    SCAN["SCAN<br/>Returns running intermediate results of a LAMBDA over an array"]
    TEXTAFTER["TEXTAFTER<br/>Returns text that occurs after a given character or string"]
    MAP["MAP<br/>Maps each value in one or more arrays with a LAMBDA"]
    TEXTJOIN["TEXTJOIN<br/>Combines text from multiple ranges with a delimiter"]
    WEBSERVICE["WEBSERVICE<br/>Returns data from a web service"]
    FVSCHEDULE["FVSCHEDULE<br/>Returns future value after a series of interest rates"]
    EXPAND["EXPAND<br/>Expands or pads an array to specified dimensions"]
    DROP["DROP<br/>Excludes a number of rows or columns from an array"]
    WRAPROWS["WRAPROWS<br/>Wraps a row or column of values into rows of a set size"]
    ENCODEURL["ENCODEURL<br/>Returns a URL-encoded string"]
    RRI["RRI<br/>Returns an equivalent interest rate for investment growth"]
    TEXTBEFORE["TEXTBEFORE<br/>Returns text that occurs before a given character or string"]
    INFO["INFO<br/>Returns information about the current operating environment"]
    WRAPCOLS["WRAPCOLS<br/>Wraps a row or column of values into columns of a set size"]
    SORTBY["SORTBY<br/>Sorts a range or array by values in a corresponding range"]
    TOROW["TOROW<br/>Returns an array or range as a single row"]
    VDB["VDB<br/>Returns depreciation for a specified or partial period"]
    CHOOSECOLS["CHOOSECOLS<br/>Returns the specified columns from an array"]
    STOCKHISTORY["STOCKHISTORY<br/>Retrieves historical data for a financial instrument"]
    VSTACK["VSTACK<br/>Appends arrays vertically to return a larger array"]
    BYCOL["BYCOL<br/>Applies a LAMBDA to each column and returns the results"]
    REDUCE["REDUCE<br/>Reduces an array to a single value with a LAMBDA"]
    RANDARRAY["RANDARRAY<br/>Returns an array of random numbers"]
    CHOOSEROWS["CHOOSEROWS<br/>Returns the specified rows from an array"]
    CUMPRINC["CUMPRINC<br/>Returns cumulative principal paid between two periods"]
    VALUETOTEXT["VALUETOTEXT<br/>Returns text from any specified value"]
    PDURATION["PDURATION<br/>Returns the periods needed for an investment to reach a value"]
    ARRAYTOTEXT["ARRAYTOTEXT<br/>Returns a text version of an array or range"]
    MAKEARRAY["MAKEARRAY<br/>Returns an array of a set size built by a LAMBDA"]
    SEQUENCE["SEQUENCE<br/>Generates a list of sequential numbers in an array"]
    LAMBDA["LAMBDA<br/>Creates custom, reusable functions without using VBA"]
    SORT["SORT<br/>Sorts the contents of a range or array"]
    CELL["CELL<br/>Returns information about a cell format, location or contents"]
    BYROW["BYROW<br/>Applies a LAMBDA to each row and returns the results"]
    TEXTSPLIT["TEXTSPLIT<br/>Splits text strings using column and row delimiters"]
    HSTACK["HSTACK<br/>Appends arrays horizontally to return a larger array"]
    IF["IF<br/>External Function"]
    TOCOL --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TOCOL --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TOCOL --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    TOCOL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    TOCOL -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CUMIPMT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CUMIPMT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CUMIPMT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    CUMIPMT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    CUMIPMT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FILTERXML --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FILTERXML --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    FILTERXML --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    FILTERXML -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    FILTERXML -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SCAN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SCAN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    SCAN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    SCAN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    SCAN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TEXTAFTER --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TEXTAFTER --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TEXTAFTER --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    TEXTAFTER -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    TEXTAFTER -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MAP --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    MAP --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    MAP --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    MAP -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    MAP -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TEXTJOIN --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TEXTJOIN --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TEXTJOIN --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    TEXTJOIN -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    TEXTJOIN -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    WEBSERVICE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    WEBSERVICE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    WEBSERVICE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    WEBSERVICE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    WEBSERVICE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    FVSCHEDULE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    FVSCHEDULE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    FVSCHEDULE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    FVSCHEDULE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    FVSCHEDULE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    EXPAND --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    EXPAND --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    EXPAND --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    EXPAND -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    EXPAND -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    DROP --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    DROP --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    DROP --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    DROP -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    DROP -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    WRAPROWS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    WRAPROWS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    WRAPROWS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    WRAPROWS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    WRAPROWS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ENCODEURL --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ENCODEURL --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ENCODEURL --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    ENCODEURL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    ENCODEURL -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    RRI --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    RRI --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    RRI --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    RRI -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    RRI -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TEXTBEFORE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TEXTBEFORE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TEXTBEFORE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    TEXTBEFORE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    TEXTBEFORE -.-> IFERROR
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
    IF["IF<br/>External Function"]
    INFO -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    INFO -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    WRAPCOLS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    WRAPCOLS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    WRAPCOLS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    WRAPCOLS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    WRAPCOLS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SORTBY --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SORTBY --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    SORTBY --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    SORTBY -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    SORTBY -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TOROW --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TOROW --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TOROW --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    TOROW -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    TOROW -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    VDB --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    VDB --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    VDB --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    VDB -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    VDB -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CHOOSECOLS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CHOOSECOLS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CHOOSECOLS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    CHOOSECOLS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    CHOOSECOLS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    STOCKHISTORY --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    STOCKHISTORY --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    STOCKHISTORY --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    STOCKHISTORY -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    STOCKHISTORY -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    VSTACK --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    VSTACK --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    VSTACK --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    VSTACK -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    VSTACK -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BYCOL --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BYCOL --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BYCOL --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    BYCOL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    BYCOL -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    REDUCE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    REDUCE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    REDUCE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    REDUCE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    REDUCE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    RANDARRAY --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    RANDARRAY --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    RANDARRAY --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    RANDARRAY -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    RANDARRAY -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CHOOSEROWS --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CHOOSEROWS --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CHOOSEROWS --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    CHOOSEROWS -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    CHOOSEROWS -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    CUMPRINC --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    CUMPRINC --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    CUMPRINC --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    CUMPRINC -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    CUMPRINC -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    VALUETOTEXT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    VALUETOTEXT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    VALUETOTEXT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    VALUETOTEXT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    VALUETOTEXT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    PDURATION --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    PDURATION --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    PDURATION --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    PDURATION -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    PDURATION -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    ARRAYTOTEXT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    ARRAYTOTEXT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    ARRAYTOTEXT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    ARRAYTOTEXT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    ARRAYTOTEXT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    MAKEARRAY --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    MAKEARRAY --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    MAKEARRAY --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    MAKEARRAY -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    MAKEARRAY -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SEQUENCE --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SEQUENCE --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    SEQUENCE --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    SEQUENCE -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    SEQUENCE -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    LAMBDA --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    LAMBDA --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    LAMBDA --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    LAMBDA -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    LAMBDA -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    SORT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    SORT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    SORT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    SORT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    SORT -.-> IFERROR
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
    IF["IF<br/>External Function"]
    CELL -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    CELL -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    BYROW --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    BYROW --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    BYROW --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    BYROW -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    BYROW -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    TEXTSPLIT --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    TEXTSPLIT --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    TEXTSPLIT --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    TEXTSPLIT -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    TEXTSPLIT -.-> IFERROR
    class IFERROR external
    IF["IF<br/>External Function"]
    HSTACK --> IF
    class IF external
    SUM["SUM<br/>External Function"]
    HSTACK --> SUM
    class SUM external
    AVERAGE["AVERAGE<br/>External Function"]
    HSTACK --> AVERAGE
    class AVERAGE external
    IF["IF<br/>External Function"]
    HSTACK -.-> IF
    class IF external
    IFERROR["IFERROR<br/>External Function"]
    HSTACK -.-> IFERROR
    class IFERROR external
    class TOCOL ExcelSpecific
    class CUMIPMT ExcelSpecific
    class FILTERXML ExcelSpecific
    class SCAN ExcelSpecific
    class TEXTAFTER ExcelSpecific
    class MAP ExcelSpecific
    class TEXTJOIN ExcelSpecific
    class WEBSERVICE ExcelSpecific
    class FVSCHEDULE ExcelSpecific
    class EXPAND ExcelSpecific
    class DROP ExcelSpecific
    class WRAPROWS ExcelSpecific
    class ENCODEURL ExcelSpecific
    class RRI ExcelSpecific
    class TEXTBEFORE ExcelSpecific
    class INFO ExcelSpecific
    class WRAPCOLS ExcelSpecific
    class SORTBY ExcelSpecific
    class TOROW ExcelSpecific
    class VDB ExcelSpecific
    class CHOOSECOLS ExcelSpecific
    class STOCKHISTORY ExcelSpecific
    class VSTACK ExcelSpecific
    class BYCOL ExcelSpecific
    class REDUCE ExcelSpecific
    class RANDARRAY ExcelSpecific
    class CHOOSEROWS ExcelSpecific
    class CUMPRINC ExcelSpecific
    class VALUETOTEXT ExcelSpecific
    class PDURATION ExcelSpecific
    class ARRAYTOTEXT ExcelSpecific
    class MAKEARRAY ExcelSpecific
    class SEQUENCE ExcelSpecific
    class LAMBDA ExcelSpecific
    class SORT ExcelSpecific
    class CELL ExcelSpecific
    class BYROW ExcelSpecific
    class TEXTSPLIT ExcelSpecific
    class HSTACK ExcelSpecific
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
```

## Legend
- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (`-.->`)**: "Similar functions" relationships
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in This Diagram: 39
