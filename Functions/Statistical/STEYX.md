---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
purpose:
  - Regression
  - Statistical Analysis
use-case:
  - Ad Spend Sales Forecast
  - Delivery Time Estimates
  - Forecast Accuracy Review
related:
  - CORREL
  - FORECAST
  - FORECAST.LINEAR
  - INTERCEPT
  - LINEST
  - RSQ
  - SLOPE
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/steyx-function
  - https://support.google.com/docs/answer/3094108
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Standard Error of Estimate
tags:
  - excel
  - forecasting
  - regression
  - sheets
  - statistical
---

# STEYX

## Description

**STEYX** returns the standard error of the predicted y-value for each x in a linear regression. It measures how far the actual y-values typically sit from the straight line fitted through your data. A small result means the points hug the line and a prediction from that line is trustworthy. A large result means the line is a rough guide.

Use STEYX when you have paired data, such as monthly ad spend and monthly sales, and want to judge the reliability of a straight-line forecast. The result is in the same units as y, so a STEYX of 1.5 on sales measured in thousands means a typical prediction is off by about 1,500 units.

STEYX does not fit the line itself. Pair it with FORECAST.LINEAR to make a prediction, with SLOPE and INTERCEPT to read the line, and with RSQ to see how much of the variation the line explains. The function needs at least three pairs of values, because with fewer points the error has no degrees of freedom.

## Syntax

```excel
=STEYX(known_y's, known_x's)
```

<!-- Image 1: Known Y and Known X Ranges. See Images/Statistical/STEYX.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `known_y's` | Yes | The range of dependent values, the results you measured. |
| `known_x's` | Yes | The range of independent values, the inputs that drive the results. Must contain the same number of points as `known_y's`. |

### Return Value

A number that is zero or greater, in the units of the y-values. It returns `#N/A` when the two ranges contain a different number of data points and `#DIV/0!` when the ranges are empty or contain fewer than three data points. Text, logical values and empty cells in ranges are ignored in Excel, while zeros are included.

## Examples

### Example 1: Standard Error for Ad Spend and Sales

Ad spend in thousands is in `A2:A7` and sales in thousands is in `B2:B7`.

```excel
=STEYX(B2:B7, A2:A7)
```

**Result:** `1.503259`

A typical monthly sales prediction from this line is off by about 1.5 thousand units.

### Example 2: Predict Sales for a New Spend Level

```excel
=FORECAST.LINEAR(9, B2:B7, A2:A7)
```

**Result:** `29.7865`

The line predicts about 29.79 thousand in sales for 9 thousand in spend. Read it together with the STEYX result from Example 1, which suggests the true value could sit about 1.5 thousand above or below it.

<!-- Image 2: Regression Line and Error Band. See Images/Statistical/STEYX.md -->

### Example 3: Too Few Points

Only two pairs exist in `A2:A3` and `B2:B3`.

```excel
=STEYX(B2:B3, A2:A3)
```

**Result:** `#DIV/0!`

STEYX needs at least three points, because the error uses the number of points minus two.

### Example 4: Friendly Message When Data Is Short

```excel
=IFERROR(STEYX(B2:B3, A2:A3), "Need 3 or more points")
```

**Result:** `Need 3 or more points`

Wrapping the function in IFERROR keeps a summary sheet readable while the data set is still growing.

## Story Problems

### Problem 1: Ad Spend and Sales

A small shop tracked six months of advertising spend and sales in `A1:B7`. Both columns are in thousands.

| Spend | Sales |
| --- | --- |
| 2 | 14 |
| 3 | 17 |
| 5 | 21 |
| 7 | 24 |
| 8 | 30 |
| 10 | 31 |

**Task:** Find the standard error of the sales prediction, then predict sales for a spend of 9.

**Solution:**

```excel
=STEYX(B2:B7, A2:A7)
```

**Answer:** `1.503259` thousand units for the standard error. The line predicts about `29.7865` thousand in sales at 9 thousand in spend, found with `=FORECAST.LINEAR(9, B2:B7, A2:A7)`.

### Problem 2: Delivery Distance and Time

A courier logged distance in kilometres and travel time in minutes for five deliveries in `A1:B6`.

| Distance (km) | Minutes |
| --- | --- |
| 3 | 18 |
| 5 | 24 |
| 8 | 31 |
| 10 | 35 |
| 12 | 44 |

**Task:** Find how far the minute predictions typically miss.

**Solution:**

```excel
=STEYX(B2:B6, A2:A6)
```

**Answer:** `1.536523` minutes. The fitted line is about 9.71 minutes plus 2.72 minutes per kilometre, so a 15 km trip is predicted near 50.5 minutes.

<!-- Image 3: Delivery Data Worksheet. See Images/Statistical/STEYX.md -->

## Use Cases

### Ad Spend Sales Forecast

**Scenario:** A marketing lead wants to know whether next quarter's sales forecast from a spend plan is reliable enough to set a budget.

```excel
=STEYX(Sales[Revenue], Sales[Spend])
```

**Why It Works:** The standard error sits next to the forecast so the team can see the likely range. A large value says to plan for a wide band of outcomes.

### Delivery Time Estimates

**Scenario:** A dispatch team quotes delivery windows from distance and wants the window width to reflect real scatter.

```excel
=FORECAST.LINEAR(D2, Trips[Minutes], Trips[Km]) + 2 * STEYX(Trips[Minutes], Trips[Km])
```

**Why It Works:** Adding twice the standard error to the predicted time gives a rough upper bound that covers most trips. Check the result against past trips before promising customers a window.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The two ranges contain different numbers of points. | Make both ranges the same length and line up the rows. |
| `#DIV/0!` | Fewer than three points, or empty ranges. | Collect at least three pairs of values. |
| Unexpected result | A text entry sits in one range and is ignored, so the pairs no longer match. | Check that each row has a number in both columns. |
| Misleading forecast | The data is not roughly a straight line. | Plot the points first, and use a different method if the pattern curves. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions | Returns `#N/A` for unequal ranges. Logical values and empty cells in ranges are ignored, zeros are included. |
| Google Sheets | Available | Ignores text in the value arguments. The documentation does not list the error conditions, so test unequal ranges before relying on them. |

## Tips and Best Practices

- Plot the points as a scatter chart before you trust a straight-line standard error.
- Keep the x-range and y-range on the same rows so each pair describes one period or one job.
- Report STEYX next to the forecast so readers see the likely error, not only the prediction.
- Use RSQ to check how much of the variation the line explains before you rely on it.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FORECAST.LINEAR](FORECAST.LINEAR.md) | Predicts a y-value from an x-value on the same line that STEYX measures. |
| [FORECAST](FORECAST.md) | Older form of the same linear prediction. |
| [SLOPE](SLOPE.md) | Returns the slope of the line that STEYX describes. |
| [INTERCEPT](INTERCEPT.md) | Returns where the line crosses the y-axis. |
| [RSQ](RSQ.md) | Shows how much of the y-variation the line explains. |
| [CORREL](CORREL.md) | Measures the strength and direction of the linear relationship. |
| [LINEST](LINEST.md) | Returns the full regression statistics, including the standard errors, in one array. |

## Official Documentation

- [Microsoft Support: STEYX function](https://support.microsoft.com/en-us/excel/functions/steyx-function)
- [Google Docs Editors Help: STEYX](https://support.google.com/docs/answer/3094108)
