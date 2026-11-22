---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
use-case:
  - Amplifier Response Checks
  - Signal Saturation Modeling
related:
  - COMPLEX
  - IMCOSH
  - IMSECH
  - IMSINH
  - IMTAN
level: 5
source:
  - https://support.google.com/docs/answer/9366655
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Complex Hyperbolic Tangent
tags:
  - complex-numbers
  - hyperbolic
  - sheets
---

# IMTANH

## Description

**IMTANH** returns the hyperbolic tangent of a complex number as text in `x+yi` form. For an input `x+yi`, it computes tanh(x+yi), which has a real part and an imaginary part of its own. A real number is treated as a complex number with an imaginary part of zero, so `IMTANH(0.75)` returns the ordinary hyperbolic tangent of 0.75.

The hyperbolic tangent is the ratio of hyperbolic sine to hyperbolic cosine. Engineers use it to model smooth limiting, where a signal rises toward a ceiling and then flattens. IMTANH applies that shape to complex values, so the real and imaginary parts can be checked together. For real numbers only, the TANH function is the simpler choice.

IMTANH is available in Google Sheets only. Microsoft Excel does not provide this function, so Excel users must build the result from IMSINH and IMCOSH, as shown in the Platform Differences section.

## Syntax

```excel
=IMTANH(number)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/IMTANH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The complex number whose hyperbolic tangent you want. Use a COMPLEX result, a real number, or text in `x+yi` form. |

### Return Value

A text string in `x+yi` form that holds tanh(x+yi). The function returns an error when the input is not a valid complex number.

## Examples

Results are shown rounded to ten decimal places.

### Example 1: Hyperbolic Tangent of Complex Text

```excel
=IMTANH("2+1i")
```

**Result:** `1.0147936161+0.0338128261i`

The function evaluates tanh(2+1i). The real part is slightly above 1, which is normal for complex inputs even though the real hyperbolic tangent never exceeds 1.

### Example 2: Hyperbolic Tangent of a Real Number

```excel
=IMTANH(0.5)
```

**Result:** `0.4621171573`

A real input has an imaginary part of zero, so the result is the ordinary hyperbolic tangent of 0.5.

### Example 3: Hyperbolic Tangent of a COMPLEX Result

```excel
=IMTANH(COMPLEX(1,-1))
```

**Result:** `1.0839233273-0.2717525853i`

COMPLEX(1,-1) builds the number 1-1i, and the result is its hyperbolic tangent. The negative imaginary part in the result comes from the negative input.

<!-- Image 2: Real and Imaginary Parts of a Hyperbolic Result. See Images/Engineering/IMTANH.md -->

### Example 4: Hyperbolic Tangent From a Cell Reference

```excel
=IMTANH(B2)
```

**Result:** `0.5640831413+0.4038964553i` (with B2 holding `0.5+0.5i`)

Pointing to a cell lets the same formula run down a column of complex inputs. Keep each input in `x+yi` form.

## Story Problems

### Problem 1: Amplifier Output Near Its Limit

A lab measures the complex gain state of an amplifier stage at one operating point, stored as text in `B2`. The stage output is modeled as IMTANH of that state.

| Operating Point | State |
| --- | --- |
| Test Point A | -1+2i |

**Task:** Find the hyperbolic tangent of the stage state so the output model can be compared with the bench reading.

**Solution:**

```excel
=IMTANH(B2)
```

**Answer:** `-1.1667362572-0.2434582012i`, rounded to ten decimal places.

### Problem 2: Limiter Response for a Real Input

A limiter circuit is tested with a real input of 0.75. The test sheet keeps the input in `B2`, and the engineer needs the output scale for that input.

| Test | Input |
| --- | --- |
| Limiter Check | 0.75 |

**Task:** Find the hyperbolic tangent of the input.

**Solution:**

```excel
=IMTANH(B2)
```

**Answer:** `0.6351489524`, rounded to ten decimal places. Because the input is real, the result has no imaginary part.

## Use Cases

### Amplifier Response Checks

**Scenario:** A design team compares the modeled output of an amplifier stage at several operating points with the measured values.

```excel
=IMTANH(OperatingStates)
```

**Why It Works:** Each operating point stays in its own row, and copying the formula down gives one result per point. The real and imaginary parts show both the level and the phase shift of the limited output.

### Signal Saturation Modeling

**Scenario:** A signal engineer models how a complex input saturates toward a ceiling as its magnitude grows.

```excel
=IMTANH(COMPLEX(RealPart, ImagPart))
```

**Why It Works:** COMPLEX builds the input from two numeric columns, so the model can vary either part without rewriting text strings.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error value | The input is not a valid complex number, such as text that is not in `x+yi` form. | Rewrite the input as text such as `2+1i`, or build it with COMPLEX. |
| `#NAME?` | The function is used in Microsoft Excel, which does not provide IMTANH. | Use the Excel alternative in Platform Differences. |
| Unexpected result | The input was a degree value instead of a radian value. | Convert degrees to radians before calling the function. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use IMDIV(IMSINH(x), IMCOSH(x)), because tanh equals sinh divided by cosh. |
| Google Sheets | Available | Argument name is number. Accepts a COMPLEX result, a real number, or text in `x+yi` form. |

## Tips and Best Practices

- Keep the input in `x+yi` form so the same formula works in Google Sheets and in any workbook copied from it.
- Check one real input against the ordinary TANH function to confirm that the real-number case matches.
- Use the Excel alternative when a workbook must open in both Excel and Google Sheets.
- Round in the cell format rather than inside the formula so the full value remains available for later steps.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds the complex input from real and imaginary coefficients. |
| [IMCOSH](IMCOSH.md) | Returns the hyperbolic cosine, the denominator in the Excel alternative. |
| [IMSECH](IMSECH.md) | Returns the hyperbolic secant of the same input. |
| [IMSINH](IMSINH.md) | Returns the hyperbolic sine, the numerator in the Excel alternative. |
| [IMTAN](IMTAN.md) | Returns the circular tangent, the trigonometric counterpart of IMTANH. |

## Official Documentation

- [Google Docs Editors Help: IMTANH](https://support.google.com/docs/answer/9366655)
