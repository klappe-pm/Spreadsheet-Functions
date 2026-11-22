---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
use-case:
  - Gain Factor Analysis
  - Signal Processing Logs
related:
  - IMEXP
  - IMLOG
  - IMLOG10
  - IMLOG2
  - LN
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imln-function
  - https://support.google.com/docs/answer/9000651
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - complex-numbers
  - excel
  - logarithm
  - sheets
---

# IMLN

## Description

**IMLN** returns the natural logarithm (base e) of a complex number. The result has a real part equal to the natural log of the magnitude and an imaginary part equal to the angle of the number. You supply the number as text in `x+yi` form (Excel also accepts `x+yj`), as the result of COMPLEX, or as a real number. For a real number greater than zero, IMLN gives the same value as LN. A negative real number returns an imaginary part of pi.

The natural logarithm turns products into sums, which is why it appears in gain and signal calculations. Excel returns the result as text, so use IMREAL or IMAGINARY to read one part, or IMSUM to add logarithms together. Use IMEXP to reverse the operation.

## Syntax

```excel
=IMLN(inumber)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/IMLN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The complex number as text (`"1+2i"` or `"1+2j"`), a COMPLEX result, or a real number. Google Sheets calls this argument `number`. |

### Return Value

The natural logarithm of the complex number, returned in `x+yi` form. Results in this guide are rounded to four decimal places. A zero input has no logarithm and returns an error.

## Examples

### Example 1: Natural Log of a Text Complex Number

```excel
=IMLN("1+2i")
```

**Result:** `0.8047+1.1071i`

The real part is the natural log of the magnitude, which is the square root of 5, and the imaginary part is the angle of 1+2i.

### Example 2: Natural Log of a Negative Real Number

```excel
=IMLN("-2")
```

**Result:** `0.6931+3.1416i`

The real part is the natural log of 2, and the imaginary part is pi, which is the angle of a negative number.

### Example 3: Real Part of the Result

```excel
=IMREAL(IMLN("1+2i"))
```

**Result:** `0.8047`

IMREAL returns the real part as a plain number that other formulas can use.

## Story Problems

### Problem 1: Gain Factor Logarithm

A bench test reports a complex gain factor for one stage. The analyst needs the natural logarithm of that gain.

| Gain | Value |
| --- | --- |
| G1 | 3+2i |

**Task:** Find the natural logarithm of the gain in cell B2.

**Solution:**

```excel
=IMLN(B2)
```

**Answer:** `1.2825+0.5880i`, rounded to four decimals.

### Problem 2: Log of a Product

Two signal factors are multiplied together, and the analyst wants to check that the log of the product equals the sum of the individual logs. The factors sit in cells B2 and B3.

| Factor | Value |
| --- | --- |
| 1 | 1+2i |
| 2 | 2-1i |

**Task:** Add the natural logarithms of the two factors in one formula.

**Solution:**

```excel
=IMSUM(IMLN(B2),IMLN(B3))
```

**Answer:** `1.6094+0.6435i`. The product of the two factors is 4+3i, and its natural log is the same value.

<!-- Image 2: Complex Number Worksheet. See Images/Engineering/IMLN.md -->

## Use Cases

### Gain Factor Analysis

**Scenario:** A test engineer compares the natural logarithm of each stage gain across a list of complex readings.

```excel
=IMLN(C2)
```

**Why It Works:** The formula copies down the column, and each row returns the logarithm of its own gain as text.

### Signal Processing Logs

**Scenario:** A signal analyst needs only the real part of the logarithm for each sampled value.

```excel
=IMREAL(IMLN(C2))
```

**Why It Works:** IMREAL turns the text result into a number that charts and comparisons can use directly.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The text is not in `x+yi` or `x+yj` form, for example `1 plus 2i`. | Rewrite the text as `1+2i`, or build the value with COMPLEX. |
| Error | A logical value such as TRUE was passed as the argument. | Pass a complex number in text form or a real number. |
| Error | The input is zero, which has no logarithm. | Check the input before calculating, or wrap the formula in IFERROR. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Microsoft 365 for Windows, Mac and web | Returns text in `x+yi` form. Accepts `i` or `j` suffixes. |
| Google Sheets | Available | Accepts a COMPLEX result, a real number or quoted `x+yi` text. For real numbers greater than zero, the result matches LN. |

## Tips and Best Practices

- Use IMSUM to add logarithms, which is the same as taking the log of a product.
- Use IMREAL or IMAGINARY to read one part of the result as a number.
- Use COMPLEX when the real and imaginary parts come from separate cells.
- Use IMEXP to reverse the operation and recover the original number.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IMEXP](IMEXP.md) | Exponential of a complex number, the inverse of IMLN. |
| [IMLOG](IMLOG.md) | Logarithm of a complex number for any base, available in Google Sheets. |
| [IMLOG10](IMLOG10.md) | Base 10 logarithm of a complex number. |
| [IMLOG2](IMLOG2.md) | Base 2 logarithm of a complex number. |
| [LN](../Math%20%26%20Trig/LN.md) | Natural logarithm of a real number. |

## Official Documentation

- [Microsoft Support: IMLN function](https://support.microsoft.com/en-us/excel/functions/imln-function)
- [Google Docs Editors Help: IMLN](https://support.google.com/docs/answer/9000651)
