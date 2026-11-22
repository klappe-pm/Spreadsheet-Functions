---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Safety Stock Levels
  - Score Cutoff Planning
  - Service Level Targets
related:
  - CONFIDENCE.NORM
  - NORM.DIST
  - NORM.S.INV
  - NORMINV
  - STANDARDIZE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/norm-inv-function
  - https://support.google.com/docs/answer/3094022
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Inverse Normal Distribution
  - Normal Percentile Value
tags:
  - distribution
  - excel
  - inverse
  - probability
  - sheets
---

# NORM.INV

## Description

**NORM.INV** returns the value that has a given cumulative probability in a normal distribution with a stated mean and standard deviation. It works in reverse from NORM.DIST: you supply the chance and the function returns the value at which that chance is reached. Use it to find cutoffs, targets and percentiles, such as the stock level that covers 95 percent of weekly demand.

The probability must be greater than 0 and less than 1. A value of exactly 0 or 1 returns `#NUM!`, because no finite value has a probability of 0 or of 1 in a normal distribution.

NORM.INV replaces the older NORMINV function and gives the same results. When the mean is 0 and the standard deviation is 1, the function is the standard normal inverse, and NORM.S.INV is the shorter form for that case.

## Syntax

```excel
=NORM.INV(probability, mean, standard_dev)
```

<!-- Image 1: Inverse Lookup on the Normal Curve. See Images/Statistical/NORM.INV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | The cumulative probability, greater than 0 and less than 1. A value of 0 or 1, or any value outside that range, returns `#NUM!`. |
| `mean` | Yes | The arithmetic mean of the distribution. |
| `standard_dev` | Yes | The standard deviation of the distribution. A value of zero or less returns `#NUM!`. |

### Return Value

A number on the scale of the data: the value x for which NORM.DIST with TRUE returns the given probability. The function returns `#VALUE!` when an argument is not a number and `#NUM!` when `probability` is outside the allowed range or `standard_dev` is zero or less.

## Examples

The examples use a mean of 100 in `B2` and a standard deviation of 12 in `B3`.

### Example 1: Value Covering Three Quarters

```excel
=NORM.INV(0.75, 100, 12)
```

**Result:** `108.094`

Three quarters of values fall at or below 108.094 in this distribution.

### Example 2: Median

```excel
=NORM.INV(0.5, 100, 12)
```

**Result:** `100`

For a normal distribution the median equals the mean, so a probability of 0.5 returns the mean.

### Example 3: Lower Cutoff

```excel
=NORM.INV(0.1, 100, 12)
```

**Result:** `84.621`

Only 10 percent of values fall below this cutoff. The function returns a value below the mean because the probability is below 0.5.

### Example 4: Rounded Target

```excel
=ROUND(NORM.INV(0.9, 100, 12), 0)
```

**Result:** `115`

The 90th percentile is 115.38, and ROUND turns it into a whole number for a target sheet.

### Example 5: Width of a Central 95 Percent Interval

```excel
=NORM.INV(0.975, 100, 12) - NORM.INV(0.025, 100, 12)
```

**Result:** `47.039`

The central 95 percent of values lies within a band about 47 units wide. Subtracting the two cutoffs gives the width of that band.

<!-- Image 2: Probability Scale Converted to a Value. See Images/Statistical/NORM.INV.md -->

## Story Problems

### Problem 1: Safety Stock for a Target Service Level

A warehouse sells an average of 120 units per week, with a standard deviation of 15 units. The operations manager wants enough stock to cover 95 percent of weeks without running out.

| Input | Value |
| --- | --- |
| Mean weekly demand (units) | 120 |
| Standard deviation (units) | 15 |
| Target service level | 0.95 |

**Task:** Enter the inputs in `E2:E4`, then find the stock level that covers the target share of weeks.

**Solution:**

```excel
=NORM.INV(E4, E2, E3)
```

**Answer:** `144.673`, so the warehouse should hold at least 145 units to cover 95 percent of weeks.

### Problem 2: Top Ten Percent Score Cutoff

A training exam has a mean score of 62 and a standard deviation of 9. The program wants to know the score that 90 percent of candidates score at or below.

| Input | Value |
| --- | --- |
| Mean score | 62 |
| Standard deviation | 9 |
| Cumulative share | 0.9 |

**Task:** Enter the inputs in `E2:E4`, then find the score at the 90th percentile.

**Solution:**

```excel
=NORM.INV(E4, E2, E3)
```

**Answer:** `73.534`. A candidate who scores 74 or higher is in the top 10 percent.

## Use Cases

### Safety Stock Levels

**Scenario:** A distributor chooses a service level for each product and needs the stock level that supports it.

```excel
=NORM.INV(C2, B2, D2)
```

**Why It Works:** `C2` holds the service level, `B2` holds average demand and `D2` holds the standard deviation. Copying the formula down the product list sets a stock target for each row.

### Score Cutoff Planning

**Scenario:** A certification body wants to pass the top 20 percent of candidates in a practice test with a mean of 500 and a standard deviation of 100.

```excel
=ROUND(NORM.INV(0.8, $F$1, $F$2), 0)
```

**Why It Works:** The probability 0.8 marks the top 20 percent boundary. Rounding gives a whole-number cutoff that matches the score scale.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `probability` is 0, 1 or outside the range, or `standard_dev` is zero or negative. | Enter a probability strictly between 0 and 1, and check the standard deviation. |
| `#VALUE!` | An argument holds text or another nonnumeric value. | Re-enter the value as a number. |
| Result far from the expected value | The mean and standard deviation are swapped in the formula. | Check that the second argument is the mean and the third is the standard deviation. |
| Percentage input returns `#NUM!` | A value such as 95 was entered instead of 0.95. | Enter probabilities as decimals or format the cell as a percentage. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Excel for the web | Microsoft documents `#NUM!` for invalid inputs. The result is found by searching NORM.DIST, so its precision depends on NORM.DIST. |
| Google Sheets | Available | The Google help entry for NORM.INV points to the NORMINV page, which documents the same three arguments. |

## Tips and Best Practices

- Enter the probability as a cumulative share (the chance of being at or below the value) so the result matches NORM.DIST.
- Round results only at the presentation step, so later calculations use the full value.
- Use NORM.S.INV when the mean is 0 and the standard deviation is 1.
- Check the probability limits before you copy a formula down a long list.

## Related Functions

| Function | Relationship |
| --- | --- |
| [NORM.DIST](NORM.DIST.md) | The forward calculation: value in, probability out. |
| [NORM.S.INV](NORM.S.INV.md) | The standard normal version with mean 0 and standard deviation 1. |
| [NORMINV](NORMINV.md) | The older form of this function, kept for compatibility. |
| [STANDARDIZE](STANDARDIZE.md) | Converts a value to a z-score before a standard normal lookup. |
| [CONFIDENCE.NORM](CONFIDENCE.NORM.md) | Uses the normal distribution to size a margin of error. |

## Official Documentation

- [Microsoft Support: NORM.INV function](https://support.microsoft.com/en-us/excel/functions/norm-inv-function)
- [Google Docs Editors Help: NORMINV](https://support.google.com/docs/answer/3094022)
