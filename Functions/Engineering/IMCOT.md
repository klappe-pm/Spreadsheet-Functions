---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
  - Trigonometry
use-case:
  - Electrical Circuit Design
  - Phase Angle Analysis
related:
  - COMPLEX
  - COT
  - IMCOS
  - IMCOTH
  - IMDIV
  - IMSIN
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imcot-function
  - https://support.google.com/docs/answer/9366254
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - complex-numbers
  - excel
  - sheets
  - trigonometry
---

# IMCOT

## Description

**IMCOT** returns the cotangent of a complex number, written as cot(x+yi). You supply the number as text in `x+yi` form (Excel also accepts `x+yj`), or as the result of COMPLEX, and the function returns the cotangent as another complex number. The regular COT function accepts only real numbers. IMCOT is useful when a phase angle or impedance ratio has both a real and an imaginary part.

The cotangent equals the cosine divided by the sine, so IMCOT gives the same result as IMDIV applied to IMCOS and IMSIN. Use IMCOT when you want the cotangent in one step, and the division form when you want to see the steps. Excel returns the result as text, so use IMREAL or IMAGINARY to read one part.

## Syntax

```excel
=IMCOT(inumber)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/IMCOT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The complex number as text (`"2+1i"` or `"2+1j"`), a COMPLEX result, or a real number. Google Sheets calls this argument `number`. |

### Return Value

The cotangent of the complex number, returned in `x+yi` form. Results in this guide are rounded to four decimal places. Excel returns `#NUM!` when the text is not in `x+yi` or `x+yj` form and `#VALUE!` when the argument is a logical value.

## Examples

### Example 1: Cotangent of a Text Complex Number

```excel
=IMCOT("2+1i")
```

**Result:** `-0.1714-0.8213i`

The text is read as a real part of 2 and an imaginary part of 1.

### Example 2: Cotangent From COMPLEX

```excel
=IMCOT(COMPLEX(1,-2))
```

**Result:** `0.0328+0.9843i`

COMPLEX builds the number from two separate values, which keeps the input readable when the parts come from other cells.

### Example 3: Same Result From Cosine Divided by Sine

```excel
=IMDIV(IMCOS("2+1i"),IMSIN("2+1i"))
```

**Result:** `-0.1714-0.8213i`

Because the cotangent is the cosine divided by the sine, this formula returns the same value as Example 1.

## Story Problems

### Problem 1: Phase Angle Ratio

A sensor reports a phasor for each of two measurement points. The engineer needs the cotangent of the phasor for Sensor A.

| Sensor | Phasor |
| --- | --- |
| A | 2+1i |
| B | 1+1i |

**Task:** Find the cotangent of the phasor for Sensor A, which sits in cell B2.

**Solution:**

```excel
=IMCOT(B2)
```

**Answer:** `-0.1714-0.8213i`, rounded to four decimals.

### Problem 2: Cotangent Without IMCOT

A reviewer needs the cotangent of Sensor B but wants to see each step. The phasor for Sensor B sits in cell B3.

**Task:** Compute the cotangent of Sensor B as the cosine divided by the sine.

**Solution:**

```excel
=IMDIV(IMCOS(B3),IMSIN(B3))
```

**Answer:** `0.2176-0.8680i`. This matches IMCOT(B3), because the cotangent is the cosine divided by the sine.

<!-- Image 2: Complex Number Worksheet. See Images/Engineering/IMCOT.md -->

## Use Cases

### Phase Angle Analysis

**Scenario:** A test engineer reviews a column of phasors and needs the cotangent of each one to compare phase angle ratios.

```excel
=IMCOT(C2)
```

**Why It Works:** The formula copies down the column, and each row returns the cotangent of its own phasor as text.

### Electrical Circuit Design

**Scenario:** A designer shows the cosine and sine steps in a worksheet so a reviewer can follow the calculation.

```excel
=IMDIV(IMCOS(C2),IMSIN(C2))
```

**Why It Works:** Splitting the calculation into cosine and sine cells keeps each step visible and easy to check against the textbook formula.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The text is not in `x+yi` or `x+yj` form, for example `2 plus 1i`. | Rewrite the text as `2+1i`, or build the value with COMPLEX. |
| `#VALUE!` | A logical value such as TRUE was passed as the argument. | Pass a complex number in text form or a real number. |
| Error at a sine of zero | The sine is zero at real multiples of pi, so the cotangent is undefined there. | Check the input before dividing, or wrap the formula in IFERROR with a message. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Microsoft 365 for Windows, Mac and web | Returns text in `x+yi` form. Accepts `i` or `j` suffixes. |
| Google Sheets | Available | Accepts a COMPLEX result, a real number or quoted `x+yi` text. The argument is named `number`. |

## Tips and Best Practices

- Use IMCOT for a single step, and the IMDIV form when a reviewer needs to see the cosine and sine.
- Use COMPLEX when the real and imaginary parts come from separate cells.
- Read the result with IMREAL or IMAGINARY before you compare it with a plain number.
- Wrap the formula in IFERROR when the input range may include a value where the sine is zero.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds the complex number from real and imaginary parts. |
| [COT](../Math%20%26%20Trig/COT.md) | Cotangent of a real number. |
| [IMCOS](IMCOS.md) | Cosine of a complex number, used in the division form. |
| [IMCOTH](IMCOTH.md) | Hyperbolic cotangent of a complex number. |
| [IMDIV](IMDIV.md) | Divides complex numbers, used to build the cotangent from cosine and sine. |
| [IMSIN](IMSIN.md) | Sine of a complex number, used in the division form. |

## Official Documentation

- [Microsoft Support: IMCOT function](https://support.microsoft.com/en-us/excel/functions/imcot-function)
- [Google Docs Editors Help: IMCOT](https://support.google.com/docs/answer/9366254)
