---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Statistical Analysis
use-case:
  - Rainfall Variability Analysis
  - Sample Spread Reporting
related:
  - STDEV.S
  - VAR.P
  - VAR.S
  - VARA
  - VARP
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/var-function
  - https://support.google.com/docs/answer/3094063
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Sample Variance
tags:
  - compatibility
  - excel
  - sample
  - sheets
  - variance
---

# VAR

## Description

**VAR** estimates the variance of a population from a sample. It measures how far the values spread around their mean, treating the numbers you supply as a sample drawn from a larger group. The result divides the sum of squared deviations by the number of values minus one, which corrects for the fact that a sample tends to understate the spread of the full population.

VAR is a legacy compatibility function. Microsoft states that it has been replaced by VAR.S, which returns the same result with a clearer name. Use VAR.S in new formulas. Use VARP or VAR.P when the numbers are the complete population rather than a sample.

When you supply a range, VAR ignores empty cells, logical values and text. To count logical values inside a range, use VARA instead. The square root of the variance is the standard deviation, which you can calculate with SQRT or with STDEV.S.

## Syntax

```excel
=VAR(number1,[number2],...)
```

<!-- Image 1: Sample Values and the Sample Variance. See Images/Statistical/VAR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, reference or array that holds values from a sample. |
| `number2, ...` | No | Up to 254 more numbers, references or arrays from the same sample. Numbers typed directly into the list are counted, including logical values and numeric text. |

### Return Value

A number: the sample variance. The function returns an error when an argument is an error value or when text typed directly into the list cannot be converted to a number. Text and logical values inside a range do not produce errors; they are skipped.

## Examples

All examples use six sample values in `A2:A7`: 4, 8, 6, 5, 3 and 7. Their mean is 5.5.

### Example 1: Sample Variance of a Range

```excel
=VAR(A2:A7)
```

**Result:** `3.5`

The squared deviations from the mean add up to 17.5, and 17.5 divided by five (six values minus one) gives 3.5.

### Example 2: The Replacement Function

```excel
=VAR.S(A2:A7)
```

**Result:** `3.5`

VAR.S returns the same sample variance as VAR. Microsoft recommends VAR.S for new work, so this is the formula to copy into new workbooks.

### Example 3: Add More Values Directly

```excel
=VAR(A2:A7,10)
```

**Result:** `5.8095`

The value 10 is added as a seventh sample value. The mean rises to 6.14 and the variance rises to 5.8095, which shows how a single high value widens the spread.

### Example 4: Blank Cells Are Skipped

```excel
=VAR(A2:A9)
```

**Result:** `3.5`

When `A8` and `A9` are empty, VAR skips them and returns the same value as Example 1. Empty cells do not count toward the sample size.

### Example 5: Values Typed Directly

```excel
=VAR(4,8,6,5,3,7)
```

**Result:** `3.5`

Typing the values into the formula gives the same result as referencing the range. This is useful for checking a small set of numbers quickly.

## Story Problems

### Problem 1: Rainfall Variability

A weather station records the rainfall in millimeters for seven days in `A1:B8`. The analyst wants the sample variance to judge how unpredictable the daily rainfall has been.

| Day | Rainfall (mm) |
| --- | --- |
| Mon | 12 |
| Tue | 0 |
| Wed | 5 |
| Thu | 9 |
| Fri | 3 |
| Sat | 14 |
| Sun | 7 |

**Task:** Compute the sample variance of the daily rainfall.

**Solution:**

```excel
=VAR(B2:B8)
```

**Answer:** `24.4762`. The mean is 7.14 mm. The seven squared deviations add up to 146.86, and dividing by six gives 24.4762. A standard deviation of about 4.95 mm follows from the square root.

<!-- Image 2: Rainfall Table and Variance Result. See Images/Statistical/VAR.md -->

## Use Cases

### Rainfall Variability Analysis

**Scenario:** A farm planner wants the standard deviation of monthly rainfall recorded in a log, to judge the risk of a dry spell.

```excel
=SQRT(VAR(RainfallLog[mm]))
```

**Why It Works:** VAR returns the variance of the logged months as a sample, and SQRT converts it to a standard deviation in the same units as the rainfall.

### Sample Spread Reporting

**Scenario:** A quality team inspects a sample of parts each week and reports how much the defect counts vary.

```excel
=VAR(Inspections[Defects])
```

**Why It Works:** Using the sample version is correct when the inspected parts are only part of the production run. Use VARP only when every part in the run was counted.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error value | An argument is an error value, or text typed directly into the list cannot be converted to a number. | Correct the source cell or the typed value. |
| Unexpected result | Logical values and text inside a range are skipped, so fewer values are counted than expected. | Use VARA when logical values should count as 1 or 0. |
| Unexpected result | The data is the complete population, not a sample. | Use VARP or VAR.P so the divisor is the number of values. |
| Unexpected result | Empty cells are assumed to be zeros. | Empty cells are skipped. Enter a 0 in the cell when the value really is zero. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all listed versions | Legacy compatibility function. Microsoft recommends VAR.S, and VAR may be removed from future versions. |
| Google Sheets | Available | Takes `value1, [value2, ...]`. Returns an error when every argument is text. Text is not counted as zero; use VARA for that. Fewer than two numeric values return `#DIV/0!`. |

## Tips and Best Practices

- Use VAR.S for new work, because VAR is kept only for compatibility.
- Use VAR.P or VARP when your data covers the entire group, not a sample of it.
- Take the square root of the variance to report the spread in the original units.
- Check for blank cells and text that a range may contain, because VAR skips them silently.
- Compare the variance with the mean to judge whether the spread is large relative to the average.

## Related Functions

| Function | Relationship |
| --- | --- |
| [VAR.S](VAR.S.md) | Modern replacement that returns the same sample variance. |
| [VAR.P](VAR.P.md) | Variance for a complete population, dividing by the number of values. |
| [VARP](VARP.md) | Legacy population variance, the compatibility partner of VAR.P. |
| [VARA](VARA.md) | Sample variance that counts logical values and text as values. |
| [STDEV.S](STDEV.S.md) | Sample standard deviation, the square root of the sample variance. |

## Official Documentation

- [Microsoft Support: VAR function](https://support.microsoft.com/en-us/excel/functions/var-function)
- [Google Docs Editors Help: VAR](https://support.google.com/docs/answer/3094063)
