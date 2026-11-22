---
domain: Spreadsheet Functions
category: Statistical
subcategory: Correlation Transforms
purpose:
  - Statistical Analysis
use-case:
  - Back Transforming Averages
  - Confidence Interval Conversion
  - Correlation Recovery
related:
  - AVERAGE
  - CORREL
  - FISHER
  - PEARSON
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/fisherinv-function
  - https://support.google.com/docs/answer/3093998
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Inverse Fisher Transformation
tags:
  - correlation
  - excel
  - sheets
  - transformation
---

# FISHERINV

## Description

**FISHERINV** returns the inverse of the Fisher transformation. It converts a value on the Fisher scale back to a correlation coefficient, so that FISHERINV(FISHER(x)) returns x. The inverse is the hyperbolic tangent, which keeps every result between -1 and 1.

Use FISHERINV at the end of a calculation that happened on the Fisher scale. The usual steps are to transform each correlation with FISHER, average the results or build an interval, and then convert the answer back with FISHERINV. Converting a raw average of correlations gives a different and less accurate answer.

FISHERINV accepts any real number, so the input does not need to be bounded. Its output is always strictly between -1 and 1.

## Syntax

```excel
=FISHERINV(value)
```

<!-- Image 1: Fisher Scale Converted Back to the Correlation Scale. See Images/Statistical/FISHERINV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | A value on the Fisher scale, usually the output of FISHER or an average of such values. |

### Return Value

A correlation-scale number between -1 and 1. Excel returns `#VALUE!` when the value is not numeric. Google's help page does not document other error conditions.

## Examples

### Example 1: Converting a Positive Value

```excel
=FISHERINV(0.5)
```

**Result:** `0.4621` (rounded to four decimal places)

A value of 0.5 on the Fisher scale corresponds to a correlation of about 0.4621.

### Example 2: Converting a Larger Value

```excel
=FISHERINV(1.2)
```

**Result:** `0.8337` (rounded to four decimal places)

Larger Fisher values move closer to 1 but never reach it, so the result stays below 1.

<!-- Image 2: Round Trip Between the Correlation and Fisher Scales. See Images/Statistical/FISHERINV.md -->

### Example 3: Round Trip With FISHER

```excel
=FISHERINV(FISHER(0.75))
```

**Result:** `0.75`

FISHER converts 0.75 to the Fisher scale, and FISHERINV converts it back. The result returns the original correlation, which confirms the two functions are inverses.

## Story Problems

### Problem 1: Combined Correlation From Averaged Values

A quality team transformed three correlations between machine speed and defect rate. The transformed values are in column B, and their average is the combined value on the Fisher scale. The team needs the combined correlation for its report.

| Study | Fisher Value |
| --- | --- |
| Line 1 | 0.80 |
| Line 2 | 1.10 |
| Line 3 | 0.95 |

**Task:** Convert the average of the Fisher values in `B2:B4` back to a correlation.

**Solution:**

```excel
=FISHERINV(AVERAGE(B2:B4))
```

**Answer:** `0.7398`. The average of the three values is 0.95, and FISHERINV(0.95) is 0.7398.

### Problem 2: Reading a Reported Interval

A consultant receives a report that gives a lower interval limit of 1.0986 on the Fisher scale. The consultant wants that limit on the correlation scale so it can be compared with the reported correlation.

| Measure | Value |
| --- | --- |
| Lower limit (Fisher scale) | 1.0986 |

**Task:** Convert the lower limit in `B2` to the correlation scale.

**Solution:**

```excel
=FISHERINV(B2)
```

**Answer:** `0.8000`. The lower limit is a correlation of 0.8, which is the value the consultant needed to compare with the report.

## Use Cases

### Back Transforming Averages

**Scenario:** A research analyst averages transformed correlations from several surveys and needs the combined correlation for a summary table.

```excel
=FISHERINV(AVERAGE(FISHER(B2), FISHER(B3), FISHER(B4)))
```

**Why It Works:** The average is taken on the Fisher scale, where the values are more evenly spread, and FISHERINV converts the final answer back to a correlation.

### Confidence Interval Conversion

**Scenario:** A statistician builds a 95 percent interval for a correlation on the Fisher scale and reports the limits as correlations.

```excel
=FISHERINV(FISHER(r) - 1.96/SQRT(n-3))
```

**Why It Works:** The lower limit is calculated on the Fisher scale, where the interval is symmetric, and FISHERINV returns it on the correlation scale. Repeat with a plus sign for the upper limit.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The value is text or a blank cell read as text. | Convert the cell to a number or fix the reference. |
| Result is too small or too large | The value was a correlation rather than a Fisher value. | Convert the correlation with FISHER first, or check which scale the number is on. |
| Result differs from the expected average | The correlations were averaged before transforming. | Transform with FISHER, average the results, then convert with FISHERINV. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current Excel, including Excel for the web | Returns `#VALUE!` for non-numeric input. Output is always between -1 and 1. |
| Google Sheets | Available | Google's help page gives the syntax and examples but does not document error values or input ranges. |

## Tips and Best Practices

- Convert back only once, at the end of the calculation, so rounding does not build up.
- Label the column as Fisher scale so readers do not mistake the values for correlations.
- Check the output with CORREL on the original data when you are unsure of the scale.
- Keep the Fisher values in a helper column, which makes the averaging and conversion steps easy to follow.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGE](AVERAGE.md) | Averages Fisher values before they are converted back. |
| [CORREL](CORREL.md) | Calculates a correlation from raw data, for checking the result. |
| [FISHER](FISHER.md) | Transforms a correlation to the Fisher scale, the inverse of this function. |
| [PEARSON](PEARSON.md) | Returns the Pearson correlation coefficient from two data sets. |

## Official Documentation

- [Microsoft Support: FISHERINV function](https://support.microsoft.com/en-us/excel/functions/fisherinv-function)
- [Google Docs Editors Help: FISHERINV](https://support.google.com/docs/answer/3093998)
