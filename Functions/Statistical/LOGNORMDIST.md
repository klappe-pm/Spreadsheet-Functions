---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Probability
use-case:
  - Legacy Workbook Maintenance
  - Lognormal Income Modeling
  - Lognormal Rate Modeling
related:
  - LOGINV
  - LOGNORM.DIST
  - LOGNORM.INV
  - NORM.DIST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/lognormdist-function
  - https://support.google.com/docs/answer/3094011
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Legacy Lognormal Distribution
tags:
  - compatibility
  - excel
  - lognormal
  - probability
  - sheets
---

# LOGNORMDIST

## Description

**LOGNORMDIST** returns the cumulative lognormal distribution of x, which is the probability that a value from a lognormal distribution is at or below x. The natural logarithm of x follows a normal distribution with the mean and standard deviation you supply. The function suits positive, right-skewed data such as claim sizes or incomes.

LOGNORMDIST is a legacy function. Microsoft lists it under compatibility, states that it has been replaced by newer functions with better accuracy and clearer names, and warns that it may not be available in future versions of Excel. The recommended replacement is LOGNORM.DIST. LOGNORM.DIST takes the same first three arguments and adds a cumulative argument, so existing results carry over directly.

Use LOGNORMDIST only when an older workbook depends on it. For new formulas, use LOGNORM.DIST with TRUE as the fourth argument. To go the other way, from a probability to a value, use LOGINV or its replacement LOGNORM.INV.

## Syntax

```excel
=LOGNORMDIST(x, mean, standard_deviation)
```

<!-- Image 1: Legacy Function Mapped to Its Replacement. See Images/Statistical/LOGNORMDIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The value at which to evaluate the cumulative distribution. It must be greater than 0. |
| `mean` | Yes | The mean of the natural logarithm of x, not the mean of x. |
| `standard_deviation` | Yes | The standard deviation of the natural logarithm of x. It must be greater than 0. |

All three arguments are required. The function returns only the cumulative probability.

### Return Value

A probability between 0 and 1 for the chance that a value is at or below x. It returns `#VALUE!` when an argument is not a number, and `#NUM!` when x is 0 or less, or when `standard_deviation` is 0 or less.

## Examples

### Example 1: Cumulative Probability

```excel
=LOGNORMDIST(20, 3, 0.4)
```

**Result:** `0.4957`

About half of values from this distribution fall at or below 20.

### Example 2: The Modern Replacement

```excel
=LOGNORM.DIST(20, 3, 0.4, TRUE)
```

**Result:** `0.4957`

With TRUE as the fourth argument, LOGNORM.DIST returns the same probability. Replace LOGNORMDIST with this form when you update a legacy sheet.

### Example 3: Catching a Value That Is Not Positive

```excel
=IFERROR(LOGNORMDIST(0, 3, 0.4), "x must be above 0")
```

**Result:** `x must be above 0`

A value of 0 falls outside the domain of the distribution, so LOGNORMDIST returns `#NUM!`. IFERROR displays a readable message instead.

## Story Problems

### Problem 1: Monthly Revenue Threshold

A subscription business models the revenue of new accounts as lognormal, with the parameters in the table below.

| Parameter | Value |
| --- | --- |
| Mean of ln(revenue) | 7.0 |
| Standard deviation of ln(revenue) | 0.8 |
| Threshold | 1500 |

**Task:** Find the probability that a new account brings in 1500 dollars or less. Use the parameters in `B2:B3` and the threshold in `B4`.

**Solution:**

```excel
=LOGNORMDIST(B4, B2, B3)
```

**Answer:** `0.6523`. About 65 percent of new accounts fall at or below 1500 dollars.

<!-- Image 2: Revenue Threshold Worksheet. See Images/Statistical/LOGNORMDIST.md -->

### Problem 2: Delivery Cost Ceiling

A logistics planner describes the cost of a single delivery with a lognormal distribution. The parameters are below.

| Parameter | Value |
| --- | --- |
| Mean of ln(cost) | 6.5 |
| Standard deviation of ln(cost) | 0.6 |
| Threshold | 800 |

**Task:** Find the probability that a delivery costs 800 dollars or less.

**Solution:**

```excel
=LOGNORMDIST(B4, B2, B3)
```

**Answer:** `0.6208`. About 62 percent of deliveries cost 800 dollars or less.

## Use Cases

### Legacy Workbook Maintenance

**Scenario:** A finance team inherits a workbook that uses LOGNORMDIST in many cells and must keep the results unchanged during an upgrade.

```excel
=LOGNORMDIST(Model!B2, Model!C2, Model!D2)
```

**Why It Works:** The formula still returns the cumulative probability. Test it against LOGNORM.DIST with TRUE, then replace it once the results match.

### Lognormal Rate Modeling

**Scenario:** An analyst estimates the share of customers whose monthly usage stays under a plan limit.

```excel
=LOGNORMDIST(Plan!B2, Usage!C2, Usage!C3)
```

**Why It Works:** The probability shows the share of customers under the limit, which informs pricing tiers.

### Lognormal Income Modeling

**Scenario:** A policy team tests how many households fall under an income threshold in a region.

```excel
=LOGNORMDIST(Threshold, Region!B2, Region!B3)
```

**Why It Works:** Placing the threshold in a named cell lets analysts change the policy line without editing the formula.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | x is 0 or less. | Filter out zero and negative values before calling the function. |
| `#NUM!` | `standard_deviation` is 0 or less. | Enter a positive standard deviation of ln(x). |
| `#VALUE!` | An argument is text or blank. | Convert the inputs to numbers. |
| Wrong probability | The mean of x was used instead of the mean of ln(x). | Compute the logarithms first, then their mean and standard deviation. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available, listed under compatibility | Replaced by LOGNORM.DIST. Microsoft warns it may not be available in future versions. |
| Google Sheets | Available | The function list shows the same three arguments, `x`, `mean` and `standard_deviation`. The help page refers to the separate LOGNORM.DIST entry for the cumulative option. |

## Tips and Best Practices

- Plan the move to LOGNORM.DIST in workbooks that use this function, and keep a note of the cells to update.
- Keep the mean and standard deviation of ln(x) in labeled cells, so reviewers can trace the model.
- Check results against LOGNORM.DIST with TRUE before retiring the legacy formula.
- Do not use this function for values of zero or less, because the lognormal model does not cover them.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LOGNORM.DIST](LOGNORM.DIST.md) | The modern replacement, with a cumulative or density option. |
| [LOGNORM.INV](LOGNORM.INV.md) | Returns the value for a given probability, the reverse calculation. |
| [LOGINV](LOGINV.md) | The legacy inverse lognormal function. |
| [NORM.DIST](NORM.DIST.md) | The normal distribution function, for data that is not logged. |

## Official Documentation

- [Microsoft Support: LOGNORMDIST function](https://support.microsoft.com/en-us/excel/functions/lognormdist-function)
- [Google Docs Editors Help: LOGNORMDIST](https://support.google.com/docs/answer/3094011)
