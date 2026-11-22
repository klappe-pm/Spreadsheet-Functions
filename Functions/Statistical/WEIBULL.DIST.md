---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Component Failure Rates
  - Light Bulb Lifetimes
  - Warranty Claims Forecast
related:
  - EXPON.DIST
  - GAMMA.DIST
  - LOGNORM.DIST
  - NORM.DIST
  - WEIBULL
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/weibull-dist-function
  - https://support.google.com/docs/answer/3094116
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Weibull Distribution
  - Weibull Probability
tags:
  - distribution
  - excel
  - reliability
  - sheets
---

# WEIBULL.DIST

## Description

**WEIBULL.DIST** returns values from the Weibull distribution, a flexible model for lifetimes, time to failure and waiting times. It returns either the probability density at a point (the height of the curve) or the cumulative probability that a value is at or below that point. Use it when you know the shape and scale of a lifetime distribution and want the chance that an item fails by a given age.

The shape parameter controls how the failure rate changes over time. A shape below 1 means items become less likely to fail as they age, a shape of 1 means the chance stays constant, and a shape above 1 means items wear out and become more likely to fail. When the shape is exactly 1, the Weibull distribution reduces to the exponential distribution, so EXPON.DIST with a rate of 1 divided by the scale gives the same cumulative result.

Microsoft Excel lists WEIBULL.DIST for Excel 2016 and later, including Microsoft 365 and Excel for the web. Google Sheets documents the same function as WEIBULL with the same four arguments, so use WEIBULL in Sheets. The Excel name WEIBULL.DIST is not listed on the Google help page.

## Syntax

```excel
=WEIBULL.DIST(x, alpha, beta, cumulative)
```

<!-- Image 1: Syntax Arguments on a Worksheet. See Images/Statistical/WEIBULL.DIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The value to evaluate, such as an age or a time. It must be numeric and cannot be negative; a negative value returns `#NUM!`. |
| `alpha` | Yes | The shape parameter. It must be greater than 0; zero or a negative value returns `#NUM!`. Google Sheets calls it `shape`. |
| `beta` | Yes | The scale parameter. It must be greater than 0; zero or a negative value returns `#NUM!`. Google Sheets calls it `scale`. |
| `cumulative` | Yes | `TRUE` returns the cumulative distribution function (the probability that the value is at or below `x`). `FALSE` returns the probability density function. |

### Return Value

A number. With `TRUE`, the result is a cumulative probability from 0 to 1. With `FALSE`, the result is the density at `x`, which is a height on the curve rather than a probability. The function returns `#VALUE!` when any numeric argument is text, and `#NUM!` when `x` is negative or when `alpha` or `beta` is 0 or less.

## Examples

All examples use a shape (`alpha`) of 1.5 and a scale (`beta`) of 5.

### Example 1: Cumulative Probability at a Point

```excel
=WEIBULL.DIST(2, 1.5, 5, TRUE)
```

**Result:** `0.223518`

About 22.4% of items are expected to fail by the time `x` reaches 2.

### Example 2: Probability Density at a Point

```excel
=WEIBULL.DIST(4, 1.5, 5, FALSE)
```

**Result:** `0.131193`

With `FALSE`, the function returns the height of the density curve at 4. Use this for plotting the curve or comparing shapes, not for reading a probability directly.

<!-- Image 2: Shape Comparison Curves. See Images/Statistical/WEIBULL.DIST.md -->

### Example 3: Chance of Surviving Past a Point

```excel
=1-WEIBULL.DIST(6, 1.5, 5, TRUE)
```

**Result:** `0.268599`

Subtracting the cumulative value from 1 gives the survival probability, the share of items still working after `x` is 6.

### Example 4: Cell References With Named Inputs

```excel
=WEIBULL.DIST(A2, Shape, Scale, TRUE)
```

**Result:** Depends on the values in `A2`, `Shape` and `Scale`.

Storing the shape and scale in named cells means one formula can be copied down a column of ages without editing the constants.

## Story Problems

### Problem 1: Pump Seal Failures

A maintenance team models the lifetime of a pump seal with a shape of 2 and a scale of 4 years. They want the share of seals that fail within 3 years.

| Input | Value | Cell |
| --- | --- | --- |
| Age to check (years) | 3 | `E2` |
| Shape | 2 | `E3` |
| Scale (years) | 4 | `E4` |

**Task:** Find the cumulative probability that a seal fails by year 3.

**Solution:**

```excel
=WEIBULL.DIST(E2, E3, E4, TRUE)
```

**Answer:** `0.430217`, so about 43% of seals are expected to fail by year 3.

<!-- Image 3: Results for the Pump Seal Story. See Images/Statistical/WEIBULL.DIST.md -->

### Problem 2: Bulb Burn Hours

A lighting supplier tests bulbs that follow a shape of 1 and a scale of 40 hours, which makes the lifetime exponential. The team wants the share of bulbs that fail within 50 hours.

| Input | Value | Cell |
| --- | --- | --- |
| Hours to check | 50 | `E2` |
| Shape | 1 | `E3` |
| Scale (hours) | 40 | `E4` |

**Task:** Find the cumulative probability that a bulb fails by 50 hours.

**Solution:**

```excel
=WEIBULL.DIST(E2, E3, E4, TRUE)
```

**Answer:** `0.713495`, so about 71% of bulbs fail within 50 hours. The same value comes from `=EXPON.DIST(50, 1/40, TRUE)`, which confirms the shape of 1 case.

## Use Cases

### Warranty Claims Forecast

**Scenario:** An appliance maker expects claims to rise as units age. Its engineers estimated a shape of 1.5 and a scale of 5 years for the failing part.

```excel
=WEIBULL.DIST(A2, Shape, Scale, TRUE)
```

**Why It Works:** Copying the formula down a column of ages gives the cumulative share of units that have failed by each age, which helps forecast claim volumes and reserves.

### Spare Parts Stock Planning

**Scenario:** A field service team wants the chance that a part installed today is still working after 2 years.

```excel
=1-WEIBULL.DIST(2, Shape, Scale, TRUE)
```

**Why It Works:** The survival probability tells the planner how many spare parts to keep on hand. Changing the shape or scale in the named cells updates the plan.

### Comparing Two Designs

**Scenario:** An engineer compares a sealed design with a shape of 2 and a cheaper design with a shape of 0.8, both with a scale of 4 years.

```excel
=WEIBULL.DIST(3, 2, 4, TRUE)
```

**Why It Works:** Evaluating both shapes at the same age shows which design fails sooner. A shape below 1 favors early failures, so the cheaper design may need a different warranty period.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `x` is negative. | Check that the age or time input is 0 or greater. |
| `#NUM!` | `alpha` or `beta` is 0 or less. | Enter a shape and scale greater than 0. |
| `#VALUE!` | An argument is text, such as a blank cell that contains a label. | Convert the input to a number or fix the reference. |
| Probability above 1 or unexpectedly small | `cumulative` is `FALSE`, so the density is returned. | Use `TRUE` for a probability. |
| Wrong result | The shape and scale are swapped. | Enter them in the order `alpha` (shape) then `beta` (scale). |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Microsoft 365 and Excel for the web | Arguments are named `x`, `alpha`, `beta` and `cumulative`. |
| Google Sheets | Available as `WEIBULL` | Same four arguments, named `x`, `shape`, `scale` and `cumulative`. The Google help page does not list `WEIBULL.DIST`. |

## Tips and Best Practices

- Store the shape and scale in labeled cells so the formula is easy to audit and reuse.
- Use `TRUE` for probabilities and `FALSE` only when you need the density curve.
- Check the shape against the physical story: a value near 1 suggests a constant failure rate, while a value above 1 suggests wear-out.
- Confirm that units match: if the scale is in years, the age must also be in years.
- Use `1-WEIBULL.DIST(...)` for survival probability rather than a separate formula.

## Related Functions

| Function | Relationship |
| --- | --- |
| [EXPON.DIST](EXPON.DIST.md) | Matches WEIBULL.DIST when the shape is 1, with a rate of 1 divided by the scale. |
| [GAMMA.DIST](GAMMA.DIST.md) | Another flexible skewed distribution for waiting times and sizes. |
| [LOGNORM.DIST](LOGNORM.DIST.md) | Models values whose logarithm is normally distributed, such as repair times. |
| [NORM.DIST](NORM.DIST.md) | Symmetric bell curve for measurements; use when the data is not skewed. |
| [WEIBULL](WEIBULL.md) | Legacy name for the same calculation in Google Sheets. |

## Official Documentation

- [Microsoft Support: WEIBULL.DIST function](https://support.microsoft.com/en-us/excel/functions/weibull-dist-function)
- [Google Docs Editors Help: WEIBULL](https://support.google.com/docs/answer/3094116)
