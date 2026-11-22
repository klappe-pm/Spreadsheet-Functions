---
domain: Spreadsheet Functions
category: Statistical
subcategory: Ranking and Percentiles
purpose:
  - Ranking
  - Statistical Analysis
use-case:
  - Sales Rep Standing
  - Support Ticket Ranking
related:
  - PERCENTILE.EXC
  - PERCENTRANK
  - PERCENTRANK.INC
  - RANK.AVG
  - RANK.EQ
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/percentrank-exc-function
  - https://support.google.com/docs/answer/3267357
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Exclusive Percentile Rank
tags:
  - excel
  - exclusive
  - percentile
  - ranking
  - sheets
---

# PERCENTRANK.EXC

## Description

**PERCENTRANK.EXC** returns the rank of a value within a dataset as a decimal strictly between 0 and 1. Neither end is included, so the smallest value does not return 0 and the largest value does not return 1. With n values, the smallest value returns 1 ÷ (n + 1) and the largest returns n ÷ (n + 1).

Use PERCENTRANK.EXC when a ranking rule must place every value strictly inside the range, for example when a score of 0 or 100 percent would be misleading. Use PERCENTRANK.INC when the bottom and top values should show 0 and 1. PERCENTRANK.EXC replaces the compatibility function PERCENTRANK for exclusive ranking.

When the value is not in the dataset, the function estimates its rank by interpolating between the two surrounding values. The default precision is three significant digits.

## Syntax

```excel
=PERCENTRANK.EXC(array, x, [significance])
```

<!-- Image 1: Exclusive Percentrank Arguments. See Images/Statistical/PERCENTRANK.EXC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array of numeric values that defines the dataset, for example `A2:A10`. |
| `x` | Yes | The value whose rank you want. |
| `significance` | No | The number of significant digits in the result. The default is 3, shown as 0.xxx. Use 1 or more. |

### Return Value

A decimal strictly between 0 and 1 that shows the rank of `x`. The function returns `#NUM!` when the array is empty or the significance is less than 1.

## Examples

All examples use these nine values in `A2:A10`: 14, 22, 27, 31, 35, 40, 46, 52 and 60.

### Example 1: A Value From the Data

```excel
=PERCENTRANK.EXC(A2:A10, 40)
```

**Result:** `0.6`

Forty is the sixth of nine values, so the rank is 6 ÷ 10.

### Example 2: The Middle Value

```excel
=PERCENTRANK.EXC(A2:A10, 35)
```

**Result:** `0.5`

Thirty-five is the fifth of nine values, so the rank is 5 ÷ 10.

### Example 3: The Smallest Value

```excel
=PERCENTRANK.EXC(A2:A10, 14)
```

**Result:** `0.1`

The smallest of nine values returns 1 ÷ 10, not 0.

### Example 4: The Largest Value

```excel
=PERCENTRANK.EXC(A2:A10, 60)
```

**Result:** `0.9`

The largest of nine values returns 9 ÷ 10, not 1.

## Story Problems

### Problem 1: Ranking a Large Order

A shop lists nine order values in `B2:B10`: 120, 180, 210, 240, 275, 300, 340, 390 and 450. The policy is that no order is ranked at the extremes.

**Task:** Find the exclusive rank of the 300 order.

**Solution:**

```excel
=PERCENTRANK.EXC(B2:B10, 300)
```

**Answer:** `0.6`. Five values sit below 300, so the rank is (5 + 1) ÷ 10.

### Problem 2: Ranking a Support Ticket

Nine resolution times in hours sit in `A2:A10`: 2, 3, 5, 8, 9, 12, 15, 20 and 26.

**Task:** Find the exclusive rank of the ticket that took 20 hours.

**Solution:**

```excel
=PERCENTRANK.EXC(A2:A10, 20)
```

**Answer:** `0.8`. Seven values sit below 20, so the rank is (7 + 1) ÷ 10.

## Use Cases

### Sales Rep Standing

**Scenario:** A sales director reports each rep's standing without showing a rep as the absolute top or bottom.

```excel
=PERCENTRANK.EXC(Reps[Revenue], Reps[@Revenue])
```

**Why It Works:** The exclusive scale keeps every standing strictly inside the range. The formula uses a structured reference inside a table, so it updates when reps are added.

### Support Ticket Ranking

**Scenario:** A support lead ranks tickets by resolution time for a monthly review.

```excel
=PERCENTRANK.EXC(Tickets[Hours], 20)
```

**Why It Works:** The formula gives each ticket a standing between the fastest and slowest, so the review shows relative speed rather than an extreme.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The array is empty or the significance is less than 1. | Check the range holds values and use a significance of 1 or more. |
| Unexpected rank | The value is not in the data, so the rank is interpolated. | Confirm the value is in the list, or report that the rank is estimated. |
| Unexpected precision | The result rounds to three significant digits by default. | Set the significance argument for the digits the report needs. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions | Returns a rank strictly between 0 and 1 and interpolates values that are not in the data. |
| Google Sheets | Available | Estimates a percentage rank from 0 to 1 exclusive. The default significant digits is 3. The official page lists no error conditions. |

## Tips and Best Practices

- Use PERCENTRANK.EXC when the result must never show a perfect 0 or 1.
- Use PERCENTRANK.INC when the bottom and top values should show 0 and 1.
- Pair the rank with PERCENTILE.EXC when a report needs both the rank of a value and the value at a given rank.
- Put the list in a table so the ranks update when rows are added.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PERCENTILE.EXC](PERCENTILE.EXC.md) | Returns the value at a given exclusive percentile, the reverse lookup. |
| [PERCENTRANK](PERCENTRANK.md) | Compatibility function that this function replaces for exclusive ranking. |
| [PERCENTRANK.INC](PERCENTRANK.INC.md) | Inclusive version that returns 0 and 1 at the extremes. |
| [RANK.AVG](RANK.AVG.md) | Returns an average position for tied values. |
| [RANK.EQ](RANK.EQ.md) | Returns the position of a value in the list. |

## Official Documentation

- [Microsoft Support: PERCENTRANK.EXC function](https://support.microsoft.com/en-us/excel/functions/percentrank-exc-function)
- [Google Docs Editors Help: PERCENTRANK.EXC](https://support.google.com/docs/answer/3267357)
