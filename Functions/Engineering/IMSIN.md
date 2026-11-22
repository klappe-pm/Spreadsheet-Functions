---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
  - Trigonometry
use-case:
  - Imported Sample Validation
  - Phasor Waveform Sampling
  - Waveform Totals
related:
  - COMPLEX
  - IMCOS
  - IMSINH
  - IMSUM
  - SIN
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imsin-function
  - https://support.google.com/docs/answer/9198962
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - complex-numbers
  - engineering
  - excel
  - sheets
  - trigonometry
---

# IMSIN

## Description

**IMSIN** returns the sine of a complex number. The input is text in `x+yi` or `x+yj` form, or a complex number built with COMPLEX. The result is a complex number in the same text form, so `=IMSIN("1+1i")` returns `1.2985+0.6350i` (rounded here to four decimal places).

Use IMSIN when a waveform, transfer function or phasor model needs the sine of a complex angle. A complex angle produces a complex result, which is how a sine wave with both growth and phase can be described in one value. For real angles, SIN returns a plain number and is simpler to use.

Angles are in radians. Convert degrees with RADIANS first. IMSIN pairs naturally with IMCOS for the cosine and with IMSUM when several complex samples must be added together.

## Syntax

```excel
=IMSIN(inumber)
```

<!-- Image 1: Complex Angle Input. See Images/Engineering/IMSIN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The complex angle, in radians, as text in `x+yi` or `x+yj` form, such as `"1+1i"`, or the result of COMPLEX. A real number is treated as a complex number with an imaginary part of 0. Google Sheets calls this argument `number`. |

### Return Value

The sine as a complex number in `x+yi` text form. A real input returns a real result, such as `IMSIN(0)` returning 0. Microsoft does not list specific error values for this function. Google Sheets returns an error when the input is not a valid complex number.

## Examples

### Example 1: Complex Angle as Text

```excel
=IMSIN("1+1i")
```

**Result:** `1.2985+0.6350i` (rounded to four decimal places)

The sine is evaluated at the angle 1 plus 1i radians.

### Example 2: Angle From Two Cells

Cell `A2` holds the real part (2) and cell `B2` holds the imaginary part (-1).

```excel
=IMSIN(COMPLEX(A2, B2))
```

**Result:** `1.4031+0.4891i` (rounded to four decimal places)

COMPLEX builds the angle 2-1i from the two cells before IMSIN evaluates it.

<!-- Image 2: Sum of Two Complex Samples. See Images/Engineering/IMSIN.md -->

### Example 3: Real Angle of Zero

```excel
=IMSIN(0)
```

**Result:** `0`

The sine of zero is zero, and the function returns that value with no imaginary part.

### Example 4: Guarded Input

```excel
=IFERROR(IMSIN(A2), "Not complex")
```

**Result:** `Not complex` when `A2` holds text that is not a complex number, such as `abc`.

## Story Problems

### Problem 1: Waveform Sample

A sensor records a complex waveform sample at two times. The samples are stored as text in `B2:B3`.

| Sample | Angle (radians) |
| --- | --- |
| 1 | 1+1i |
| 2 | 2-1i |

**Task:** Find the sine of sample 1 in cell `B2`.

**Solution:**

```excel
=IMSIN(B2)
```

**Answer:** `1.2985+0.6350i` (rounded to four decimal places).

### Problem 2: Combined Sample Value

The same two samples are added to give a combined value for a report. Each sample's sine is calculated first, and the results are then summed.

| Sample | Angle (radians) |
| --- | --- |
| 1 | 1+1i |
| 2 | 2-1i |

**Task:** Add the sines of both samples in `B2:B3`.

**Solution:**

```excel
=IMSUM(IMSIN(B2), IMSIN(B3))
```

**Answer:** `2.7016+1.1240i` (rounded to four decimal places), which is the sum of 1.2985+0.6350i and 1.4031+0.4891i.

## Use Cases

### Phasor Waveform Sampling

**Scenario:** An engineer samples a complex waveform at several angles and keeps each sine value in a column next to its input.

```excel
=IMSIN(B2)
```

**Why It Works:** Fill the formula down the column. Each sample is independent, so a bad input shows an error only in its own row.

### Imported Sample Validation

**Scenario:** A team imports angles from a measurement file, and some entries are text that is not a complex number. The report must still calculate the rest.

```excel
=IFERROR(IMSIN(B2), "Check sample")
```

**Why It Works:** IFERROR marks the invalid rows and keeps the valid results.

### Waveform Totals

**Scenario:** A report adds the sine values of several samples to get one combined figure.

```excel
=IMSUM(IMSIN(B2), IMSIN(B3), IMSIN(B4))
```

**Why It Works:** IMSUM adds complex values, so the total keeps both the real and imaginary parts.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error value | The input is not in `x+yi` or `x+yj` form. | Rewrite the value as text such as `"1+1i"` or build it with COMPLEX. |
| Unexpected result | The angle is in degrees, but the function expects radians. | Convert the angle with RADIANS before calling IMSIN. |
| Text instead of a number | The result is complex text, so it cannot be added to a number. | Use IMSUM for complex totals, or IMREAL and IMAGINARY to split the result. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365, and Excel for the web | Returns complex text in `x+yi` form. The input argument is named `inumber`. |
| Google Sheets | Available | Returns a complex value. The input argument is named `number`. |

## Tips and Best Practices

- Use SIN for real angles, since it returns a plain number.
- Convert degrees with RADIANS before calling the function.
- Use IMSUM to add complex sine values, because a plain SUM ignores the text results.
- Wrap imported data in IFERROR so one bad sample does not stop the column.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds the complex angle from real and imaginary coefficients. |
| [IMCOS](IMCOS.md) | Cosine of a complex number, the companion function to IMSIN. |
| [IMSINH](IMSINH.md) | Hyperbolic sine of a complex number. |
| [IMSUM](IMSUM.md) | Adds complex values, such as several IMSIN results. |
| [SIN](../Math%20%26%20Trig/SIN.md) | Sine of a real angle. |

## Official Documentation

- [Microsoft Support: IMSIN function](https://support.microsoft.com/en-us/excel/functions/imsin-function)
- [Google Docs Editors Help: IMSIN](https://support.google.com/docs/answer/9198962)
