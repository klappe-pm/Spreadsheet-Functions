---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
purpose:
  - Regression
  - Statistical Analysis
use-case:
  - Calibration Offset
  - Fixed Cost Estimate
  - Sales Baseline Forecast
related:
  - FORECAST.LINEAR
  - LINEST
  - RSQ
  - SLOPE
  - STEYX
  - TREND
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/intercept-function
  - https://support.google.com/docs/answer/3093632
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Regression Intercept
  - Y Intercept
tags:
  - excel
  - linear-regression
  - regression
  - sheets
  - statistical
---

# INTERCEPT

## Description

**INTERCEPT** fits a straight line through a set of x and y values using least squares, then returns the point where that line crosses the vertical y-axis. That point is the predicted y value when x is 0. The result is the baseline: the part of the outcome that does not change as x changes.

Use INTERCEPT when you need the starting value of a linear relationship, such as a fixed fee in a cost curve, a sensor offset in a calibration table, or the sales level a trend would show with no marketing spend. Pair it with SLOPE, which returns the rate of change, to describe the full line. The two together give the equation y = intercept + slope × x.

INTERCEPT only describes a straight-line trend. If the data curves, the intercept of the best straight line can be a poor description of the real starting value, so check the data with a chart first. If you need the whole fitted line, or several x variables at once, use LINEST. If you need the predicted y for a specific x, use FORECAST.LINEAR.

## Syntax

```excel
=INTERCEPT(known_y's, known_x's)
```

<!-- Image 1: Regression Line and Intercept Point. See Images/Statistical/INTERCEPT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `known_y's` | Yes | The dependent values, the outcome you measure. Enter a range, an array or a list of numbers. |
| `known_x's` | Yes | The independent values that the outcome depends on. It must contain the same number of data points as `known_y's`. |

The order matters: the y values come first and the x values second. Swapping them returns a different number without an error.

### Return Value

A number: the y value where the best-fit line crosses the y-axis. It returns `#N/A` when the two arrays are empty or contain a different number of data points. It returns `#DIV/0!` when every x value is the same, because the slope cannot be calculated.

## Examples

The examples use this data in `A1:B6`, with a header row in row 1.

| Sales | Ad Spend |
| --- | --- |
| 7 | 2 |
| 11 | 4 |
| 13 | 6 |
| 19 | 8 |
| 21 | 10 |

### Example 1: Basic Intercept

```excel
=INTERCEPT(A2:A6, B2:B6)
```

**Result:** `3.4`

The best-fit line is y = 3.4 + 1.8x. With no advertising spend, the trend predicts sales of 3.4.

### Example 2: Predicting a Value From the Intercept and Slope

```excel
=INTERCEPT(A2:A6, B2:B6) + SLOPE(A2:A6, B2:B6) * 12
```

**Result:** `25`

The slope is 1.8, so 1.8 × 12 = 21.6 is added to the intercept of 3.4. The same value comes from `=FORECAST.LINEAR(12, A2:A6, B2:B6)`.

<!-- Image 2: Predicting Sales at Ten Units of Spend. See Images/Statistical/INTERCEPT.md -->

### Example 3: Handling Mismatched Ranges

```excel
=IFERROR(INTERCEPT(A2:A6, B2:B5), "Check that both ranges have the same length")
```

**Result:** `Check that both ranges have the same length`

`B2:B5` has four values and `A2:A6` has five, so INTERCEPT returns `#N/A`. IFERROR replaces that error with a message that tells the user what to fix.

## Story Problems

### Problem 1: Support Staff and Ticket Volume

A help desk records how many agents were on shift and how many tickets the team closed each day. Staff counts are in `B2:B6` and tickets closed are in `C2:C6`.

| Day | Agents On Shift | Tickets Closed |
| --- | --- | --- |
| Mon | 2 | 9 |
| Tue | 3 | 12 |
| Wed | 4 | 14 |
| Thu | 5 | 18 |
| Fri | 6 | 19 |

**Task:** Find the number of tickets closed that does not depend on staffing, the baseline the team closes even with no extra agents.

**Solution:**

```excel
=INTERCEPT(C2:C6, B2:B6)
```

**Answer:** `4` tickets per day. The fitted slope is 2.6 tickets per agent, and the intercept is the baseline from automated replies and self-service answers.

<!-- Image 3: Support Staff and Ticket Volume. See Images/Statistical/INTERCEPT.md -->

### Problem 2: Fixed Fee in a Shipping Quote

A courier charges a base fee plus a charge per kilogram. The table lists the weight and the total price of five parcels.

| Parcel | Weight (kg) | Price |
| --- | --- | --- |
| A | 1 | 6.50 |
| B | 2 | 8.00 |
| C | 3 | 9.50 |
| D | 4 | 11.00 |
| E | 5 | 12.50 |

**Task:** Find the fixed fee that applies to every parcel, regardless of weight.

**Solution:**

```excel
=INTERCEPT(C2:C6, B2:B6)
```

**Answer:** `5`, so the fixed fee is 5.00. The slope is 1.50 per kilogram, which the SLOPE function returns for the same ranges.

## Use Cases

### Calibration Offset

**Scenario:** A lab compares a temperature sensor with a reference thermometer at several set points. Readings are in `D2:D8`, and reference values are in `E2:E8`.

```excel
=INTERCEPT(D2:D8, E2:E8)
```

**Why It Works:** The intercept shows the constant offset of the sensor when the reference is 0 degrees. Combine it with SLOPE to correct each new reading.

### Fixed Cost Estimate

**Scenario:** A shop tracks total monthly cost and units produced for the last year. The fixed cost is the part of the bill that does not change with output.

```excel
=INTERCEPT(Costs[Total Cost], Costs[Units Produced])
```

**Why It Works:** Structured references keep the formula correct as new months are added. The result is the monthly fixed cost, which feeds break-even planning.

### Sales Baseline Forecast

**Scenario:** A marketing team wants to know what sales would look like with no advertising, so it can measure the lift from campaigns.

```excel
=INTERCEPT(Sales!B2:B53, Sales!C2:C53)
```

**Why It Works:** The intercept is the expected weekly sales with no spend. Subtracting it from actual sales shows how much each campaign added.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The two ranges have different numbers of values, or one is empty. | Make both ranges the same length and check for missing rows. |
| `#DIV/0!` | Every x value is the same, so the slope has no spread to measure. | Use x values that vary, or use a different method for a single x value. |
| Wrong intercept | The y and x ranges were swapped. | Put the outcome in known_y's and the driver in known_x's. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions, including Excel for the web | Text, logical values and empty cells in a range are ignored. Mismatched lengths return `#N/A`. |
| Google Sheets | Available | Same two arguments in the same order. Text in the value ranges is ignored. The help page does not list the mismatched-length error, so check that ranges match. |

## Tips and Best Practices

- Plot the data as a scatter chart first. The intercept only means something when a straight line describes the pattern.
- Use INTERCEPT and SLOPE together, and read the pair as the equation of the line.
- Keep the y and x ranges the same size and aligned row by row, so each pair belongs to one observation.
- Extrapolating far beyond the observed x values, including x equal to 0 when no data sits near 0, can produce an intercept that is not realistic.
- Use LINEST when you need the intercept with fit statistics such as R squared and standard errors.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SLOPE](SLOPE.md) | Returns the rate of change of the same fitted line. |
| [FORECAST.LINEAR](FORECAST.LINEAR.md) | Predicts y for a chosen x using the same line. |
| [LINEST](LINEST.md) | Returns the slope, intercept and fit statistics together. |
| [RSQ](RSQ.md) | Measures how closely the line fits the data. |
| [STEYX](STEYX.md) | Returns the standard error of the predicted y values. |
| [TREND](TREND.md) | Returns predicted y values for several x values at once. |

## Official Documentation

- [Microsoft Support: INTERCEPT function](https://support.microsoft.com/en-us/excel/functions/intercept-function)
- [Google Docs Editors Help: INTERCEPT](https://support.google.com/docs/answer/3093632)
