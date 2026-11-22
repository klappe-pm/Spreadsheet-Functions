---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Percentile Targets
  - Project Completion Estimates
  - Simulation Inputs
related:
  - BETA.DIST
  - BETADIST
  - BETAINV
  - NORM.S.INV
  - PERCENTILE.INC
level: 4
source:
  - https://support.google.com/docs/answer/9061377
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Beta Quantile
  - Inverse Beta
tags:
  - distributions
  - probability
  - sheets
  - statistics
---

# BETA.INV

## Description

**BETA.INV** is the inverse of the beta cumulative distribution. You give it a probability and the two shape parameters, and it returns the value at which the cumulative probability reaches that level. For example, it finds the median (probability 0.5) or the 90th percentile (probability 0.9) of a beta-distributed quantity.

Use BETA.INV when you know the probability and need the value. Use BETA.DIST when you know the value and need the probability. The two functions are matched: if BETA.DIST returns 0.6875 for a value of 0.5, then BETA.INV returns 0.5 for a probability of 0.6875. Shape parameters must be positive, and the probability must be between 0 and 1 inclusive.

The optional `A` and `B` arguments set the interval of the distribution. In Excel they default to 0 and 1. The Google Sheets help page lists default bounds that could not be confirmed, so pass the bounds explicitly in Sheets if the interval is not 0 to 1. That keeps the formula correct no matter which defaults a platform uses.

## Syntax

```excel
=BETA.INV(probability, alpha, beta, [A], [B])
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/BETA.INV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | The cumulative probability at which to evaluate the inverse. It must be between 0 and 1, inclusive. |
| `alpha` | Yes | The first shape parameter. It must be greater than 0. |
| `beta` | Yes | The second shape parameter. It must be greater than 0. |
| `A` | No | The lower bound of the interval for the result. Defaults to 0 in Excel. |
| `B` | No | The upper bound of the interval for the result. Defaults to 1 in Excel. |

### Return Value

A number: the value `x` for which the cumulative beta distribution equals `probability`. The result lies between `A` and `B`. The function returns `#VALUE!` when any argument is not numeric. It returns `#NUM!` when `alpha` or `beta` is 0 or less, or when `probability` is 0 or less, or greater than 1.

## Examples

### Example 1: Inverting a Known Probability

```excel
=BETA.INV(0.6875, 2, 3)
```

**Result:** `0.5`

Example 1 on the BETA.DIST page showed that a value of 0.5 gives a cumulative probability of 0.6875 for alpha 2 and beta 3. The inverse returns 0.5 when given that probability.

### Example 2: Median of a Symmetric Distribution

```excel
=BETA.INV(0.5, 2, 2)
```

**Result:** `0.5`

When alpha and beta are equal, the distribution is symmetric around 0.5, so the median is 0.5.

### Example 3: Result on a Custom Interval

```excel
=BETA.INV(0.6875, 2, 3, 1, 5)
```

**Result:** `3`

The inverse on the 0 to 1 scale is 0.5. Rescaled to the interval from 1 to 5, that point is 1 + 0.5 × 4, which is 3.

<!-- Image 2: Probability to Value Mapping. See Images/Statistical/BETA.INV.md -->

### Example 4: A High Percentile

```excel
=BETA.INV(0.9, 3, 3)
```

**Result:** `0.7534`

With alpha 3 and beta 3, nine out of ten outcomes fall at or below about 0.7534. The result is rounded to four decimals.

### Example 5: Probability Outside the Valid Range

```excel
=BETA.INV(1.2, 2, 3)
```

**Result:** `#NUM!`

A probability cannot exceed 1, so the function returns an error. Validate probabilities before passing them in, especially when they come from user input.

## Story Problems

### Problem 1: Median Completion Share

A project planner models the share of a workstream completed by the deadline as a beta distribution with alpha 2 and beta 2, scaled to percentages from 0 to 100. The inputs are in `A1:B4`.

| Input | Value |
| --- | --- |
| Probability | 0.5 |
| Alpha | 2 |
| Beta | 2 |

**Task:** Find the completion percentage that half of the projects reach or exceed, which is the median.

**Solution:**

```excel
=BETA.INV(B2, B3, B4, 0, 100)
```

**Answer:** `50`. The distribution is symmetric, so the median sits at the midpoint of 0 and 100 percent.

<!-- Image 3: Results Panel for the Completion Problem. See Images/Statistical/BETA.INV.md -->

### Problem 2: Lower Quartile of Delivery Times

A logistics model places delivery times between 10 and 20 minutes with alpha 2 and beta 2. The planner wants the time that only 25 percent of deliveries beat.

**Task:** Find the 25th percentile of delivery time.

**Solution:**

```excel
=BETA.INV(0.25, 2, 2, 10, 20)
```

**Answer:** `13.26` minutes, rounded to two decimals. One delivery in four is expected to finish faster than this time.

## Use Cases

### Percentile Targets

**Scenario:** A finance team sets a conservative target for the share of a budget that a program will use, based on a beta model of past spending.

```excel
=BETA.INV(0.1, Alpha, Beta)
```

**Why It Works:** The result is the value that only 10 percent of outcomes fall below, which gives a clear conservative threshold. Keep Alpha and Beta in labeled cells so the model can be refreshed.

### Project Completion Estimates

**Scenario:** A project manager reports the completion share that the team reaches in nine out of ten cases.

```excel
=BETA.INV(0.9, Alpha, Beta, 0, 100)
```

**Why It Works:** Passing the bounds explicitly keeps the answer on the percentage scale, and the report stays correct if the model is ever moved to a different platform.

### Simulation Inputs

**Scenario:** An analyst generates random values from a beta distribution by feeding uniform random numbers into the inverse function.

```excel
=BETA.INV(RAND(), 2, 5)
```

**Why It Works:** When the probability is a uniform random number, the result follows the beta distribution. Each recalculation produces a new sample, so use fixed values when results must be repeatable.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `probability` is less than 0 or greater than 1. | Limit the probability to the range 0 to 1. |
| `#NUM!` | `alpha` or `beta` is 0 or less. | Use positive shape parameters. |
| `#VALUE!` | An argument is text or blank. | Convert the input to a number or reference a numeric cell. |
| Unexpected result | The bounds are omitted, so the result stays between 0 and 1. | Pass `A` and `B` explicitly when the scale is different. |
| Unexpected result | Percentile is entered as 90 instead of 0.9. | Enter the probability as a decimal. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, Excel 2019, Excel 2021, Excel 2024 and Microsoft 365, Windows, Mac and web | Arguments are `probability, alpha, beta, A, B`, with `A` and `B` defaulting to 0 and 1. |
| Google Sheets | Available | Arguments are `probability, alpha, beta, lower_bound, upper_bound`. The help page lists default bounds that could not be confirmed, so pass the bounds explicitly. |

## Tips and Best Practices

- Pass the bounds explicitly in every formula, so the result does not depend on a default.
- Check the inverse with BETA.DIST: the cumulative probability at the result should match the input.
- Keep probabilities as decimals between 0 and 1, and validate them when they come from user input.
- Use the inverse to create percentile targets, then check them against the historical data.
- Use BETA.DIST for the forward calculation and BETA.INV for the reverse.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BETA.DIST](BETA.DIST.md) | Forward calculation: returns the probability for a value, the reverse of this function. |
| [BETADIST](BETADIST.md) | Compatibility version of the forward calculation. |
| [BETAINV](BETAINV.md) | Compatibility version of this function. |
| [NORM.S.INV](NORM.S.INV.md) | Inverse of the standard normal distribution, for comparison. |
| [PERCENTILE.INC](PERCENTILE.INC.md) | Percentile of a list of observed values rather than a model. |

## Official Documentation

- [Google Docs Editors Help: BETA.INV](https://support.google.com/docs/answer/9061377)
