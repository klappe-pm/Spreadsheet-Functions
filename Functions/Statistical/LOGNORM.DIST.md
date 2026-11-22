---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
use-case:
  - Claim Size Probability
  - Income Distribution Analysis
  - Service Time Probability
related:
  - LOGINV
  - LOGNORM.INV
  - LOGNORMDIST
  - NORM.DIST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/lognorm-dist-function
  - https://support.google.com/docs/answer/3094011
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Lognormal Cumulative Distribution
  - Lognormal Density
tags:
  - distribution
  - excel
  - lognormal
  - probability
  - sheets
---

# LOGNORM.DIST

## Description

**LOGNORM.DIST** returns the lognormal distribution of x, where the natural logarithm of x follows a normal distribution with a given mean and standard deviation. It suits positive, right-skewed data such as claim sizes, incomes, and service times, where a few large values pull the average upward.

Set `cumulative` to TRUE to get the probability that a value is at or below x. Set it to FALSE to get the probability density, the height of the curve at x. Density values are useful for charts and comparisons, but they are not probabilities, so use the TRUE form whenever you need a chance.

LOGNORM.DIST is the current version of LOGNORMDIST, which returns only the cumulative probability. Use LOGNORM.DIST in new work. To reverse the calculation and find the value for a given probability, use LOGNORM.INV.

## Syntax

```excel
=LOGNORM.DIST(x, mean, standard_dev, cumulative)
```

<!-- Image 1: Lognormal Curve With Cumulative Area. See Images/Statistical/LOGNORM.DIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The value at which to evaluate the distribution. It must be greater than 0. |
| `mean` | Yes | The mean of the natural logarithm of x, not the mean of x. |
| `standard_dev` | Yes | The standard deviation of the natural logarithm of x. It must be greater than 0. |
| `cumulative` | Yes | TRUE returns the cumulative probability that a value is at or below x. FALSE returns the probability density. |

### Return Value

A number. With `cumulative` TRUE it is a probability between 0 and 1. With FALSE it is the density, which can be greater than 1. The function returns `#VALUE!` when an argument is not a number, and `#NUM!` when x is 0 or less, or when `standard_dev` is 0 or less.

## Examples

### Example 1: Cumulative Probability

```excel
=LOGNORM.DIST(10, 2, 0.5, TRUE)
```

**Result:** `0.7275`

About 73 percent of values from this distribution are at or below 10.

### Example 2: Probability Density at a Point

```excel
=LOGNORM.DIST(10, 2, 0.5, FALSE)
```

**Result:** `0.0664`

This is the height of the density curve at x equal to 10. Use it to compare shapes, not to read a probability.

### Example 3: Catching a Value That Is Not Positive

```excel
=IFERROR(LOGNORM.DIST(0, 2, 0.5, TRUE), "x must be above 0")
```

**Result:** `x must be above 0`

Because x must be greater than 0, a value of 0 returns `#NUM!`. IFERROR shows a message that explains the rule.

## Story Problems

### Problem 1: Insurance Claim Sizes

An insurer models claim amounts as lognormal. The parameters are in the table below.

| Parameter | Value |
| --- | --- |
| Mean of ln(claim) | 7.0 |
| Standard deviation of ln(claim) | 0.8 |

**Task:** Find the probability that a new claim is 2000 dollars or less. Put 2000 in `B4`, and the parameters in `B2:B3`.

**Solution:**

```excel
=LOGNORM.DIST(B4, B2, B3, TRUE)
```

**Answer:** `0.7737`. About 77 percent of claims fall at or below 2000 dollars.

<!-- Image 2: Claim Size Worksheet. See Images/Statistical/LOGNORM.DIST.md -->

### Problem 2: Large Claims Reserve

Using the same parameters as Problem 1, the reserving team wants the share of claims above 5000 dollars, which need extra review.

| Parameter | Value |
| --- | --- |
| Mean of ln(claim) | 7.0 |
| Standard deviation of ln(claim) | 0.8 |
| Threshold | 5000 |

**Task:** Find the probability that a claim exceeds 5000 dollars.

**Solution:**

```excel
=1 - LOGNORM.DIST(B4, B2, B3, TRUE)
```

**Answer:** `0.0289`. About 2.9 percent of claims are large enough to need extra review.

## Use Cases

### Claim Size Probability

**Scenario:** A claims team checks each new claim against the fitted distribution to estimate how unusual it is.

```excel
=LOGNORM.DIST(Claims[Amount], Params!B2, Params!B3, TRUE)
```

**Why It Works:** The formula returns a percentile for each claim, so the team can flag values near the top of the distribution.

### Income Distribution Analysis

**Scenario:** A policy analyst builds a density curve of household incomes to compare two regions.

```excel
=LOGNORM.DIST(Chart!A2:A60, Region!B2, Region!B3, FALSE)
```

**Why It Works:** An array of x values returns the density for each point, which makes a smooth curve for a chart.

### Service Time Probability

**Scenario:** A call center wants the chance that a call takes longer than a given number of minutes.

```excel
=1 - LOGNORM.DIST(Calls[Minutes], Stats!B2, Stats!B3, TRUE)
```

**Why It Works:** Subtracting the cumulative probability from 1 gives the chance of exceeding each value, which feeds staffing models.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | x is 0 or less. | Only pass positive values. Filter out zeros and blanks first. |
| `#NUM!` | `standard_dev` is 0 or less. | Enter a positive standard deviation of ln(x). |
| `#VALUE!` | An argument is text or blank. | Convert the input to a number. |
| Wrong probability | The mean of x was used instead of the mean of ln(x). | Compute the mean and standard deviation of the logarithms. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available, including Excel for the web | Supports both cumulative and density results through the fourth argument. |
| Google Sheets | Available | The function list shows three arguments, `x`, `mean` and `standard_deviation`, and refers to LOGNORMDIST for details. Check the cumulative option in the Sheets help before relying on it. |

## Tips and Best Practices

- Compute the logarithms in a helper column, then use AVERAGE and STDEV.S on that column to get the mean and standard deviation.
- Label the cumulative and density results clearly, so a reader does not read a density as a probability.
- Use LOGNORM.DIST rather than LOGNORMDIST for new formulas.
- Put the threshold in its own cell so the probability updates when the business rule changes.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LOGNORM.INV](LOGNORM.INV.md) | Returns the value for a probability, the reverse of this function. |
| [LOGNORMDIST](LOGNORMDIST.md) | The legacy cumulative lognormal function that this function replaces. |
| [LOGINV](LOGINV.md) | The legacy inverse lognormal function. |
| [NORM.DIST](NORM.DIST.md) | The normal distribution version, for data that is not logged. |

## Official Documentation

- [Microsoft Support: LOGNORM.DIST function](https://support.microsoft.com/en-us/excel/functions/lognorm-dist-function)
- [Google Docs Editors Help: LOGNORM.DIST](https://support.google.com/docs/answer/3094011)
