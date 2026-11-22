---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Hyperbolic
purpose:
  - Trigonometry
use-case:
  - Amplifier Output Curves
  - Small Value Approximation Checks
related:
  - ASINH
  - COSH
  - EXP
  - SIN
  - TANH
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/sinh-function
  - https://support.google.com/docs/answer/3093517
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Hyperbolic Sine
tags:
  - excel
  - hyperbolic
  - sheets
  - sine
---

# SINH

## Description

**SINH** returns the hyperbolic sine of a number. It is defined from the exponential function as (e^x minus e^-x) divided by 2. Unlike SIN, which repeats between -1 and 1, SINH grows without limit as the input moves away from zero, and it has no repeating pattern.

The input is a plain number, not an angle. Do not convert a value with RADIANS before passing it to SINH, because the hyperbolic functions do not read angles. Use SIN for circular angles in radians.

SINH is an odd function, so SINH(-x) equals -SINH(x). It returns 0 at zero, and for small inputs its value is close to the input itself. That near-linear behavior is useful for checking approximations.

Microsoft Excel and Google Sheets both accept any real number. Google Sheets does not support complex numbers, so imaginary inputs are not valid.

## Syntax

```excel
=SINH(number)
```

<!-- Image 1: Hyperbolic Sine Curve. See Images/Math & Trig/SINH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | Any real number for which you want the hyperbolic sine. The value is a plain number, not an angle. |

### Return Value

Returns the hyperbolic sine of the number as a decimal value. The result has the same sign as the input. The function returns #VALUE! when the argument is text that cannot be read as a number.

## Examples

### Example 1: Hyperbolic Sine of One

```excel
=SINH(1)
```

**Result:** 1.1752

The value is (e to the power 1 minus e to the power -1) divided by 2, which equals about 1.1752.

### Example 2: Hyperbolic Sine of Zero

```excel
=SINH(0)
```

**Result:** 0

The hyperbolic sine of zero is zero, the only input that produces zero.

<!-- Image 2: Odd Symmetry Around Zero. See Images/Math & Trig/SINH.md -->

### Example 3: Negative Input

```excel
=SINH(-1)
```

**Result:** -1.1752

SINH is an odd function, so a negative input returns the negative of the positive result.

### Example 4: Larger Input

```excel
=SINH(2)
```

**Result:** 3.6269

The value grows quickly as the input increases. At 2, the result is more than three times the result at 1.

### Example 5: Scaled Output

```excel
=2.5 * SINH(0.5)
```

**Result:** 1.3027

Multiplying by a gain of 2.5 scales the curve. This is the pattern used when a model's output is a constant times the hyperbolic sine of an input.

## Story Problems

### Problem 1: Amplifier Output for Three Inputs

A sensor amplifier produces an output equal to 2.5 times the hyperbolic sine of the input signal. The test team applies three input levels and records each input.

| Test | Input Level |
| --- | --- |
| Low | 0.5 |
| Middle | 1 |
| High | 1.5 |

**Task:** Find the total output for the three tests, rounded to two decimal places.

**Solution:**

```excel
=ROUND(SUMPRODUCT(2.5 * SINH(B2:B4)), 2)
```

**Answer:** `9.56`. The individual outputs are about 1.30, 2.94, and 5.32, and they total 9.5639 before rounding.

### Problem 2: Checking a Small-Value Approximation

An engineer uses x as an approximation for SINH(x) when x is small. The engineer checks how far the approximation is from the exact value at x = 0.1.

| Cell | Value |
| --- | --- |
| A2 (input) | 0.1 |

**Task:** Find the difference between SINH(0.1) and 0.1, rounded to six decimal places.

**Solution:**

```excel
=ROUND(SINH(A2) - A2, 6)
```

**Answer:** `0.000167`, which is about 0.17 percent of the input. For small inputs, the approximation is close enough for many checks.

## Use Cases

### Amplifier Output Curves

**Scenario:** A hardware team models an amplifier whose output follows a hyperbolic sine curve, and it needs the output for a range of input levels.

```excel
=B2 * SINH(A2)
```

**Why It Works:** A2 holds the input level and B2 holds the gain. The output grows faster than the input, so the table shows how quickly the output rises at high levels.

### Small Value Approximation Checks

**Scenario:** A research team replaces SINH with its input for small values in a model, and it needs to confirm that the error stays within tolerance.

```excel
=ABS(SINH(A2) - A2) / SINH(A2)
```

**Why It Works:** The relative error compares the approximation with the exact value. ABS keeps the result positive, so each row can be checked against the same tolerance.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is text, not a number. | Convert the text with VALUE or correct the source cell. |
| Unexpected result for an angle | The value was converted with RADIANS. | Pass the plain number to SINH, and use SIN for circular angles. |
| Confusion with SIN | The circular and hyperbolic functions have similar names. | Use SIN for angles and SINH for exponential-based curves. |
| Unexpected large value | The input is large, so the output grows quickly. | Check the input range before you scale the result. |
| `#NAME?` | The function name is misspelled. | Check that the name is spelled SINH. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Microsoft 365 for Mac, Excel for the web, Excel 2024, Excel 2024 for Mac, Excel 2021, Excel 2021 for Mac, Excel 2019, and Excel 2016 | Accepts any real number. |
| Google Sheets | Available | Accepts any real number. Imaginary and complex numbers are not supported. |

## Tips and Best Practices

- Use SINH when a curve is defined by exponential growth or decay, not when a formula measures an angle.
- Store a gain or scale factor in its own cell, so the curve can be changed without rewriting the formula.
- Compare SINH with its input for small values to see whether a linear approximation is good enough.
- Check the sign of the input, because the function is odd and the output changes sign with it.
- Use ASINH to recover the input from a hyperbolic sine value.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ASINH](ASINH.md) | Returns the inverse hyperbolic sine, which recovers the input from SINH. |
| [COSH](COSH.md) | Returns the hyperbolic cosine, which is paired with SINH in many formulas. |
| [EXP](EXP.md) | Returns e raised to a power, which is the basis of SINH. |
| [SIN](SIN.md) | Returns the circular sine of an angle in radians. |
| [TANH](TANH.md) | Returns the hyperbolic tangent, the ratio of SINH to COSH. |

## Official Documentation

- [Microsoft Support: SINH function](https://support.microsoft.com/en-us/excel/functions/sinh-function)
- [Google Docs Editors Help: SINH](https://support.google.com/docs/answer/3093517)
