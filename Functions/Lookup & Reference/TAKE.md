---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Array Shaping
purpose:
  - Array Shaping
use-case:
  - Latest Log Entries
  - Quarterly Top Performers
  - Top Five Lists
related:
  - CHOOSECOLS
  - CHOOSEROWS
  - DROP
  - SORT
  - UNIQUE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/take-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Take Rows
  - Take Columns
tags:
  - array-shaping
  - dynamic-array
  - excel
---

# TAKE

## Description

**TAKE** returns a set of contiguous rows or columns from the start or the end of an array or range. It answers questions such as "what are the first five rows" or "what are the last ten entries" without any helper cells or offsets.

Give TAKE a positive number to count from the top or left, and a negative number to count from the bottom or right. Leave the rows argument empty to keep every row and take only columns, or leave out the columns argument to keep every column. TAKE pairs well with SORT: sort the list, then take the first rows to build a top-N list.

TAKE is the counterpart to DROP, which removes rows or columns instead of keeping them. TAKE works in Microsoft 365 and Excel 2024. It is not available in Excel 2021 or earlier, and Google Sheets does not have it.

## Syntax

```excel
=TAKE(array, rows, [columns])
```

<!-- Image 1: TAKE Arguments. See Images/Lookup & Reference/TAKE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array to take rows and columns from. |
| `rows` | Yes | The number of rows to take. A positive value counts from the top, and a negative value counts from the bottom. Leave it empty to take all rows. |
| `columns` | No | The number of columns to take. A positive value counts from the left, and a negative value counts from the right. Leave it out to take all columns. |

### Return Value

An array containing the requested rows and columns. It spills into the cells below and to the right of the formula. If `rows` or `columns` is 0, the formula returns `#CALC!`, because that would produce an empty array. If the array is too large, the formula returns `#NUM!`.

## Examples

All examples use this block in `A2:C6`.

| Column A | Column B | Column C |
| --- | --- | --- |
| 12 | 7 | 3 |
| 4 | 15 | 6 |
| 9 | 2 | 11 |
| 8 | 5 | 10 |
| 1 | 14 | 13 |

### Example 1: First Two Rows

```excel
=TAKE(A2:C6, 2)
```

**Result:** `12 7 3` and `4 15 6` on two rows

The columns argument is left out, so all three columns come through.

### Example 2: First Two Columns of Every Row

```excel
=TAKE(A2:C6,,2)
```

**Result:** Five rows, each with two values: `12 7`, `4 15`, `9 2`, `8 5` and `1 14`

The rows argument is empty, so every row is kept. The columns argument of 2 keeps the first two columns.

### Example 3: Last Two Rows

```excel
=TAKE(A2:C6, -2)
```

**Result:** `8 5 10` and `1 14 13` on two rows

A negative row count counts from the bottom of the block.

### Example 4: Top-Left Corner

```excel
=TAKE(A2:C6, 2, 2)
```

**Result:** `12 7` and `4 15`

Two rows and two columns are taken from the top left of the block.

### Example 5: Sum of the Three Largest Values

```excel
=SUM(TAKE(SORT(A2:A6, 1, -1), 3))
```

**Result:** `29`

SORT orders the values in column A from largest to smallest: 12, 9, 8, 4, 1. TAKE keeps the first three, and SUM adds 12, 9 and 8.

<!-- Image 2: Positive and Negative Counts. See Images/Lookup & Reference/TAKE.md -->

## Story Problems

### Problem 1: Top Three Sales Totals

A sales team records the sale amount for each of six reps in `B2:B7`.

| Rep | Sales |
| --- | --- |
| Rep A | 4200 |
| Rep B | 3100 |
| Rep C | 5600 |
| Rep D | 2750 |
| Rep E | 3900 |
| Rep F | 4800 |

**Task:** Find the total of the three largest sales.

**Solution:**

```excel
=SUM(TAKE(SORT(B2:B7, 1, -1), 3))
```

**Answer:** `14600`. The three largest amounts are 5600, 4800 and 4200, and they add to 14600.

### Problem 2: Most Recent Log Entries

A system log lists event IDs in `A2:A9`, oldest first. The last eight entries run from E-101 to E-108.

**Task:** Show the four most recent entries and name them.

**Solution:**

```excel
=TAKE(A2:A9, -4)
```

**Answer:** E-105, E-106, E-107 and E-108. The negative row count keeps the last four rows.

## Use Cases

### Latest Log Entries

**Scenario:** An operations dashboard shows the ten most recent rows from a log that grows every day.

```excel
=TAKE(Log!A2:D5000, -10)
```

**Why It Works:** A negative count keeps the bottom of the range. If the range has blank rows at the bottom, those blanks are returned too, so size the range to the expected data.

### Quarterly Top Performers

**Scenario:** A manager wants a list of the top five performers for the current quarter.

```excel
=TAKE(SORT(Sales!A2:C200, 3, -1), 5)
```

**Why It Works:** SORT ranks the rows by sales, and TAKE keeps the first five. The list updates whenever the sales data changes.

### Fixed Width Report

**Scenario:** A report should show only the first three columns of an export that has many more.

```excel
=TAKE(Export!A1:Z500,, 3)
```

**Why It Works:** An empty rows argument keeps every row, and the columns argument limits the report to three columns.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#CALC!` | The rows or columns argument is 0. | Use a count of 1 or more, or a negative count from the end. |
| `#NUM!` | The array is too large to return. | Take fewer rows or columns, or filter the source first. |
| `#SPILL!` | The cells below or beside the formula are not empty. | Clear the spill range, or move the formula. |
| Blank rows in the result | The source range extends past the data. | Reference only the rows that contain data. |
| `#NAME?` | The Excel version is 2021 or earlier. | Use INDEX with a row range, or upgrade to Excel 2024 or Microsoft 365. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Excel 2024 and Excel for the web | Not listed for Excel 2021 or earlier. Negative counts take from the end. |
| Google Sheets | Not available | Use a fixed range reference, or ARRAY_CONSTRAIN to limit the rows and columns of an array. |

## Tips and Best Practices

- Pair TAKE with SORT to build top-N lists that update automatically.
- Use a negative count to read the most recent rows of a list that grows at the bottom.
- Keep the source range close to the data so the result contains no unused blank rows.
- Use DROP when it is easier to name the rows to remove than the rows to keep.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DROP](DROP.md) | Removes rows or columns, the opposite of TAKE. |
| [CHOOSEROWS](CHOOSEROWS.md) | Returns chosen rows by position, not a contiguous block. |
| [CHOOSECOLS](CHOOSECOLS.md) | Returns chosen columns by position, the column counterpart. |
| [SORT](SORT.md) | Orders the rows so TAKE can keep the top or bottom ones. |
| [UNIQUE](UNIQUE.md) | Removes duplicates before TAKE keeps the first values. |

## Official Documentation

- [Microsoft Support: TAKE function](https://support.microsoft.com/en-us/excel/functions/take-function)
