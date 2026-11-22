---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Reference Building
purpose:
  - Data Retrieval
use-case:
  - Dynamic Chart Ranges
  - Growing Data Named Range
  - Rolling Average Window
related:
  - COUNTA
  - INDEX
  - INDIRECT
  - MATCH
  - ROW
  - ROWS
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/offset-function
  - https://support.google.com/docs/answer/3093379
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Cell Offset
  - Dynamic Range
  - Range Offset
tags:
  - dynamic-range
  - excel
  - reference
  - sheets
  - volatile
---

# OFFSET

## Description

**OFFSET** returns a reference to a cell or range that sits a given number of rows and columns away from a starting cell. You name the start, how far to move down or up, how far to move right or left, and, optionally, how many rows and columns the result should cover. OFFSET does not move or change any data. It only points at cells, so the result can be used anywhere a range is accepted, such as inside SUM, AVERAGE or a chart source.

OFFSET is useful when a range must start in a calculated position or change size as data arrives. A formula can count the filled rows, convert that count into a height, and total exactly the entries that exist. A named range built with OFFSET can feed a chart that grows with the data.

OFFSET is volatile. Excel recalculates every OFFSET formula whenever any cell in the workbook changes, which can slow large workbooks. Where a fixed or INDEX-based range will do, prefer it. INDEX returns a reference without being volatile, so `SUM(B2:INDEX(B:B, n))` gives the same result as a range built with OFFSET in many cases.

## Syntax

```excel
=OFFSET(reference, rows, cols, [height], [width])
```

<!-- Image 1: OFFSET Argument Anatomy. See Images/Lookup & Reference/OFFSET.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `reference` | Yes | The starting cell or range. It must be a single cell or a block of adjacent cells. |
| `rows` | Yes | How far to move from the starting cell. A positive number moves down, a negative number moves up, and zero keeps the same row. Decimal parts are cut off. |
| `cols` | Yes | How far to move from the starting cell. A positive number moves right, a negative number moves left, and zero keeps the same column. Decimal parts are cut off. |
| `height` | No | The number of rows in the result. It must be positive. When omitted, the result has the same height as `reference`. |
| `width` | No | The number of columns in the result. It must be positive. When omitted, the result has the same width as `reference`. |

### Return Value

A reference to the cell or range that OFFSET identifies. It is not a value, so `=OFFSET(B2, 3, 0)` returns a reference to cell B5, and the formula displays the value in B5. OFFSET returns `#REF!` when the offset moves the result beyond the top or left edge of the sheet. It returns `#VALUE!` when `reference` is not a cell or a range of adjacent cells.

## Examples

All examples use this weekly sales table in `A1:B7`. The header is in row 1, weeks 1 to 6 are in `A2:A7`, and sales are in `B2:B7`.

| Week | Sales |
| --- | --- |
| Week 1 | 40 |
| Week 2 | 55 |
| Week 3 | 30 |
| Week 4 | 62 |
| Week 5 | 48 |
| Week 6 | 70 |

### Example 1: One Cell Three Rows Down

```excel
=OFFSET(B2, 3, 0)
```

**Result:** `62`

The formula starts at B2 and moves down three rows to B5. Since no height or width is given, the result is the single cell B5, and its value is 62.

### Example 2: Total of the First Three Weeks

```excel
=SUM(OFFSET(B2, 0, 0, 3, 1))
```

**Result:** `125`

The formula stays at B2 and returns a range three rows tall and one column wide, which is B2:B4. The sum is 40 + 55 + 30 = 125.

### Example 3: Average of the Last Three Weeks

```excel
=AVERAGE(OFFSET(B7, -2, 0, 3, 1))
```

**Result:** `60`

Starting at B7 and moving up two rows gives B5. A height of three covers B5:B7, which holds 62, 48 and 70. Their average is 60.

<!-- Image 2: Rolling Window Range. See Images/Lookup & Reference/OFFSET.md -->

### Example 4: Window Size From a Cell

```excel
=SUM(OFFSET(B7, 1-C1, 0, C1, 1))
```

Where `C1` contains `3`

**Result:** `180`

The formula moves up `C1 - 1` rows from B7 and uses a height of C1 rows. With C1 set to 3, it covers B5:B7 and returns 62 + 48 + 70 = 180. Change C1 and the window changes size.

### Example 5: Reference From a Labeled Row

```excel
=OFFSET(A4, 2, 1)
```

**Result:** `48`

Row 4 holds the label Week 3 in column A. Moving down two rows reaches row 6, and moving right one column reaches column B. The cell B6 holds 48, the sales for Week 5.

### Example 6: Same Total Without OFFSET

```excel
=SUM(B2:INDEX(B:B, COUNTA(B:B)))
```

**Result:** `305`

COUNTA counts seven filled cells in column B, including the header. INDEX returns a reference to B7, and the range B2:B7 sums to 305. This version is not volatile, so it recalculates only when the referenced cells change.

## Story Problems

### Problem 1: Total of the Four Most Recent Weeks

The weekly sales table from the examples is in `A1:B7`. A manager enters the number of recent weeks in `D1` and wants the total of those weeks.

**Task:** Put 4 in `D1` and return the total sales for the four most recent weeks.

**Solution:**

```excel
=SUM(OFFSET(B7, 1-D1, 0, D1, 1))
```

**Answer:** `210`. The formula moves up three rows from B7 to B4 and covers four rows, B4:B7, which hold 30, 62, 48 and 70. Their total is 210.

<!-- Image 3: Four Week Window Result. See Images/Lookup & Reference/OFFSET.md -->

### Problem 2: Value Two Rows Below a Label

A manager wants the sales figure two rows below the label Week 3 in `A4`, without typing the cell address into the formula.

**Task:** Enter a formula that returns the sales value two rows below the cell that contains the label Week 3.

**Solution:**

```excel
=OFFSET(A4, 2, 1)
```

**Answer:** `48`, the sales for Week 5. Moving down two rows from row 4 reaches row 6, and moving one column right reaches column B.

## Use Cases

### Growing Data Named Range

**Scenario:** A sales log gains a new row each day. A chart and several summary formulas should include every entry without anyone editing a range address.

```excel
=OFFSET(SalesLog!$A$1, 0, 0, COUNTA(SalesLog!$A:$A), 2)
```

**Why It Works:** Define this formula as a named range, such as `LogData`, in the Name Manager in Excel or in Named ranges in Google Sheets. The height is the count of filled cells in column A, which includes the header, so the range covers the header and every entry. The width of two covers columns A and B. Because OFFSET is volatile, keep the number of such names small in a large workbook.

### Rolling Average Window

**Scenario:** A finance analyst reports the average of the last N months, where N is typed in a cell. The table keeps growing, and N may be larger than the number of months available.

```excel
=AVERAGE(OFFSET($B$2, MAX(0, COUNTA($B:$B)-1-$D$1), 0, MIN($D$1, COUNTA($B:$B)-1), 1))
```

**Why It Works:** COUNTA minus 1 counts the monthly entries under the header. The start row moves down so that only the last N entries are included, and MAX keeps the start at the first entry when N is larger than the data. The height uses MIN for the same reason, so the average covers all available months rather than returning an error. With the Week table and N set to 3, the formula averages B5:B7 and returns 60.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#REF!` | The offset moves the result past the top or left edge of the sheet. | Use MAX to keep the starting row and column at 1 or higher. |
| `#REF!` | The result would overwrite part of its own starting range in an array formula, which creates a circular reference. | Move the formula so the result does not overlap its starting range. |
| `#VALUE!` | `reference` is not a single cell or a block of adjacent cells. | Use a single cell or contiguous range as the starting point. |
| Error or wrong size | `height` or `width` is zero or negative. | Wrap the value in MAX(1, ...) so it stays positive. |
| Slow workbook | Many OFFSET formulas recalculate on every change. | Replace them with INDEX-based ranges where possible. |
| Unexpected total | A decimal row or column value was cut off. | Round the calculated offset with INT or ROUND before using it. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Excel 2024, Excel 2021, Excel 2019 and Excel 2016, including Mac and web versions | Returns a reference that can be used in named ranges, charts and functions that accept references. Volatile, so it recalculates on every worksheet change. |
| Google Sheets | Available | Uses the same arguments. Decimal row and column values are truncated. Circular array references return `#REF!`. The documentation does not describe volatility, so test performance on large sheets. |

## Tips and Best Practices

- Prefer INDEX-based ranges such as `B2:INDEX(B:B, n)` when the result only needs to be a range, because INDEX is not volatile.
- Give the height and width every time, so the result size is clear to the next person who reads the formula.
- Define a dynamic range once as a named range and reuse the name, rather than repeating OFFSET in many cells.
- Use MAX and MIN to keep the starting point and the size within the available data.
- Test a named range by selecting its name in the Name Box and checking the highlighted cells.

## Related Functions

| Function | Relationship |
| --- | --- |
| [INDEX](INDEX.md) | Returns a reference or value without volatility, and often replaces OFFSET for ranges. |
| [INDIRECT](INDIRECT.md) | Builds a reference from text, which is also volatile. |
| [COUNTA](../Statistical/COUNTA.md) | Counts filled cells, which often supplies the height for a dynamic range. |
| [MATCH](MATCH.md) | Finds a position that can be used as the row or column offset. |
| [ROW](ROW.md) | Returns a row number that can be used to calculate offsets. |
| [ROWS](ROWS.md) | Counts the rows in a range, which can supply a height. |

## Official Documentation

- [Microsoft Support: OFFSET function](https://support.microsoft.com/en-us/excel/functions/offset-function)
- [Google Docs Editors Help: OFFSET](https://support.google.com/docs/answer/3093379)
