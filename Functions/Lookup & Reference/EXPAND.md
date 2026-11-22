---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Array Shaping
purpose:
  - Array Shaping
use-case:
  - Aligning Stacked Exports
  - Building Fixed Size Grids
  - Padding Quarterly Tables
related:
  - CHOOSECOLS
  - DROP
  - HSTACK
  - TAKE
  - VSTACK
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/expand-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Pad Array
  - Resize Array
tags:
  - array-shaping
  - dynamic-array
  - excel
  - padding
---

# EXPAND

## Description

**EXPAND** resizes an array to a larger number of rows and columns. It keeps the original values in the top-left corner and fills every new cell with a value that you choose. Use it to make two blocks the same size before stacking them, to give a report a fixed number of rows, or to pad a table so that a later formula always receives the same shape.

If you leave the rows or columns value blank, that direction keeps its current size. EXPAND can only add rows and columns. A requested size smaller than the array returns `#VALUE!`, so use DROP or TAKE to shrink an array.

When you omit `pad_with`, Excel fills the new cells with `#N/A`. That default makes missing data easy to spot, but most reports should supply a value such as 0 or an empty string.

## Syntax

```excel
=EXPAND(array, rows, [columns], [pad_with])
```

<!-- Image 1: Expand Argument Anatomy. See Images/Lookup & Reference/EXPAND.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The array or range to expand. |
| `rows` | Yes | The number of rows in the result. A blank value keeps the array's existing row count. It cannot be smaller than the array. |
| `columns` | No | The number of columns in the result. If omitted or blank, the existing column count is kept. It cannot be smaller than the array. |
| `pad_with` | No | The value placed in each new cell. If omitted, the new cells show `#N/A`. |

### Return Value

An array with the requested number of rows and columns. The original values stay in the top-left corner and the new cells hold the pad value. Excel returns `#VALUE!` when the requested rows or columns are smaller than the array, and `#NUM!` when the array is too large.

## Examples

All examples use this two-by-two block in `A2:B3`.

| Value 1 | Value 2 |
| --- | --- |
| 5 | 7 |
| 2 | 4 |

### Example 1: Expand With the Default Padding

```excel
=EXPAND(A2:B3, 4, 3)
```

**Result:** a four-row, three-column block. The original four values sit in the top-left corner, and the new cells show `#N/A`.

Two rows and one column are added. Because `pad_with` is left out, the new cells show `#N/A`.

### Example 2: Expand a Single Cell

```excel
=EXPAND(A2, 3, 3, "-")
```

**Result:** a three-by-three block with the value of A2 in the top-left cell and `-` in the other eight cells

A one-cell array can grow into a larger block, and the text pad fills the rest.

### Example 3: Keep the Rows and Add Columns

```excel
=EXPAND(A2:B3,, 4, 0)
```

**Result:** a two-row, four-column block with 0 in the two new columns

The rows argument is blank, so the two rows stay the same. Two columns of 0 are added on the right.

<!-- Image 2: Padded Cells Versus Original Values. See Images/Lookup & Reference/EXPAND.md -->

### Example 4: Sum a Padded Block

```excel
=SUM(EXPAND(A2:B3, 3, 2, 0))
```

**Result:** `18`

The new row is filled with 0, which adds nothing to the total. The original values 5, 7, 2 and 4 add to 18.

## Story Problems

### Problem 1: Quarterly Totals for a Four-Branch Table

A branch report has values for two branches in `B2:C3`. The finance template expects four branches and four quarterly columns, with unused cells set to 0.

| Branch | Q1 | Q2 |
| --- | --- | --- |
| North | 120 | 135 |
| South | 98 | 110 |

**Task:** Total all the values once the block is padded to four rows and four columns.

**Solution:**

```excel
=SUM(EXPAND(B2:C3, 4, 4, 0))
```

**Answer:** `463`. The four values are 120, 135, 98 and 110. The padded cells hold 0, so they add nothing.

### Problem 2: Fixed Six-Row Label Sheet

A label printer prints six rows per sheet. The name list has four names in `A2:A5`, and the last two rows must show "Open".

| Name |
| --- |
| Ana |
| Ben |
| Cy |
| Dee |

**Task:** Return the value in row 6 of the padded list.

**Solution:**

```excel
=INDEX(EXPAND(A2:A5, 6, 1, "Open"), 6, 1)
```

**Answer:** `Open`. The list is padded to six rows, and row 6 is one of the new cells that hold the pad text.

## Use Cases

### Aligning Stacked Exports

**Scenario:** Two monthly exports have different numbers of columns, and their rows must be stacked into one list with the same width.

```excel
=VSTACK(EXPAND(Jan!A1:C10, 10, 4, ""), EXPAND(Feb!A1:D8, 10, 4, ""))
```

**Why It Works:** Both blocks are padded to four columns and ten rows before stacking, so the rows line up. The empty text pad keeps the new cells blank.

### Padding Quarterly Tables

**Scenario:** A regional sales table covers fewer quarters than the dashboard expects, and the chart must always receive a four-by-four block.

```excel
=EXPAND(QuarterData, 4, 4, 0)
```

**Why It Works:** The formula returns a fixed shape no matter how many regions or quarters are filled in, so the chart range stays stable.

### Building Fixed Size Grids

**Scenario:** A seating plan sheet needs a grid of ten rows and ten columns, even when only a few seats are listed in the source.

```excel
=EXPAND(Seats, 10, 10, "Empty")
```

**Why It Works:** Every missing seat shows the word "Empty", and the grid keeps the same size as the source list grows.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The rows or columns value is smaller than the array. | Use a count equal to or larger than the array, or use TAKE or DROP to shrink it. |
| `#N/A` in new cells | The pad_with argument was left out. | Supply a pad value such as 0 or `""`. |
| `#NUM!` | The array is too large. | Narrow the source range. |
| Stacked arrays do not line up | The arrays have different widths before stacking. | Expand both arrays to the same number of columns. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024 (Windows and Mac) | Pads with `#N/A` by default. Blank rows or columns keep the existing size. |
| Google Sheets | Not available | Reference a fixed-size range and fill the extra cells with a default value, or use IF to show a blank for empty cells. |

## Tips and Best Practices

- Choose a pad value that matches the data type, such as 0 for numbers and `""` for text.
- Leave `pad_with` out when padded cells should show `#N/A`, so missing data stands out.
- Pair EXPAND with TAKE when an array must match an exact size in both directions.
- Expand arrays to the same width before stacking them with VSTACK or HSTACK.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHOOSECOLS](CHOOSECOLS.md) | Selects named columns, which can reduce a wide array before expanding it. |
| [DROP](DROP.md) | Removes rows or columns, the opposite of EXPAND. |
| [HSTACK](HSTACK.md) | Joins arrays side by side once they share the same row count. |
| [TAKE](TAKE.md) | Keeps the first or last rows or columns, which shrinks an array to a set size. |
| [VSTACK](VSTACK.md) | Joins arrays top to bottom once they share the same column count. |

## Official Documentation

- [Microsoft Support: EXPAND function](https://support.microsoft.com/en-us/excel/functions/expand-function)
