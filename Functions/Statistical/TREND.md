---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
purpose:
  - Forecasting
  - Regression
use-case:
  - Revenue Trend Analysis
  - Sales Forecasting
  - Support Volume Planning
related:
  - FORECAST.LINEAR
  - GROWTH
  - INTERCEPT
  - LINEST
  - SLOPE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/trend-function
  - https://support.google.com/docs/answer/3094263
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Linear Trend Forecast
tags:
  - dynamic-array
  - excel
  - forecasting
  - linear-trend
  - regression
  - sheets
---

# TREND

## Description

**TREND** fits a straight line through known y values and known x values by the least squares method, then returns the y values that sit on that line for the x values you specify. Use it to project a steady pattern forward, such as monthly sales or ticket counts, or to compare actual values with the fitted line.

TREND accepts one x variable or several. With one x variable, the line it fits is the same line that SLOPE and INTERCEPT describe. When you supply several new x values in one formula, TREND returns a predicted value for each of them, so a single formula can fill a block of forecasts.

If you omit `new_x's`, TREND returns the fitted values for the known x values. Compare those fitted values with the actual values to judge how well a straight line describes the data. For a single prediction, FORECAST.LINEAR uses a simpler syntax and returns the same result. For data that grows by a constant percentage rather than a constant amount, use GROWTH, which fits an exponential curve.

## Syntax

```excel
=TREND(known_y's, [known_x's], [new_x's], [const])
```

<!-- Image 1: Known Data and New Points on a Trend Line. See Images/Statistical/TREND.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `known_y's` | Yes | The dependent values you already have, such as `B2:B7`. A single column treats each column of `known_x's` as a separate variable; a single row treats each row as a separate variable. |
| `known_x's` | No | The independent values that match `known_y's`, such as `A2:A7`. When omitted, TREND uses 1, 2, 3 and so on, sized to match `known_y's`. |
| `new_x's` | No | The x values for which TREND returns predicted y values. When omitted, TREND uses `known_x's`. It must have one column for each variable in `known_x's`. |
| `const` | No | TRUE or omitted calculates the intercept normally. FALSE sets the intercept to 0, so the line passes through the origin. |

### Return Value

An array of y values: one predicted value for each row of `new_x's`, or one fitted value for each known x when `new_x's` is omitted. Microsoft documents the dimension rules but does not name the error that appears when they are broken, so check that the shapes match when a result looks like an error.

## Examples

All examples use the monthly sales history in `A2:B7`, where column A holds the month number and column B holds the sales.

| Month | Sales |
| --- | --- |
| 1 | 120 |
| 2 | 135 |
| 3 | 150 |
| 4 | 158 |
| 5 | 171 |
| 6 | 186 |

### Example 1: Predict One Future Month

```excel
=TREND(B2:B7,A2:A7,7)
```

**Result:** `197.93`

TREND fits the line through the six points and returns the y value at month 7. The slope is about 12.74 sales per month and the intercept is about 108.73.

### Example 2: Fitted Values for the Known Months

```excel
=TREND(B2:B7,A2:A7)
```

**Result:** `121.48` in the first cell of the output

Without `new_x's`, TREND returns the value on the line for each known month. The first fitted value is 121.48 against an actual 120, which shows how closely the straight line follows the history.

### Example 3: Several Predictions in One Formula

```excel
=TREND(B2:B7,A2:A7,{7,8})
```

**Result:** `197.93` and `210.68` in two adjacent cells

The array constant `{7,8}` asks for two predictions. In Microsoft 365 the result fills both cells; in older versions, select both cells first and confirm with Ctrl+Shift+Enter.

<!-- Image 2: Forced Zero Intercept Comparison. See Images/Statistical/TREND.md -->

### Example 4: Force the Line Through the Origin

```excel
=TREND(B2:B7,A2:A7,7,FALSE)
```

**Result:** `264.85`

Setting `const` to FALSE removes the intercept, so the line must pass through (0, 0). The forced line gives a much higher prediction, which shows why the intercept setting matters. Use FALSE only when a value of zero at zero is part of the model.

### Example 5: Check the Result Against FORECAST.LINEAR

```excel
=FORECAST.LINEAR(7,B2:B7,A2:A7)
```

**Result:** `197.93`

With one x variable and one new x value, FORECAST.LINEAR returns the same prediction as Example 1. Use it to confirm a single forecast.

## Story Problems

### Problem 1: Support Tickets Forecast

A help desk logs tickets per month in `A1:B6`. The support lead wants the expected volume for month 8 to plan staffing.

| Month | Tickets |
| --- | --- |
| 1 | 210 |
| 2 | 232 |
| 3 | 251 |
| 4 | 270 |
| 5 | 288 |

**Task:** Predict the ticket count for month 8 using the straight-line trend.

**Solution:**

```excel
=TREND(B2:B6,A2:A6,8)
```

**Answer:** `347.20`. The slope is 19.4 tickets per month and the intercept is 192, so 192 + 19.4 × 8 = 347.2.

### Problem 2: Cold Drink Demand by Temperature

A café records the daily high temperature and the number of cold drinks sold. The owner wants an estimate for a day forecast to reach 33 degrees.

| Temperature | Drinks Sold |
| --- | --- |
| 18 | 42 |
| 21 | 49 |
| 24 | 55 |
| 27 | 62 |
| 30 | 70 |

**Task:** Estimate drink sales at 33 degrees using the trend in `A2:B6`.

**Solution:**

```excel
=TREND(B2:B6,A2:A6,33)
```

**Answer:** `76.30`. The slope is 2.3 drinks per degree and the intercept is 0.4, so 2.3 × 33 + 0.4 = 76.3. The forecast is an extension beyond the observed range, so treat it as an estimate.

<!-- Image 3: Cold Drink Forecast Worksheet. See Images/Statistical/TREND.md -->

## Use Cases

### Sales Forecast With a Named Table

**Scenario:** A finance analyst keeps 24 months of revenue in a table and wants the expected revenue for the next month.

```excel
=TREND(SalesHistory[Revenue],SalesHistory[Month],25)
```

**Why It Works:** Structured references grow with the table, so the forecast updates when new months are added. Check that the new month number is one more than the last row.

### Fitted Line Check

**Scenario:** A planner suspects that a straight line does not describe a product's demand well.

```excel
=TREND(C2:C13,B2:B13)
```

**Why It Works:** Omitting `new_x's` returns the fitted values beside the actuals. Large gaps between the two columns mean the straight line is a poor model, and GROWTH may fit better.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error value | `known_y's` and `known_x's` contain different numbers of values. | Select ranges with the same count of values. |
| Error value | `new_x's` has a different number of columns from `known_x's`. | Match the columns of `new_x's` to the variables in `known_x's`. |
| Blocked result | Cells below or beside the result are not empty in Microsoft 365. | Clear the output range so the array can spill. |
| Unexpected intercept | `const` is FALSE, which forces the line through zero. | Omit `const` or set it to TRUE unless the origin must be fixed. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | In Microsoft 365 the formula returns an array by default. Older versions need the output range selected and the formula confirmed with Ctrl+Shift+Enter. |
| Google Sheets | Available | Same behavior with the argument names `known_data_y`, `known_data_x`, `new_data_x` and `b`, where `b` plays the role of `const`. |

## Tips and Best Practices

- Keep `known_y's` and `known_x's` in matching rows so each y value pairs with the correct x value.
- Use FORECAST.LINEAR for one prediction and TREND when you need a block of predictions.
- Compare the fitted values with the actuals before trusting a forecast.
- Avoid extrapolating far beyond the known x values, because the straight line may not hold.
- Use GROWTH instead when the data grows by a constant percentage each period.
- Set `const` to FALSE only when the model genuinely requires a zero intercept.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FORECAST.LINEAR](FORECAST.LINEAR.md) | Returns one predicted value on the same straight line. |
| [GROWTH](GROWTH.md) | Fits an exponential curve instead of a straight line. |
| [INTERCEPT](INTERCEPT.md) | Returns the intercept of the same fitted line. |
| [LINEST](LINEST.md) | Returns the full regression coefficients and statistics. |
| [SLOPE](SLOPE.md) | Returns the slope of the same fitted line. |

## Official Documentation

- [Microsoft Support: TREND function](https://support.microsoft.com/en-us/excel/functions/trend-function)
- [Google Docs Editors Help: TREND](https://support.google.com/docs/answer/3094263)
