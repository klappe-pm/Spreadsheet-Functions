---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
  - Trigonometry
use-case:
  - Alternating Current Analysis
  - Electrical Circuit Design
  - Signal Phase Modeling
related:
  - COMPLEX
  - COS
  - IMCOSH
  - IMREAL
  - IMSIN
  - IMSUM
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imcos-function
  - https://support.google.com/docs/answer/9116546
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - complex-numbers
  - excel
  - sheets
  - trigonometry
---

# IMCOS

## Description

**IMCOS** returns the cosine of a complex number. You supply the number as text in `x+yi` form (Excel also accepts `x+yj`), or as the result of COMPLEX, and the function returns the cosine as another complex number. The regular COS function accepts only real numbers. IMCOS extends the same idea to values that have an imaginary part, which appear in alternating current analysis and signal phase work.

Build the input with COMPLEX when the real and imaginary parts sit in separate cells. Google Sheets also accepts a plain real number, which it treats as a complex number with an imaginary part of 0. Excel returns the result as text, so pass it to IMREAL or IMAGINARY to read one part, to IMABS for the magnitude, or to another IM function to keep calculating.

## Syntax

```excel
=IMCOS(inumber)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/IMCOS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The complex number as text (`"2+1i"` or `"2+1j"`), a COMPLEX result, or a real number. Google Sheets calls this argument `number`. |

### Return Value

The cosine of the complex number, returned in `x+yi` form. Results in this guide are rounded to four decimal places. A logical value such as TRUE returns `#VALUE!` in Excel, and text that is not a valid complex number returns an error.

## Examples

### Example 1: Cosine of a Text Complex Number

```excel
=IMCOS("2+1i")
```

**Result:** `-0.6421-1.0686i`

The text is read as a real part of 2 and an imaginary part of 1.

### Example 2: Cosine From COMPLEX

```excel
=IMCOS(COMPLEX(3,-1))
```

**Result:** `-1.5276+0.1658i`

COMPLEX builds the number from two separate values, which is useful when the parts come from different columns.

### Example 3: Adding Two Cosines

```excel
=IMSUM(IMCOS("2+1i"),IMCOS(COMPLEX(3,-1)))
```

**Result:** `-2.1697-0.9028i`

IMSUM adds complex numbers. The real parts add to about -2.1697 and the imaginary parts add to about -0.9028.

## Story Problems

### Problem 1: Phasor Checks at Three Test Points

A test rig records a phasor at three points along a transmission line. The engineer needs the cosine of the phasor at Point A.

| Point | Phasor |
| --- | --- |
| A | 0.5+0.5i |
| B | 2+1i |
| C | 3-1i |

**Task:** Find the cosine of the phasor at Point A, which sits in cell B2.

**Solution:**

```excel
=IMCOS(B2)
```

**Answer:** `0.9896-0.2498i`, rounded to four decimals.

### Problem 2: Total Response of Two Channels

Two sensor channels report phasors into cells B2 and B3. The engineer needs the combined cosine response of both channels.

| Channel | Phasor |
| --- | --- |
| 1 | 2-1i |
| 2 | 3+1i |

**Task:** Add the cosine of channel 1 to the cosine of channel 2 in one formula.

**Solution:**

```excel
=IMSUM(IMCOS(B2),IMCOS(B3))
```

**Answer:** `-2.1698+0.9028i`. Rounded to four decimals, the channel 1 cosine is -0.6421+1.0686i and the channel 2 cosine is -1.5276-0.1658i.

<!-- Image 2: Complex Number Worksheet. See Images/Engineering/IMCOS.md -->

## Use Cases

### Alternating Current Analysis

**Scenario:** A design engineer models a load voltage as a phasor and needs its cosine to check phase relationships across a column of operating points.

```excel
=IMCOS(C2)
```

**Why It Works:** The phasor is stored as text in each row, so the same formula copies down the column and returns one cosine per operating point.

### Electrical Circuit Design

**Scenario:** A circuit designer wants only the real part of the cosine of each phasor to compare against a reference table.

```excel
=IMREAL(IMCOS(C2))
```

**Why It Works:** IMREAL reads the real part of the text result, so the output is a plain number that other formulas can compare.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A logical value such as TRUE was passed as the argument. | Pass a complex number as text, a COMPLEX result, or a real number. |
| Error | The text is not a complex number, for example `2 plus 1i` or a missing `i`. | Rewrite the text as `2+1i`, or build the value with COMPLEX. |
| `#VALUE!` | The text result is multiplied with an ordinary operator, as in `=IMCOS(B2)*2`. | Use IMPRODUCT to multiply complex results. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Microsoft 365 for Windows, Mac and web | Returns text in `x+yi` form. Accepts `i` or `j` suffixes. |
| Google Sheets | Available | Accepts a COMPLEX result, a real number or quoted `x+yi` text. The argument is named `number`. |

## Tips and Best Practices

- Use COMPLEX when the real and imaginary parts sit in separate cells.
- Wrap the result with IMREAL or IMAGINARY to read one part as a plain number.
- Use IMSUM or IMPRODUCT for arithmetic, because complex results are text.
- Confirm the angle unit and the sign convention before comparing results from different tools.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds the complex number from real and imaginary parts. |
| [COS](../Math%20%26%20Trig/COS.md) | Cosine of a real number. |
| [IMCOSH](IMCOSH.md) | Hyperbolic cosine of a complex number. |
| [IMREAL](IMREAL.md) | Returns the real part of a complex result. |
| [IMSIN](IMSIN.md) | Sine of a complex number. |
| [IMSUM](IMSUM.md) | Adds complex numbers, such as two cosine results. |

## Official Documentation

- [Microsoft Support: IMCOS function](https://support.microsoft.com/en-us/excel/functions/imcos-function)
- [Google Docs Editors Help: IMCOS](https://support.google.com/docs/answer/9116546)
