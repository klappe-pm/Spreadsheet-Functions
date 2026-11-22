---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
purpose:
  - Forecasting
  - Regression
use-case:
  - Adoption Curve Fitting
  - Cost Escalation Trends
  - Referral Growth Modeling
related:
  - GROWTH
  - LINEST
  - LN
  - RSQ
  - TREND
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/logest-function
  - https://support.google.com/docs/answer/3094251
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Exponential Coefficients
  - Exponential Curve Fit
tags:
  - array-formula
  - excel
  - exponential-regression
  - regression
  - sheets
---

# LOGEST

## Description

**LOGEST** fits an exponential curve, y = b × m^x, to known x and y values using the least-squares method. It returns the growth factor m and the starting coefficient b. A growth factor of 1.10 means each step multiplies the value by 1.10, which is 10 percent growth per step.

Use LOGEST when the data grows or shrinks by a similar percentage each period, such as referral sign-ups, repair costs that rise each year, or a population that doubles at a steady pace. If the data rises by a similar amount each period instead, use LINEST, which fits a straight line.

LOGEST returns the coefficients, not the predicted values. To predict y for new x values, use GROWTH, which takes the same known values and adds the new x values to predict. The output has the same layout as LINEST: with one x variable it returns m and then b, and with the statistics option set to TRUE it adds the regression statistics.

## Syntax

```excel
=LOGEST(known_y's, [known_x's], [const], [stats])
```

<!-- Image 1: Exponential Curve and Its Coefficients. See Images/Statistical/LOGEST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `known_y's` | Yes | The y values of the relationship y = b × m^x. Use positive numbers. |
| `known_x's` | No | The x values. If omitted, the values 1, 2, 3 and so on are used. With several x variables, `known_y's` must be a single row or column. |
| `const` | No | TRUE or omitted calculates b normally. FALSE sets b to 1 and fits only the growth factors. |
| `stats` | No | TRUE returns the regression statistics. FALSE or omitted returns only the coefficients. |

### Return Value

With `stats` omitted or FALSE, a one-row array: the growth factor m, then the coefficient b, for one x variable. With `stats` TRUE, the same five-row layout that LINEST uses, with the statistics for the logarithmic fit. The results are an array, so use INDEX to read one value.

## Examples

The examples use x values 1 to 5 in `A2:A6` and y values in `B2:B6`: 3.2, 5.9, 12.4, 23.1 and 49.5.

### Example 1: The Growth Factor

```excel
=INDEX(LOGEST(B2:B6, A2:A6), 1)
```

**Result:** `1.9823`

Each step multiplies the value by about 1.98, so the values roughly double from one x to the next.

### Example 2: The Starting Value

```excel
=INDEX(LOGEST(B2:B6, A2:A6), 2)
```

**Result:** `1.5632`

The coefficient b is the value the curve predicts at x equal to 0.

### Example 3: Fixing the Coefficient at 1

```excel
=INDEX(LOGEST(B2:B6, A2:A6, FALSE), 1)
```

**Result:** `2.2392`

With `const` set to FALSE, b is forced to 1 and only the growth factor is fitted. The growth factor is different from Example 1 because the curve has no free starting value.

### Example 4: Predicting the Next Value

```excel
=GROWTH(B2:B6, A2:A6, 6)
```

**Result:** `94.85`

GROWTH returns the predicted y value at x equal to 6. The same value comes from `=INDEX(LOGEST(B2:B6, A2:A6), 2) * INDEX(LOGEST(B2:B6, A2:A6), 1)^6`.

## Story Problems

### Problem 1: Referral Sign-Ups

A subscription service counts referral sign-ups each month in `B2:B7`. The month numbers are in `A2:A7`.

| Month | Sign-Ups |
| --- | --- |
| 1 | 110 |
| 2 | 122 |
| 3 | 141 |
| 4 | 160 |
| 5 | 181 |
| 6 | 205 |

**Task:** Estimate the sign-ups in month 8, assuming the monthly growth rate stays constant.

**Solution:**

```excel
=INDEX(LOGEST(B2:B7, A2:A7), 2) * INDEX(LOGEST(B2:B7, A2:A7), 1)^8
```

**Answer:** `264.26`. The growth factor is 1.1347, which means sign-ups rise about 13.5 percent each month.

<!-- Image 2: Referral Sign-Ups Growth Chart. See Images/Statistical/LOGEST.md -->

### Problem 2: Yearly Repair Costs

A workshop records the total repair cost for one vehicle fleet each year for five years in `B2:B6`. The year numbers are in `A2:A6`.

| Year | Cost |
| --- | --- |
| 1 | 1200 |
| 2 | 1310 |
| 3 | 1460 |
| 4 | 1580 |
| 5 | 1740 |

**Task:** Estimate the cost in year 7 so that the budget can reflect the rising trend.

**Solution:**

```excel
=INDEX(LOGEST(B2:B6, A2:A6), 2) * INDEX(LOGEST(B2:B6, A2:A6), 1)^7
```

**Answer:** `2097.25`. The growth factor is 1.0975, so costs rise about 9.75 percent a year on this trend.

## Use Cases

### Adoption Curve Fitting

**Scenario:** A product team wants to describe the early growth of active users, which doubles at a steady rate.

```excel
=INDEX(LOGEST(Users[Active], Users[Week]), 1)
```

**Why It Works:** The growth factor shows the weekly multiplier. A value near 1 means the product is growing slowly, while a value well above 1 means fast adoption.

### Cost Escalation Trends

**Scenario:** A procurement analyst compares the historical price of a raw material with the price the budget assumed.

```excel
=GROWTH(Prices!C2:C12, Prices!B2:B12, Budget!B2)
```

**Why It Works:** GROWTH applies the fitted curve to the budget year. The result is a benchmark the team can compare with the figure in the plan.

### Referral Growth Modeling

**Scenario:** A marketing lead estimates how many referral sign-ups to expect next quarter.

```excel
=TREND(LN(Referrals!B2:B13), Referrals!A2:A13, Referrals!A14)
```

**Why It Works:** Taking the natural log of the counts turns the exponential curve into a straight line, so TREND can predict on the log scale. Apply EXP to the result to return to sign-up counts.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Wrong number | The data is a straight line, not a curve, so the growth factor is misleading. | Plot the data first, and use LINEST if the change is a steady amount. |
| Unusable result | A y value is zero or negative, and its logarithm is undefined. | Remove or correct the non-positive values before fitting. |
| Single value shows | The array was not read with INDEX or entered in a large enough range. | Wrap the formula in INDEX or enter it as an array. |
| Unreliable forecast | The predicted x lies far outside the observed range. | Limit predictions to the range of observed x values, or review the trend. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions, including Excel for the web | In older versions, enter the formula as an array. Microsoft 365 spills the output automatically. |
| Google Sheets | Available | Same arguments named `known_data_y`, `known_data_x`, `b` and `verbose`. The `b` argument plays the role of `const`. |

## Tips and Best Practices

- Use LOGEST to find the rate, and GROWTH to make predictions. Both start from the same known values.
- Subtract 1 from the growth factor and multiply by 100 to report the rate as a percentage.
- Check the chart on a log scale. A straight line on that scale confirms that an exponential curve fits.
- Keep the x and y ranges the same length, with one row for each observation.
- Avoid forecasting far beyond the observed period, because a constant growth rate rarely lasts forever.

## Related Functions

| Function | Relationship |
| --- | --- |
| [GROWTH](GROWTH.md) | Predicts values on the same exponential curve. |
| [LINEST](LINEST.md) | Fits a straight line with the same output layout. |
| [TREND](TREND.md) | Predicts values on a straight line, the counterpart of GROWTH. |
| [LN](../Math%20%26%20Trig/LN.md) | Converts values to logarithms, which turns an exponential curve into a line. |
| [RSQ](RSQ.md) | Measures how closely a line fits the data. |

## Official Documentation

- [Microsoft Support: LOGEST function](https://support.microsoft.com/en-us/excel/functions/logest-function)
- [Google Docs Editors Help: LOGEST](https://support.google.com/docs/answer/3094251)
