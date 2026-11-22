---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Reference Building
purpose:
  - Reference Building
use-case:
  - Column Position Lookups
  - Formula Column Offsets
  - Template Column Labels
related:
  - ADDRESS
  - COLUMNS
  - INDEX
  - ROW
  - ROWS
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/column-function
  - https://support.google.com/docs/answer/3093373
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Column Number
  - Column Position
tags:
  - column-number
  - excel
  - reference-building
  - sheets
---

# COLUMN

## Description

**COLUMN** returns the column number of a cell. Column A is 1, column B is 2, column Z is 26, and column AA is 27. With no argument, COLUMN returns the number of the column that holds the formula.

Use COLUMN when a formula needs a column position rather than a value. Common uses are offsetting from a starting column, passing a column number to INDEX or ADDRESS, and numbering the columns of a template. COLUMN returns a position only; it does not read the cell's contents.

When the reference is a range wider than one cell, the result depends on how the formula is entered. In Microsoft Excel, the page says that a formula entered as a horizontal array returns one column number per cell, and that otherwise the leftmost column is returned. In current Microsoft 365 versions, a formula entered normally in the top-left cell of the output range fills the row, so it returns the array. The reference cannot cover more than one area.

## Syntax

```excel
=COLUMN([reference])
```

<!-- Image 1: Column Number Positions. See Images/Lookup & Reference/COLUMN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `reference` | No | The cell or range whose column number you want. If it is omitted, COLUMN uses the cell that holds the formula. It cannot cover more than one area. |

### Return Value

A whole number: the column number of the cell, where column A is 1. For a range, Excel returns the column number of the leftmost column, or a row of column numbers when the formula is entered as a horizontal array.

## Examples

### Example 1: Column of a Cell

```excel
=COLUMN(F3)
```

**Result:** `6`

Column F is the sixth letter of the alphabet, so the result is 6. The row number 3 does not affect the result.

### Example 2: Column of the Formula Cell

```excel
=COLUMN()
```

**Result:** `5` when the formula is in cell E1

With no argument, COLUMN reports the column of its own cell, which is column E here.

### Example 3: Column Numbers Across a Range

```excel
=COLUMN(B2:D2)
```

**Result:** `2`, `3` and `4` across three cells in Microsoft 365

Entered as a horizontal array, the formula returns one column number for each column in the range, so it spills across three cells. A formula entered as a single-cell formula in older versions returns only the leftmost number, 2.

### Example 4: Offsetting From a Column

```excel
=COLUMN(A1) + 2
```

**Result:** `3`

Adding 2 moves the position forward by two columns, so the result is column C.

<!-- Image 2: Column Offset Map. See Images/Lookup & Reference/COLUMN.md -->

### Example 5: Using the Column as an Index

```excel
=INDEX($A$2:$H$2, COLUMN(F1))
```

**Result:** the value in cell F2

COLUMN(F1) returns 6, and INDEX returns the sixth value of the range A2:H2, which is the value in F2.

## Story Problems

### Problem 1: Adding Two Column Positions

A report sheet has its headers in row 1. The header Region is in cell A1, Units is in D1 and Price is in G1.

| Header | Cell |
| --- | --- |
| Region | A1 |
| Units | D1 |
| Price | G1 |

**Task:** Add the column numbers of the Units and Price headers.

**Solution:**

```excel
=COLUMN(D1) + COLUMN(G1)
```

**Answer:** `11`. Units is in column 4, Price is in column 7, and 4 + 7 is 11.

### Problem 2: Month Number From a Column

A budget sheet puts January in column B, February in column C and so on across the row. The month number for any column is its position from column B.

| Month | Column |
| --- | --- |
| January | B |
| February | C |
| March | D |

**Task:** In the cell for March, which is column D, return the month number.

**Solution:**

```excel
=COLUMN() - COLUMN($B$1) + 1
```

**Answer:** `3`. COLUMN() is 4 for column D, COLUMN($B$1) is 2, and `4 - 2 + 1` is 3.

## Use Cases

### Column Position Lookups

**Scenario:** A summary row shows the first twelve values of a monthly data row. The summary copies across columns, and each copy must read the next month.

```excel
=INDEX(Figures!$B$2:$M$2, COLUMN() - 1)
```

**Why It Works:** Placed in column B of the summary, COLUMN() is 2, so the formula reads position 1. Copied into column C, it reads position 2, and so on across the row.

### Formula Column Offsets

**Scenario:** A sheet numbers its period columns from the first period column, so that the period count updates when columns are added.

```excel
=COLUMN() - COLUMN($A$1)
```

**Why It Works:** The absolute reference `$A$1` always returns 1, so the formula returns the number of columns to the right of column A, which is the period count when periods start in column B.

### Template Column Labels

**Scenario:** A data-entry template needs a visible code above each input column, such as "Column 4", that stays correct when columns are inserted.

```excel
="Column "&COLUMN()
```

**Why It Works:** The formula builds the label from the current column each time it is copied, so the codes always match the column positions.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unexpected number | The column letter is counted from the wrong place. | Column A is 1, so recount from A. |
| Result changes when copied | A relative reference such as `COLUMN(A1)` moves with the copy. | Use `COLUMN($A$1)` when the column must stay fixed. |
| Only one number returned | A range was entered as a single-cell formula in an older version. | Enter the formula as a horizontal array, or use Microsoft 365. |
| `#SPILL!` | The cells the array needs already contain data. | Clear the blocked cells. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, Excel 2019, Excel 2016, Microsoft Office and Office for iPhone | With a range, returns the leftmost column, or a row of column numbers when entered as a horizontal array. |
| Google Sheets | Available | The page states that a range that is not an array formula returns the position of the first column. |

## Tips and Best Practices

- Use `COLUMN(A1)` instead of a typed number when a formula must show which column it means.
- Use absolute references such as `$A$1` inside COLUMN when a formula is copied across columns.
- Use COLUMNS when you need the number of columns in a range rather than the position of one.
- Combine COLUMN with ADDRESS when a reference must be written as text from a computed column number.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ADDRESS](ADDRESS.md) | Builds a cell address as text from a row number and a column number. |
| [COLUMNS](COLUMNS.md) | Counts the columns in a range, the size measure rather than the position. |
| [INDEX](INDEX.md) | Returns a value by position, often using COLUMN to supply the column number. |
| [ROW](ROW.md) | Returns the row number, the vertical counterpart of this function. |
| [ROWS](ROWS.md) | Counts the rows in a range. |

## Official Documentation

- [Microsoft Support: COLUMN function](https://support.microsoft.com/en-us/excel/functions/column-function)
- [Google Docs Editors Help: COLUMN](https://support.google.com/docs/answer/3093373)
