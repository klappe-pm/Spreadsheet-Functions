---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
purpose:
  - Statistical Analysis
use-case:
  - Pilot Study Comparisons
  - Sample Survey Relationships
  - Trial Batch Quality Checks
related:
  - CORREL
  - COVAR
  - COVARIANCE.P
  - PEARSON
  - STDEV.S
  - VAR.S
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/covariance-s-function
  - https://support.google.com/docs/answer/9365675
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Sample Covariance
  - Covariance Sample
tags:
  - covariance
  - excel
  - sample-statistics
  - sheets
---

# COVARIANCE.S

## Description

**COVARIANCE.S** returns the sample covariance of two data sets. It averages the products of the deviations of each pair of data points from their means, but it divides by one less than the number of pairs. That adjustment corrects for the fact that a sample tends to understate the spread of the whole group. Use it when your data is a sample taken from a larger group, such as ten pilot stores, a survey of households, or a few test bottles from a production run.

Use COVARIANCE.P when the data covers the whole group. For the same data, COVARIANCE.S returns a larger value, because it divides by a smaller number. The sign of the result is the same for both functions, and the sign is the part of the answer that shows the direction of the relationship.

Covariance depends on the units of both data sets, so the number does not show how strong the link is. Use CORREL for a unit-free value from -1 to 1.

## Syntax

```excel
=COVARIANCE.S(array1, array2)
```

<!-- Image 1: COVARIANCE.S Syntax Anatomy. See Images/Statistical/COVARIANCE.S.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array1` | Yes | The first range or array of numbers. Google Sheets calls it `data_y`, the dependent data. |
| `array2` | Yes | The second range or array of numbers, with the same number of data points as `array1`. Google Sheets calls it `data_x`, the independent data. |

### Return Value

A number: the sample covariance of the two data sets. It returns `#N/A` when the arrays have different numbers of data points. It returns `#DIV/0!` when either array is empty or when each array contains only one data point, because the divisor would be zero. Text, logical values and empty cells are ignored, while zeros are included.

## Examples

All examples use this table in `A1:C6`. Column A holds the number of training sessions each trial employee attended, column B holds the test score for each employee, and column C holds the number of errors made in the first week.

| Sessions | Test Score | First Week Errors |
| --- | --- | --- |
| 1 | 2 | 9 |
| 2 | 5 | 8 |
| 3 | 6 | 6 |
| 4 | 8 | 5 |
| 5 | 11 | 3 |

### Example 1: Sessions and Test Scores

```excel
=COVARIANCE.S(A2:A6, B2:B6)
```

**Result:** `5.25`

The deviation products sum to 21. Because this is a sample, the sum is divided by 4 instead of 5, which gives 5.25.

### Example 2: Two Points

```excel
=COVARIANCE.S({4,8}, {2,6})
```

**Result:** `8`

The means are 6 and 4. Each point is 2 away from its mean in both lists, so the two products are 4 and 4. The sum is 8, and dividing by one gives 8.

<!-- Image 2: Sample Divisor Compared With Population. See Images/Statistical/COVARIANCE.S.md -->

### Example 3: Opposite Movement

```excel
=COVARIANCE.S(A2:A6, C2:C6)
```

**Result:** `-3.75`

As sessions rise, first-week errors fall. The deviation products sum to -15, and dividing by 4 gives -3.75.

### Example 4: Sample Versus Population

```excel
=COVARIANCE.S(A2:A6, B2:B6) / COVARIANCE.P(A2:A6, B2:B6)
```

**Result:** `1.25`

The ratio equals 5 divided by 4 for five pairs. Use this check to confirm that the two functions differ only by the divisor.

## Story Problems

### Problem 1: Cooking Hours and Takeout Orders in a Household Survey

A nutrition researcher surveys four households and records weekly cooking hours and takeout orders per month. The four homes are a sample of a larger neighborhood, so the sample form applies. The data is in `A1:C5`.

| Household | Cooking Hours | Takeout Orders |
| --- | --- | --- |
| Household A | 3 | 10 |
| Household B | 5 | 8 |
| Household C | 7 | 5 |
| Household D | 9 | 3 |

**Task:** Find the sample covariance of cooking hours and takeout orders.

**Solution:**

```excel
=COVARIANCE.S(B2:B5, C2:C5)
```

**Answer:** `-8`. The mean cooking time is 6 hours and the mean takeout count is 6.5. The deviation products sum to -24, and dividing by 3 gives -8. More cooking goes with fewer takeout orders.

<!-- Image 3: Household Survey Result. See Images/Statistical/COVARIANCE.S.md -->

### Problem 2: Promotion Discounts in Pilot Stores

Four pilot stores offered different discounts, and each store reported its extra units sold in `A1:C5`. The four stores are a sample of the chain.

| Store | Discount Percent | Extra Units Sold |
| --- | --- | --- |
| Store 1 | 5 | 11 |
| Store 2 | 10 | 20 |
| Store 3 | 15 | 26 |
| Store 4 | 20 | 33 |

**Task:** Find the sample covariance of discount percent and extra units sold.

**Solution:**

```excel
=COVARIANCE.S(B2:B5, C2:C5)
```

**Answer:** `60`. The mean discount is 12.5 percent and the mean extra sales figure is 22.5 units. The deviation products sum to 180, and dividing by 3 gives 60.

## Use Cases

### Pilot Study Comparisons

**Scenario:** A retail planner tests a new layout in twenty stores and compares the store's floor space change with its sales change.

```excel
=COVARIANCE.S(Pilot!B2:B21, Pilot!C2:C21)
```

**Why It Works:** The twenty pilot stores are a sample of the chain, so the divisor of n minus 1 is correct. Keep the two ranges the same length, with each store in the same row.

### Sample Survey Relationships

**Scenario:** A researcher keeps survey responses in a table and wants the direction of the link between hours of exercise and monthly spending on fitness.

```excel
=COVARIANCE.S(Survey[Exercise Hours], Survey[Fitness Spend])
```

**Why It Works:** The table grows with new responses, and the sign of the result shows whether the two measures rise together.

### Trial Batch Quality Checks

**Scenario:** A plant engineer measures line speed and scrap rate on a trial batch of bottles, and treats the batch as a sample of the full run.

```excel
=COVARIANCE.S(Trial[Line Speed], Trial[Scrap Rate])
```

**Why It Works:** The trial batch is a subset of the full run, so the sample form is the right choice. Compare the result with CORREL before deciding whether to change the line speed.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | Only one data point, or an empty array. | Use at least two pairs of values. |
| `#N/A` | The two arrays have different numbers of data points. | Make both ranges the same length. |
| Value is larger than expected | The data is the whole group, but the sample divisor was used. | Use COVARIANCE.P for a complete population. |
| Result read as strength | Covariance depends on the units of both data sets. | Use CORREL for a value from -1 to 1. |
| Unexpected value | Blanks or text in one range are ignored, so rows no longer match. | Check both ranges for blanks and text. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | The support page documents `#N/A` for unequal arrays and `#DIV/0!` for an empty array or a single data point. |
| Google Sheets | Available | The help page gives the syntax `COVARIANCE.S(data_y, data_x)` with the dependent data first. |

## Tips and Best Practices

- Use COVARIANCE.S when the data is a sample, and COVARIANCE.P when the data is the whole group.
- Compare the two functions on the same data to see the size of the sample adjustment.
- Read the sign first, then use CORREL when the strength of the link matters.
- Keep paired values in the same rows and check both ranges for blanks.
- Include the units in the label beside the result, because covariance does not have a unit-free scale.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COVARIANCE.P](COVARIANCE.P.md) | Divides by n, for data that covers the whole group. |
| [COVAR](COVAR.md) | Legacy covariance that matches COVARIANCE.P. |
| [CORREL](CORREL.md) | Returns the unit-free correlation, from -1 to 1. |
| [PEARSON](PEARSON.md) | Returns the Pearson correlation coefficient. |
| [STDEV.S](STDEV.S.md) | Returns the sample standard deviation of one data set. |
| [VAR.S](VAR.S.md) | Returns the sample variance of one data set. |

## Official Documentation

- [Microsoft Support: COVARIANCE.S function](https://support.microsoft.com/en-us/excel/functions/covariance-s-function)
- [Google Docs Editors Help: COVARIANCE.S](https://support.google.com/docs/answer/9365675)
