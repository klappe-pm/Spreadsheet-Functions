---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Matrix
purpose:
  - Matrix Math
  - Statistical Analysis
use-case:
  - Forecast Error Totals
  - Planned Versus Actual Checks
related:
  - CORREL
  - MMULT
  - SUMPRODUCT
  - SUMSQ
  - SUMX2MY2
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/sumxmy2-function
  - https://support.google.com/docs/answer/3094298
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Sum of Squared Differences
tags:
  - arrays
  - excel
  - sheets
  - statistics
---

# SUMXMY2

## Description

**SUMXMY2** takes two arrays of the same length, subtracts each value in the second array from the matching value in the first, squares each difference, and adds the squares. The result is the sum of squared differences across all pairs. Because every term is squared, the total is never negative and large misses count more than small ones.

The function pairs values by position, so the first value in `array_x` goes with the first value in `array_y`. A total of zero means the two arrays match exactly. Use SUMX2MY2 when you need the difference of the squares instead, and SUMX2PY2 when you need the sum of both squares.

Text, logical values and empty cells in an array or reference are ignored. Cells that contain zero are included. When the two arrays hold different numbers of values, the function returns `#N/A`.

## Syntax

```excel
=SUMXMY2(array_x, array_y)
```

<!-- Image 1: Paired Differences. See Images/Math & Trig/SUMXMY2.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array_x` | Yes | The first array or range of values. Each value is reduced by the matching `array_y` value. |
| `array_y` | Yes | The second array or range of values. It is subtracted from the matching `array_x` value before the difference is squared. |

### Return Value

A single number equal to the sum of the squared differences between paired values. The result is zero or positive. The function returns `#N/A` when the arrays contain different numbers of values.

## Examples

All examples use these values. The first array is in `A2:A5`: 5, 3, 8 and 4. The second array is in `B2:B5`: 2, 6, 1 and 4.

### Example 1: Two Ranges

```excel
=SUMXMY2(A2:A5, B2:B5)
```

**Result:** `67`

The differences are 3, -3, 7 and 0. Their squares are 9, 9, 49 and 0, and the total is 67.

### Example 2: Array Constants

```excel
=SUMXMY2({5,3,8,4}, {2,6,1,4})
```

**Result:** `67`

The same values typed directly in the formula give the same total as Example 1.

### Example 3: Root Mean Square Style Error

```excel
=ROUND(SQRT(SUMXMY2(A2:A5, B2:B5)), 2)
```

**Result:** `8.19`

The square root of 67 is 8.185, which ROUND shows as 8.19. This is the root of the total squared error, not an average.

### Example 4: Mismatched Arrays

```excel
=SUMXMY2(A2:A5, B2:B4)
```

**Result:** `#N/A`

The arrays have four and three values, so the function returns `#N/A`. Extend the second range to B5 to fix the formula.

## Story Problems

### Problem 1: Planned Versus Actual Picks

A warehouse planned a number of picks each day and recorded the actual picks. The supervisor wants the total of the squared differences to measure how far the plan was from the results.

| Day | Planned | Actual |
| --- | --- | --- |
| Monday | 40 | 38 |
| Tuesday | 55 | 59 |
| Wednesday | 30 | 27 |
| Thursday | 62 | 60 |

**Task:** Calculate the sum of the squared differences between the planned and actual picks.

**Solution:**

```excel
=SUMXMY2(B2:B5, C2:C5)
```

**Answer:** `33`, from 2 squared (4), (-4) squared (16), 3 squared (9) and 2 squared (4).

<!-- Image 2: Planned and Actual Table. See Images/Math & Trig/SUMXMY2.md -->

### Problem 2: Checking Two Price Lists

A buyer compares two suppliers' prices for the same five items to see how closely they agree. Each price is in a row, and the total of squared differences shows the spread.

| Item | Supplier A | Supplier B |
| --- | --- | --- |
| Bolt | 2 | 3 |
| Nut | 4 | 4 |
| Washer | 1 | 3 |
| Pin | 5 | 2 |
| Clip | 6 | 6 |

**Task:** Calculate the sum of the squared differences between the two suppliers' prices.

**Solution:**

```excel
=SUMXMY2(B2:B6, C2:C6)
```

**Answer:** `14`, from 1 (bolt), 0 (nut), 4 (washer), 9 (pin) and 0 (clip).

## Use Cases

### Forecast Error Totals

**Scenario:** A planner measures how far a forecast was from actual sales across a year.

```excel
=SUMXMY2(Sales[Actual], Forecast[Estimate])
```

**Why It Works:** Squaring each error makes large misses count more than small ones. Comparing this total across two forecasting methods shows which one is closer overall.

### Planned Versus Actual Checks

**Scenario:** A production manager checks whether a machine's output matches the schedule for a month.

```excel
=SUMXMY2(Schedule[Planned], Output[Produced])
```

**Why It Works:** A total of zero means the output matches the plan exactly, and a larger total means more deviation overall. Pair the check with the mean of the errors to see whether the deviation is consistently high or low.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The arrays hold different numbers of values. | Make both ranges the same length. |
| Result looks too large | The function returns squared errors, not the errors themselves. | Take the square root for a root sum of squared differences. |
| Unexpected total | Text or blank cells were skipped in one array but not the other. | Check that both arrays contain numbers in the same rows. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions, including Excel for the web | Returns `#N/A` for arrays of different sizes. Ignores text, logical values and empty cells. |
| Google Sheets | Available | The arguments are `array_x` and `array_y`. The help page describes the same pairing but does not state a size rule, so test with your data before relying on the result. |

## Tips and Best Practices

- Use SUMXMY2 for error totals, since squaring removes the sign of each difference.
- Keep the forecast and the actual values in the same row order.
- Compare totals only between data sets with the same number of rows, because a larger set adds more squared terms.
- Divide by the count when you need a mean squared error.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CORREL](../Statistical/CORREL.md) | Measures how closely two arrays move together, a related fit measure. |
| [MMULT](MMULT.md) | Multiplies matrices, a related array operation. |
| [SUMPRODUCT](SUMPRODUCT.md) | Multiplies paired arrays and sums the products. |
| [SUMSQ](SUMSQ.md) | Sums the squares of one set of values. |
| [SUMX2MY2](SUMX2MY2.md) | Sums the difference of the squares of paired values, which keeps the sign. |

## Official Documentation

- [Microsoft Support: SUMXMY2 function](https://support.microsoft.com/en-us/excel/functions/sumxmy2-function)
- [Google Docs Editors Help: SUMXMY2](https://support.google.com/docs/answer/3094298)
