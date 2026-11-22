---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Array Shaping
purpose:
  - Array Shaping
use-case:
  - Name Badge Sheet
  - Product Catalog Columns
related:
  - CHOOSECOLS
  - COLUMNS
  - HSTACK
  - TOCOL
  - WRAPROWS
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/wrapcols-function
  - https://support.google.com/docs/answer/13184284
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Wrap Columns
  - Wrap Into Columns
tags:
  - array-shaping
  - dynamic-array
  - excel
  - reshaping
  - sheets
---

# WRAPCOLS

## Description

**WRAPCOLS** takes a single row or column of values and reshapes it into columns. You choose how many values each column holds. The function fills the first column from top to bottom, starts the next column when that one is full, and continues until every value is placed.

Use WRAPCOLS when a list must read across a page, such as a long product list that should fill three columns on a printed catalog, or a set of sample readings that should sit in columns for comparison. The result is a dynamic array, so it updates when the source list changes.

Each column holds exactly the number of values you set, so the last column may be incomplete. The optional `pad_with` argument fills the empty positions. Without it, Excel shows `#N/A` there, so supply a blank text or a zero when the output is printed or summed.

[WRAPROWS](WRAPROWS.md) does the same job in the other direction, filling rows first. [HSTACK](HSTACK.md) places arrays side by side without reshaping them.

WRAPCOLS is available in Excel for Microsoft 365, Excel for the web and Excel 2024. It is not available in Excel 2021 or earlier. Google Sheets supports it under the same name.

## Syntax

```excel
=WRAPCOLS(vector, wrap_count, [pad_with])
```

<!-- Image 1: WRAPCOLS Syntax Anatomy. See Images/Lookup & Reference/WRAPCOLS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `vector` | Yes | The one-dimensional row or column of values to reshape. It can be a range or an array, but it cannot be a two-dimensional block. |
| `wrap_count` | Yes | The maximum number of values in each column. It must be 1 or more. |
| `pad_with` | No | The value used to fill the empty positions in the last column. When omitted, the empty positions show `#N/A`. |

### Return Value

A two-dimensional array with columns of up to `wrap_count` values, filled from top to bottom. When `wrap_count` is at least as large as the number of values, the result is one column. The function returns `#VALUE!` when `vector` is not one-dimensional and `#NUM!` when `wrap_count` is less than 1.

## Examples

All examples use six values in `A2:A7`: 12, 7, 9, 15, 4 and 11.

### Example 1: Wrapping Into Columns of Two

```excel
=WRAPCOLS(A2:A7, 2)
```

**Result:** A two-row, three-column array. Row 1 holds 12, 9, 4. Row 2 holds 7, 15, 11.

Column 1 takes the first two values, column 2 takes the next two, and column 3 takes the last two.

### Example 2: Padding an Incomplete Last Column

```excel
=WRAPCOLS(A2:A6, 2, 0)
```

**Result:** A two-row, three-column array. Row 1 holds 12, 9, 4. Row 2 holds 7, 15, 0.

Five values fill two full columns and one column with a single value, so the last position takes the padding value 0.

### Example 3: Three-Row Columns

```excel
=WRAPCOLS(A2:A7, 3, "")
```

**Result:** A three-row, two-column array. Column 1 holds 12, 7, 9. Column 2 holds 15, 4, 11.

Each column holds three values, so the result has two columns. No padding is needed because six values divide evenly.

### Example 4: Summing One Column of the Result

```excel
=SUM(INDEX(WRAPCOLS(A2:A7, 2), 0, 1))
```

**Result:** `19`

`INDEX` with a row position of 0 returns the whole first column, which holds 12 and 7. Their sum is 19.

<!-- Image 2: Source List Versus Wrapped Columns. See Images/Lookup & Reference/WRAPCOLS.md -->

### Example 5: Counting the Columns

```excel
=COLUMNS(WRAPCOLS(A2:A7, 2))
```

**Result:** `3`

Six values with two per column produce three columns, which `COLUMNS` reports directly.

## Story Problems

### Problem 1: Attendance Across Two Sessions

A training provider runs eight sessions. The attendance counts for the sessions are in `B2:B9`, in date order. The first four sessions form the first block and the last four form the second block.

| Session | Attendance |
| --- | --- |
| 1 | 14 |
| 2 | 9 |
| 3 | 22 |
| 4 | 17 |
| 5 | 11 |
| 6 | 19 |
| 7 | 8 |
| 8 | 13 |

**Task:** Total the attendance for the second block, using a single formula that wraps the counts into columns of four.

**Solution:**

```excel
=SUM(INDEX(WRAPCOLS(B2:B9, 4), 0, 2))
```

**Answer:** `51`, because 11 + 19 + 8 + 13 = 51.

<!-- Image 3: Block Totals From Wrapped Columns. See Images/Lookup & Reference/WRAPCOLS.md -->

### Problem 2: Columns for a Printed Name List

An event team has 10 attendee names in `A2:A11` and wants them printed in columns of three names each, reading down the page.

**Task:** Write the formula that counts how many columns the printed list needs.

**Solution:**

```excel
=COLUMNS(WRAPCOLS(A2:A11, 3))
```

**Answer:** `4`. Ten names with three per column need four columns, and the last column holds one name.

## Use Cases

### Name Badge Sheet

**Scenario:** A conference team lists registered attendees in one column and prints badge sheets with eight badges per column.

```excel
=WRAPCOLS(Attendees!A2:A49, 8, "")
```

**Why It Works:** Each column becomes one stack of badges. The blank padding keeps the final column clean when the number of attendees is not a multiple of eight.

### Product Catalog Columns

**Scenario:** A small shop keeps its product names in a long column and wants a printed catalog that uses three columns across the page.

```excel
=WRAPCOLS(Products!A2:A25, 6)
```

**Why It Works:** Six products per column fill each column in turn. When the product list changes, the catalog reflows without manual copying.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The last column is incomplete and no `pad_with` value was given. | Add a `pad_with` value such as `""` or `0`. |
| `#VALUE!` | `vector` is a two-dimensional range. | Pass one row or one column, or stack the blocks into one column first. |
| `#NUM!` | `wrap_count` is 0 or negative. | Use a whole number of 1 or more. |
| `#SPILL!` | Cells in the spill area already contain data. | Clear the cells to the right of and below the formula. |
| `#NAME?` | The workbook is opened in Excel 2021 or earlier. | Open the file in Excel for Microsoft 365, Excel 2024 or Google Sheets. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365, Excel for the web and Excel 2024. | Arguments are named `vector`, `wrap_count` and `pad_with`. Empty positions show `#N/A` without `pad_with`. |
| Google Sheets | Available. | Arguments are named `range`, `wrap_count` and `pad_with`. A `wrap_count` that is not a whole number is rounded down. |

## Tips and Best Practices

- Choose `wrap_count` as the number of rows you want per column, not the number of columns.
- Supply `pad_with` whenever the output is printed or summed.
- Wrap with `INDEX` and a row position of 0 to pull a full column into another formula.
- Use WRAPROWS instead when the reader scans across rows rather than down columns.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHOOSECOLS](CHOOSECOLS.md) | Picks specific columns from an array, useful after the layout is built. |
| [COLUMNS](COLUMNS.md) | Counts how many columns a wrapped result contains. |
| [HSTACK](HSTACK.md) | Places arrays side by side without reshaping them. |
| [TOCOL](TOCOL.md) | Flattens an array into one column, the reverse of wrapping. |
| [WRAPROWS](WRAPROWS.md) | Wraps the same values into rows instead of columns. |

## Official Documentation

- [Microsoft Support: WRAPCOLS function](https://support.microsoft.com/en-us/excel/functions/wrapcols-function)
- [Google Docs Editors Help: WRAPCOLS](https://support.google.com/docs/answer/13184284)
