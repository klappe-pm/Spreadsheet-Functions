---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Delivery Time Targets
  - Exam Score Benchmarks
  - Manufacturing Tolerance Checks
related:
  - CONFIDENCE.NORM
  - NORM.INV
  - NORM.S.DIST
  - NORMDIST
  - STANDARDIZE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/norm-dist-function
  - https://support.google.com/docs/answer/3094021
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Normal Cumulative Probability
  - Normal Distribution
tags:
  - distribution
  - excel
  - normal-distribution
  - probability
  - sheets
---

# NORM.DIST

## Description

**NORM.DIST** returns the normal distribution for a value, given the mean and standard deviation of the data. The normal distribution describes many measurements that cluster around an average, such as exam scores, machine dimensions and delivery times. Use it to answer questions about how likely a value is, such as the share of scores at or below 85 when the average score is 70.

The cumulative argument sets the form of the result. TRUE returns the cumulative probability, which is the chance of a value at or below x. FALSE returns the height of the density curve at x. The density is not a probability, so use TRUE for almost every business question.

NORM.DIST replaces the older NORMDIST function. It uses the same arguments and gives the same results, and Microsoft describes it as the newer version with improved accuracy. For the standard normal curve (mean 0, standard deviation 1), NORM.S.DIST is a shorter option.

## Syntax

```excel
=NORM.DIST(x, mean, standard_dev, cumulative)
```

<!-- Image 1: Normal Curve With Mean and Standard Deviation. See Images/Statistical/NORM.DIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The value at which you want the distribution evaluated. |
| `mean` | Yes | The arithmetic mean of the distribution. |
| `standard_dev` | Yes | The standard deviation of the distribution. A value of zero or less returns `#NUM!`. |
| `cumulative` | Yes | TRUE returns the cumulative distribution (the chance of a value at or below x). FALSE returns the probability density at x. |

### Return Value

A decimal number. With TRUE it is a probability between 0 and 1. With FALSE it is a density value, which can be greater than 1 when the standard deviation is small. The function returns `#VALUE!` when an argument is not a number and `#NUM!` when `standard_dev` is zero or less.

## Examples

The examples use a mean of 70 in `B2` and a standard deviation of 8 in `B3`, which describe a set of exam scores.

### Example 1: Share at or Below 85

```excel
=NORM.DIST(85, 70, 8, TRUE)
```

**Result:** `0.969604`

About 97 percent of scores fall at or below 85. The score of 85 sits about 1.9 standard deviations above the mean.

### Example 2: Density at 85

```excel
=NORM.DIST(85, 70, 8, FALSE)
```

**Result:** `0.008598`

This is the height of the curve at 85, not a probability. Use it when you compare shapes of distributions, not when you need a chance.

### Example 3: Share Between Two Values

```excel
=NORM.DIST(85, 70, 8, TRUE) - NORM.DIST(60, 70, 8, TRUE)
```

**Result:** `0.863954`

Subtracting the cumulative chance at 60 from the cumulative chance at 85 gives the share of scores between the two marks.

### Example 4: Percentage for a Report

```excel
=ROUND(NORM.DIST(85, 70, 8, TRUE) * 100, 1)
```

**Result:** `97`

Multiplying by 100 turns the probability into a percentage, and ROUND keeps one decimal place. The result shows 97.0 when formatted with one decimal.

### Example 5: Share Above 85

```excel
=1 - NORM.DIST(85, 70, 8, TRUE)
```

**Result:** `0.030396`

The chance of scoring above 85 is the complement of the cumulative chance at 85.

<!-- Image 2: Area Under the Curve Below a Value. See Images/Statistical/NORM.DIST.md -->

## Story Problems

### Problem 1: Underfilled Bottles

A bottling line fills bottles with a mean volume of 500 ml and a standard deviation of 4 ml. Bottles at or below 495 ml fail the weight check. The quality lead wants the share of bottles that fail.

| Input | Value |
| --- | --- |
| Mean fill volume (ml) | 500 |
| Standard deviation (ml) | 4 |
| Failure limit (ml) | 495 |

**Task:** Enter the three inputs in `E2:E4`, then find the share of bottles at or below the limit.

**Solution:**

```excel
=NORM.DIST(E4, E2, E3, TRUE)
```

**Answer:** `0.10565`, or about 10.6 percent of bottles fail the check.

### Problem 2: Delivery Times Within a Window

A courier's delivery times have a mean of 42 minutes and a standard deviation of 6 minutes. The operations team promises delivery between 30 and 48 minutes.

| Input | Value |
| --- | --- |
| Mean delivery time (minutes) | 42 |
| Standard deviation (minutes) | 6 |
| Earliest promised time (minutes) | 30 |
| Latest promised time (minutes) | 48 |

**Task:** Enter the inputs in `E2:E5`, then find the share of deliveries that fall inside the promised window.

**Solution:**

```excel
=NORM.DIST(E5, E2, E3, TRUE) - NORM.DIST(E4, E2, E3, TRUE)
```

**Answer:** `0.81859`, or about 82 percent of deliveries fall inside the window. The formula subtracts the cumulative chance at the earliest time from the chance at the latest time.

## Use Cases

### Exam Score Benchmarks

**Scenario:** A school wants to report the share of students who score at or below each mark in a practice test with a mean of 70 and a standard deviation of 8.

```excel
=NORM.DIST(B2, $F$1, $F$2, TRUE)
```

**Why It Works:** `B2` holds the mark being reported, while `F1` and `F2` hold the mean and standard deviation. Copying the formula down a column produces a benchmark for each mark.

### Manufacturing Tolerance Checks

**Scenario:** A plant accepts shafts whose diameter falls between 24.8 mm and 25.2 mm. The diameters have a mean of 25.0 mm and a standard deviation of 0.1 mm.

```excel
=NORM.DIST(25.2, 25, 0.1, TRUE) - NORM.DIST(24.8, 25, 0.1, TRUE)
```

**Why It Works:** The difference between two cumulative values gives the share of shafts inside the tolerance band. The result shows how many shafts will pass without manual measurement.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `standard_dev` is zero or negative. | Recalculate the standard deviation from the data, or check the input cell. |
| `#VALUE!` | `mean`, `standard_dev` or `x` holds text. | Convert the value to a number. |
| Result is not a probability | `cumulative` is FALSE, which returns a density. | Set `cumulative` to TRUE for a probability. |
| Result looks shifted | The mean and standard deviation are swapped in the formula. | Check that the second argument is the mean and the third is the standard deviation. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Excel for the web | Four required arguments. Microsoft describes it as the replacement for NORMDIST. |
| Google Sheets | Available | The Google help entry for NORM.DIST points to the NORMDIST page, which documents the same four arguments. |

## Tips and Best Practices

- Use TRUE for probabilities and FALSE only when you need the density curve.
- Store the mean and standard deviation in labeled cells so every formula can share them.
- Check that the standard deviation is computed from the same data as the mean.
- For a standard normal value (mean 0, standard deviation 1), use NORM.S.DIST to shorten the formula.

## Related Functions

| Function | Relationship |
| --- | --- |
| [NORM.INV](NORM.INV.md) | Returns the x value for a given cumulative probability, the reverse of this function. |
| [NORM.S.DIST](NORM.S.DIST.md) | The same distribution with mean 0 and standard deviation 1. |
| [NORMDIST](NORMDIST.md) | The older form of this function, kept for compatibility. |
| [STANDARDIZE](STANDARDIZE.md) | Converts a value to a z-score that can be used with NORM.S.DIST. |
| [CONFIDENCE.NORM](CONFIDENCE.NORM.md) | Uses the normal distribution to size a confidence interval. |

## Official Documentation

- [Microsoft Support: NORM.DIST function](https://support.microsoft.com/en-us/excel/functions/norm-dist-function)
- [Google Docs Editors Help: NORMDIST](https://support.google.com/docs/answer/3094021)
