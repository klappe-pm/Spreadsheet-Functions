---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Normal Curve Height
  - Z Score Density
related:
  - NORM.DIST
  - NORM.S.DIST
  - NORM.S.INV
  - NORMDIST
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/phi-function
  - https://support.google.com/docs/answer/9116365
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Normal Density
tags:
  - density
  - distribution
  - excel
  - normal
  - sheets
---

# PHI

## Description

**PHI** returns the value of the density function of the standard normal distribution at a given point x. The standard normal distribution has a mean of 0 and a standard deviation of 1, so PHI gives the height of the bell curve at x. The curve is highest at 0, where PHI returns about 0.398942.

PHI returns a density, not a probability. A density can be larger than 1 for some distributions, and for the standard normal curve it is simply a height on the curve. To find the probability that a value falls below x, use NORM.S.DIST instead. Google Sheets documents PHI as the standard normal case of NORMDIST, with the mean set to 0, the standard deviation set to 1 and the cumulative argument set to FALSE.

For a normal distribution with a different mean or standard deviation, convert the value to a z score first with (x − mean) ÷ standard deviation, then divide the PHI result by the standard deviation to express the density on the original scale.

## Syntax

```excel
=PHI(x)
```

<!-- Image 1: Phi Argument Diagram. See Images/Statistical/PHI.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The number at which you want the density of the standard normal distribution, such as a z score. |

### Return Value

The density of the standard normal distribution at `x`, a positive decimal. The function returns `#NUM!` for a numeric value that is not valid, and `#VALUE!` for a non-numeric argument.

## Examples

### Example 1: The Peak of the Curve

```excel
=PHI(0)
```

**Result:** `0.398942280`

The density at the center of the standard normal curve is 1 ÷ √(2π).

### Example 2: One Standard Deviation Above the Mean

```excel
=PHI(1)
```

**Result:** `0.241970725`

The curve is lower one standard deviation from the mean than at its peak.

### Example 3: Symmetry Around Zero

```excel
=PHI(-1)
```

**Result:** `0.241970725`

The standard normal curve is symmetric, so negative and positive z scores of the same size return the same density.

### Example 4: Two Standard Deviations Above the Mean

```excel
=PHI(2)
```

**Result:** `0.053990967`

The curve is much lower at two standard deviations, so values there are much less common.

## Story Problems

### Problem 1: Checking a Sensor Reading

A quality engineer converts one sensor reading to a z score of 0.75 and wants the height of the standard normal curve at that point.

| Reading | Z Score |
| --- | --- |
| Sensor A | 0.75 |

**Task:** Find the density at the z score in `B2`.

**Solution:**

```excel
=PHI(B2)
```

**Answer:** `0.301137432`. The curve is about 0.30 at this point, below its peak of 0.399 at zero.

### Problem 2: Comparing Two Readings

Two readings in `B2:B3` have z scores of 0.5 and 1.5.

| Reading | Z Score |
| --- | --- |
| Reading A | 0.5 |
| Reading B | 1.5 |

**Task:** Compare the density at each z score to see which reading sits closer to the center of the distribution.

**Solution:**

```excel
=PHI(B2)
```

Fill the formula down to `B3`.

**Answer:** Reading A is `0.352065327` and Reading B is `0.129517596`. Reading A has the higher density, so it sits closer to the center.

<!-- Image 2: Standard Normal Curve With Two Readings. See Images/Statistical/PHI.md -->

## Use Cases

### Normal Curve Height

**Scenario:** An analyst plots the expected density of part lengths from their mean and standard deviation.

```excel
=PHI((Parts[Length] - AVERAGE(Parts[Length])) / STDEV.S(Parts[Length])) / STDEV.S(Parts[Length])
```

**Why It Works:** The formula converts each length to a z score, applies PHI, and divides by the standard deviation so the density matches the original length scale.

### Z Score Density

**Scenario:** A statistics student checks the density at a z score computed in a helper column.

```excel
=PHI(Z)
```

**Why It Works:** PHI takes the z score directly, so the helper column does the standardizing. For a probability rather than a height, use NORM.S.DIST on the same z score.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The argument is a numeric value that the function does not accept. | Check the input cell and the calculation that produced it. |
| `#VALUE!` | The argument is text or a blank cell. | Enter a number or reference a cell that holds one. |
| Density used as a probability | PHI returns a height on the curve, not a chance. | Use NORM.S.DIST when the result must be a probability. |
| Wrong scale | The value was not standardized for a non-standard normal distribution. | Convert to a z score first, then divide by the standard deviation. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions | Accepts one numeric argument. Returns `#NUM!` for invalid numbers and `#VALUE!` for non-numeric input. |
| Google Sheets | Available | Equivalent to NORMDIST with mean 0, standard deviation 1 and cumulative set to FALSE. The official page does not list error conditions. |

## Tips and Best Practices

- Standardize with a helper column, so PHI always receives a z score.
- Use NORM.S.DIST when the report needs the probability of falling below a value.
- Round the output for display only, because the calculation keeps full precision.
- Check one value against a normal curve table or a second formula before you publish a chart built on PHI.

## Related Functions

| Function | Relationship |
| --- | --- |
| [NORM.S.DIST](NORM.S.DIST.md) | Returns the cumulative probability for the standard normal distribution. |
| [NORM.DIST](NORM.DIST.md) | Returns the density or cumulative value for any mean and standard deviation. |
| [NORM.S.INV](NORM.S.INV.md) | Returns the z score for a given cumulative probability, the inverse of NORM.S.DIST. |
| [NORMDIST](NORMDIST.md) | Legacy form of NORM.DIST that PHI matches when the mean is 0 and the standard deviation is 1. |

## Official Documentation

- [Microsoft Support: PHI function](https://support.microsoft.com/en-us/excel/functions/phi-function)
- [Google Docs Editors Help: PHI](https://support.google.com/docs/answer/9116365)
