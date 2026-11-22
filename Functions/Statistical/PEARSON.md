---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
purpose:
  - Regression
  - Statistical Analysis
use-case:
  - Ad Spend and Revenue
  - Maintenance Age and Defects
  - Temperature and Sales
related:
  - CORREL
  - COVARIANCE.S
  - FORECAST.LINEAR
  - RSQ
  - SLOPE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/pearson-function
  - https://support.google.com/docs/answer/3094092
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Correlation Coefficient
  - Pearson Correlation
tags:
  - correlation
  - excel
  - regression
  - sheets
---

# PEARSON

## Description

**PEARSON** returns r, the Pearson product-moment correlation coefficient. It measures how closely two lists of numbers move together along a straight line. The result runs from -1 to 1: a value near 1 means the two lists rise together, a value near -1 means one list rises as the other falls, and a value near 0 means no straight-line relationship.

Use PEARSON before you build a trendline or forecast from two measures, such as ad spend and sales, to confirm the measures are related. The two lists must contain the same number of values, and each position in the first list is paired with the same position in the second.

Correlation describes association, not cause. PEARSON only detects straight-line patterns, so a strong curved relationship can return a value close to 0. Squaring the result gives the same value as RSQ.

## Syntax

```excel
=PEARSON(array1, array2)
```

<!-- Image 1: Pearson Arguments Diagram. See Images/Statistical/PEARSON.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array1` | Yes | The first set of values, for example `A2:A6`. Google Sheets calls this argument `data_y`. |
| `array2` | Yes | The second set of values, paired position by position with `array1`. Google Sheets calls this argument `data_x`. |

Text, logical values and empty cells are ignored. Keep both ranges the same size so each row pairs its two values correctly.

### Return Value

A number from -1 to 1. PEARSON returns `#N/A` when the two arrays are empty or contain a different number of data points.

## Examples

All examples use this table in `A1:B6`, with hours studied in column A and quiz scores in column B.

| Hours | Score |
| --- | --- |
| 2 | 65 |
| 3 | 70 |
| 5 | 78 |
| 7 | 85 |
| 9 | 93 |

### Example 1: Correlation of Two Columns

```excel
=PEARSON(A2:A6, B2:B6)
```

**Result:** `0.998989`

The scores rise almost perfectly in step with the hours, so r is very close to 1.

### Example 2: Swapping the Arguments

```excel
=PEARSON(B2:B6, A2:A6)
```

**Result:** `0.998989`

Correlation is symmetric, so the order of the two arrays does not change the result.

### Example 3: A Negative Relationship

Months since service are in `D2:D6` (30, 45, 60, 75, 90) and defects per 100 units are in `E2:E6` (9, 8, 7, 5, 3).

```excel
=PEARSON(D2:D6, E2:E6)
```

**Result:** `-0.984798`

As the months grow, defects fall. A negative r close to -1 shows a strong inverse relationship.

### Example 4: Coefficient of Determination

```excel
=PEARSON(A2:A6, B2:B6)^2
```

**Result:** `0.997979`

Squaring r gives the share of variation in the scores that the hours explain on a straight line. The same value comes from `=RSQ(B2:B6, A2:A6)`.

## Story Problems

### Problem 1: Lemonade Sales and Temperature

A stand records the daily high temperature and the cups of lemonade sold on six days in `A1:B7`.

| Temperature (C) | Cups Sold |
| --- | --- |
| 18 | 12 |
| 20 | 15 |
| 22 | 14 |
| 25 | 20 |
| 27 | 22 |
| 30 | 27 |

**Task:** Measure how strongly temperature and cups sold move together.

**Solution:**

```excel
=PEARSON(B2:B7, A2:A7)
```

**Answer:** `0.975017`. Sales climb with the temperature, so the correlation is strong and positive.

### Problem 2: Maintenance Age and Defects

A plant records how many months each machine has gone since its last service and the defects per 100 units it produced.

| Months Since Service | Defects per 100 |
| --- | --- |
| 30 | 9 |
| 45 | 8 |
| 60 | 7 |
| 75 | 5 |
| 90 | 3 |

**Task:** Determine whether the defect rate tends to rise or fall as service intervals grow.

**Solution:**

```excel
=PEARSON(A2:A6, B2:B6)
```

**Answer:** `-0.984798`. Defects fall steadily as time since service grows, so the relationship is strong and negative.

<!-- Image 2: Scatter Plot of the Lemonade Data. See Images/Statistical/PEARSON.md -->

## Use Cases

### Marketing Spend Check

**Scenario:** A marketing team wants to know whether monthly ad spend tracks monthly revenue before it commits next year's budget.

```excel
=PEARSON(Marketing[Ad Spend], Marketing[Revenue])
```

**Why It Works:** A value near 1 supports a budget model based on spend. A value near 0 means spend is not driving revenue in a straight-line way, and the team should look for other drivers.

### Maintenance Schedule Review

**Scenario:** A maintenance supervisor checks whether longer gaps between services lead to more defects.

```excel
=PEARSON(Machines[Months Since Service], Machines[Defects per 100])
```

**Why It Works:** A strong negative value is a signal to shorten service intervals. Confirm the pattern with a scatter chart, because one outlier machine can change r noticeably.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The arrays are empty or have a different number of values. | Make both ranges the same length and covering the same rows. |
| Misaligned pairs | A blank or text cell in one column shifts the pairing with the other column. | Remove or fill the gaps so each row has a value in both columns. |
| Unexpected low value | The relationship is curved, not straight. | Plot the data first and consider a different model. |
| Error with a flat column | A column has no variation, so the calculation cannot produce a coefficient. | Check that both columns contain varying values. The official page does not name the error returned. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Arguments are named `array1` and `array2`. |
| Google Sheets | Available | Arguments are named `data_y` and `data_x`. The result is the same for either order. |

## Tips and Best Practices

- Plot the two columns as a scatter chart before you trust the number, because r cannot show curves or clusters.
- Use RSQ when you want the share of variation explained, and use SLOPE or FORECAST.LINEAR when you need a line.
- Keep the two ranges as paired columns in the same rows so each record stays together when you sort.
- Use a table with structured references so the ranges grow with new rows.
- Confirm a weak value with a chart before acting on it, because a low r does not prove that two measures are unrelated.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CORREL](CORREL.md) | Returns the same correlation coefficient, using the same argument order. |
| [COVARIANCE.S](COVARIANCE.S.md) | Measures joint variation in raw units, which is not scaled to -1 to 1. |
| [FORECAST.LINEAR](FORECAST.LINEAR.md) | Predicts a value from a straight-line fit of the same pairs. |
| [RSQ](RSQ.md) | Returns the squared correlation, the share of variation explained. |
| [SLOPE](SLOPE.md) | Returns the slope of the straight-line fit for the same pairs. |

## Official Documentation

- [Microsoft Support: PEARSON function](https://support.microsoft.com/en-us/excel/functions/pearson-function)
- [Google Docs Editors Help: PEARSON](https://support.google.com/docs/answer/3094092)
