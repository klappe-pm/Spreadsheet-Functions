---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
purpose:
  - Forecasting
  - Regression
use-case:
  - Exponential Sales Trends
  - Subscriber Growth Forecasts
related:
  - FORECAST.LINEAR
  - LINEST
  - LOGEST
  - RSQ
  - SLOPE
  - TREND
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/growth-function
  - https://support.google.com/docs/answer/3094287
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Exponential Forecast
  - Exponential Trend
tags:
  - excel
  - forecasting
  - regression
  - sheets
  - trend
---

# GROWTH

## Description

**GROWTH** fits an exponential curve to known data and returns the curve's y values for new x values. An exponential curve grows by a constant multiple for each step in x, such as a customer base that adds 10 percent each month or a bacteria count that doubles each hour. The function finds the curve that best fits the known points and then reads off the predicted values.

Use GROWTH when the data bends upward at a steady rate and a straight line would understate the later values. For a straight-line trend, use TREND or FORECAST.LINEAR. For the same exponential fit expressed as coefficients, use LOGEST. GROWTH is also useful for a single forecast point, such as the expected value in the next period.

GROWTH works with one or more independent variables. With one variable, the x values can be any range with the same shape as the y values. With more than one variable, the y values must form a single column or row. Microsoft requires every y value to be greater than 0, because the exponential curve cannot pass through zero or negative values.

## Syntax

```excel
=GROWTH(known_y's, [known_x's], [new_x's], [const])
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/GROWTH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `known_y's` | Yes | The y values of the data you already have. They must be greater than 0 in Excel. |
| `known_x's` | No | The x values for the known y values. If omitted, the function uses 1, 2, 3 and so on. |
| `new_x's` | No | The x values for which to return predicted y values. If omitted, it uses `known_x's`. |
| `const` | No | TRUE, or omitted, calculates the constant b in y = b × m^x. FALSE forces b to 1 and fits y = m^x. |

### Return Value

An array of predicted y values, one for each value in `new_x's`. A single new x value returns one number. The function returns `#NUM!` when any known y value is 0 or negative, and `#VALUE!` when a value is not numeric. Enter a formula that returns several results as an array formula in older versions of Excel.

## Examples

All examples below use the x values 1 to 5 in `A2:A6`.

### Example 1: Predicting the Next Period

Known y values in `B2:B6`: 6, 12, 24, 48, 96.

```excel
=GROWTH(B2:B6, A2:A6, 6)
```

**Result:** `192`

The y values double each period, so the exponential fit predicts 192 at x = 6.

### Example 2: Forcing the Constant to 1

Known y values in `B2:B6`: 2, 4, 8, 16, 32.

```excel
=GROWTH(B2:B6, A2:A6, 6, FALSE)
```

**Result:** `64`

With `const` set to FALSE, the fit is y = m^x. Because these values follow 2^x exactly, the prediction for x = 6 is 64.

### Example 3: Fitted Values for the Known Points

```excel
=GROWTH(B2:B6)
```

**Result:** `6, 12, 24, 48, 96` (spilled as five values)

When `known_x's` and `new_x's` are omitted, the function returns the fitted values at x = 1 to 5. For exact exponential data, the fitted values match the original points.

### Example 4: Guarding Against Zero

```excel
=IFERROR(GROWTH(C2:C6, A2:A6, 6), "Use positive values")
```

**Result:** `Use positive values` when a value in `C2:C6` is 0

A zero or negative known y value returns `#NUM!`, so IFERROR displays a message instead.

## Story Problems

### Problem 1: Subscriber Forecast

A newsletter's subscriber count grew by 10 percent each month for five months.

| Month | Subscribers |
| --- | --- |
| 1 | 500 |
| 2 | 550 |
| 3 | 605 |
| 4 | 665.5 |
| 5 | 732.05 |

**Task:** Predict the subscriber count in month 6 using an exponential trend.

**Solution:**

```excel
=GROWTH(B2:B6, A2:A6, 6)
```

**Answer:** `805.255`, or about 805 subscribers. The data grows by a factor of 1.1 each month, so the month 6 value is 732.05 × 1.1.

### Problem 2: Bacteria Culture Count

A lab counts a culture every hour. The counts are 20, 30, 45 and 67.5 at hours 1 to 4, and the counts keep growing by the same factor.

| Hour | Count |
| --- | --- |
| 1 | 20 |
| 2 | 30 |
| 3 | 45 |
| 4 | 67.5 |

**Task:** Predict the count at hour 5.

**Solution:**

```excel
=GROWTH(B2:B5, A2:A5, 5)
```

**Answer:** `101.25`, because each hour multiplies the count by 1.5, and 67.5 × 1.5 equals 101.25.

## Use Cases

### Exponential Sales Trends

**Scenario:** A retail analyst fits a trend to five years of sales that compound each year, then reads the expected figure for the next year.

```excel
=GROWTH(Sales[Revenue], Sales[Year], NextYear)
```

**Why It Works:** The exponential curve matches compounding growth better than a straight line. Check the fit with RSQ before relying on the forecast.

<!-- Image 2: Exponential Fit Versus Straight Line. See Images/Statistical/GROWTH.md -->

### Subscriber Growth Forecasts

**Scenario:** A product manager fills a row of future months with predicted subscriber counts.

```excel
=GROWTH(SubsRange, MonthRange, FutureMonths)
```

**Why It Works:** Passing a range for `new_x's` returns one prediction per month. Keep the known x values in the same orientation as the y values.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | A known y value is 0 or negative. | Remove or correct the value, or use TREND for data that crosses zero. |
| `#VALUE!` | A value is text or the ranges contain non-numeric entries. | Clean the data before calling the function. |
| Mismatched results | The known x and y ranges have different numbers of values. | Make the ranges the same length and shape. |
| Poor forecast | The data does not follow an exponential pattern. | Compare with TREND and check the fit with RSQ. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Listed on the Microsoft page for current versions | Requires y values greater than 0. Returns an array of predictions. |
| Google Sheets | Available as GROWTH with the arguments known_data_y, known_data_x, new_data_x and b | The help page documents the same four arguments. The default for `b` is TRUE. |

## Tips and Best Practices

- Plot the data first. Use GROWTH only when the points curve upward at a steady rate.
- Use FALSE for `const` only when the data should start from a multiplier of 1 at x = 0.
- Compare the result with TREND, which fits a straight line, to see which model matches better.
- Keep known and new x values on the same scale so the predictions line up with the data.

## Related Functions

| Function | Relationship |
| --- | --- |
| [TREND](TREND.md) | Straight-line fit for the same kind of forecast. |
| [LOGEST](LOGEST.md) | Returns the coefficients of the exponential fit that GROWTH uses. |
| [LINEST](LINEST.md) | Returns the coefficients of a straight-line fit. |
| [FORECAST.LINEAR](FORECAST.LINEAR.md) | Linear forecast for one x value. |
| [SLOPE](SLOPE.md) | Slope of a straight-line fit, useful for comparing trends. |
| [RSQ](RSQ.md) | Shows how closely the data follows the fitted line. |

## Official Documentation

- [Microsoft Support: GROWTH function](https://support.microsoft.com/en-us/excel/functions/growth-function)
- [Google Docs Editors Help: GROWTH](https://support.google.com/docs/answer/3094287)
