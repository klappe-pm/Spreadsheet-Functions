---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Reference Building
purpose:
  - Counting
  - Reference Building
use-case:
  - Invoice Line Counts
  - Numbered Lists
  - Table Size Checks
related:
  - COLUMNS
  - COUNTA
  - FILTER
  - ROW
  - SEQUENCE
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/rows-function
  - https://support.google.com/docs/answer/3093382
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Count Rows
  - Row Count
tags:
  - counting
  - excel
  - lookup-reference
  - sheets
---

# ROWS

## Description

**ROWS** returns the number of rows in a range, a reference or an array. It counts every row in the argument, whether the cells are filled or empty, so it measures the size of a block rather than the number of records in it.

Use ROWS when a formula needs to know how tall a block is: to build a sequence the same length as a list, to check that two ranges line up, or to size a dynamic output. A range of 10 cells in one column returns 10. A range of 10 cells in two columns still returns 10, because ROWS counts only rows. Use COLUMNS for the width.

ROWS does not skip blank cells. If you want the number of filled entries, use COUNTA on the key column instead. If you want the number of rows that meet a condition, wrap the range in FILTER and pass the result to ROWS.

ROWS works the same way in Microsoft Excel and Google Sheets. Google Sheets counts null values as rows, just as Excel does.

## Syntax

```excel
=ROWS(array)
```

<!-- Image 1: Syntax Anatomy. See Images/Lookup & Reference/ROWS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | A cell range, a reference to a range, an array constant or the result of a formula that returns an array. The function returns the number of rows in it. |

### Return Value

A whole number: the count of rows in the argument. A single-row reference returns 1. The function does not return an error for blank cells, because blank cells are still rows.

## Examples

### Example 1: Count Rows in a Data Block

```excel
=ROWS(A2:D12)
```

**Result:** `11`

The block runs from row 2 to row 12, which is 11 rows. The four columns do not affect the count.

### Example 2: Count Items in an Array Constant

```excel
=ROWS({"Red";"Green";"Blue"})
```

**Result:** `3`

In an array constant, a semicolon starts a new row. This constant has three rows, so ROWS returns 3.

### Example 3: Count a Single Column Range

```excel
=ROWS(B5:B40)
```

**Result:** `36`

Rows 5 through 40 contain 40 minus 5 plus 1, or 36, rows.

### Example 4: Multiply Rows by Columns to Count Cells

```excel
=ROWS(A1:D10)*COLUMNS(A1:D10)
```

**Result:** `40`

ROWS returns 10 and COLUMNS returns 4. Their product is the number of cells in the block, whether or not the cells contain values.

<!-- Image 2: Counting Filtered Rows. See Images/Lookup & Reference/ROWS.md -->

## Story Problems

### Problem 1: Shipped Pallets

A warehouse lists pallets and their status in `A1:B9`. The first row is a header, and the remaining eight rows are pallets.

| Pallet | Status |
| --- | --- |
| P-01 | Shipped |
| P-02 | Waiting |
| P-03 | Shipped |
| P-04 | Shipped |
| P-05 | Waiting |
| P-06 | Shipped |
| P-07 | Waiting |
| P-08 | Shipped |

**Task:** Count the pallets that have shipped.

**Solution:**

```excel
=ROWS(FILTER(A2:B9, B2:B9="Shipped"))
```

**Answer:** `5`. Pallets P-01, P-03, P-04, P-06 and P-08 have the status Shipped.

### Problem 2: Entries Without the Header

A course roster in `A1:A13` has a header in row 1 and one name in each of rows 2 to 13.

**Task:** Count the names, leaving out the header.

**Solution:**

```excel
=ROWS(A1:A13)-1
```

**Answer:** `12`. The range has 13 rows, and subtracting the header leaves 12 names.

## Use Cases

### Invoice Line Counts

**Scenario:** An accounts team wants the number of line items on each invoice so it can flag invoices with unusually many lines.

```excel
=ROWS(Invoices[Line Item])
```

**Why It Works:** A structured reference to a table column grows and shrinks with the table, so ROWS always returns the current number of table rows. Blank rows inside the table are counted too.

### Numbered Lists

**Scenario:** A sheet needs a running number beside each entry in a list that changes length.

```excel
=SEQUENCE(ROWS(A2:A200))
```

**Why It Works:** ROWS sizes the sequence to match the source range, so the numbers stay aligned with the list when the range is resized to the same height.

### Table Size Checks

**Scenario:** A monthly import should contain exactly 500 rows. A check cell should warn when the import is a different size.

```excel
=IF(ROWS(Import!A2:A600)=500,"Size OK","Check import")
```

**Why It Works:** Comparing ROWS to an expected count catches exports that are shorter or longer than expected before the data feeds other formulas.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Count is one higher than expected | The range includes the header row. | Start the range below the header, or subtract 1. |
| Count is larger than the number of records | The range includes blank rows at the bottom. | Use COUNTA on the key column, or trim the range to the filled rows. |
| Count is 1 | The reference covers a single row, such as `A2:D2`. | Check that the reference covers the rows you intended. |
| Count does not match the filled cells | ROWS counts blank rows, but COUNTA does not. | Choose ROWS for block size and COUNTA for filled entries. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Excel 2024, Excel 2021, Excel 2019 and Excel for the web | Counts rows in a reference or array. |
| Google Sheets | Available | Counts rows in a range or inline array, and counts null values as rows. |

## Tips and Best Practices

- Subtract the header row explicitly so the formula reads clearly to the next person who edits it.
- Pair ROWS with COLUMNS to check the dimensions of a block before you paste or reshape it.
- Use COUNTA when the question is "how many entries," and ROWS when the question is "how tall is this block."
- Wrap a range in FILTER before passing it to ROWS when you need the count of rows that meet a condition.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COLUMNS](COLUMNS.md) | Returns the number of columns, the width counterpart to ROWS. |
| [ROW](ROW.md) | Returns the row number of a cell, not the count of rows. |
| [COUNTA](../Statistical/COUNTA.md) | Counts filled cells, which ROWS does not do. |
| [FILTER](FILTER.md) | Returns the rows that meet a condition, which ROWS can then count. |
| [SEQUENCE](../Math%20%26%20Trig/SEQUENCE.md) | Builds a list of numbers, often sized with ROWS. |

## Official Documentation

- [Microsoft Support: ROWS function](https://support.microsoft.com/en-us/excel/functions/rows-function)
- [Google Docs Editors Help: ROWS](https://support.google.com/docs/answer/3093382)
