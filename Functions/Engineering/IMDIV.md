---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
use-case:
  - Circuit Current Calculation
  - Phasor Averaging
related:
  - COMPLEX
  - IMPRODUCT
  - IMREAL
  - IMSUB
  - IMSUM
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imdiv-function
  - https://support.google.com/docs/answer/7411898
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - complex-numbers
  - division
  - excel
  - sheets
---

# IMDIV

## Description

**IMDIV** divides one complex number by another and returns the quotient as a complex number. The first argument is the numerator (dividend) and the second is the denominator (divisor). You supply each number as text in `x+yi` form, as the result of COMPLEX, or as a real number. Both numbers must use the same suffix, either `i` or `j`, so `"4+3i"` and `"1+2j"` cannot be combined.

Division of complex numbers is common in electrical engineering, where a voltage divided by an impedance gives a current. Excel returns the quotient as text, so pass it to IMREAL or IMAGINARY to read one part, or to another IM function to keep calculating. Use COMPLEX when the real and imaginary parts come from separate cells.

## Syntax

```excel
=IMDIV(inumber1, inumber2)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/IMDIV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber1` | Yes | The numerator (dividend). Google Sheets calls this argument `dividend`. |
| `inumber2` | Yes | The denominator (divisor). It cannot be zero. Google Sheets calls this argument `divisor`. |

### Return Value

The quotient of the two complex numbers, returned in `x+yi` form. Results in this guide are exact where the division comes out to whole or simple decimal parts. A zero divisor returns an error.

## Examples

### Example 1: Dividing Two Text Complex Numbers

```excel
=IMDIV("6+8i","1+2i")
```

**Result:** `4.4-0.8i`

The quotient is (6+8i) divided by (1+2i), which is 4.4 minus 0.8i.

### Example 2: Current From Voltage and Impedance

```excel
=IMDIV("220+100i","4+2i")
```

**Result:** `54-2i`

Dividing the voltage by the impedance gives the current, which is 54 minus 2i in this example.

### Example 3: Dividing by a Real Number

```excel
=IMDIV("10+5i",2)
```

**Result:** `5+2.5i`

A real divisor is treated as a complex number with an imaginary part of 0, so each part is halved.

## Story Problems

### Problem 1: Circuit Current

A lab compares two circuits. Each row lists the complex voltage and the complex impedance. The engineer needs the current in Circuit B.

| Circuit | Voltage | Impedance |
| --- | --- | --- |
| A | 220+100i | 4+2i |
| B | 120+60i | 3+4i |

**Task:** Find the current in Circuit B, which uses the voltage in cell B3 and the impedance in cell C3.

**Solution:**

```excel
=IMDIV(B3,C3)
```

**Answer:** `24-12i`. Check the result by multiplying it by the impedance: (3+4i) times (24-12i) equals 120+60i, which is the voltage.

### Problem 2: Averaging Two Phasors

A sensor logs two phasor readings. The analyst wants their average as one complex number.

| Sample | Phasor |
| --- | --- |
| 1 | 4+2i |
| 2 | 2+6i |

**Task:** Find the average of the two phasors, which sit in cells B2 and B3.

**Solution:**

```excel
=IMDIV(IMSUM(B2,B3),2)
```

**Answer:** `3+4i`. The sum is 6+8i, and dividing it by 2 gives 3+4i.

<!-- Image 2: Complex Number Worksheet. See Images/Engineering/IMDIV.md -->

## Use Cases

### Circuit Current Calculation

**Scenario:** A technician calculates the current for each circuit on a test sheet from its voltage and impedance columns.

```excel
=IMDIV(C2,D2)
```

**Why It Works:** Each row divides its own voltage by its own impedance, so the formula copies down the table without changes.

### Phasor Averaging

**Scenario:** A signal analyst averages several phasor readings taken at the same test point.

```excel
=IMDIV(IMSUM(B2:B4),3)
```

**Why It Works:** IMSUM adds the readings first and IMDIV divides the total by the count, which gives the average phasor.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error | The divisor is zero, such as `0+0i`. | Test the divisor with IF before dividing. |
| Error | The two inputs use different suffixes, such as `i` and `j`. | Use the same suffix in both inputs. |
| Error | The text is not a complex number, for example `4 plus 2i`. | Rewrite the text as `4+2i`, or build the value with COMPLEX. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Microsoft 365 for Windows, Mac and web | Returns text in `x+yi` form. Accepts `i` or `j` suffixes, which must match. |
| Google Sheets | Available | Arguments are named `dividend` and `divisor`. Mixed suffixes are not allowed. |

## Tips and Best Practices

- Use COMPLEX when the real and imaginary parts come from separate cells.
- Keep both inputs on the same suffix, and use `i` throughout a workbook.
- Use IMREAL or IMAGINARY to read one part of the quotient as a number.
- Test the divisor before dividing when a column may contain blanks or zeros.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds the complex number from real and imaginary parts. |
| [IMPRODUCT](IMPRODUCT.md) | Multiplies complex numbers, the reverse operation. |
| [IMREAL](IMREAL.md) | Returns the real part of a complex result. |
| [IMSUB](IMSUB.md) | Subtracts complex numbers. |
| [IMSUM](IMSUM.md) | Adds complex numbers, used before division to get an average. |

## Official Documentation

- [Microsoft Support: IMDIV function](https://support.microsoft.com/en-us/excel/functions/imdiv-function)
- [Google Docs Editors Help: IMDIV](https://support.google.com/docs/answer/7411898)
