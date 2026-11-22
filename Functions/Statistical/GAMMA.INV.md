---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Repair Time Targets
  - Service Level Time Targets
related:
  - CHISQ.INV
  - EXPON.DIST
  - GAMMA.DIST
  - GAMMAINV
  - NORM.INV
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/gamma-inv-function
  - https://support.google.com/docs/answer/9116467
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Inverse Gamma Distribution
tags:
  - distribution
  - excel
  - inverse-distribution
  - sheets
---

# GAMMA.INV

## Description

**GAMMA.INV** returns the value x for which the gamma distribution gives a given cumulative probability. It is the inverse of GAMMA.DIST: if p equals GAMMA.DIST(x, alpha, beta, TRUE), then GAMMA.INV(p, alpha, beta) returns x. Use it when you know the target probability and need the value that reaches it, such as the time by which 90 percent of jobs are complete.

The function works through an iterative search, so its precision depends on GAMMA.DIST. If the search does not converge within 64 iterations, Microsoft's page states that the function returns `#N/A`. The inputs must be valid: the probability must be between 0 and 1, and alpha and beta must be positive.

Microsoft lists the older name GAMMAINV as an alternative for this function. Microsoft's page does not name a replacement, so use GAMMA.INV in new work. Google Sheets supports GAMMA.INV under the same name.

## Syntax

```excel
=GAMMA.INV(probability, alpha, beta)
```

<!-- Image 1: Probability and Parameters. See Images/Statistical/GAMMA.INV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | The cumulative probability, which must be between 0 and 1. |
| `alpha` | Yes | The shape parameter. It must be greater than 0. |
| `beta` | Yes | The scale parameter. It must be greater than 0. With `beta` equal to 1, the result is the standard gamma distribution. |

### Return Value

A single number: the value of x at which the cumulative gamma distribution equals `probability`. The function returns `#VALUE!` when an argument is text, `#NUM!` when `probability` is outside 0 to 1 or when `alpha` or `beta` is zero or negative, and `#N/A` when the iterative search does not converge.

## Examples

### Example 1: Median of an Exponential Wait

```excel
=GAMMA.INV(0.5, 1, 5)
```

**Result:** `3.4657`

With alpha equal to 1, the distribution is exponential. Half the waits are shorter than about 3.47 time units when the scale is 5.

### Example 2: Long Life Target

```excel
=GAMMA.INV(0.9, 1, 500)
```

**Result:** `1151.29`

Ninety percent of the units in this model last no longer than about 1,151 hours. The exact value uses the natural logarithm of 0.1, multiplied by 500 and negated.

<!-- Image 2: Round Trip Diagram. See Images/Statistical/GAMMA.INV.md -->

### Example 3: Round Trip With GAMMA.DIST

```excel
=GAMMA.INV(GAMMA.DIST(6, 2, 3, TRUE), 2, 3)
```

**Result:** `6`

The inner GAMMA.DIST returns the probability at 6, and GAMMA.INV returns the value back. The result matches the original x, which is a useful check on both formulas.

### Example 4: Using a Named Target

```excel
=GAMMA.INV(Target_Probability, Shape, Scale)
```

**Result:** The value that reaches the target probability for the given shape and scale.

Store the probability and the two parameters in named cells so a planner can test different service levels without changing the formula.

## Story Problems

### Problem 1: Battery Life Guarantee

A manufacturer models battery life with an exponential pattern and an average life of 500 hours. The warranty team wants the life that 90 percent of batteries will not exceed.

**Task:** Return the 90th percentile of battery life.

**Solution:**

```excel
=GAMMA.INV(0.9, 1, 500)
```

**Answer:** `1151.29` hours. Ninety percent of batteries last no longer than about 1,151 hours in this model.

<!-- Image 3: Battery Life Target. See Images/Statistical/GAMMA.INV.md -->

### Problem 2: Median Call Answer Time

A call center models the time to answer a call with an exponential pattern and an average of 12 seconds. The manager wants the time by which half of calls are answered.

**Task:** Return the median answer time.

**Solution:**

```excel
=GAMMA.INV(0.5, 1, 12)
```

**Answer:** `8.3178` seconds. Half of calls are answered within about 8.32 seconds under this model.

## Use Cases

### Repair Time Targets

**Scenario:** A maintenance manager sets a time target that 95 percent of repairs should meet.

```excel
=GAMMA.INV(0.95, Repair_Shape, Repair_Scale)
```

**Why It Works:** The formula returns the time that 95 percent of past repair patterns fit within. Recalculate the shape and scale from recent jobs each quarter, so the target reflects current work.

### Service Level Time Targets

**Scenario:** A support lead reviews the response time that 90 percent of tickets should beat.

```excel
=GAMMA.INV(Service_Level, Shape_Hist, Scale_Hist)
```

**Why It Works:** Changing the service level in one cell shows how much time the team must add to reach a higher target, which makes the trade-off easy to discuss.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The probability is below 0 or above 1, or alpha or beta is zero or negative. | Check the probability and the parameters. |
| `#VALUE!` | An argument is text. | Enter numeric values. |
| `#N/A` | The iterative search did not converge within 64 iterations. | Check the parameters, and compare the result with GAMMA.DIST. |
| Wrong percentile | The probability was entered as a percentage, such as 90, instead of 0.9. | Enter the probability as a decimal between 0 and 1. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | GAMMAINV is the older name. Microsoft's page does not name a replacement. |
| Google Sheets | Available | The help page states that the probability must be between 0 and 1 and that alpha and beta must be positive. |

## Tips and Best Practices

- Enter the probability as a decimal, such as 0.9, not as 90.
- Check one value with GAMMA.DIST after you build the model to confirm the round trip.
- Store the shape and scale in labeled cells so reviewers can see where the targets come from.
- Recalculate the parameters from recent data, because a target built on old history drifts as the process changes.
- Use EXPON.DIST for the exponential case, when alpha equals 1, if that formula is easier for your readers.

## Related Functions

| Function | Relationship |
| --- | --- |
| [GAMMA.DIST](GAMMA.DIST.md) | The forward function: it returns the probability for a value. |
| [EXPON.DIST](EXPON.DIST.md) | Gives the exponential distribution that GAMMA.INV reduces to when alpha equals 1. |
| [CHISQ.INV](CHISQ.INV.md) | Returns the inverse of the chi-squared distribution, a gamma case with shape n divided by 2 and scale 2. |
| [GAMMAINV](GAMMAINV.md) | Older name for the same function, kept for compatibility. |
| [NORM.INV](NORM.INV.md) | Returns the inverse of the normal distribution for symmetric targets. |

## Official Documentation

- [Microsoft Support: GAMMA.INV function](https://support.microsoft.com/en-us/excel/functions/gamma-inv-function)
- [Google Docs Editors Help: GAMMA.INV](https://support.google.com/docs/answer/9116467)
