---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Ranking
  - Statistical Analysis
use-case:
  - Order Value Ranking
  - Test Score Standing
related:
  - PERCENTILE
  - PERCENTRANK.EXC
  - PERCENTRANK.INC
  - RANK.AVG
  - RANK.EQ
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/percentrank-function
  - https://support.google.com/docs/answer/3094095
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - compatibility
  - excel
  - percentile
  - ranking
  - sheets
---

# PERCENTRANK

## Description

**PERCENTRANK** returns the rank of a value within a dataset as a decimal between 0 and 1. A value at the bottom of the data returns 0, and a value at the top returns 1. The default precision is three significant digits.

PERCENTRANK is a compatibility function that Microsoft keeps for older workbooks. For new work, use PERCENTRANK.INC, which includes 0 and 1 in its range, or PERCENTRANK.EXC, which excludes them. PERCENTRANK and PERCENTRANK.INC return the same value for a number that appears in the data, while PERCENTRANK.EXC uses a different scale so that the bottom and top values are never 0 or 1.

Excel and Google Sheets differ when the value is not in the data. Excel interpolates a rank between the two surrounding values, while Sheets returns `#N/A`. Check which behavior your audience expects before you rely on the result for a value outside the list.

## Syntax

```excel
=PERCENTRANK(array, x, [significance])
```

<!-- Image 1: Percentrank Arguments Diagram. See Images/Statistical/PERCENTRANK.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array of numeric values that defines the dataset, for example `A2:A10`. |
| `x` | Yes | The value whose rank you want. |
| `significance` | No | The number of significant digits in the result. The default is 3, shown as 0.xxx. Google Sheets uses the default when you enter 0 or a negative number. |

### Return Value

A decimal from 0 to 1 that shows where `x` sits in the dataset. Excel returns `#NUM!` when the array is empty or the significance is less than 1. Google Sheets returns `#N/A` when `x` does not appear in the array.

## Examples

All examples use these nine values in `A2:A10`: 14, 22, 27, 31, 35, 40, 46, 52 and 60.

### Example 1: A Value From the Data

```excel
=PERCENTRANK(A2:A10, 40)
```

**Result:** `0.625`

Forty is the sixth of nine values, so five values sit below it, and 5 ÷ 8 = 0.625.

### Example 2: A Value Between Two Data Points

```excel
=PERCENTRANK(A2:A10, 50)
```

**Result:** `0.833` in Excel

Fifty is not in the list, so Excel interpolates between 46 (0.75) and 52 (0.875). Google Sheets returns `#N/A` for this formula.

### Example 3: The Smallest Value

```excel
=PERCENTRANK(A2:A10, 14)
```

**Result:** `0`

The smallest value has no values below it, so its rank is 0.

## Story Problems

### Problem 1: Ranking a Large Order

A shop lists nine order values in `B2:B10`: 120, 180, 210, 240, 275, 300, 340, 390 and 450.

**Task:** Find the rank of the 340 order within the list.

**Solution:**

```excel
=PERCENTRANK(B2:B10, 340)
```

**Answer:** `0.75`. Six values sit below 340, and the rank is 6 ÷ (9 − 1) = 0.75.

### Problem 2: Ranking a Support Ticket

Nine resolution times in hours sit in `A2:A10`: 2, 3, 5, 8, 9, 12, 15, 20 and 26.

**Task:** Find the rank of the ticket that took 8 hours.

**Solution:**

```excel
=PERCENTRANK(A2:A10, 8)
```

**Answer:** `0.375`. Three values are below 8, so the rank is 3 ÷ 8.

<!-- Image 2: Rank Scale for the Order List. See Images/Statistical/PERCENTRANK.md -->

## Use Cases

### Order Value Ranking

**Scenario:** A sales manager shows each order's standing among last quarter's orders.

```excel
=PERCENTRANK(Orders[Value], 340)
```

**Why It Works:** The rank scales the order against the whole table. Use PERCENTRANK.INC in new workbooks, which returns the same answer for a value that is in the data.

### Test Score Standing

**Scenario:** A trainer checks where a 78 score falls in a class of scores.

```excel
=PERCENTRANK(Scores[Points], 78)
```

**Why It Works:** The formula shows the share of the class below the score. Because 78 is interpolated in Excel, check the number against the data before you share it with students.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | Excel: the array is empty or the significance is less than 1. | Check that the range holds values and use a significance of 1 or more. |
| `#N/A` | Google Sheets: `x` does not appear in the array. | Use a value from the data, or switch to PERCENTRANK.INC, which estimates the rank. |
| Unexpected precision | The result is rounded to three significant digits by default. | Set the significance argument to show more digits. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available as a compatibility function | Interpolates the rank for a value not in the data. Returns `#NUM!` when significance is less than 1. |
| Google Sheets | Available | Returns `#N/A` for a value not in the data. Uses the default of 3 when significance is 0 or negative. |

## Tips and Best Practices

- Use PERCENTRANK.INC in new workbooks, and keep this function only where existing formulas depend on it.
- Match the value against the list before you interpret a rank, so an interpolated number does not look like a real data point.
- Put the significance argument in a cell when the report needs a fixed number of digits.
- Use RANK.EQ or RANK.AVG when you need a position number rather than a percentage.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PERCENTRANK.INC](PERCENTRANK.INC.md) | Current replacement that includes 0 and 1 in its range. |
| [PERCENTRANK.EXC](PERCENTRANK.EXC.md) | Current replacement that excludes 0 and 1. |
| [PERCENTILE](PERCENTILE.md) | Reverses the lookup: it returns the value at a given percentile. |
| [RANK.EQ](RANK.EQ.md) | Returns the position of a value in the list, not a percentage. |
| [RANK.AVG](RANK.AVG.md) | Returns an average position for tied values. |

## Official Documentation

- [Microsoft Support: PERCENTRANK function](https://support.microsoft.com/en-us/excel/functions/percentrank-function)
- [Google Docs Editors Help: PERCENTRANK](https://support.google.com/docs/answer/3094095)
