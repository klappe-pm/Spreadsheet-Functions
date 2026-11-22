---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Hypothesis Testing
  - Probability
use-case:
  - Confidence Interval Margins
  - Two-Sided Control Limits
related:
  - CONFIDENCE.T
  - T.DIST.2T
  - T.INV
  - T.TEST
  - TDIST
  - TINV
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/t-inv-2t-function
  - https://support.google.com/docs/answer/6055811
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Two Tailed Student T Critical Value
tags:
  - distribution
  - excel
  - hypothesis-test
  - sheets
  - statistical
---

# T.INV.2T

## Description

**T.INV.2T** returns the two-tailed critical t-value for a Student t-distribution. You give it the total probability that sits in both tails combined, and it returns the positive t-value that cuts off that probability, half in each tail. The result is the cutoff for a two-sided test or the multiplier for a two-sided confidence interval.

A common case is a 95 percent confidence interval, which leaves 5 percent in total outside the interval, so `probability` is 0.05. A two-sided test at the 1 percent level uses 0.01. Because the probability is the total of both tails, do not halve it before you enter it. For a one-sided cutoff, use T.INV with the single-tail probability instead.

The probability must be greater than 0 and no more than 1, and the degrees of freedom must be at least 1. Fractional degrees of freedom are truncated. The older TINV function returns the same two-tailed value and remains for compatibility.

## Syntax

```excel
=T.INV.2T(probability, deg_freedom)
```

<!-- Image 1: Two-Tailed Probability Split. See Images/Statistical/T.INV.2T.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | The total probability in both tails, such as 0.05 for a 95 percent two-sided interval. Must be greater than 0 and no more than 1. |
| `deg_freedom` | Yes | The degrees of freedom. A fractional value is truncated. Must be at least 1. |

### Return Value

A positive t-value. Excel returns `#NUM!` when `probability` is 0 or less, greater than 1, or when `deg_freedom` is less than 1. It returns `#VALUE!` when an argument is not numeric.

## Examples

### Example 1: Critical Value for a Two-Sided 5 Percent Test

```excel
=T.INV.2T(0.05, 18)
```

**Result:** `2.100922`

A t-value beyond 2.100922 in either direction with 18 degrees of freedom is significant at the 5 percent level.

### Example 2: Stricter One Percent Level

```excel
=T.INV.2T(0.01, 30)
```

**Result:** `2.749996`

The stricter level needs a larger cutoff, so the critical value grows.

### Example 3: Interval Multiplier

```excel
=T.INV.2T(0.1, 20)
```

**Result:** `1.724718`

A 90 percent two-sided interval with 20 degrees of freedom uses this multiplier on the standard error.

### Example 4: Probability Versus Cutoff

```excel
=T.INV.2T(0.546449, 60)
```

**Result:** `0.606533`

The function returns the t-value whose two-tailed probability equals the input, so a large input such as 0.546449 gives a small cutoff.

<!-- Image 2: Critical Values by Level. See Images/Statistical/T.INV.2T.md -->

### Example 5: Probability Outside the Range

```excel
=T.INV.2T(-0.05, 10)
```

**Result:** `#NUM!`

A probability of zero or less is not valid, so the function returns an error.

## Story Problems

### Problem 1: Two-Sided Test of a Price Change

A retailer compared sales before and after a price change over 19 weeks, which gives 18 degrees of freedom. The team uses a two-sided test at the 5 percent level, so it needs the critical t-value.

**Task:** Find the critical value for a two-sided test at the 5 percent level.

**Solution:**

```excel
=T.INV.2T(0.05, 18)
```

**Answer:** `2.100922`. A test statistic beyond 2.100922, positive or negative, counts as significant.

### Problem 2: Strict Quality Limit

A plant checks the mean fill weight of 31 samples, which gives 30 degrees of freedom. Its quality policy uses a two-sided 1 percent level.

**Task:** Find the critical t-value for the 1 percent two-sided level.

**Solution:**

```excel
=T.INV.2T(0.01, 30)
```

**Answer:** `2.749996`. The mean is flagged only when the standardized difference exceeds this value in either direction.

<!-- Image 3: Critical Value Worksheet. See Images/Statistical/T.INV.2T.md -->

## Use Cases

### Confidence Interval Margins

**Scenario:** A survey analyst reports a mean with a 95 percent interval and wants the margin of error in a single cell.

```excel
=T.INV.2T(0.05, B2 - 1) * C2 / SQRT(B2)
```

**Why It Works:** `B2` is the sample size and `C2` is the sample standard deviation. The critical value times the standard error gives the half-width of the interval.

### Two-Sided Control Limits

**Scenario:** An operations team sets control limits that flag a process mean drifting high or low.

```excel
=AVERAGE(Readings[Value]) + T.INV.2T(0.05, COUNT(Readings[Value]) - 1) * STDEV.S(Readings[Value]) / SQRT(COUNT(Readings[Value]))
```

**Why It Works:** The upper limit uses the critical value for both tails, so a mean below the lower limit or above the upper limit triggers the same review.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The probability is 0 or less, or greater than 1. | Enter the total two-tailed probability, between 0 and 1. |
| `#NUM!` | `deg_freedom` is less than 1. | Check the sample size. |
| Cutoff too small | The probability was halved before entering it. | Enter the total probability for both tails. |
| Cutoff for the wrong test | The question is one-sided, but this function assumes two tails. | Use T.INV with the single-tail probability. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2010 and later, including Microsoft 365 | Returns a positive two-tailed value. The older TINV returns the same two-tailed result. |
| Google Sheets | Available | Same arguments and order. The documentation does not list error messages, but the same range rules apply. |

## Tips and Best Practices

- Enter the total two-tailed probability, and never halve it first.
- Pair the critical value with a standard error to build a confidence interval.
- Keep the significance level in a labeled cell so the test level is visible.
- Use T.INV for one-sided cutoffs and T.INV.2T for two-sided cutoffs.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CONFIDENCE.T](CONFIDENCE.T.md) | Returns the margin of error for a sample mean using the t-distribution. |
| [T.DIST.2T](T.DIST.2T.md) | Returns the two-tailed probability, the reverse of this function. |
| [T.INV](T.INV.md) | Returns the one-tailed t-value for a single-tail probability. |
| [T.TEST](T.TEST.md) | Runs a complete t-test and returns its p-value for comparison. |
| [TDIST](TDIST.md) | Older function that returns one-tailed or two-tailed probabilities. |
| [TINV](TINV.md) | Older two-tailed inverse that returns the same value as this function. |

## Official Documentation

- [Microsoft Support: T.INV.2T function](https://support.microsoft.com/en-us/excel/functions/t-inv-2t-function)
- [Google Docs Editors Help: T.INV.2T](https://support.google.com/docs/answer/6055811)
