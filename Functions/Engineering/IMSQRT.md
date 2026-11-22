---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
use-case:
  - Pole Radius Calculations
  - Quadratic Root Finding
  - Root Method Comparison
related:
  - COMPLEX
  - IMABS
  - IMPOWER
  - IMREAL
  - SQRT
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imsqrt-function
  - https://support.google.com/docs/answer/9003168
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Complex Square Root
tags:
  - complex-numbers
  - engineering
  - excel
  - sheets
---

# IMSQRT

## Description

**IMSQRT** returns the square root of a complex number. The input is text in `x+yi` or `x+yj` form, or a complex number built with COMPLEX. The result is a complex number in the same text form, so `=IMSQRT("-3+4i")` returns `1+2i`.

Use IMSQRT when a quadratic equation has complex roots, when a pole or a root location must be found, or when a negative value needs a square root. Unlike SQRT, which returns an error for a negative number, IMSQRT accepts any complex input, including negative real numbers. A negative real input returns an imaginary result, such as `2i` for -4.

Google Sheets documents IMSQRT as equivalent to IMPOWER with an exponent of 0.5. In Excel, IMPOWER with 0.5 gives the same root and is the choice when the power is a variable.

## Syntax

```excel
=IMSQRT(inumber)
```

<!-- Image 1: Complex Input Layout. See Images/Engineering/IMSQRT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The complex number to take the square root of, as text in `x+yi` or `x+yj` form, such as `"-3+4i"`, or the result of COMPLEX. A real number is treated as a complex number with an imaginary part of 0. Google Sheets calls this argument `complex_number`. |

### Return Value

The principal square root as a complex number in `x+yi` text form. A real result such as the root of 4 is returned as 2. Microsoft lists no specific error values for this function.

## Examples

### Example 1: Negative Complex Input

```excel
=IMSQRT("-3+4i")
```

**Result:** `1+2i`

The check is (1+2i) multiplied by itself, which gives -3+4i.

### Example 2: Real Part Other Than Zero

```excel
=IMSQRT("8-6i")
```

**Result:** `3-i`

Squaring 3-i gives 9 minus 6i, minus 1, which equals 8-6i.

### Example 3: Built From Coefficients

```excel
=IMSQRT(COMPLEX(0, 2))
```

**Result:** `1+i`

COMPLEX builds the value 2i from the coefficients, and (1+i) squared is 2i.

<!-- Image 2: Root Results in a Story Table. See Images/Engineering/IMSQRT.md -->

### Example 4: Negative Real Input

```excel
=IMSQRT(16)
```

**Result:** `4`

The square root of 16 is a real number, so the result has no imaginary part. The same function accepts negative real inputs, which SQRT rejects.

## Story Problems

### Problem 1: Target Impedance Root

A design target is stored as a complex value in cell `B2`. The engineer needs its square root for the next step of a calculation.

| Quantity | Value |
| --- | --- |
| Target | -3+4i |

**Task:** Find the square root of the target value in `B2`.

**Solution:**

```excel
=IMSQRT(B2)
```

**Answer:** `1+2i`, because (1+2i) multiplied by itself equals -3+4i.

### Problem 2: Pole Radius

A filter pole is stored as `8-6i` in cell `B3`. The team takes the square root to find a simpler form for the same location in the plane.

| Quantity | Value |
| --- | --- |
| Pole | 8-6i |

**Task:** Find the square root of the pole value in `B3`.

**Solution:**

```excel
=IMSQRT(B3)
```

**Answer:** `3-i`, because (3-i) multiplied by itself equals 8-6i.

## Use Cases

### Pole Radius Calculations

**Scenario:** A signal analyst computes the square root of each pole value in a list to compare the locations on a common scale.

```excel
=IMSQRT(B2)
```

**Why It Works:** Fill the formula down the column. Each row is independent, so the list can be extended without changing the formula.

### Quadratic Root Finding

**Scenario:** A student solves a quadratic whose discriminant is negative. The square root of the discriminant gives the imaginary part of each root.

```excel
=IMSQRT(B2)
```

**Why It Works:** Because the discriminant is negative, SQRT cannot take its root. IMSQRT returns the imaginary root directly, so the quadratic formula still works.

### Root Method Comparison

**Scenario:** A reviewer checks that two methods give the same root. One column uses IMSQRT and the other uses IMPOWER with an exponent of 0.5.

```excel
=IMPOWER(B2, 0.5)
```

**Why It Works:** Both columns should match. Small rounding differences can appear in the last digits, so compare the parts with IMREAL and IMAGINARY and allow a tolerance.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` in SQRT | A negative number is passed to SQRT, which only accepts non-negative values. | Use IMSQRT, which accepts negative and complex inputs. |
| Error value | The input is not in `x+yi` or `x+yj` form. | Rewrite the value as text such as `"-3+4i"` or build it with COMPLEX. |
| Unexpected sign | The principal root is returned, so the other root with the opposite sign is not shown. | Negate the result to get the second root of a quadratic. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365, and Excel for the web | Returns complex text in `x+yi` form. The input argument is named `inumber`. |
| Google Sheets | Available | Equivalent to IMPOWER with an exponent of 0.5. The input argument is named `complex_number`. |

## Tips and Best Practices

- Use SQRT for non-negative real numbers, and IMSQRT whenever the input can be negative or complex.
- Build complex inputs with COMPLEX from numeric cells rather than joining text.
- Use IMREAL and IMAGINARY to read each part of the root in separate cells.
- Use IMPOWER with a variable exponent when the power is not always 0.5.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds the complex input from real and imaginary coefficients. |
| [IMABS](IMABS.md) | Returns the magnitude of the complex number. |
| [IMPOWER](IMPOWER.md) | Raises a complex number to any power, including 0.5. |
| [IMREAL](IMREAL.md) | Returns the real part of the root. |
| [SQRT](../Math%20%26%20Trig/SQRT.md) | Square root of a non-negative real number. |

## Official Documentation

- [Microsoft Support: IMSQRT function](https://support.microsoft.com/en-us/excel/functions/imsqrt-function)
- [Google Docs Editors Help: IMSQRT](https://support.google.com/docs/answer/9003168)
