---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Probability
use-case:
  - Legacy Workbook Maintenance
  - Response Time Targets
  - Service Level Planning
related:
  - LOGNORM.DIST
  - LOGNORM.INV
  - LOGNORMDIST
  - NORM.INV
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/loginv-function
  - https://support.google.com/docs/answer/3094010
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Inverse Lognormal Distribution
tags:
  - compatibility
  - excel
  - lognormal
  - probability
  - sheets
---

# LOGINV

## Description

**LOGINV** returns the value x at which a lognormal distribution reaches a given cumulative probability. The distribution describes a variable whose natural logarithm follows a normal bell curve. You supply the probability, the mean of ln(x) and the standard deviation of ln(x), and LOGINV returns the matching value of x.

LOGINV is a legacy function. Microsoft lists it under compatibility and warns that it may not be available in future versions of Excel. The modern replacement is LOGNORM.INV, which takes the same three arguments and returns the same result. For new work, use LOGNORM.INV. Keep LOGINV only in workbooks that already rely on it.

Use the function to find a threshold, such as the value that 95 percent of waiting times stay under. Pair it with LOGNORMDIST or LOGNORM.DIST when you need the probability for a given value, which is the reverse calculation.

## Syntax

```excel
=LOGINV(probability, mean, standard_dev)
```

<!-- Image 1: Probability Mapped to a Lognormal Value. See Images/Statistical/LOGINV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | A probability greater than 0 and less than 1, such as 0.95 for the 95th percentile. Google Sheets names this argument `x`. |
| `mean` | Yes | The mean of the natural logarithm of x, not the mean of x itself. |
| `standard_dev` | Yes | The standard deviation of the natural logarithm of x. It must be greater than 0. Google Sheets names this argument `standard_deviation`. |

All three arguments are required.

### Return Value

A number: the value of x at which the cumulative lognormal probability equals the probability supplied. The result is always positive. It returns `#VALUE!` when an argument is not a number, `#NUM!` when the probability is 0 or less or 1 or more, and `#NUM!` when `standard_dev` is 0 or less.

## Examples

### Example 1: Finding an Upper Percentile

```excel
=LOGINV(0.9, 2, 0.5)
```

**Result:** `14.0241`

Nine out of ten values from this distribution fall at or below 14.0241.

### Example 2: The Median

```excel
=LOGINV(0.5, 2, 0.5)
```

**Result:** `7.3891`

At probability 0.5, the result is the median, which equals e raised to the mean of ln(x), so e^2 = 7.3891.

### Example 3: The Modern Replacement

```excel
=LOGNORM.INV(0.9, 2, 0.5)
```

**Result:** `14.0241`

LOGNORM.INV returns the same value as LOGINV for the same arguments. Replace LOGINV with LOGNORM.INV when you rewrite a legacy sheet.

### Example 4: Catching an Invalid Probability

```excel
=IFERROR(LOGINV(1, 2, 0.5), "Probability must be below 1")
```

**Result:** `Probability must be below 1`

A probability of 1 has no finite value on the distribution, so LOGINV returns `#NUM!`. IFERROR displays a message instead.

## Story Problems

### Problem 1: Response Time Target

A help desk models the time to first response, in minutes, as lognormal. The parameters are in `B2:B4`.

| Parameter | Value |
| --- | --- |
| Probability | 0.95 |
| Mean of ln(minutes) | 3.4 |
| Standard deviation of ln(minutes) | 0.4 |

**Task:** Find the response time that 95 percent of requests beat, so the team can set a service target.

**Solution:**

```excel
=LOGINV(B2, B3, B4)
```

**Answer:** `57.86` minutes. Ninety-five percent of first responses arrive within this time, so 60 minutes is a realistic public target.

<!-- Image 2: Service Target on a Lognormal Curve. See Images/Statistical/LOGINV.md -->

### Problem 2: Household Spending Ceiling

A budget estimate describes monthly household spending, in dollars, with the parameters below.

| Parameter | Value |
| --- | --- |
| Probability | 0.8 |
| Mean of ln(spending) | 6.5 |
| Standard deviation of ln(spending) | 0.6 |

**Task:** Find the spending level that 80 percent of households stay below.

**Solution:**

```excel
=LOGINV(B2, B3, B4)
```

**Answer:** `1102.10` dollars. Four out of five households spend less than this amount in a typical month.

## Use Cases

### Legacy Workbook Maintenance

**Scenario:** An older forecast workbook uses LOGINV in dozens of cells, and the team wants to know which ones to update.

```excel
=LOGINV(Model!B2, Model!C2, Model!D2)
```

**Why It Works:** The formula still calculates correctly. Plan a switch to LOGNORM.INV before the function disappears from future Excel versions.

### Response Time Targets

**Scenario:** A support manager sets a target that 90 percent of tickets are answered within a given time.

```excel
=ROUND(LOGINV(0.9, Stats!B2, Stats!B3), 0)
```

**Why It Works:** Rounding turns the result into whole minutes that are easy to put in a service level agreement.

### Service Level Planning

**Scenario:** A warehouse estimates the order processing time that 95 percent of orders will meet.

```excel
=LOGINV(0.95, Orders!E2, Orders!E3)
```

**Why It Works:** The result sets the service target in the same unit as the historical data, so staffing decisions use a realistic upper bound.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | An argument is text or blank. | Check that all three inputs are numbers. |
| `#NUM!` | The probability is 0 or less, or 1 or more. | Use a probability strictly between 0 and 1. |
| `#NUM!` | `standard_dev` is 0 or less. | Enter a positive standard deviation of ln(x). |
| Unexpected value | The mean of x was entered instead of the mean of ln(x). | Take the natural logarithm of the sample first, then compute the mean and standard deviation. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available, listed under compatibility | Superseded by LOGNORM.INV. Microsoft warns it may not be available in future versions. |
| Google Sheets | Available | Same three arguments in the same order. The first argument is named `x`, and the help page does not give error notes. |

## Tips and Best Practices

- Use LOGNORM.INV for new formulas, and treat LOGINV as a legacy function to replace over time.
- Work on the logarithm scale: calculate ln of the data, then its mean and standard deviation, before calling the function.
- Keep the probability in a labeled cell, so reports show which percentile a figure represents.
- Check the result against the data. If the historical values rarely exceed the result, the parameters may be wrong.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LOGNORM.INV](LOGNORM.INV.md) | The modern replacement that returns the same result. |
| [LOGNORM.DIST](LOGNORM.DIST.md) | Returns the probability for a value, the reverse of LOGINV. |
| [LOGNORMDIST](LOGNORMDIST.md) | The legacy cumulative lognormal function, also a compatibility function. |
| [NORM.INV](NORM.INV.md) | The normal distribution version of an inverse function, for data that is not logged. |

## Official Documentation

- [Microsoft Support: LOGINV function](https://support.microsoft.com/en-us/excel/functions/loginv-function)
- [Google Docs Editors Help: LOGINV](https://support.google.com/docs/answer/3094010)
