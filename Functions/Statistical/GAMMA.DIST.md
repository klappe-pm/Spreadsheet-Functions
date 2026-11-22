---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Rainfall Amount Distribution
  - Waiting Time Probability
related:
  - CHISQ.DIST
  - EXPON.DIST
  - GAMMA
  - GAMMA.INV
  - GAMMADIST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/gamma-dist-function
  - https://support.google.com/docs/answer/7013990
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Gamma Probability
tags:
  - distribution
  - excel
  - probability
  - sheets
---

# GAMMA.DIST

## Description

**GAMMA.DIST** returns the gamma distribution for a value x. The gamma distribution models positive, skewed quantities that add up over time or over events, such as the time until several arrivals, total rainfall over a period, or the size of insurance claims. It has two shape and scale parameters, alpha and beta.

Set the last argument to TRUE for the cumulative distribution, which gives the probability that a value is at or below x. Set it to FALSE for the probability density, which shows how likely values near x are. Use the cumulative form to answer questions such as "what is the chance the total takes less than this long?"

When alpha equals 1, the gamma distribution becomes the exponential distribution, with a rate of 1 divided by beta. When alpha is a positive whole number, the distribution is also called the Erlang distribution. GAMMA.DIST is the current name for the older GAMMADIST function, which Google's page lists as a synonym. Use GAMMA.DIST in new work.

## Syntax

```excel
=GAMMA.DIST(x, alpha, beta, cumulative)
```

<!-- Image 1: Distribution Arguments. See Images/Statistical/GAMMA.DIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The value at which to evaluate the distribution. It must be at least 0. |
| `alpha` | Yes | The shape parameter. It must be greater than 0. |
| `beta` | Yes | The scale parameter. It must be greater than 0. With `beta` equal to 1, the result is the standard gamma distribution. |
| `cumulative` | Yes | `TRUE` returns the cumulative distribution, the probability at or below `x`. `FALSE` returns the probability density at `x`. |

### Return Value

A probability when `cumulative` is `TRUE`, or a density when it is `FALSE`. The function returns `#VALUE!` when an argument is not numeric, and `#NUM!` when `x` is negative or when `alpha` or `beta` is zero or negative.

## Examples

### Example 1: Cumulative Probability

```excel
=GAMMA.DIST(6, 2, 3, TRUE)
```

**Result:** `0.5940`

The probability that the value is at or below 6 is about 59 percent for this gamma distribution with shape 2 and scale 3.

### Example 2: Density at a Point

```excel
=GAMMA.DIST(6, 2, 3, FALSE)
```

**Result:** `0.0902`

The density shows how likely values near 6 are. A density is not a probability, so it is not read as a percentage.

<!-- Image 2: Cumulative Versus Density Curves. See Images/Statistical/GAMMA.DIST.md -->

### Example 3: Exponential Case

```excel
=GAMMA.DIST(5, 1, 5, TRUE)
```

**Result:** `0.6321`

With alpha equal to 1, the gamma distribution is exponential. The result equals 1 minus e to the power of negative 1, which is about 0.6321.

### Example 4: Erlang Waiting Time

```excel
=GAMMA.DIST(4, 3, 2, TRUE)
```

**Result:** `0.3233`

This is the probability that the third event in a process with mean gap 2 happens by time 4. The shape of 3 counts the events.

## Story Problems

### Problem 1: Third Customer Arrival

A coffee shop has an average of 2 minutes between customers. The owner wants the chance that the third customer arrives within 4 minutes of opening.

**Task:** Return the probability that the third arrival happens at or before minute 4.

**Solution:**

```excel
=GAMMA.DIST(4, 3, 2, TRUE)
```

**Answer:** `0.3233`, which means about a 32 percent chance that the third customer arrives by minute 4.

<!-- Image 3: Waiting Time Chart. See Images/Statistical/GAMMA.DIST.md -->

### Problem 2: Battery Life Without Wear

A battery's time to failure follows an exponential pattern with an average life of 500 hours. The engineer wants the chance that a battery lasts at most 300 hours.

**Task:** Return the probability that the time to failure is 300 hours or less.

**Solution:**

```excel
=GAMMA.DIST(300, 1, 500, TRUE)
```

**Answer:** `0.4512`, which means about a 45 percent chance of failure by 300 hours.

## Use Cases

### Rainfall Amount Distribution

**Scenario:** A water manager estimates the chance that a monsoon season's rainfall stays below a reservoir threshold.

```excel
=GAMMA.DIST(Rainfall_mm, Shape_Est, Scale_Est, TRUE)
```

**Why It Works:** The gamma distribution fits positive, skewed totals. The shape and scale come from historical data, so refresh them each season before using the probability.

### Waiting Time Probability

**Scenario:** A service desk estimates the chance that the third ticket of the hour is resolved within a target time.

```excel
=GAMMA.DIST(Target_Minutes, 3, Mean_Gap, TRUE)
```

**Why It Works:** A shape of 3 counts events, and the scale is the average time per event. The result gives the chance the target is met, which is easier to explain than an average.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `x` is negative, or `alpha` or `beta` is zero or negative. | Check the sign of each input. |
| `#VALUE!` | An argument is text or a blank that cannot be read as a number. | Enter numeric values in each argument. |
| Density read as a probability | `cumulative` was set to `FALSE`. | Set it to `TRUE` for a probability. |
| Confusing the scale | `beta` is treated as a rate instead of a scale. | Enter the average time per event for `beta`, or use 1 divided by the rate. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | GAMMADIST is the older name. Microsoft's page has no replacement note for GAMMA.DIST. |
| Google Sheets | Available | The help page states that x, alpha and beta must be numeric and that alpha and beta must be greater than zero. |

## Tips and Best Practices

- Use TRUE for probability questions and FALSE only when you need the density for a plot.
- Keep alpha and beta in labeled cells so a reviewer can check the source of each parameter.
- Use GAMMA.INV to convert a probability back into a value.
- For a shape of n divided by 2 and a scale of 2, the result matches CHISQ.DIST with n degrees of freedom, which is a useful check.
- Plot the density across a range of x values to see the shape before you use the probability.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHISQ.DIST](CHISQ.DIST.md) | Matches GAMMA.DIST for shape n divided by 2 and scale 2. |
| [EXPON.DIST](EXPON.DIST.md) | Matches GAMMA.DIST when alpha equals 1. |
| [GAMMA](GAMMA.md) | Returns the gamma function used in the distribution's constant. |
| [GAMMA.INV](GAMMA.INV.md) | Returns the value for a given cumulative probability. |
| [GAMMADIST](GAMMADIST.md) | Older name for the same distribution, kept for compatibility. |

## Official Documentation

- [Microsoft Support: GAMMA.DIST function](https://support.microsoft.com/en-us/excel/functions/gamma-dist-function)
- [Google Docs Editors Help: GAMMA.DIST](https://support.google.com/docs/answer/7013990)
