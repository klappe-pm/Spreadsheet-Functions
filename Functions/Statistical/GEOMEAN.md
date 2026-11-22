---
domain: Spreadsheet Functions
category: Statistical
subcategory: Averages
purpose:
  - Aggregation
  - Statistical Analysis
use-case:
  - Average Annual Investment Growth
  - Population Growth Rates
related:
  - AVERAGE
  - GROWTH
  - HARMEAN
  - MEDIAN
  - POWER
  - PRODUCT
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/geomean-function
  - https://support.google.com/docs/answer/3094001
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Compound Average
  - Geometric Average
tags:
  - averages
  - excel
  - growth
  - sheets
  - statistics
---

# GEOMEAN

## Description

**GEOMEAN** returns the geometric mean of a set of positive numbers. It multiplies the values together and takes the nth root of the product, where n is the count of values. Use it for data that compounds, such as yearly growth factors, price indexes or ratios, where each value multiplies the one before it. An arithmetic average of growth factors overstates the typical growth, because a large gain and a large loss do not cancel out the way they would in a simple sum.

For a set of growth factors, the geometric mean gives the single constant factor that would produce the same final result over the same number of periods. Subtract 1 from the result to convert it to a rate. For ordinary values such as test scores or heights, use AVERAGE instead.

GEOMEAN accepts up to 255 numbers, or a single range or array. Microsoft requires every data point to be greater than 0, so zero and negative values cause an error. Google's help page does not describe how zero or negative values are handled, so check the data before relying on the result in Sheets.

## Syntax

```excel
=GEOMEAN(number1, [number2], ...)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/GEOMEAN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, range or array. Each value should be greater than 0. |
| `number2, ...` | No | Up to 254 more numbers, ranges or arrays. |

### Return Value

A number: the geometric mean of the positive data. In Excel, the function returns `#NUM!` when any value is 0 or less, including a zero in a referenced range. Text and empty cells in a range are ignored, while text typed directly into the argument list causes an error.

## Examples

### Example 1: Two Values

```excel
=GEOMEAN(2, 8)
```

**Result:** `4`

The product of 2 and 8 is 16, and the square root of 16 is 4.

### Example 2: Three Growth Factors

```excel
=GEOMEAN(1.10, 0.95, 1.20)
```

**Result:** `1.078365`

The three yearly factors compound to the same total as three years at 1.078365 each. Subtract 1 to read the result as 7.84 percent a year.

### Example 3: Zero in a Range

```excel
=GEOMEAN(B2:B4)
```

**Result:** `#NUM!` when B3 contains 0

One zero in the range makes the product zero, and the function returns an error. Replace or remove the zero before taking the mean.

### Example 4: Guarding Against Zero

```excel
=IFERROR(GEOMEAN(B2:B4), "Check for zero values")
```

**Result:** `Check for zero values`

IFERROR shows a message instead of an error when a zero or negative value is present.

<!-- Image 2: Arithmetic Versus Geometric Mean. See Images/Statistical/GEOMEAN.md -->

## Story Problems

### Problem 1: Investment Growth Over Four Years

An investor's portfolio grew or shrank by the yearly factors shown below.

| Year | Growth Factor |
| --- | --- |
| 2024 | 1.12 |
| 2025 | 0.90 |
| 2026 | 1.25 |
| 2027 | 1.05 |

**Task:** Find the constant yearly growth factor that gives the same four-year result, and state it as a percentage gain.

**Solution:**

```excel
=GEOMEAN(B2:B5)
```

**Answer:** `1.072482`, which is about a 7.25 percent gain per year. The four factors multiply to 1.323, and 1.072482 raised to the fourth power gives the same total. The simple average of 1.08 would overstate the result.

### Problem 2: Town Population Trend

A town's population changed by 4 percent, then grew 6 percent, then fell 2 percent over three years. The planners want one annual factor for the forecast.

**Task:** Find the average yearly growth factor, using the three factors 1.04, 1.06 and 0.98.

**Solution:**

```excel
=GEOMEAN(1.04, 1.06, 0.98)
```

**Answer:** `1.026097`, which is about 2.61 percent growth per year.

## Use Cases

### Average Annual Investment Growth

**Scenario:** A financial analyst reports the typical yearly return for a fund over several years.

```excel
=GEOMEAN(GrowthFactors) - 1
```

**Why It Works:** Each yearly factor is multiplied with the others, so the result reflects compounding. Enter growth factors (1 plus the return), not raw percentages.

### Population Growth Rates

**Scenario:** A city planner compares the average growth of several districts across the same period.

```excel
=GEOMEAN(DistrictFactors)
```

**Why It Works:** The geometric mean avoids giving too much weight to one fast-growing district, because the result depends on the product of all the factors.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | A value is 0 or negative, including a zero inside a range. | Remove or correct the value before calculating. |
| `#VALUE!` | Text typed directly into the argument list cannot be read as a number. | Put the value in a cell, or remove the text. |
| Result near 1 | The input is a percentage change, not a growth factor. | Add 1 to each percentage change, such as 1 plus 0.12. |
| Unexpectedly low result | A growth factor was entered as a return. | Use growth factors like 1.12 instead of 0.12. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Every value must be greater than 0. Zero and negative values return `#NUM!`. |
| Google Sheets | Available | The help page describes the nth root of the product. It does not describe how zero or negative values are handled. |

## Tips and Best Practices

- Enter growth factors (1 plus the rate) so the result is a factor you can use directly.
- Check ranges for zeros and negative values before using the mean.
- Subtract 1 from the result to report a yearly rate.
- Use AVERAGE for values that add rather than multiply, such as scores or distances.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGE](AVERAGE.md) | Arithmetic mean, the right choice for values that add together. |
| [HARMEAN](HARMEAN.md) | Harmonic mean, used for rates and prices paid per unit. |
| [MEDIAN](MEDIAN.md) | Middle value, which resists outliers. |
| [GROWTH](GROWTH.md) | Fits an exponential trend to data over time. |
| [POWER](../Math%20%26%20Trig/POWER.md) | Raises a number to a power, useful for converting a factor into a total. |
| [PRODUCT](../Math%20%26%20Trig/PRODUCT.md) | Multiplies the values that GEOMEAN combines. |

## Official Documentation

- [Microsoft Support: GEOMEAN function](https://support.microsoft.com/en-us/excel/functions/geomean-function)
- [Google Docs Editors Help: GEOMEAN](https://support.google.com/docs/answer/3094001)
