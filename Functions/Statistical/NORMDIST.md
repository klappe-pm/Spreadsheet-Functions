---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Rainfall Planning
  - Service Time Targets
  - Shipment Weight Checks
related:
  - NORM.DIST
  - NORMINV
  - NORMSDIST
  - STANDARDIZE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/normdist-function
  - https://support.google.com/docs/answer/3094021
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Legacy Normal Distribution
tags:
  - compatibility
  - distribution
  - excel
  - normal-distribution
  - probability
  - sheets
---

# NORMDIST

## Description

**NORMDIST** returns the normal distribution for a value, given the mean and standard deviation of the data. It performs the same calculation as NORM.DIST, which is the function Microsoft now recommends. Use it to find the chance that a value is at or below a threshold, or the height of the curve at a point.

Microsoft has superseded NORMDIST with NORM.DIST, which it describes as the function with improved accuracy and a name that better reflects its purpose. NORMDIST remains for backward compatibility and Microsoft warns that it may not be available in future versions of Excel. Use NORM.DIST in new workbooks and keep NORMDIST only where older files depend on it.

With cumulative set to TRUE the function returns the chance of a value at or below x. With cumulative set to FALSE it returns the density at x, which is not a probability.

<!-- Image 1: Normal Curve With Mean and Standard Deviation. See Images/Statistical/NORMDIST.md -->

## Syntax

```excel
=NORMDIST(x, mean, standard_dev, cumulative)
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The value at which you want the distribution evaluated. |
| `mean` | Yes | The arithmetic mean of the distribution. |
| `standard_dev` | Yes | The standard deviation of the distribution. A value of zero or less returns `#NUM!`. |
| `cumulative` | Yes | TRUE returns the cumulative distribution. FALSE returns the probability density at x. |

### Return Value

A decimal number. With TRUE it is a probability between 0 and 1. With FALSE it is a density value. The function returns `#VALUE!` when an argument is not a number and `#NUM!` when `standard_dev` is zero or less.

## Examples

The examples use a mean of 80 in `B2` and a standard deviation of 12 in `B3`, which describe monthly rainfall in millimeters.

### Example 1: Cumulative Share Up to a Limit

```excel
=NORMDIST(95, 80, 12, TRUE)
```

**Result:** `0.894350`

About 89 percent of months have rainfall at or below 95 mm.

### Example 2: Density at the Mean

```excel
=NORMDIST(80, 80, 12, FALSE)
```

**Result:** `0.033245`

The curve is highest at the mean. This value is a density, not a probability, so do not report it as a percentage.

### Example 3: Share Between Two Values

```excel
=NORMDIST(95, 80, 12, TRUE) - NORMDIST(70, 80, 12, TRUE)
```

**Result:** `0.692022`

The formula subtracts the cumulative chance at 70 mm from the chance at 95 mm, which gives the share of months between the two amounts.

### Example 4: Percentage for a Summary

```excel
=ROUND(NORMDIST(95, 80, 12, TRUE) * 100, 1)
```

**Result:** `89.4`

The probability is multiplied by 100 and rounded to one decimal place for a percentage summary.

### Example 5: Same Result With NORMSDIST

```excel
=NORMSDIST((95 - 80) / 12)
```

**Result:** `0.894350`

Converting 95 to a z-score of 1.25 and passing it to NORMSDIST returns the same probability as Example 1.

<!-- Image 2: Equivalent Calculation Through a Z-Score. See Images/Statistical/NORMDIST.md -->

## Story Problems

### Problem 1: Rainy Months for a Reservoir

A reservoir receives monthly rainfall with a mean of 80 mm and a standard deviation of 12 mm. The water authority wants the share of months with rainfall at or below 95 mm.

| Input | Value |
| --- | --- |
| Mean rainfall (mm) | 80 |
| Standard deviation (mm) | 12 |
| Threshold (mm) | 95 |

**Task:** Enter the inputs in `E2:E4`, then find the share of months at or below the threshold.

**Solution:**

```excel
=NORMDIST(E4, E2, E3, TRUE)
```

**Answer:** `0.89435`, or about 89.4 percent of months.

### Problem 2: Call Center Wait Times

A support line has an average wait of 4.5 minutes with a standard deviation of 1.2 minutes. The manager wants the share of calls answered between 3 and 6 minutes.

| Input | Value |
| --- | --- |
| Mean wait (minutes) | 4.5 |
| Standard deviation (minutes) | 1.2 |
| Shortest target wait (minutes) | 3 |
| Longest target wait (minutes) | 6 |

**Task:** Enter the inputs in `E2:E5`, then find the share of calls whose wait falls between the two targets.

**Solution:**

```excel
=NORMDIST(E5, E2, E3, TRUE) - NORMDIST(E4, E2, E3, TRUE)
```

**Answer:** `0.78870`, or about 78.9 percent of calls fall inside the target window.

## Use Cases

### Rainfall Planning

**Scenario:** A drainage team sizes channels so that they handle rainfall up to the level that 90 percent of months stay below.

```excel
=NORMDIST(B2, $F$1, $F$2, TRUE)
```

**Why It Works:** `B2` holds the candidate capacity, while `F1` and `F2` hold the mean and standard deviation. The result shows the share of months the channel would handle without overflow.

### Shipment Weight Checks

**Scenario:** A packing line accepts boxes whose weight falls between 9.8 kg and 10.2 kg. The weights have a mean of 10.0 kg and a standard deviation of 0.1 kg.

```excel
=NORMDIST(10.2, 10, 0.1, TRUE) - NORMDIST(9.8, 10, 0.1, TRUE)
```

**Why It Works:** The difference between two cumulative values gives the share of boxes inside the acceptance band.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `standard_dev` is zero or negative. | Check the standard deviation or recalculate it from the data. |
| `#VALUE!` | An argument holds text or another nonnumeric value. | Re-enter the value as a number. |
| Result is not a probability | `cumulative` is FALSE, which returns a density. | Set `cumulative` to TRUE for a probability. |
| Unexpected values in a new workbook | A new workbook uses NORMDIST where NORM.DIST is the current choice. | Replace the function with NORM.DIST and keep the same arguments. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available, listed in the compatibility group | Four required arguments. Microsoft recommends NORM.DIST and warns that NORMDIST may not be available in future versions. |
| Google Sheets | Available | Documented with the same four arguments, including the cumulative argument. |

## Tips and Best Practices

- Use NORM.DIST in new workbooks, and keep NORMDIST only in files that already rely on it.
- Use TRUE for probability questions and FALSE only when you need the density.
- Store the mean and standard deviation in labeled cells so every formula uses the same values.
- Round results only for display, so later calculations keep full precision.

## Related Functions

| Function | Relationship |
| --- | --- |
| [NORM.DIST](NORM.DIST.md) | The current replacement with the same arguments. |
| [NORMINV](NORMINV.md) | The inverse of this function: probability in, value out. |
| [NORMSDIST](NORMSDIST.md) | The standard normal version, with mean 0 and standard deviation 1. |
| [STANDARDIZE](STANDARDIZE.md) | Converts a raw value to a z-score for use with the standard normal functions. |

## Official Documentation

- [Microsoft Support: NORMDIST function](https://support.microsoft.com/en-us/excel/functions/normdist-function)
- [Google Docs Editors Help: NORMDIST](https://support.google.com/docs/answer/3094021)
