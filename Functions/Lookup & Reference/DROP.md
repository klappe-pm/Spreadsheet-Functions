---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Array Shaping
purpose:
  - Array Shaping
use-case:
  - Dropping Leading Columns
  - Removing Header Rows
  - Trimming Total Rows
related:
  - CHOOSECOLS
  - CHOOSEROWS
  - EXPAND
  - FILTER
  - TAKE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/drop-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Drop Rows
  - Remove Leading Rows
tags:
  - array-shaping
  - dynamic-array
  - excel
  - header-removal
---

# DROP

## Description

**DROP** removes rows or columns from the start or end of an array and returns the rows and columns that remain. A positive number drops rows from the top or columns from the left. A negative number drops rows from the bottom or columns from the right. The result is an array, so it can feed SUM, FILTER or another array function in the same formula.

Use DROP to strip a header row from an imported list, remove a total line at the bottom of a report, or remove a few leading columns. When you want only a few columns or rows, CHOOSECOLS or TAKE can be simpler, because they name what to keep.

DROP is available in Microsoft Excel. Google Sheets does not have it; the Platform Differences section gives the closest alternative.

## Syntax

```excel
=DROP(array, rows, [columns])
```

<!-- Image 1: Drop Direction Diagram. See Images/Lookup & Reference/DROP.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array to trim. |
| `rows` | Yes | The number of rows to remove. A positive number removes rows from the top, and a negative number removes rows from the bottom. Zero is not allowed. |
| `columns` | No | The number of columns to remove, with the same sign rules. Leave `rows` empty, as in `DROP(A1:C5,,2)`, to remove columns only. |

### Return Value

The part of the array that remains after the rows or columns are removed. In Excel, a `rows` or `columns` value of 0 returns `#CALC!`, which the page describes as an empty array. An array that is too large returns `#NUM!`.

## Examples

All examples use this three-row block in `A2:C4`.

| Left | Middle | Right |
| --- | --- | --- |
| 3 | 8 | 12 |
| 5 | 9 | 14 |
| 2 | 7 | 11 |

### Example 1: Drop Rows From the Top

```excel
=DROP(A2:C4, 2)
```

**Result:** the last row, 2, 7 and 11

Two rows are removed from the top, so only the bottom row remains.

### Example 2: Drop Columns From the Left

```excel
=DROP(A2:C4,, 2)
```

**Result:** the last column, 12, 14 and 11

The rows argument is left empty, so no rows are removed, and two columns are removed from the left.

### Example 3: Drop a Row From the Bottom

```excel
=DROP(A2:C4, -1)
```

**Result:** the first two rows, 3, 8, 12 and 5, 9, 14

A negative number removes rows from the bottom, so the last row is dropped.

### Example 4: Sum Without the First Row

```excel
=SUM(DROP(A2:C4, 1))
```

**Result:** `48`

The first row is removed. The remaining values are 5, 9, 14, 2, 7 and 11, which add to 48.

<!-- Image 2: Rows and Columns Removed Together. See Images/Lookup & Reference/DROP.md -->

### Example 5: Drop Rows and Columns Together

```excel
=DROP(A2:C4, 2, 2)
```

**Result:** `11`

Two rows are removed from the top and two columns from the left, which leaves the single value in the bottom-right corner.

## Story Problems

### Problem 1: Sales Total Without the Header

A regional report keeps its header in row 1 and its data in rows 2 to 5 of column B.

| Region | Sales | Returns |
| --- | --- | --- |
| North | 1200 | 40 |
| South | 980 | 25 |
| East | 1430 | 60 |
| West | 760 | 15 |

**Task:** Total the sales values, excluding the header in row 1.

**Solution:**

```excel
=SUM(DROP(B1:B5, 1))
```

**Answer:** `4370`. The four sales figures are 1200, 980, 1430 and 760, which add to 4370.

### Problem 2: Store Total Without the Total Line

A chain lists its stores in rows 2 to 4 and a total in row 5. The total line must not be counted twice.

| Store | Revenue |
| --- | --- |
| Central | 500 |
| Harbor | 410 |
| Hilltop | 300 |
| Total | 1210 |

**Task:** Total the store revenues without the total line.

**Solution:**

```excel
=SUM(DROP(B2:B5, -1))
```

**Answer:** `1210`. The three store figures are 500, 410 and 300, which add to 1210.

## Use Cases

### Removing Header Rows

**Scenario:** An import from a CSV file has a title line above the column headers. The analysis needs only the data rows.

```excel
=SUM(DROP(Import!B1:B500, 1))
```

**Why It Works:** The formula drops the first row of the import before the sum starts. If the title grows to two lines, change the 1 to 2.

### Trimming Total Rows

**Scenario:** A monthly report puts a grand total in the last row, and a chart must show only the monthly rows.

```excel
=DROP(SalesData, -1)
```

**Why It Works:** The negative count removes the bottom row, so the chart range excludes the total and updates when the sheet has the same layout.

### Dropping Leading Columns

**Scenario:** An export starts with two index columns that the sheet does not need. The analysis uses the rest.

```excel
=DROP(Export!A1:Z50,, 2)
```

**Why It Works:** The empty rows argument keeps every row, and the 2 removes the first two columns from the left.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#CALC!` | The rows or columns value is 0. | Use a count of 1 or more, or leave the argument empty to skip it. |
| `#NUM!` | The array is too large. | Narrow the range. |
| Unexpected rows removed | A positive count was used where a negative count was meant, or the reverse. | Positive removes from the top or left; negative removes from the bottom or right. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024 (Windows and Mac) | Returns the remaining array, which can be used inside other array functions. |
| Google Sheets | Not available | Use INDEX or OFFSET with a range that starts on the first row you need, or FILTER to keep rows that meet a condition. |

## Tips and Best Practices

- Use a negative count to remove footer rows from a list that grows at the bottom.
- Leave the rows argument empty when only columns must be removed.
- Nest DROP inside SUM, FILTER or TAKE to clean and calculate in one formula.
- Remember that zero is not a valid count; use the empty argument instead.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHOOSECOLS](CHOOSECOLS.md) | Keeps named columns instead of removing them, which suits a short list of wanted columns. |
| [CHOOSEROWS](CHOOSEROWS.md) | Keeps named rows by position. |
| [EXPAND](EXPAND.md) | Adds rows and columns, the opposite of removing them. |
| [FILTER](FILTER.md) | Keeps rows that meet a condition rather than rows at fixed positions. |
| [TAKE](TAKE.md) | Keeps the first or last rows or columns of an array. |

## Official Documentation

- [Microsoft Support: DROP function](https://support.microsoft.com/en-us/excel/functions/drop-function)
