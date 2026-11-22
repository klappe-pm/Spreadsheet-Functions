---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Credit Score Cutoffs
  - Process Control Limits
  - Top Percentile Thresholds
related:
  - CONFIDENCE.NORM
  - NORM.INV
  - NORM.S.DIST
  - NORMSINV
  - Z.TEST
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/norm-s-inv-function
  - https://support.google.com/docs/answer/3094091
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Inverse Standard Normal
  - Z-Score From Probability
tags:
  - distribution
  - excel
  - inverse
  - normal-distribution
  - probability
  - sheets
  - z-score
---

# NORM.S.INV

## Description

**NORM.S.INV** returns the z-score for a given cumulative probability in the standard normal distribution, the curve with a mean of 0 and a standard deviation of 1. It is the reverse of NORM.S.DIST. You supply a probability, such as 0.975, and the function returns the number of standard deviations that marks that share of the distribution.

Use it to set thresholds in standard deviation units, such as the cutoff for the top 1 percent of results or the limit for a two-sided 95 percent confidence band. The result is a z-score, so convert it back to the data scale with `mean + z * standard deviation` when you need the raw value.

The probability must be greater than 0 and less than 1. NORM.S.INV replaces the older NORMSINV function. For a normal distribution with a different mean or standard deviation, NORM.INV takes those values directly.

## Syntax

```excel
=NORM.S.INV(probability)
```

<!-- Image 1: Probability Scale to Z-Score Scale. See Images/Statistical/NORM.S.INV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | The cumulative probability, greater than 0 and less than 1. A value of 0 or 1, or any value outside that range, returns `#NUM!`. |

### Return Value

A z-score: the number of standard deviations above or below the mean that corresponds to the probability. Negative values appear for probabilities below 0.5. The function returns `#VALUE!` when the probability is not a number and `#NUM!` when it is outside the allowed range.

## Examples

### Example 1: Z-Score for the Upper 97.5 Percent Mark

```excel
=NORM.S.INV(0.975)
```

**Result:** `1.959964`

This is the familiar 1.96 cutoff. Only 2.5 percent of values fall above it.

### Example 2: Lower Tail Cutoff

```excel
=NORM.S.INV(0.05)
```

**Result:** `-1.644854`

Five percent of values fall below this negative z-score. The result is negative because the probability is less than 0.5.

### Example 3: Median Z-Score

```excel
=NORM.S.INV(0.5)
```

**Result:** `0`

The median of a standard normal distribution equals the mean, so the z-score is 0.

### Example 4: Rounded Cutoff

```excel
=ROUND(NORM.S.INV(0.99), 2)
```

**Result:** `2.33`

The 99th percentile sits 2.33 standard deviations above the mean. ROUND keeps two decimal places for a policy document.

### Example 5: Converting Back to Raw Units

```excel
=70 + NORM.S.INV(0.8) * 8
```

**Result:** `76.733`

For a distribution with mean 70 and standard deviation 8, the 80th percentile is 70 plus 0.841621 times 8. This is the same result NORM.INV returns for the same inputs.

<!-- Image 2: Z-Score Conversion to Raw Values. See Images/Statistical/NORM.S.INV.md -->

## Story Problems

### Problem 1: Top One Percent Threshold

A bank flags applications for manual review when their standardized risk score falls in the top 1 percent of the distribution. The analyst needs the z-score for that cutoff.

| Input | Value |
| --- | --- |
| Share of applications to keep below the cutoff | 0.99 |

**Task:** Enter the probability in `E2`, then find the z-score that marks the top 1 percent.

**Solution:**

```excel
=NORM.S.INV(E2)
```

**Answer:** `2.326348`, so applications with a standardized score above 2.33 go to manual review.

### Problem 2: Lower Five Percent Screen

A pharmacy compares standardized wait times with a lower screen that catches the fastest 5 percent of visits. The operations team needs the z-score for the lower limit.

| Input | Value |
| --- | --- |
| Share of visits at or below the limit | 0.05 |

**Task:** Enter the probability in `E2`, then find the z-score for the lower limit.

**Solution:**

```excel
=NORM.S.INV(E2)
```

**Answer:** `-1.644854`, so visits with a standardized wait time at or below about -1.64 fall into the fastest 5 percent.

## Use Cases

### Credit Score Cutoffs

**Scenario:** A lender approves the top 80 percent of applicants by standardized score, so the cutoff sits at the 20th percentile.

```excel
=NORM.S.INV(0.2)
```

**Why It Works:** The probability 0.2 marks the point below which 20 percent of standardized scores fall. Applicants above that z-score are approved, and converting the z-score back to the score scale gives the final cutoff.

### Process Control Limits

**Scenario:** A production team wants upper and lower control limits that include the central 99 percent of standardized measurements.

```excel
=NORM.S.INV(0.995)
```

**Why It Works:** The probability 0.995 gives the upper limit for a two-sided 99 percent band. The lower limit is the negative of the same value because the distribution is symmetric.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The probability is 0, 1, or outside the range. | Enter a probability strictly between 0 and 1. |
| `#VALUE!` | The probability holds text or an empty string. | Re-enter the value as a number. |
| Wrong sign | A probability below 0.5 was expected to give a positive z-score. | Remember that probabilities below 0.5 give negative z-scores. |
| Percentage input returns `#NUM!` | A value such as 95 was entered instead of 0.95. | Enter probabilities as decimals or format the cell as a percentage. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Excel for the web | One required argument. Excel documents NORM.S.INV as the replacement for NORMSINV. |
| Google Sheets | Available | The Google help entry for NORM.S.INV points to the NORMSINV page, which documents a single argument and returns `#NUM!` when the value is not strictly between 0 and 1. |

## Tips and Best Practices

- Keep the probability in its own cell so the threshold is easy to change and audit.
- Convert z-scores back to raw values with the mean and standard deviation when reporting to non-technical readers.
- Use NORM.INV when the mean and standard deviation are not 0 and 1.
- Check the probability direction. A value of 0.05 marks the lower tail, while 0.95 marks the upper tail.

## Related Functions

| Function | Relationship |
| --- | --- |
| [NORM.S.DIST](NORM.S.DIST.md) | The forward calculation: z-score in, probability out. |
| [NORM.INV](NORM.INV.md) | The same reverse calculation for any mean and standard deviation. |
| [NORMSINV](NORMSINV.md) | The older standard normal inverse, kept for compatibility. |
| [CONFIDENCE.NORM](CONFIDENCE.NORM.md) | Uses the normal distribution to size a margin of error. |
| [Z.TEST](Z.TEST.md) | Uses standard normal probabilities to test a sample mean. |

## Official Documentation

- [Microsoft Support: NORM.S.INV function](https://support.microsoft.com/en-us/excel/functions/norm-s-inv-function)
- [Google Docs Editors Help: NORMSINV](https://support.google.com/docs/answer/3094091)
