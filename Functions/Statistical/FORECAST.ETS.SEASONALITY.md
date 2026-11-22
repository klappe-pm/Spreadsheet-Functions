---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
purpose:
  - Forecasting
  - Statistical Analysis
use-case:
  - Quarterly Sales Cycle Check
  - Retail Demand Pattern Review
related:
  - FORECAST.ETS
  - FORECAST.ETS.CONFINT
  - FORECAST.ETS.STAT
  - FORECAST.LINEAR
  - TREND
level: 5
source:
  - https://support.microsoft.com/en-us/excel/forecasting-functions-reference#_forecast.ets.seasonality
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - excel
  - forecasting
  - seasonality
  - time-series
---

# FORECAST.ETS.SEASONALITY

## Description

**FORECAST.ETS.SEASONALITY** returns the length of the repeating pattern that Excel detects in a time series. The result is a count of periods, such as 4 for quarterly data that repeats every four quarters, or 0 when no repeating pattern is found. It reports the same seasonality that FORECAST.ETS uses for the same inputs, so you can run it before a forecast to confirm what the model will assume.

Use it as a check, not as the forecast itself. Compare the detected length with the cycle you expect from the business, such as a yearly holiday peak in monthly data. If the two disagree, set the `seasonality` argument of FORECAST.ETS yourself.

The function accepts missing data and aggregated timestamps in the same way as FORECAST.ETS. Microsoft's support page states that the function is not available in Excel for the web, iOS, or Android, and Google Sheets does not offer it.

## Syntax

```excel
=FORECAST.ETS.SEASONALITY(values, timeline, [data_completion], [aggregation])
```

<!-- Image 1: Seasonality Arguments Layout. See Images/Statistical/FORECAST.ETS.SEASONALITY.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `values` | Yes | The historical values to analyze. |
| `timeline` | Yes | Numeric dates or period numbers with a constant, nonzero step. The rows do not need to be sorted. |
| `data_completion` | No | `1` (default) fills a missing point with the average of its neighbors. `0` treats missing points as zeros. Up to 30 percent of the data can be missing. |
| `aggregation` | No | How to combine values that share a timestamp. `0` (default) uses AVERAGE. The other options are SUM, COUNT, COUNTA, MIN, MAX and MEDIAN. |

### Return Value

A whole number: the number of periods in the detected seasonal cycle. The function returns `#NUM!` when no constant step can be found in the timeline. It returns `#VALUE!` when the timeline contains duplicate values and `#N/A` when `values` and `timeline` differ in size.

## Examples

The examples use period numbers 1 to 16 in `A2:A17` and quarterly sales in `B2:B17`. Sixteen quarters cover four years.

### Example 1: Detecting the Cycle

```excel
=FORECAST.ETS.SEASONALITY(B2:B17, A2:A17)
```

**Result:** The number of quarters in the cycle Excel detects, for example `4` for a yearly pattern.

The result describes the history only. It does not forecast any value. Read it before you choose the `seasonality` argument of FORECAST.ETS.

<!-- Image 2: Quarterly Pattern Chart. See Images/Statistical/FORECAST.ETS.SEASONALITY.md -->

### Example 2: Using the Result in a Forecast

```excel
=FORECAST.ETS(A18, B2:B17, A2:A17, FORECAST.ETS.SEASONALITY(B2:B17, A2:A17))
```

**Result:** A forecast for period 18 that uses the detected cycle length.

This formula passes the detected length straight into FORECAST.ETS. Use it when you trust the detection and want the forecast to follow whatever pattern the function finds.

### Example 3: Flagging an Unexpected Cycle

```excel
=IF(FORECAST.ETS.SEASONALITY(B2:B17, A2:A17) = 4, "Yearly cycle confirmed", "Review the cycle")
```

**Result:** `Yearly cycle confirmed` when the detected length is 4, or `Review the cycle` for any other length.

Use this flag in a model review so a reader sees when the detected cycle differs from the one the business expects.

### Example 4: Treating Missing Data as Zero

```excel
=FORECAST.ETS.SEASONALITY(B2:B17, A2:A17, 0)
```

**Result:** The cycle length when missing points count as zeros.

Use `0` only when a blank truly means zero sales. In most business data, a blank means no record, so the default fill of `1` is usually the better choice.

## Story Problems

### Problem 1: Quarterly Cycle

A retailer records quarterly sales for four years. Each year follows the same pattern: a low first quarter, a rise in the second, and a peak in the fourth.

| Quarter Number | Sales |
| --- | --- |
| 1 | 180 |
| 2 | 210 |
| 3 | 205 |
| 4 | 260 |
| 5 | 185 |
| 6 | 215 |
| 7 | 210 |
| 8 | 265 |

**Task:** Find the seasonal cycle length that Excel detects for the quarterly history in `A2:B9`.

**Solution:**

```excel
=FORECAST.ETS.SEASONALITY(B2:B9, A2:A9)
```

**Answer:** Excel should report a cycle of 4 quarters, because the pattern repeats every four rows. Run the formula in your version to confirm the reported value before you set `seasonality` manually.

<!-- Image 3: Cycle Check Result. See Images/Statistical/FORECAST.ETS.SEASONALITY.md -->

### Problem 2: Checking a Surprising Cycle

A planner runs the function on the same quarterly history and gets a detected length of 6, although the business sees a yearly cycle of 4 quarters.

**Task:** Decide which seasonality value to pass to FORECAST.ETS.

**Solution:**

```excel
=FORECAST.ETS(A18, B2:B9, A2:A9, 4)
```

**Answer:** Pass 4 for the yearly cycle, because the planner sets the seasonality manually when the detected length does not match the business pattern. Confirm the forecast against last year's results before you use it.

## Use Cases

### Quarterly Sales Cycle Check

**Scenario:** A sales operations lead confirms that quarterly revenue repeats yearly before setting a forecast target.

```excel
=FORECAST.ETS.SEASONALITY(Revenue_Q, Period_Q)
```

**Why It Works:** Named ranges `Revenue_Q` and `Period_Q` keep the formula readable. A result of 4 confirms the yearly cycle, and any other result is a prompt to review the data.

### Retail Demand Pattern Review

**Scenario:** A store manager checks whether weekly foot traffic follows a 52-week cycle.

```excel
=FORECAST.ETS.SEASONALITY(C2:C105, B2:B105)
```

**Why It Works:** Two years of weekly data give the model enough history to test a yearly cycle. Compare the result with the expected 52; a different value means the planning model should use the detected cycle only after the manager reviews it.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The timeline has no constant step. | Use evenly spaced periods, and enter missing periods as blank values. |
| `#VALUE!` | The timeline contains duplicate periods. | Remove the duplicates or set `aggregation` to combine them. |
| `#N/A` | The `values` and `timeline` ranges have different sizes. | Select ranges with the same number of rows. |
| Unexpected cycle length | The history is short or has an irregular pattern. | Add more periods or set `seasonality` manually. |
| `#NAME?` | The version does not support the function. | Confirm the Excel version, or use FORECAST.LINEAR for a non-seasonal forecast. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later (Windows and Mac) | Microsoft's page states the function is not available in Excel for the web, iOS, or Android. |
| Google Sheets | Not available | Use TREND or FORECAST.LINEAR for a linear forecast without a detected cycle. |

## Tips and Best Practices

- Run this function before FORECAST.ETS when the cycle length matters to the decision.
- Use at least two full cycles of history; a single year of quarterly data gives the model little to compare.
- Keep the timeline in period numbers rather than dates with irregular gaps, so the constant-step rule holds.
- Record the detected length next to the forecast so reviewers know which cycle the model assumed.
- Re-run the check whenever new periods are added to the history.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FORECAST.ETS](FORECAST.ETS.md) | Uses the same detected seasonality to build the forecast. |
| [FORECAST.ETS.CONFINT](FORECAST.ETS.CONFINT.md) | Builds the confidence interval using the same model. |
| [FORECAST.ETS.STAT](FORECAST.ETS.STAT.md) | Returns model statistics for the same fit. |
| [FORECAST.LINEAR](FORECAST.LINEAR.md) | Straight-line forecast for data without a seasonal pattern. |
| [TREND](TREND.md) | Returns linear trend values for known points. |

## Official Documentation

- [Microsoft Support: Forecasting functions reference](https://support.microsoft.com/en-us/excel/forecasting-functions-reference#_forecast.ets.seasonality)
