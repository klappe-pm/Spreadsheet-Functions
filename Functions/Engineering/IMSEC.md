---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
  - Trigonometry
use-case:
  - Complex Angle Sweeps
  - Imported Angle Validation
  - Phase Response Analysis
related:
  - COMPLEX
  - IMCOS
  - IMCSC
  - IMSECH
  - SEC
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imsec-function
  - https://support.google.com/docs/answer/9366728
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

# IMSEC

## Description

**IMSEC** returns the secant of a complex number. The input is text in `x+yi` or `x+yj` form, or a complex number built with COMPLEX. The result is a complex number in the same text form, so `=IMSEC("1+1i")` returns `0.4983+0.5911i` (rounded here to four decimal places).

The secant is the reciprocal of the cosine. Use IMSEC when a model needs the secant of a complex angle, such as a frequency response that is evaluated at complex points. For a real angle, SEC returns a plain number and is the simpler choice.

Angles are in radians. Convert degrees with RADIANS before passing them in. IMSEC is one of several complex trigonometric functions; IMCOS, IMCSC and IMSECH cover the related cosine, cosecant and hyperbolic secant cases.

## Syntax

```excel
=IMSEC(inumber)
```

<!-- Image 1: Complex Angle Input. See Images/Engineering/IMSEC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The complex angle, in radians, as text in `x+yi` or `x+yj` form, such as `"1+1i"`, or the result of COMPLEX. A real number is treated as a complex number with an imaginary part of 0. Google Sheets calls this argument `number`. |

### Return Value

The secant as a complex number in `x+yi` text form. A real input returns a value with no imaginary part, such as `IMSEC(0)` returning 1. Microsoft documents `#NUM!` when the input is not in `x+yi` or `x+yj` text form and `#VALUE!` when the input is a logical value.

## Examples

### Example 1: Complex Angle as Text

```excel
=IMSEC("1+1i")
```

**Result:** `0.4983+0.5911i` (rounded to four decimal places)

The secant is evaluated at the angle 1 plus 1i radians.

### Example 2: Angle From Two Cells

Cell `A2` holds the real part (2) and cell `B2` holds the imaginary part (-1).

```excel
=IMSEC(COMPLEX(A2, B2))
```

**Result:** `-0.4131-0.6875i` (rounded to four decimal places)

COMPLEX combines the two numeric cells into the angle 2-1i.

<!-- Image 2: Complex Angle From Two Cells. See Images/Engineering/IMSEC.md -->

### Example 3: Real Angle of Zero

```excel
=IMSEC(0)
```

**Result:** `1`

The cosine of zero is 1, and the secant is its reciprocal, so the result is 1.

### Example 4: Guarded Input

```excel
=IFERROR(IMSEC(A2), "Not complex")
```

**Result:** `Not complex` when `A2` holds text that is not in `x+yi` form, such as `abc`.

Microsoft documents `#NUM!` for this input, and IFERROR gives a clear message in its place.

## Story Problems

### Problem 1: Test Point Angle

A lab evaluates the secant at two complex test angles. The angles are stored as text in `B2:B3`.

| Test Point | Angle (radians) |
| --- | --- |
| 1 | 1+1i |
| 2 | 2-1i |

**Task:** Find the secant at test point 2.

**Solution:**

```excel
=IMSEC(B3)
```

**Answer:** `-0.4131-0.6875i` (rounded to four decimal places), which is the secant of the angle 2-1i.

### Problem 2: Calibration Zero

A sensor calibration sheet uses a zero reference angle. The secant of zero is a known value that the team checks before using the sheet.

| Reference | Angle |
| --- | --- |
| Zero | 0 |

**Task:** Find the secant of the zero reference in cell `B2`, so the team can compare the result with the known value.

**Solution:**

```excel
=IMSEC(B2)
```

**Answer:** `1`, because the cosine of zero is 1 and its reciprocal is 1.

## Use Cases

### Complex Angle Sweeps

**Scenario:** An analyst evaluates the secant at a list of complex angles and keeps the results in a column next to the inputs.

```excel
=IMSEC(B2)
```

**Why It Works:** Fill the formula down the column. Each row is evaluated on its own, so one invalid angle shows an error only in its row.

### Imported Angle Validation

**Scenario:** A team imports angles from a measurement file. Some rows contain text that is not a complex number, and the report must still calculate.

```excel
=IFERROR(IMSEC(B2), "Check angle")
```

**Why It Works:** IFERROR marks the bad rows so the rest of the column can be used without manual cleanup.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input is not in `x+yi` or `x+yj` form. | Rewrite the value as text such as `"1+1i"` or build it with COMPLEX. |
| `#VALUE!` | The input is a logical value such as TRUE. | Pass a number or a complex text value instead. |
| Unexpected result | The angle is in degrees, but the function expects radians. | Convert the angle with RADIANS before calling IMSEC. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365, and Excel for the web | Returns complex text in `x+yi` form. The input argument is named `inumber`. |
| Google Sheets | Available | Returns a complex value. The input argument is named `number`. |

## Tips and Best Practices

- Use SEC instead when the angle is a real number, since SEC returns a plain number.
- Convert degrees with RADIANS before passing them to IMSEC.
- Build complex angles with COMPLEX from numeric cells to avoid text joins.
- Wrap imported data in IFERROR so one bad angle does not stop the column.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds the complex angle from real and imaginary coefficients. |
| [IMCOS](IMCOS.md) | Cosine of a complex number; the reciprocal of IMSEC. |
| [IMCSC](IMCSC.md) | Cosecant of a complex number, the sine-side counterpart. |
| [IMSECH](IMSECH.md) | Hyperbolic secant of a complex number. |
| [SEC](../Math%20%26%20Trig/SEC.md) | Secant of a real angle. |

## Official Documentation

- [Microsoft Support: IMSEC function](https://support.microsoft.com/en-us/excel/functions/imsec-function)
- [Google Docs Editors Help: IMSEC](https://support.google.com/docs/answer/9366728)
