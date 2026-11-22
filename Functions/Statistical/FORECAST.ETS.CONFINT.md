---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
purpose:
  - Forecasting
  - Statistical Analysis
use-case:
  - Budget Variance Bands
  - Inventory Safety Levels
related:
  - CONFIDENCE.NORM
  - FORECAST.ETS
  - FORECAST.ETS.SEASONALITY
  - FORECAST.ETS.STAT
  - FORECAST.LINEAR
  - NORM.S.INV
level: 4
source:
  - https://support.microsoft.com/en-us/excel/forecasting-functions-reference#_forecast.ets.confint
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - confidence-interval
  - excel
  - forecasting
  - time-series
---

# FORECAST.ETS.CONFINT

## Description

**FORECAST.ETS.CONFINT** returns a confidence interval around the FORECAST.ETS prediction for a target date. The result is a radius, the distance from the forecast to each end of the interval. Microsoft describes the interval as the range where 95 percent of future points are expected to fall, assuming a normal distribution. A smaller radius means the forecast for that particular point is more certain.

Add the radius to the forecast for the upper bound and subtract it for the lower bound. The same historical data, timeline and seasonality settings must be used for both the forecast and the interval, or the bounds will not match. Use the function when a planner needs a range rather than a single number, such as a stock level that must cover demand most of the time.

The interval is wider for target dates further from the historical data, so a forecast for next month usually has a tighter band than one for next year. Microsoft's support page states that the function is not available in Excel for the web, iOS, or Android, and Google Sheets does not offer it. Check the platform before you share the workbook.

## Syntax

```excel
=FORECAST.ETS.CONFINT(target_date, values, timeline, [confidence_level], [seasonality], [data_completion], [aggregation])
```

<!-- Image 1: Interval Arguments Layout. See Images/Statistical/FORECAST.ETS.CONFINT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `target_date` | Yes | The date or period number to predict. A target before the end of the historical timeline returns `#NUM!`. |
| `values` | Yes | The historical values used for the forecast. |
| `timeline` | Yes | Numeric dates or period numbers with a constant, nonzero step. The rows do not need to be sorted, because the function sorts them internally. |
| `confidence_level` | No | A value greater than 0 and less than 1. The default is 0.95 (95 percent). Values of 0, 1 or outside that range return `#NUM!`. |
| `seasonality` | No | `1` (default) detects the cycle automatically. `0` forces no seasonality. A positive whole number sets the cycle length in periods. The maximum is 8,760. |
| `data_completion` | No | `1` (default) fills a missing point with the average of its neighbors. `0` treats missing points as zeros. Up to 30 percent of the data can be missing. |
| `aggregation` | No | How to combine values that share a timestamp. `0` (default) uses AVERAGE. The other options are SUM, COUNT, COUNTA, MIN, MAX and MEDIAN. |

### Return Value

A single positive number: the radius of the confidence interval for `target_date`. The forecast from FORECAST.ETS plus or minus this radius gives the upper and lower bounds. The function returns `#NUM!` when the target is before the historical timeline ends, when the confidence level is not between 0 and 1, when no constant step can be found, or when seasonality is invalid. It returns `#VALUE!` for duplicate timeline values and `#N/A` when `values` and `timeline` differ in size.

## Examples

The examples use period numbers 1 to 12 in `A2:A13`, monthly sales in `B2:B13`, and the target period 13 in `A14`.

### Example 1: Default 95 Percent Radius

```excel
=FORECAST.ETS.CONFINT(A14, B2:B13, A2:A13)
```

**Result:** A positive number, the radius for period 13 at the default 95 percent confidence level.

Add this value to FORECAST.ETS for the same inputs to get the upper bound. The exact radius depends on how well the fitted model matches the history.

### Example 2: A Narrower 90 Percent Band

```excel
=FORECAST.ETS.CONFINT(A14, B2:B13, A2:A13, 0.9)
```

**Result:** A smaller radius than Example 1 for the same data.

A lower confidence level needs a narrower band, so this radius is smaller than the 95 percent result. Use it when a tighter planning range is acceptable.

### Example 3: Building the Lower Bound

```excel
=FORECAST.ETS(A14, B2:B13, A2:A13) - FORECAST.ETS.CONFINT(A14, B2:B13, A2:A13)
```

**Result:** The lower bound of the 95 percent interval for period 13.

Use the same arguments in both functions. A mismatch, such as different seasonality values, produces bounds that do not belong to the same model.

<!-- Image 2: Forecast Band Chart. See Images/Statistical/FORECAST.ETS.CONFINT.md -->

### Example 4: Linear Interval With No Seasonality

```excel
=FORECAST.ETS.CONFINT(A14, B2:B13, A2:A13, 0.95, 0)
```

**Result:** A radius for a model that assumes no seasonal pattern.

Setting seasonality to `0` in the fifth position removes the cycle from the model. Compare this result with Example 1 to see how much the detected pattern changes the uncertainty.

## Story Problems

### Problem 1: Narrower Planning Range

A planner forecasts monthly orders in `A2:B13` and compares two confidence levels for period 13 in `A14`.

| Period | Orders |
| --- | --- |
| 1 | 210 |
| 2 | 225 |
| 3 | 218 |
| 4 | 240 |
| 5 | 252 |
| 6 | 247 |
| 7 | 265 |
| 8 | 271 |
| 9 | 268 |
| 10 | 290 |
| 11 | 298 |
| 12 | 305 |

**Task:** Decide whether a 90 percent band or a 95 percent band is narrower for period 13.

**Solution:**

```excel
=FORECAST.ETS.CONFINT(A14, B2:B13, A2:A13, 0.9)
```

**Answer:** The 90 percent radius is smaller than the 95 percent radius for the same data, because a lower confidence level allows a narrower band.

<!-- Image 3: Confidence Level Comparison. See Images/Statistical/FORECAST.ETS.CONFINT.md -->

### Problem 2: Invalid Confidence Input

A dashboard lets a user type a confidence level in `D1`. The user enters 1, which means 100 percent.

**Task:** Predict what the interval formula returns when `D1` holds 1.

**Solution:**

```excel
=FORECAST.ETS.CONFINT(A14, B2:B13, A2:A13, D1)
```

**Answer:** `#NUM!`, because the confidence level must be greater than 0 and less than 1.

## Use Cases

### Inventory Safety Levels

**Scenario:** A distributor sets its reorder level at the upper bound of expected demand for the next month.

```excel
=FORECAST.ETS(A38, B2:B37, A2:A37) + FORECAST.ETS.CONFINT(A38, B2:B37, A2:A37)
```

**Why It Works:** The formula adds the 95 percent radius to the forecast, so the reorder level covers most expected demand. Extend the ranges when a new month is added to the history.

### Budget Variance Bands

**Scenario:** A department head reviews a monthly cost forecast with a range instead of one number.

```excel
=FORECAST.ETS.CONFINT(A14, B2:B13, A2:A13, 0.8)
```

**Why It Works:** An 80 percent radius gives a narrower band for the review meeting. Show the band next to the forecast so the reader sees both the point estimate and its spread.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The confidence level is 0, 1 or outside the range, the target is before the history ends, or the step is not constant. | Use a level above 0 and below 1, move the target forward, and space the timeline evenly. |
| `#VALUE!` | The timeline contains duplicate periods. | Remove the duplicates or set `aggregation` to combine them. |
| `#N/A` | The `values` and `timeline` ranges have different sizes. | Select ranges with the same number of rows. |
| Bounds do not match the forecast | The forecast and interval use different arguments. | Copy the same arguments into both formulas. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later (Windows and Mac) | Microsoft's page states the function is not available in Excel for the web, iOS, or Android. |
| Google Sheets | Not available | Use FORECAST or FORECAST.LINEAR for the point forecast only. |

## Tips and Best Practices

- Use the same `timeline`, `values` and seasonality settings in every forecast and interval formula so the bounds describe one model.
- Set the confidence level to match the cost of missing the target: a higher level gives a safer but wider range.
- Read the radius as a width for one target date; intervals for different dates are not interchangeable.
- Check the forecast with FORECAST.ETS.SEASONALITY before trusting a band built on an automatically detected cycle.
- Store the confidence level in one labeled input cell so reviewers can change it without editing the formulas.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FORECAST.ETS](FORECAST.ETS.md) | Returns the point forecast that the radius is built around. |
| [FORECAST.ETS.SEASONALITY](FORECAST.ETS.SEASONALITY.md) | Returns the cycle length the model uses. |
| [FORECAST.ETS.STAT](FORECAST.ETS.STAT.md) | Returns model statistics such as error measures. |
| [FORECAST.LINEAR](FORECAST.LINEAR.md) | Straight-line forecast without an interval. |
| [CONFIDENCE.NORM](CONFIDENCE.NORM.md) | Returns a normal-distribution confidence radius for a sample mean, not a time series forecast. |
| [NORM.S.INV](NORM.S.INV.md) | Returns the z value for a probability, a building block for manual intervals. |

## Official Documentation

- [Microsoft Support: Forecasting functions reference](https://support.microsoft.com/en-us/excel/forecasting-functions-reference#_forecast.ets.confint)
