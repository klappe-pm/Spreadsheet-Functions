---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Call Arrival Timing
  - Equipment Failure Timing
  - Service Wait Forecasts
related:
  - EXPONDIST
  - GAMMA.DIST
  - NORM.DIST
  - POISSON.DIST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/expon-dist-function
  - https://support.google.com/docs/answer/3093995
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Exponential Distribution
  - Exponential Probability
tags:
  - distribution
  - excel
  - probability
  - sheets
---

# EXPON.DIST

## Description

**EXPON.DIST** returns the exponential distribution, which models the time between events that happen at a steady average rate. Typical examples are the gap between customer calls, the time until a machine fails, and the wait between arrivals at a counter. The distribution is defined by a single parameter, lambda, which is the rate of events per unit of time.

The function has two modes, set by the last argument. With `TRUE`, it returns the cumulative probability that the value is less than or equal to `x`. With `FALSE`, it returns the probability density at `x`, which is not a probability and can be greater than 1. Most business questions need the cumulative form.

Lambda is a rate, not an average. When you know the average time between events, the rate is 1 divided by that average. For example, a call every 4 minutes on average has a lambda of 0.25 per minute. The older EXPONDIST function is kept for compatibility, and Microsoft's EXPONDIST page names EXPON.DIST as its replacement.

## Syntax

```excel
=EXPON.DIST(x, lambda, cumulative)
```

<!-- Image 1: EXPON.DIST Syntax Anatomy. See Images/Statistical/EXPON.DIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The value at which to evaluate the distribution. It must be 0 or greater. |
| `lambda` | Yes | The rate parameter: the number of events per unit of time. It must be greater than 0. |
| `cumulative` | Yes | `TRUE` returns the cumulative distribution, the probability of a value up to `x`. `FALSE` returns the probability density at `x`. |

### Return Value

A number. With `TRUE`, the result is a probability from 0 to 1. With `FALSE`, the result is the density at `x`, which can be larger than 1. It returns `#VALUE!` when `x` or `lambda` is not numeric and `#NUM!` when `x` is below 0 or `lambda` is 0 or less.

## Examples

### Example 1: Cumulative Probability

```excel
=EXPON.DIST(2, 0.25, TRUE)
```

**Result:** `0.3935`

With one event every four minutes, the chance that the next event happens within two minutes is about 39 percent.

### Example 2: Probability Density

```excel
=EXPON.DIST(2, 0.25, FALSE)
```

**Result:** `0.1516`

The density at 2 minutes shows how quickly the probability is building at that point. It is not the chance of the event happening at exactly 2 minutes.

### Example 3: Values From Cells

Cell `A2` holds `3`, cell `A3` holds `0.5` and cell `A4` holds `TRUE`.

```excel
=EXPON.DIST(A2, A3, A4)
```

**Result:** `0.7769`

Change the three cells to test other times, rates or result types without rewriting the formula.

### Example 4: Probability Between Two Times

```excel
=EXPON.DIST(4, 0.25, TRUE) - EXPON.DIST(2, 0.25, TRUE)
```

**Result:** `0.2387`

Subtracting the cumulative probability at 2 minutes from the cumulative probability at 4 minutes gives the chance that the event falls between those two times.

<!-- Image 2: Cumulative Probability Between Two Times. See Images/Statistical/EXPON.DIST.md -->

### Example 5: Negative Time Is Not Allowed

```excel
=EXPON.DIST(-1, 0.25, TRUE)
```

**Result:** `#NUM!`

Time cannot be negative in this model, so the function returns an error for any `x` below 0.

## Story Problems

### Problem 1: Customer Calls Within Three Minutes

A support line receives calls at an average rate of one every four minutes. The team wants the chance that the next call arrives within three minutes, so it can schedule staff for quick answers.

| Input | Value |
| --- | --- |
| Average time between calls | 4 minutes |
| Rate, lambda (1 divided by 4) | 0.25 per minute |
| Time window | 3 minutes |

**Task:** Find the probability that the next call arrives within 3 minutes.

**Solution:**

```excel
=EXPON.DIST(3, 0.25, TRUE)
```

**Answer:** `0.5276`. The chance is a little over half. The result is the cumulative probability at 3 minutes, which is 1 minus e to the power of negative 0.75.

<!-- Image 3: Call Arrival Result. See Images/Statistical/EXPON.DIST.md -->

### Problem 2: Components Still Working After 1,000 Hours

A manufacturer reports an average component life of 500 hours. The engineering team wants the chance that a component is still working after 1,000 hours.

| Input | Value |
| --- | --- |
| Average life | 500 hours |
| Rate, lambda (1 divided by 500) | 0.002 per hour |
| Hours of operation | 1,000 |

**Task:** Find the probability that a component is still working after 1,000 hours.

**Solution:**

```excel
=1 - EXPON.DIST(1000, 0.002, TRUE)
```

**Answer:** `0.1353`. The chance of surviving past 1,000 hours is the complement of the cumulative probability, which is e to the power of negative 2. About 13.5 percent of components last that long.

## Use Cases

### Call Arrival Timing

**Scenario:** A call center manager wants the chance that a new call arrives within a set window, using the average gap between calls logged in cell `H1`.

```excel
=EXPON.DIST(H2, 1/H1, TRUE)
```

**Why It Works:** The formula converts the average gap to a rate with `1/H1`, which is the form lambda needs. Changing the window in `H2` updates the probability.

### Equipment Failure Timing

**Scenario:** A maintenance planner wants the chance that a pump runs longer than a planned service interval.

```excel
=1 - EXPON.DIST(Service_Hours, 1/Mean_Hours_To_Failure, TRUE)
```

**Why It Works:** Subtracting the cumulative probability from 1 gives the chance of surviving past the interval. The named ranges make the assumptions visible to anyone who reviews the plan.

### Service Wait Forecasts

**Scenario:** A help desk expects customers to arrive at a steady rate and wants the chance that the next customer waits no longer than five minutes.

```excel
=EXPON.DIST(5, Arrival_Rate_Per_Minute, TRUE)
```

**Why It Works:** The rate is entered per minute, so the window is also in minutes. Mixing units, such as a rate per hour and a window in minutes, is a frequent cause of a wrong answer.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `x` is negative, or `lambda` is 0 or less. | Use a time of 0 or more and a rate above 0. |
| `#VALUE!` | `x` or `lambda` is text or a blank cell. | Enter numbers, not text. |
| Probability is too small | The average time was entered as the lambda. | Use the rate, which is 1 divided by the average time. |
| Result greater than 1 | `cumulative` is `FALSE`, which returns a density. | Use `TRUE` for a probability. |
| Mismatched results | The rate and the time are in different units. | Convert both to the same unit, such as minutes. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | EXPONDIST is the older name of the same function, kept for compatibility. |
| Google Sheets | Available | Accepts EXPON.DIST, and the help page says EXPONDIST can also be used. |

## Tips and Best Practices

- Convert an average time to a rate with `1/average` before you use it as lambda.
- Use `TRUE` for probabilities, and reserve `FALSE` for density values in a formula that needs them.
- Keep the rate and the time window in the same unit.
- Subtract two cumulative results to get the probability for a window, rather than using a density.
- Test a case you can check by hand, such as x of 0, which returns 0 for the cumulative form.

## Related Functions

| Function | Relationship |
| --- | --- |
| [EXPONDIST](EXPONDIST.md) | The older name of the same function. |
| [GAMMA.DIST](GAMMA.DIST.md) | Models the total time until several events happen. |
| [NORM.DIST](NORM.DIST.md) | Models symmetric data around a mean rather than waiting times. |
| [POISSON.DIST](POISSON.DIST.md) | Models how many events happen in a fixed period, which pairs with exponential waiting times. |

## Official Documentation

- [Microsoft Support: EXPON.DIST function](https://support.microsoft.com/en-us/excel/functions/expon-dist-function)
- [Google Docs Editors Help: EXPON.DIST](https://support.google.com/docs/answer/3093995)
