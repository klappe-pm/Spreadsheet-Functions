---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Statistical Analysis
use-case:
  - Price and Demand Relationships
  - Staffing and Output Comparisons
  - Temperature and Energy Use
related:
  - CORREL
  - COVARIANCE.P
  - COVARIANCE.S
  - DEVSQ
  - PEARSON
  - SLOPE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/covar-function
  - https://support.google.com/docs/answer/3093993
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Covariance Of Two Ranges
  - Legacy Covariance
tags:
  - compatibility
  - covariance
  - excel
  - sheets
---

# COVAR

## Description

**COVAR** returns covariance, the average of the products of the deviations of each pair of data points from their means. Covariance shows how two data sets move together. A positive result means that high values in one list tend to appear with high values in the other. A negative result means that high values tend to appear with low values. The size of the result depends on the units of both lists, so it does not tell you how strong the relationship is on its own. CORREL gives a unit-free strength measure.

Microsoft lists COVAR as a compatibility function. Its support page says that COVAR has been replaced by COVARIANCE.P and COVARIANCE.S, and that it remains for backward compatibility but may not be available in future versions. COVAR divides by the number of data points, so it returns the same value as COVARIANCE.P. For new work, use COVARIANCE.P for the population calculation or COVARIANCE.S for the sample calculation.

Google Sheets also lists COVAR, with its arguments named `data_y` and `data_x`. The dependent data comes first.

## Syntax

```excel
=COVAR(array1, array2)
```

<!-- Image 1: COVAR Syntax Anatomy. See Images/Statistical/COVAR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array1` | Yes | The first range of numbers, such as `A2:A6`. Google Sheets calls it `data_y`. |
| `array2` | Yes | The second range of numbers, with exactly as many data points as `array1`. Google Sheets calls it `data_x`. |

### Return Value

A number: the covariance of the two data sets. The function returns `#N/A` when the two arrays have different numbers of data points. It returns `#DIV/0!` when either array is empty. Text, logical values and empty cells in an array or reference are ignored, while cells that contain zero are included.

## Examples

All examples use this table in `A1:C6`. Column A holds overtime hours, column B holds units packed, and column C holds defects found at the end of each shift.

| Overtime Hours | Units Packed | Defects |
| --- | --- | --- |
| 3 | 120 | 9 |
| 5 | 150 | 7 |
| 6 | 160 | 6 |
| 9 | 210 | 4 |
| 12 | 240 | 2 |

### Example 1: Two Lists That Rise Together

```excel
=COVAR(A2:A6, B2:B6)
```

**Result:** `136`

Shifts with more overtime also packed more units. Each pair contributes a positive product, so the average is positive.

### Example 2: Array Constants

```excel
=COVAR({2,4,6}, {1,3,5})
```

**Result:** `2.6667`, which is 8 divided by 3

The means are 4 and 3. The deviation products are 4, 0 and 4, which sum to 8. COVAR divides by the three data points, not by two.

<!-- Image 2: Positive and Negative Covariance. See Images/Statistical/COVAR.md -->

### Example 3: Two Lists That Move in Opposite Directions

```excel
=COVAR(A2:A6, C2:C6)
```

**Result:** `-7.6`

As overtime rises, defects fall. The result is negative because high overtime values line up with low defect values.

### Example 4: A List Compared With Itself

```excel
=COVAR(A2:A6, A2:A6)
```

**Result:** `10`

When both arguments are the same range, covariance equals the population variance of that range. Here the mean is 7 and the squared deviations sum to 50, and 50 divided by 5 is 10.

## Story Problems

### Problem 1: Staffing and Orders Shipped

A distribution center records staff on shift and orders shipped for five days in `A1:C6`.

| Day | Staff On Shift | Orders Shipped |
| --- | --- | --- |
| Monday | 40 | 310 |
| Tuesday | 52 | 380 |
| Wednesday | 48 | 350 |
| Thursday | 60 | 450 |
| Friday | 56 | 410 |

**Task:** Find the covariance between staff on shift and orders shipped.

**Solution:**

```excel
=COVAR(B2:B6, C2:C6)
```

**Answer:** `328`. The mean staff count is 51.2 and the mean order count is 380. The deviation products sum to 1,640, and 1,640 divided by 5 is 328. The positive sign shows that busier days had more staff.

<!-- Image 3: Staffing Covariance Result. See Images/Statistical/COVAR.md -->

### Problem 2: Temperature and Iced Drink Sales

A café records the afternoon temperature and the iced drinks it sold for five days in `A1:C6`.

| Day | Temperature | Drinks Sold |
| --- | --- | --- |
| Monday | 18 | 40 |
| Tuesday | 22 | 55 |
| Wednesday | 25 | 70 |
| Thursday | 29 | 95 |
| Friday | 31 | 110 |

**Task:** Find the covariance between temperature and drinks sold.

**Solution:**

```excel
=COVAR(B2:B6, C2:C6)
```

**Answer:** `119`. The mean temperature is 25 and the mean sales figure is 74. The deviation products sum to 595, and 595 divided by 5 is 119. The positive result matches the pattern that warmer days sold more drinks.

## Use Cases

### Keeping an Older Workbook Working

**Scenario:** An accounts team inherited a workbook from several years ago that uses COVAR across two ranges of monthly figures.

```excel
=COVAR(Old!B2:B49, Old!C2:C49)
```

**Why It Works:** The formula still calculates in current Excel. When the team edits the workbook, they can replace COVAR with COVARIANCE.P, which returns the same value and uses the current name.

### Comparing Ad Spend With Revenue

**Scenario:** A marketing analyst checks whether monthly ad spend and revenue move together across regions.

```excel
=COVAR(Regions[Ad Spend], Regions[Revenue])
```

**Why It Works:** Structured references follow the table as rows are added. The sign of the result shows the direction of the relationship, and CORREL can then show its strength on a scale from -1 to 1.

### Checking Direction in a Quality Dashboard

**Scenario:** A plant supervisor tracks machine temperature and reject rate, and wants to know whether the two rise together.

```excel
=IF(COVAR(Readings!B2:B200, Readings!C2:C200)>0, "Move together", "Move apart")
```

**Why It Works:** The formula converts the sign of the covariance into a label for the dashboard. The label does not show strength, so pair it with CORREL when the strength matters.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The two arrays have different numbers of data points. | Make both ranges the same length and check for a missing row. |
| `#DIV/0!` | One of the arrays is empty. | Confirm that both ranges contain data. |
| Result looks too small or too large | The size depends on the units of both lists. | Compare covariances only for the same pair of measures, or use CORREL for a unit-free value. |
| Result differs from a sample calculation | COVAR divides by n, which is the population method. | Use COVARIANCE.S when the data is a sample and a divisor of n minus 1 is needed. |
| Unexpected value | Text or blanks in one range are ignored, so the pairs no longer line up. | Check both ranges for blanks and text before calculating. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available as a compatibility function | Replaced by COVARIANCE.P and COVARIANCE.S. Kept for backward compatibility, and Microsoft notes it may not be available in future versions. |
| Google Sheets | Available | Arguments are named `data_y` and `data_x`, with the dependent data first. The help page gives the syntax without sample results. |

## Tips and Best Practices

- Use COVARIANCE.P for new population calculations and keep COVAR only in workbooks that already rely on it.
- Read the sign first. Then use CORREL when you need to know how strong the relationship is.
- Keep both ranges the same length, with the paired values in the same rows.
- Remember that covariance uses the units of both lists, so a result in dollars times units is normal.
- Check a small example by hand once, so you can confirm the formula sums the products you expect.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CORREL](CORREL.md) | Gives the unit-free strength of the relationship, from -1 to 1. |
| [COVARIANCE.P](COVARIANCE.P.md) | Returns the same population covariance under the current name. |
| [COVARIANCE.S](COVARIANCE.S.md) | Returns the sample covariance, which divides by n minus 1. |
| [DEVSQ](DEVSQ.md) | Returns the sum of squared deviations for one data set. |
| [PEARSON](PEARSON.md) | Returns the Pearson correlation coefficient for two data sets. |
| [SLOPE](SLOPE.md) | Returns the slope of the line that fits the two data sets. |

## Official Documentation

- [Microsoft Support: COVAR function](https://support.microsoft.com/en-us/excel/functions/covar-function)
- [Google Docs Editors Help: COVAR](https://support.google.com/docs/answer/3093993)
