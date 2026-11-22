---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Hypothesis Testing
  - Probability
  - Statistical Analysis
use-case:
  - Chi Squared Density Plots
  - Sample Variance Review
  - Variance Confidence Checks
related:
  - CHIDIST
  - CHISQ.DIST.RT
  - CHISQ.INV
  - CHISQ.TEST
  - GAMMA.DIST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/chisq-dist-function
  - https://support.google.com/docs/answer/7003347
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Chi Squared Distribution
  - Chi Squared Cumulative
tags:
  - chi-squared
  - distributions
  - excel
  - probability
  - sheets
---

# CHISQ.DIST

## Description

**CHISQ.DIST** returns the chi-squared distribution at a value x. It takes a single number and a degrees-of-freedom count, and a logical argument chooses the form. TRUE returns the left-tail cumulative probability: the chance that a chi-squared value is at or below x. FALSE returns the probability density at x, which is useful for drawing the shape of the distribution.

Most hypothesis tests need the right tail instead, which is the chance of a value at or above x. Use CHISQ.DIST.RT for that. Use CHISQ.DIST when you need the left tail, a confidence bound on a variance, or the density for a chart.

CHISQ.DIST replaced the legacy CHIDIST function for the left-tail and density forms. Microsoft recommends CHISQ.DIST and CHISQ.DIST.RT in place of CHIDIST, so new workbooks should use the modern names.

## Syntax

```excel
=CHISQ.DIST(x, deg_freedom, cumulative)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/CHISQ.DIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The value at which to evaluate the distribution. It must not be negative. |
| `deg_freedom` | Yes | The number of degrees of freedom. It must be from 1 to 10^10. Non-integers are truncated. |
| `cumulative` | Yes | TRUE returns the cumulative distribution function (left tail). FALSE returns the probability density function. |

### Return Value

A number. For TRUE, a probability from 0 to 1. For FALSE, a density, which can exceed 1 for some inputs. The function returns `#VALUE!` when an argument is not numeric. It returns `#NUM!` when `x` is negative, or when `deg_freedom` is below 1 or above 10^10.

## Examples

### Example 1: Left-Tail Probability

```excel
=CHISQ.DIST(3, 4, TRUE)
```

**Result:** `0.4422`

About 44 percent of a chi-squared distribution with 4 degrees of freedom lies at or below 3.

### Example 2: Density at a Point

```excel
=CHISQ.DIST(3, 4, FALSE)
```

**Result:** `0.1673`

FALSE returns the height of the density curve at x = 3. The value is a density, not a probability, so it is not a chance on its own.

### Example 3: Reading Inputs From Cells

Row 2 holds the value 2.5 in `B2`, 5 degrees of freedom in `C2` and the logical value TRUE in `D2`.

```excel
=CHISQ.DIST(B2, C2, D2)
```

**Result:** `0.2235`

Keeping the cumulative flag in a cell makes it easy to switch between the probability and the density when building a chart.

<!-- Image 2: Cumulative Versus Density. See Images/Statistical/CHISQ.DIST.md -->

### Example 4: Density Peak for Two Degrees of Freedom

```excel
=CHISQ.DIST(2, 2, FALSE)
```

**Result:** `0.1839`

With 2 degrees of freedom the density falls steadily from x = 0, so this value sits near the start of the curve. It equals half of e raised to the power of minus 1.

## Story Problems

### Problem 1: Consistency Test Statistic

A team models a consistency test statistic with 5 degrees of freedom. The reviewer wants to know the chance that the statistic comes in at or below 2.5, which would signal unusually consistent results.

| Input | Value |
| --- | --- |
| Statistic | 2.5 |
| Degrees of Freedom | 5 |
| Cumulative | TRUE |

**Task:** Find the left-tail probability using the inputs in `B1:B3`.

**Solution:**

```excel
=CHISQ.DIST(B1, B2, B3)
```

**Answer:** `0.2235`. About 22 percent of results are at or below that level.

### Problem 2: Density Height for a Chart

A chart plots the density curve for 2 degrees of freedom. The analyst needs the height of the curve at x = 6 to label one point.

| Input | Value |
| --- | --- |
| Statistic | 6 |
| Degrees of Freedom | 2 |
| Cumulative | FALSE |

**Task:** Find the density height at the statistic using the inputs in `B1:B3`.

**Solution:**

```excel
=CHISQ.DIST(B1, B2, B3)
```

**Answer:** `0.0249`. The density is a height on the curve, so it should be labeled as a density and not as a probability.

## Use Cases

### Chi Squared Density Plots

**Scenario:** An analyst builds a column of x values from 0 to 20 and wants the density for 4 degrees of freedom to plot the curve.

```excel
=CHISQ.DIST(A2, $B$1, FALSE)
```

**Why It Works:** The degrees of freedom sit in a fixed cell, and the x value changes row by row. Copying the formula down creates the whole curve.

### Sample Variance Review

**Scenario:** A quality analyst compares the sample variance of a process with a known target variance. The statistic (n minus 1) times the sample variance divided by the target variance follows a chi-squared distribution with n minus 1 degrees of freedom.

```excel
=CHISQ.DIST(B3 * C3 / D3, B3, TRUE)
```

**Why It Works:** `B3` holds n minus 1, `C3` holds the sample variance and `D3` holds the target variance. The formula returns the left-tail probability of that statistic.

### Variance Confidence Checks

**Scenario:** A lab wants the probability that a chi-squared statistic of 12.5 with 9 degrees of freedom falls at or below its observed value.

```excel
=CHISQ.DIST(12.5, 9, TRUE)
```

**Why It Works:** The left-tail value shows how much of the distribution lies below the observed statistic, which supports a lower confidence bound.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `x` is negative. | Chi-squared values are never negative, so check the statistic formula. |
| `#NUM!` | `deg_freedom` is below 1 or above 10^10. | Enter a whole number of degrees of freedom within the range. |
| `#VALUE!` | An argument is text. | Convert the inputs to numbers. |
| Result is too large or too small | The logical argument is wrong. | Use TRUE for the probability and FALSE for the density. |
| Result is greater than 1 | FALSE was used and a density was returned. | Densities are heights, not probabilities. Use TRUE when you need a probability. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Replaces CHIDIST for the left tail and the density. Use CHISQ.DIST.RT for the right tail. |
| Google Sheets | Available | Same arguments in the same order. The value x must be positive, and degrees of freedom must be from 1 to 10^10. |

## Tips and Best Practices

- Use TRUE when the question asks for a probability and FALSE only when you need the density for a chart or a calculation.
- Use CHISQ.DIST.RT for the p-value of a test, because hypothesis tests use the right tail.
- Truncate degrees of freedom yourself if they come from a calculation that can return decimals.
- Check the result with CHISQ.INV, which returns the x value for a given left-tail probability.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHIDIST](CHIDIST.md) | The legacy right-tail function that CHISQ.DIST.RT replaces. |
| [CHISQ.DIST.RT](CHISQ.DIST.RT.md) | Returns the right-tail probability, which most tests need. |
| [CHISQ.INV](CHISQ.INV.md) | Returns the x value for a left-tail probability, the reverse of this function. |
| [CHISQ.TEST](CHISQ.TEST.md) | Returns the p-value for a table of observed and expected counts. |
| [GAMMA.DIST](../Statistical/GAMMA.DIST.md) | Models the gamma family, which includes the chi-squared distribution as a special case. |

## Official Documentation

- [Microsoft Support: CHISQ.DIST function](https://support.microsoft.com/en-us/excel/functions/chisq-dist-function)
- [Google Docs Editors Help: CHISQ.DIST](https://support.google.com/docs/answer/7003347)
