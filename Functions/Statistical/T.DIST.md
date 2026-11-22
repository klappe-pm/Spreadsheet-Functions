---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Hypothesis Testing
  - Probability
use-case:
  - Left Tail Risk
  - Model Coefficient Checks
  - Small Sample Probability
related:
  - T.DIST.2T
  - T.DIST.RT
  - T.INV
  - T.INV.2T
  - T.TEST
  - TDIST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/t-dist-function
  - https://support.google.com/docs/answer/9369014
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Student T Cumulative Distribution
tags:
  - distribution
  - excel
  - probability
  - sheets
  - statistical
---

# T.DIST

## Description

**T.DIST** returns the Student t-distribution at a value `x`. With `cumulative` set to `TRUE`, it returns the probability that a t-value is less than or equal to `x`, which is the left-tail area. With `cumulative` set to `FALSE`, it returns the height of the probability density curve at `x`.

Use T.DIST when your sample is small, usually fewer than 30 observations, and the population standard deviation is unknown. The t-distribution has a little more spread than the normal curve, and that extra spread matters most when the degrees of freedom are low. As the degrees of freedom grow, the t-distribution approaches the normal curve.

The cumulative form answers questions such as "how likely is a result this low or lower?" For the upper tail, subtract the cumulative result from 1 or use T.DIST.RT. For a two-tailed test, use T.DIST.2T, which accepts only a non-negative `x`. T.DIST replaces TDIST for one-tailed work, and unlike TDIST it accepts negative values of `x`.

## Syntax

```excel
=T.DIST(x, deg_freedom, cumulative)
```

<!-- Image 1: Cumulative and Density Arguments. See Images/Statistical/T.DIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The t-value at which to evaluate the distribution. Negative values are allowed. |
| `deg_freedom` | Yes | The degrees of freedom, usually the sample size minus one for a single sample. Must be at least 1. |
| `cumulative` | Yes | `TRUE` returns the cumulative probability from the left tail up to `x`. `FALSE` returns the density at `x`. |

### Return Value

A number. With `TRUE`, the result is a probability between 0 and 1. With `FALSE`, the result is a density, which is not a probability. Excel returns `#NUM!` when `deg_freedom` is less than 1 and `#VALUE!` when an argument is not numeric.

## Examples

### Example 1: Cumulative Probability

```excel
=T.DIST(1.5, 10, TRUE)
```

**Result:** `0.917746`

About 92 percent of t-values with 10 degrees of freedom fall at or below 1.5.

### Example 2: Density at a Point

```excel
=T.DIST(1.5, 10, FALSE)
```

**Result:** `0.127445`

This is the height of the curve at 1.5, not a probability. Use it to plot the shape of the distribution.

### Example 3: Negative Values

```excel
=T.DIST(-1.98, 2, TRUE)
```

**Result:** `0.093126`

A negative `x` is valid, and the result is the area to the left of -1.98 with 2 degrees of freedom.

### Example 4: Large Sample Behavior

```excel
=T.DIST(1.96, 60, TRUE)
```

**Result:** `0.972678`

With 60 degrees of freedom the result is close to the normal curve value for 1.96.

<!-- Image 2: Left Tail Area Under the Curve. See Images/Statistical/T.DIST.md -->

## Story Problems

### Problem 1: Cumulative Chance of a Modest Gain

A researcher measured a product trial on 13 stores, which gives 12 degrees of freedom. The test statistic for the gain is 2.0. The team wants the chance of a statistic at or below that value.

| Store Count | Degrees of Freedom | Test Statistic |
| --- | --- | --- |
| 13 | 12 | 2.0 |

**Task:** Find the cumulative probability at 2.0 with 12 degrees of freedom.

**Solution:**

```excel
=T.DIST(2, 12, TRUE)
```

**Answer:** `0.965672`. About 96.6 percent of results from this trial sit at or below 2.0.

### Problem 2: Left Tail Risk of a Forecast Miss

A finance analyst compared eight monthly forecast errors and got a t-statistic of -1.2 with 8 degrees of freedom. She wants the chance of a miss at least that negative.

**Task:** Find the left-tail probability at -1.2 with 8 degrees of freedom.

**Solution:**

```excel
=T.DIST(-1.2, 8, TRUE)
```

**Answer:** `0.132234`, or about 13.2 percent.

## Use Cases

### Small Sample Probability

**Scenario:** A quality lab tests six batches and wants the probability of a t-statistic below a threshold they set in advance.

```excel
=T.DIST(B2, COUNT(Lab[Batches]) - 1, TRUE)
```

**Why It Works:** The degrees of freedom come from the sample count, so the formula updates when batches are added. Check that the threshold uses the same units as the statistic.

### Model Coefficient Checks

**Scenario:** An analyst wants to know how unusual a regression coefficient is when the sample has only 15 rows.

```excel
=T.DIST(B2, COUNT(Model[Rows]) - 2, TRUE)
```

**Why It Works:** A regression with one predictor loses two degrees of freedom, so subtracting 2 from the row count gives the correct value for the test. Use the two-tailed function when the question is about any difference.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `deg_freedom` is less than 1. | Check the sample size and subtract one for a single sample. |
| `#VALUE!` | An argument is text or blank. | Make sure each argument is a number or a cell that holds one. |
| Unexpected value above 1 | `cumulative` is `FALSE`, which returns a density. | Set `cumulative` to `TRUE` for a probability. |
| Wrong tail | The cumulative result is the left tail, but the question asks about the right tail. | Subtract the result from 1, or use T.DIST.RT. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2010 and later, including Microsoft 365 | Returns the left-tail area when `cumulative` is `TRUE`. Returns `#NUM!` for `deg_freedom` less than 1. |
| Google Sheets | Available | Same arguments and order. The documentation does not say how a fractional `deg_freedom` is handled. |

## Tips and Best Practices

- Choose `cumulative` deliberately, because a density result looks like a probability but is not one.
- Use T.DIST.2T for two-tailed tests and T.DIST.RT for the right tail, so the tail is named in the formula.
- Keep degrees of freedom as a formula, such as sample size minus one, so it updates with the data.
- Round displayed probabilities to four or six decimals to avoid false precision.

## Related Functions

| Function | Relationship |
| --- | --- |
| [T.DIST.2T](T.DIST.2T.md) | Two-tailed probability for a non-negative t-value. |
| [T.DIST.RT](T.DIST.RT.md) | Right-tail probability for a t-value. |
| [T.INV](T.INV.md) | Returns the t-value for a given left-tail probability, the reverse of this function. |
| [T.INV.2T](T.INV.2T.md) | Returns the critical t-value for a two-tailed probability. |
| [T.TEST](T.TEST.md) | Runs a complete t-test and returns its p-value. |
| [TDIST](TDIST.md) | Older function that returns one-tailed or two-tailed probabilities. |

## Official Documentation

- [Microsoft Support: T.DIST function](https://support.microsoft.com/en-us/excel/functions/t-dist-function)
- [Google Docs Editors Help: T.DIST](https://support.google.com/docs/answer/9369014)
