---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Hyperbolic
purpose:
  - Statistical Analysis
  - Trigonometry
use-case:
  - Correlation Averaging
  - Fisher Z Transformation
related:
  - ACOSH
  - ASINH
  - ATAN
  - SINH
  - TANH
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/atanh-function
  - https://support.google.com/docs/answer/3093397
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Inverse Hyperbolic Tangent
tags:
  - excel
  - hyperbolic
  - inverse
  - sheets
  - statistics
---

# ATANH

## Description

**ATANH** returns the inverse hyperbolic tangent of a number. It is the reverse of `TANH`: if `TANH(x)` gives `y`, then `ATANH(y)` gives `x` back. The input must be strictly between -1 and 1, so -1 and 1 themselves are not valid inputs.

The most common business use is the Fisher z-transformation in statistics. Correlation coefficients do not average well on their own, so analysts convert each correlation with ATANH, average the converted values, and convert the average back with `TANH`. Averaging on the z scale gives a more accurate combined correlation than averaging the raw values.

ATANH is a specialist function. Most spreadsheets never need it, but it is useful whenever a value must be mapped from the bounded range (-1, 1) onto the full real number line. Microsoft Excel and Google Sheets both accept one argument with the same meaning.

## Syntax

```excel
=ATANH(number)
```

<!-- Image 1: Inverse Hyperbolic Tangent Domain. See Images/Math & Trig/ATANH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | A real number strictly between -1 and 1. Google Sheets calls this argument `value`. Values of exactly -1 or 1, or outside that range, are outside the valid domain. |

### Return Value

A real number. The result is the value whose hyperbolic tangent equals the input. Values outside the valid domain do not produce a usable result, and the Microsoft page does not name the error value returned for them, so test edge values before relying on the output.

## Examples

### Example 1: Basic Usage

```excel
=ATANH(0.5)
```

**Result:** `0.549306144`

The result equals the natural logarithm of 3 divided by 2. The input 0.5 is well inside the valid range.

### Example 2: A Negative Input

```excel
=ATANH(-0.9)
```

**Result:** `-1.472219490`

Negative inputs return negative results. Values close to -1 or 1 produce large magnitudes, which is why the domain stops short of the endpoints.

### Example 3: Round Trip With TANH

```excel
=ATANH(TANH(0.8))
```

**Result:** `0.8`

`TANH` converts 0.8 into a value between -1 and 1, and `ATANH` converts it back. The round trip confirms the two functions are inverses.

### Example 4: Guarding the Domain

```excel
=IF(ABS(B2)<1, ATANH(B2), "Out of range")
```

**Result:** `0.447692024` when B2 is 0.42

The `IF` test checks that the absolute value is below 1 before the function runs. Use this pattern when a column of correlations may include a value of exactly 1 or -1.

## Story Problems

### Problem 1: Combining Three Correlation Studies

A research team reviews three studies. Each reports a correlation coefficient between training hours and test scores.

| Study | Correlation (r) | Fisher z |
| --- | --- | --- |
| Study A | 0.42 | |
| Study B | 0.55 | |
| Study C | 0.31 | |

**Task:** Compute the combined correlation. Average the z values, then convert the average back to a correlation.

**Solution:**

```excel
=TANH(AVERAGE(ATANH(B2:B4)))
```

**Answer:** `0.4319`. The average z is about 0.4622, and `TANH` converts that back to about 0.4319.

<!-- Image 2: Fisher Z Averaging Steps. See Images/Math & Trig/ATANH.md -->

### Problem 2: Mixed Positive and Negative Correlations

A quality analyst compares two supplier surveys. One reports a correlation of -0.6 and the other reports 0.2.

| Survey | Correlation (r) | Fisher z |
| --- | --- | --- |
| Survey 1 | -0.6 | |
| Survey 2 | 0.2 | |

**Task:** Find the average Fisher z value for the two surveys.

**Solution:**

```excel
=AVERAGE(ATANH(B2:B3))
```

**Answer:** `-0.2452`. The first survey contributes -0.6931 and the second contributes 0.2027, and their mean is -0.2452. Convert it back with `TANH` to get a combined correlation of -0.2404.

<!-- Image 3: Mixed Sign Correlation Table. See Images/Math & Trig/ATANH.md -->

## Use Cases

### Correlation Averaging

**Scenario:** A portfolio analyst has correlations between several asset pairs over different periods and needs one average for a report.

```excel
=TANH(AVERAGE(ATANH(Correlations[Value])))
```

**Why It Works:** Averaging on the z scale avoids the bias that appears when raw correlations near 1 are averaged directly. `TANH` returns the result to the correlation scale that the report uses.

### Fisher Z Transformation

**Scenario:** A survey team needs to test whether two correlation coefficients differ, which requires comparing their z values.

```excel
=(ATANH(C2) - ATANH(C3)) / SQRT(1 / (N2 - 3) + 1 / (N3 - 3))
```

**Why It Works:** `ATANH` produces the z values, and the standard error uses the sample sizes in N2 and N3. Each sample size must be greater than 3, or the denominator fails.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| No usable result | The input is 1 or -1, or lies outside the range. | Check the input with `ABS(x)<1` before calling the function. |
| `#VALUE!` | The argument is text, or a range is used in a formula that needs a single value. | Convert the input to a number, or wrap the range in `AVERAGE` or `SUM`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions and Excel for the web | Argument is named `number`. Microsoft documents the domain as strictly between -1 and 1. |
| Google Sheets | Available | Argument is named `value`. Google documents the domain as strictly between -1 and 1. |

## Tips and Best Practices

- Test inputs with `ABS(x)<1` before calling ATANH, because the function is only defined inside the open interval.
- Average z values, not raw correlations, when combining correlation coefficients.
- Convert the final average back with `TANH` so the output reads as a correlation again.
- Keep the sample sizes beside the correlations when a test of difference is needed.
- Use `ATANH(TANH(x))` as a quick check when you build a model that uses both functions.

## Related Functions

| Function | Relationship |
| --- | --- |
| [TANH](../Math%20%26%20Trig/TANH.md) | Forward hyperbolic tangent; use it to convert a z value back to a correlation. |
| [ATAN](../Math%20%26%20Trig/ATAN.md) | Inverse circular tangent, which works on the full real line. |
| [ACOSH](../Math%20%26%20Trig/ACOSH.md) | Inverse hyperbolic cosine, the counterpart for cosh values of 1 or more. |
| [ASINH](../Math%20%26%20Trig/ASINH.md) | Inverse hyperbolic sine, which accepts any real number. |
| [SINH](../Math%20%26%20Trig/SINH.md) | Hyperbolic sine, the forward function for ASINH. |

## Official Documentation

- [Microsoft Support: ATANH function](https://support.microsoft.com/en-us/excel/functions/atanh-function)
- [Google Docs Editors Help: ATANH](https://support.google.com/docs/answer/3093397)
