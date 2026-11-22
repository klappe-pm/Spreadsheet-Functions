---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Fill Weight Tolerances
  - Within Sigma Limits
related:
  - NORM.DIST
  - NORM.S.DIST
  - NORM.S.INV
  - NORMDIST
  - NORMSDIST
  - STANDARDIZE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/gauss-function
  - https://support.google.com/docs/answer/9116278
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Normal Deviation Probability
  - Sigma Band Probability
tags:
  - distribution
  - excel
  - normal-distribution
  - probability
  - sheets
---

# GAUSS

## Description

**GAUSS** returns the probability that a value drawn from a standard normal distribution falls between the mean and a point `z` standard deviations above or below the mean. The result is always a number from -0.5 to 0.5. It is the standard normal cumulative distribution minus 0.5, so GAUSS(`z`) equals NORM.S.DIST(`z`, TRUE) minus 0.5.

Use GAUSS when you want the share of values inside one side of a band around the mean, for example the chance that a measurement sits between the target and one standard deviation above it. Double the result to get the share inside a symmetric band, because the normal curve is symmetric around the mean. A negative `z` returns a negative number with the same size, so GAUSS(-1) equals -GAUSS(1).

GAUSS is not a compatibility function. For a full cumulative probability, use NORM.S.DIST, which returns the total probability up to `z` instead of the part between the mean and `z`.

## Syntax

```excel
=GAUSS(z)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/GAUSS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `z` | Yes | The number of standard deviations from the mean. Positive values look above the mean, and negative values look below it. |

### Return Value

A number from -0.5 to 0.5: the probability between the mean and `z` standard deviations from the mean, with the sign of `z`. The function returns `#NUM!` for an invalid number and `#VALUE!` for a value of the wrong data type. An empty cell reference returns 0 in Google Sheets.

## Examples

### Example 1: One and a Half Standard Deviations

```excel
=GAUSS(1.5)
```

**Result:** `0.433193`

About 43 percent of values lie between the mean and a point 1.5 standard deviations above it.

### Example 2: A Negative Distance

```excel
=GAUSS(-1)
```

**Result:** `-0.341345`

The sign shows the direction. The size matches GAUSS(1), which is the share between the mean and one standard deviation below it.

### Example 3: Symmetric Band

```excel
=2*GAUSS(1)
```

**Result:** `0.682689`

Doubling the one-sided result gives the share of values within one standard deviation on either side of the mean.

### Example 4: Matching NORM.S.DIST

```excel
=NORM.S.DIST(2, TRUE) - 0.5
```

**Result:** `0.477250`

This equals GAUSS(2), because the cumulative distribution up to 2 is 0.977250.

<!-- Image 2: Share of the Curve Between the Mean and z. See Images/Statistical/GAUSS.md -->

## Story Problems

### Problem 1: Bottle Fill Tolerance

A bottling line fills bottles to a target of 500 ml with a standard deviation of 4 ml. The quality team wants the share of fills that land between the target and 506 ml.

| Measure | Value |
| --- | --- |
| Target (ml) | 500 |
| Standard deviation (ml) | 4 |
| Upper point (ml) | 506 |

**Task:** Find the share of fills between the target and 506 ml.

**Solution:**

```excel
=GAUSS((506 - 500) / 4)
```

**Answer:** `0.4332`, because 506 is 1.5 standard deviations above the target. About 43 percent of fills fall in that range.

### Problem 2: Score Bands

Test scores are normally distributed with a mean of 70 and a standard deviation of 8. The teacher wants the share of students within one standard deviation of the mean, which runs from 62 to 78.

**Task:** Find the share of scores between 62 and 78.

**Solution:**

```excel
=2*GAUSS((78 - 70) / 8)
```

**Answer:** `0.6827`, which means about 68 percent of students score within one standard deviation of the mean.

## Use Cases

### Fill Weight Tolerances

**Scenario:** A plant manager checks how often a fill lands above a limit that is a fixed number of standard deviations from the target.

```excel
=GAUSS((UpperLimit - Target) / StdDev)
```

**Why It Works:** Converting the limit to a z value makes the same formula work for any product, as long as the process is close to normal.

### Within Sigma Limits

**Scenario:** A quality analyst reports the share of measurements inside plus or minus two standard deviations for a monthly control chart.

```excel
=2*GAUSS(2)
```

**Why It Works:** The symmetric band is twice the one-sided share. Check that the data is roughly bell shaped before you report the result.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | `z` is text or refers to a text cell. | Convert the input to a number. |
| `#NUM!` | `z` is not a valid number. | Check the calculation that produces `z`. |
| Result near 0.5 or -0.5 | The result was read as a full probability. | Add 0.5 to get the cumulative probability, or use NORM.S.DIST. |
| Half the expected value | The one-sided result was used for a two-sided band. | Multiply by 2 for a symmetric band. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Listed on the Microsoft page with no version restriction | Returns the part between the mean and `z`. The page notes that GAUSS(z) equals NORM.S.DIST(z, TRUE) minus 0.5. |
| Google Sheets | Available | The same single argument. An empty cell reference returns 0. |

## Tips and Best Practices

- Use NORM.S.DIST when you need the full cumulative probability, which is often easier to explain.
- Convert raw values to z values with (value minus mean) divided by standard deviation before calling the function.
- Double the result only for symmetric bands around the mean.
- Keep the sign in mind when a negative z is used.

## Related Functions

| Function | Relationship |
| --- | --- |
| [NORM.S.DIST](NORM.S.DIST.md) | Full cumulative standard normal probability. GAUSS equals this minus 0.5. |
| [NORM.DIST](NORM.DIST.md) | Normal distribution for any mean and standard deviation. |
| [NORM.S.INV](NORM.S.INV.md) | Returns the z value for a cumulative probability, the reverse of GAUSS. |
| [NORMDIST](NORMDIST.md) | Compatibility version of NORM.DIST. |
| [NORMSDIST](NORMSDIST.md) | Compatibility version of NORM.S.DIST. |
| [STANDARDIZE](STANDARDIZE.md) | Converts a value to a z score before using GAUSS. |

## Official Documentation

- [Microsoft Support: GAUSS function](https://support.microsoft.com/en-us/excel/functions/gauss-function)
- [Google Docs Editors Help: GAUSS](https://support.google.com/docs/answer/9116278)
