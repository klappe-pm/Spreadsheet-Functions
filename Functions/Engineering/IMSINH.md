---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
  - Trigonometry
use-case:
  - Complex Ramp Response Checks
  - Hyperbolic Transmission Profiles
related:
  - COMPLEX
  - IMCOSH
  - IMSECH
  - IMSIN
  - SINH
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imsinh-function
  - https://support.google.com/docs/answer/9366445
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

# IMSINH

## Description

**IMSINH** returns the hyperbolic sine of a complex number. The input is text in `x+yi` or `x+yj` form, or a complex number built with COMPLEX. The result is a complex number in the same text form, so `=IMSINH("1+1i")` returns `0.6350+1.2985i` (rounded here to four decimal places).

Use IMSINH when a model with exponential growth along one direction and oscillation along another is evaluated at complex points, such as a transmission line or a ramp response. For a real number, SINH returns a plain number and is the simpler choice.

Input angles are in radians. IMSINH is the hyperbolic counterpart of IMSIN, and it accepts the same COMPLEX and text formats.

## Syntax

```excel
=IMSINH(inumber)
```

<!-- Image 1: Complex Input for a Hyperbolic Function. See Images/Engineering/IMSINH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The complex number, as text in `x+yi` or `x+yj` form, such as `"1+1i"`, or the result of COMPLEX. A real number is treated as a complex number with an imaginary part of 0. Google Sheets calls this argument `number`. |

### Return Value

The hyperbolic sine as a complex number in `x+yi` text form. Microsoft documents `#NUM!` when the input is not in `x+yi` or `x+yj` text form and `#VALUE!` when the input is a logical value.

## Examples

### Example 1: Complex Input as Text

```excel
=IMSINH("1+1i")
```

**Result:** `0.6350+1.2985i` (rounded to four decimal places)

The function evaluates the hyperbolic sine at the complex value 1 plus 1i.

### Example 2: Input From Two Cells

Cell `A2` holds the real part (2) and cell `B2` holds the imaginary part (-1).

```excel
=IMSINH(COMPLEX(A2, B2))
```

**Result:** `1.9596-3.1658i` (rounded to four decimal places)

COMPLEX builds the value 2-1i from the two cells before IMSINH runs.

<!-- Image 2: Imaginary Part of a Result. See Images/Engineering/IMSINH.md -->

### Example 3: Real Input of Zero

```excel
=IMSINH(0)
```

**Result:** `0`

The hyperbolic sine of zero is zero.

### Example 4: Guarded Input

```excel
=IFERROR(IMSINH(A2), "Not complex")
```

**Result:** `Not complex` when `A2` holds text that is not in `x+yi` form, such as `abc`.

## Story Problems

### Problem 1: Ramp Response Point

A ramp response is sampled at a complex point stored as text in cell `B2`.

| Point | Value |
| --- | --- |
| Ramp | 1+1i |

**Task:** Find the hyperbolic sine of the ramp point in `B2`.

**Solution:**

```excel
=IMSINH(B2)
```

**Answer:** `0.6350+1.2985i` (rounded to four decimal places).

### Problem 2: Imaginary Readout

A report needs only the imaginary part of the hyperbolic sine at a second point, `2-1i`, which is stored in cell `B3`.

| Point | Value |
| --- | --- |
| Second | 2-1i |

**Task:** Find the imaginary part of the hyperbolic sine of the second point.

**Solution:**

```excel
=IMAGINARY(IMSINH(B3))
```

**Answer:** `-3.1658` (rounded to four decimal places), which is the imaginary coefficient of 1.9596-3.1658i.

## Use Cases

### Hyperbolic Transmission Profiles

**Scenario:** An engineer evaluates the hyperbolic sine at a list of complex points along a line and keeps each result beside its point.

```excel
=IMSINH(B2)
```

**Why It Works:** Fill the formula down the column. Each point is calculated on its own, so one invalid point shows an error only in its row.

### Complex Ramp Response Checks

**Scenario:** A team imports ramp points from a file. Some entries are text that is not a complex number, and the report must still run.

```excel
=IFERROR(IMSINH(B2), "Check value")
```

**Why It Works:** IFERROR flags the bad rows and keeps the valid results readable.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input is not in `x+yi` or `x+yj` form. | Rewrite the value as text such as `"1+1i"` or build it with COMPLEX. |
| `#VALUE!` | The input is a logical value such as TRUE. | Pass a number or a complex text value instead. |
| Text instead of a number | The result is complex text, so it cannot be used directly in arithmetic. | Use IMREAL or IMAGINARY to extract the part you need. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365, and Excel for the web | Returns complex text in `x+yi` form. The input argument is named `inumber`. |
| Google Sheets | Available | Returns a complex value. The input argument is named `number`. |

## Tips and Best Practices

- Use SINH for real inputs, since it returns a plain number.
- Use IMAGINARY or IMREAL to read one part of the result without parsing the text.
- Build complex inputs with COMPLEX from numeric cells rather than joining text.
- Wrap imported data in IFERROR so one invalid value does not stop the column.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds the complex input from real and imaginary coefficients. |
| [IMCOSH](IMCOSH.md) | Hyperbolic cosine of a complex number, the companion function. |
| [IMSIN](IMSIN.md) | Ordinary sine of a complex number. |
| [IMSECH](IMSECH.md) | Hyperbolic secant of a complex number. |
| [SINH](../Math%20%26%20Trig/SINH.md) | Hyperbolic sine of a real number. |

## Official Documentation

- [Microsoft Support: IMSINH function](https://support.microsoft.com/en-us/excel/functions/imsinh-function)
- [Google Docs Editors Help: IMSINH](https://support.google.com/docs/answer/9366445)
