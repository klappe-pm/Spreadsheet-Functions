---
domain: Spreadsheet Functions
category: Statistical
subcategory: Spread and Variance
purpose:
  - Statistical Analysis
use-case:
  - Complete Group Comparison
  - Production Batch Consistency
  - Shift Output Variability
related:
  - AVERAGE
  - SKEW.P
  - STDEV.S
  - STDEVP
  - VARP
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/stdev-p-function
  - https://support.google.com/docs/answer/3094105
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Population Standard Deviation
tags:
  - excel
  - population
  - sheets
  - spread
---

# STDEV.P

## Description

**STDEV.P** returns the standard deviation of a population, which measures how far the values in a complete group typically sit from their average. A small result means the values are tightly grouped, and a large result means they are widely spread.

Use STDEV.P when your values are the entire group you want to describe, such as every batch made in one run, every shift in one week or every machine on a line. When your values are a sample drawn from a larger group, use STDEV.S instead. The population version divides by n, while the sample version divides by n minus 1, so the two functions give different answers for the same numbers.

STDEV.P replaces the older STDEVP function. Microsoft recommends STDEV.P for new work and keeps STDEVP for backward compatibility. Its result is the square root of the population variance, which VARP returns for the same values.

## Syntax

```excel
=STDEV.P(number1, [number2], ...)
```

<!-- Image 1: Population Arguments for STDEV.P. See Images/Statistical/STDEV.P.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, range, array or reference that contains numbers, treated as the whole population. |
| `number2, ...` | No | Additional numbers or ranges. Excel accepts up to 254 arguments in total. |

### Return Value

A number: the population standard deviation. In a range or array, only numbers are counted, and empty cells, logical values, text and errors are ignored. Numbers, text that looks like a number, and logical values typed directly into the argument list are counted. Error values and text that cannot be converted to a number cause an error.

## Examples

All examples use the values 4, 8, 6, 5, 3 and 7 in `A2:A7`.

### Example 1: Population Standard Deviation

```excel
=STDEV.P(A2:A7)
```

**Result:** `1.7078` (rounded to four decimals)

The squared distances from the mean of 5.5 add up to 17.5. Dividing by 6, the count of values, gives a variance of 2.9167, and its square root is 1.7078.

### Example 2: Variance From the Same Values

```excel
=STDEV.P(A2:A7)^2
```

**Result:** `2.9167` (rounded to four decimals)

Squaring the standard deviation returns the population variance, which is useful when a later formula needs the variance itself.

### Example 3: Text and Blank Cells in a Range

With `A8` holding the text `n/a` and `A9` left empty:

```excel
=STDEV.P(A2:A9)
```

**Result:** `1.7078` (rounded to four decimals)

Text and empty cells in a range are ignored, so the result matches Example 1.

<!-- Image 2: Population Variance Versus Standard Deviation. See Images/Statistical/STDEV.P.md -->

### Example 4: Typed Values

```excel
=STDEV.P(98, 102, 95, 101, 104)
```

**Result:** `3.1623` (rounded to four decimals)

The five values have a mean of 100 and a population variance of exactly 10, so the standard deviation is the square root of 10.

## Story Problems

### Problem 1: Five Batches of One Run

A chemist makes five batches in a single production run and records the purity of each batch as a percentage. The five batches are the entire run, so the population function applies.

| Batch | Purity (%) |
| --- | --- |
| 1 | 98 |
| 2 | 102 |
| 3 | 95 |
| 4 | 101 |
| 5 | 104 |

**Task:** Measure how much the purity varies across this run.

**Solution:**

```excel
=STDEV.P(B2:B6)
```

**Answer:** `3.1623` percentage points. The batches average 100 percent, and a typical batch differs from that by about 3 points.

### Problem 2: Shift Output in One Week

A plant records the number of units packed on each of six shifts during one week. These shifts are the complete set the plant wants to describe.

| Shift | Units |
| --- | --- |
| 1 | 40 |
| 2 | 38 |
| 3 | 44 |
| 4 | 41 |
| 5 | 39 |
| 6 | 46 |

**Task:** Find how much output varies from shift to shift during the week.

**Solution:**

```excel
=STDEV.P(B2:B7)
```

**Answer:** `2.8087` units. Output varies by a little under 3 units from the average of about 41.3 units per shift.

<!-- Image 3: Story Problem Results. See Images/Statistical/STDEV.P.md -->

## Use Cases

### Production Batch Consistency

**Scenario:** A quality team compares the purity of every batch from one run to decide whether the run met its target.

```excel
=STDEV.P(RunPurity)
```

**Why It Works:** The run is the complete group, so the population version describes it exactly. Compare the result against the spread the process owner allows.

### Shift Output Variability

**Scenario:** A plant manager reviews the output of every shift in a week to see whether staffing changes made the output more uneven.

```excel
=STDEV.P(WeeklyUnits)/AVERAGE(WeeklyUnits)
```

**Why It Works:** Dividing the standard deviation by the average gives a relative spread that can be compared across weeks with different output levels.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A text value that cannot be read as a number was typed into the argument list. | Put the values in cells, or remove the text from the argument list. |
| Result too large | A sample of the group was entered, but the population formula was used. | Use STDEV.S when the values are a sample. |
| Result too small | Blank or text cells were skipped while the numbers were meant to be zeros. | Enter 0 in cells that should count as zero. |
| Unexpected value | A label or header was included in the range. | Select only the numeric cells. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel for Microsoft 365, Excel for the web | Replaces STDEVP. Text, logical values and empty cells in a range are ignored. |
| Google Sheets | Available | Its documentation lists STDEV.P alongside STDEVP, which calculates the population standard deviation. |

## Tips and Best Practices

- Use STDEV.P only when the values are the complete group; otherwise use STDEV.S.
- Compare STDEV.P with AVERAGE to judge whether the spread is large relative to the center.
- Use VARP or the square of STDEV.P when a formula needs the variance rather than the standard deviation.
- Select only the numeric cells, so headers and notes are not counted.
- Label the range clearly in reports so readers know it covers the whole group.

## Related Functions

| Function | Relationship |
| --- | --- |
| [STDEV.S](STDEV.S.md) | Standard deviation for a sample, using n minus 1. |
| [STDEVP](STDEVP.md) | The older population function; STDEV.P is its replacement. |
| [STDEV](STDEV.md) | The older sample function. |
| [VARP](VARP.md) | Population variance, the square of STDEV.P. |
| [AVERAGE](AVERAGE.md) | The mean that the spread is measured around. |

## Official Documentation

- [Microsoft Support: STDEV.P function](https://support.microsoft.com/en-us/excel/functions/stdev-p-function)
- [Google Docs Editors Help: STDEV.P](https://support.google.com/docs/answer/3094105)
