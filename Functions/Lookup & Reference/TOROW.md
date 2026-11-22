---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Array Shaping
purpose:
  - Array Shaping
  - Data Cleaning
use-case:
  - Counting Named Items
  - Header Row Lists
  - Summing Grids With Errors
related:
  - FILTER
  - HSTACK
  - TOCOL
  - TRANSPOSE
  - UNIQUE
  - WRAPROWS
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/torow-function
  - https://support.google.com/docs/answer/13187459
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - To Row
  - Flatten to Row
tags:
  - array-shaping
  - data-cleaning
  - excel
  - sheets
---

# TOROW

## Description

**TOROW** reshapes a range or array into a single row. It reads the cells in order, either row by row or column by column, and places every value in one horizontal line. Use it when a grid needs to become a header row, a single list across the sheet, or input for a formula that expects one row.

Like its column counterpart TOCOL, TOROW can skip values as it reads them. The `ignore` argument drops blank cells, error values, or both. By default nothing is ignored, so a blank comes through as 0. Set `ignore` to 1 to skip blanks, or to 2 to skip errors so that one bad cell does not break a total.

The `scan_by_column` argument sets the reading order. The default reads left to right across each row. Set it to TRUE to read down each column in turn.

TOROW is available in Microsoft 365 and Excel 2024, and in Google Sheets. It is not available in Excel 2021 or earlier. The Excel and Google Sheets versions take the same arguments.

## Syntax

```excel
=TOROW(array, [ignore], [scan_by_column])
```

<!-- Image 1: TOROW Output Shape. See Images/Lookup & Reference/TOROW.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array to convert into a single row. |
| `ignore` | No | Which values to drop: `0` keeps all values (the default), `1` ignores blanks, `2` ignores errors, and `3` ignores blanks and errors. |
| `scan_by_column` | No | FALSE (the default) reads row by row. TRUE reads column by column. |

### Return Value

A single row containing the values from `array` in the chosen reading order. Blank cells return 0 when `ignore` is 0. The result spills to the right of the formula. If an array constant holds numbers that are not whole numbers, the formula returns `#VALUE!`. If the array is too large, it returns `#NUM!`.

## Examples

All examples use this block in `A2:C4`. The cell in row 3, column B is blank.

| Column A | Column B | Column C |
| --- | --- | --- |
| 4 | 7 | 1 |
| 2 | (blank) | 9 |
| 6 | 3 | 5 |

### Example 1: Keep Every Value, Read by Row

```excel
=TOROW(A2:C4)
```

**Result:** 4, 7, 1, 2, 0, 9, 6, 3, 5

The blank cell comes through as 0 because `ignore` is left at its default of 0.

### Example 2: Skip Blank Cells

```excel
=TOROW(A2:C4, 1)
```

**Result:** 4, 7, 1, 2, 9, 6, 3, 5

Setting `ignore` to 1 drops the blank, so the row has eight values.

### Example 3: Read Column by Column

```excel
=TOROW(A2:C4, 0, TRUE)
```

**Result:** 4, 2, 6, 7, 0, 3, 1, 9, 5

The first column is read top to bottom, then the second column (with its blank as 0), then the third.

### Example 4: Largest Filled Value

```excel
=MAX(TOROW(A2:C4, 1))
```

**Result:** `9`

The blank is skipped, and the largest of the remaining values is 9.

<!-- Image 2: Counting Named Items. See Images/Lookup & Reference/TOROW.md -->

## Story Problems

### Problem 1: Counting Named Items

A grid in `A2:C4` lists the names of team members, with one cell left empty.

| Column A | Column B | Column C |
| --- | --- | --- |
| Alpha | Bravo | Charlie |
| Delta | (blank) | Echo |
| Foxtrot | Golf | Hotel |

**Task:** Count how many names the grid contains, leaving out the empty cell.

**Solution:**

```excel
=COUNTA(TOROW(A2:C4, 1))
```

**Answer:** `8`. The grid has nine cells, and the empty one is skipped.

### Problem 2: Totalling a Grid With Errors

A small report in `A2:C3` has two error cells: one divides by zero and one uses NA. The four other cells hold 6, 14, 8 and 2.

**Task:** Total the valid numbers, skipping every error.

**Solution:**

```excel
=SUM(TOROW(A2:C3, 2))
```

**Answer:** `30`. Six, 14, 8 and 2 add to 30.

## Use Cases

### Header Row Lists

**Scenario:** A template needs a single row of field names collected from a multi-row header block.

```excel
=TOROW(Template!A1:D3, 1)
```

**Why It Works:** Blanks are skipped, so the row contains only the names that were typed, in the order they appear across the block.

### Dropdown Source Across a Row

**Scenario:** A planner keeps approved vendor names in a grid, and a dropdown needs them in one row.

```excel
=UNIQUE(TOROW(Vendors!B2:F20, 1))
```

**Why It Works:** TOROW gives one row of names, and UNIQUE returns each vendor once, which keeps the dropdown free of repeats.

### Totals That Survive Errors

**Scenario:** A monthly grid sometimes shows errors from broken lookups, and the total must still reflect the valid figures.

```excel
=SUM(TOROW(Costs!B2:M20, 2))
```

**Why It Works:** Setting `ignore` to 2 drops the error values before SUM adds the rest.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Zeros appear in the row | Blank cells are returned as 0 when `ignore` is 0. | Set `ignore` to 1 to skip blanks. |
| Total fails with an error | An error value is included in the result. | Set `ignore` to 2 or 3. |
| `#VALUE!` | An array constant contains numbers that are not whole numbers. | Use whole numbers, or pass a range. |
| Values in an unexpected order | Row-by-row reading is the default. | Set `scan_by_column` to TRUE for column order. |
| `#NAME?` | The Excel version is 2021 or earlier. | Use TOROW in Microsoft 365 or Excel 2024, or use TRANSPOSE on a helper column. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 and Excel 2024, including Excel for the web | Not listed for Excel 2021 or earlier. |
| Google Sheets | Available | Same arguments. `scan_by_column` takes TRUE or FALSE. |

## Tips and Best Practices

- Use `ignore` set to 1 whenever the grid has gaps, so the row does not fill with zeros.
- Use `ignore` set to 2 when a grid can contain errors and the total must still work.
- Use TOCOL when the output should be one column instead of one row.
- Wrap TOROW in UNIQUE or COUNTA to answer questions about every value in a grid in one step.

## Related Functions

| Function | Relationship |
| --- | --- |
| [TOCOL](TOCOL.md) | Returns the same values as a single column. |
| [WRAPROWS](WRAPROWS.md) | Builds a grid of rows from a list, the reverse direction. |
| [TRANSPOSE](TRANSPOSE.md) | Swaps rows and columns, keeping every cell. |
| [HSTACK](HSTACK.md) | Places several ranges side by side, an alternative when the ranges are separate. |
| [UNIQUE](UNIQUE.md) | Removes repeated values from the flattened row. |
| [FILTER](FILTER.md) | Keeps only the values that meet a condition. |

## Official Documentation

- [Microsoft Support: TOROW function](https://support.microsoft.com/en-us/excel/functions/torow-function)
- [Google Docs Editors Help: TOROW](https://support.google.com/docs/answer/13187459)
