---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
purpose:
  - Regression
  - Statistical Analysis
use-case:
  - Cost Driver Analysis
  - Sales Trend Modeling
  - Unit Cost Estimation
related:
  - GROWTH
  - INTERCEPT
  - LOGEST
  - RSQ
  - SLOPE
  - TREND
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/linest-function
  - https://support.google.com/docs/answer/3094249
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Least Squares Coefficients
  - Linear Regression Coefficients
tags:
  - array-formula
  - excel
  - least-squares
  - linear-regression
  - sheets
---

# LINEST

## Description

**LINEST** fits a straight line to known x and y values using the least-squares method and returns the coefficients of that line. With one x variable, it returns the slope and the y-intercept. With several x variables, it returns one coefficient for each variable plus the intercept. When you set the statistics option to TRUE, it also returns the standard errors, the R squared value, the F statistic and the sums of squares.

LINEST is the full regression tool behind the simpler functions. SLOPE and INTERCEPT return one coefficient each, RSQ returns the fit, and TREND predicts y values. Use LINEST when you need more than one of these results, when you have several x variables, or when you want to review the statistics that show whether the fit is reliable.

The output is an array, so the formula returns several values at once. To read one value, wrap LINEST in INDEX. Results are in reverse order for several x variables: the last coefficient in the output belongs to the first x column. Check the data first, because the coefficients are only meaningful when a straight line describes the relationship.

## Syntax

```excel
=LINEST(known_y's, [known_x's], [const], [stats])
```

<!-- Image 1: Output Array With Statistics. See Images/Statistical/LINEST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `known_y's` | Yes | The dependent values. With one x variable, they can be in any shape that matches `known_x's`. |
| `known_x's` | No | The independent values. If omitted, the values 1, 2, 3 and so on are used. With several x variables, `known_y's` must be a single row or column. |
| `const` | No | TRUE or omitted calculates the intercept normally. FALSE forces the intercept to 0, so the line passes through the origin. |
| `stats` | No | TRUE returns the regression statistics. FALSE or omitted returns only the coefficients and the intercept. |

### Return Value

With `stats` omitted or FALSE, a one-row array: the slope, then the intercept, for one x variable. With `stats` TRUE, a five-row array. Row 1 holds the coefficients and the intercept, row 2 holds their standard errors, row 3 holds R squared and the standard error of y, row 4 holds the F statistic and the degrees of freedom, and row 5 holds the regression and residual sums of squares. The standard error of the intercept returns `#N/A` when `const` is FALSE.

## Examples

The examples use production units in `A2:A6` and total cost in `B2:B6`. The values are 10, 20, 30, 40, 50 and the costs are 195, 232, 268, 310, 345.

### Example 1: The Slope

```excel
=INDEX(LINEST(B2:B6, A2:A6), 1)
```

**Result:** `3.78`

Position 1 of the single-row output is the slope. Each extra unit adds about 3.78 to cost.

### Example 2: The Intercept

```excel
=INDEX(LINEST(B2:B6, A2:A6), 2)
```

**Result:** `156.6`

Position 2 is the intercept, the cost the line predicts at zero units.

### Example 3: Forcing the Line Through the Origin

```excel
=INDEX(LINEST(B2:B6, A2:A6, FALSE), 1)
```

**Result:** `8.0509`

With `const` set to FALSE, the intercept is fixed at 0 and only the slope is fitted. The slope is a different number from Example 1 because the line is no longer free to shift.

### Example 4: Reading R Squared

```excel
=INDEX(LINEST(B2:B6, A2:A6, TRUE, TRUE), 3, 1)
```

**Result:** `0.9993`

Row 3, column 1 of the statistics output is R squared. A value this close to 1 means the straight line explains almost all of the variation in cost.

### Example 5: Predicting Cost at 60 Units

```excel
=INDEX(LINEST(B2:B6, A2:A6), 1) * 60 + INDEX(LINEST(B2:B6, A2:A6), 2)
```

**Result:** `383.4`

The slope times 60 is 226.8, and adding the intercept of 156.6 gives 383.4.

## Story Problems

### Problem 1: Fixed and Variable Cost of a Print Run

A print shop records the units printed and the total cost of each run in `B2:C6`.

| Run | Units | Cost |
| --- | --- | --- |
| 1 | 100 | 2750 |
| 2 | 200 | 3990 |
| 3 | 300 | 5240 |
| 4 | 400 | 6480 |
| 5 | 500 | 7750 |

**Task:** Find the variable cost per unit and the fixed cost per run. Then find the cost of a 350-unit run.

**Solution:**

```excel
=INDEX(LINEST(C2:C6, B2:B6), 1) * 350 + INDEX(LINEST(C2:C6, B2:B6), 2)
```

**Answer:** The variable cost is 12.49 per unit and the fixed cost is 1495. A 350-unit run costs `5866.5`.

### Problem 2: Subscriber Growth Forecast

A newsletter counted subscribers at the end of each month for six months. The months are in `A2:A7` and the subscriber counts are in `B2:B7`.

| Month | Subscribers |
| --- | --- |
| 1 | 52 |
| 2 | 57 |
| 3 | 60 |
| 4 | 66 |
| 5 | 71 |
| 6 | 75 |

**Task:** Estimate the subscriber count in month 9 using the linear trend.

**Solution:**

```excel
=INDEX(LINEST(B2:B7, A2:A7), 1) * 9 + INDEX(LINEST(B2:B7, A2:A7), 2)
```

**Answer:** `89.11`. The slope is about 4.66 subscribers per month and the intercept is 47.2. Month 9 is outside the observed months, so treat the forecast as a rough guide.

<!-- Image 2: Story Problem Chart With Trend Line. See Images/Statistical/LINEST.md -->

## Use Cases

### Cost Driver Analysis

**Scenario:** A manufacturer wants to know how much of each cost depends on machine hours.

```excel
=INDEX(LINEST(Costs[Total], Costs[MachineHours]), 1)
```

**Why It Works:** The slope is the cost change per machine hour. Structured references keep the formula current as new months are added.

### Multiple Driver Model

**Scenario:** A property team estimates rent from floor area and the number of rooms.

```excel
=LINEST(Rent!D2:D40, Rent!B2:C40, TRUE, TRUE)
```

**Why It Works:** With two x columns, the output lists the room coefficient first and the area coefficient second, because the coefficients come back in reverse column order. Check the row 3 R squared before trusting the result.

### Unit Cost Estimation

**Scenario:** A procurement analyst predicts the price of a part from order volume.

```excel
=INDEX(LINEST(Quotes!C2:C30, Quotes!B2:B30), 1)
```

**Why It Works:** The slope shows how much the unit price falls as volume rises, which supports negotiation with suppliers.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` in the second row | The standard error of the intercept is undefined when `const` is FALSE. | Expect this result, or use TRUE for `const` when an intercept is needed. |
| Zero coefficients | LINEST removed x columns that are collinear, which means one column is a combination of others. | Remove the duplicate or redundant x column. |
| Only one value shows | The formula was entered in one cell, so the array was truncated. | Enter the formula in a range large enough for the output, or wrap it in INDEX. |
| Wrong coefficient order | With several x columns the output runs in reverse order. | Read the output from the last position to the first, or label each position. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions, including Excel for the web | In older versions, enter the formula as an array with Ctrl+Shift+Enter. Microsoft 365 spills the output automatically. |
| Google Sheets | Available | Same arguments named `known_data_y`, `known_data_x`, `calculate_b` and `verbose`. The verbose output lists the statistics in the same order. |

## Tips and Best Practices

- Use INDEX to pick one coefficient. Pointing a single cell at the whole output shows only the first value.
- Check R squared and the standard errors before using a coefficient in a decision.
- Keep x and y ranges the same length and aligned, so each row is one observation.
- Predictions far outside the range of the observed x values are unreliable.
- For a quick slope or intercept with no statistics, SLOPE and INTERCEPT are simpler.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SLOPE](SLOPE.md) | Returns only the slope of the same line. |
| [INTERCEPT](INTERCEPT.md) | Returns only the intercept of the same line. |
| [RSQ](RSQ.md) | Returns R squared directly, without the full output. |
| [TREND](TREND.md) | Returns predicted y values using the same linear model. |
| [LOGEST](LOGEST.md) | Fits an exponential curve instead of a straight line, with the same output layout. |
| [GROWTH](GROWTH.md) | Predicts values on an exponential curve, the counterpart of TREND. |

## Official Documentation

- [Microsoft Support: LINEST function](https://support.microsoft.com/en-us/excel/functions/linest-function)
- [Google Docs Editors Help: LINEST](https://support.google.com/docs/answer/3094249)
