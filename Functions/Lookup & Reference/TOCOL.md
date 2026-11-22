---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Array Shaping
purpose:
  - Array Shaping
  - Data Cleaning
use-case:
  - Collecting Grid Values
  - Counting Filled Responses
  - Flattening Lookup Sources
related:
  - FILTER
  - TOROW
  - TRANSPOSE
  - UNIQUE
  - VSTACK
  - WRAPCOLS
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/tocol-function
  - https://support.google.com/docs/answer/13187258
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - To Column
  - Flatten to Column
tags:
  - array-shaping
  - data-cleaning
  - excel
  - sheets
---

# TOCOL

## Description

**TOCOL** reshapes a range or array into a single column. It reads the cells in order, either row by row or column by column, and stacks every value in one column. Use it when data arranged in a grid needs to become a list, for example before counting, summing or deduplicating every value at once.

TOCOL can also drop values as it reads them. The `ignore` argument skips blank cells, error values, or both. By default nothing is ignored, so a blank cell comes through as 0. Set `ignore` to 1 to skip blanks, which is the usual choice for survey grids and sparse tables.

The `scan_by_column` argument sets the reading order. The default reads left to right across each row. Set it to TRUE to read top to bottom down each column.

TOCOL is available in Microsoft 365 and Excel 2024, and in Google Sheets. It is not available in Excel 2021 or earlier. The Excel function and the Google Sheets function take the same arguments.

## Syntax

```excel
=TOCOL(array, [ignore], [scan_by_column])
```

<!-- Image 1: TOCOL Reading Order. See Images/Lookup & Reference/TOCOL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array to convert into a single column. |
| `ignore` | No | Which values to drop: `0` keeps all values (the default), `1` ignores blanks, `2` ignores errors, and `3` ignores blanks and errors. |
| `scan_by_column` | No | FALSE (the default) reads row by row. TRUE reads column by column. |

### Return Value

A single column containing the values from `array` in the chosen reading order. Blank cells return 0 when `ignore` is 0. The result spills downward. If an array constant holds numbers that are not whole numbers, the formula returns `#VALUE!`. If the array is too large, it returns `#NUM!`.

## Examples

All examples use this block in `A2:C4`. The cell in row 3, column B is blank.

| Column A | Column B | Column C |
| --- | --- | --- |
| 4 | 7 | 1 |
| 2 | (blank) | 9 |
| 6 | 3 | 5 |

### Example 1: Keep Every Value, Read by Row

```excel
=TOCOL(A2:C4)
```

**Result:** 4, 7, 1, 2, 0, 9, 6, 3, 5

The blank cell comes through as 0 because `ignore` is left at its default of 0.

### Example 2: Skip Blank Cells

```excel
=TOCOL(A2:C4, 1)
```

**Result:** 4, 7, 1, 2, 9, 6, 3, 5

Setting `ignore` to 1 drops the blank cell, so the column has eight values.

### Example 3: Read Column by Column, Skipping Blanks

```excel
=TOCOL(A2:C4, 1, TRUE)
```

**Result:** 4, 2, 6, 7, 3, 1, 9, 5

The first column is read top to bottom, then the second column (skipping its blank), then the third.

### Example 4: Sum the Filled Cells

```excel
=SUM(TOCOL(A2:C4, 1))
```

**Result:** `37`

The blank is skipped, and the eight values 4, 7, 1, 2, 9, 6, 3 and 5 add to 37.

<!-- Image 2: Ignore Options. See Images/Lookup & Reference/TOCOL.md -->

## Story Problems

### Problem 1: Monthly Store Sales Grid

A grid in `B2:D4` shows monthly sales for three stores. One store has not reported its second month, so that cell is blank.

| Store | Jan | Feb | Mar |
| --- | --- | --- | --- |
| North | 120 | 95 | 140 |
| South | 80 | (blank) | 110 |
| West | 75 | 130 | 90 |

**Task:** Find the total of all reported sales, leaving out the blank cell.

**Solution:**

```excel
=SUM(TOCOL(B2:D4, 1))
```

**Answer:** `840`. The eight reported values add to 840.

### Problem 2: Summing Around Errors

A cost sheet in `A2:C3` has two cells that return errors, because one divides by zero and one uses NA. The other four cells hold 10, 25, 30 and 5.

**Task:** Total the valid costs, skipping every error cell.

**Solution:**

```excel
=SUM(TOCOL(A2:C3, 2))
```

**Answer:** `70`. Ten, 25, 30 and 5 add to 70. The error cells are dropped, so the total does not fail.

## Use Cases

### Collecting Grid Values

**Scenario:** A planner has a grid of department codes spread across several columns, and needs one list of the unique codes for a dropdown.

```excel
=UNIQUE(TOCOL(Codes!B2:F100, 1))
```

**Why It Works:** TOCOL turns the grid into a single column and skips blanks, and UNIQUE then returns each code once.

### Counting Filled Survey Responses

**Scenario:** A survey stores each answer in a grid, and the team wants to know how many answers were given.

```excel
=COUNT(TOCOL(Survey!B2:F200, 1))
```

**Why It Works:** Skipping blanks leaves only the answers that were given, and COUNT counts the numeric ones.

### Flattening a Lookup Source

**Scenario:** A lookup needs a single column of values from a two-dimensional table, but the table is laid out across many columns.

```excel
=TOCOL(Table!B2:M13, 1, TRUE)
```

**Why It Works:** `scan_by_column` set to TRUE reads down each month column in turn, which keeps the values of each column together.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Zeros appear in the result | Blank cells are returned as 0 when `ignore` is 0. | Set `ignore` to 1 to skip blanks. |
| `#VALUE!` | An array constant contains numbers that are not whole numbers. | Use whole numbers in the constant, or pass a range instead. |
| Errors stop a total | The error values are included in the result. | Set `ignore` to 2 or 3. |
| Values come out in an unexpected order | The reading order is row by row by default. | Set `scan_by_column` to TRUE for column order. |
| `#NAME?` | The Excel version is 2021 or earlier. | Use TOCOL in Microsoft 365 or Excel 2024, or flatten the grid with a helper formula. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 and Excel 2024, including Excel for the web | Not listed for Excel 2021 or earlier. |
| Google Sheets | Available | Same arguments. `scan_by_column` takes TRUE or FALSE. |

## Tips and Best Practices

- Use `ignore` set to 1 for grids with gaps, so blanks do not appear as zeros in the list.
- Combine TOCOL with UNIQUE, SUM or COUNT to answer questions across an entire grid in one formula.
- Use TOROW when the output should be one row instead of one column.
- Set `scan_by_column` to TRUE only when the grid is organized by columns; the default matches most grids laid out by rows.

## Related Functions

| Function | Relationship |
| --- | --- |
| [TOROW](TOROW.md) | Returns the same values as a single row. |
| [WRAPCOLS](WRAPCOLS.md) | Builds a grid of columns from a list, the reverse direction. |
| [TRANSPOSE](TRANSPOSE.md) | Swaps rows and columns without removing blanks. |
| [FILTER](FILTER.md) | Keeps only the rows that match a condition. |
| [UNIQUE](UNIQUE.md) | Removes repeated values from the flattened column. |
| [VSTACK](VSTACK.md) | Stacks several ranges into one, an alternative when the ranges are already separate. |

## Official Documentation

- [Microsoft Support: TOCOL function](https://support.microsoft.com/en-us/excel/functions/tocol-function)
- [Google Docs Editors Help: TOCOL](https://support.google.com/docs/answer/13187258)
