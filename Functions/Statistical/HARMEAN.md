---
domain: Spreadsheet Functions
category: Statistical
subcategory: Averages
purpose:
  - Aggregation
  - Statistical Analysis
use-case:
  - Average Speed Over Equal Distances
  - Equal Spend Unit Costs
related:
  - AVERAGE
  - GEOMEAN
  - MAX
  - MEDIAN
  - MIN
  - MODE.SNGL
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/harmean-function
  - https://support.google.com/docs/answer/3094003
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Harmonic Average
  - Harmonic Mean
tags:
  - averages
  - excel
  - rates
  - sheets
  - statistics
---

# HARMEAN

## Description

**HARMEAN** returns the harmonic mean of a set of numbers. It is the reciprocal of the arithmetic mean of the reciprocals: each value is inverted, the inverses are averaged, and the average is inverted again. The harmonic mean is the right average for rates measured per unit of something, such as speed over equal distances or the cost per unit when the same amount of money is spent on each purchase.

The result is always lower than or equal to the arithmetic average of the same numbers, and it gives more weight to small values. That is why it suits averages of rates. For a simple average of quantities that add together, such as scores or totals, use AVERAGE instead. For values that multiply together, such as growth factors, use GEOMEAN.

HARMEAN accepts up to 255 numbers, or a single range or array. Every value must be greater than 0 in Microsoft Excel, because a zero cannot be inverted. Google's help page does not describe how zero or negative values are handled, so check the data before relying on the result in Sheets.

## Syntax

```excel
=HARMEAN(number1, [number2], ...)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/HARMEAN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, range or array. Each value should be greater than 0. |
| `number2, ...` | No | Up to 254 more numbers, ranges or arrays. |

### Return Value

A number: the harmonic mean of the data. The function returns `#NUM!` when any value is 0 or less, including a zero in a referenced range. In a range or array, text, logical values and empty cells are ignored. Text typed directly into the argument list causes an error.

## Examples

### Example 1: Two Speeds Over the Same Distance

```excel
=HARMEAN(60, 40)
```

**Result:** `48`

A round trip with equal distances at 60 and 40 km/h averages 48 km/h, not 50.

### Example 2: Three Values

```excel
=HARMEAN(3, 6, 6)
```

**Result:** `4.5`

The reciprocals are 1/3, 1/6 and 1/6. Their average is 1/4.5, so the harmonic mean is 4.5.

### Example 3: A Range of Prices

```excel
=HARMEAN(B2:B4)
```

**Result:** `3.157895` when B2:B4 holds 2, 4 and 5

The function returns the harmonic mean of the three prices, which is the average cost per unit when the same amount is spent on each.

### Example 4: Guarding Against Zero

```excel
=IFERROR(HARMEAN(B2:B4), "Check for zero values")
```

**Result:** `Check for zero values` when a value in B2:B4 is 0

A zero cannot be inverted, so the function returns `#NUM!`, and IFERROR shows a message instead.

<!-- Image 2: Harmonic Versus Arithmetic Mean. See Images/Statistical/HARMEAN.md -->

## Story Problems

### Problem 1: Average Cost Per Unit

A buyer spends 100 dollars at each of three suppliers. The unit prices are listed below.

| Supplier | Price Per Unit |
| --- | --- |
| Alpha | 2 |
| Beta | 4 |
| Gamma | 5 |

**Task:** Find the average cost per unit across the three purchases.

**Solution:**

```excel
=HARMEAN(B2:B4)
```

**Answer:** `$3.16` per unit, from the calculated 3.157895. The buyer gets 50, 25 and 20 units for 300 dollars in total, which is 95 units, so 300 divided by 95 equals 3.157895.

### Problem 2: Average Speed Over a Route

A courier covers three equal-length legs of a route at 30, 45 and 60 km/h.

| Leg | Speed (km/h) |
| --- | --- |
| Leg 1 | 30 |
| Leg 2 | 45 |
| Leg 3 | 60 |

**Task:** Find the average speed for the whole route.

**Solution:**

```excel
=HARMEAN(B2:B4)
```

**Answer:** `41.54` km/h, from the calculated 41.5385. The arithmetic average of 45 km/h would overstate the speed, because the slowest leg takes the most time.

## Use Cases

### Average Speed Over Equal Distances

**Scenario:** A fleet manager reports the typical speed for trips that cover the same distance at different speeds.

```excel
=HARMEAN(TripSpeeds)
```

**Why It Works:** Equal distances mean the time for each trip depends on its inverse speed, so the harmonic mean gives the true average speed.

### Equal Spend Unit Costs

**Scenario:** A procurement team compares the average price paid per unit when the same budget is spent with each vendor.

```excel
=HARMEAN(UnitPrices)
```

**Why It Works:** Equal budgets buy different quantities, so the harmonic mean gives the average cost per unit across the total budget.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | A value is 0 or negative, including a zero inside a range. | Remove or correct the value before calculating. |
| `#VALUE!` | Text typed directly into the argument list cannot be read as a number. | Put the value in a cell, or remove the text. |
| Result too low | The data is not rates, or the arithmetic average is more appropriate. | Use AVERAGE for quantities that add together. |
| Result too high | Values were entered as their reciprocals. | Enter the rates themselves, not 1 divided by the rate. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Listed on the Microsoft page for current versions | Every value must be greater than 0. Zero and negative values return `#NUM!`. |
| Google Sheets | Available | The help page describes the population divided by the sum of reciprocals. It does not describe how zero or negative values are handled. |

## Tips and Best Practices

- Use HARMEAN for rates, such as speed, price per unit or throughput per hour.
- Use AVERAGE for totals, scores and other values that add together.
- Check ranges for zeros before calculating, because one zero makes the function return an error.
- Compare HARMEAN with GEOMEAN and AVERAGE. The harmonic mean is the lowest of the three for positive data.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGE](AVERAGE.md) | Arithmetic mean, the right choice for values that add together. |
| [GEOMEAN](GEOMEAN.md) | Geometric mean, used for values that multiply, such as growth factors. |
| [MEDIAN](MEDIAN.md) | Middle value, which resists outliers. |
| [MODE.SNGL](MODE.SNGL.md) | Most frequent value in a data set. |
| [MIN](MIN.md) | Smallest value, useful for checking the range before averaging. |
| [MAX](MAX.md) | Largest value, useful for checking the range before averaging. |

## Official Documentation

- [Microsoft Support: HARMEAN function](https://support.microsoft.com/en-us/excel/functions/harmean-function)
- [Google Docs Editors Help: HARMEAN](https://support.google.com/docs/answer/3094003)
