---
domain: Spreadsheet Functions
category: Statistical
subcategory: Averages
purpose:
  - Statistical Analysis
use-case:
  - Energy Use Estimates
  - Machine Tolerance Checks
  - Sample Mean Intervals
related:
  - AVERAGE
  - CONFIDENCE
  - CONFIDENCE.T
  - NORM.S.INV
  - STDEV.S
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/confidence-norm-function
  - https://support.google.com/docs/answer/3093988
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Confidence Half Width Normal
  - Normal Confidence Margin
tags:
  - averages
  - confidence-interval
  - excel
  - normal-distribution
  - sheets
---

# CONFIDENCE.NORM

## Description

**CONFIDENCE.NORM** returns the half-width of a confidence interval for a population mean, using a normal distribution. You add the result to the sample mean to get the upper limit and subtract it to get the lower limit. The function assumes that the population standard deviation is known, which is common in mature processes where years of data give a reliable value.

Use CONFIDENCE.NORM when the standard deviation comes from a long history or a known process specification. When the standard deviation is calculated from the same small sample, use CONFIDENCE.T instead. The t distribution gives a wider margin that reflects the extra uncertainty in the sample standard deviation.

CONFIDENCE.NORM replaces the older CONFIDENCE function, which returns the same value. Use CONFIDENCE.NORM in new workbooks.

## Syntax

```excel
=CONFIDENCE.NORM(alpha, standard_dev, size)
```

<!-- Image 1: Normal Margin Arguments. See Images/Statistical/CONFIDENCE.NORM.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `alpha` | Yes | The significance level, one minus the confidence level. A value of 0.05 gives a 95 percent interval, and 0.1 gives 90 percent. |
| `standard_dev` | Yes | The population standard deviation, assumed known. Google Sheets names this argument `standard_deviation`. |
| `size` | Yes | The sample size. A value that is not an integer is truncated. Google Sheets names this argument `pop_size`. |

### Return Value

A positive number: the margin of error. For a 95 percent interval with alpha 0.05, the standard normal value is about 1.96, so the margin is about 1.96 times the standard deviation divided by the square root of the sample size. The function returns `#VALUE!` when an argument is not numeric, and `#NUM!` when alpha is 0 or less or 1 or more, when standard_dev is 0 or less, or when size is less than 1.

## Examples

### Example 1: Margin for a Large Sample

```excel
=CONFIDENCE.NORM(0.1, 12, 64)
```

**Result:** `2.467280`

With a 90 percent interval, a known standard deviation of 12 and 64 observations, the sample mean can differ from the true mean by about 2.47 in either direction.

### Example 2: Margin From Cells

Alpha is in `A2` (0.01), the standard deviation in `A3` (2.5), and the sample size in `A4` (400).

```excel
=CONFIDENCE.NORM(A2, A3, A4)
```

**Result:** `0.321979`

Keeping the inputs in cells lets a reviewer test a different confidence level without changing the formula.

### Example 3: Interval Around a Sample Mean

The sample mean is in `B2` (80.2).

```excel
=B2 - CONFIDENCE.NORM(0.1, 12, 64)
```

**Result:** `77.73272` (lower limit)

The upper limit is `82.66728`, found by adding the same margin to the mean. Report both limits together so readers see the range.

<!-- Image 2: Interval Limits Around a Mean. See Images/Statistical/CONFIDENCE.NORM.md -->

### Example 4: Effect of a Smaller Alpha

```excel
=CONFIDENCE.NORM(0.01, 2.5, 400)
```

**Result:** `0.321979`

Lower alpha means a higher confidence level and a wider margin. Compare this with a 90 percent margin for the same data before you choose a level.

## Story Problems

### Problem 1: Bolt Length Tolerance

A machine shop measures 100 bolts from a line. The sample mean length is 25.012 mm. Years of inspection data give a standard deviation of 0.05 mm. The quality team wants a 95 percent interval.

| Measure | Value |
| --- | --- |
| Sample mean (mm) | 25.012 |
| Standard deviation (mm) | 0.05 |
| Sample size | 100 |

**Task:** Compute the margin of error and the lower and upper limits of the interval.

**Solution:**

```excel
=CONFIDENCE.NORM(0.05, 0.05, 100)
```

**Answer:** The margin is `0.0098` mm. The lower limit is 25.0022 mm and the upper limit is 25.0218 mm.

### Problem 2: Monthly Energy Use

A building manager records energy use in 36 months. The mean is 412 kWh per month, and the known standard deviation from the utility's data is 18 kWh. The manager wants a 90 percent interval.

**Task:** Find the margin of error at alpha 0.1.

**Solution:**

```excel
=CONFIDENCE.NORM(0.1, 18, 36)
```

**Answer:** `4.934561` kWh. The interval runs from 407.07 to 416.93 kWh per month.

## Use Cases

### Energy Use Estimates

**Scenario:** A facilities team reports a range for average monthly energy use so budget owners can see how stable the number is.

```excel
=AVERAGE(Usage) - CONFIDENCE.NORM(Alpha, KnownSD, COUNT(Usage))
```

**Why It Works:** `AVERAGE` and `COUNT` read the same range, so the interval stays consistent when months are added. The known standard deviation comes from the utility's historical data, which is the assumption this function needs.

### Machine Tolerance Checks

**Scenario:** A plant checks whether the average part length from a sample stays inside a tolerance band that uses a known process spread.

```excel
=IF(ABS(AVERAGE(Lengths) - Target) > CONFIDENCE.NORM(Alpha, Sigma, COUNT(Lengths)), "Out of Band", "In Band")
```

**Why It Works:** The margin defines how far the sample mean may drift from the target before the result counts as a real shift rather than sampling noise.

### Sample Mean Intervals

**Scenario:** An analyst publishes an interval next to each average in a dashboard, with one confidence level for the whole report.

**Why It Works:** Storing alpha in a single cell keeps every interval on the same basis, and the same formula works for each row.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | An argument is text or blank. | Check that every argument is a number. |
| `#NUM!` | alpha is 0 or less, or 1 or more. | Enter a value between 0 and 1, such as 0.05. |
| `#NUM!` | standard_dev is 0 or less. | Use a positive population standard deviation. |
| `#NUM!` | size is less than 1. | Use a sample size of at least 1. |
| Interval too narrow | The sample standard deviation was used here instead of the known population value. | Use CONFIDENCE.T when the standard deviation comes from the same sample. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions | Argument names are `alpha`, `standard_dev` and `size`. |
| Google Sheets | Available | Argument names are `alpha`, `standard_deviation` and `pop_size`. The help page gives an example with alpha 0.1 for a 90 percent confidence level. |

## Tips and Best Practices

- Use CONFIDENCE.T when the standard deviation comes from the sample you are analyzing.
- Report the confidence level with every interval so readers know what alpha represents.
- Keep the margin and the mean in separate cells so each can be checked on its own.
- Round the displayed limits, but keep the full values in calculations that compare two intervals.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGE](AVERAGE.md) | Supplies the sample mean at the center of the interval. |
| [CONFIDENCE](CONFIDENCE.md) | The older name for the same normal calculation. |
| [CONFIDENCE.T](CONFIDENCE.T.md) | The version to use when the standard deviation comes from the sample. |
| [NORM.S.INV](NORM.S.INV.md) | Returns the z value for a probability, the number behind the margin. |
| [STDEV.S](STDEV.S.md) | Estimates a sample standard deviation that can be compared with a known value. |

## Official Documentation

- [Microsoft Support: CONFIDENCE.NORM function](https://support.microsoft.com/en-us/excel/functions/confidence-norm-function)
- [Google Docs Editors Help: CONFIDENCE.NORM](https://support.google.com/docs/answer/3093988)
