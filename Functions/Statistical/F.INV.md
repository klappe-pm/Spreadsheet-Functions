---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Confidence Interval Bounds
  - Percentile Thresholds
related:
  - F.DIST
  - F.DIST.RT
  - F.INV.RT
  - FINV
  - NORM.S.INV
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/f-inv-function
  - https://support.google.com/docs/answer/7004265
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Left Tailed F Inverse
tags:
  - distribution
  - excel
  - inverse
  - probability
  - sheets
---

# F.INV

## Description

**F.INV** returns the F value at which the left-tailed cumulative probability equals the `probability` you supply. It is the inverse of F.DIST with `cumulative` set to TRUE. If `p` equals F.DIST(x, df1, df2, TRUE), then F.INV(p, df1, df2) returns `x`.

Use F.INV when you know the probability and need the threshold. A common case is the lower bound of a confidence interval for a ratio of two variances. Another is a percentile threshold, such as the value that 90 percent of ratios fall below.

For the right tail, use F.INV.RT instead. The two functions are not interchangeable: F.INV(0.05, df1, df2) returns a value below 1 in many cases, while F.INV.RT(0.05, df1, df2) returns the usual upper critical value for a 5 percent test.

The probability must be between 0 and 1. The degrees of freedom are each sample size minus 1, and non-integer values are truncated.

## Syntax

```excel
=F.INV(probability, deg_freedom1, deg_freedom2)
```

<!-- Image 1: Left Tail Threshold on the F Curve. See Images/Statistical/F.INV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | The cumulative probability from the left tail, from 0 to 1. |
| `deg_freedom1` | Yes | The numerator degrees of freedom, which is the numerator sample size minus 1. |
| `deg_freedom2` | Yes | The denominator degrees of freedom, which is the denominator sample size minus 1. |

### Return Value

The F value whose left-tail probability equals `probability`. Excel returns `#VALUE!` when an argument is not numeric, and `#NUM!` when the probability is outside 0 to 1 or a degrees-of-freedom value is less than 1.

## Examples

### Example 1: Ninetieth Percentile Threshold

```excel
=F.INV(0.9, 4, 20)
```

**Result:** `2.2489` (rounded to four decimal places)

Ninety percent of variance ratios with 4 and 20 degrees of freedom fall at or below 2.2489.

### Example 2: Lower Tail Threshold

```excel
=F.INV(0.05, 10, 10)
```

**Result:** `0.3358` (rounded to four decimal places)

Only 5 percent of ratios fall below 0.3358 for these degrees of freedom. The result is below 1 because the lower tail sits on the small-ratio side.

<!-- Image 2: Percentile Threshold Versus Cumulative Probability. See Images/Statistical/F.INV.md -->

### Example 3: Round Trip With F.DIST

```excel
=F.INV(F.DIST(2, 8, 10, TRUE), 8, 10)
```

**Result:** `2`

F.DIST converts 2 to a cumulative probability of 0.8492, and F.INV converts that probability back to 2. The round trip confirms the two functions use the same distribution.

## Story Problems

### Problem 1: Lower Bound for a Variance Ratio

Two assembly stations have been sampled for bolt torque. Station A has 11 readings and Station B has 13 readings. The team wants the lower bound of a 95 percent interval for the variance ratio, which uses 2.5 percent in the left tail.

| Station | Sample Size |
| --- | --- |
| Station A | 11 |
| Station B | 13 |

**Task:** Find the lower critical value for the 95 percent interval, using the sample sizes in `B2:B3`.

**Solution:**

```excel
=F.INV(0.025, B2-1, B3-1)
```

**Answer:** `0.2762`. The degrees of freedom are 10 and 12. A ratio below this value would fall outside the lower bound.

### Problem 2: Ninetieth Percentile of Run Ratios

A process engineer compares two production runs. Run 1 has 5 samples and Run 2 has 21 samples. She wants the ratio that 90 percent of comparisons fall below.

| Run | Sample Size |
| --- | --- |
| Run 1 | 5 |
| Run 2 | 21 |

**Task:** Find the 90th percentile of the variance ratio, using the sample sizes in `B2:B3`.

**Solution:**

```excel
=F.INV(0.9, B2-1, B3-1)
```

**Answer:** `2.2489`. The degrees of freedom are 4 and 20, the same as Example 1. Any ratio above 2.2489 falls in the top 10 percent.

## Use Cases

### Confidence Interval Bounds

**Scenario:** An analyst builds a 95 percent confidence interval for the ratio of two process variances.

```excel
=F.INV(0.025, n1-1, n2-1)
```

**Why It Works:** This returns the lower bound. The upper bound uses F.INV.RT with the same 0.025 probability and degrees of freedom. Both bounds are needed to report the interval.

### Percentile Thresholds

**Scenario:** A quality lead wants a cutoff so that only the most variable 10 percent of batches trigger a review.

```excel
=F.INV(0.9, DaysA-1, DaysB-1)
```

**Why It Works:** The formula returns the 90th percentile of the variance ratio for the two batch sets. Any ratio above the cutoff is flagged, and the cutoff updates when the sample sizes change.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The probability is less than 0 or greater than 1. | Enter a probability between 0 and 1, such as 0.05 for 5 percent. |
| `#NUM!` | A degrees-of-freedom value is less than 1. | Check that each sample has at least two values. |
| `#VALUE!` | An argument is text. | Convert the value or fix the reference. |
| Probability read as a percentage | The value 5 was typed instead of 0.05. | Type 0.05 or format the cell with a percent sign and let Excel convert it. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current Excel, including Excel for the web | Probability may equal 0 or 1 in Excel, which is documented as inclusive. |
| Google Sheets | Available | Requires the probability to be strictly between 0 and 1. Both degrees-of-freedom values must be at least 1. |

## Tips and Best Practices

- Use F.INV for the left tail and F.INV.RT for the right tail, and label each cell so readers know which one they are reading.
- Put the probability in its own cell so the threshold can be changed without editing the formula.
- Round the output only for display, not inside later calculations.
- Pair the result with the sample sizes in the same table, so the degrees of freedom are visible.

## Related Functions

| Function | Relationship |
| --- | --- |
| [F.DIST](F.DIST.md) | Returns the probability for a given x, the forward calculation of this function. |
| [F.DIST.RT](F.DIST.RT.md) | Returns the right-tail probability for a given x. |
| [F.INV.RT](F.INV.RT.md) | Returns the value for a right-tail probability, used for upper bounds and critical values. |
| [FINV](FINV.md) | Legacy right-tail inverse kept for older workbooks. |
| [NORM.S.INV](NORM.S.INV.md) | Inverse of the standard normal distribution, used for z based intervals. |

## Official Documentation

- [Microsoft Support: F.INV function](https://support.microsoft.com/en-us/excel/functions/f-inv-function)
- [Google Docs Editors Help: F.INV](https://support.google.com/docs/answer/7004265)
