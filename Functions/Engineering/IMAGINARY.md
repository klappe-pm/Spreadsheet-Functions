---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
use-case:
  - AC Reactance Extraction
  - Phasor Component Reporting
related:
  - COMPLEX
  - IMABS
  - IMARGUMENT
  - IMCONJUGATE
  - IMREAL
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imaginary-function
  - https://support.google.com/docs/answer/7408639
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Imaginary Coefficient
tags:
  - complex-numbers
  - excel
  - sheets
---

# IMAGINARY

## Description

**IMAGINARY** returns the imaginary coefficient of a complex number. For a complex number written as x + yi (or x + yj), the imaginary coefficient is y, the number that multiplies the imaginary unit.

In AC circuit analysis, the imaginary part of an impedance is the reactance, which describes how much the circuit stores and releases energy instead of dissipating it. IMAGINARY lets you pull that value out of a text entry such as `30+40i` without splitting the text by hand. Use IMREAL for the real coefficient and IMABS for the overall size of the value.

If the text has no imaginary part, IMAGINARY returns 0. Microsoft and Google both accept a bare imaginary term such as `4j`, which has an imaginary coefficient of 4 and no real part. The result is a real number, so it can be used directly in arithmetic or comparisons.

## Syntax

```excel
=IMAGINARY(inumber)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/IMAGINARY.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The complex number, in text form such as `"3+5i"` or `"4j"`, a cell that contains that text, or a result from COMPLEX. A real number is accepted and has an imaginary coefficient of 0. |

### Return Value

A real number: the imaginary coefficient of the complex number. It returns 0 when the input has no imaginary part. Text that is not in x + yi or x + yj form returns an error.

## Examples

### Example 1: Standard Form

```excel
=IMAGINARY("3+5i")
```

**Result:** `5`

The imaginary coefficient is the number attached to i, which is 5.

### Example 2: Bare Imaginary Term

```excel
=IMAGINARY("4j")
```

**Result:** `4`

The text has no real part. The j form works the same way as the i form.

### Example 3: Negative Imaginary Coefficient

```excel
=IMAGINARY("0-j")
```

**Result:** `-1`

The coefficient of j is negative, so the function returns -1.

### Example 4: Real Number Input

```excel
=IMAGINARY(4)
```

**Result:** `0`

A real number has no imaginary part, so the result is 0.

<!-- Image 2: Impedance Components Diagram. See Images/Engineering/IMAGINARY.md -->

## Story Problems

### Problem 1: Reactance of Each Branch

A power engineer stores the impedance of four AC branches as text in the form resistance plus reactance. The reactance is needed for a capacitor sizing report.

| Branch | Impedance |
| --- | --- |
| Pump | 30+40i |
| Fan | 8-6i |
| Lamp | 12+5i |
| Fridge | 20+0i |

**Task:** In column C, extract the reactance of each branch, then find the reactance of the fan branch in `C3`.

**Solution:**

```excel
=IMAGINARY(B2)
```

Fill the formula down to `C5`.

**Answer:** `-6` for the fan branch. The other branches return `40`, `5` and `0`. The fridge branch has no reactance because its imaginary part is zero.

### Problem 2: Phase Components of a Reading

A signal test records a phasor with an imaginary component of 9. The analyst wants that component in its own column.

**Task:** Extract the imaginary part of `2+9i` in cell `B2`.

**Solution:**

```excel
=IMAGINARY(B2)
```

**Answer:** `9`. The real part, 2, is not included in the result.

## Use Cases

### AC Reactance Extraction

**Scenario:** A facilities team exports impedance values from a meter and needs the reactance column for a capacitor bank calculation.

```excel
=IMAGINARY(Meter[Impedance])
```

**Why It Works:** The formula returns one reactance per row. Pair it with IMREAL to build a table that shows resistance and reactance side by side.

### Phasor Component Reporting

**Scenario:** A lab report lists the imaginary part of each measured phasor to show the phase shift direction.

```excel
=IF(IMAGINARY(B2)>=0,"Lagging","Leading")
```

**Why It Works:** The sign of the imaginary part decides the direction of the phase shift in this convention, so the IF test turns the number into a readable label.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error value | The text is not in x + yi or x + yj form. | Rewrite the value with a single `i` or `j` after the imaginary coefficient. |
| Unexpected `0` | The value is entered as a real number, so there is no imaginary part. | Check the source; a value such as `4` has an imaginary coefficient of 0. |
| Sign flipped | The text uses a minus sign before j, such as `0-j`, which gives -1. | Read the sign with the text, not with the number alone. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel 2019, Excel 2021, Excel 2024, Excel for Microsoft 365 and Excel for the web | Accepts `i` or `j` as the imaginary unit. |
| Google Sheets | Available | Accepts the same text forms and returns the same coefficient. |

## Tips and Best Practices

- Use IMAGINARY and IMREAL together to split a complex value into two numeric columns.
- Keep impedance text in one format, such as `R+Xi`, so every row parses the same way.
- Use COMPLEX to build the text when the parts come from separate measurement columns.
- Remember that the result is the coefficient, not the angle; use IMARGUMENT for the angle.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds the complex text from real and imaginary coefficients. |
| [IMREAL](IMREAL.md) | Returns the real coefficient, the counterpart of IMAGINARY. |
| [IMABS](IMABS.md) | Returns the overall size of the complex number. |
| [IMARGUMENT](IMARGUMENT.md) | Returns the angle of the complex number in radians. |
| [IMCONJUGATE](IMCONJUGATE.md) | Changes the sign of the imaginary coefficient. |

## Official Documentation

- [Microsoft Support: IMAGINARY function](https://support.microsoft.com/en-us/excel/functions/imaginary-function)
- [Google Docs Editors Help: IMAGINARY](https://support.google.com/docs/answer/7408639)
