---
domain: Spreadsheet Functions
category: Statistical
subcategory: Ranking and Percentiles
purpose:
  - Statistical Analysis
use-case:
  - Exclusive Percentile Cutoffs
  - Support Ticket Benchmarks
related:
  - MEDIAN
  - PERCENTILE
  - PERCENTILE.INC
  - PERCENTRANK.EXC
  - QUARTILE.EXC
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/percentile-exc-function
  - https://support.google.com/docs/answer/9368167
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Exclusive Percentile
tags:
  - excel
  - exclusive
  - interpolation
  - percentile
  - sheets
---

# PERCENTILE.EXC

## Description

**PERCENTILE.EXC** returns the k-th percentile of the values in a range, where k must be strictly greater than 0 and strictly less than 1. Both ends are excluded, so the function never returns the smallest or largest value as a percentile unless the data falls exactly on a rank.

The valid range of k depends on how many values you have. The function ranks each value at position k × (n + 1), where n is the count of values, so the rank must fall between 1 and n. For example, with five values the page's own tests show that 0.15 and 0.9 return `#NUM!`, while 0.4, 0.5 and 0.8 return results. With nine values, the usable range runs from 0.1 to 0.9.

Use PERCENTILE.EXC when a rule requires an exclusive range, such as a cutoff that must sit inside the observed data. Use PERCENTILE.INC when k can be 0 or 1. PERCENTILE.EXC replaces the compatibility function PERCENTILE for exclusive ranges.

## Syntax

```excel
=PERCENTILE.EXC(array, k)
```

<!-- Image 1: Exclusive Percentile Arguments. See Images/Statistical/PERCENTILE.EXC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array of values that defines the distribution, for example `A2:A10`. |
| `k` | Yes | The percentile to return, as a decimal strictly between 0 and 1. Enter 0.25 for the 25th percentile. |

### Return Value

The k-th percentile as a number, interpolated when k falls between two ranked values. The function returns `#NUM!` when the array is empty, when k is 0 or 1 or beyond the range the data allows, and `#VALUE!` when k is not numeric.

## Examples

All examples use these nine values in `A2:A10`: 14, 22, 27, 31, 35, 40, 46, 52 and 60.

### Example 1: Lower Quartile Without the Endpoints

```excel
=PERCENTILE.EXC(A2:A10, 0.25)
```

**Result:** `24.5`

The rank is 0.25 × 10 = 2.5, halfway between the second value (22) and the third value (27).

### Example 2: Upper Quartile

```excel
=PERCENTILE.EXC(A2:A10, 0.75)
```

**Result:** `49`

The rank is 7.5, halfway between 46 and 52.

### Example 3: The Median

```excel
=PERCENTILE.EXC(A2:A10, 0.5)
```

**Result:** `35`

With an odd count of values, the median rank is the fifth value.

### Example 4: Handling a Percentile Outside the Valid Range

```excel
=IFERROR(PERCENTILE.EXC(A2:A10, 0.05), "Out of Range")
```

**Result:** `Out of Range`

The rank for k = 0.05 is 0.5, which is below the first value, so the function returns `#NUM!` and IFERROR shows the message.

## Story Problems

### Problem 1: Support Ticket Resolution Times

A help desk records the hours it took to resolve nine tickets in `A2:A10`: 2, 3, 5, 8, 9, 12, 15, 20 and 26.

**Task:** Find the resolution time at the exclusive 25th percentile, which the team uses as its fast-track target.

**Solution:**

```excel
=PERCENTILE.EXC(A2:A10, 0.25)
```

**Answer:** `4` hours. The rank is 0.25 × 10 = 2.5, halfway between 3 and 5.

### Problem 2: Escalation Threshold Request

The same nine tickets appear in `A2:A10`. A manager asks for the exclusive 95th percentile as the escalation threshold.

**Task:** Compute the threshold with PERCENTILE.EXC and report the result.

**Solution:**

```excel
=PERCENTILE.EXC(A2:A10, 0.95)
```

**Answer:** `#NUM!`. The rank is 0.95 × 10 = 9.5, which is above the ninth value. For this threshold, use `=PERCENTILE.INC(A2:A10, 0.95)`, which returns 23.6.

<!-- Image 2: Exclusive Rank Between Two Values. See Images/Statistical/PERCENTILE.EXC.md -->

## Use Cases

### Exclusive Percentile Cutoffs

**Scenario:** A quality team wants a cutoff at the 25th percentile of test scores, and the rule forbids using the lowest recorded score as the cutoff.

```excel
=PERCENTILE.EXC(Scores[Points], 0.25)
```

**Why It Works:** The exclusive range keeps the cutoff inside the observed data. With few scores, wrap the formula in IFERROR, because a valid k depends on the number of values.

### Support Ticket Benchmarks

**Scenario:** A support manager sets a benchmark at the exclusive 75th percentile of resolution times.

```excel
=PERCENTILE.EXC(Tickets[Hours], 0.75)
```

**Why It Works:** The result is interpolated between two tickets, so it can be a decimal such as 49. Round the value for the report if the team works in whole hours.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | k is 0 or 1, or the rank k × (n + 1) is below 1 or above n. | Choose a k inside the range the data allows, or use PERCENTILE.INC for the endpoints. |
| `#NUM!` | The array is empty. | Check that the range holds values. |
| `#VALUE!` | k is text or a blank reference. | Enter k as a number. |
| Decimal result | The percentile falls between two values. | Round the result for display if needed. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions | Accepts k only in the open interval from 0 to 1, and returns `#NUM!` when interpolation is not possible. |
| Google Sheets | Available | Arguments are named `data` and `percentile`. The percentile must be strictly between 0 and 1, and the function returns `#NUM!` when it cannot interpolate. |

## Tips and Best Practices

- Calculate the valid k range before you publish a threshold: with n values, k must lie between 1 ÷ (n + 1) and n ÷ (n + 1).
- Use PERCENTILE.INC when the rule allows the minimum or maximum, because it accepts 0 and 1.
- Store k in a labeled input cell so reviewers can see and change the threshold.
- Test the formula with a small list where you can count the ranks by hand.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PERCENTILE.INC](PERCENTILE.INC.md) | Inclusive version that accepts 0 and 1. |
| [PERCENTILE](PERCENTILE.md) | Compatibility function that PERCENTILE.EXC and PERCENTILE.INC replace. |
| [PERCENTRANK.EXC](PERCENTRANK.EXC.md) | Returns the exclusive rank of a value, the reverse lookup. |
| [MEDIAN](MEDIAN.md) | Gives the same result as k = 0.5. |
| [QUARTILE.EXC](QUARTILE.EXC.md) | Returns exclusive quartile cut points of the same data. |

## Official Documentation

- [Microsoft Support: PERCENTILE.EXC function](https://support.microsoft.com/en-us/excel/functions/percentile-exc-function)
- [Google Docs Editors Help: PERCENTILE.EXC](https://support.google.com/docs/answer/9368167)
