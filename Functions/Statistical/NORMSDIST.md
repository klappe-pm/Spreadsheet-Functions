---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Delivery Delay Ranking
  - Quality Score Percentiles
  - Two-Sided Tail Checks
related:
  - NORM.S.DIST
  - NORMDIST
  - NORMSINV
  - STANDARDIZE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/normsdist-function
  - https://support.google.com/docs/answer/3094089
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Legacy Standard Normal Probability
tags:
  - compatibility
  - distribution
  - excel
  - normal-distribution
  - probability
  - sheets
  - z-score
---

# NORMSDIST

## Description

**NORMSDIST** returns the standard normal cumulative distribution for a z-score. The standard normal distribution has a mean of 0 and a standard deviation of 1, so the function returns the chance of a value at or below the z-score. Use it to convert a standardized value into a percentile.

Microsoft has replaced NORMSDIST with NORM.S.DIST. Microsoft keeps NORMSDIST for backward compatibility, notes that it may not be available in future versions of Excel, and recommends NORM.S.DIST for new work.

In Excel, NORMSDIST takes only the z-score and always returns the cumulative probability. Google Sheets documents a second argument, cumulative, that switches between the cumulative probability and the density, so a formula that works in one platform may need a change in the other.

<!-- Image 1: Standard Normal Curve With Z-Scores. See Images/Statistical/NORMSDIST.md -->

## Syntax

```excel
=NORMSDIST(z)
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `z` | Yes | The z-score, the number of standard deviations from the mean, at which to evaluate the distribution. |

### Return Value

A probability between 0 and 1: the chance of a standard normal value at or below z. The function returns `#VALUE!` when z is not a number.

## Examples

### Example 1: Percentile of a Z-Score of 0.67

```excel
=NORMSDIST(0.67)
```

**Result:** `0.748571`

About 75 percent of standard normal values fall at or below 0.67.

### Example 2: Probability Below a Negative Z-Score

```excel
=NORMSDIST(-1.2)
```

**Result:** `0.115070`

About 11.5 percent of values fall at or below 1.2 standard deviations below the mean.

### Example 3: Probability at the Mean

```excel
=NORMSDIST(0)
```

**Result:** `0.5`

Half the distribution lies at or below the mean.

### Example 4: Upper Tail Probability

```excel
=1 - NORMSDIST(2.33)
```

**Result:** `0.009903`

The chance of a value above 2.33 standard deviations is under 1 percent.

### Example 5: Central Band Probability

```excel
=NORMSDIST(1.5) - NORMSDIST(-1.5)
```

**Result:** `0.866386`

The central band from -1.5 to 1.5 standard deviations holds about 86.6 percent of values.

<!-- Image 2: Central Band Between Two Z-Scores. See Images/Statistical/NORMSDIST.md -->

## Story Problems

### Problem 1: Delivery Delay Percentile

A carrier measures each route's average delay as a z-score. A route with a z-score of 0.67 is compared with the rest of the network. The analyst wants the share of routes with a delay at or below that level.

| Input | Value |
| --- | --- |
| Route z-score | 0.67 |

**Task:** Enter the z-score in `E2`, then find the share of routes at or below it.

**Solution:**

```excel
=NORMSDIST(E2)
```

**Answer:** `0.748571`, or about 74.9 percent of routes.

### Problem 2: Low Quality Score Share

A supplier's quality scores are standardized, and a batch sits at a z-score of -1.2. The quality team wants the share of batches that score at or below this level.

| Input | Value |
| --- | --- |
| Batch z-score | -1.2 |

**Task:** Enter the z-score in `E2`, then find the share of batches at or below it.

**Solution:**

```excel
=NORMSDIST(E2)
```

**Answer:** `0.115070`, or about 11.5 percent of batches.

## Use Cases

### Delivery Delay Ranking

**Scenario:** A logistics analyst converts each route's delay to a z-score and ranks the routes by percentile.

```excel
=NORMSDIST(C2)
```

**Why It Works:** `C2` holds the route z-score. The result is the percentile rank for that route, which can be sorted or charted.

### Two-Sided Tail Checks

**Scenario:** A lab flags a result when its z-score is more than 2 standard deviations from the mean in either direction.

```excel
=2 * (1 - NORMSDIST(ABS(D2)))
```

**Why It Works:** ABS removes the sign, and doubling the upper tail covers both sides. The result is the chance of a flag under a normal process.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | `z` holds text or an empty string. | Convert the value to a number or check the cell reference. |
| Result near 0.5 when a tail was expected | A raw value was entered instead of its z-score. | Standardize the value first with STANDARDIZE. |
| Missing argument in Google Sheets | A formula written for Excel omits the cumulative argument. | Add TRUE for the cumulative probability as the second argument. |
| Unexpected density in Google Sheets | `cumulative` is FALSE, which returns the density. | Set `cumulative` to TRUE for a probability. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available, listed in the compatibility group | One argument, `z`, and always the cumulative probability. Microsoft recommends NORM.S.DIST. |
| Google Sheets | Available | Two arguments: `x` and `cumulative`. With TRUE it returns the cumulative probability, and with FALSE the density. |

## Tips and Best Practices

- Use NORM.S.DIST in new workbooks, because it has a cumulative argument in Excel and Microsoft recommends it.
- Convert raw values with STANDARDIZE or the formula (value minus mean) divided by standard deviation before you call this function.
- Keep the z-score in its own column so the reasoning is visible.
- When a workbook is shared with Sheets users, check that every NORMSDIST formula has the arguments that platform expects.

## Related Functions

| Function | Relationship |
| --- | --- |
| [NORM.S.DIST](NORM.S.DIST.md) | The current replacement, with a cumulative argument in Excel. |
| [NORMDIST](NORMDIST.md) | The general version for any mean and standard deviation. |
| [NORMSINV](NORMSINV.md) | The inverse: probability in, z-score out. |
| [STANDARDIZE](STANDARDIZE.md) | Converts a raw value to a z-score. |

## Official Documentation

- [Microsoft Support: NORMSDIST function](https://support.microsoft.com/en-us/excel/functions/normsdist-function)
- [Google Docs Editors Help: NORMSDIST](https://support.google.com/docs/answer/3094089)
