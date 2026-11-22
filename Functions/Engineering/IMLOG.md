---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
use-case:
  - Logarithm Base Conversion
  - Measurement Logarithms
related:
  - IMDIV
  - IMLN
  - IMLOG10
  - IMLOG2
  - LOG
level: 5
source:
  - https://support.google.com/docs/answer/9366486
date-created: 2026-11-22
date-revised: 2026-11-22
aliases: []
tags:
  - complex-numbers
  - logarithm
  - sheets
---

# IMLOG

## Description

**IMLOG** returns the logarithm of a complex number for a base you choose. It divides the natural logarithm of the value by the natural logarithm of the base, so `IMLOG(z, 2)` gives the base 2 logarithm of z. You supply the value as quoted text in `x+yi` form, as the result of COMPLEX, or as a real number, and the base must be a positive real number. The result is a complex number.

IMLOG is available in Google Sheets. Excel does not include it. Use IMLOG10 for base 10 or IMLOG2 for base 2 in Excel, or use IMDIV with IMLN for any other base, because the logarithm to base b equals the natural log of the value divided by the natural log of b.

## Syntax

```excel
=IMLOG(value, base)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/IMLOG.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The complex number as quoted text (`"4+1i"`), a COMPLEX result, or a real number. It cannot be zero. |
| `base` | Yes | The base of the logarithm. It must be a positive real number. The source gives no default, so always supply it. |

### Return Value

The logarithm of the complex number for the given base, returned as a complex number. Results in this guide are rounded to four decimal places. A value that is not a valid complex number, or a base that is not a positive real number, returns an error.

## Examples

### Example 1: Base 2 Logarithm of a Text Complex Number

```excel
=IMLOG("1+2i",2)
```

**Result:** `1.1610+1.5973i`

The natural log of 1+2i is divided by the natural log of 2, which gives this value.

### Example 2: Base 2 Logarithm of a COMPLEX Result

```excel
=IMLOG(COMPLEX(3,3),2)
```

**Result:** `2.0850+1.1331i`

COMPLEX builds the value from two cells or numbers, so the same formula works for a column of inputs.

### Example 3: Base 10 Logarithm of a Real Number

```excel
=IMLOG(1000,10)
```

**Result:** `3`

A real input is treated as a complex number with an imaginary part of 0, and the base 10 logarithm of 1000 is 3.

## Story Problems

### Problem 1: Logarithm of a Measurement

A lab records a complex measurement for one sample. The analyst needs its base 10 logarithm.

| Sample | Value |
| --- | --- |
| 1 | 4+1i |

**Task:** Find the base 10 logarithm of the measurement in cell B2.

**Solution:**

```excel
=IMLOG(B2,10)
```

**Answer:** `0.6152+0.1064i`, rounded to four decimals.

### Problem 2: Building the Result in Excel

A colleague who uses Excel needs the base 2 logarithm of the same kind of measurement, but IMLOG is not available there. The calculation uses the natural log of the value divided by the natural log of 2.

| Sample | Value |
| --- | --- |
| 2 | 1+2i |

**Task:** Compute the base 2 logarithm of the value in cell B3 using IMLN and IMDIV.

**Solution:**

```excel
=IMDIV(IMLN(B3),IMLN(2))
```

**Answer:** `1.1610+1.5973i`, which matches Example 1.

<!-- Image 2: Complex Number Worksheet. See Images/Engineering/IMLOG.md -->

## Use Cases

### Logarithm Base Conversion

**Scenario:** A team converts a list of complex measurements to base 10 logarithms for a report that uses decades.

```excel
=IMLOG(C2,10)
```

**Why It Works:** The formula copies down the column, and each row returns the base 10 logarithm of its own value.

### Measurement Logarithms

**Scenario:** A lab compares base 2 logarithms of several complex readings in a shared Google Sheets file.

```excel
=IMLOG(C3,2)
```

**Why It Works:** Choosing base 2 in the second argument keeps the base visible, so reviewers can see which logarithm each cell holds.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error | The base is zero, negative or not a real number. | Use a positive real number for the base. |
| Error | The base is 1, because the natural log of 1 is zero and the division has no answer. | Choose a base other than 1. |
| `#NAME?` in Excel | IMLOG is not part of Excel. | Use `=IMDIV(IMLN(value),IMLN(base))`, or IMLOG10 and IMLOG2 for bases 10 and 2. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use IMLOG10 for base 10, IMLOG2 for base 2, or IMDIV with IMLN for any base. |
| Google Sheets | Available | Accepts quoted `x+yi` text, a COMPLEX result or a real number. The base must be a positive real number. |

## Tips and Best Practices

- Keep the base in its own cell so a reviewer can change it without editing the formula.
- Use COMPLEX when the real and imaginary parts come from separate cells.
- Use IMREAL or IMAGINARY to read one part of the result as a number.
- Use IMDIV with IMLN when a workbook must open in Excel.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IMDIV](IMDIV.md) | Divides complex numbers, used to build any base in Excel. |
| [IMLN](IMLN.md) | Natural logarithm of a complex number, the building block for IMLOG. |
| [IMLOG10](IMLOG10.md) | Base 10 logarithm of a complex number, available in Excel. |
| [IMLOG2](IMLOG2.md) | Base 2 logarithm of a complex number, available in Excel. |
| [LOG](../Math%20%26%20Trig/LOG.md) | Logarithm of a real number for a chosen base. |

## Official Documentation

- [Google Docs Editors Help: IMLOG](https://support.google.com/docs/answer/9366486)
