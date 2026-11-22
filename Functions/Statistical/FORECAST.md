---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
purpose:
  - Forecasting
  - Regression
use-case:
  - Sales Forecasting
  - Staffing Plans
  - Utility Cost Forecasting
related:
  - FORECAST.LINEAR
  - GROWTH
  - INTERCEPT
  - LINEST
  - RSQ
  - SLOPE
  - TREND
level: 3
source:
  - https://support.microsoft.com/en-us/excel/forecast-and-forecast-linear-functions
  - https://support.google.com/docs/answer/3094000
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Linear Forecast
tags:
  - excel
  - forecasting
  - regression
  - sheets
---

# FORECAST

## Description

**FORECAST** predicts a y value for a given x by fitting a straight line through known x and y values using linear regression. The line has the form a + bx, where b is the slope and a is the intercept. Use it when the relationship between the two sets of values is roughly linear and you want a single estimate for a new x.

Microsoft replaced FORECAST with FORECAST.LINEAR in Excel 2016 as part of its forecasting functions. The two have the same syntax and return the same result, and Microsoft says FORECAST will eventually be deprecated. Use FORECAST.LINEAR in new work, and keep FORECAST in workbooks that already rely on it.

Predictions far outside the range of the known x values are less reliable, because the straight line may not hold there. Check the data with a chart before you trust a long-range estimate.

## Syntax

```excel
=FORECAST(x, known_y's, known_x's)
```

<!-- Image 1: Known X and Y Ranges With the Forecast Point. See Images/Statistical/FORECAST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The x value for which to predict y. |
| `known_y's` | Yes | The dependent range of y values that you want to predict. |
| `known_x's` | Yes | The independent range of x values that explain the y values. |

### Return Value

A single predicted y value as a number. Excel returns `#VALUE!` when `x` is not numeric, `#N/A` when the known ranges are empty or hold different numbers of data points, and `#DIV/0!` when the variance of the known x values is zero.

## Examples

Examples 1 to 3 use these values: `A2:A7` holds ad spend of 10, 15, 20, 25, 30 and 35 thousand, and `B2:B7` holds sales of 105, 128, 146, 170, 188 and 215 thousand.

### Example 1: Forecast at a New Spend Level

```excel
=FORECAST(40, B2:B7, A2:A7)
```

**Result:** `234.07` (rounded to two decimal places)

The fitted line has a slope of about 4.31 and an intercept of about 61.72, so a spend of 40 predicts sales of about 234.07.

<!-- Image 2: Scatter Plot With the Fitted Line and Forecast Point. See Images/Statistical/FORECAST.md -->

### Example 2: Forecast Inside the Data Range

```excel
=FORECAST(22, B2:B7, A2:A7)
```

**Result:** `156.51` (rounded to two decimal places)

A spend of 22 lies inside the known range, so this estimate is more reliable than the forecast at 40.

### Example 3: Change Per Unit of X

```excel
=FORECAST(40, B2:B7, A2:A7) - FORECAST(30, B2:B7, A2:A7)
```

**Result:** `43.09` (rounded to two decimal places)

The difference between two forecasts equals the slope times the change in x. Here the slope is about 4.31 per thousand of spend, and the change in spend is 10.

## Story Problems

### Problem 1: Overtime and Orders Processed

A warehouse manager records weekly overtime hours and the number of orders processed. The manager wants to estimate the orders processed in a week with 45 overtime hours.

| Week | Overtime Hours | Orders Processed |
| --- | --- | --- |
| 1 | 20 | 310 |
| 2 | 25 | 335 |
| 3 | 30 | 352 |
| 4 | 35 | 380 |
| 5 | 40 | 401 |

**Task:** Put 45 in `E2` and forecast the orders processed, using the known y values in `C2:C6` and the known x values in `B2:B6`.

**Solution:**

```excel
=FORECAST(E2, C2:C6, B2:B6)
```

**Answer:** `423.70`. The slope is 4.54 orders per overtime hour and the intercept is 219.4, so 219.4 + 4.54 × 45 equals 423.70.

### Problem 2: Heating Degree Days and Gas Bills

A property company compares heating degree days with monthly gas bills at one building. It wants to estimate the bill for a month with 400 degree days.

| Month | Heating Degree Days | Gas Bill ($) |
| --- | --- | --- |
| Jan | 200 | 480 |
| Feb | 250 | 560 |
| Mar | 300 | 655 |
| Apr | 350 | 720 |

**Task:** Put 400 in `E2` and forecast the gas bill, using the bills in `C2:C5` and the degree days in `B2:B5`.

**Solution:**

```excel
=FORECAST(E2, C2:C5, B2:B5)
```

**Answer:** `807.50`. The slope is 1.63 dollars per degree day and the intercept is 155.50. The forecast point lies just beyond the highest known value, so the company should treat it as a rough estimate.

## Use Cases

### Sales Forecasting

**Scenario:** A sales planner estimates next quarter's revenue from planned advertising spend, using the last 12 months of data.

```excel
=FORECAST(PlannedSpend, Sales, AdSpend)
```

**Why It Works:** Named ranges show which input is the predicted value and which are the known values. Check the fit with RSQ before you rely on the forecast.

### Staffing Plans

**Scenario:** An operations manager estimates the orders that a team can process at a given level of overtime before setting a rota.

```excel
=FORECAST(PlannedHours, OrdersProcessed, OvertimeHours)
```

**Why It Works:** The forecast gives one planning figure for each overtime level. Use a range of planned hours and fill the formula down to build a table of options.

### Utility Cost Forecasting

**Scenario:** A facilities team estimates the gas bill for a month with a forecast number of heating degree days.

```excel
=FORECAST(ForecastDays, GasBills, DegreeDays)
```

**Why It Works:** The known ranges come from past bills, and the forecast point comes from the weather planning figure. Update the known ranges each quarter so the line reflects the latest data.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The known y and x ranges have different numbers of values, or one is empty. | Make both ranges the same size and fill them with data. |
| `#DIV/0!` | Every known x value is the same, so no line can be fitted. | Use x values that vary. |
| `#VALUE!` | The x value is text. | Convert the value to a number. |
| Arguments reversed | The known y values were entered in the x position. | Use the order `x`, `known_y's`, `known_x's`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available, with FORECAST.LINEAR as the current name | Microsoft replaced FORECAST with FORECAST.LINEAR in Excel 2016 and says FORECAST will eventually be deprecated. |
| Google Sheets | Available | Uses the same syntax. Google's help page says text in the value arguments is ignored. |

## Tips and Best Practices

- Plot the known values as a scatter chart before you trust the line, because a curved pattern will produce a misleading forecast.
- Use FORECAST.LINEAR in new work so the formula is ready when FORECAST is retired.
- Check RSQ or the chart for the strength of the relationship, since a weak fit gives a forecast that is not much better than the average.
- Keep the known ranges the same length and on the same rows, so pairs of x and y values stay matched.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FORECAST.LINEAR](FORECAST.LINEAR.md) | The current name for the same linear forecast, with identical syntax. |
| [GROWTH](GROWTH.md) | Forecasts along an exponential curve instead of a straight line. |
| [INTERCEPT](INTERCEPT.md) | Returns the value a, where the fitted line crosses the y axis. |
| [LINEST](LINEST.md) | Returns the slope and intercept together, along with fit statistics. |
| [RSQ](RSQ.md) | Returns the R squared value, a measure of how well the line fits. |
| [SLOPE](SLOPE.md) | Returns the slope b of the fitted line. |
| [TREND](TREND.md) | Returns predicted values for one or more x values on the same line. |

## Official Documentation

- [Microsoft Support: FORECAST and FORECAST.LINEAR functions](https://support.microsoft.com/en-us/excel/forecast-and-forecast-linear-functions)
- [Google Docs Editors Help: FORECAST](https://support.google.com/docs/answer/3094000)
