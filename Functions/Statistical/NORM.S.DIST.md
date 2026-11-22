---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Control Chart Signals
  - Peer Ranking
  - Z-Score Comparisons
related:
  - NORM.DIST
  - NORM.S.INV
  - NORMSDIST
  - STANDARDIZE
  - Z.TEST
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/norm-s-dist-function
  - https://support.google.com/docs/answer/3094089
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Standard Normal Distribution
  - Z-Score Probability
tags:
  - distribution
  - excel
  - normal-distribution
  - probability
  - sheets
  - z-score
---

# NORM.S.DIST

## Description

**NORM.S.DIST** returns the standard normal distribution, the normal curve with a mean of 0 and a standard deviation of 1. Most business workflows convert data to z-scores first, which express each value as the number of standard deviations it sits from the mean. NORM.S.DIST then turns a z-score into a probability.

The cumulative argument sets the form of the result. TRUE returns the chance of a z-score at or below the value, and FALSE returns the height of the standard normal curve at that point. Use TRUE for probability questions and FALSE only when you compare curve shapes.

NORM.S.DIST replaces the older NORMSDIST function. Unlike Excel's NORMSDIST, which returns only the probability, it has a cumulative argument that covers both the probability and the density in one function. For data with any other mean and standard deviation, use NORM.DIST.

## Syntax

```excel
=NORM.S.DIST(z, cumulative)
```

<!-- Image 1: Standard Normal Curve With Z-Scores. See Images/Statistical/NORM.S.DIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `z` | Yes | The z-score, the number of standard deviations from the mean, at which to evaluate the distribution. |
| `cumulative` | Yes | TRUE returns the chance of a value at or below z. FALSE returns the density of the standard normal curve at z. |

### Return Value

A decimal number. With TRUE it is a probability between 0 and 1. With FALSE it is a density value. The function returns `#VALUE!` when z is not a number.

## Examples

### Example 1: Probability Below a Z-Score of 1.2

```excel
=NORM.S.DIST(1.2, TRUE)
```

**Result:** `0.884930`

About 88 percent of values in a standard normal distribution fall at or below 1.2 standard deviations above the mean.

### Example 2: Probability Below a Negative Z-Score

```excel
=NORM.S.DIST(-0.5, TRUE)
```

**Result:** `0.308538`

Values below the mean make up more than half of the distribution, so a z-score below 0 gives a probability under 0.5. This result shows about 31 percent.

### Example 3: Density at the Mean

```excel
=NORM.S.DIST(0, FALSE)
```

**Result:** `0.398942`

The curve is at its highest point at the mean. The density is not a probability, so use it only to compare shapes.

### Example 4: Two-Sided Tail Probability

```excel
=2 * (1 - NORM.S.DIST(1.96, TRUE))
```

**Result:** `0.049996`

Doubling the upper tail gives the chance of a value at least 1.96 standard deviations away from the mean in either direction, about 5 percent.

### Example 5: Working From Raw Data

```excel
=NORM.S.DIST(STANDARDIZE(85, 70, 8), TRUE)
```

**Result:** `0.969604`

STANDARDIZE converts 85 to the z-score 1.875 for a mean of 70 and a standard deviation of 8. NORM.S.DIST then returns the same probability that NORM.DIST returns for the raw value.

<!-- Image 2: Two-Sided Tail Areas. See Images/Statistical/NORM.S.DIST.md -->

## Story Problems

### Problem 1: Percentile of a Standardized Score

A student's standardized test result is 1.2 z-scores above the mean. The counselor wants to know what share of peers the student scored at or above.

| Input | Value |
| --- | --- |
| Student z-score | 1.2 |

**Task:** Enter the z-score in `E2`, then find the share of peers scoring at or below the student.

**Solution:**

```excel
=NORM.S.DIST(E2, TRUE)
```

**Answer:** `0.88493`, or about 88.5 percent. The student scored at or above roughly 88 percent of peers.

### Problem 2: Control Chart Signal

A process control chart flags any measurement whose z-score is more than 1.96 standard deviations from the mean in either direction. The quality engineer wants the chance that a process in control triggers the flag.

| Input | Value |
| --- | --- |
| Flag threshold (z-score) | 1.96 |

**Task:** Enter the threshold in `E2`, then find the two-sided chance of a flag.

**Solution:**

```excel
=2 * (1 - NORM.S.DIST(E2, TRUE))
```

**Answer:** `0.049996`, or about 5 percent. About one measurement in twenty will be flagged even when the process is working correctly.

## Use Cases

### Control Chart Signals

**Scenario:** A plant converts each sensor reading to a z-score and wants to know how often a normal reading crosses a limit of 2.5 standard deviations.

```excel
=2 * (1 - NORM.S.DIST(B2, TRUE))
```

**Why It Works:** `B2` holds the limit in z-score units. Doubling the upper tail covers both sides of the mean, so the result is the chance of a false alarm.

### Peer Ranking

**Scenario:** An analyst ranks employees by z-score from a performance survey and reports the share of colleagues each person outranks.

```excel
=NORM.S.DIST(C2, TRUE)
```

**Why It Works:** `C2` holds the employee's z-score. The result is the share of the distribution at or below that score, which is a percentile rank.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | `z` holds text or an empty string. | Convert the value to a number or check the cell reference. |
| Result above 1 | `cumulative` is FALSE, which returns a density. | Set `cumulative` to TRUE for a probability. |
| Result near 0.5 when a tail was expected | The raw value was entered instead of its z-score. | Standardize the value with STANDARDIZE or subtract the mean and divide by the standard deviation first. |
| Missing argument | The cumulative argument was left out. | Add TRUE or FALSE as the second argument. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Excel for the web | Two required arguments. Excel documents NORM.S.DIST as the replacement for NORMSDIST. |
| Google Sheets | Available | The Google help entry for NORM.S.DIST points to the NORMSDIST page, which documents the same cumulative argument. |

## Tips and Best Practices

- Standardize raw values with STANDARDIZE before you apply NORM.S.DIST to a different mean and standard deviation.
- Use TRUE for probabilities and FALSE only for density comparisons.
- Put the z-score in its own column so the reasoning is visible in the sheet.
- Use NORM.DIST when the data does not need standardizing.

## Related Functions

| Function | Relationship |
| --- | --- |
| [NORM.DIST](NORM.DIST.md) | The general version for any mean and standard deviation. |
| [NORM.S.INV](NORM.S.INV.md) | The reverse calculation: probability in, z-score out. |
| [NORMSDIST](NORMSDIST.md) | The older standard normal function, which has no cumulative argument in Excel. |
| [STANDARDIZE](STANDARDIZE.md) | Converts a raw value to a z-score. |
| [Z.TEST](Z.TEST.md) | Uses the standard normal distribution to test a sample mean. |

## Official Documentation

- [Microsoft Support: NORM.S.DIST function](https://support.microsoft.com/en-us/excel/functions/norm-s-dist-function)
- [Google Docs Editors Help: NORMSDIST](https://support.google.com/docs/answer/3094089)
