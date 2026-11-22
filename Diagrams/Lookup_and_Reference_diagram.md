---
domain: Spreadsheet Functions
category: Diagrams
subcategory: Lookup & Reference
purpose:
  - Function Relationships
use-case:
  - Choosing a Lookup Function
  - Returning Ranges and Arrays
related:
  - ADDRESS
  - AREAS
  - AVERAGE
  - CHOOSE
  - CHOOSECOLS
  - CHOOSEROWS
  - COLUMN
  - COLUMNS
  - DROP
  - EXPAND
  - FILTER
  - FIND
  - GETPIVOTDATA
  - HLOOKUP
  - HSTACK
  - HYPERLINK
  - IF
  - IFERROR
  - INDEX
  - INDIRECT
  - LOOKUP
  - MATCH
  - MAX
  - OFFSET
  - ROW
  - ROWS
  - SMALL
  - SUM
  - TAKE
  - TRANSPOSE
  - VLOOKUP
  - VSTACK
  - WRAPCOLS
  - WRAPROWS
  - XLOOKUP
  - XMATCH
level: 3
source:
  - https://support.microsoft.com/en-us/office/excel-functions-by-category-5f91f4e9-7b42-46d2-9bd1-63f26a86c0eb
  - https://support.google.com/docs/table/25273
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - diagrams
  - excel
  - google-sheets
  - lookup
---

# Lookup and Reference Functions Relationship Diagram

This diagram shows the relationships between functions in the Lookup & Reference category and their connections to commonly used functions. It shows 29 of the category's functions.

```mermaid
graph TD
    classDef LookupReference fill:#FECA57,stroke:#333,stroke-width:2px,color:#000
    classDef external fill:#f9f9f9,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
    TAKE["TAKE<br/>Returns rows or columns from the start or end of an array"]
    FILTER["FILTER<br/>Returns the rows or columns that meet specified conditions"]
    XLOOKUP["XLOOKUP<br/>Searches a range and returns the matching item from another range"]
    COLUMNS["COLUMNS<br/>Returns the number of columns in a range or array"]
    INDIRECT["INDIRECT<br/>Returns the reference named by a text string"]
    TRANSPOSE["TRANSPOSE<br/>Swaps the rows and columns of a range or array"]
    EXPAND["EXPAND<br/>Enlarges an array to more rows and columns"]
    MATCH["MATCH<br/>Returns the relative position of a value in a range"]
    DROP["DROP<br/>Removes rows or columns from the start or end of an array"]
    COLUMN["COLUMN<br/>Returns the column number of a cell"]
    WRAPROWS["WRAPROWS<br/>Reshapes a single row or column into rows of a set length"]
    XMATCH["XMATCH<br/>Returns the relative position of an item in a range or array"]
    ROWS["ROWS<br/>Returns the number of rows in a range or array"]
    WRAPCOLS["WRAPCOLS<br/>Reshapes a single row or column into columns of a set length"]
    ROW["ROW<br/>Returns the row number of a cell or range"]
    CHOOSECOLS["CHOOSECOLS<br/>Returns a new array made of the columns you name"]
    CHOOSE["CHOOSE<br/>Returns one value from a list, selected by position number"]
    VSTACK["VSTACK<br/>Joins arrays one below the other"]
    INDEX["INDEX<br/>Returns the value at a specified row and column position"]
    ADDRESS["ADDRESS<br/>Returns a cell reference as text from row and column numbers"]
    CHOOSEROWS["CHOOSEROWS<br/>Returns a new array made of the rows you name"]
    OFFSET["OFFSET<br/>Returns a reference offset a set number of rows and columns"]
    HLOOKUP["HLOOKUP<br/>Searches the top row of a table and returns a value from a row"]
    VLOOKUP["VLOOKUP<br/>Searches the first column of a range and returns a matching row value"]
    GETPIVOTDATA["GETPIVOTDATA<br/>Returns a summarized value from a PivotTable"]
    AREAS["AREAS<br/>Returns the number of areas in a reference"]
    LOOKUP["LOOKUP<br/>Searches a single row or column and returns a matching value"]
    HYPERLINK["HYPERLINK<br/>Creates a clickable link in a cell"]
    HSTACK["HSTACK<br/>Joins arrays side by side, column by column"]
    IF["IF<br/>Returns one value if a condition is TRUE, another if FALSE"]
    SUM["SUM<br/>Adds numbers"]
    AVERAGE["AVERAGE<br/>Returns the arithmetic mean of its numeric arguments"]
    IFERROR["IFERROR<br/>Returns a replacement value when a formula returns an error"]
    FIND["FIND<br/>Finds one text string inside another"]
    MAX["MAX<br/>Returns the largest number in a set of values"]
    SMALL["SMALL<br/>Returns the k-th smallest value in a set of numbers"]
    TAKE --> IF
    TAKE --> SUM
    TAKE --> AVERAGE
    TAKE -.-> IF
    TAKE -.-> IFERROR
    FILTER --> IF
    FILTER --> SUM
    FILTER --> AVERAGE
    FILTER -.-> IF
    FILTER -.-> IFERROR
    XLOOKUP --> IF
    XLOOKUP --> SUM
    XLOOKUP --> AVERAGE
    XLOOKUP -.-> IF
    XLOOKUP -.-> IFERROR
    COLUMNS --> IF
    COLUMNS --> SUM
    COLUMNS --> AVERAGE
    COLUMNS -.-> IF
    COLUMNS -.-> IFERROR
    INDIRECT --> IF
    INDIRECT --> SUM
    INDIRECT --> AVERAGE
    INDIRECT -.-> IF
    INDIRECT -.-> IFERROR
    TRANSPOSE --> IF
    TRANSPOSE --> SUM
    TRANSPOSE --> AVERAGE
    TRANSPOSE -.-> IF
    TRANSPOSE -.-> IFERROR
    EXPAND --> IF
    EXPAND --> SUM
    EXPAND --> AVERAGE
    EXPAND -.-> IF
    EXPAND -.-> IFERROR
    MATCH --> INDEX
    MATCH --> IF
    MATCH --> MAX
    MATCH -.-> INDEX
    MATCH -.-> FIND
    DROP --> IF
    DROP --> SUM
    DROP --> AVERAGE
    DROP -.-> IF
    DROP -.-> IFERROR
    COLUMN --> IF
    COLUMN --> SUM
    COLUMN --> AVERAGE
    COLUMN -.-> IF
    COLUMN -.-> IFERROR
    WRAPROWS --> IF
    WRAPROWS --> SUM
    WRAPROWS --> AVERAGE
    WRAPROWS -.-> IF
    WRAPROWS -.-> IFERROR
    XMATCH --> IF
    XMATCH --> SUM
    XMATCH --> AVERAGE
    XMATCH -.-> IF
    XMATCH -.-> IFERROR
    ROWS --> IF
    ROWS --> SUM
    ROWS --> AVERAGE
    ROWS -.-> IF
    ROWS -.-> IFERROR
    WRAPCOLS --> IF
    WRAPCOLS --> SUM
    WRAPCOLS --> AVERAGE
    WRAPCOLS -.-> IF
    WRAPCOLS -.-> IFERROR
    ROW --> IF
    ROW --> SUM
    ROW --> AVERAGE
    ROW -.-> IF
    ROW -.-> IFERROR
    CHOOSECOLS --> IF
    CHOOSECOLS --> SUM
    CHOOSECOLS --> AVERAGE
    CHOOSECOLS -.-> IF
    CHOOSECOLS -.-> IFERROR
    CHOOSE --> IF
    CHOOSE --> SUM
    CHOOSE --> AVERAGE
    CHOOSE -.-> IF
    CHOOSE -.-> IFERROR
    VSTACK --> IF
    VSTACK --> SUM
    VSTACK --> AVERAGE
    VSTACK -.-> IF
    VSTACK -.-> IFERROR
    INDEX --> MATCH
    INDEX --> IF
    INDEX --> SMALL
    INDEX -.-> MATCH
    INDEX -.-> OFFSET
    ADDRESS --> IF
    ADDRESS --> SUM
    ADDRESS --> AVERAGE
    ADDRESS -.-> IF
    ADDRESS -.-> IFERROR
    CHOOSEROWS --> IF
    CHOOSEROWS --> SUM
    CHOOSEROWS --> AVERAGE
    CHOOSEROWS -.-> IF
    CHOOSEROWS -.-> IFERROR
    OFFSET --> IF
    OFFSET --> SUM
    OFFSET --> AVERAGE
    OFFSET -.-> IF
    OFFSET -.-> IFERROR
    HLOOKUP --> IF
    HLOOKUP --> SUM
    HLOOKUP --> AVERAGE
    HLOOKUP -.-> IF
    HLOOKUP -.-> IFERROR
    VLOOKUP --> IF
    VLOOKUP --> IFERROR
    VLOOKUP --> MATCH
    VLOOKUP -.-> HLOOKUP
    VLOOKUP -.-> INDEX
    GETPIVOTDATA --> IF
    GETPIVOTDATA --> SUM
    GETPIVOTDATA --> AVERAGE
    GETPIVOTDATA -.-> IF
    GETPIVOTDATA -.-> IFERROR
    AREAS --> IF
    AREAS --> SUM
    AREAS --> AVERAGE
    AREAS -.-> IF
    AREAS -.-> IFERROR
    LOOKUP --> IF
    LOOKUP --> SUM
    LOOKUP --> AVERAGE
    LOOKUP -.-> IF
    LOOKUP -.-> IFERROR
    HYPERLINK --> IF
    HYPERLINK --> SUM
    HYPERLINK --> AVERAGE
    HYPERLINK -.-> IF
    HYPERLINK -.-> IFERROR
    HSTACK --> IF
    HSTACK --> SUM
    HSTACK --> AVERAGE
    HSTACK -.-> IF
    HSTACK -.-> IFERROR
    class TAKE,FILTER,XLOOKUP,COLUMNS,INDIRECT,TRANSPOSE,EXPAND,MATCH,DROP,COLUMN,WRAPROWS,XMATCH,ROWS,WRAPCOLS,ROW,CHOOSECOLS,CHOOSE,VSTACK,INDEX,ADDRESS,CHOOSEROWS,OFFSET,HLOOKUP,VLOOKUP,GETPIVOTDATA,AREAS,LOOKUP,HYPERLINK,HSTACK LookupReference
    class IF,SUM,AVERAGE,IFERROR,FIND,MAX,SMALL external
```

## Legend

- **Solid arrows (→)**: "Commonly used with" relationships
- **Dashed arrows (-.->)**: "Similar functions" relationships
- **Colored nodes**: Functions in this category
- **Gray dashed nodes**: External functions from other categories

## Functions in This Category: 41
