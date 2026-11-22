---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
purpose:
  - Regression
  - Statistical Analysis
use-case:
  - Ad Spend Sales Link
  - Calibration Drift Check
  - Study Hours and Scores
related:
  - FORECAST.LINEAR
  - INTERCEPT
  - PEARSON
  - RSQ
  - SLOPE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/correl-function
  - https://support.google.com/docs/answer/3093990
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

# CORREL

## Description

**CORREL** returns the correlation coefficient r for two ranges of values. The result runs from -1 to 1. A value near 1 means the two sets rise together, a value near -1 means one falls as the other rises, and a value near 0 means no linear relationship. The function measures how closely the points follow a straight line, using the Pearson method.

Use CORREL to screen for a linear relationship before you fit a trend line or build a forecast. Square the result to get the share of variation that one measure explains of the other, or use RSQ, which returns the same value directly. A high correlation does not show that one variable causes the other, and it can be distorted by outliers, so check a scatter chart as well.

Google Sheets treats CORREL as synonymous with PEARSON. Both functions return the same value.

## Syntax

```excel
=CORREL(array1, array2)
```

<!-- Image 1: Paired Ranges. See Images/Statistical/CORREL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array1` | Yes | The first range of values, such as a column of ad spend. |
| `array2` | Yes | The second range of values, such as a column of sales. It must contain the same number of data points as `array1`. |

In Google Sheets the arguments are named `data_y` (the dependent values) and `data_x` (the independent values). The correlation is symmetric, so the order does not change the result, but keep the same order as the Sheets help page when you share formulas across platforms.

### Return Value

A number from -1 to 1. The function returns `#N/A` when the two arrays have different numbers of data points, and `#DIV/0!` when either array is empty or when all the values in one array are the same.

## Examples

### Example 1: Correlation Between Two Columns

Ad spend in thousands is in `A2:A7` and sales in thousands is in `B2:B7`.

```excel
=CORREL(A2:A7, B2:B7)
```

**Result:** `0.984007`

The result is close to 1, so the two columns rise together in a nearly straight line.

### Example 2: Share of Variation Explained

```excel
=CORREL(A2:A7, B2:B7)^2
```

**Result:** `0.968270`

Squaring the correlation gives about 0.97, which means roughly 97 percent of the variation in sales follows a straight-line pattern with ad spend in this sample. The same value is returned by `RSQ(B2:B7, A2:A7)`.

### Example 3: Constant Column Returns an Error

Column `C2:C7` holds the value 5 in every row.

```excel
=CORREL(A2:A7, C2:C7)
```

**Result:** `#DIV/0!`

A column with no variation has a standard deviation of zero, so no correlation can be computed. Check for constant columns before you run the test.

### Example 4: Negative Correlation

Column `D2:D7` holds 9, 8, 6, 4, 3 and 1, paired with the ad spend in `A2:A7`.

```excel
=CORREL(A2:A7, D2:D7)
```

**Result:** `-0.985765`

The value is close to -1, so the second column falls as the first rises. A strong negative correlation is as useful as a strong positive one when you are screening drivers.

<!-- Image 2: Scatter Chart With Trend Line. See Images/Statistical/CORREL.md -->

## Story Problems

### Problem 1: Study Hours and Quiz Scores

A teacher records weekly study hours and quiz scores for eight students. Hours are in `A2:A9` and scores are in `B2:B9`.

| Hours | Score |
| --- | --- |
| 1 | 55 |
| 2 | 60 |
| 3 | 58 |
| 4 | 65 |
| 5 | 70 |
| 6 | 72 |
| 7 | 71 |
| 8 | 80 |

**Task:** Find the correlation between hours and score, and the share of score variation explained by hours.

**Solution:**

```excel
=CORREL(A2:A9, B2:B9)
```

**Answer:** `0.961649`. The share explained is `RSQ(B2:B9, A2:A9)`, which equals `0.924769`, so about 92 percent of the score variation follows the hours in this group.

### Problem 2: Calibration Drift

A lab records days since the last calibration (`A2:A7`) and the percent of parts still in tolerance (`B2:B7`). The values are 3, 6, 8, 10, 12 and 15 days, paired with 88, 85, 80, 79, 74 and 70 percent.

**Task:** Find the correlation and decide whether the relationship is strong and negative.

**Solution:**

```excel
=CORREL(A2:A7, B2:B7)
```

**Answer:** `-0.990644`. The value is close to -1, so the share of parts in tolerance falls steadily as time since calibration grows.

## Use Cases

### Ad Spend Sales Link

**Scenario:** A marketing team checks whether weekly ad spend moves with weekly sales before it commits budget to a trend forecast.

```excel
=CORREL(AdSpend, Sales)
```

**Why It Works:** Named ranges keep the formula readable. A value near 1 suggests a linear link worth modeling, while a value near 0 suggests the spend has little effect on sales in this data.

### Calibration Drift Check

**Scenario:** A quality engineer tracks how long equipment goes between calibrations and how many parts stay within tolerance.

```excel
=IF(CORREL(Days, InTolerance) < -0.7, "Calibrate More Often", "Interval Acceptable")
```

**Why It Works:** The threshold turns the correlation into a clear action. The -0.7 cutoff is an example and should be set by the team's own standards.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The two arrays have a different number of data points. | Make both ranges the same length and aligned by row. |
| `#DIV/0!` | One array is empty or holds the same value in every cell. | Check the ranges for constant or missing data. |
| Unexpected value | Text or empty cells are ignored, so rows may no longer pair up as intended. | Clean both columns so each row has a number in both. |
| Misreading the result | A strong correlation was treated as proof of cause. | Check a scatter chart and consider other factors before drawing conclusions. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions | Arguments are `array1` and `array2`. Text, logical values and empty cells in the ranges are ignored. Cells with zero are included. |
| Google Sheets | Available | Arguments are `data_y` and `data_x`. Text in the arguments is ignored. CORREL is synonymous with PEARSON. |

## Tips and Best Practices

- Plot the two columns on a scatter chart before you trust the number. One outlier can change the result.
- Keep both ranges the same length and aligned row by row.
- Use RSQ when you want the squared value directly, or FORECAST.LINEAR when you need a prediction.
- Report the sample size with the correlation, since small samples give unstable values.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FORECAST.LINEAR](FORECAST.LINEAR.md) | Predicts a value from the same straight-line relationship. |
| [INTERCEPT](INTERCEPT.md) | Returns the point where the fitted line crosses the vertical axis. |
| [PEARSON](PEARSON.md) | Returns the same correlation coefficient under a different name. |
| [RSQ](RSQ.md) | Returns the squared correlation, the share of variation explained. |
| [SLOPE](SLOPE.md) | Returns the steepness of the fitted line that the correlation describes. |

## Official Documentation

- [Microsoft Support: CORREL function](https://support.microsoft.com/en-us/excel/functions/correl-function)
- [Google Docs Editors Help: CORREL](https://support.google.com/docs/answer/3093990)
