---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Candidate Shortlisting
  - Defect Rate Screening
  - Scaled Score Conversion
related:
  - NORM.S.INV
  - NORMINV
  - NORMSDIST
  - STANDARDIZE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/normsinv-function
  - https://support.google.com/docs/answer/3094091
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Legacy Standard Normal Inverse
tags:
  - compatibility
  - distribution
  - excel
  - inverse
  - normal-distribution
  - probability
  - sheets
  - z-score
---

# NORMSINV

## Description

**NORMSINV** returns the z-score for a given cumulative probability in the standard normal distribution, which has a mean of 0 and a standard deviation of 1. It reverses NORMSDIST: you supply a probability and the function returns the number of standard deviations that marks it. Use it to set z-score thresholds such as a top-10 percent cutoff.

Microsoft has replaced NORMSINV with NORM.S.INV. Microsoft keeps NORMSINV for backward compatibility, notes that it may be removed in future versions, and recommends NORM.S.INV for new work.

The probability must be greater than 0 and less than 1. Values at or outside those limits return `#NUM!`.

<!-- Image 1: Probability Scale to Z-Score Scale. See Images/Statistical/NORMSINV.md -->

## Syntax

```excel
=NORMSINV(probability)
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | The cumulative probability, greater than 0 and less than 1. |

### Return Value

A z-score: the number of standard deviations from the mean that corresponds to the probability. The function returns `#VALUE!` when the probability is not a number, `#NUM!` when it is 0 or lower or 1 or higher, and `#N/A` when the internal search does not converge after 100 iterations.

## Examples

### Example 1: Z-Score Covering Ninety Percent

```excel
=NORMSINV(0.9)
```

**Result:** `1.281552`

A value at the 90th percentile sits about 1.28 standard deviations above the mean.

### Example 2: Lower Two-Sided Limit

```excel
=NORMSINV(0.025)
```

**Result:** `-1.959964`

Only 2.5 percent of values fall below this z-score, the lower limit of a central 95 percent band.

### Example 3: Median

```excel
=NORMSINV(0.5)
```

**Result:** `0`

The median of the standard normal distribution is 0.

### Example 4: Rounded Upper Quartile

```excel
=ROUND(NORMSINV(0.75), 3)
```

**Result:** `0.674`

The upper quartile sits 0.674 standard deviations above the mean.

### Example 5: Converting to a Scaled Score

```excel
=100 + 15 * NORMSINV(0.9)
```

**Result:** `119.223`

Multiplying the z-score by 15 and adding 100 places the 90th percentile on a scale with mean 100 and standard deviation 15.

<!-- Image 2: Converting a Z-Score to a Scaled Score. See Images/Statistical/NORMSINV.md -->

## Story Problems

### Problem 1: Shortlisting the Top Ten Percent

A recruiting team shortlists candidates whose standardized assessment score is at or above the 90th percentile. The team needs the z-score for that cutoff.

| Input | Value |
| --- | --- |
| Cumulative share for the cutoff | 0.9 |

**Task:** Enter the probability in `E2`, then find the z-score for the cutoff.

**Solution:**

```excel
=NORMSINV(E2)
```

**Answer:** `1.281552`. Candidates with a standardized score of 1.28 or higher are shortlisted.

### Problem 2: Lower Two Percent Defect Screen

A factory flags lots whose standardized defect rate falls in the lowest 2 percent of lots. The quality lead needs the z-score for the flag.

| Input | Value |
| --- | --- |
| Cumulative share for the flag | 0.02 |

**Task:** Enter the probability in `E2`, then find the z-score that marks the lowest 2 percent.

**Solution:**

```excel
=NORMSINV(E2)
```

**Answer:** `-2.053749`. Lots with a standardized score at or below -2.05 are flagged.

## Use Cases

### Candidate Shortlisting

**Scenario:** A hiring panel converts assessment results to z-scores and wants the z-score that marks the top 10 percent.

```excel
=NORMSINV(0.9)
```

**Why It Works:** The probability 0.9 leaves 10 percent of the distribution above the result. Candidates with a z-score at or above that value are shortlisted.

### Scaled Score Conversion

**Scenario:** An assessment reports scores on a scale with mean 100 and standard deviation 15. The team needs the score at the 90th percentile.

```excel
=100 + 15 * NORMSINV(0.9)
```

**Why It Works:** The z-score from NORMSINV is converted back to the reporting scale. The result is the score that 90 percent of results fall at or below.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The probability is 0, 1 or outside the range. | Enter a probability strictly between 0 and 1. |
| `#VALUE!` | The probability holds text or an empty string. | Re-enter the value as a number. |
| `#N/A` | The internal search did not converge after 100 iterations. | Check the probability for extreme values, or switch to NORM.S.INV. |
| Percentage input returns `#NUM!` | A value such as 90 was entered instead of 0.9. | Enter probabilities as decimals. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available, listed in the compatibility group | One required argument. Microsoft recommends NORM.S.INV. |
| Google Sheets | Available | One argument, `x`, which must be strictly between 0 and 1. Values outside that range return `#NUM!`. |

## Tips and Best Practices

- Use NORM.S.INV in new workbooks, because Microsoft recommends it and it accepts the same probability input.
- Keep the probability in its own cell so the threshold is easy to change and review.
- Convert z-scores back to raw values with the mean and standard deviation when you report to others.
- Remember that probabilities below 0.5 return negative z-scores.

## Related Functions

| Function | Relationship |
| --- | --- |
| [NORM.S.INV](NORM.S.INV.md) | The current replacement with one argument. |
| [NORMINV](NORMINV.md) | The inverse for any mean and standard deviation. |
| [NORMSDIST](NORMSDIST.md) | The forward calculation: z-score in, probability out. |
| [STANDARDIZE](STANDARDIZE.md) | Converts a raw value to a z-score. |

## Official Documentation

- [Microsoft Support: NORMSINV function](https://support.microsoft.com/en-us/excel/functions/normsinv-function)
- [Google Docs Editors Help: NORMSINV](https://support.google.com/docs/answer/3094091)
