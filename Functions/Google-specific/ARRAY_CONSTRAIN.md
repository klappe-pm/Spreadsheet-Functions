---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Array Tools
purpose:
  - Array Shaping
use-case:
  - Monthly Visit Snapshots
  - Sample Rows for Review
  - Top Sales Leaderboard
related:
  - ARRAYFORMULA
  - CHOOSEROWS
  - FILTER
  - FLATTEN
  - SORT
  - TAKE
level: 3
source:
  - https://support.google.com/docs/answer/3267036
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Constrain Array
tags:
  - arrays
  - dynamic-array
  - sheets
---

# ARRAY_CONSTRAIN

## Description

**ARRAY_CONSTRAIN** takes an array result and limits it to a specified number of rows and columns. It keeps the part of the input that starts at the top left corner, so a request for two rows and three columns returns the first two rows and the first three columns of the input.

Use ARRAY_CONSTRAIN when a formula produces more rows or columns than the report needs. A common case is a sorted list where only the top results should appear, such as the five highest sales. The function works well with SORT and FILTER, because those functions return arrays that ARRAY_CONSTRAIN can trim.

The official help page describes the function as constraining an array to a specified size and gives the three arguments. It does not state what happens when the requested size is larger than the input or when a size is zero or negative. Test those cases on a copy of your sheet before relying on them. The function is available only in Google Sheets. Excel 365 has a related function, TAKE, described in the platform section.

<!-- Image 1: ARRAY_CONSTRAIN Trim Example. See Images/Google-specific/ARRAY_CONSTRAIN.md -->

## Syntax

```excel
=ARRAY_CONSTRAIN(input_range, num_rows, num_cols)
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `input_range` | Yes | The range or array to constrain. It can be a plain range or a result from another function such as SORT or FILTER. |
| `num_rows` | Yes | The number of rows the result should contain. |
| `num_cols` | Yes | The number of columns the result should contain. |

### Return Value

An array of the requested size, taken from the top left of `input_range`. The result spills into the cells below and to the right of the formula, so those cells must be empty.

## Examples

### Example 1: Keeping the First Two Rows and Two Columns

```excel
=ARRAY_CONSTRAIN(A2:C4, 2, 2)
```

**Result:** Two rows and two columns: `Apple` and `3` in the first row, `Pear` and `5` in the second, when A2:C4 holds `Apple, 3, 1.2`, `Pear, 5, 0.8` and `Plum, 2, 2.5`.

The third row and the price column are dropped because the requested size is two by two.

### Example 2: Top Result From a Sorted List

```excel
=ARRAY_CONSTRAIN(SORT(A2:B4, 2, FALSE), 1, 2)
```

**Result:** `Pear` and `5`, the row with the largest quantity in column B of the same data.

SORT orders the rows by the second column from largest to smallest, and ARRAY_CONSTRAIN keeps only the first row.

### Example 3: Sorting by Price and Keeping Two Rows

```excel
=ARRAY_CONSTRAIN(SORT(A2:C4, 3, TRUE), 2, 3)
```

**Result:** Two rows: `Pear, 5, 0.8` followed by `Apple, 3, 1.2`.

Sorting by the third column in ascending order puts the lowest price first. Keeping two rows returns the two cheapest items with all three columns.

## Story Problems

### Problem 1: Top Three Sales Representatives

Five sales representatives are listed in `A2:B6` with their monthly sales in column B.

| Representative | Sales |
| --- | --- |
| Rina | 420 |
| Omar | 515 |
| Lena | 390 |
| Ken | 610 |
| Sara | 480 |

**Task:** Show only the three highest sales with the names and amounts, starting in `D2`.

**Solution:**

```excel
=ARRAY_CONSTRAIN(SORT(A2:B6, 2, FALSE), 3, 2)
```

**Answer:** Ken with 610, Omar with 515 and Sara with 480. Rina and Lena do not appear in the top three.

### Problem 2: First Four Months of Visits

A website team logs visits by month in `A2:B7`. The report has room for four months.

| Month | Visits |
| --- | --- |
| January | 1200 |
| February | 1350 |
| March | 1100 |
| April | 1500 |
| May | 1420 |
| June | 980 |

**Task:** Show the first four months and their visits starting in `D2`.

**Solution:**

```excel
=ARRAY_CONSTRAIN(A2:B7, 4, 2)
```

**Answer:** January 1200, February 1350, March 1100 and April 1500. May and June are left out of this view.

<!-- Image 2: ARRAY_CONSTRAIN Visit Snapshot. See Images/Google-specific/ARRAY_CONSTRAIN.md -->

## Use Cases

### Top Sales Leaderboard

**Scenario:** A regional manager wants a leaderboard that updates each week and shows only the top five reps.

```excel
=ARRAY_CONSTRAIN(SORT(A2:B20, 2, FALSE), 5, 2)
```

**Why It Works:** SORT ranks the full list, and ARRAY_CONSTRAIN keeps five rows. When the data grows, the leaderboard still shows exactly five rows.

### Sample Rows for Review

**Scenario:** An auditor wants a short sample of the first rows of a long export to check its layout.

```excel
=ARRAY_CONSTRAIN(Export!A2:H5000, 10, 8)
```

**Why It Works:** The formula returns the first ten rows and eight columns of the export without copying the whole file. Use it for review, and reference the full range in formulas that need every row.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Cells below are not empty | The result spills into cells that already hold data. | Clear the cells in the output area, or move the formula. |
| Unexpected size | The requested rows or columns are larger than the input, which the official page does not describe. | Test on a copy of the sheet and request only the size the input can supply. |
| Unexpected result | A zero or negative size was given, and the official page does not state the behavior. | Use a positive whole number for each size. |
| Sorted result is wrong | The sort column is not the one you meant, so the top rows are not the top values. | Check the sort column number and the ascending flag in SORT. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available. The closest alternative is TAKE in Microsoft 365, which returns a set number of rows and columns from the start of an array. | Excel has no ARRAY_CONSTRAIN function. |
| Google Sheets | Available | Constrains an array result to the size you give. Behavior for oversized or zero sizes is not documented on the official page. |

## Tips and Best Practices

- Combine ARRAY_CONSTRAIN with SORT or FILTER so the array is ordered before it is trimmed.
- Keep the output area clear, because a spilled result cannot overwrite existing data.
- Check the sort column number when building a top list, since a wrong column produces a plausible but wrong top result.
- Use CHOOSEROWS or CHOOSECOLS when you need a specific set of rows or columns rather than the top corner.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ARRAYFORMULA](ARRAYFORMULA.md) | Runs a formula across a range; ARRAY_CONSTRAIN trims the result that a formula returns. |
| [CHOOSEROWS](../Lookup%20%26%20Reference/CHOOSEROWS.md) | Returns chosen rows by position, when the rows you need are not the first ones. |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Returns only the rows that match a condition, which ARRAY_CONSTRAIN can then trim. |
| [FLATTEN](FLATTEN.md) | Turns several ranges into one column, which can be trimmed to a size. |
| [SORT](../Lookup%20%26%20Reference/SORT.md) | Orders an array, usually the step before a top-N trim. |
| [TAKE](../Lookup%20%26%20Reference/TAKE.md) | The closest Excel 365 function for taking a set number of rows or columns from an array. |

## Official Documentation

- [Google Docs Editors Help: ARRAY_CONSTRAIN](https://support.google.com/docs/answer/3267036)
