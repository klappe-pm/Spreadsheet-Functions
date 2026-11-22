---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Statistical Analysis
use-case:
  - Carrier Parcel Weights
  - Delivery Time Estimates
related:
  - AVERAGE
  - CONFIDENCE.NORM
  - CONFIDENCE.T
  - NORM.S.INV
  - STDEV.S
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/confidence-function
  - https://support.google.com/docs/answer/3093988
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Confidence Half Width Legacy
  - Mean Confidence Interval Legacy
tags:
  - averages
  - compatibility
  - confidence-interval
  - excel
  - sheets
---

# CONFIDENCE

## Description

**CONFIDENCE** returns the half-width of a confidence interval for a population mean, using a normal distribution. You add the result to the sample mean to get the upper limit, and subtract it to get the lower limit. The function assumes that the population standard deviation is known.

Microsoft Excel lists CONFIDENCE as a compatibility function. Its support page says it has been superseded by CONFIDENCE.NORM and CONFIDENCE.T and may not be available in future versions. Use CONFIDENCE.NORM when the population standard deviation is known, and CONFIDENCE.T when you only have the sample standard deviation. CONFIDENCE.NORM returns the same value that CONFIDENCE returns.

Google Sheets does not give CONFIDENCE its own page. The Sheets help page for CONFIDENCE.NORM states that you can use either CONFIDENCE or CONFIDENCE.NORM for the same calculation.

## Syntax

```excel
=CONFIDENCE(alpha, standard_dev, size)
```

<!-- Image 1: Confidence Interval Arguments. See Images/Statistical/CONFIDENCE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `alpha` | Yes | The significance level. The confidence level equals 100 times (1 minus alpha) percent, so 0.05 gives a 95 percent interval. Must be greater than 0 and less than 1. |
| `standard_dev` | Yes | The population standard deviation, assumed known. Must be greater than 0. |
| `size` | Yes | The sample size. A value that is not an integer is truncated. Must be at least 1. |

### Return Value

A positive number: the margin of error for the sample mean. The interval is the sample mean plus or minus this value. The function returns `#VALUE!` when an argument is not numeric and `#NUM!` when alpha is out of range, standard_dev is 0 or less, or size is less than 1.

## Examples

### Example 1: Margin of Error for a Sample

```excel
=CONFIDENCE(0.05, 4.2, 36)
```

**Result:** `1.371975`

With a 5 percent significance level, a known standard deviation of 4.2 and 36 observations, the sample mean can vary by about 1.37 in either direction.

### Example 2: Lower and Upper Limits From Cells

The sample mean is in `B2` (52.4), the standard deviation in `B3` (4.2), and the sample size in `B4` (36).

```excel
=B2-CONFIDENCE(0.05, B3, B4)
```

**Result:** `51.028025` (lower limit)

Replace the minus sign with a plus sign to get the upper limit, `53.771975`. The interval runs from 51.03 to 53.77 when rounded for display.

<!-- Image 2: Interval Limits From a Sample Mean. See Images/Statistical/CONFIDENCE.md -->

### Example 3: Same Result as CONFIDENCE.NORM

```excel
=CONFIDENCE(0.05, 4.2, 36) - CONFIDENCE.NORM(0.05, 4.2, 36)
```

**Result:** `0`

The two functions agree in the normal case, so this check confirms a workbook can move to CONFIDENCE.NORM without changing its intervals.

### Example 4: Fractional Sample Size

```excel
=CONFIDENCE(0.05, 4.2, 36.9)
```

**Result:** `1.371975`

The size 36.9 is truncated to 36. Enter whole numbers for sample sizes so the formula reads clearly.

## Story Problems

### Problem 1: Delivery Time Estimate

A courier logs delivery times for 50 stops. The sample mean is 28.6 minutes. Past data gives a population standard deviation of 3.1 minutes. The team wants a 90 percent interval, so alpha is 0.1.

| Measure | Value |
| --- | --- |
| Sample mean (minutes) | 28.6 |
| Standard deviation (minutes) | 3.1 |
| Stops | 50 |

**Task:** Find the lower and upper limits of the 90 percent interval for the mean delivery time.

**Solution:**

```excel
=28.6-CONFIDENCE(0.1, 3.1, 50)
```

**Answer:** The lower limit is `27.878886` and the upper limit is `29.321114` (27.88 to 29.32 minutes). The margin of error is 0.721114 minutes.

### Problem 2: Parcel Weight Check

A depot weighed 200 parcels and found a standard deviation of 0.8 kg from years of data. The mean weight is 6.35 kg. The depot wants a 99 percent interval.

**Task:** Find the margin of error at alpha 0.01.

**Solution:**

```excel
=CONFIDENCE(0.01, 0.8, 200)
```

**Answer:** `0.145711` kg. The interval runs from 6.204289 to 6.495711 kg.

## Use Cases

### Delivery Time Estimates

**Scenario:** A logistics coordinator publishes an expected delivery window for each route and wants the window to reflect sampling error.

```excel
=AVERAGE(Times) - CONFIDENCE(0.1, KnownSD, COUNT(Times))
```

**Why It Works:** `COUNT` supplies the sample size from the same range that `AVERAGE` uses, so the interval updates when new times are added.

### Carrier Parcel Weights

**Scenario:** A shipping team reports the average parcel weight for each carrier and shows a margin of error next to it.

```excel
=CONFIDENCE(Alpha, Sigma, Parcels)
```

**Why It Works:** Named cells keep the significance level, the known standard deviation and the parcel count visible to reviewers. Only the standard deviation must come from a reliable historical source.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | An argument is text or blank. | Check that every argument is a number. |
| `#NUM!` | alpha is 0 or less, or 1 or more. | Enter a value greater than 0 and less than 1. |
| `#NUM!` | standard_dev is 0 or less. | Use the population standard deviation, which must be positive. |
| `#NUM!` | size is less than 1. | Use a sample size of at least 1. |
| Too narrow an interval | The sample standard deviation was used with the normal method. | Use CONFIDENCE.T when the standard deviation comes from the same sample. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Compatibility function | Superseded by CONFIDENCE.NORM and CONFIDENCE.T. The support page warns that it may not be available in future versions. |
| Google Sheets | Available as CONFIDENCE | The Sheets help page for CONFIDENCE.NORM states that CONFIDENCE and CONFIDENCE.NORM perform the same function. Sheets names the arguments `alpha`, `standard_deviation` and `pop_size`. |

## Tips and Best Practices

- Use CONFIDENCE.NORM in new Excel work. Keep CONFIDENCE only where an existing formula depends on it.
- Use CONFIDENCE.T when the standard deviation was calculated from the same sample.
- Store alpha in a labeled cell so that every interval in a report uses the same confidence level.
- Report the interval as the mean plus or minus the margin so readers can see both the estimate and its precision.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGE](AVERAGE.md) | Supplies the sample mean at the center of the interval. |
| [CONFIDENCE.NORM](CONFIDENCE.NORM.md) | The modern name for the normal case of this calculation. |
| [CONFIDENCE.T](CONFIDENCE.T.md) | Uses the t distribution when the standard deviation comes from the sample. |
| [NORM.S.INV](NORM.S.INV.md) | Returns the z value behind the margin for a given probability. |
| [STDEV.S](STDEV.S.md) | Estimates the sample standard deviation that often feeds the margin. |

## Official Documentation

- [Microsoft Support: CONFIDENCE function](https://support.microsoft.com/en-us/excel/functions/confidence-function)
- [Google Docs Editors Help: CONFIDENCE.NORM](https://support.google.com/docs/answer/3093988)
