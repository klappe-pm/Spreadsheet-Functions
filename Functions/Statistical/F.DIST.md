---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Campaign Variability
  - Process Variance Review
  - Variance Comparison
related:
  - CHISQ.DIST
  - F.DIST.RT
  - F.INV
  - F.TEST
  - FDIST
  - NORM.DIST
  - VAR.S
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/f-dist-function
  - https://support.google.com/docs/answer/6055706
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - distribution
  - excel
  - f-distribution
  - probability
  - sheets
---

# F.DIST

## Description

**F.DIST** returns the left-tailed F probability distribution for two samples. You give it a value `x` and the degrees of freedom for each sample, and it returns how likely a result is to fall at or below `x`. The F distribution describes the ratio of two sample variances, so F.DIST answers questions such as "how likely is a variance ratio of 2 or less if both samples come from the same process?"

Set `cumulative` to TRUE to get that cumulative probability. Set it to FALSE to get the density, which is the height of the F curve at `x`. The density is useful for charting the curve, but it is not a probability. Use F.DIST.RT when you need the right tail, which is the usual form for a p-value.

The degrees of freedom are each sample size minus 1. A sample of 9 values has 8 degrees of freedom. Non-integer degrees of freedom are truncated to whole numbers.

Use F.DIST when you need the probability to the left of a point. For most significance tests, F.DIST.RT is the more useful function, because it returns 1 minus the left-tail value directly.

## Syntax

```excel
=F.DIST(x, deg_freedom1, deg_freedom2, cumulative)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/F.DIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The value at which to evaluate the distribution. It cannot be negative in Excel. |
| `deg_freedom1` | Yes | The numerator degrees of freedom, which is the numerator sample size minus 1. |
| `deg_freedom2` | Yes | The denominator degrees of freedom, which is the denominator sample size minus 1. |
| `cumulative` | Yes | TRUE returns the cumulative probability up to `x`. FALSE returns the density at `x`. |

### Return Value

A number. With `cumulative` set to TRUE, the result is a probability from 0 to 1. With FALSE, the result is the non-negative density at `x`. Excel returns `#VALUE!` when an argument is not numeric and `#NUM!` when `x` is negative or a degrees-of-freedom value is less than 1.

## Examples

### Example 1: Cumulative Probability at a Point

```excel
=F.DIST(4.5, 5, 10, TRUE)
```

**Result:** `0.9792` (rounded to four decimal places)

About 97.9 percent of variance ratios from these samples fall at or below 4.5. The numerator has 5 degrees of freedom and the denominator has 10.

### Example 2: Density at a Point

```excel
=F.DIST(4.5, 5, 10, FALSE)
```

**Result:** `0.0143` (rounded to four decimal places)

Setting `cumulative` to FALSE returns the height of the curve at 4.5. This value is not a probability, so do not compare it with 0.05.

<!-- Image 2: Cumulative Probability and Density Curve. See Images/Statistical/F.DIST.md -->

### Example 3: Cumulative Probability With Larger Samples

```excel
=F.DIST(2.2, 8, 12, TRUE)
```

**Result:** `0.8945` (rounded to four decimal places)

Here the numerator sample has 9 values and the denominator sample has 13. The result is the probability that the variance ratio is 2.2 or less.

## Story Problems

### Problem 1: Two Filling Lines

A beverage plant measures the variance of fill volume on two lines. Line X has been sampled 9 times and Line Y 11 times.

| Line | Sample Size | Sample Variance |
| --- | --- | --- |
| Line X | 9 | 2.4 |
| Line Y | 11 | 1.2 |

**Task:** Find the probability that the variance ratio of Line X to Line Y is 2.0 or less, with the sample sizes in `B2:B3` and the variances in `C2:C3`.

**Solution:**

```excel
=F.DIST(C2/C3, B2-1, B3-1, TRUE)
```

**Answer:** `0.8492`. The ratio is 2.4 divided by 1.2, which is 2.0, and the degrees of freedom are 8 and 10.

### Problem 2: Campaign Click Variability

A marketing team tracks daily clicks for two campaigns. Campaign A ran for 8 days and Campaign B ran for 16 days. The variance of Campaign A divided by the variance of Campaign B is 1.8.

| Campaign | Days Sampled |
| --- | --- |
| Campaign A | 8 |
| Campaign B | 16 |

**Task:** Find the probability that the variance ratio is 1.8 or less, using the day counts in `B2:B3`.

**Solution:**

```excel
=F.DIST(1.8, B2-1, B3-1, TRUE)
```

**Answer:** `0.8394`. The degrees of freedom are 7 for Campaign A and 15 for Campaign B.

## Use Cases

### Comparing Variability Across Two Lines

**Scenario:** A production manager wants to know whether a new filling line is more consistent than the old one, using the variances of recent samples.

```excel
=F.DIST(C2/C3, B2-1, B3-1, TRUE)
```

**Why It Works:** The variance ratio is the test statistic, and the sample sizes minus 1 are the degrees of freedom. Check that the numerator is the variance you expect to be larger, because a reversed ratio gives a different answer.

### Campaign Variability Check

**Scenario:** A marketing analyst compares click variability between two campaigns before deciding which one to scale.

```excel
=F.DIST(VarA/VarB, DaysA-1, DaysB-1, TRUE)
```

**Why It Works:** Named cells such as `VarA` and `DaysA` keep the formula readable. Use the sample variance from VAR.S for each campaign so the ratio uses the same measure.

### Density Curve for a Chart

**Scenario:** An analyst plots the shape of the F distribution for 5 and 10 degrees of freedom to explain a test to a non-technical audience.

```excel
=F.DIST(A2:A60, 5, 10, FALSE)
```

**Why It Works:** Each x value in column A returns its density, which gives the points for a line chart. The results are heights, not probabilities, so label the vertical axis as density.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `x` is negative, or a degrees-of-freedom value is less than 1. | Check that `x` is zero or positive, and that each sample has at least two values. |
| `#VALUE!` | An argument is text or a blank cell that was read as text. | Convert the value with VALUE or fix the reference. |
| Wrong probability | The sample size was entered in place of sample size minus 1. | Subtract 1 from each sample size in the formula. |
| Density instead of probability | `cumulative` was set to FALSE. | Use TRUE for a cumulative probability. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current Excel, including Excel for the web | `cumulative` is required. Returns `#NUM!` for negative `x` or degrees of freedom below 1. |
| Google Sheets | Available | Requires `x` to be positive and each degrees-of-freedom value to be greater than 1 and no more than 10^10. Omitting `cumulative` defaults to FALSE. |

## Tips and Best Practices

- Put the larger sample variance in the numerator when you want a one-sided comparison, and state that choice in the sheet so readers know the direction.
- Use `sample size minus 1` for each degrees-of-freedom argument, not the raw count.
- Use F.DIST.RT for p-values and F.DIST for the left tail, so the two results add to 1.
- Keep the variances in cells with VAR.S so the ratio updates when the data changes.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHISQ.DIST](CHISQ.DIST.md) | Chi square distribution, used for tests on a single variance. |
| [F.DIST.RT](F.DIST.RT.md) | Returns the right-tail probability, usually used as a p-value. |
| [F.INV](F.INV.md) | Returns the x value for a given left-tail probability, the inverse of F.DIST. |
| [F.TEST](F.TEST.md) | Tests whether two samples have equal variances and returns a two-tailed probability. |
| [FDIST](FDIST.md) | Legacy right-tail version kept for older workbooks. |
| [NORM.DIST](NORM.DIST.md) | Normal distribution, a common comparison when a sample is large. |
| [VAR.S](VAR.S.md) | Calculates the sample variance that forms the variance ratio. |

## Official Documentation

- [Microsoft Support: F.DIST function](https://support.microsoft.com/en-us/excel/functions/f-dist-function)
- [Google Docs Editors Help: F.DIST](https://support.google.com/docs/answer/6055706)
