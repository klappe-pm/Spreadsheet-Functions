---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
use-case:
  - Branch Resistance Totals
  - Coil Resistance Checks
  - Impedance Component Splitting
related:
  - COMPLEX
  - IMABS
  - IMAGINARY
  - IMARGUMENT
  - IMCONJUGATE
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imreal-function
  - https://support.google.com/docs/answer/7408138
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Real Part
tags:
  - complex-numbers
  - engineering
  - excel
  - sheets
---

# IMREAL

## Description

**IMREAL** returns the real coefficient of a complex number, which is the part written before the `i` or `j`. The input is text in `x+yi` or `x+yj` form, or a complex number built with COMPLEX. The result is a plain number, so you can use it directly in sums, comparisons and charts.

Use IMREAL when a complex value holds two quantities, such as a resistance and a reactance, and only the real quantity is needed for a total or a check. A real number passed to IMREAL is treated as a complex number with no imaginary part, so the function returns the number unchanged.

To read the imaginary coefficient instead, use IMAGINARY. To get the size of the whole value, use IMABS, and for its angle, use IMARGUMENT.

## Syntax

```excel
=IMREAL(inumber)
```

<!-- Image 1: Complex Input Layout. See Images/Engineering/IMREAL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The complex number to read, as text in `x+yi` or `x+yj` form, such as `"120+45i"`, or the result of COMPLEX. A real number is treated as having an imaginary part of 0. Google Sheets calls this argument `complex_number`. |

### Return Value

The real coefficient as a number. For `"4j"`, which has no real part, the function returns 0. Microsoft does not list specific error values for this function.

## Examples

### Example 1: Text Input

```excel
=IMREAL("120+45i")
```

**Result:** `120`

The real coefficient is the number before the `+` sign, and the `45i` term is ignored.

### Example 2: Negative Real Part

```excel
=IMREAL("-7.5-2i")
```

**Result:** `-7.5`

The real coefficient keeps its sign, so a negative real part returns a negative number.

### Example 3: Purely Imaginary Input

```excel
=IMREAL("4j")
```

**Result:** `0`

The value has no real part, so the function returns zero.

### Example 4: Built From Coefficients

```excel
=IMREAL(COMPLEX(9, -4))
```

**Result:** `9`

COMPLEX builds 9-4i from the two coefficients, and IMREAL returns the first one.

<!-- Image 2: Real Part in a Story Table. See Images/Engineering/IMREAL.md -->

## Story Problems

### Problem 1: Branch Resistance Totals

A panel has three parallel branches. Each branch impedance is written as text, and the design team needs the total of the resistive (real) parts.

| Branch | Impedance |
| --- | --- |
| A | 120+45i |
| B | 80-30i |
| C | 60+0i |

**Task:** Add the real part of each branch impedance, using the values in `B2:B4`.

**Solution:**

```excel
=IMREAL(B2)+IMREAL(B3)+IMREAL(B4)
```

**Answer:** `260`, because the real parts are 120, 80 and 60, which add to 260.

### Problem 2: Coil Resistance

A technician records the impedance of a coil as `45-12i` in cell `B2`. The resistance is the real part of that value.

| Component | Impedance |
| --- | --- |
| Coil | 45-12i |

**Task:** Extract the resistance of the coil from cell `B2`.

**Solution:**

```excel
=IMREAL(B2)
```

**Answer:** `45`, because the real coefficient of 45-12i is 45.

## Use Cases

### Branch Resistance Totals

**Scenario:** A maintenance log lists the complex impedance of every branch on a feeder, and the team needs the total real part for a quick check.

```excel
=SUMPRODUCT(--(IMREAL(B2:B9)))
```

**Why It Works:** IMREAL reads each branch, and SUMPRODUCT adds the results. The double minus converts the values to numbers in the same step. Check that every row holds valid text first, because one invalid cell breaks the total.

### Coil Resistance Checks

**Scenario:** A quality team flags any coil whose resistance falls outside a tolerance band.

```excel
=IF(ABS(IMREAL(B2)-50)<=2, "Within tolerance", "Check coil")
```

**Why It Works:** IMREAL converts the text to a number, so ordinary comparison and ABS work on it directly.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `0` | The input has no real part, such as `"4j"`. | Use IMAGINARY when you need the imaginary coefficient. |
| Error value | The input text is not in `x+yi` or `x+yj` form. | Correct the text or build the value with COMPLEX. |
| Unexpected total | A blank cell or a text label in the range is included in the sum. | Limit the range to the impedance cells only. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365, and Excel for the web | Returns a number. The input argument is named `inumber`. |
| Google Sheets | Available | Returns a number. The input argument is named `complex_number`. |

## Tips and Best Practices

- Store impedance values as COMPLEX results or as clean text so IMREAL reads them consistently.
- Pair IMREAL with IMAGINARY when a row needs both parts.
- Use IMREAL to check a real part before adding it to a total, so text errors are caught early.
- Reference a single cell per branch instead of long concatenated text strings.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds a complex number from real and imaginary coefficients. |
| [IMABS](IMABS.md) | Returns the size of the whole complex number. |
| [IMAGINARY](IMAGINARY.md) | Returns the imaginary coefficient, the counterpart to IMREAL. |
| [IMARGUMENT](IMARGUMENT.md) | Returns the angle of the complex number. |
| [IMCONJUGATE](IMCONJUGATE.md) | Flips the sign of the imaginary part. |

## Official Documentation

- [Microsoft Support: IMREAL function](https://support.microsoft.com/en-us/excel/functions/imreal-function)
- [Google Docs Editors Help: IMREAL](https://support.google.com/docs/answer/7408138)
