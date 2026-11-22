---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Probability
use-case:
  - Component Lifetime Planning
  - Failure Probability Estimates
related:
  - BETA.DIST
  - EXPON.DIST
  - GAMMA.DIST
  - NORM.DIST
  - WEIBULL.DIST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/weibull-function
  - https://support.google.com/docs/answer/3094116
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Weibull Distribution
tags:
  - compatibility
  - distribution
  - excel
  - reliability
  - sheets
---

# WEIBULL

## Description

**WEIBULL** returns the Weibull distribution for a value x, either as a probability density or as a cumulative probability. The Weibull distribution is widely used to model lifetimes and time to failure, because its shape parameter can describe failures that become more likely with age, less likely with age, or occur at a steady rate.

Set `cumulative` to TRUE to get the probability that the value is at or below x, which answers questions such as how many units fail within a given time. Set it to FALSE to get the density, the height of the distribution curve at x, which is useful for charts and for comparing shapes. The probability that a value falls between two points is the difference between two cumulative results.

WEIBULL is a legacy compatibility function. Microsoft states that it has been replaced by WEIBULL.DIST, which takes the same arguments and gives the same results. WEIBULL remains available for older workbooks but may be removed in future versions of Excel. When the shape parameter is 1, the distribution is exponential with a rate equal to 1 divided by the scale, which EXPON.DIST computes directly.

## Syntax

```excel
=WEIBULL(x,alpha,beta,cumulative)
```

<!-- Image 1: The Weibull Parameters on a Curve. See Images/Statistical/WEIBULL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The value at which to evaluate the distribution. It cannot be negative. |
| `alpha` | Yes | The shape parameter, which must be greater than 0. Google Sheets calls it `shape`. |
| `beta` | Yes | The scale parameter, which must be greater than 0. Google Sheets calls it `scale`. |
| `cumulative` | Yes | TRUE returns the cumulative distribution, the probability of a value at or below x. FALSE returns the probability density. |

### Return Value

A number: the cumulative probability when `cumulative` is TRUE, or the density when it is FALSE. The function returns `#VALUE!` when any numeric argument is not a number, and `#NUM!` when x is negative or when alpha or beta is 0 or less.

## Examples

These examples use the arguments x = 2, alpha = 1.5 and beta = 3 unless a different value is given.

### Example 1: Cumulative Probability

```excel
=WEIBULL(2,1.5,3,TRUE)
```

**Result:** `0.4198`

About 42 percent of units in this distribution fail at or before x = 2.

### Example 2: Probability Density

```excel
=WEIBULL(2,1.5,3,FALSE)
```

**Result:** `0.2369`

The density at x = 2 is 0.2369. Densities describe the shape of the curve rather than a probability, so they are not read as percentages.

### Example 3: Exponential Special Case

```excel
=WEIBULL(2,1,3,TRUE)
```

**Result:** `0.4866`

With alpha set to 1, the result equals 1 minus the exponential survival at 2 with a rate of 1/3. EXPON.DIST(2,1/3,TRUE) returns the same value.

### Example 4: Probability Between Two Points

```excel
=WEIBULL(4,1.5,3,TRUE)-WEIBULL(2,1.5,3,TRUE)
```

**Result:** `0.3658`

The probability that a value falls between 2 and 4 is the cumulative value at 4 minus the cumulative value at 2. The unrounded values are 0.78553 and 0.41977, so the difference is 0.36576.

### Example 5: The Replacement Function

```excel
=WEIBULL.DIST(2,1.5,3,TRUE)
```

**Result:** `0.4198`

WEIBULL.DIST returns the same cumulative probability as WEIBULL. Use it in new formulas.

## Story Problems

### Problem 1: Fan Motor Failures

A manufacturer models the time to failure of a fan motor with a Weibull distribution, where alpha is 1.8 and beta is 1200 operating hours. The reliability team wants the share of motors that fail between 600 and 900 hours, to plan spare stock.

| Parameter | Value |
| --- | --- |
| Shape (alpha) | 1.8 |
| Scale (beta) | 1200 hours |
| Window start | 600 hours |
| Window end | 900 hours |

**Task:** Compute the probability that a motor fails between 600 and 900 hours.

**Solution:**

```excel
=WEIBULL(900,1.8,1200,TRUE)-WEIBULL(600,1.8,1200,TRUE)
```

**Answer:** `0.1993`. The cumulative probability is 0.4489 by 900 hours and 0.2496 by 600 hours, and the difference is 0.1993. About 20 percent of motors fail inside that window.

<!-- Image 2: Failure Window on the Cumulative Curve. See Images/Statistical/WEIBULL.md -->

### Problem 2: Bulb Survival Past 1000 Hours

A lighting supplier uses the same Weibull model for a bulb, with alpha of 1.8 and beta of 1200 hours. The supplier wants the probability that a bulb is still working after 1000 hours, which is the complement of the cumulative value.

| Parameter | Value |
| --- | --- |
| Shape (alpha) | 1.8 |
| Scale (beta) | 1200 hours |
| Hours of operation | 1000 |

**Task:** Compute the probability that a bulb survives beyond 1000 hours.

**Solution:**

```excel
=1-WEIBULL(1000,1.8,1200,TRUE)
```

**Answer:** `0.4866`. The cumulative probability by 1000 hours is 0.5134, so about 49 percent of bulbs are still working past that point.

## Use Cases

### Component Lifetime Planning

**Scenario:** A maintenance planner wants the probability that a pump seal fails before its scheduled service interval.

```excel
=WEIBULL(Service_Interval,Shape,Scale,TRUE)
```

**Why It Works:** The shape and scale come from fitted lifetime data, and the service interval is a named input. Changing the interval updates the probability without rewriting the formula.

### Failure Probability Estimates

**Scenario:** A reliability engineer compares the failure density at different ages to see when failures are most likely.

```excel
=WEIBULL(Age_Hours,Shape,Scale,FALSE)
```

**Why It Works:** The density shows where the failure rate is highest. Plot the density across a range of ages to see the peak of the curve.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | `x`, `alpha` or `beta` is not a number. | Enter numbers, or reference cells that hold numbers. |
| `#NUM!` | `x` is negative. | Use a value of 0 or greater. |
| `#NUM!` | `alpha` or `beta` is 0 or less. | Enter a positive shape and a positive scale. |
| Unexpected result | `cumulative` is FALSE, so the density is returned instead of the probability. | Set `cumulative` to TRUE for probabilities. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Legacy compatibility function. Microsoft recommends WEIBULL.DIST, and WEIBULL may be removed from future versions. |
| Google Sheets | Available | Takes `WEIBULL(x, shape, scale, cumulative)`. The official page requires shape and scale to be greater than 0, and TRUE returns the cumulative distribution while FALSE returns the density. |

## Tips and Best Practices

- Use WEIBULL.DIST in new work, and keep WEIBULL only in workbooks that already rely on it.
- Check that the shape and scale come from a fitted model before reporting probabilities.
- Use the difference of two cumulative values to find the probability of a range.
- Remember that FALSE returns a density, which is not a probability, so do not format it as a percentage.
- Use EXPON.DIST when the shape is 1, because the formula is simpler to read.

## Related Functions

| Function | Relationship |
| --- | --- |
| [WEIBULL.DIST](WEIBULL.DIST.md) | Modern replacement with the same arguments and results. |
| [EXPON.DIST](EXPON.DIST.md) | Exponential distribution, the special case when the shape is 1. |
| [GAMMA.DIST](GAMMA.DIST.md) | Another distribution for waiting times and skewed positive data. |
| [NORM.DIST](NORM.DIST.md) | Normal distribution for symmetric data. |
| [BETA.DIST](BETA.DIST.md) | Distribution for values bounded between 0 and 1. |

## Official Documentation

- [Microsoft Support: WEIBULL function](https://support.microsoft.com/en-us/excel/functions/weibull-function)
- [Google Docs Editors Help: WEIBULL](https://support.google.com/docs/answer/3094116)
