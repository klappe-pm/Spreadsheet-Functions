---
domain: Spreadsheet Functions
category: Statistical
subcategory: Ranking and Percentiles
purpose:
  - Statistical Analysis
use-case:
  - Bonus Threshold Setting
  - Order Value Benchmarks
related:
  - MEDIAN
  - PERCENTILE
  - PERCENTILE.EXC
  - PERCENTRANK.INC
  - QUARTILE.INC
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/percentile-inc-function
  - https://support.google.com/docs/answer/3094093
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Inclusive Percentile
tags:
  - excel
  - inclusive
  - interpolation
  - percentile
  - sheets
---

# PERCENTILE.INC

## Description

**PERCENTILE.INC** returns the k-th percentile of the values in a range, where k is a number from 0 to 1 inclusive. A k of 0 returns the smallest value, a k of 1 returns the largest value, and a k of 0.5 returns the median. When k falls between two ranked values, the function interpolates and may return a decimal that does not appear in the data.

Use PERCENTILE.INC for most new percentile work, because its inclusive range covers the full span of the data. It replaces the compatibility function PERCENTILE, and it gives the same results as PERCENTILE for the same inputs. Use PERCENTILE.EXC when a rule requires an exclusive range that excludes 0 and 1.

The function ranks each value at position k × (n − 1) + 1, where n is the number of values. That rank is the basis for every interpolated result on this page.

## Syntax

```excel
=PERCENTILE.INC(array, k)
```

<!-- Image 1: Inclusive Percentile Arguments. See Images/Statistical/PERCENTILE.INC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array of values that defines the distribution, for example `A2:A10`. |
| `k` | Yes | The percentile to return, as a decimal from 0 to 1 inclusive. Enter 0.9 for the 90th percentile. |

### Return Value

The k-th percentile as a number, interpolated when needed. The function returns `#NUM!` when the array is empty or k is less than 0 or greater than 1, and `#VALUE!` when k is not numeric.

## Examples

All examples use these nine values in `A2:A10`: 14, 22, 27, 31, 35, 40, 46, 52 and 60.

### Example 1: Lower Quartile

```excel
=PERCENTILE.INC(A2:A10, 0.25)
```

**Result:** `27`

The rank is 0.25 × 8 + 1 = 3, which is the third value.

### Example 2: Interpolated Upper Range

```excel
=PERCENTILE.INC(A2:A10, 0.9)
```

**Result:** `53.6`

The rank is 0.9 × 8 + 1 = 8.2, which falls 20 percent of the way from 52 to 60.

### Example 3: The Smallest Value

```excel
=PERCENTILE.INC(A2:A10, 0)
```

**Result:** `14`

A k of 0 returns the minimum, which the exclusive version cannot return.

### Example 4: Guarding Against a Bad Percentile

```excel
=IFERROR(PERCENTILE.INC(A2:A10, 1.2), "Out of Range")
```

**Result:** `Out of Range`

A k above 1 returns `#NUM!`, so IFERROR shows a readable message.

## Story Problems

### Problem 1: Setting a Bonus Threshold

A sales team records the value of nine orders in `B2:B10`: 120, 180, 210, 240, 275, 300, 340, 390 and 450.

**Task:** Find the order value at the 90th percentile. Reps who reach that value earn a bonus.

**Solution:**

```excel
=PERCENTILE.INC(B2:B10, 0.9)
```

**Answer:** `402`. The rank is 0.9 × 8 + 1 = 8.2, which is 20 percent of the way from 390 to 450.

### Problem 2: Resolution Times for Quick Support

A help desk logs the hours it took to resolve nine tickets in `A2:A10`: 2, 3, 5, 8, 9, 12, 15, 20 and 26.

**Task:** Find the resolution time at the 25th percentile, inclusive, to set a quick-response target.

**Solution:**

```excel
=PERCENTILE.INC(A2:A10, 0.25)
```

**Answer:** `5` hours. The rank is 0.25 × 8 + 1 = 3, which is the third value.

<!-- Image 2: Bonus Threshold on the Order Column. See Images/Statistical/PERCENTILE.INC.md -->

## Use Cases

### Bonus Threshold Setting

**Scenario:** A sales manager sets the bonus line at the 90th percentile of last quarter's order values.

```excel
=PERCENTILE.INC(Orders[Value], 0.9)
```

**Why It Works:** The formula recalculates as new orders are added to the table. Because the result is interpolated, a bonus line can fall between two real orders, so state the rule clearly to the team.

### Order Value Benchmarks

**Scenario:** An analyst uses the 75th percentile of order values as the benchmark for large orders.

```excel
=PERCENTILE.INC(Orders[Value], 0.75)
```

**Why It Works:** The inclusive range allows any percentage from 0 to 100 percent, so the benchmark can be changed in one input cell without restructuring the formula.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | k is below 0 or above 1, or the array is empty. | Enter a k from 0 to 1 and check the range holds values. |
| `#VALUE!` | k is text or a blank reference. | Enter k as a number. |
| Decimal result | The percentile falls between two values. | Round the display if the team needs whole numbers. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions | Replaces PERCENTILE for new work and accepts 0 and 1 for k. |
| Google Sheets | Available | The Google help page for PERCENTILE defines the two-argument form used here. The official page does not list an inclusive or exclusive variant. |

## Tips and Best Practices

- Use PERCENTILE.INC for new formulas and keep PERCENTILE only in workbooks that already use it.
- Use PERCENTILE.EXC when a rule forbids the minimum or maximum as a result.
- Put k in an input cell with a label so the threshold is easy to find and change.
- Check one result by hand: count the rank with k × (n − 1) + 1 and interpolate.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PERCENTILE](PERCENTILE.md) | Compatibility function that PERCENTILE.INC replaces, with the same inclusive behavior. |
| [PERCENTILE.EXC](PERCENTILE.EXC.md) | Exclusive version that rejects 0 and 1 for k. |
| [PERCENTRANK.INC](PERCENTRANK.INC.md) | Returns the inclusive rank of a value, the reverse lookup. |
| [MEDIAN](MEDIAN.md) | Gives the same result as k = 0.5. |
| [QUARTILE.INC](QUARTILE.INC.md) | Returns inclusive quartile cut points of the same data. |

## Official Documentation

- [Microsoft Support: PERCENTILE.INC function](https://support.microsoft.com/en-us/excel/functions/percentile-inc-function)
- [Google Docs Editors Help: PERCENTILE](https://support.google.com/docs/answer/3094093)
