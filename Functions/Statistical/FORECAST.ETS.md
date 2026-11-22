---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
purpose:
  - Forecasting
  - Statistical Analysis
use-case:
  - Monthly Sales Forecast
  - Seasonal Demand Planning
related:
  - FORECAST
  - FORECAST.ETS.CONFINT
  - FORECAST.ETS.SEASONALITY
  - FORECAST.ETS.STAT
  - FORECAST.LINEAR
  - TREND
level: 4
source:
  - https://support.microsoft.com/en-us/excel/forecasting-functions-reference#_forecast.ets
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Exponential Smoothing Forecast
tags:
  - excel
  - exponential-smoothing
  - forecasting
  - time-series
---

# FORECAST.ETS

## Description

**FORECAST.ETS** predicts a future value from historical values by using the AAA version of Exponential Smoothing (ETS). ETS gives recent observations more weight than older ones, and it adjusts for a trend and for a repeating seasonal pattern when the history contains one. Use it when the data has a cycle, such as monthly sales that peak every December, because the function can detect that cycle on its own.

Use FORECAST.LINEAR or TREND when the data follows a straight line and no seasonal pattern matters. The timeline must have a constant step between points, such as one day, one month or one quarter, and the target must come after the last historical point.

Microsoft lists FORECAST.ETS for Excel 2016 and later on Windows and Mac. Its support page also states that the function is not available in Excel for the web, iOS, or Android, so check the platform your readers use before you depend on it. Google Sheets does not offer this function.

## Syntax

```excel
=FORECAST.ETS(target_date, values, timeline, [seasonality], [data_completion], [aggregation])
```

<!-- Image 1: Timeline and Values Layout. See Images/Statistical/FORECAST.ETS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `target_date` | Yes | The date or period number to predict. A target that falls before the end of the historical timeline returns `#NUM!`. |
| `values` | Yes | The historical values to project forward. |
| `timeline` | Yes | Numeric dates or period numbers with a constant, nonzero step. The rows do not need to be sorted. |
| `seasonality` | No | `1` (default) detects the cycle automatically. `0` forces no seasonality. A positive whole number sets the cycle length in periods. The maximum is 8,760. |
| `data_completion` | No | `1` (default) fills a missing point with the average of its neighbors. `0` treats missing points as zeros. Up to 30 percent of the data can be missing. |
| `aggregation` | No | How to combine values that share a timestamp. `0` (default) uses AVERAGE. The other options are SUM, COUNT, COUNTA, MIN, MAX and MEDIAN. |

### Return Value

A single number: the forecast for `target_date`. The function returns `#NUM!` when the target is before the historical timeline ends, when no constant step can be found, or when `seasonality` is invalid or above 8,760. It returns `#VALUE!` when the timeline contains duplicate values and `#N/A` when `values` and `timeline` have different sizes.

## Examples

The examples use period numbers 1 to 12 in `A2:A13`, monthly sales in `B2:B13`, and the target period 13 in `A14`.

### Example 1: Basic Forecast

```excel
=FORECAST.ETS(A14, B2:B13, A2:A13)
```

**Result:** A single forecast for period 13.

Excel fits the smoothing model to the twelve values and detects any cycle automatically. The exact result depends on that fitted model, so run the formula to read it.

### Example 2: Forcing a Linear Forecast

```excel
=FORECAST.ETS(A14, B2:B13, A2:A13, 0)
```

**Result:** A forecast that follows the smoothed trend with no seasonal adjustment.

The `0` in the fourth position turns off seasonality. Use it when the months show no repeating pattern and you want the forecast to ignore any cycle Excel might find.

<!-- Image 2: Actual Versus Forecast Chart. See Images/Statistical/FORECAST.ETS.md -->

### Example 3: Handling Bad Inputs

```excel
=IFERROR(FORECAST.ETS(A14, B2:B13, A2:A13), "Check timeline")
```

**Result:** The forecast when the inputs are valid, or `Check timeline` when they are not.

The wrapper hides error codes from a report. Keep the error visible during model building, because a `#VALUE!` often points to a duplicated period.

### Example 4: Setting the Cycle Length

```excel
=FORECAST.ETS(A14, B2:B13, A2:A13, 4)
```

**Result:** A forecast that assumes a four-period cycle.

Set the cycle length yourself when you know it, such as four for quarterly data. Check the detected length first with FORECAST.ETS.SEASONALITY.

<!-- Image 3: Seasonality Setting Comparison. See Images/Statistical/FORECAST.ETS.md -->

## Story Problems

### Problem 1: Flat Seat Count

A software team tracks paid seats by month in `A1:B7`. The seat count has held at 500 for six months.

| Month | Seats |
| --- | --- |
| 1 | 500 |
| 2 | 500 |
| 3 | 500 |
| 4 | 500 |
| 5 | 500 |
| 6 | 500 |

**Task:** Forecast the seat count for month 7, which is in `A8`.

**Solution:**

```excel
=FORECAST.ETS(A8, B2:B7, A2:A7)
```

**Answer:** `500`, because smoothing a series with no change keeps its level.

### Problem 2: Choosing the Right Function

A bakery records weekly cake orders for two years. Orders peak in the weeks before each holiday, so the pattern repeats every year.

**Task:** Decide whether FORECAST.LINEAR or FORECAST.ETS fits the data better.

**Solution:** Compare the two forecasts for the next holiday week and the week after it.

**Answer:** FORECAST.ETS fits the repeating holiday peak, while FORECAST.LINEAR draws one straight line through the peaks and troughs. Use FORECAST.ETS here, and confirm the result against the holiday weeks from last year.

## Use Cases

### Monthly Sales Forecast

**Scenario:** A finance team forecasts next month's sales from three years of monthly totals.

```excel
=FORECAST.ETS(A38, B2:B37, A2:A37)
```

**Why It Works:** The 36 monthly totals and their period numbers feed the model, and cell `A38` holds the next period. The forecast updates when a new month is added to the bottom of the list and the ranges are extended.

### Seasonal Demand Planning

**Scenario:** A warehouse plans staffing from weekly order volumes that repeat every 52 weeks.

```excel
=FORECAST.ETS(H2, C2:C105, B2:B105, 52)
```

**Why It Works:** Setting the seasonality to 52 tells the model that the pattern repeats yearly in weekly data. Without that setting, the function must find the cycle itself, which can fail on short histories.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The target date is before the last timeline point, the timeline has no constant step, or seasonality is invalid. | Move the target after the history, space the timeline evenly, and use a whole number from 0 to 8,760 for seasonality. |
| `#VALUE!` | The timeline contains duplicate periods. | Remove the duplicates or set `aggregation` to combine them. |
| `#N/A` | The `values` and `timeline` ranges have different sizes. | Select ranges with the same number of rows. |
| Unexpected forecast | Excel detected a cycle that does not match the business pattern. | Check the cycle with FORECAST.ETS.SEASONALITY and set `seasonality` manually. |
| `#NAME?` | The version does not support the function. | Confirm the version, or use FORECAST.LINEAR for a linear forecast. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later (Windows and Mac) | Microsoft's page states the function is not available in Excel for the web, iOS, or Android. |
| Google Sheets | Not available | Use TREND or FORECAST.LINEAR for a linear forecast. |

## Tips and Best Practices

- Keep the timeline evenly spaced, and enter missing periods as blank cells so `data_completion` can fill them.
- Run FORECAST.ETS.SEASONALITY first to see the cycle length Excel detects, then decide whether to set `seasonality` yourself.
- Compare the result with FORECAST.LINEAR; a large gap means the history has a pattern that a straight line misses.
- Check the uncertainty with FORECAST.ETS.CONFINT before you commit a budget or stock level to the forecast.
- Use `aggregation` when several records share one date, such as multiple sales on the same day.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FORECAST](FORECAST.md) | Linear forecast that predates the ETS family. |
| [FORECAST.ETS.CONFINT](FORECAST.ETS.CONFINT.md) | Returns the confidence interval around the forecast. |
| [FORECAST.ETS.SEASONALITY](FORECAST.ETS.SEASONALITY.md) | Returns the cycle length Excel detects. |
| [FORECAST.ETS.STAT](FORECAST.ETS.STAT.md) | Returns model statistics such as the smoothing parameters and error measures. |
| [FORECAST.LINEAR](FORECAST.LINEAR.md) | Straight-line forecast for data without a seasonal pattern. |
| [TREND](TREND.md) | Returns the linear trend values for a set of known points. |

## Official Documentation

- [Microsoft Support: Forecasting functions reference](https://support.microsoft.com/en-us/excel/forecasting-functions-reference#_forecast.ets)
