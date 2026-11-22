---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Delivery Time Thresholds
  - Percentile Cutoffs for Service Levels
related:
  - BETA.DIST
  - GAMMA.DIST
  - GAMMA.INV
  - GAMMADIST
  - NORM.S.INV
  - PERCENTILE.INC
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/gammainv-function
  - https://support.google.com/docs/answer/9116467
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Inverse Gamma Distribution
tags:
  - compatibility
  - distribution
  - excel
  - probability
  - sheets
---

# GAMMAINV

## Description

**GAMMAINV** returns the value `x` at which the gamma cumulative distribution reaches a given probability. It runs the process in reverse: GAMMADIST takes a value and returns a probability, while GAMMAINV takes a probability and returns the value. If `p` equals GAMMADIST(`x`, alpha, beta, TRUE), then GAMMAINV(`p`, alpha, beta) returns `x` again.

Use GAMMAINV to find percentile cutoffs, such as the time by which 90 percent of orders arrive, or the amount that 75 percent of periods stay below. The shape `alpha` and the scale `beta` must match the distribution you are modeling.

GAMMAINV is a compatibility function. Microsoft replaced it with GAMMA.INV, which takes the same arguments. Google documents that the function can be written as either GAMMAINV or GAMMA.INV. New workbooks should use GAMMA.INV, because Microsoft says the compatibility name may not be available in future versions of Excel.

## Syntax

```excel
=GAMMAINV(probability, alpha, beta)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/GAMMAINV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | The cumulative probability to invert. Must be between 0 and 1. |
| `alpha` | Yes | The shape parameter of the gamma distribution. Must be greater than 0. |
| `beta` | Yes | The scale parameter of the gamma distribution. Must be greater than 0. A value of 1 gives the standard gamma distribution. |

### Return Value

A number of zero or greater: the value whose cumulative probability equals `probability`. The function returns `#NUM!` when `probability` is below 0 or above 1, or when `alpha` or `beta` is 0 or less. It returns `#VALUE!` when an argument is not a number, and `#N/A` when the search does not converge within 100 iterations.

## Examples

### Example 1: Median of a Gamma Distribution

```excel
=GAMMAINV(0.5, 2, 3)
```

**Result:** `5.035041`

Half of all outcomes fall below about 5.04 when the shape is 2 and the scale is 3.

### Example 2: Round Trip With GAMMADIST

```excel
=GAMMAINV(GAMMADIST(4, 2, 3, TRUE), 2, 3)
```

**Result:** `4`

GAMMADIST turns 4 into a probability of about 0.384940, and GAMMAINV turns that probability back into 4.

### Example 3: A 90 Percent Cutoff

```excel
=GAMMAINV(0.9, 4, 5)
```

**Result:** `33.4039`

Nine out of ten outcomes fall at or below about 33.40 when the shape is 4 and the scale is 5.

### Example 4: Guarding Against Invalid Probabilities

```excel
=IFERROR(GAMMAINV(1.2, 2, 3), "Check probability")
```

**Result:** `Check probability`

A probability above 1 returns `#NUM!`, so IFERROR shows a message instead.

<!-- Image 2: Probability to Value Mapping. See Images/Statistical/GAMMAINV.md -->

## Story Problems

### Problem 1: Delivery Time Targets

A warehouse records how many minutes each order takes to reach the packing bench. The times follow a gamma distribution with shape 4 and scale 5 minutes.

| Target Level | Probability |
| --- | --- |
| Median | 0.5 |
| Ninety Percent | 0.9 |
| Ninety Five Percent | 0.95 |

**Task:** Put the shape `4` in `E2` and the scale `5` in `E3`, then find the time by which 90 percent of orders reach the packing bench (row Ninety Percent).

**Solution:**

```excel
=GAMMAINV(B3, E2, E3)
```

**Answer:** `33.40` minutes, from the calculated 33.4039. Nine in ten orders reach the bench within that time.

### Problem 2: Reservoir Inflow Planning

A water utility models weekly inflow to a reservoir as a gamma distribution with shape 2 and scale 10 million liters. Planners want the inflow level that is exceeded only one week in four.

**Task:** Find the 75th percentile of weekly inflow.

**Solution:**

```excel
=GAMMAINV(0.75, 2, 10)
```

**Answer:** `26.93` million liters, from the calculated 26.9263. Inflow stays below this level in about three weeks out of four.

## Use Cases

### Percentile Cutoffs for Service Levels

**Scenario:** A support team sets a promise time that 90 percent of customers should see.

```excel
=GAMMAINV(0.9, FittedShape, FittedScale)
```

**Why It Works:** The probability is the service target, and the shape and scale come from the fitted history. Recalculate when the fit changes.

### Delivery Time Thresholds

**Scenario:** A logistics planner wants the time by which half of shipments have left the depot.

```excel
=GAMMAINV(0.5, Alpha, Beta)
```

**Why It Works:** A probability of 0.5 returns the median of the fitted distribution, which is less affected by a few very long delays than the mean.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The probability is below 0 or above 1, or `alpha` or `beta` is 0 or less. | Enter a probability between 0 and 1 and positive parameters. |
| `#VALUE!` | An argument is text or refers to a text cell. | Convert the input to a number. |
| `#N/A` | The search did not converge within 100 iterations. | Check the parameters for extreme values and try again. |
| Wrong value | A percentage such as 90 was entered instead of 0.9. | Divide percentages by 100 before calling the function. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions, marked as a compatibility function | Replaced by GAMMA.INV, which takes the same arguments. |
| Google Sheets | Available as GAMMAINV or GAMMA.INV | The Sheets help page documents GAMMA.INV and states that GAMMAINV is an alternative name. |

## Tips and Best Practices

- Enter probabilities as decimals (0.9), not as whole numbers (90).
- Check the result with GAMMADIST, which should return the probability you started with.
- Use GAMMA.INV in new Excel workbooks because it is the current name.
- Keep `alpha` and `beta` in labeled cells so the cutoffs update when the fit changes.

## Related Functions

| Function | Relationship |
| --- | --- |
| [GAMMA.INV](GAMMA.INV.md) | The current name for this function, with the same arguments. |
| [GAMMA.DIST](GAMMA.DIST.md) | Gives the probability for a value, the reverse of this function. |
| [GAMMADIST](GAMMADIST.md) | The compatibility function that returns the probability for a value. |
| [PERCENTILE.INC](PERCENTILE.INC.md) | Percentile of a list of observed values, without a distribution model. |
| [NORM.S.INV](NORM.S.INV.md) | The matching inverse for the standard normal distribution. |
| [BETA.DIST](BETA.DIST.md) | Another continuous distribution for values between 0 and 1. |

## Official Documentation

- [Microsoft Support: GAMMAINV function](https://support.microsoft.com/en-us/excel/functions/gammainv-function)
- [Google Docs Editors Help: GAMMAINV](https://support.google.com/docs/answer/9116467)
