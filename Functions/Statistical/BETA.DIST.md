---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Conversion Rate Estimates
  - Project Completion Shares
  - Satisfaction Score Ranges
related:
  - BETA.INV
  - BETADIST
  - BINOM.DIST
  - GAMMA.DIST
  - NORM.DIST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/beta-dist-function
  - https://support.google.com/docs/answer/9084228
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Beta Cumulative Distribution
  - Beta Density
tags:
  - distributions
  - excel
  - probability
  - sheets
  - statistics
---

# BETA.DIST

## Description

**BETA.DIST** returns values from the beta distribution, a flexible probability model for quantities that fall between two bounds. The two shape parameters, `alpha` and `beta`, control where the probability is concentrated. By default the bounds are 0 and 1, so the function suits proportions such as conversion rates, completion shares and yields. Optional `A` and `B` arguments rescale the model to any interval, such as scores from 1 to 5.

Set `cumulative` to TRUE to get the probability that the value is at or below `x`. Set it to FALSE to get the density, which is the height of the distribution curve at `x`. The density is not a probability by itself, but it shows where values are most likely.

BETA.DIST replaces the older BETADIST function, which is still available for compatibility. Use BETA.DIST in new work, because it supports the density option that BETADIST does not. In Excel, BETA.DIST is available in Excel 2016, Excel 2019, Excel 2021, Excel 2024 and Microsoft 365. Google Sheets accepts five arguments and has no cumulative argument, so the Sheets version does not offer the density option. Check the arguments in each platform before sharing a formula.

## Syntax

```excel
=BETA.DIST(x, alpha, beta, cumulative, [A], [B])
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/BETA.DIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The value at which to evaluate the function. It must fall between `A` and `B`. |
| `alpha` | Yes | The first shape parameter. It must be greater than 0. |
| `beta` | Yes | The second shape parameter. It must be greater than 0. |
| `cumulative` | Yes | TRUE returns the cumulative probability (at or below `x`). FALSE returns the probability density at `x`. |
| `A` | No | The lower bound of the interval for `x`. Defaults to 0. |
| `B` | No | The upper bound of the interval for `x`. Defaults to 1. |

### Return Value

A number. With `cumulative` set to TRUE, the result is a probability between 0 and 1. With FALSE, the result is the density, which can be greater than 1. The function returns `#VALUE!` when any argument is not numeric. It returns `#NUM!` when `alpha` or `beta` is 0 or less, when `x` is outside `A` and `B`, or when `A` equals `B`.

## Examples

### Example 1: Cumulative Probability on the Default Interval

```excel
=BETA.DIST(0.5, 2, 3, TRUE)
```

**Result:** `0.6875`

With alpha 2 and beta 3, the chance that the value is at or below 0.5 is 68.75 percent. This is the sum of the binomial terms for 2, 3 and 4 successes out of 4, which is 11 of 16.

### Example 2: Density at a Point

```excel
=BETA.DIST(0.5, 2, 3, FALSE)
```

**Result:** `1.5`

The density at 0.5 is 1.5. It is a height on the curve, not a probability. Densities only become probabilities after they are integrated over an interval.

### Example 3: Rescaled to a Custom Interval

```excel
=BETA.DIST(3, 2, 3, TRUE, 1, 5)
```

**Result:** `0.6875`

The interval from 1 to 5 is rescaled to 0 to 1, so 3 becomes 0.5. That is the same point as Example 1, which is why the result matches.

<!-- Image 2: Default and Custom Bounds. See Images/Statistical/BETA.DIST.md -->

### Example 4: Probability Below a Small Threshold

```excel
=BETA.DIST(0.2, 2, 5, TRUE)
```

**Result:** `0.3446`

With alpha 2 and beta 5, about 34.5 percent of the probability lies at or below 0.2.

### Example 5: A Value Outside the Bounds

```excel
=BETA.DIST(6, 2, 3, TRUE, 1, 5)
```

**Result:** `#NUM!`

The value 6 is greater than the upper bound of 5, so the function has no answer. Check that the input falls inside the interval before calling the function.

## Story Problems

### Problem 1: Conversion Rate Estimate

A marketing team models the conversion rate of a new landing page with alpha 2 and beta 5. The values are stored in `A1:B4`.

| Input | Value |
| --- | --- |
| Alpha | 2 |
| Beta | 5 |
| Threshold rate | 0.2 |

**Task:** Find the probability that the true conversion rate is at or below 20 percent.

**Solution:**

```excel
=BETA.DIST(B4, B2, B3, TRUE)
```

**Answer:** `0.3446`, or about 34.5 percent. The model gives roughly a one-in-three chance that the rate is 20 percent or lower.

<!-- Image 3: Results Panel for the Conversion Problem. See Images/Statistical/BETA.DIST.md -->

### Problem 2: Satisfaction Scores on a 1 to 5 Scale

A survey model places satisfaction on a scale from 1 to 5 with alpha 2 and beta 3. The lower bound is 1 and the upper bound is 5.

**Task:** Find the probability that a customer's score is at or below 4.

**Solution:**

```excel
=BETA.DIST(4, 2, 3, TRUE, 1, 5)
```

**Answer:** `0.9492`. The score 4 maps to 0.75 on the 0 to 1 scale, and the cumulative probability at 0.75 is 94.92 percent.

## Use Cases

### Conversion Rate Estimates

**Scenario:** A growth team wants the chance that a test variant converts below a target rate, based on a prior that has been updated with past results.

```excel
=BETA.DIST(TargetRate, Alpha, Beta, TRUE)
```

**Why It Works:** The cumulative option gives a direct probability for the target. Keep the shape parameters in labeled cells so the analysis can be rerun as new results arrive.

### Project Completion Shares

**Scenario:** A project planner models the share of work finished by a date, bounded between 0 and 100 percent.

```excel
=BETA.DIST(Share, 3, 2, TRUE, 0, 100)
```

**Why It Works:** Setting `A` to 0 and `B` to 100 lets the model use percentages directly, without dividing by 100 first.

### Satisfaction Score Ranges

**Scenario:** A research team compares the share of responses at or below a rating on a 1 to 5 scale.

```excel
=BETA.DIST(Rating, 2, 3, TRUE, 1, 5)
```

**Why It Works:** The lower and upper bounds map the scale onto the model, so each rating gets the correct cumulative probability.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `x` is outside the interval from `A` to `B`, or `A` equals `B`. | Confirm the input range and bounds. |
| `#NUM!` | `alpha` or `beta` is 0 or less. | Use positive shape parameters. |
| `#VALUE!` | An argument is text or blank. | Convert the value to a number or reference a numeric cell. |
| Unexpected result | `cumulative` is set to FALSE when a probability was wanted. | Use TRUE for a probability, FALSE for a density. |
| Unexpected result | Percentages are passed as whole numbers with the default bounds. | Set `B` to 100 or divide by 100 first. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, Excel 2019, Excel 2021, Excel 2024 and Microsoft 365, Windows, Mac and web | Six arguments, including the `cumulative` option and optional bounds. |
| Google Sheets | Available | Five arguments: `value`, `alpha`, `beta`, `lower_bound` and `upper_bound`. No cumulative argument. |

## Tips and Best Practices

- Use the default bounds for proportions, and set `A` and `B` for any other scale.
- Store alpha and beta in labeled cells so they can be changed without editing formulas.
- Check the density option with a simple case before using it in a chart.
- Use BETA.INV to go the other way, from a probability to a value.
- Document the source of the shape parameters, because the answer depends on them directly.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BETA.INV](BETA.INV.md) | Returns the value for a given cumulative probability, the inverse of this function. |
| [BETADIST](BETADIST.md) | Earlier version that returns only the cumulative probability. |
| [BINOM.DIST](BINOM.DIST.md) | Models counts of successes rather than a continuous proportion. |
| [GAMMA.DIST](GAMMA.DIST.md) | Another continuous distribution for positive values. |
| [NORM.DIST](NORM.DIST.md) | Normal distribution for values that cluster around a mean. |

## Official Documentation

- [Microsoft Support: BETA.DIST function](https://support.microsoft.com/en-us/excel/functions/beta-dist-function)
- [Google Docs Editors Help: BETA.DIST](https://support.google.com/docs/answer/9084228)
