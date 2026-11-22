---
domain: Spreadsheet Functions
category: Statistical
subcategory: Spread and Variance
purpose:
  - Statistical Analysis
use-case:
  - Process Consistency Checks
  - Rainfall Variability
  - Sample Quality Review
related:
  - AVERAGE
  - STDEV
  - STDEV.P
  - STDEVA
  - VAR.S
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/stdev-s-function
  - https://support.google.com/docs/answer/3094054
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Sample Standard Deviation
tags:
  - excel
  - sheets
  - spread
  - standard-deviation
---

# STDEV.S

## Description

**STDEV.S** returns the standard deviation of a sample, which measures how far the values in a set typically sit from their average. A small result means the values cluster tightly around the mean, and a large result means they are widely spread.

Use STDEV.S when your values are a sample taken from a larger group, such as five bottles pulled from a production run or seven days chosen from a month. The function divides by n minus 1 instead of n, which corrects for the fact that a sample tends to understate the spread of the full group. When your values are the complete group, use STDEV.P.

STDEV.S replaces the older STDEV function, which Microsoft recommends you use only for backward compatibility. Both give the same result for the same sample. Google Sheets documents this calculation on its STDEV page, and STDEV.S returns the same sample standard deviation there.

## Syntax

```excel
=STDEV.S(number1, [number2], ...)
```

<!-- Image 1: Number Arguments for STDEV.S. See Images/Statistical/STDEV.S.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, range, array or reference that contains numbers, treated as a sample. |
| `number2, ...` | No | Additional numbers or ranges. Excel accepts up to 254 arguments in total. |

### Return Value

A number: the sample standard deviation. In a range or array, only numbers are counted, and empty cells, logical values, text and errors are ignored. Numbers, text that looks like a number, and logical values typed directly into the argument list are counted. Error values and text that cannot be converted to a number cause an error.

## Examples

All examples use the values 4, 8, 6, 5, 3 and 7 in `A2:A7`.

### Example 1: Sample Standard Deviation

```excel
=STDEV.S(A2:A7)
```

**Result:** `1.8708` (rounded to four decimals)

The mean of the six values is 5.5. The squared distances from the mean add up to 17.5, which divided by 5 gives a variance of 3.5, and its square root is 1.8708.

### Example 2: Text and Blank Cells in a Range

With `A8` holding the text `n/a` and `A9` left empty:

```excel
=STDEV.S(A2:A9)
```

**Result:** `1.8708` (rounded to four decimals)

Text and empty cells in a range are ignored, so the result matches Example 1.

### Example 3: Sample Versus Population

```excel
=STDEV.S(A2:A7)/STDEV.P(A2:A7)
```

**Result:** `1.0954` (rounded to four decimals)

The sample result is larger than the population result for the same values. The ratio is the square root of 6 divided by 5.

<!-- Image 2: Sample Versus Population Spread. See Images/Statistical/STDEV.S.md -->

### Example 4: Typed Values

```excel
=STDEV.S(4, 8, 6, 5, 3, 7)
```

**Result:** `1.8708` (rounded to four decimals)

Typed numbers in the argument list produce the same result as the range in Example 1.

## Story Problems

### Problem 1: Rainfall for a Sample of Days

A gardener records the rainfall in millimeters on seven randomly chosen days of a month.

| Day | Rainfall (mm) |
| --- | --- |
| 1 | 22 |
| 2 | 0 |
| 3 | 15 |
| 4 | 8 |
| 5 | 30 |
| 6 | 12 |
| 7 | 5 |

**Task:** Measure how much daily rainfall varies from day to day, treating the seven days as a sample of the month.

**Solution:**

```excel
=STDEV.S(B2:B8)
```

**Answer:** `10.2702` mm. The mean is about 13.1 mm, and the typical day differs from that mean by roughly 10 mm, so rainfall varies widely.

### Problem 2: Bottle Fill Volumes

A bottling line checks five bottles from a shift and records the fill volume in milliliters. The five bottles are a sample of all bottles filled that shift.

| Bottle | Volume (ml) |
| --- | --- |
| 1 | 498 |
| 2 | 503 |
| 3 | 501 |
| 4 | 496 |
| 5 | 500 |

**Task:** Estimate the spread of fill volumes for the whole shift.

**Solution:**

```excel
=STDEV.S(B2:B6)
```

**Answer:** `2.7019` ml. The sample standard deviation is an estimate of the variation across the full shift.

<!-- Image 3: Story Problem Results. See Images/Statistical/STDEV.S.md -->

## Use Cases

### Rainfall Variability

**Scenario:** A farm planner checks whether daily rainfall is steady enough to rely on for irrigation planning.

```excel
=STDEV.S(RainfallDaily)
```

**Why It Works:** A large standard deviation relative to the average signals that the average alone is a poor planning guide.

### Process Consistency Checks

**Scenario:** A production supervisor compares the spread of a sample of parts against a tolerance band.

```excel
=IF(STDEV.S(PartWeights)<=MaxSpread,"Consistent","Review Process")
```

**Why It Works:** A single number summarizes the spread of the sample, so the supervisor can compare it with a limit that the process owner sets.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | Too few values to measure spread, for example a single number. | Supply at least two values. Google Sheets requires at least two values as well. |
| `#VALUE!` | A text value that cannot be read as a number was typed into the argument list. | Put the values in cells, or remove the text from the argument list. |
| Result too small | The list is the complete population, but the sample formula was used. | Use STDEV.P for a complete group. |
| Unexpected value | A cell holds a typed 0 that was meant to be blank. | Blank and text cells in a range are ignored, but a 0 counts as a value, so clear the cell instead. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel for Microsoft 365, Excel for the web | Replaces STDEV. Text, logical values and empty cells in a range are ignored. |
| Google Sheets | Available | Its documentation lists STDEV.S alongside STDEV, which calculates the sample standard deviation. |

## Tips and Best Practices

- Use STDEV.S for samples and STDEV.P for complete populations; the choice changes the result.
- Compare the standard deviation with the average to judge whether the spread is large or small.
- Use VAR.S to get the variance, then take the square root if you need the variance first.
- Keep the data range free of headings so that labels are not counted.
- Pair STDEV.S with AVERAGE in the same report so readers see both the center and the spread.

## Related Functions

| Function | Relationship |
| --- | --- |
| [STDEV](STDEV.md) | The older sample function; STDEV.S is its replacement. |
| [STDEV.P](STDEV.P.md) | Standard deviation for a complete population. |
| [STDEVA](STDEVA.md) | Sample standard deviation that counts text and logical values differently. |
| [VAR.S](VAR.S.md) | Sample variance, the square of the standard deviation. |
| [AVERAGE](AVERAGE.md) | The mean that the spread is measured around. |

## Official Documentation

- [Microsoft Support: STDEV.S function](https://support.microsoft.com/en-us/excel/functions/stdev-s-function)
- [Google Docs Editors Help: STDEV](https://support.google.com/docs/answer/3094054)
