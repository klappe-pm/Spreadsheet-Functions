---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
use-case:
  - Decay and Growth Modeling
  - Phasor Combination
related:
  - EXP
  - IMLN
  - IMPOWER
  - IMPRODUCT
  - IMREAL
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imexp-function
  - https://support.google.com/docs/answer/9198277
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - complex-numbers
  - excel
  - exponential
  - sheets
---

# IMEXP

## Description

**IMEXP** returns Euler's number, e (about 2.718), raised to a complex power. For an exponent x+yi, the result is e to the power x, multiplied by cos(y) plus i times sin(y). You supply the exponent as text in `x+yi` form (Excel also accepts `x+yj`), or as the result of COMPLEX, and the function returns the result as a complex number. The regular EXP function accepts only real exponents.

IMEXP is useful in decay and phase models, where a complex exponent describes a signal that both shrinks or grows and rotates. Excel returns the result as text, so use IMREAL or IMAGINARY to read one part, or IMPRODUCT to multiply several exponential results together.

## Syntax

```excel
=IMEXP(inumber)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/IMEXP.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The exponent as text (`"0+1i"` or `"0+1j"`), a COMPLEX result, or a real number. Google Sheets calls this argument `exponent`. |

### Return Value

The exponential of the complex number, returned in `x+yi` form. Results in this guide are rounded to four decimal places. Text that is not a valid complex number returns an error.

## Examples

### Example 1: Euler Form for a Pure Imaginary Exponent

```excel
=IMEXP("0+1i")
```

**Result:** `0.5403+0.8415i`

With a real part of 0, the result is cos(1) plus i times sin(1), which is Euler's formula at an angle of 1 radian.

### Example 2: Exponent With Both Parts

```excel
=IMEXP("0.5+2i")
```

**Result:** `-0.6861+1.4992i`

The real part 0.5 sets the growth factor e to the power 0.5, and the imaginary part 2 sets the rotation angle.

### Example 3: Real Part of the Result

```excel
=IMREAL(IMEXP("0.5+2i"))
```

**Result:** `-0.6861`

IMREAL returns the real part as a plain number that other formulas can compare.

## Story Problems

### Problem 1: Euler Phasor

A phase model uses an exponent of 0+1i for one channel. The analyst needs the complex exponential for that channel.

| Channel | Exponent |
| --- | --- |
| A | 0+1i |

**Task:** Find the exponential of the exponent for Channel A, which sits in cell B2.

**Solution:**

```excel
=IMEXP(B2)
```

**Answer:** `0.5403+0.8415i`, rounded to four decimals.

### Problem 2: Combined Growth Stages

Two growth stages each have a complex exponent. The analyst wants the combined effect of both stages in one value.

| Stage | Exponent |
| --- | --- |
| 1 | 1+1i |
| 2 | 0+2i |

**Task:** Multiply the exponentials of the two stages, which use cells B2 and B3.

**Solution:**

```excel
=IMPRODUCT(IMEXP(B2),IMEXP(B3))
```

**Answer:** `-2.6911+0.3836i`. Multiplying exponentials adds the exponents, so this equals the exponential of 1+3i.

<!-- Image 2: Complex Number Worksheet. See Images/Engineering/IMEXP.md -->

## Use Cases

### Decay and Growth Modeling

**Scenario:** A reliability engineer models a decaying oscillation at a list of complex decay rates.

```excel
=IMEXP(C2)
```

**Why It Works:** The formula copies down the column, and each row returns the exponential for its own exponent.

### Phasor Combination

**Scenario:** An analyst combines the effects of two stages that each have a complex exponent.

```excel
=IMPRODUCT(IMEXP(C2),IMEXP(C3))
```

**Why It Works:** IMPRODUCT multiplies the two complex results, which gives the combined effect in one cell.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error | A logical value such as TRUE was passed as the argument. | Pass a complex number in text form or a real number. |
| Error | The text is not a complex number, for example `1 plus 1i`. | Rewrite the text as `1+1i`, or build the value with COMPLEX. |
| `#VALUE!` | The text result is added with an ordinary operator, as in `=IMEXP(B2)+1`. | Use IMSUM to add complex results. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Microsoft 365 for Windows, Mac and web | Returns text in `x+yi` form. Accepts `i` or `j` suffixes. |
| Google Sheets | Available | Accepts a COMPLEX result, a real number or quoted `x+yi` text. The argument is named `exponent`. |

## Tips and Best Practices

- Use IMREAL or IMAGINARY to read one part of the result as a number.
- Use IMPRODUCT to multiply exponential results, because the exponents add.
- Use COMPLEX when the real and imaginary parts come from separate cells.
- Keep the exponent in its own column so the same formula copies down a list of stages.

## Related Functions

| Function | Relationship |
| --- | --- |
| [EXP](../Math%20%26%20Trig/EXP.md) | Exponential of a real number. |
| [IMLN](IMLN.md) | Natural logarithm of a complex number, the inverse operation. |
| [IMPOWER](IMPOWER.md) | Raises a complex number to a whole-number power. |
| [IMPRODUCT](IMPRODUCT.md) | Multiplies complex numbers, used to combine exponential results. |
| [IMREAL](IMREAL.md) | Returns the real part of a complex result. |

## Official Documentation

- [Microsoft Support: IMEXP function](https://support.microsoft.com/en-us/excel/functions/imexp-function)
- [Google Docs Editors Help: IMEXP](https://support.google.com/docs/answer/9198277)
