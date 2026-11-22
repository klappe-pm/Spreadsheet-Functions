---
domain: Spreadsheet Functions
category: Statistical
subcategory: Correlation Transforms
purpose:
  - Statistical Analysis
use-case:
  - Confidence Interval for Correlation
  - Correlation Averaging
  - Meta Analysis
related:
  - AVERAGE
  - CORREL
  - FISHERINV
  - PEARSON
  - RSQ
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/fisher-function
  - https://support.google.com/docs/answer/3093626
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Fisher Transformation
tags:
  - correlation
  - excel
  - sheets
  - transformation
---

# FISHER

## Description

**FISHER** returns the Fisher transformation of a value. The transformation is the inverse hyperbolic tangent, so FISHER(0.75) returns about 0.9730. Its purpose is to turn a correlation coefficient, which is bounded between -1 and 1, into a scale that is close to normally distributed and has no hard limits.

Use FISHER before you average correlations from several studies, or before you build a confidence interval for a correlation. Average the transformed values, not the raw correlations, and then convert the result back with FISHERINV. Averaging on the transformed scale avoids the bias that appears when correlations near 1 or -1 are averaged directly.

FISHER accepts one value at a time. To transform a column of correlations, enter the formula in a helper column and fill it down.

## Syntax

```excel
=FISHER(value)
```

<!-- Image 1: Correlation Scale Compared With the Fisher Scale. See Images/Statistical/FISHER.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The number to transform. For a correlation, use a value strictly between -1 and 1. |

### Return Value

A number on the Fisher scale. Excel returns `#VALUE!` when the value is not numeric, and `#NUM!` when the value is -1 or less, or 1 or more, because the transformation is undefined at those points.

## Examples

### Example 1: Transforming a Moderate Correlation

```excel
=FISHER(0.6)
```

**Result:** `0.6931` (rounded to four decimal places)

A correlation of 0.6 becomes 0.6931 on the Fisher scale. The transformed value is the one to average or to use in an interval.

### Example 2: Transforming a Strong Correlation

```excel
=FISHER(0.9)
```

**Result:** `1.4722` (rounded to four decimal places)

A correlation of 0.9 becomes 1.4722. The gap between 0.6 and 0.9 is wider on the Fisher scale than it looks on the correlation scale.

### Example 3: Transforming a Negative Correlation

```excel
=FISHER(-0.5)
```

**Result:** `-0.5493` (rounded to four decimal places)

Negative correlations transform to negative values with the same size, so the sign is preserved.

<!-- Image 2: Transformed Values in a Helper Column. See Images/Statistical/FISHER.md -->

## Story Problems

### Problem 1: Averaging Three Studies

Three studies report the correlation between training hours and sales results. The team wants one combined value. It transforms each correlation in column C, averages the transformed values, and then converts the average back.

| Study | Correlation | Fisher Value |
| --- | --- | --- |
| Study 1 | 0.42 | 0.4477 |
| Study 2 | 0.55 | 0.6184 |
| Study 3 | 0.61 | 0.7089 |

**Task:** Find the average of the transformed values in `C2:C4`.

**Solution:**

```excel
=AVERAGE(C2:C4)
```

**Answer:** `0.5917`. Each value in column C came from `=FISHER(B2)`, filled down. Convert this average back with FISHERINV to get the combined correlation.

### Problem 2: Interval Around a Strong Correlation

A logistics analyst finds a correlation of 0.97 between route length and fuel use. Before building a confidence interval, the analyst needs the value on the Fisher scale.

| Measure | Value |
| --- | --- |
| Correlation | 0.97 |

**Task:** Transform the correlation in `B2` to the Fisher scale.

**Solution:**

```excel
=FISHER(B2)
```

**Answer:** `2.0923`. The interval is built on this scale and then converted back to correlations with FISHERINV.

## Use Cases

### Meta Analysis

**Scenario:** A research team combines correlations from several published studies into a single estimate.

```excel
=FISHERINV(AVERAGE(FISHER(B2), FISHER(B3), FISHER(B4)))
```

**Why It Works:** The formula transforms each correlation, averages the results, and converts the average back. Each correlation has its own cell reference, so the formula works in every version of the function.

### Confidence Interval for Correlation

**Scenario:** An analyst reports a 95 percent interval for a correlation based on a sample of 40 pairs.

```excel
=FISHERINV(FISHER(r) - 1.96/SQRT(n-3))
```

**Why It Works:** The interval is symmetric on the Fisher scale, with a standard error of 1 over the square root of n minus 3. Converting the lower bound back with FISHERINV gives the lower limit on the correlation scale. Repeat with a plus sign for the upper limit.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The value is -1 or less, or 1 or more. | Check that the input is a correlation strictly between -1 and 1. |
| `#VALUE!` | The value is text or a blank cell read as text. | Convert the cell to a number or fix the reference. |
| Biased combined correlation | Raw correlations were averaged directly. | Transform each value with FISHER, average the results, then use FISHERINV. |
| Blank result when filled down | A helper cell still refers to a blank row. | Fill the formula only through rows that contain data. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current Excel, including Excel for the web | Returns `#NUM!` at -1 and 1 and beyond, and `#VALUE!` for non-numeric input. |
| Google Sheets | Available | Google's help page gives the syntax and examples but does not document domain limits or error values. |

## Tips and Best Practices

- Keep correlations in their own column and the transformed values in a helper column, so the averaging step is easy to audit.
- Average on the Fisher scale and convert back only at the end.
- For a weighted average, weight each transformed value by its sample size minus 3 and divide by the sum of those weights.
- Check that every input is strictly between -1 and 1 before transforming, because values at the limits return an error.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGE](AVERAGE.md) | Averages the transformed values before converting back. |
| [CORREL](CORREL.md) | Calculates the correlation coefficient that FISHER transforms. |
| [FISHERINV](FISHERINV.md) | Converts a Fisher value back to a correlation, the inverse of this function. |
| [PEARSON](PEARSON.md) | Returns the Pearson correlation coefficient from two data sets. |
| [RSQ](RSQ.md) | Returns the squared correlation, a related measure of fit. |

## Official Documentation

- [Microsoft Support: FISHER function](https://support.microsoft.com/en-us/excel/functions/fisher-function)
- [Google Docs Editors Help: FISHER](https://support.google.com/docs/answer/3093626)
