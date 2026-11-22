---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
purpose:
  - Forecasting
  - Regression
use-case:
  - Cost Estimation
  - Sales Trend Projection
related:
  - FORECAST
  - FORECAST.ETS
  - INTERCEPT
  - LINEST
  - SLOPE
  - TREND
level: 3
source:
  - https://support.microsoft.com/en-us/excel/forecasting-functions-reference#_forecast.linear
  - https://support.google.com/docs/answer/3094000
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Linear Forecast
tags:
  - excel
  - forecasting
  - linear-regression
  - sheets
---

# FORECAST.LINEAR

## Description

**FORECAST.LINEAR** predicts a y value for a given x value by fitting a straight line through known x and y values with linear regression. Use it when one quantity moves in a steady, roughly straight relationship with another, such as sales rising with advertising spend or cost rising with machine hours.

FORECAST.LINEAR replaces the older FORECAST function in Excel 2016 and later. Microsoft states that the two functions have the same syntax and usage and keeps FORECAST for backward compatibility. Use FORECAST.LINEAR in new work. Google's help page documents the same calculation under the FORECAST name with the same arguments.

The function ignores the time pattern of the data. If the history has a cycle, such as holiday peaks, use FORECAST.ETS instead, because a straight line cannot follow the peaks.

## Syntax

```excel
=FORECAST.LINEAR(x, known_y's, known_x's)
```

<!-- Image 1: Known Values Layout. See Images/Statistical/FORECAST.LINEAR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The x value for which you want a predicted y value. A nonnumeric value returns `#VALUE!`. |
| `known_y's` | Yes | The dependent values, the quantity you want to predict. |
| `known_x's` | Yes | The independent values that the known y values depend on. It must contain the same number of points as `known_y's`. |

### Return Value

A single number: the predicted y value at `x`, based on the least-squares line through the known points. The function returns `#N/A` when either range is empty or when the two ranges have different numbers of points. It returns `#DIV/0!` when every known x value is the same, because no line can be fitted.

## Examples

The examples use advertising spend in thousands of dollars in `A2:A6` as the known x values, and sales in thousands of dollars in `B2:B6` as the known y values. The rows are 40, 50, 60, 70 and 80 for spend, paired with 220, 260, 290, 330 and 360 for sales.

### Example 1: Predicting Sales for a New Spend Level

```excel
=FORECAST.LINEAR(90, B2:B6, A2:A6)
```

**Result:** `397`

The fitted line has a slope of 3.5 and an intercept of 82, so 82 + 3.5 times 90 gives 397.

<!-- Image 2: Scatter Plot With Fitted Line. See Images/Statistical/FORECAST.LINEAR.md -->

### Example 2: Handling a Blank Input

```excel
=IFERROR(FORECAST.LINEAR(C2, B2:B6, A2:A6), "Enter a spend value")
```

**Result:** `432` when `C2` holds 100, or `Enter a spend value` when `C2` holds text.

The wrapper shows a clear message instead of an error code. The function returns `#VALUE!` for nonnumeric `x`, and IFERROR turns that into the message.

### Example 3: Checking the Slope

```excel
=SLOPE(B2:B6, A2:A6)
```

**Result:** `3.5`

Each extra thousand dollars of spend is associated with 3.5 thousand dollars of additional sales in this history. Read it as an association in the data, not as proof that spend causes the change.

### Example 4: Checking the Intercept

```excel
=INTERCEPT(B2:B6, A2:A6)
```

**Result:** `82`

The intercept is the predicted sales at zero spend. The data only covers spend from 40 to 80, so treat the intercept as a fitting value rather than a real forecast for zero spend.

## Story Problems

### Problem 1: Sales at a Higher Budget

A marketing team tracks monthly advertising spend and sales in thousands of dollars.

| Spend | Sales |
| --- | --- |
| 40 | 220 |
| 50 | 260 |
| 60 | 290 |
| 70 | 330 |
| 80 | 360 |

**Task:** Predict sales if the team spends 90 thousand dollars.

**Solution:**

```excel
=FORECAST.LINEAR(90, B2:B6, A2:A6)
```

**Answer:** `397`, which is 397 thousand dollars of sales. The slope is 3.5 and the intercept is 82, so 82 + 3.5 times 90 = 397.

<!-- Image 3: Story Problem Results Panel. See Images/Statistical/FORECAST.LINEAR.md -->

### Problem 2: Output at a Longer Shift

A plant records machine hours and units produced for five shifts. The hours are in `A2:A6` and the units are in `B2:B6`.

| Hours | Units |
| --- | --- |
| 10 | 52 |
| 12 | 60 |
| 14 | 67 |
| 16 | 71 |
| 18 | 79 |

**Task:** Predict output for a 20 hour shift.

**Solution:**

```excel
=FORECAST.LINEAR(20, B2:B6, A2:A6)
```

**Answer:** `85.3`, rounded to one decimal place. The slope is 3.25 and the intercept is 20.3, so 20.3 + 3.25 times 20 = 85.3.

## Use Cases

### Sales Trend Projection

**Scenario:** A sales manager estimates next quarter's revenue from the spend levels planned in the budget.

```excel
=FORECAST.LINEAR(Planned_Spend, Revenue_Hist, Spend_Hist)
```

**Why It Works:** Named ranges keep the formula readable. The result is only as reliable as the straight-line pattern in the history, so check the scatter plot before you use it for planning.

### Cost Estimation

**Scenario:** A production planner estimates the cost of a job from its machine hours before a quote is sent.

```excel
=FORECAST.LINEAR(C2, Cost_Hist, Hours_Hist)
```

**Why It Works:** When cost grows steadily with hours, the fitted line gives a quick estimate. Recalculate the line when the price of materials changes, because the old history no longer reflects the cost.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The `x` argument is text. | Enter a number, or wrap the formula in IFERROR with a clear message. |
| `#N/A` | One range is empty or the two ranges have different numbers of points. | Select ranges with the same number of rows. |
| `#DIV/0!` | Every known x value is the same. | Use a history where the x values vary. |
| Unexpected value | The relationship is curved, so a straight line misses the pattern. | Plot the data, and use FORECAST.ETS for series with cycles. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later (Windows and Mac) | Replaces FORECAST, which remains for backward compatibility. Microsoft states the two have the same syntax. |
| Google Sheets | Available | The help page documents the calculation under the FORECAST name with the same arguments. Use FORECAST if the FORECAST.LINEAR name is not recognized. |

## Tips and Best Practices

- Plot the known x and y values in a scatter chart first, so you can see whether a straight line is a reasonable fit.
- Keep the known x and y ranges the same length, because a mismatch returns `#N/A`.
- Do not forecast far outside the range of the known x values, because the line is only tested inside that range.
- Use FORECAST.LINEAR in new work, and keep FORECAST only in older workbooks that already use it.
- Pair the forecast with SLOPE, INTERCEPT or LINEST when a reviewer wants to see the fitted line.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FORECAST](FORECAST.md) | Earlier name for the same calculation, kept for compatibility. |
| [FORECAST.ETS](FORECAST.ETS.md) | Forecast for series with seasonal patterns. |
| [INTERCEPT](INTERCEPT.md) | Returns the y value where the fitted line crosses the axis. |
| [LINEST](LINEST.md) | Returns the full regression statistics for the same line. |
| [SLOPE](SLOPE.md) | Returns the slope of the fitted line. |
| [TREND](TREND.md) | Returns fitted values for several x values at once. |

## Official Documentation

- [Microsoft Support: Forecasting functions reference](https://support.microsoft.com/en-us/excel/forecasting-functions-reference#_forecast.linear)
- [Google Docs Editors Help: FORECAST](https://support.google.com/docs/answer/3094000)
