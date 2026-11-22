---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
purpose:
  - Forecasting
  - Regression
use-case:
  - Advertising Return Estimates
  - Sales Trend Review
  - Study Time and Scores
related:
  - CORREL
  - FORECAST.LINEAR
  - INTERCEPT
  - LINEST
  - RSQ
  - TREND
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/slope-function
  - https://support.google.com/docs/answer/3094048
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Linear Regression Slope
tags:
  - excel
  - forecasting
  - regression
  - sheets
---

# SLOPE

## Description

**SLOPE** returns the slope of the straight line that best fits a set of x and y values, found by linear regression. The slope tells you how much the y value changes for each one-unit increase in x. A slope of 4 means that, on average, y rises by 4 for every extra unit of x.

Use SLOPE when you want to measure the rate of change between two related quantities, such as advertising spend and leads, or hours studied and test scores. It works on the same data as INTERCEPT, which gives the point where the line crosses the y axis, and RSQ, which shows how closely the points follow a straight line.

SLOPE fits a single straight line and ignores the curve a non-linear relationship might follow. Check the points with a chart before you rely on the result. Both lists must contain the same number of data points. Excel returns `#N/A` when they differ, and `#DIV/0!` when the x values do not vary at all.

## Syntax

```excel
=SLOPE(known_y's, known_x's)
```

<!-- Image 1: Known Y and Known X Arguments. See Images/Statistical/SLOPE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `known_y's` | Yes | The range or array of dependent values, the results you are trying to predict. |
| `known_x's` | Yes | The range or array of independent values, the inputs that drive the result. Must have the same number of data points as `known_y's`. |

### Return Value

A number: the slope of the regression line. Text, logical values and empty cells in a range are ignored. Cells that contain zero are included. The function returns `#N/A` when the two arguments are empty or contain different numbers of data points, and `#DIV/0!` when the x values have no variation.

## Examples

All examples use the x values 1, 2, 3, 4 and 5 in `A2:A6` and the y values 2, 4, 5, 4 and 5 in `B2:B6`.

### Example 1: Basic Slope

```excel
=SLOPE(B2:B6, A2:A6)
```

**Result:** `0.6`

For each one-unit increase in x, the fitted line rises by 0.6 units of y. Note the order: the y values come first.

### Example 2: Slope Per Ten Units

```excel
=SLOPE(B2:B6, A2:A6)*10
```

**Result:** `6`

Multiplying the slope converts it to a more useful unit, such as change per ten units of x.

<!-- Image 2: Reading Slope in a Results Cell. See Images/Statistical/SLOPE.md -->

### Example 3: Forecasting With the Slope

```excel
=FORECAST.LINEAR(6, B2:B6, A2:A6)
```

**Result:** `5.8`

The line has a slope of 0.6 and an intercept of 2.2, so at x equal to 6 the forecast is 0.6 × 6 + 2.2 = 5.8.

### Example 4: Mismatched Lists

```excel
=SLOPE(B2:B6, A2:A5)
```

**Result:** `#N/A`

The y list has five values and the x list has four. Extend or trim one list so both cover the same rows.

## Story Problems

### Problem 1: Advertising Spend and Leads

A marketing team records monthly spend in thousands of dollars and the number of sales leads each month.

| Month | Spend (Thousands) | Leads |
| --- | --- | --- |
| Jan | 1 | 12 |
| Feb | 2 | 15 |
| Mar | 3 | 21 |
| Apr | 4 | 24 |
| May | 5 | 28 |
| Jun | 6 | 33 |

**Task:** Estimate how many extra leads each additional thousand dollars of spend produces.

**Solution:**

```excel
=SLOPE(C2:C7, B2:B7)
```

**Answer:** `4.2`. Each extra thousand dollars of spend adds about 4.2 leads on this line. The intercept is about 7.47 leads, which is the estimate when spend is zero.

### Problem 2: Study Hours and Quiz Scores

A tutor records weekly study hours and the quiz score each student earned.

| Student | Hours | Score |
| --- | --- | --- |
| 1 | 2 | 55 |
| 2 | 3 | 60 |
| 3 | 5 | 68 |
| 4 | 6 | 71 |
| 5 | 8 | 80 |
| 6 | 9 | 84 |
| 7 | 10 | 88 |

**Task:** Find the typical score gain for each extra hour of study.

**Solution:**

```excel
=SLOPE(C2:C8, B2:B8)
```

**Answer:** `4.0781`, or about 4.08 points per hour. The tutor can use this rate to set expectations, but it describes these seven students only.

<!-- Image 3: Story Problem Results. See Images/Statistical/SLOPE.md -->

## Use Cases

### Advertising Return Estimates

**Scenario:** A campaign manager wants a rough estimate of how many leads a larger budget would produce next quarter.

```excel
=SLOPE(Leads, Spend)
```

**Why It Works:** The slope converts past spend and lead counts into a rate. Use it as a planning estimate, and check the fit with RSQ before trusting it.

### Sales Trend Review

**Scenario:** A finance analyst compares monthly revenue against the month number to see whether revenue is rising steadily.

```excel
=SLOPE(RevenueRange, MonthNumberRange)
```

**Why It Works:** A positive slope indicates steady growth on average. Keep the month numbers as numbers, not text labels, so the regression reads them correctly.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The two lists have different lengths or are empty. | Select the same number of rows in both lists. |
| `#DIV/0!` | Every x value is identical, so no line can be fitted. | Check that the x values vary. |
| `#VALUE!` | A range contains text that cannot be read as a number. | Clean the source data or convert the values. |
| Misleading slope | The relationship is curved, or a single outlier controls the line. | Plot the points and remove or review outliers. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel for Microsoft 365, Excel for the web | Returns `#N/A` for unequal or empty lists. Text and empty cells in ranges are ignored. |
| Google Sheets | Available | Same syntax and argument names. Text in the value arguments is ignored. |

## Tips and Best Practices

- Put the y values first and the x values second, which the syntax requires.
- Plot a scatter chart before trusting the slope, because the fit only describes a straight line.
- Pair SLOPE with INTERCEPT to build a full forecast equation.
- Use RSQ to see how much of the variation in y the line explains.
- Keep both lists on the same rows, so each x value matches its own y value.

## Related Functions

| Function | Relationship |
| --- | --- |
| [INTERCEPT](INTERCEPT.md) | The y value where the regression line crosses the axis. |
| [FORECAST.LINEAR](FORECAST.LINEAR.md) | Predicts a y value for a new x value using the same line. |
| [RSQ](RSQ.md) | Shows how closely the points follow the line. |
| [LINEST](LINEST.md) | Returns the slope and intercept together, plus fit statistics. |
| [CORREL](CORREL.md) | Measures the strength and direction of the linear relationship. |
| [TREND](TREND.md) | Returns predicted y values for one or more x values. |

## Official Documentation

- [Microsoft Support: SLOPE function](https://support.microsoft.com/en-us/excel/functions/slope-function)
- [Google Docs Editors Help: SLOPE](https://support.google.com/docs/answer/3094048)
