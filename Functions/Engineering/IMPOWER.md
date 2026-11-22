---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
use-case:
  - Phasor Growth Modeling
  - Repeated Rotation Checks
  - Transfer Function Inversion
related:
  - COMPLEX
  - IMABS
  - IMPRODUCT
  - IMSQRT
  - POWER
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/impower-function
  - https://support.google.com/docs/answer/9003065
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Complex Power
tags:
  - complex-numbers
  - engineering
  - excel
  - sheets
---

# IMPOWER

## Description

**IMPOWER** raises a complex number to a power and returns the result as a complex number. The base is text in `x+yi` or `x+yj` form, or a complex number built with COMPLEX. The power can be a positive integer, a negative number, or a fraction.

Use IMPOWER when a repeated complex multiplication or a root is needed, such as a phasor that grows by the same complex factor each period, or a value that must be inverted. Raising a complex number to the power -1 returns its reciprocal, which is useful when a transfer function must be run backward.

For real numbers, POWER does the same job without the text handling. For products of different complex numbers rather than one number raised to a power, use IMPRODUCT. Fractional powers return the principal value of the root, which is the one with an angle between minus pi and pi.

## Syntax

```excel
=IMPOWER(inumber, number)
```

<!-- Image 1: Complex Base and Exponent. See Images/Engineering/IMPOWER.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The complex number to raise to a power, as text in `x+yi` or `x+yj` form, or the result of COMPLEX. Google Sheets calls this argument `complex_base`. |
| `number` | Yes | The power. It can be an integer, a fraction, or a negative number. It must be numeric; text returns `#VALUE!`. Google Sheets calls this argument `exponent`. |

### Return Value

A complex number in `x+yi` text form. The function returns `#VALUE!` in Excel when `number` is not numeric. Microsoft lists no other error values for this function.

## Examples

### Example 1: Squaring a Phasor

```excel
=IMPOWER("1+2i", 2)
```

**Result:** `-3+4i`

Squaring is repeated complex multiplication: (1+2i)(1+2i) equals -3+4i.

### Example 2: Cubing the Same Value

```excel
=IMPOWER("1+2i", 3)
```

**Result:** `-11-2i`

The result is the earlier square multiplied by 1+2i once more, which gives -11-2i.

### Example 3: Reciprocal With a Negative Power

```excel
=IMPOWER("1+2i", -1)
```

**Result:** `0.2-0.4i`

A power of -1 returns the reciprocal. Multiplying 1+2i by 0.2-0.4i gives 1, so the two values are inverses.

<!-- Image 2: Power Result in a Story Table. See Images/Engineering/IMPOWER.md -->

### Example 4: Guarded Exponent

```excel
=IFERROR(IMPOWER(A2, B2), "Check exponent")
```

**Result:** `Check exponent` when `B2` holds text such as `two` instead of a number.

Microsoft documents `#VALUE!` for a non-numeric power, and IFERROR turns that error into a readable message.

## Story Problems

### Problem 1: Two-Step Phasor Growth

An oscillator's phasor grows by the same complex factor each step. The starting phasor is stored in cell `B2`.

| Step | Phasor |
| --- | --- |
| Start | 1+2i |

**Task:** Find the phasor after two steps, which is the starting phasor raised to the power 2.

**Solution:**

```excel
=IMPOWER(B2, 2)
```

**Answer:** `-3+4i`, because (1+2i) multiplied by itself is -3+4i.

### Problem 2: Inverse Transfer Value

A calibration sheet needs the value that cancels a stage. The stage's complex value is `1+2i` in cell `B2`, and its inverse is the value raised to the power -1.

| Stage | Value |
| --- | --- |
| Filter | 1+2i |

**Task:** Find the inverse of the stage value, which is the value raised to the power -1.

**Solution:**

```excel
=IMPOWER(B2, -1)
```

**Answer:** `0.2-0.4i`, because multiplying this result by 1+2i gives 1.

## Use Cases

### Phasor Growth Modeling

**Scenario:** A signal model multiplies a phasor by the same factor each period. Each row holds the starting phasor and the number of periods.

```excel
=IMPOWER(A2, B2)
```

**Why It Works:** Each row returns the phasor after its own number of periods. Copy the formula down and change only the period count in column B.

### Repeated Rotation Checks

**Scenario:** An engineer tests whether a rotation factor returns to its starting value after a fixed number of steps.

```excel
=IMPOWER(B2, C2)
```

**Why It Works:** The result is compared with the starting value in a separate check cell. Compare the text with an exact match, or use IMREAL and IMAGINARY to compare each part.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The power is text or blank. | Enter a number for `number`, or wrap the call with IFERROR to flag it. |
| Error value | The base is not in `x+yi` or `x+yj` form. | Rewrite the base as text such as `"1+2i"` or build it with COMPLEX. |
| Unexpected root | A fractional power returns the principal root, not the one you expected. | Check the angle of the result with IMARGUMENT and choose the root you need. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365, and Excel for the web | Returns `#VALUE!` for a non-numeric power. |
| Google Sheets | Available | Arguments are named `complex_base` and `exponent`. The exponent must be a number. |

## Tips and Best Practices

- Use COMPLEX to build the base from numeric real and imaginary cells, which keeps the formula free of text joins.
- Use a power of -1 to get a reciprocal instead of dividing complex values by hand.
- Check the result with IMABS when the magnitude is what matters, because the magnitude of a power is the base magnitude raised to the same power.
- Use POWER instead when the base is a real number.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds the complex base from real and imaginary coefficients. |
| [IMABS](IMABS.md) | Returns the magnitude of a complex number, useful for checking a power. |
| [IMPRODUCT](IMPRODUCT.md) | Multiplies several complex numbers, for products that are not repeated powers. |
| [IMSQRT](IMSQRT.md) | Square root of a complex number, equivalent to a power of 0.5. |
| [POWER](../Math%20%26%20Trig/POWER.md) | Raises a real number to a power. |

## Official Documentation

- [Microsoft Support: IMPOWER function](https://support.microsoft.com/en-us/excel/functions/impower-function)
- [Google Docs Editors Help: IMPOWER](https://support.google.com/docs/answer/9003065)
