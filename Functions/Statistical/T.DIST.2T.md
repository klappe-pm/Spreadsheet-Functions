---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Hypothesis Testing
  - Probability
use-case:
  - Two-Tailed Experiment Results
  - Two-Tailed Quality Alerts
related:
  - T.DIST
  - T.DIST.RT
  - T.INV.2T
  - T.TEST
  - TDIST
  - TINV
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/t-dist-2t-function
  - https://support.google.com/docs/answer/9368252
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Two Tailed Student T Probability
tags:
  - distribution
  - excel
  - hypothesis-test
  - sheets
  - statistical
---

# T.DIST.2T

## Description

**T.DIST.2T** returns the two-tailed probability of a Student t-value. It adds together the area in the left tail and the area in the right tail beyond the absolute value of `x`, so the result is the chance of seeing a difference at least this large in either direction. Use it when a test asks whether two results differ, without caring which one is larger.

The function accepts only a non-negative `x`. A negative `x` returns `#NUM!` in Excel. When your statistic is negative, wrap it in ABS, because the two-tailed probability is the same for `x` and `-x`. The degrees of freedom must be at least 1.

T.DIST.2T replaces the older TDIST function when `tails` is set to 2, and it is the two-tailed counterpart of T.DIST.RT. Use T.DIST.RT for a one-tailed question, and T.DIST for the full cumulative distribution.

## Syntax

```excel
=T.DIST.2T(x, deg_freedom)
```

<!-- Image 1: Two Tails of the Distribution. See Images/Statistical/T.DIST.2T.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The non-negative t-value at which to evaluate the two-tailed probability. Use ABS for a negative statistic. |
| `deg_freedom` | Yes | The degrees of freedom, usually the sample size minus one for a single sample. Must be at least 1. |

### Return Value

A probability between 0 and 1. Excel returns `#NUM!` when `x` is negative or `deg_freedom` is less than 1, and `#VALUE!` when an argument is not numeric.

## Examples

### Example 1: Two-Tailed Probability for a Test Statistic

```excel
=T.DIST.2T(2.5, 20)
```

**Result:** `0.021234`

Only about 2.1 percent of t-values with 20 degrees of freedom would land this far from zero in either direction.

### Example 2: Large Sample Comparison

```excel
=T.DIST.2T(1.96, 60)
```

**Result:** `0.054645`

With 60 degrees of freedom this is close to the familiar 5 percent two-tailed level.

### Example 3: Small Degrees of Freedom

```excel
=T.DIST.2T(1, 2)
```

**Result:** `0.422650`

With only 2 degrees of freedom, a t-value of 1 is far from unusual, so the probability is high.

### Example 4: Negative Statistic With ABS

```excel
=T.DIST.2T(ABS(-1.8), 15)
```

**Result:** `0.092002`

ABS turns the negative statistic into a non-negative value, and the two-tailed probability is unchanged by the sign.

<!-- Image 2: Negative Statistic Handling. See Images/Statistical/T.DIST.2T.md -->

### Example 5: Negative Input Without ABS

```excel
=T.DIST.2T(-1.8, 15)
```

**Result:** `#NUM!`

The function rejects a negative `x`, so wrap the statistic in ABS first.

## Story Problems

### Problem 1: Price Change Test

A retailer compared a new price against the old one across 21 weeks, which gives 20 degrees of freedom. The test statistic is 2.5. The question is whether the sales change differs from zero in either direction.

| Weeks | Degrees of Freedom | Test Statistic |
| --- | --- | --- |
| 21 | 20 | 2.5 |

**Task:** Find the two-tailed probability for the test statistic.

**Solution:**

```excel
=T.DIST.2T(2.5, 20)
```

**Answer:** `0.021234`. The change is unlikely to be chance alone at the usual 5 percent level.

### Problem 2: Support Ticket Times

A help desk measured the response time difference between two teams on 16 tickets, giving 15 degrees of freedom. The statistic came out as -1.8, and the team needs the two-tailed probability.

**Task:** Find the two-tailed probability using the absolute value of the statistic.

**Solution:**

```excel
=T.DIST.2T(ABS(B2), 15)
```

**Answer:** `0.092002`, where `B2` holds -1.8. The result is above 0.05, so the difference is not strong evidence on its own.

<!-- Image 3: Support Ticket Worksheet. See Images/Statistical/T.DIST.2T.md -->

## Use Cases

### Two-Tailed Experiment Results

**Scenario:** A product team runs an A/B test and wants to know whether the conversion gap is real, whichever version performed better.

```excel
=T.DIST.2T(ABS(B2), C2)
```

**Why It Works:** `B2` holds the test statistic and `C2` holds the degrees of freedom calculated for the test design. ABS makes the formula safe for either direction of difference.

### Two-Tailed Quality Alerts

**Scenario:** A plant wants an alert when a batch's mean weight differs from target, high or low.

```excel
=IF(T.DIST.2T(ABS(B2), 9) < 0.05, "Investigate", "Within Range")
```

**Why It Works:** A two-tailed threshold flags shifts in both directions, which a one-tailed test would miss on the low side.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `x` is negative. | Wrap the statistic in ABS. |
| `#NUM!` | `deg_freedom` is less than 1. | Check the sample size. |
| `#VALUE!` | An argument is text or blank. | Confirm both inputs are numbers. |
| Result looks double | The one-tailed value was doubled by hand. | Use this function directly rather than doubling T.DIST.RT. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2010 and later, including Microsoft 365 | Returns `#NUM!` for negative `x`. The page states it replaces TDIST with `tails` set to 2. |
| Google Sheets | Available | Same arguments and order. The documentation also states the negative-`x` error. |

## Tips and Best Practices

- Use ABS on the statistic so the formula works regardless of the sign of the difference.
- Pick the tail before you see the data, because choosing after seeing the sign inflates false alarms.
- Compare the result with a significance level in a separate cell so the threshold is easy to change.
- Use T.INV.2T to find the critical value that matches the same two-tailed level.

## Related Functions

| Function | Relationship |
| --- | --- |
| [T.DIST](T.DIST.md) | Returns the cumulative or density value rather than the two-tailed probability. |
| [T.DIST.RT](T.DIST.RT.md) | One-tailed right-tail probability. Use it when only one direction matters. |
| [T.INV.2T](T.INV.2T.md) | Returns the two-tailed critical t-value for a given probability, the reverse of this function. |
| [T.TEST](T.TEST.md) | Runs a complete t-test on two data sets and returns its p-value. |
| [TDIST](TDIST.md) | Older function that returns the same two-tailed result when `tails` is 2. |
| [TINV](TINV.md) | Older two-tailed inverse of the t-distribution. |

## Official Documentation

- [Microsoft Support: T.DIST.2T function](https://support.microsoft.com/en-us/excel/functions/t-dist-2t-function)
- [Google Docs Editors Help: T.DIST.2T](https://support.google.com/docs/answer/9368252)
