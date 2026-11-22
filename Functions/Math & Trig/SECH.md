---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Hyperbolic
purpose:
  - Trigonometry
use-case:
  - Decaying Signal Amplitude
  - Symmetric Response Curves
related:
  - COSH
  - EXP
  - SEC
  - SINH
  - TANH
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/sech-function
  - https://support.google.com/docs/answer/9116560
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Hyperbolic Secant
tags:
  - decay
  - excel
  - hyperbolic
  - sheets
---

# SECH

## Description

**SECH** returns the hyperbolic secant of a number. It is the reciprocal of the hyperbolic cosine, so SECH(x) equals 1 divided by COSH(x). The result is always between 0 and 1 for real inputs, and it is largest at 0, where SECH(0) is 1.

Use SECH for curves that fall off smoothly on both sides of zero, such as a decaying signal, a pulse shape, or a symmetric response. Because the function is even, SECH(-x) and SECH(x) return the same value.

The input is a plain number, not an angle. It is a common mistake to convert degrees with RADIANS before calling SECH, because the hyperbolic functions do not measure circular angles. The circular version is SEC, which takes an angle in radians.

Microsoft Excel and Google Sheets both accept any real number. Excel documents a #NUM! error when the input is out of range, and results for large positive or negative inputs approach zero very quickly.

## Syntax

```excel
=SECH(number)
```

<!-- Image 1: Hyperbolic Argument Anatomy. See Images/Math & Trig/SECH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | Any real number for which you want the hyperbolic secant. The value is a plain number, not an angle in degrees. |

### Return Value

Returns a number greater than 0 and no more than 1 for real inputs. The result equals 1 when the input is 0. The function returns #NUM! when the input is outside the range Excel supports, and #VALUE! when the argument is text that cannot be read as a number.

## Examples

### Example 1: Hyperbolic Secant of One

```excel
=SECH(1)
```

**Result:** 0.6481

The hyperbolic cosine of 1 is about 1.5431. Dividing 1 by 1.5431 gives 0.6481.

### Example 2: Hyperbolic Secant of Zero

```excel
=SECH(0)
```

**Result:** 1

At zero the hyperbolic cosine is 1, so the secant is also 1. This is the peak of the SECH curve.

<!-- Image 2: Symmetric Response Curve. See Images/Math & Trig/SECH.md -->

### Example 3: Symmetry Around Zero

```excel
=SECH(-1)
```

**Result:** 0.6481

The function is even, so a negative input returns the same value as its positive counterpart. SECH(-1) equals SECH(1).

### Example 4: Response at a Large Input

```excel
=SECH(4)
```

**Result:** 0.0366

At 4 the response has already fallen to about 3.7 percent of its peak value. Large inputs produce small outputs quickly.

### Example 5: Scaled Amplitude

```excel
=10 * SECH(2)
```

**Result:** 2.6580

Multiplying by 10 scales the curve to an amplitude of 10. At x = 2, the scaled response is about 2.66.

## Story Problems

### Problem 1: Decaying Pulse Amplitude

A lab tests a pulse that starts at amplitude 10 and follows the curve 10 times SECH(t). The lab samples the pulse at four times, measured in seconds from the start.

| Time (seconds) |
| --- |
| 0 |
| 0.5 |
| 1 |
| 2 |

**Task:** Find the total of the four sampled amplitudes, rounded to two decimal places.

**Solution:**

```excel
=ROUND(SUMPRODUCT(10 * SECH(B2:B5)), 2)
```

**Answer:** `28.01`, from the amplitudes 10.00, 8.87, 6.48, and 2.66. The total is 28.0067 before rounding.

### Problem 2: Symmetric Response Check

An engineer checks that a response curve is symmetric by comparing its value at x = -1 with its value at x = 1.

| Point | x |
| --- | --- |
| Left | -1 |
| Right | 1 |

**Task:** Find the sum of the two SECH values, rounded to four decimal places.

**Solution:**

```excel
=ROUND(SECH(B2) + SECH(B3), 4)
```

**Answer:** `1.2961`, because each side returns 0.6481. Equal values on both sides confirm the curve is symmetric.

## Use Cases

### Decaying Signal Amplitude

**Scenario:** A sensor records a shock that decays on both sides of its peak, and the analyst wants the expected amplitude at each sample time.

```excel
=B2 * SECH(C2)
```

**Why It Works:** The peak amplitude in B2 is scaled by the SECH value for the sample time in C2. Keep the time scale consistent with the curve's constant, or the decay will fall too fast or too slowly.

### Symmetric Response Curves

**Scenario:** A modeler builds a symmetric response table for a range of inputs centered on zero.

```excel
=SECH(A2)
```

**Why It Works:** Because SECH is even, the table only needs one side of the curve to be checked. Values that differ on each side point to a data entry error.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input is outside the range Excel supports. | Check the input for an error from an earlier step, and reduce very large values. |
| `#VALUE!` | The argument is text, not a number. | Convert the text with VALUE or correct the source cell. |
| Very small result shown as 0 | The input is large, so the result is close to zero. | Use a scientific number format to display the small value. |
| Wrong values | A degree value was converted with RADIANS. | Pass the plain number. RADIANS is for circular angles, not hyperbolic functions. |
| Confusion with SEC | The circular and hyperbolic functions have similar names. | Use SEC for angles and SECH for hyperbolic curves. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Microsoft 365 for Mac, Excel for the web, Excel 2024, Excel 2021, Excel 2019, and Excel 2016 | Returns #NUM! when the input is out of range. |
| Google Sheets | Available | Accepts any real number. Negative inputs return the same value as positive inputs. |

## Tips and Best Practices

- Use SECH when the curve is symmetric around zero, and use SEC when the input is a circular angle in radians.
- Multiply by a peak amplitude in a separate cell, so the scale is easy to change.
- Check symmetry with one negative and one positive input when you are not sure the model is even.
- Format small outputs with scientific notation rather than rounding them to zero.
- Name the input unit in the column header, because a time or a distance is not an angle.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COSH](COSH.md) | The hyperbolic cosine. SECH(x) equals 1 divided by COSH(x). |
| [EXP](EXP.md) | Raises e to a power, which is the building block of the hyperbolic functions. |
| [SEC](SEC.md) | The circular secant, which takes an angle in radians. |
| [SINH](SINH.md) | The hyperbolic sine, used alongside SECH in hyperbolic formulas. |
| [TANH](TANH.md) | The hyperbolic tangent, the ratio of SINH to COSH. |

## Official Documentation

- [Microsoft Support: SECH function](https://support.microsoft.com/en-us/excel/functions/sech-function)
- [Google Docs Editors Help: SECH](https://support.google.com/docs/answer/9116560)
