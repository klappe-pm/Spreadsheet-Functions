---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
  - Trigonometry
use-case:
  - Damping Profile Analysis
  - Hyperbolic Pulse Shaping
  - Imported Value Screening
related:
  - COMPLEX
  - IMCOSH
  - IMSEC
  - IMSINH
  - SECH
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imsech-function
  - https://support.google.com/docs/answer/9366440
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - complex-numbers
  - engineering
  - excel
  - hyperbolic
  - sheets
---

# IMSECH

## Description

**IMSECH** returns the hyperbolic secant of a complex number. The input is text in `x+yi` or `x+yj` form, or a complex number built with COMPLEX. The result is a complex number in the same text form, so `=IMSECH("1+1i")` returns `0.4983-0.5911i` (rounded here to four decimal places).

The hyperbolic secant is the reciprocal of the hyperbolic cosine. Use IMSECH when a model with a hyperbolic shape, such as a decaying pulse or a transmission line profile, is evaluated at complex points. For a real number, SECH returns a plain number and is the simpler choice.

Input angles are in radians. IMSECH is the hyperbolic counterpart of IMSEC, which uses the ordinary secant, and it works with the same COMPLEX input format.

## Syntax

```excel
=IMSECH(inumber)
```

<!-- Image 1: Complex Input for a Hyperbolic Function. See Images/Engineering/IMSECH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The complex number, as text in `x+yi` or `x+yj` form, such as `"1+1i"`, or the result of COMPLEX. A real number is treated as a complex number with an imaginary part of 0. Google Sheets calls this argument `number`. |

### Return Value

The hyperbolic secant as a complex number in `x+yi` text form. Microsoft documents `#NUM!` when the input is not in `x+yi` or `x+yj` text form and `#VALUE!` when the input is a logical value.

## Examples

### Example 1: Complex Input as Text

```excel
=IMSECH("1+1i")
```

**Result:** `0.4983-0.5911i` (rounded to four decimal places)

The function evaluates the hyperbolic secant at the complex value 1 plus 1i.

### Example 2: Input From Two Cells

Cell `A2` holds the real part (2) and cell `B2` holds the imaginary part (-1).

```excel
=IMSECH(COMPLEX(A2, B2))
```

**Result:** `0.1512+0.2270i` (rounded to four decimal places)

COMPLEX builds the value 2-1i from the two cells before IMSECH runs.

<!-- Image 2: Input From Two Cells. See Images/Engineering/IMSECH.md -->

### Example 3: Real Input of Zero

```excel
=IMSECH(0)
```

**Result:** `1`

The hyperbolic cosine of zero is 1, so its reciprocal is also 1.

### Example 4: Guarded Input

```excel
=IFERROR(IMSECH(A2), "Not complex")
```

**Result:** `Not complex` when `A2` holds text that is not in `x+yi` form, such as `abc`.

## Story Problems

### Problem 1: Damping Profile Points

A damped pulse is sampled at two complex points. The points are stored as text in `B2:B3`.

| Point | Value |
| --- | --- |
| 1 | 1+1i |
| 2 | 2-1i |

**Task:** Find the hyperbolic secant at point 2.

**Solution:**

```excel
=IMSECH(B3)
```

**Answer:** `0.1512+0.2270i` (rounded to four decimal places).

### Problem 2: Real Sample Check

A calibration sheet stores a real sample angle of 0.5 radians in cell `B2`. The team wants the hyperbolic secant of that angle, which is a real number.

| Sample | Angle |
| --- | --- |
| Check | 0.5 |

**Task:** Find the hyperbolic secant of the sample angle in `B2`.

**Solution:**

```excel
=IMSECH(B2)
```

**Answer:** `0.8868` (rounded to four decimal places), because 1 divided by the hyperbolic cosine of 0.5 is about 0.8868.

## Use Cases

### Damping Profile Analysis

**Scenario:** An analyst evaluates the hyperbolic secant at a list of complex sample points and keeps the results in a column beside the inputs.

```excel
=IMSECH(B2)
```

**Why It Works:** Fill the formula down the column. Each row is evaluated separately, so an invalid point shows an error only in its own row.

### Imported Value Screening

**Scenario:** A team imports sample points from a data file. Some entries are text that is not a complex number, and the report must still run.

```excel
=IFERROR(IMSECH(B2), "Check point")
```

**Why It Works:** IFERROR flags the bad entries and leaves the valid rows intact.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input is not in `x+yi` or `x+yj` form. | Rewrite the value as text such as `"1+1i"` or build it with COMPLEX. |
| `#VALUE!` | The input is a logical value such as TRUE. | Pass a number or a complex text value instead. |
| Unexpected result | The angle is in degrees, but the function expects radians. | Convert the angle with RADIANS before calling IMSECH. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365, and Excel for the web | Returns complex text in `x+yi` form. The input argument is named `inumber`. |
| Google Sheets | Available | Returns a complex value. The input argument is named `number`. |

## Tips and Best Practices

- Use SECH for real inputs, since it returns a plain number.
- Convert degrees with RADIANS before calling the function.
- Build complex inputs with COMPLEX from numeric cells rather than joining text.
- Wrap imported data in IFERROR so a single invalid point does not stop the column.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds the complex input from real and imaginary coefficients. |
| [IMCOSH](IMCOSH.md) | Hyperbolic cosine of a complex number; the reciprocal of IMSECH. |
| [IMSEC](IMSEC.md) | Ordinary secant of a complex number. |
| [IMSINH](IMSINH.md) | Hyperbolic sine of a complex number. |
| [SECH](../Math%20%26%20Trig/SECH.md) | Hyperbolic secant of a real number. |

## Official Documentation

- [Microsoft Support: IMSECH function](https://support.microsoft.com/en-us/excel/functions/imsech-function)
- [Google Docs Editors Help: IMSECH](https://support.google.com/docs/answer/9366440)
