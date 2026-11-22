---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
purpose:
  - Statistical Analysis
use-case:
  - Complete Store Records
  - Full Production Runs
  - Whole Season Comparisons
related:
  - CORREL
  - COVAR
  - COVARIANCE.S
  - PEARSON
  - SLOPE
  - VAR.P
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/covariance-p-function
  - https://support.google.com/docs/answer/3093993
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Population Covariance
  - Covariance Population
tags:
  - covariance
  - excel
  - population
  - sheets
---

# COVARIANCE.P

## Description

**COVARIANCE.P** returns the population covariance of two data sets. It averages the products of the deviations of each pair of data points from their means, dividing by the number of pairs. Use it when the data covers every member of the group you are studying, such as all twelve months of a year, every machine on a line, or every game in a season.

The result has the units of both data sets multiplied together, so a positive value shows that the two sets rise together and a negative value shows that they move in opposite directions. The size alone does not show how strong the link is. For a unit-free measure from -1 to 1, use CORREL.

When the data is a sample taken from a larger group, use COVARIANCE.S instead. It divides by one less than the number of pairs, which gives a larger result for the same data.

COVAR returns the same value as COVARIANCE.P. It is kept for older workbooks, so new formulas should use COVARIANCE.P.

## Syntax

```excel
=COVARIANCE.P(array1, array2)
```

<!-- Image 1: COVARIANCE.P Syntax Anatomy. See Images/Statistical/COVARIANCE.P.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array1` | Yes | The first range or array of numbers. Google Sheets calls it `data_y`. |
| `array2` | Yes | The second range or array of numbers. It must contain the same number of data points as `array1`. Google Sheets calls it `data_x`. |

### Return Value

A number: the population covariance of the two data sets. It returns `#N/A` when the arrays have different numbers of data points and `#DIV/0!` when either array is empty. Text, logical values and empty cells are ignored, while zeros are included in the calculation.

## Examples

All examples use this table in `A1:C6`. Column A holds the number of email campaigns sent in a month, in thousands. Column B holds the new sign-ups from those campaigns, and column C holds the unsubscribes.

| Campaigns | Sign-Ups | Unsubscribes |
| --- | --- | --- |
| 1 | 10 | 4 |
| 2 | 14 | 3 |
| 3 | 20 | 2 |
| 4 | 26 | 1 |
| 5 | 30 | 1 |

### Example 1: Campaigns and Sign-Ups

```excel
=COVARIANCE.P(A2:A6, B2:B6)
```

**Result:** `10.4`

More campaigns went with more sign-ups in every month. The deviation products are 20, 6, 0, 6 and 20, which sum to 52. Dividing by 5 gives 10.4.

### Example 2: Array Constants

```excel
=COVARIANCE.P({2,4,6}, {1,3,5})
```

**Result:** `2.6667`, which is 8 divided by 3

The means are 4 and 3. The deviation products sum to 8, and the three data points give the divisor.

<!-- Image 2: Population Versus Sample Divisor. See Images/Statistical/COVARIANCE.P.md -->

### Example 3: Opposite Movement

```excel
=COVARIANCE.P(A2:A6, C2:C6)
```

**Result:** `-1.6`

As campaigns increase, unsubscribes fall. The deviation products sum to -8, and dividing by 5 gives -1.6.

### Example 4: A Range Compared With Itself

```excel
=COVARIANCE.P(A2:A6, A2:A6)
```

**Result:** `2`

Covariance of a range with itself is its population variance. The values 1 through 5 have a population variance of 2.

## Story Problems

### Problem 1: Practice Hours and Points for a Full Season

A coach records team practice hours and points scored for each of the five games in the season, which is the complete set of games. The data is in `A1:C6`.

| Game | Practice Hours | Points Scored |
| --- | --- | --- |
| Game 1 | 4 | 60 |
| Game 2 | 6 | 70 |
| Game 3 | 8 | 85 |
| Game 4 | 10 | 90 |
| Game 5 | 12 | 110 |

**Task:** Find the population covariance of practice hours and points scored.

**Solution:**

```excel
=COVARIANCE.P(B2:B6, C2:C6)
```

**Answer:** `48`. The mean practice time is 8 hours and the mean score is 83 points. The deviation products sum to 240, and 240 divided by 5 is 48.

<!-- Image 3: Season Covariance Result. See Images/Statistical/COVARIANCE.P.md -->

### Problem 2: Machine Speed and Defects Across the Plant

A plant manager has one speed setting and one defect count for each of its four machines in `A1:C5`. These four machines are the whole plant, so the population form applies.

| Machine | Speed Setting | Defects |
| --- | --- | --- |
| M1 | 2 | 9 |
| M2 | 3 | 7 |
| M3 | 4 | 5 |
| M4 | 5 | 2 |

**Task:** Find the population covariance of speed setting and defects.

**Solution:**

```excel
=COVARIANCE.P(B2:B5, C2:C5)
```

**Answer:** `-2.875`. The mean speed is 3.5 and the mean defect count is 5.75. The deviation products sum to -11.5, and dividing by 4 gives -2.875. Faster settings line up with fewer defects.

## Use Cases

### Complete Store Records

**Scenario:** A retail chain has twelve months of advertising spend and sales for one store, and the analyst treats the full year as the whole population.

```excel
=COVARIANCE.P(Stores!B2:B13, Stores!C2:C13)
```

**Why It Works:** The full year is the complete record, so the population form is the correct choice. Keep both ranges the same length, with each month in the same row.

### Full Production Runs

**Scenario:** A quality engineer compares line speed and defect counts for every production run in a quarter, stored in a table.

```excel
=COVARIANCE.P(Runs[Speed], Runs[Defects])
```

**Why It Works:** The table covers every run, so no sampling is involved. Structured references keep the formula correct when runs are added to the table.

### Whole Season Comparisons

**Scenario:** A sports analyst wants the strength of the link between practice hours and points, not only its direction.

```excel
=COVARIANCE.P(Season[Hours], Season[Points]) / (STDEV.P(Season[Hours]) * STDEV.P(Season[Points]))
```

**Why It Works:** Dividing by the two population standard deviations turns the covariance into a unit-free correlation. The result equals CORREL for the same data, and the formula shows where the number comes from.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The two arrays have different numbers of data points. | Make both ranges the same length and check for a missing row. |
| `#DIV/0!` | One array is empty. | Confirm that both ranges contain values. |
| Value is smaller than the sample version | The data is a sample, but the population divisor was used. | Use COVARIANCE.S for a sample, which divides by n minus 1. |
| Result treated as a strength | Covariance depends on the units of both data sets. | Use CORREL for a value from -1 to 1. |
| Pairs out of step | Blanks or text in one range are ignored, so rows no longer match. | Check both ranges for blanks and text before calculating. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | The Microsoft support page lists Excel 2016 and later among the versions it applies to. |
| Google Sheets | Available | Uses the arguments `data_y` and `data_x`, the same as COVAR. Check results against a hand calculation on known data. |

## Tips and Best Practices

- Choose COVARIANCE.P only when the data is the whole group, and COVARIANCE.S when it is a sample.
- Read the sign first, then use CORREL when the strength of the relationship matters.
- Keep the paired values in the same rows, so each data point in one range matches the point in the other.
- Test a small set by hand once to confirm the divisor and the sign.
- Label the units next to the result, because the same covariance means different things in dollars and in units.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COVARIANCE.S](COVARIANCE.S.md) | Divides by n minus 1 for a sample of the group. |
| [COVAR](COVAR.md) | Returns the same value; kept for older workbooks. |
| [CORREL](CORREL.md) | Returns the unit-free correlation, from -1 to 1. |
| [PEARSON](PEARSON.md) | Returns the Pearson correlation coefficient, which matches CORREL. |
| [SLOPE](SLOPE.md) | Returns the slope of the line through the paired points. |
| [VAR.P](VAR.P.md) | Returns the population variance of one data set, which is the covariance of a set with itself. |

## Official Documentation

- [Microsoft Support: COVARIANCE.P function](https://support.microsoft.com/en-us/excel/functions/covariance-p-function)
- [Google Docs Editors Help: COVARIANCE.P](https://support.google.com/docs/answer/3093993)
