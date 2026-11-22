---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
purpose:
  - Forecasting
  - Statistical Analysis
use-case:
  - Forecast Error Tracking
  - Model Parameter Review
related:
  - FORECAST.ETS
  - FORECAST.ETS.CONFINT
  - FORECAST.ETS.SEASONALITY
  - FORECAST.LINEAR
  - STEYX
level: 5
source:
  - https://support.microsoft.com/en-us/excel/forecasting-functions-reference#_forecast.ets.stat
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - excel
  - forecasting
  - model-accuracy
  - time-series
---

# FORECAST.ETS.STAT

## Description

**FORECAST.ETS.STAT** returns one statistic from the Exponential Smoothing (ETS) model that Excel fits to a time series. The statistic is chosen by a number from 1 to 8. The statistics cover the smoothing parameters that the model learned, error measures that show how closely the model fits the history, and the timeline step that Excel detected.

Use it when a reviewer needs to see inside the model, for example to compare two forecasts for the same history by their error measures. The function does not return a forecast; use FORECAST.ETS for that. Run it with the same `values`, `timeline` and seasonality settings as the forecast, so the statistic describes the model that produced the forecast.

Microsoft's support page lists the eight statistics in this order: alpha, beta, gamma, MASE, SMAPE, MAE, RMSE and the detected step size. The page does not state the numbering in a table, so confirm the mapping in your version before you rely on a specific number. Microsoft also states that the function is not available in Excel for the web, iOS, or Android. Google Sheets does not offer it.

## Syntax

```excel
=FORECAST.ETS.STAT(values, timeline, statistic_type, [seasonality], [data_completion], [aggregation])
```

<!-- Image 1: Statistic Type Argument. See Images/Statistical/FORECAST.ETS.STAT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `values` | Yes | The historical values the model is fitted to. |
| `timeline` | Yes | Numeric dates or period numbers with a constant, nonzero step. The rows do not need to be sorted. |
| `statistic_type` | Yes | A whole number from 1 to 8 that selects the statistic to return. The page lists the statistics in this order: alpha, beta, gamma, MASE, SMAPE, MAE, RMSE and step size detected. |
| `seasonality` | No | `1` (default) detects the cycle automatically. `0` forces no seasonality. A positive whole number sets the cycle length in periods. The maximum is 8,760. |
| `data_completion` | No | `1` (default) fills a missing point with the average of its neighbors. `0` treats missing points as zeros. Up to 30 percent of the data can be missing. |
| `aggregation` | No | How to combine values that share a timestamp. `0` (default) uses AVERAGE. The other options are SUM, COUNT, COUNTA, MIN, MAX and MEDIAN. |

### Return Value

A single number for the selected statistic. Smoothing parameters and error measures are numbers that describe the fitted model, not forecast values. The function returns `#NUM!` when no constant step can be found, when the step is zero, or when `seasonality` is invalid or above 8,760. It returns `#VALUE!` for duplicate timeline values and `#N/A` when `values` and `timeline` differ in size.

## Examples

The examples use period numbers 1 to 12 in `A2:A13` and monthly sales in `B2:B13`.

### Example 1: Reading the First Smoothing Parameter

```excel
=FORECAST.ETS.STAT(B2:B13, A2:A13, 1)
```

**Result:** The value of the first statistic in the page's list, alpha.

Alpha is the smoothing parameter for the level of the series. Read it as a model setting, not as a sales figure.

### Example 2: Comparing Error Measures

```excel
=FORECAST.ETS.STAT(B2:B13, A2:A13, 4)
```

**Result:** The fourth statistic in the page's list, MASE.

Error measures are compared across models fitted to the same history. A model with a smaller error value fits the history more closely.

<!-- Image 2: Model Comparison Table. See Images/Statistical/FORECAST.ETS.STAT.md -->

### Example 3: Wrapping Errors for a Report

```excel
=IFERROR(FORECAST.ETS.STAT(B2:B13, A2:A13, 7), "Check timeline")
```

**Result:** The seventh statistic in the page's list, RMSE, or `Check timeline` when the inputs are not valid.

The wrapper keeps a model review sheet readable when one input changes. Remove it while building the model so errors stay visible.

### Example 4: Checking the Detected Step

```excel
=FORECAST.ETS.STAT(B2:B13, A2:A13, 8)
```

**Result:** The step size Excel detects in the timeline.

Use it to confirm that the timeline has the step you expect. A step that differs from the business calendar points to a mistake in the period numbers.

## Story Problems

### Problem 1: Choosing Between Two Models

A planner fits two models to the same twelve months of sales. One uses automatic seasonality and the other uses no seasonality. The planner compares the RMSE statistic for each model in cells `E1` and `E2`.

| Model | Seasonality Setting | RMSE Formula |
| --- | --- | --- |
| Automatic | 1 | `=FORECAST.ETS.STAT(B2:B13, A2:A13, 7, 1)` |
| No Seasonality | 0 | `=FORECAST.ETS.STAT(B2:B13, A2:A13, 7, 0)` |

**Task:** Decide which model fits the history more closely.

**Solution:** Compare the two results in `E1` and `E2`, and keep the model with the smaller RMSE value.

**Answer:** The model with the smaller RMSE fits the history more closely. Read the two results in your version and choose that model, because the exact values depend on the fitted data.

### Problem 2: Confirming the Timeline Step

A data analyst loads monthly period numbers 1 to 12 in `A2:A13` and wants to confirm the step before forecasting.

**Task:** Return the step size that Excel detects.

**Solution:**

```excel
=FORECAST.ETS.STAT(B2:B13, A2:A13, 8)
```

**Answer:** `1`, because the period numbers increase by one each row.

## Use Cases

### Forecast Error Tracking

**Scenario:** A finance team records the error measure for each monthly forecast to see whether accuracy is improving.

```excel
=FORECAST.ETS.STAT(Sales_Hist, Period_Hist, 4, 1)
```

**Why It Works:** Logging the MASE value each month shows whether the model is getting closer to the actuals. Named ranges keep the formula readable when the history grows.

<!-- Image 3: Error Tracking Chart. See Images/Statistical/FORECAST.ETS.STAT.md -->

### Model Parameter Review

**Scenario:** A planning lead asks why a forecast reacts quickly to recent changes.

```excel
=FORECAST.ETS.STAT(Sales_Hist, Period_Hist, 1, 1)
```

**Why It Works:** The alpha value shows how strongly the level follows recent periods. Pair it with the beta value in the next row to see how the trend is weighted.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The timeline has no constant step, the step is zero, or seasonality is invalid. | Space the timeline evenly and use a whole number from 0 to 8,760 for seasonality. |
| `#VALUE!` | The timeline contains duplicate periods. | Remove the duplicates or set `aggregation` to combine them. |
| `#N/A` | The `values` and `timeline` ranges have different sizes. | Select ranges with the same number of rows. |
| Wrong statistic | The `statistic_type` number does not match the statistic you intended. | Check the page's list order in your version, and label the cell with the statistic name. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later (Windows and Mac) | Microsoft's page states the function is not available in Excel for the web, iOS, or Android. |
| Google Sheets | Not available | No direct equivalent. Use FORECAST.LINEAR and STEYX to measure a straight-line fit. |

## Tips and Best Practices

- Label every statistic cell with its name, because the numbers 1 to 8 are easy to mix up.
- Use the same `values`, `timeline` and seasonality arguments as the forecast so the statistic describes that forecast.
- Compare error measures only for models fitted to the same history.
- Store the statistic numbers in a labeled table so reviewers can see which model each value came from.
- Read the step size statistic first when a new data feed starts, because an irregular step breaks every model that uses the timeline.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FORECAST.ETS](FORECAST.ETS.md) | Returns the forecast that these statistics describe. |
| [FORECAST.ETS.CONFINT](FORECAST.ETS.CONFINT.md) | Returns the interval radius for the same model. |
| [FORECAST.ETS.SEASONALITY](FORECAST.ETS.SEASONALITY.md) | Returns the cycle length the model uses. |
| [FORECAST.LINEAR](FORECAST.LINEAR.md) | Straight-line forecast for comparison. |
| [STEYX](STEYX.md) | Returns the standard error of a straight-line regression, a simpler error measure. |

## Official Documentation

- [Microsoft Support: Forecasting functions reference](https://support.microsoft.com/en-us/excel/forecasting-functions-reference#_forecast.ets.stat)
