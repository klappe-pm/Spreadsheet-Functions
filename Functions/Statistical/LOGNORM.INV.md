---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
use-case:
  - Delivery Time Targets
  - Percentile Planning
  - Response Time Percentiles
related:
  - LOGINV
  - LOGNORM.DIST
  - LOGNORMDIST
  - NORM.INV
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/lognorm-inv-function
  - https://support.google.com/docs/answer/3094010
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Inverse Lognormal
  - Lognormal Percentile
tags:
  - distribution
  - excel
  - lognormal
  - percentile
  - sheets
---

# LOGNORM.INV

## Description

**LOGNORM.INV** returns the value of x whose cumulative lognormal probability equals the probability you supply. It is the inverse of LOGNORM.DIST: if p equals LOGNORM.DIST(x, mean, standard_dev, TRUE), then LOGNORM.INV(p, mean, standard_dev) returns x again.

Use LOGNORM.INV to set a target from a percentile. For example, it finds the delivery time that 90 percent of orders beat, or the order value below which the smallest tenth of orders fall. The mean and standard deviation describe the natural logarithm of the data, so take logs of the history before you estimate them.

LOGNORM.INV replaces LOGINV, which takes the same arguments. Use LOGNORM.INV in new work. For the forward calculation, from a value to a probability, use LOGNORM.DIST.

## Syntax

```excel
=LOGNORM.INV(probability, mean, standard_dev)
```

<!-- Image 1: Percentile Mapped Back to a Value. See Images/Statistical/LOGNORM.INV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | A probability greater than 0 and less than 1, such as 0.9 for the 90th percentile. Google Sheets names this argument `x`. |
| `mean` | Yes | The mean of the natural logarithm of x, not the mean of x. |
| `standard_dev` | Yes | The standard deviation of the natural logarithm of x. It must be greater than 0. |

All three arguments are required. Any non-numeric argument returns `#VALUE!`.

### Return Value

A positive number: the value of x at the given cumulative probability. It returns `#NUM!` when the probability is 0 or less or 1 or more, and when `standard_dev` is 0 or less.

## Examples

### Example 1: Finding a Lower Percentile

```excel
=LOGNORM.INV(0.05, 2, 0.5)
```

**Result:** `3.2465`

Five percent of values from this distribution fall at or below 3.2465.

### Example 2: The Median

```excel
=LOGNORM.INV(0.5, 2, 0.5)
```

**Result:** `7.3891`

At probability 0.5, the result is the median. For a lognormal distribution, the median equals e raised to the mean of ln(x), so e^2 = 7.3891.

### Example 3: Checking the Round Trip

```excel
=LOGNORM.DIST(LOGNORM.INV(0.05, 2, 0.5), 2, 0.5, TRUE)
```

**Result:** `0.05`

Converting a probability to a value and back returns the original probability, which confirms that the two functions are inverses.

### Example 4: Catching an Invalid Probability

```excel
=IFERROR(LOGNORM.INV(1, 2, 0.5), "Probability must be below 1")
```

**Result:** `Probability must be below 1`

A probability of 1 has no finite value, so LOGNORM.INV returns `#NUM!`. IFERROR shows a message instead.

## Story Problems

### Problem 1: Ninetieth Percentile Delivery Time

A courier models delivery time in minutes as lognormal. The parameters are in the table below.

| Parameter | Value |
| --- | --- |
| Probability | 0.9 |
| Mean of ln(minutes) | 2.8 |
| Standard deviation of ln(minutes) | 0.3 |

**Task:** Find the delivery time that 90 percent of orders beat, so the courier can publish a promise.

**Solution:**

```excel
=LOGNORM.INV(B2, B3, B4)
```

**Answer:** `24.15` minutes. Nine out of ten deliveries arrive within this time.

<!-- Image 2: Delivery Time Percentile Worksheet. See Images/Statistical/LOGNORM.INV.md -->

### Problem 2: Low Order Value Cutoff

An online shop models order values in dollars as lognormal. The parameters are below.

| Parameter | Value |
| --- | --- |
| Probability | 0.1 |
| Mean of ln(order value) | 4.2 |
| Standard deviation of ln(order value) | 0.5 |

**Task:** Find the order value below which the smallest tenth of orders fall, so the shop can review very small orders.

**Solution:**

```excel
=LOGNORM.INV(B2, B3, B4)
```

**Answer:** `35.14` dollars. About one order in ten is worth less than this amount.

## Use Cases

### Delivery Time Targets

**Scenario:** A fulfillment manager sets a delivery promise that the warehouse can meet for most orders.

```excel
=ROUND(LOGNORM.INV(0.9, Deliveries!B2, Deliveries!B3), 0)
```

**Why It Works:** The rounded value gives a whole-minute promise that matches the 90th percentile of past deliveries.

### Percentile Planning

**Scenario:** A planning team sizes a staffing buffer using the 95th percentile of daily call volume.

```excel
=LOGNORM.INV(0.95, Calls!E2, Calls!E3)
```

**Why It Works:** Planning to the 95th percentile covers almost all busy days without overstaffing for the most extreme ones.

### Response Time Percentiles

**Scenario:** A service team reports the time that 80 percent of tickets are answered within.

```excel
=LOGNORM.INV(0.8, Stats!B2, Stats!B3)
```

**Why It Works:** Reporting a percentile is clearer than reporting an average for skewed data, because a few very slow responses do not distort it.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The probability is 0 or less, or 1 or more. | Use a probability strictly between 0 and 1. |
| `#NUM!` | `standard_dev` is 0 or less. | Enter a positive standard deviation of ln(x). |
| `#VALUE!` | An argument is text or blank. | Convert the input to a number. |
| Unexpected value | The mean and standard deviation of x were used. | Compute them from the natural logarithms of the data. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available, including Excel for the web | Returns the inverse of LOGNORM.DIST with the same three arguments. |
| Google Sheets | Available | Listed with the syntax LOGNORM.INV(x, mean, standard_deviation). The first argument is named `x`, and the help page refers to LOGINV for details. |

## Tips and Best Practices

- Use the logarithms of the data to estimate the mean and standard deviation, not the raw values.
- Keep the percentile in a labeled cell so the target is easy to change.
- Use LOGNORM.INV rather than LOGINV for new formulas.
- Check the result against the history. If very few past values exceed it, the parameters may need review.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LOGNORM.DIST](LOGNORM.DIST.md) | Returns the probability for a value, the forward calculation. |
| [LOGINV](LOGINV.md) | The legacy inverse lognormal function with the same result. |
| [LOGNORMDIST](LOGNORMDIST.md) | The legacy cumulative lognormal function. |
| [NORM.INV](NORM.INV.md) | The inverse for normally distributed data that is not logged. |

## Official Documentation

- [Microsoft Support: LOGNORM.INV function](https://support.microsoft.com/en-us/excel/functions/lognorm-inv-function)
- [Google Docs Editors Help: LOGNORM.INV](https://support.google.com/docs/answer/3094010)
