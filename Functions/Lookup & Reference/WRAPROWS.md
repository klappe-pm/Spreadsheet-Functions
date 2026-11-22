---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Array Shaping
purpose:
  - Array Shaping
use-case:
  - Quarterly Summary Grid
  - Seating Chart Layout
  - Shift Schedule Grid
related:
  - CHOOSEROWS
  - ROWS
  - TOROW
  - VSTACK
  - WRAPCOLS
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/wraprows-function
  - https://support.google.com/docs/answer/13184285
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Wrap Into Rows
  - Wrap Rows
tags:
  - array-shaping
  - dynamic-array
  - excel
  - reshaping
  - sheets
---

# WRAPROWS

## Description

**WRAPROWS** takes a single row or column of values and reshapes it into rows. You choose how many values each row holds. The function fills the first row from left to right, starts the next row when that one is full, and continues until every value is placed.

Use WRAPROWS when a long list needs to appear as a grid, such as twelve monthly figures arranged as four rows of three quarters, or a list of guests arranged as tables of eight. The result is a dynamic array, so it updates when the source list changes.

The last row may not be full. The optional `pad_with` argument fills the empty positions. When you leave it out, Excel shows `#N/A` in those positions, so supply a blank text or a zero when the grid will be printed or summed.

[WRAPCOLS](WRAPCOLS.md) does the same job in the opposite direction, filling columns first. [VSTACK](VSTACK.md) joins arrays one below the other, which is the reverse of reshaping a list into a grid.

WRAPROWS is available in Excel for Microsoft 365, Excel for the web and Excel 2024. It is not available in Excel 2021 or earlier. Google Sheets supports it under the same name.

## Syntax

```excel
=WRAPROWS(vector, wrap_count, [pad_with])
```

<!-- Image 1: WRAPROWS Syntax Anatomy. See Images/Lookup & Reference/WRAPROWS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `vector` | Yes | The one-dimensional row or column of values to reshape. It can be a range or an array, but it cannot be a two-dimensional block. |
| `wrap_count` | Yes | The maximum number of values in each row. It must be 1 or more. |
| `pad_with` | No | The value used to fill the empty positions in the last row. When omitted, the empty positions show `#N/A`. |

### Return Value

A two-dimensional array with rows of up to `wrap_count` values, filled from left to right. When `wrap_count` is at least as large as the number of values, the result is one row. The function returns `#VALUE!` when `vector` is not one-dimensional and `#NUM!` when `wrap_count` is less than 1.

## Examples

All examples use six values in `A2:A7`: 12, 7, 9, 15, 4 and 11.

### Example 1: Wrapping Into Rows of Three

```excel
=WRAPROWS(A2:A7, 3)
```

**Result:** A two-row array. Row 1 holds 12, 7, 9. Row 2 holds 15, 4, 11.

The function fills each row with three values. Six values divide evenly, so no padding is needed.

### Example 2: Padding an Incomplete Last Row

```excel
=WRAPROWS(A2:A6, 3, 0)
```

**Result:** A two-row array. Row 1 holds 12, 7, 9. Row 2 holds 15, 4, 0.

Only five values exist in `A2:A6`, so the last position is filled with the `pad_with` value 0. Without that argument, the position would show `#N/A`.

### Example 3: Blank Padding for Printing

```excel
=WRAPROWS(A2:A6, 3, "")
```

**Result:** The same grid as Example 2, with a blank cell in the last position

Text padding keeps the printed grid tidy. The blank cell is still a text value, so `SUM` ignores it, but a formula that counts non-empty cells will count it.

### Example 4: Reading One Row of the Result

```excel
=INDEX(WRAPROWS(A2:A6, 3, 0), 2, 0)
```

**Result:** The second row, 15, 4, 0

`INDEX` with a column position of 0 returns the whole row. This pattern pulls one row from the grid without a helper range.

<!-- Image 2: Source List Versus Wrapped Grid. See Images/Lookup & Reference/WRAPROWS.md -->

### Example 5: Counting the Rows in the Grid

```excel
=ROWS(WRAPROWS(A2:A7, 4))
```

**Result:** `2`

Six values with four per row make one full row and one row with two values, so the grid has two rows.

## Story Problems

### Problem 1: Shift Counts in a Grid

A warehouse records the number of pallets moved in each of seven shifts in `A2:A8`. The supervisor wants the shifts in rows of three.

| Shift | Pallets |
| --- | --- |
| 1 | 4 |
| 2 | 6 |
| 3 | 3 |
| 4 | 5 |
| 5 | 7 |
| 6 | 2 |
| 7 | 8 |

**Task:** Sum the pallets in the last row of the grid, using a blank padding of zero.

**Solution:**

```excel
=SUM(INDEX(WRAPROWS(A2:A8, 3, 0), 3, 0))
```

**Answer:** `8`. The grid has three rows, and the last row holds the seventh shift (8) plus two zeros of padding.

### Problem 2: Seating Tables of Eight

A caterer has 19 names in `A2:A20` and needs them listed in rows that represent tables of eight. The sheet must show a row for each table with empty seats marked.

**Task:** Write the formula that places all names into rows of eight, with a blank text in unused seats.

**Solution:**

```excel
=WRAPROWS(A2:A20, 8, "")
```

**Answer:** Three rows of eight. The first two tables are full, and the third table holds three names followed by five blank seats.

<!-- Image 3: Seating Grid With Padding. See Images/Lookup & Reference/WRAPROWS.md -->

## Use Cases

### Quarterly Summary Grid

**Scenario:** A finance team keeps twelve monthly revenue figures in one column and wants a grid with one row per quarter for a dashboard.

```excel
=WRAPROWS(Revenue!B2:B13, 3)
```

**Why It Works:** Three values per row turns each block of three months into a quarter. Because twelve divides evenly by three, no padding is needed. A `SUM` over each row then gives quarterly totals.

### Seating Chart Layout

**Scenario:** An events coordinator lists guests in a column and prints the seating chart with eight guests per table.

```excel
=WRAPROWS(Guests!A2:A60, 8, "")
```

**Why It Works:** The blank padding keeps the last table tidy. When the guest list grows, the formula still reflows the grid, and the coordinator does not need to move names by hand.

### Shift Schedule Grid

**Scenario:** A call center stores a list of staff names for one week and needs them arranged in rows of five, one row for each day.

```excel
=WRAPROWS(Staff!A2:A16, 5, "Open")
```

**Why It Works:** The text `Open` marks unused slots, so unfilled positions are visible to managers instead of showing errors.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The last row is incomplete and no `pad_with` value was given. | Add a `pad_with` value such as `""` or `0`. |
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

- Always supply `pad_with` when the grid will be summed, printed or shown to readers.
- Use `""` for padding in printed grids and `0` when the grid feeds calculations.
- Pair WRAPROWS with `INDEX` and a column position of 0 to pull whole rows.
- Keep the source list in one column or one row so the function accepts it.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHOOSEROWS](CHOOSEROWS.md) | Picks specific rows from an array, which is useful after a grid is built. |
| [ROWS](ROWS.md) | Counts how many rows a wrapped grid contains. |
| [TOROW](TOROW.md) | Flattens an array into one row, the reverse of wrapping. |
| [VSTACK](VSTACK.md) | Stacks arrays vertically instead of reshaping one list. |
| [WRAPCOLS](WRAPCOLS.md) | Wraps the same values into columns instead of rows. |

## Official Documentation

- [Microsoft Support: WRAPROWS function](https://support.microsoft.com/en-us/excel/functions/wraprows-function)
- [Google Docs Editors Help: WRAPROWS](https://support.google.com/docs/answer/13184285)
