---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Service Ticket Resolution Times
  - Waiting Time Probabilities
related:
  - BETA.DIST
  - GAMMA
  - GAMMA.DIST
  - GAMMA.INV
  - GAMMAINV
  - GAMMALN
  - NORM.S.DIST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/gammadist-function
  - https://support.google.com/docs/answer/7013989
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Gamma Distribution
  - Legacy Gamma Distribution
tags:
  - compatibility
  - distribution
  - excel
  - probability
  - sheets
---

# GAMMADIST

## Description

**GAMMADIST** returns the gamma distribution for a value `x`. A gamma distribution models positive quantities that are skewed to the right, such as the time needed to finish a series of steps, the total waiting time for several events, or the amount of rainfall in a period. With `cumulative` set to TRUE, the function returns the probability that a value is less than or equal to `x`. With FALSE, it returns the probability density at `x`.

GAMMADIST is a compatibility function. Microsoft replaced it with GAMMA.DIST, which takes the same four arguments and may offer improved accuracy. GAMMADIST still calculates in current versions of Excel, but Microsoft says it may not be available in future versions. Google documents GAMMA.DIST as synonymous with GAMMADIST, so new workbooks should use GAMMA.DIST.

The shape argument `alpha` controls how the curve bends. When `alpha` is 1, the distribution becomes the exponential distribution. The scale argument `beta` stretches the curve along the x axis. When `beta` is 1, the function returns the standard gamma distribution.

## Syntax

```excel
=GAMMADIST(x, alpha, beta, cumulative)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/GAMMADIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The value at which to evaluate the distribution. Must be zero or greater. |
| `alpha` | Yes | The shape parameter. Must be greater than 0. |
| `beta` | Yes | The scale parameter. Must be greater than 0. A value of 1 gives the standard gamma distribution. |
| `cumulative` | Yes | TRUE returns the cumulative distribution (the probability of a value up to `x`). FALSE returns the probability density. |

### Return Value

A number between 0 and 1 when `cumulative` is TRUE, or a non-negative density when it is FALSE. The function returns `#NUM!` when `x` is negative or when `alpha` or `beta` is 0 or less, and `#VALUE!` when any argument is not a number.

## Examples

### Example 1: Cumulative Probability

```excel
=GAMMADIST(4, 2, 3, TRUE)
```

**Result:** `0.384940`

About 38 percent of cases finish at or before 4 time units when the shape is 2 and the scale is 3.

### Example 2: Probability Density

```excel
=GAMMADIST(4, 2, 3, FALSE)
```

**Result:** `0.117154`

The density is the height of the curve at `x = 4`. It is not a probability, so it can be greater than 1 for other inputs.

<!-- Image 2: Density and Cumulative Curves. See Images/Statistical/GAMMADIST.md -->

### Example 3: Exponential Special Case

```excel
=GAMMADIST(2, 1, 4, TRUE)
```

**Result:** `0.393469`

With `alpha` set to 1, the result matches the exponential formula `1 - EXP(-2/4)`.

### Example 4: Guarding Against Invalid Input

```excel
=IFERROR(GAMMADIST(-1, 2, 3, TRUE), "Invalid")
```

**Result:** `Invalid`

A negative `x` returns `#NUM!`, so IFERROR replaces the error with a label.

## Story Problems

### Problem 1: Support Ticket Resolution

A help desk records how many hours each ticket takes to close. Historical data fits a gamma distribution with shape 2 and scale 3 hours.

| Ticket | Hours Open |
| --- | --- |
| T1 | 2 |
| T2 | 4 |
| T3 | 6 |
| T4 | 8 |

**Task:** Put the shape `2` in `D2` and the scale `3` in `D3`, then find the probability that a ticket closes within 6 hours (row T3).

**Solution:**

```excel
=GAMMADIST(B4, D2, D3, TRUE)
```

**Answer:** `0.5940`. The cumulative probability at 6 hours is about 59 percent.

### Problem 2: Machine Repair Times

A maintenance team has repair times that follow a gamma distribution with shape 3 and scale 2 days. The shop wants to know how often a repair runs past five days.

| Repair | Days |
| --- | --- |
| R1 | 3 |
| R2 | 5 |
| R3 | 7 |

**Task:** Find the probability that a repair takes more than 5 days.

**Solution:**

```excel
=1-GAMMADIST(5, 3, 2, TRUE)
```

**Answer:** `0.5438`. The chance of a repair running past five days is about 54 percent, so the shop should not plan around the five-day mark.

## Use Cases

### Service Level Reporting

**Scenario:** A support manager wants the share of tickets resolved within an agreed window, based on a fitted gamma model.

```excel
=GAMMADIST(Hours, Shape, Scale, TRUE)
```

**Why It Works:** Each ticket's hours feed the same parameters, so the formula returns a probability per ticket. Use GAMMA.DIST in new reports.

### Component Lifetime Planning

**Scenario:** An engineer estimates the chance that a part fails before a planned inspection.

```excel
=GAMMADIST(InspectionHours, Alpha, Beta, TRUE)
```

**Why It Works:** The cumulative setting gives the failure probability by the inspection date. Check that the parameters came from a fit to real data.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `x` is negative, or `alpha` or `beta` is 0 or less. | Validate inputs before calling the function. |
| `#VALUE!` | One of the arguments is text or an empty reference. | Convert the input to a number. |
| Probability above 1 | Cumulative set to FALSE, which returns a density. | Set `cumulative` to TRUE for a probability. |
| Unexpected shape | `beta` was entered as a rate. | Enter the scale, which is 1 divided by the rate. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions, marked as a compatibility function | Replaced by GAMMA.DIST. Microsoft notes it may be removed in future versions. |
| Google Sheets | Documented as synonymous with GAMMA.DIST | The same four arguments apply. Use GAMMA.DIST in new sheets. |

## Tips and Best Practices

- Use TRUE for `cumulative` when you need a probability, and FALSE only when you need the curve height.
- Keep `alpha` and `beta` in labeled cells so the parameters are easy to update.
- Use GAMMA.DIST in new work because Microsoft has replaced this function.
- Use `1 - GAMMADIST(...)` to find the chance of exceeding a value.

## Related Functions

| Function | Relationship |
| --- | --- |
| [GAMMA.DIST](GAMMA.DIST.md) | The current replacement with the same arguments. |
| [GAMMA.INV](GAMMA.INV.md) | Returns the x value for a given cumulative probability. |
| [GAMMAINV](GAMMAINV.md) | The compatibility version of GAMMA.INV. |
| [GAMMALN](GAMMALN.md) | Natural log of the gamma function, used in gamma calculations. |
| [NORM.S.DIST](NORM.S.DIST.md) | Standard normal distribution, useful for comparison with another bell-shaped model. |
| [BETA.DIST](BETA.DIST.md) | Another continuous distribution for values bounded between 0 and 1. |

## Official Documentation

- [Microsoft Support: GAMMADIST function](https://support.microsoft.com/en-us/excel/functions/gammadist-function)
- [Google Docs Editors Help: GAMMADIST](https://support.google.com/docs/answer/7013989)
