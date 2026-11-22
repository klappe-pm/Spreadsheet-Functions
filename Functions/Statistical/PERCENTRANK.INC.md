---
domain: Spreadsheet Functions
category: Statistical
subcategory: Ranking and Percentiles
purpose:
  - Ranking
  - Statistical Analysis
use-case:
  - Order Value Ranking
  - Sales Rep Standing
related:
  - PERCENTILE.INC
  - PERCENTRANK
  - PERCENTRANK.EXC
  - RANK.AVG
  - RANK.EQ
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/percentrank-inc-function
  - https://support.google.com/docs/answer/3267360
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Inclusive Percentile Rank
tags:
  - excel
  - inclusive
  - percentile
  - ranking
  - sheets
---

# PERCENTRANK.INC

## Description

**PERCENTRANK.INC** returns the rank of a value within a dataset as a decimal from 0 to 1 inclusive. The smallest value returns 0 and the largest returns 1. Values in between receive their proportional position, so a value halfway through the ranked list returns about 0.5.

Use PERCENTRANK.INC for most new ranking work, because the bottom and top of the list show 0 and 1. It replaces the compatibility function PERCENTRANK and returns the same result for values that appear in the data. Use PERCENTRANK.EXC when the ranking must stay strictly inside the range.

When the value is not in the dataset, the function interpolates its rank between the two surrounding values. For example, a value one quarter of the way between two ranked values returns a rank one quarter of the way between their ranks. The default precision is three significant digits.

## Syntax

```excel
=PERCENTRANK.INC(array, x, [significance])
```

<!-- Image 1: Inclusive Percentrank Arguments. See Images/Statistical/PERCENTRANK.INC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array of numeric values that defines the dataset, for example `A2:A10`. |
| `x` | Yes | The value whose rank you want. |
| `significance` | No | The number of significant digits in the result. The default is 3, shown as 0.xxx. Use 1 or more. |

### Return Value

A decimal from 0 to 1 inclusive that shows the rank of `x`. The function returns `#NUM!` when the array is empty or the significance is less than 1.

## Examples

All examples use these nine values in `A2:A10`: 14, 22, 27, 31, 35, 40, 46, 52 and 60.

### Example 1: A Value From the Data

```excel
=PERCENTRANK.INC(A2:A10, 40)
```

**Result:** `0.625`

Five values sit below 40, and the rank is 5 ÷ (9 − 1).

### Example 2: An Interpolated Value

```excel
=PERCENTRANK.INC(A2:A10, 50)
```

**Result:** `0.833`

Fifty is between 46 (0.75) and 52 (0.875). It is two-thirds of the way from 46 to 52, so the rank is 0.75 + (2 ÷ 3) × 0.125, which rounds to 0.833.

### Example 3: The Smallest Value

```excel
=PERCENTRANK.INC(A2:A10, 14)
```

**Result:** `0`

The smallest value returns 0.

### Example 4: The Largest Value

```excel
=PERCENTRANK.INC(A2:A10, 60)
```

**Result:** `1`

The largest value returns 1.

## Story Problems

### Problem 1: Ranking a Large Order

A shop lists nine order values in `B2:B10`: 120, 180, 210, 240, 275, 300, 340, 390 and 450.

**Task:** Find the inclusive rank of the 300 order.

**Solution:**

```excel
=PERCENTRANK.INC(B2:B10, 300)
```

**Answer:** `0.625`. Five values sit below 300, and the rank is 5 ÷ (9 − 1).

### Problem 2: Where Nine Hours Falls

Nine resolution times in hours sit in `A2:A10`: 2, 3, 5, 8, 9, 12, 15, 20 and 26.

**Task:** Find the inclusive rank of the ticket that took 9 hours.

**Solution:**

```excel
=PERCENTRANK.INC(A2:A10, 9)
```

**Answer:** `0.5`. Four values sit below 9, and the rank is 4 ÷ (9 − 1).

<!-- Image 2: Rank Scale for the Order List. See Images/Statistical/PERCENTRANK.INC.md -->

## Use Cases

### Order Value Ranking

**Scenario:** A sales manager shows where each order sits among last quarter's orders, with the smallest at 0 and the largest at 1.

```excel
=PERCENTRANK.INC(Orders[Value], 300)
```

**Why It Works:** The inclusive scale makes the extremes easy to read. Because the function interpolates, check that the value appears in the list when the report needs an exact rank.

### Sales Rep Standing

**Scenario:** A regional manager ranks each rep's revenue against the team.

```excel
=PERCENTRANK.INC(Reps[Revenue], Reps[@Revenue])
```

**Why It Works:** The formula returns 1 for the top rep and 0 for the bottom rep, which suits a simple standing report.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The array is empty or the significance is less than 1. | Check the range holds values and use a significance of 1 or more. |
| Estimated rank | The value is not in the data, so the rank is interpolated. | Use a value from the list when an exact rank is required. |
| Unexpected precision | The result rounds to three significant digits by default. | Set the significance argument for the digits the report needs. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions | Returns a rank from 0 to 1 inclusive and interpolates values that are not in the data. |
| Google Sheets | Available | Estimates a percentage rank from 0 to 1 inclusive. The default significant digits is 3. The official page lists no error conditions. |

## Tips and Best Practices

- Use PERCENTRANK.INC for new ranking formulas, and keep PERCENTRANK only where older files depend on it.
- Pair the rank with PERCENTILE.INC when a report needs both a rank and the value at a given rank.
- Put the list in a table so the ranks update when rows are added.
- Use RANK.EQ when the report needs a position number instead of a percentage.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PERCENTILE.INC](PERCENTILE.INC.md) | Returns the value at a given inclusive percentile, the reverse lookup. |
| [PERCENTRANK](PERCENTRANK.md) | Compatibility function that this function replaces. |
| [PERCENTRANK.EXC](PERCENTRANK.EXC.md) | Exclusive version that keeps ranks strictly between 0 and 1. |
| [RANK.AVG](RANK.AVG.md) | Returns an average position for tied values. |
| [RANK.EQ](RANK.EQ.md) | Returns the position of a value in the list. |

## Official Documentation

- [Microsoft Support: PERCENTRANK.INC function](https://support.microsoft.com/en-us/excel/functions/percentrank-inc-function)
- [Google Docs Editors Help: PERCENTRANK.INC](https://support.google.com/docs/answer/3267360)
