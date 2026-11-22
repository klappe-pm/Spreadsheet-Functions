---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
use-case:
  - Demand Band Forecasting
  - Shipping Delay Risk
related:
  - BINOM.DIST
  - FREQUENCY
  - NORM.DIST
  - POISSON.DIST
  - RANDBETWEEN
  - SUMPRODUCT
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/prob-function
  - https://support.google.com/docs/answer/3094039
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Probability Between Limits
tags:
  - distribution
  - excel
  - probability
  - sheets
---

# PROB

## Description

**PROB** returns the probability that a randomly chosen value falls between two limits, when you already know the probability of each value. The values and their probabilities are supplied as two ranges of the same length, so PROB works for a discrete probability table such as a list of possible delivery delays or sales volumes.

If you give only the lower limit, PROB returns the probability that the value equals that limit exactly. If you give both limits, it adds the probabilities of every value from the lower limit up to the upper limit, inclusive.

The probabilities should add up to 1. Excel returns an error when they do not, and the Google Sheets documentation does not describe this check, so run a SUM over the probability range before you rely on the result. Microsoft Excel calls the arguments `x_range`, `prob_range`, `lower_limit` and `upper_limit`. Google Sheets calls them `data`, `probabilities`, `low_limit` and `high_limit`.

## Syntax

```excel
=PROB(x_range, prob_range, [lower_limit], [upper_limit])
```

<!-- Image 1: PROB Syntax Anatomy. See Images/Statistical/PROB.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x_range` | Yes | The numeric values that have associated probabilities, such as `A2:A5`. |
| `prob_range` | Yes | The probability for each value in `x_range`, in the same order and the same count. Each value is above 0 and at most 1. |
| `lower_limit` | No | The lowest value to include. When `upper_limit` is omitted, the function returns the probability of exactly this value. |
| `upper_limit` | No | The highest value to include. Values equal to this limit are counted. |

### Return Value

A probability from 0 to 1. Excel returns `#NUM!` when a probability is outside the allowed range or the probabilities do not sum to 1, and `#N/A` when `x_range` and `prob_range` have a different number of values.

## Examples

Examples use `A2:A5` for the values 1, 2, 3 and 4, and `B2:B5` for the probabilities 0.1, 0.2, 0.3 and 0.4.

### Example 1: Probability Between Two Limits

```excel
=PROB(A2:A5, B2:B5, 2, 3)
```

**Result:** `0.5`

The values 2 and 3 have probabilities 0.2 and 0.3, and 0.2 + 0.3 = 0.5.

### Example 2: Probability of One Exact Value

```excel
=PROB(A2:A5, B2:B5, 3)
```

**Result:** `0.3`

With no upper limit, PROB returns the probability of exactly 3.

### Example 3: Wider Range

```excel
=PROB(A2:A5, B2:B5, 2, 4)
```

**Result:** `0.9`

The values 2, 3 and 4 have probabilities 0.2, 0.3 and 0.4. The total is 0.9, so the value 1 is excluded.

<!-- Image 2: Limits Applied to a Probability Table. See Images/Statistical/PROB.md -->

### Example 4: Limit Outside the Values

```excel
=PROB(A2:A5, B2:B5, 5)
```

**Result:** `0`

No value in `A2:A5` equals 5, so the probability is zero.

## Story Problems

### Problem 1: Supplier Delivery Delays

A supplier reports how many days late a shipment arrives. The probabilities are in `B2:B5` for the delays in `A2:A5`.

| Days Late | Probability |
| --- | --- |
| 0 | 0.50 |
| 1 | 0.25 |
| 2 | 0.15 |
| 3 | 0.10 |

**Task:** Find the probability that a shipment is between 1 and 2 days late.

**Solution:**

```excel
=PROB(A2:A5, B2:B5, 1, 2)
```

**Answer:** `0.4`, because 0.25 + 0.15 = 0.4.

### Problem 2: Weekly Unit Demand

A shop forecasts weekly unit sales as 10, 20 or 30 units with probabilities 0.2, 0.5 and 0.3. The buyer wants the chance of selling at least 20 units.

| Units Sold | Probability |
| --- | --- |
| 10 | 0.20 |
| 20 | 0.50 |
| 30 | 0.30 |

**Task:** Find the probability of selling at least 20 units, using 30 as the upper limit.

**Solution:**

```excel
=PROB(A2:A4, B2:B4, 20, 30)
```

**Answer:** `0.8`, because 0.50 + 0.30 = 0.8. Only the 10-unit week falls outside the range.

## Use Cases

### Demand Band Forecasting

**Scenario:** A planner has a probability estimate for each sales volume and needs the chance that demand lands in a stocking band.

```excel
=PROB(VolumeRange, ProbRange, LowBand, HighBand)
```

**Why It Works:** The two named ranges hold the volumes and their probabilities. The band limits can come from input cells so the planner can change the band without editing the formula.

### Shipping Delay Risk

**Scenario:** An operations manager wants to know the chance that a delivery is late by a set number of days.

```excel
=PROB(DelayDays, DelayProbability, 2)
```

**Why It Works:** Omitting the upper limit returns the probability of exactly the given delay. Add an upper limit to measure a range of delays instead.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | `x_range` and `prob_range` have a different number of values. | Make both ranges the same length and in the same order. |
| `#NUM!` | A probability is zero, negative, above 1, or the total is not 1. | Check each probability and make the total 1. |
| `0` | The limits do not include any value in `x_range`. | Confirm the limits fall within the values. |
| Unexpected total | The probabilities are percentages, such as 25, instead of decimals. | Divide each percentage by 100. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Returns `#NUM!` and `#N/A` as documented in the Return Value section. |
| Google Sheets | Available | Upper limit defaults to the lower limit; probabilities must be above 0 and at most 1, and both ranges must have the same number of values. |

## Tips and Best Practices

- Check that `SUM(prob_range)` returns 1 before you trust a result.
- Keep the values and probabilities in adjacent columns so the ranges stay aligned.
- Use decimal probabilities. Percentages entered as whole numbers produce errors or wrong totals.
- Use PROB for discrete values. For continuous distributions, use a function such as NORM.DIST.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SUMPRODUCT](../Math%20%26%20Trig/SUMPRODUCT.md) | Expected value of a probability table: multiply each value by its probability and add. |
| [POISSON.DIST](POISSON.DIST.md) | Probabilities for counts of events in a fixed interval. |
| [BINOM.DIST](BINOM.DIST.md) | Probabilities for successes in a fixed number of trials. |
| [NORM.DIST](NORM.DIST.md) | Probabilities for continuous, bell-shaped distributions. |
| [FREQUENCY](FREQUENCY.md) | Counts how many values fall in each bin, which you can convert to probabilities. |
| [RANDBETWEEN](../Math%20%26%20Trig/RANDBETWEEN.md) | Generates random whole numbers for simulations. |

## Official Documentation

- [Microsoft Support: PROB function](https://support.microsoft.com/en-us/excel/functions/prob-function)
- [Google Docs Editors Help: PROB](https://support.google.com/docs/answer/3094039)
