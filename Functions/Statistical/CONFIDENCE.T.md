---
domain: Spreadsheet Functions
category: Statistical
subcategory: Averages
purpose:
  - Statistical Analysis
use-case:
  - Bulb Lifetime Testing
  - Cookie Weight Checks
  - Sample Mean Intervals
related:
  - AVERAGE
  - CONFIDENCE
  - CONFIDENCE.NORM
  - STDEV.S
  - T.INV.2T
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/confidence-t-function
  - https://support.google.com/docs/answer/9365672
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Confidence Half Width Student
  - Small Sample Confidence Margin
tags:
  - averages
  - confidence-interval
  - excel
  - sheets
  - t-distribution
---

# CONFIDENCE.T

## Description

**CONFIDENCE.T** returns the half-width of a confidence interval for a population mean, using Student's t distribution. You add the result to the sample mean to get the upper limit and subtract it to get the lower limit. Use this function when the standard deviation comes from the sample itself, which is the usual situation with small samples.

The t distribution has heavier tails than the normal distribution, so the margin is wider for small samples and the gap narrows as the sample grows. For large samples the result is close to CONFIDENCE.NORM. For a sample of 36 the two margins differ by less than 0.05 in the worked example below, but for a sample of 10 the difference is larger.

Use CONFIDENCE.NORM when the population standard deviation is known from a long history. The older CONFIDENCE function gives the normal result and is covered on its own page.

## Syntax

```excel
=CONFIDENCE.T(alpha, standard_dev, size)
```

<!-- Image 1: T Distribution Margin Arguments. See Images/Statistical/CONFIDENCE.T.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `alpha` | Yes | The significance level, one minus the confidence level. A value of 0.05 gives a 95 percent interval. Must be greater than 0 and less than 1. |
| `standard_dev` | Yes | The standard deviation, usually the sample standard deviation. Must be greater than 0. Google Sheets names this argument `standard_deviation`. |
| `size` | Yes | The sample size. A value that is not an integer is truncated. Must be at least 2, because a size of 1 returns `#DIV/0!`. Google Sheets names this argument `size`. |

### Return Value

A positive number: the margin of error for the sample mean. The interval is the sample mean plus or minus this value. The function returns `#VALUE!` when an argument is not numeric, `#NUM!` when alpha is 0 or less or 1 or more, when standard_dev is 0 or less, or when size is less than 1, and `#DIV/0!` when size equals 1.

## Examples

### Example 1: Margin for a Sample of 36

```excel
=CONFIDENCE.T(0.05, 4.2, 36)
```

**Result:** `1.421076`

The sample standard deviation is 4.2 and the sample has 36 observations. The margin is slightly wider than the normal result of 1.371975 from the same inputs.

### Example 2: Interval Limits From Cells

The sample mean is in `B2` (52.4), the standard deviation in `B3` (4.2), and the sample size in `B4` (36).

```excel
=B2 - CONFIDENCE.T(0.05, B3, B4)
```

**Result:** `50.978924` (lower limit)

The upper limit is `53.821076`, found by adding the same margin to the mean. The 95 percent interval runs from 50.98 to 53.82 when rounded.

<!-- Image 2: Small Sample Margin. See Images/Statistical/CONFIDENCE.T.md -->

### Example 3: Difference From the Normal Margin

```excel
=CONFIDENCE.T(0.05, 4.2, 36) - CONFIDENCE.NORM(0.05, 4.2, 36)
```

**Result:** `0.049101`

The t margin exceeds the normal margin by about 0.05 for this sample. The gap is the price of estimating the standard deviation from the sample.

### Example 4: Small Sample Margin

```excel
=CONFIDENCE.T(0.05, 4.2, 10)
```

**Result:** `3.004499`

With 10 observations the margin is 3.004499, compared with 2.603139 from CONFIDENCE.NORM for the same inputs. The wider result shows why small samples need the t distribution.

## Story Problems

### Problem 1: Bulb Lifetime Test

A lab tests 18 bulbs and records a sample standard deviation of 42 hours. The mean lifetime is 1,250 hours. The lab wants a 95 percent interval.

| Measure | Value |
| --- | --- |
| Sample mean (hours) | 1,250 |
| Sample standard deviation (hours) | 42 |
| Bulbs tested | 18 |

**Task:** Find the margin of error for the 95 percent interval.

**Solution:**

```excel
=CONFIDENCE.T(0.05, 42, 18)
```

**Answer:** `20.886109` hours. The interval runs from 1229.11 to 1270.89 hours.

### Problem 2: Cookie Weight Check

A bakery weighs 9 cookies from a batch. The mean weight is 14.5 grams, and the sample standard deviation is 1.2 grams. The team wants a 90 percent interval, so alpha is 0.1.

**Task:** Find the lower and upper limits of the interval.

**Solution:**

```excel
=14.5 - CONFIDENCE.T(0.1, 1.2, 9)
```

**Answer:** The lower limit is `13.756181` grams. The margin is `0.743819`, so the upper limit is 15.243819 grams.

## Use Cases

### Bulb Lifetime Testing

**Scenario:** A product team tests a small batch of components and reports an interval for mean lifetime, using only the data from the test.

```excel
=AVERAGE(Lifetimes) - CONFIDENCE.T(0.05, STDEV.S(Lifetimes), COUNT(Lifetimes))
```

**Why It Works:** The standard deviation and the sample size both come from the same test data, which is what the t distribution assumes.

### Sample Mean Intervals

**Scenario:** An analyst publishes a mean and interval for each product line where samples range from 8 to 40 observations.

**Why It Works:** One formula handles every sample size, and the interval widens automatically when a line has fewer observations.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | size equals 1. | Use a sample of at least 2 observations. |
| `#VALUE!` | An argument is text or blank. | Check that every argument is a number. |
| `#NUM!` | alpha is 0 or less, or 1 or more. | Enter a value between 0 and 1, such as 0.05. |
| `#NUM!` | standard_dev is 0 or less. | Check that the standard deviation is positive. |
| Wrong standard deviation | A population value was entered from a different source. | Use STDEV.S on the same sample, or switch to CONFIDENCE.NORM for a known population value. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions | The support page states that the function returns `#DIV/0!` when size is 1. |
| Google Sheets | Available | The help page describes the margin as the half-width of the interval for a t distribution. It does not state rules for alpha or for size truncation, so test edge cases before relying on them. |

## Tips and Best Practices

- Use CONFIDENCE.T for samples where the standard deviation is estimated from the data.
- Compare the result with CONFIDENCE.NORM when the sample is large, to see how close the two margins are.
- Keep the sample size in a cell that counts the same range as the mean, so the interval stays in step with the data.
- Report the sample size with the interval so readers can judge how much to trust a narrow margin.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGE](AVERAGE.md) | Supplies the sample mean at the center of the interval. |
| [CONFIDENCE](CONFIDENCE.md) | The older normal-distribution version of the calculation. |
| [CONFIDENCE.NORM](CONFIDENCE.NORM.md) | Use instead when the population standard deviation is known. |
| [STDEV.S](STDEV.S.md) | Calculates the sample standard deviation used as the input. |
| [T.INV.2T](T.INV.2T.md) | Returns the two-tailed t value behind the margin. |

## Official Documentation

- [Microsoft Support: CONFIDENCE.T function](https://support.microsoft.com/en-us/excel/functions/confidence-t-function)
- [Google Docs Editors Help: CONFIDENCE.T](https://support.google.com/docs/answer/9365672)
