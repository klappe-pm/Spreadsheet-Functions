---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Legacy Workbook Maintenance
  - Light Bulb Lifetime
  - Machine Failure Windows
related:
  - EXPON.DIST
  - GAMMA.DIST
  - NORM.DIST
  - POISSON.DIST
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/expondist-function
  - https://support.google.com/docs/answer/3093995
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Exponential Distribution Compatibility
  - Legacy Exponential Distribution
tags:
  - compatibility
  - distribution
  - excel
  - sheets
---

# EXPONDIST

## Description

**EXPONDIST** returns the exponential distribution. It does the same calculation as EXPON.DIST and takes the same three arguments in the same order. Microsoft lists it as a compatibility function, and its support page names EXPON.DIST as the replacement. EXPONDIST remains available for backward compatibility but may not be available in future versions.

The exponential distribution models the time between events that occur at a steady average rate, such as the time until a bulb burns out or the gap between arrivals at a counter. Lambda is the rate, the number of events per unit of time. When the average time is known, the rate is 1 divided by that average.

With `TRUE` as the last argument, the function returns the cumulative distribution, which is the probability that the event happens by time `x`. With `FALSE`, it returns the probability density. Microsoft gives the two forms as the following equations.

```text
Density:      f(x; lambda) = lambda * e^(-lambda * x)
Cumulative:   F(x; lambda) = 1 - e^(-lambda * x)
```

## Syntax

```excel
=EXPONDIST(x, lambda, cumulative)
```

<!-- Image 1: EXPONDIST Syntax Anatomy. See Images/Statistical/EXPONDIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The value at which to evaluate the function. It must be 0 or greater. |
| `lambda` | Yes | The rate parameter. It must be greater than 0. |
| `cumulative` | Yes | `TRUE` returns the cumulative distribution. `FALSE` returns the probability density. |

### Return Value

A number. With `TRUE`, the result is a probability from 0 to 1. With `FALSE`, the result is the density, which can be greater than 1. It returns `#VALUE!` when `x` or `lambda` is not numeric, and `#NUM!` when `x` is below 0 or `lambda` is 0 or less.

## Examples

### Example 1: Cumulative Probability for a Rate

Cell `A2` holds `2` and cell `A3` holds `0.25`.

```excel
=EXPONDIST(A2, A3, TRUE)
```

**Result:** `0.3935`

With an average of one event every four units of time, the chance of an event within two units is about 39 percent.

### Example 2: Probability Density

```excel
=EXPONDIST(2, 0.25, FALSE)
```

**Result:** `0.1516`

The density is a rate of change in probability, not a probability. Use it only when a formula needs the density itself.

### Example 3: Rate From an Average Lifetime

```excel
=EXPONDIST(500, 1/800, TRUE)
```

**Result:** `0.4647`

The average life is 800 hours, so the rate is 1 divided by 800. The result is the chance that the item fails within 500 hours.

<!-- Image 2: Rate From an Average Lifetime. See Images/Statistical/EXPONDIST.md -->

### Example 4: Zero Time

```excel
=EXPONDIST(0, 0.5, TRUE)
```

**Result:** `0`

No time has passed at `x` equal to 0, so the cumulative probability is 0.

### Example 5: Negative Time Is Not Allowed

```excel
=EXPONDIST(-1, 0.25, TRUE)
```

**Result:** `#NUM!`

A negative time is outside the domain of the function, so it returns an error.

## Story Problems

### Problem 1: Light Bulbs Failing Early

A lighting supplier reports an average bulb life of 800 hours. The warranty team wants the chance that a bulb fails within its first 500 hours.

| Input | Value |
| --- | --- |
| Average bulb life | 800 hours |
| Early failure window | 500 hours |

**Task:** Find the probability that a bulb fails within 500 hours.

**Solution:**

```excel
=EXPONDIST(500, 1/800, TRUE)
```

**Answer:** `0.4647`. Under this model, about 46 percent of bulbs fail within 500 hours.

<!-- Image 3: Light Bulb Result. See Images/Statistical/EXPONDIST.md -->

### Problem 2: Machine Failure Within Two Months

A machine has a mean time to failure of 40 days. The plant manager wants the chance that the machine fails within 60 days, so the spare parts order can be timed.

| Input | Value |
| --- | --- |
| Mean time to failure | 40 days |
| Window | 60 days |

**Task:** Find the probability that the machine fails within 60 days.

**Solution:**

```excel
=EXPONDIST(60, 1/40, TRUE)
```

**Answer:** `0.7769`. The chance is about 78 percent. The rate is 1 divided by 40, and the formula returns 1 minus e to the power of negative 1.5.

## Use Cases

### Legacy Workbook Maintenance

**Scenario:** An operations team inherited a reliability workbook that uses EXPONDIST in many cells, and it wants to update the formulas without changing the results.

```excel
=EXPON.DIST(A2, A3, TRUE)
```

**Why It Works:** EXPON.DIST takes the same three arguments in the same order, so each EXPONDIST formula can be replaced by changing only the function name. Check a few results before and after the change.

### Light Bulb Lifetime

**Scenario:** A procurement analyst compares bulb suppliers by the chance of failing within a warranty period stored in `H1`.

```excel
=EXPONDIST(H1, 1/H2, TRUE)
```

**Why It Works:** `H2` holds the average life, and `1/H2` converts it to the rate that lambda requires. Changing either cell updates the comparison.

### Machine Failure Windows

**Scenario:** A plant planner wants the chance that a machine fails inside each planned maintenance window.

```excel
=EXPONDIST(Window_Days, 1/Mean_Days_To_Failure, TRUE)
```

**Why It Works:** Named ranges make the assumptions readable. Keep the window and the mean in the same unit, or convert one of them first.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `x` is negative, or `lambda` is 0 or less. | Use a time of 0 or more and a rate above 0. |
| `#VALUE!` | `x` or `lambda` is text or a blank cell. | Enter numbers, not text. |
| Probability is far too small | The average life was entered in place of the rate. | Use `1/average` as the lambda argument. |
| Result above 1 | `cumulative` is `FALSE`, which returns a density. | Use `TRUE` for a probability. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Compatibility function | Replaced by EXPON.DIST. Kept for backward compatibility, and Microsoft notes it may not be available in future versions. |
| Google Sheets | Available | The help page says EXPONDIST and EXPON.DIST can both be used for this function. |

## Tips and Best Practices

- Use EXPON.DIST in new work, and keep EXPONDIST only where an existing file uses it.
- Convert an average to a rate with `1/average` before you use it as lambda.
- Use `TRUE` for probabilities, and check that a density result is intended before you use `FALSE`.
- Check a formula with x of 0, which should return 0 for the cumulative form.
- Keep the rate and the time in the same unit.

## Related Functions

| Function | Relationship |
| --- | --- |
| [EXPON.DIST](EXPON.DIST.md) | The current name for the same calculation. |
| [GAMMA.DIST](GAMMA.DIST.md) | Models the total time until several events happen. |
| [NORM.DIST](NORM.DIST.md) | Models symmetric data around a mean. |
| [POISSON.DIST](POISSON.DIST.md) | Models the number of events in a fixed period. |

## Official Documentation

- [Microsoft Support: EXPONDIST function](https://support.microsoft.com/en-us/excel/functions/expondist-function)
- [Google Docs Editors Help: EXPON.DIST and EXPONDIST](https://support.google.com/docs/answer/3093995)
