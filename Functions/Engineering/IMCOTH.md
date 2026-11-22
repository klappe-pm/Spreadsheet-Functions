---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
  - Trigonometry
use-case:
  - Filter Response Analysis
  - Hyperbolic Response Modeling
related:
  - COTH
  - IMCOSH
  - IMCOT
  - IMDIV
  - IMSINH
level: 5
source:
  - https://support.google.com/docs/answer/9366256
date-created: 2026-11-22
date-revised: 2026-11-22
aliases: []
tags:
  - complex-numbers
  - hyperbolic
  - sheets
---

# IMCOTH

## Description

**IMCOTH** returns the hyperbolic cotangent of a complex number, written as coth(x+yi). It is the hyperbolic counterpart of IMCOT. You supply the number as quoted text in `x+yi` form, as the result of COMPLEX, or as a real number, and the function returns the result as a complex number. The regular COTH function accepts only real numbers.

IMCOTH is available in Google Sheets. Excel does not include it, so a workbook built in Excel should use IMDIV with IMCOSH and IMSINH, because the hyperbolic cotangent equals the hyperbolic cosine divided by the hyperbolic sine. That division gives the same result in both programs.

## Syntax

```excel
=IMCOTH(number)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/IMCOTH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The complex number as quoted text (`"2+1i"`), a COMPLEX result, or a real number. |

### Return Value

The hyperbolic cotangent of the complex number, returned as a complex number in `x+yi` form. Results in this guide are rounded to four decimal places. A value that is not a valid complex number returns an error.

## Examples

### Example 1: Hyperbolic Cotangent of a Text Complex Number

```excel
=IMCOTH("2+1i")
```

**Result:** `0.9843-0.0328i`

The text is read as a real part of 2 and an imaginary part of 1.

### Example 2: Conjugate Input

```excel
=IMCOTH("2-1i")
```

**Result:** `0.9843+0.0328i`

Changing the sign of the imaginary part gives the complex conjugate of the result in Example 1.

### Example 3: Excel Equivalent Using IMDIV

```excel
=IMDIV(IMCOSH("2+1i"),IMSINH("2+1i"))
```

**Result:** `0.9843-0.0328i`

This formula works in Excel, which has no IMCOTH. It returns the same value as Example 1.

## Story Problems

### Problem 1: Hyperbolic Ratio Check

A reviewer checks a hyperbolic ratio at one test point. The complex input sits in cell B2.

| Point | Value |
| --- | --- |
| A | 2+1i |

**Task:** Find the hyperbolic cotangent of Point A.

**Solution:**

```excel
=IMCOTH(B2)
```

**Answer:** `0.9843-0.0328i`, rounded to four decimals.

### Problem 2: Building the Result in Excel

A colleague who uses Excel needs the hyperbolic cotangent of a second point, which sits in cell B3. IMCOTH is not available there, so the calculation uses the division form.

| Point | Value |
| --- | --- |
| B | 2-1i |

**Task:** Compute the hyperbolic cotangent of Point B using IMCOSH and IMSINH.

**Solution:**

```excel
=IMDIV(IMCOSH(B3),IMSINH(B3))
```

**Answer:** `0.9843+0.0328i`, rounded to four decimals.

<!-- Image 2: Complex Number Worksheet. See Images/Engineering/IMCOTH.md -->

## Use Cases

### Hyperbolic Response Modeling

**Scenario:** A research team in Google Sheets models a hyperbolic response at a list of complex operating points.

```excel
=IMCOTH(C2)
```

**Why It Works:** The formula copies down the column, and each row returns the hyperbolic cotangent of its own input.

### Filter Response Analysis

**Scenario:** A team member who uses Excel needs the same ratio in a shared workbook, so the calculation uses IMCOSH and IMSINH instead.

```excel
=IMDIV(IMCOSH(C2),IMSINH(C2))
```

**Why It Works:** The division form uses only functions that Excel supports, so the same result is available in both programs.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` in Excel | IMCOTH is not part of Excel. | Use `=IMDIV(IMCOSH(z),IMSINH(z))` in Excel. |
| Error | The input is not a valid complex number, for example `2 plus 1i`. | Rewrite the input as `2+1i`, or build it with COMPLEX. |
| Error | The hyperbolic sine is zero at imaginary multiples of pi, so the cotangent is undefined there. | Check the input before calculating, or wrap the formula in IFERROR. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use IMDIV with IMCOSH and IMSINH, which return the same result. |
| Google Sheets | Available | Accepts quoted `x+yi` text, a COMPLEX result or a real number. |

## Tips and Best Practices

- Use IMDIV with IMCOSH and IMSINH when a workbook must open in Excel.
- Keep the input in a cell and reference it, so the same formula works for every row.
- Compare the result with IMDIV output once when you first build a workbook, to confirm both forms agree.
- Use COMPLEX when the real and imaginary parts come from separate cells.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COTH](../Math%20%26%20Trig/COTH.md) | Hyperbolic cotangent of a real number. |
| [IMCOSH](IMCOSH.md) | Hyperbolic cosine, the numerator in the division form. |
| [IMCOT](IMCOT.md) | Trigonometric cotangent of a complex number. |
| [IMDIV](IMDIV.md) | Divides complex numbers, used to build the result in Excel. |
| [IMSINH](IMSINH.md) | Hyperbolic sine, the denominator in the division form. |

## Official Documentation

- [Google Docs Editors Help: IMCOTH](https://support.google.com/docs/answer/9366256)
