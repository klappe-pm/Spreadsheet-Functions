---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
  - Trigonometry
use-case:
  - Filter Response Analysis
  - Signal Phase Modeling
related:
  - COMPLEX
  - COSH
  - IMABS
  - IMCOS
  - IMSINH
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imcosh-function
  - https://support.google.com/docs/answer/9366233
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - complex-numbers
  - excel
  - hyperbolic
  - sheets
---

# IMCOSH

## Description

**IMCOSH** returns the hyperbolic cosine of a complex number, written as cosh(x+yi). You supply the number as text in `x+yi` form (Excel also accepts `x+yj`), or as the result of COMPLEX, and the function returns another complex number. The regular COSH function accepts only real numbers. IMCOSH is used in filter response and transmission line models where the input has both a real and an imaginary part.

Build the input with COMPLEX when the parts sit in separate cells. Google Sheets also accepts a plain real number, which it treats as having an imaginary part of 0. Excel returns the result as text, so use IMABS for the magnitude, IMREAL or IMAGINARY for one part, or another IM function to keep calculating.

## Syntax

```excel
=IMCOSH(inumber)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/IMCOSH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The complex number as text (`"2+1i"` or `"2+1j"`), a COMPLEX result, or a real number. Google Sheets calls this argument `number`. |

### Return Value

The hyperbolic cosine of the complex number, returned in `x+yi` form. Results in this guide are rounded to four decimal places. Excel returns `#NUM!` when the text is not in `x+yi` or `x+yj` form and `#VALUE!` when the argument is a logical value.

## Examples

### Example 1: Hyperbolic Cosine of a Text Complex Number

```excel
=IMCOSH("2+1i")
```

**Result:** `2.0327+3.0519i`

The text is read as a real part of 2 and an imaginary part of 1.

### Example 2: Using the Identity With a Negative Imaginary Part

```excel
=IMCOSH(COMPLEX(1,-2))
```

**Result:** `-0.6421-1.0686i`

The hyperbolic cosine of a number w equals the regular cosine of i times w. Here i times (1-2i) is 2+1i, so this result equals the cosine of 2+1i.

### Example 3: Magnitude of the Result

```excel
=IMABS(IMCOSH("2+1i"))
```

**Result:** `3.6669`

IMABS returns the modulus, which is the square root of the squared real part plus the squared imaginary part.

## Story Problems

### Problem 1: Filter Gain Readings

A bench test records complex gain readings for a filter. The analyst needs the magnitude of the hyperbolic cosine for Reading A.

| Reading | Value |
| --- | --- |
| A | 2+1i |
| B | 1-2i |

**Task:** Find the magnitude of the hyperbolic cosine of Reading A, which sits in cell B2.

**Solution:**

```excel
=IMABS(IMCOSH(B2))
```

**Answer:** `3.6669`. The real part of cosh(2+1i) is about 2.0327 and the imaginary part is about 3.0519, so the magnitude is about 3.6669.

### Problem 2: Matching Two Readings

The analyst suspects that Reading B matches a standard value already on file. The check is the hyperbolic cosine of Reading B, which sits in cell B3.

**Task:** Compute the hyperbolic cosine of Reading B in one formula.

**Solution:**

```excel
=IMCOSH(B3)
```

**Answer:** `-0.6421-1.0686i`. This matches the cosine of 2+1i because cosh(1-2i) equals cos(2+1i).

<!-- Image 2: Complex Number Worksheet. See Images/Engineering/IMCOSH.md -->

## Use Cases

### Filter Response Analysis

**Scenario:** An electronics team compares the gain magnitude of several filter stages across a list of complex operating points.

```excel
=IMABS(IMCOSH(C2))
```

**Why It Works:** IMABS turns each text result into one plain number, so the team can sort or chart the magnitudes directly.

### Signal Phase Modeling

**Scenario:** A signal analyst wants only the real part of the hyperbolic cosine for each sampled phasor.

```excel
=IMREAL(IMCOSH(C2))
```

**Why It Works:** IMREAL reads the real part of the text result and gives a number that other formulas can use.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The text is not in `x+yi` or `x+yj` form, for example `2 plus 1i`. | Rewrite the text as `2+1i`, or build the value with COMPLEX. |
| `#VALUE!` | A logical value such as TRUE was passed as the argument. | Pass a complex number in text form or a real number. |
| `#VALUE!` | The text result is multiplied with an ordinary operator, as in `=IMCOSH(B2)*2`. | Use IMPRODUCT to multiply complex results. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Microsoft 365 for Windows, Mac and web | Returns text in `x+yi` form. Accepts `i` or `j` suffixes. |
| Google Sheets | Available | Accepts a COMPLEX result, a real number or quoted `x+yi` text. The argument is named `number`. |

## Tips and Best Practices

- Use IMABS to get the magnitude of a hyperbolic cosine result as a single number.
- Use COMPLEX when the real and imaginary parts come from separate cells.
- Check the input text for a missing `i` before you copy a formula down a long column.
- Keep the real and imaginary parts in separate columns when you need to chart them.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds the complex number from real and imaginary parts. |
| [COSH](../Math%20%26%20Trig/COSH.md) | Hyperbolic cosine of a real number. |
| [IMABS](IMABS.md) | Returns the magnitude of a complex result. |
| [IMCOS](IMCOS.md) | Cosine of a complex number, the trigonometric counterpart. |
| [IMSINH](IMSINH.md) | Hyperbolic sine of a complex number, used with IMCOSH to build other ratios. |

## Official Documentation

- [Microsoft Support: IMCOSH function](https://support.microsoft.com/en-us/excel/functions/imcosh-function)
- [Google Docs Editors Help: IMCOSH](https://support.google.com/docs/answer/9366233)
