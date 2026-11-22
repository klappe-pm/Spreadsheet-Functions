---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
use-case:
  - Power Calculation Setup
  - Signal Sign Reversal
related:
  - COMPLEX
  - IMABS
  - IMAGINARY
  - IMPRODUCT
  - IMREAL
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imconjugate-function
  - https://support.google.com/docs/answer/7410791
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Complex Conjugate
tags:
  - complex-numbers
  - excel
  - sheets
---

# IMCONJUGATE

## Description

**IMCONJUGATE** returns the complex conjugate of a complex number. For x + yi, the conjugate is `x - yi`: the real part stays the same and the sign of the imaginary part flips. Both values have the same modulus, which means IMABS returns the same result for either one.

The conjugate is used in AC power calculations. The complex power is the voltage phasor multiplied by the conjugate of the current phasor, and the real part of that product is the average power. It is also used to divide complex numbers, because multiplying the top and bottom by the conjugate of the denominator removes the imaginary part from the denominator.

The result is returned as text in x + yi or x + yj form. Use IMPRODUCT to multiply the conjugate by another complex value, and use IMREAL or IMAGINARY to extract a part of the result as a number.

## Syntax

```excel
=IMCONJUGATE(inumber)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/IMCONJUGATE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The complex number, in text form such as `"3+4i"`, a cell that contains that text, or a result from COMPLEX. A real number is accepted and returns the same real number. |

### Return Value

A text value in x + yi or x + yj form that holds the conjugate of the input. Text that is not a valid complex number returns an error.

## Examples

### Example 1: Basic Conjugate

```excel
=IMCONJUGATE("3+4i")
```

**Result:** `3-4i`

The real part stays 3 and the sign of the imaginary part changes from plus to minus.

### Example 2: Built With COMPLEX

```excel
=IMCONJUGATE(COMPLEX(-2, -5, "j"))
```

**Result:** `-2+5j`

COMPLEX builds the text `-2-5j`. The conjugate flips the sign of the imaginary part, so the result is `-2+5j`.

### Example 3: Conjugate Times the Original

Cell `B2` holds the text `3+4i`.

```excel
=IMPRODUCT(B2, IMCONJUGATE(B2))
```

**Result:** `25`

The product of a complex number and its conjugate is x squared plus y squared, which is 9 + 16 = 25. The imaginary part is 0, so the result displays as a plain 25.

### Example 4: Real Number Input

```excel
=IMCONJUGATE(6)
```

**Result:** `6`

A real number is its own conjugate, so the result is the same value.

<!-- Image 2: Mirror Image Across the Real Axis. See Images/Engineering/IMCONJUGATE.md -->

## Story Problems

### Problem 1: Current Phasors for a Load Study

An engineer records three current phasors in the form `real+imaginary i`. For a power calculation, each current must be replaced by its conjugate.

| Phasor | Current (A) |
| --- | --- |
| I1 | 4+3i |
| I2 | 2-5i |
| I3 | 6+0i |

**Task:** In column C, return the conjugate of each current, then return the conjugate of I2 in `C3`.

**Solution:**

```excel
=IMCONJUGATE(B2)
```

Fill the formula down to `C4`.

**Answer:** `2+5i` for I2. The other two conjugates are `4-3i` and `6`, because a zero imaginary part is not shown.

### Problem 2: Checking a Conjugate Pair

A reviewer wants to confirm that the conjugate of `7+2i` has the same modulus as the original.

**Task:** Calculate the modulus of `7+2i` in `B2` and of its conjugate in `C2`.

**Solution:**

```excel
=IMABS(B2)
```

Use `=IMABS(IMCONJUGATE(B2))` in `C2` to compare the conjugate.

**Answer:** Both return `7.2801099`, the square root of 53. A conjugate never changes the size of a complex number.

## Use Cases

### Power Calculation Setup

**Scenario:** An energy analyst computes complex power for each load from a voltage phasor and a current phasor.

```excel
=IMPRODUCT(VoltageCell, IMCONJUGATE(CurrentCell))
```

**Why It Works:** Multiplying by the conjugate of the current gives the complex power in one step. The real part of the result is the average power, and the imaginary part is the reactive power.

### Signal Sign Reversal

**Scenario:** A signal processing team flips the sign of the imaginary part of each sample to match a reference convention.

```excel
=IMCONJUGATE(SampleTable[Value])
```

**Why It Works:** The function changes only the imaginary sign, so the modulus of each sample stays the same and the magnitude checks still pass.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error value | The text is not in x + yi or x + yj form. | Rewrite the value with a valid imaginary term. |
| Unexpected sign | The input is written as `-yi` with a leading minus, so the result looks like a double negative. | Check the input text; the conjugate changes only the sign of the imaginary term. |
| Text result in a math step | The conjugate is returned as text, so it cannot be used directly in a multiplication. | Wrap it in IMPRODUCT or another complex function. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel 2019, Excel 2021, Excel 2024, Excel for Microsoft 365 and Excel for the web | Returns text in x + yi or x + yj form. |
| Google Sheets | Available | Accepts the same text forms and returns the same conjugate. |

## Tips and Best Practices

- Use IMCONJUGATE with IMPRODUCT to compute complex power or to divide complex numbers.
- Build the input with COMPLEX when the coefficients are in separate cells.
- Check the modulus with IMABS before and after conjugation when you need to confirm the value was not altered.
- Keep complex results as text inside formulas and extract parts with IMREAL or IMAGINARY only when a number is needed.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds the complex text from real and imaginary coefficients. |
| [IMABS](IMABS.md) | Returns the size of a complex number, which the conjugate does not change. |
| [IMAGINARY](IMAGINARY.md) | Returns the imaginary coefficient of the conjugate or the original value. |
| [IMPRODUCT](IMPRODUCT.md) | Multiplies the conjugate by another complex value, such as a voltage phasor. |
| [IMREAL](IMREAL.md) | Returns the real coefficient, which the conjugate keeps the same. |

## Official Documentation

- [Microsoft Support: IMCONJUGATE function](https://support.microsoft.com/en-us/excel/functions/imconjugate-function)
- [Google Docs Editors Help: IMCONJUGATE](https://support.google.com/docs/answer/7410791)
