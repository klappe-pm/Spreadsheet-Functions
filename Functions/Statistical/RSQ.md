---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
purpose:
  - Regression
use-case:
  - Advertising Spend Analysis
  - Sales Trend Fit
  - Study Hours and Scores
related:
  - CORREL
  - FORECAST.LINEAR
  - INTERCEPT
  - PEARSON
  - SLOPE
  - STEYX
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/rsq-function
  - https://support.google.com/docs/answer/3094099
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - R Squared
tags:
  - excel
  - regression
  - sheets
---

# RSQ

## Description

**RSQ** returns the square of the Pearson correlation coefficient for two sets of values. The result, usually written as r squared, is the share of the variation in the dependent values (y) that a straight-line relationship with the independent values (x) explains. It runs from 0 to 1, where values near 1 mean the points sit close to a straight line.

Use RSQ to judge how well a simple linear trend fits, such as how closely advertising spend tracks sales. A high value shows that the line explains the pattern, but it does not prove that x causes y. A low value means a straight line is a poor model, even when the two variables are related in a curved way.

RSQ gives the same result as squaring the output of CORREL or PEARSON. The sign of the correlation is lost when you square it, so use CORREL or PEARSON when you need to know whether the relationship rises or falls.

## Syntax

```excel
=RSQ(known_y's, known_x's)
```

<!-- Image 1: RSQ Syntax Anatomy. See Images/Statistical/RSQ.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `known_y's` | Yes | The dependent values, such as sales, in a range or array. Google Sheets calls this argument `data_y`. |
| `known_x's` | Yes | The independent values, such as advertising spend, in a range or array. Google Sheets calls this argument `data_x`. |

Both arguments must contain the same number of data points. The order matters: y comes first.

### Return Value

A number from 0 to 1. The function returns `#N/A` when the arguments are empty or hold different numbers of data points, and `#DIV/0!` when they hold only one data point.

## Examples

Examples use advertising spend in thousands in `C2:C6` (x) and sales in thousands in `D2:D6` (y): 2, 4, 6, 8 and 10 for spend, and 5, 7, 11, 13 and 18 for sales.

### Example 1: Share of Variation Explained

```excel
=RSQ(D2:D6, C2:C6)
```

**Result:** `0.977099`

About 98 percent of the variation in sales is explained by a straight-line relationship with spend.

### Example 2: Rounded for a Report

```excel
=ROUND(RSQ(D2:D6, C2:C6), 2)
```

**Result:** `0.98`

Two decimal places are enough for most reports.

### Example 3: Expressed as a Percentage

```excel
=RSQ(D2:D6, C2:C6) * 100
```

**Result:** `97.7099`

Multiplying by 100 gives the share as a percentage of the variation.

### Example 4: Same Result From CORREL

```excel
=CORREL(D2:D6, C2:C6)^2
```

**Result:** `0.977099`

Squaring the correlation coefficient gives the same value as RSQ.

## Story Problems

### Problem 1: Study Hours and Test Scores

Five students recorded hours of study in `A2:A6` (1 to 5) and their test scores in `B2:B6`: 52, 58, 65, 70 and 79. The tutor wants to know how well study hours explain the scores.

| Hours | Score |
| --- | --- |
| 1 | 52 |
| 2 | 58 |
| 3 | 65 |
| 4 | 70 |
| 5 | 79 |

**Task:** Find the share of score variation explained by study hours. Put the scores first in the formula.

**Solution:**

```excel
=RSQ(B2:B6, A2:A6)
```

**Answer:** `0.992707`, so study hours explain about 99 percent of the variation in scores. The points lie very close to a straight line.

### Problem 2: Marketing Spend and Sales

A shop tracked marketing spend (1 to 4 thousand, in `E2:E5`) and sales (2, 4, 5 and 7 thousand, in `F2:F5`) over four weeks. The owner wants the share of sales variation explained by spend.

**Task:** Find the r squared value with sales as the dependent values.

**Solution:**

```excel
=RSQ(F2:F5, E2:E5)
```

**Answer:** `0.984615`, which is 64/65. Spend explains about 98 percent of the variation in sales over these four weeks, although four points is too few to rely on for a forecast.

## Use Cases

### Advertising Spend Analysis

**Scenario:** A marketing analyst checks whether monthly spend is a good predictor of monthly sales before proposing a budget increase.

```excel
=RSQ(SalesRange, SpendRange)
```

**Why It Works:** A high value shows the straight-line relationship is strong. Pair it with SLOPE to see how much sales change for each extra unit of spend.

### Sales Trend Fit

**Scenario:** A planner tests whether a straight-line trend fits recent sales well enough to use for forecasting.

```excel
=RSQ(SalesRange, MonthNumbers)
```

**Why It Works:** Using the month number as x gives a trend fit. A low value suggests seasonality or another pattern that a straight line misses.

### Study Hours and Scores

**Scenario:** A teacher compares hours of study with test results across a class.

```excel
=RSQ(ScoreRange, HoursRange)
```

**Why It Works:** The result shows how much of the spread in scores study hours account for. Other factors, such as prior knowledge, usually explain the rest.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The arguments are empty or have different numbers of data points. | Make both ranges the same length and check for blank rows. |
| `#DIV/0!` | Only one data point is supplied. | Use at least two pairs of values. |
| Error values | A cell in either range contains an error. | Fix the source cells first. |
| Unexpected result | The arguments are swapped, so x and y change places. | Put the dependent values (y) first. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Arguments are named known_y's and known_x's. Text and logical values in ranges are ignored. |
| Google Sheets | Available | Arguments are named data_y and data_x. Text in the input arguments is skipped. |

## Tips and Best Practices

- Put the dependent values (y) first and the independent values (x) second.
- Keep both ranges the same length, and remove blank rows, before you calculate.
- Use SLOPE and INTERCEPT with RSQ to describe the fitted line and its fit.
- Remember that RSQ is not evidence of cause. Check the scatter plot for curves or outliers before you rely on it.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CORREL](CORREL.md) | The correlation coefficient. Squaring it gives RSQ, and it keeps the sign. |
| [PEARSON](PEARSON.md) | The Pearson correlation coefficient, which RSQ squares. |
| [SLOPE](SLOPE.md) | The slope of the same straight-line fit. |
| [INTERCEPT](INTERCEPT.md) | The point where the same fitted line crosses the y-axis. |
| [STEYX](STEYX.md) | The standard error of the predicted y values for the same fit. |
| [FORECAST.LINEAR](FORECAST.LINEAR.md) | Predicts a y value from a new x value using the same fit. |

## Official Documentation

- [Microsoft Support: RSQ function](https://support.microsoft.com/en-us/excel/functions/rsq-function)
- [Google Docs Editors Help: RSQ](https://support.google.com/docs/answer/3094099)
