---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Exam Cut Scores
  - Invoice Size Review
  - Shipping Time Quartiles
related:
  - NORM.INV
  - NORM.S.INV
  - NORMDIST
  - NORMSINV
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/norminv-function
  - https://support.google.com/docs/answer/3094022
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Legacy Inverse Normal
tags:
  - compatibility
  - distribution
  - excel
  - inverse
  - probability
  - sheets
---

# NORMINV

## Description

**NORMINV** returns the value that has a given cumulative probability in a normal distribution with a stated mean and standard deviation. It reverses NORMDIST: you supply a probability and the function returns the value at which that probability is reached. Use it to set cutoffs, targets and quartiles on data that follows a normal curve.

Microsoft has replaced NORMINV with NORM.INV, which returns the same results. Microsoft describes NORMINV as kept only for backward compatibility and recommends NORM.INV for new work.

The probability must be greater than 0 and less than 1. A value of 0 or 1 returns `#NUM!`, because the normal distribution has no finite value at those probabilities.

<!-- Image 1: Inverse Lookup on the Normal Curve. See Images/Statistical/NORMINV.md -->

## Syntax

```excel
=NORMINV(probability, mean, standard_dev)
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | The cumulative probability, greater than 0 and less than 1. |
| `mean` | Yes | The arithmetic mean of the distribution. |
| `standard_dev` | Yes | The standard deviation of the distribution. A value of zero or less returns `#NUM!`. |

### Return Value

A number on the scale of the data, the value whose cumulative probability equals the input. The function returns `#VALUE!` when an argument is not a number, `#NUM!` when the probability is outside the allowed range or `standard_dev` is zero or less, and `#N/A` when the internal search does not converge after 100 iterations.

## Examples

The examples use a mean of 65 in `B2` and a standard deviation of 10 in `B3`, which describe exam scores.

### Example 1: Score Covering Eighty Percent

```excel
=NORMINV(0.8, 65, 10)
```

**Result:** `73.416`

Eighty percent of scores fall at or below 73.416 in this distribution.

### Example 2: Median Score

```excel
=NORMINV(0.5, 65, 10)
```

**Result:** `65`

The median of a normal distribution equals its mean.

### Example 3: Low Score Cutoff

```excel
=NORMINV(0.1, 65, 10)
```

**Result:** `52.184`

Only 10 percent of scores fall below this cutoff.

### Example 4: Rounded Pass Mark

```excel
=ROUND(NORMINV(0.95, 65, 10), 0)
```

**Result:** `81`

The 95th percentile is 81.449, and ROUND turns it into a whole-number pass mark.

### Example 5: Interquartile Range

```excel
=NORMINV(0.75, 65, 10) - NORMINV(0.25, 65, 10)
```

**Result:** `13.490`

The middle half of scores spans about 13.5 points. The difference between the upper and lower quartiles gives this width.

<!-- Image 2: Quartile Cutoffs on the Normal Curve. See Images/Statistical/NORMINV.md -->

## Story Problems

### Problem 1: Invoice Size Review

An accounts team reviews the largest 3 percent of invoices. Invoice amounts have a mean of 900 and a standard deviation of 150. The team wants the amount above which invoices are flagged.

| Input | Value |
| --- | --- |
| Mean invoice amount | 900 |
| Standard deviation | 150 |
| Share of invoices below the flag level | 0.97 |

**Task:** Enter the inputs in `E2:E4`, then find the amount that marks the top 3 percent.

**Solution:**

```excel
=NORMINV(E4, E2, E3)
```

**Answer:** `1182.12`. Invoices above that amount are flagged for review.

### Problem 2: Lower Quartile of Delivery Times

A delivery service has a mean delivery time of 40 minutes with a standard deviation of 8 minutes. The operations lead wants the time that the fastest quarter of deliveries beat.

| Input | Value |
| --- | --- |
| Mean delivery time (minutes) | 40 |
| Standard deviation (minutes) | 8 |
| Cumulative share | 0.25 |

**Task:** Enter the inputs in `E2:E4`, then find the delivery time at the lower quartile.

**Solution:**

```excel
=NORMINV(E4, E2, E3)
```

**Answer:** `34.604` minutes. One delivery in four finishes at or below this time.

## Use Cases

### Exam Cut Scores

**Scenario:** A training program passes the top 20 percent of candidates on a practice exam with a mean of 65 and a standard deviation of 10.

```excel
=ROUND(NORMINV(0.8, $F$1, $F$2), 0)
```

**Why It Works:** The probability 0.8 marks the 80th percentile, so candidates at or above the result are in the top 20 percent. Rounding gives a whole-number cut score.

### Shipping Time Quartiles

**Scenario:** A logistics team defines its fastest quarter of shipments by the lower quartile of delivery times.

```excel
=NORMINV(0.25, B2, C2)
```

**Why It Works:** `B2` holds the mean shipping time and `C2` holds the standard deviation. The result is the boundary below which one shipment in four falls.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The probability is 0, 1 or outside the range, or `standard_dev` is zero or negative. | Enter a probability strictly between 0 and 1, and check the standard deviation. |
| `#VALUE!` | An argument holds text or another nonnumeric value. | Re-enter the value as a number. |
| `#N/A` | The internal search did not converge after 100 iterations. | Check the inputs for extreme values, or switch to NORM.INV. |
| Percentage input returns `#NUM!` | A value such as 80 was entered instead of 0.8. | Enter probabilities as decimals. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available, listed in the compatibility group | Three required arguments. Microsoft recommends NORM.INV. |
| Google Sheets | Available | The help page labels the first argument `x`, but it holds the probability, as in Excel. Sheets documents the same three arguments. |

## Tips and Best Practices

- Use NORM.INV in new workbooks, because it returns the same results and Microsoft recommends it.
- Enter probabilities as cumulative shares, so 0.8 means 80 percent of values fall at or below the result.
- Keep the mean and standard deviation in labeled cells so the cutoffs can be recalculated when the data changes.
- Use NORMSINV when the mean is 0 and the standard deviation is 1.

## Related Functions

| Function | Relationship |
| --- | --- |
| [NORM.INV](NORM.INV.md) | The current replacement with the same arguments. |
| [NORM.S.INV](NORM.S.INV.md) | The standard normal inverse, with one argument. |
| [NORMDIST](NORMDIST.md) | The forward calculation: value in, probability out. |
| [NORMSINV](NORMSINV.md) | The older standard normal inverse. |

## Official Documentation

- [Microsoft Support: NORMINV function](https://support.microsoft.com/en-us/excel/functions/norminv-function)
- [Google Docs Editors Help: NORMINV](https://support.google.com/docs/answer/3094022)
