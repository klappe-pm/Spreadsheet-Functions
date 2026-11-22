---
domain: Spreadsheet Functions
category: Statistical
subcategory: Spread and Variance
purpose:
  - Statistical Analysis
use-case:
  - Production Quality Spread
  - Sample Variability Checks
related:
  - DVAR
  - STDEV.S
  - VAR
  - VAR.P
  - VARA
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/var-s-function
  - https://support.google.com/docs/answer/3094063
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Sample Variance
tags:
  - dispersion
  - excel
  - sample
  - sheets
  - variance
---

# VAR.S

## Description

**VAR.S** estimates the variance of a population from a sample. It measures how widely the values spread around their mean, and it divides the sum of squared deviations by the number of values minus one. Because the numbers are treated as a sample, the result is slightly larger than the variance of the same numbers treated as a complete population.

VAR.S replaces the older VAR function. It returns the same result as VAR, and its name makes clear that it handles sample data, matching VAR.P for populations. Use VAR.S in all new formulas and keep VAR only in workbooks that already contain it.

Arguments can be numbers, names, arrays or references. When a range is supplied, the function skips empty cells, logical values and text, so logical values inside a range do not count. To include logical values and numeric text from a range, use VARA. The square root of the variance gives the standard deviation, which STDEV.S returns directly.

## Syntax

```excel
=VAR.S(number1,[number2],...)
```

<!-- Image 1: Sample Variance Compared With Population Variance. See Images/Statistical/VAR.S.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, reference or array that holds sample values. |
| `number2, ...` | No | Up to 253 more numbers, references or arrays from the same sample, for a total of 254 arguments. Numbers typed directly into the list are counted, including logical values and numeric text. |

### Return Value

A number: the sample variance. The function returns an error when an argument is an error value or when text typed directly into the list cannot be converted to a number. Empty cells, logical values and text inside a range are skipped rather than causing an error.

## Examples

All examples use six sample values in `A2:A7`: 4, 8, 6, 5, 3 and 7. Their mean is 5.5 and the sum of squared deviations is 17.5.

### Example 1: Sample Variance of a Range

```excel
=VAR.S(A2:A7)
```

**Result:** `3.5`

Dividing 17.5 by five (six values minus one) gives the sample variance.

### Example 2: Add a Value Typed Directly

```excel
=VAR.S(A2:A7,10)
```

**Result:** `5.8095`

Adding 10 as a seventh value raises the mean to 6.14 and widens the spread. The divisor becomes six.

### Example 3: Standard Deviation From the Variance

```excel
=SQRT(VAR.S(A2:A7))
```

**Result:** `1.8708`

The square root of the sample variance is the sample standard deviation, expressed in the same units as the data.

### Example 4: Compare the Sample and Population Versions

```excel
=VAR.S(A2:A7)/VAR.P(A2:A7)
```

**Result:** `1.2`

With six values, the sample divisor is five and the population divisor is six, so the sample variance is 6/5 or 1.2 times the population variance.

### Example 5: Empty Cells Are Skipped

```excel
=VAR.S(A2:A10)
```

**Result:** `3.5`

When `A8` through `A10` are empty, the function skips them. The result is the same as Example 1 because only the six filled cells count.

## Story Problems

### Problem 1: Fill Weight Consistency

A bottling line samples eight bottles from a batch and records each fill weight in grams in `A2:A9`. The quality engineer wants the sample variance to decide whether the filling machine is stable.

| Bottle | Fill Weight (g) |
| --- | --- |
| 1 | 12.4 |
| 2 | 11.8 |
| 3 | 12.9 |
| 4 | 12.1 |
| 5 | 11.6 |
| 6 | 12.6 |
| 7 | 12.0 |
| 8 | 11.9 |

**Task:** Compute the sample variance of the fill weights.

**Solution:**

```excel
=VAR.S(A2:A9)
```

**Answer:** `0.19125`, or about 0.1913 square grams. The mean is 12.16 grams. The standard deviation is about 0.44 grams, which the engineer can compare with the tolerance on the label.

<!-- Image 2: Fill Weight Sample Result. See Images/Statistical/VAR.S.md -->

### Problem 2: Sample of Shipment Delays

A logistics team measures the delay in hours for 6 shipments picked at random from the month and records them in `A2:A7`. The team wants the sample variance of the delays.

| Shipment | Delay (hours) |
| --- | --- |
| S1 | 4 |
| S2 | 9 |
| S3 | 6 |
| S4 | 2 |
| S5 | 7 |
| S6 | 8 |

**Task:** Compute the sample variance of the six delays.

**Solution:**

```excel
=VAR.S(A2:A7)
```

**Answer:** `6.8`. The mean delay is 6.0 hours. The squared deviations add up to 34, and dividing by five gives 6.8.

## Use Cases

### Production Quality Spread

**Scenario:** A plant samples parts from each shift and tracks how consistent the diameters are over time.

```excel
=STDEV.S(Shift1Diameters)
```

**Why It Works:** Each shift is a sample of the full output, so VAR.S is the right estimator. Compare the spread between shifts before changing the machine settings.

### Sample Variability Checks

**Scenario:** A customer support team reviews a random sample of calls each week and wants to see whether the handling times are steady.

```excel
=VAR.S(CallSample[Minutes])
```

**Why It Works:** The sample variance reports how much the handling times vary across the sampled calls. Use the same sample size each week so the results stay comparable.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error value | An argument is an error value, or text typed directly into the list cannot be converted to a number. | Correct the source cell or the typed value. |
| Unexpected result | Logical values and text inside a range are skipped, so the count is smaller than expected. | Use VARA when logical values should count as 1 or 0 inside a range. |
| Unexpected result | The data is the full population rather than a sample. | Use VAR.P, which divides by the number of values instead of one fewer. |
| Unexpected result | A range includes a header or a footer row that holds a number. | Select only the rows that hold data values. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows and Mac), Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Accepts up to 254 arguments. Logical values and text inside a range are skipped. |
| Google Sheets | Available as an alias | The Sheets help page for VAR.S refers to VAR, which calculates the same sample variance. |

## Tips and Best Practices

- Use VAR.S in new formulas and reserve VAR for older workbooks.
- Choose VAR.P only when the data covers every item in the group.
- Report the standard deviation alongside the variance, since it uses the original units.
- Keep the sample size in view, because the variance of a very small sample is unstable.
- Use VARA rather than VAR.S when the range contains logical flags that should count.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DVAR](../Database/DVAR.md) | Sample variance of the records that match database criteria. |
| [STDEV.S](STDEV.S.md) | Sample standard deviation, the square root of this result. |
| [VAR](VAR.md) | Legacy sample variance that returns the same result. |
| [VAR.P](VAR.P.md) | Population variance that divides by the number of values. |
| [VARA](VARA.md) | Sample variance that counts logical values inside a range. |

## Official Documentation

- [Microsoft Support: VAR.S function](https://support.microsoft.com/en-us/excel/functions/var-s-function)
- [Google Docs Editors Help: VAR](https://support.google.com/docs/answer/3094063)
