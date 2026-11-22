---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
use-case:
  - AC Impedance Magnitude
  - Phasor Amplitude
related:
  - COMPLEX
  - IMAGINARY
  - IMARGUMENT
  - IMCONJUGATE
  - IMREAL
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imabs-function
  - https://support.google.com/docs/answer/7411899
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Complex Absolute Value
  - Complex Modulus
tags:
  - complex-numbers
  - excel
  - sheets
---

# IMABS

## Description

**IMABS** returns the absolute value, also called the modulus, of a complex number. For a complex number x + yi, the modulus is the square root of x squared plus y squared. It gives the length of the number when it is drawn as a point or arrow on the complex plane.

In electrical engineering, the modulus of an impedance gives the total opposition to current in an AC circuit, and the modulus of a phasor gives its amplitude. Use IMABS when you have the complex value as text and need its size, not its angle or its parts. Use IMARGUMENT for the angle and IMREAL or IMAGINARY for the two coefficients.

The input must be a complex number in x + yi or x + yj text form. A plain real number is treated as a complex number with an imaginary part of 0, so IMABS(5) returns 5. Use COMPLEX to build the text from separate real and imaginary coefficients.

## Syntax

```excel
=IMABS(inumber)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/IMABS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The complex number to measure, in text form such as `"3+4i"` or `"3+4j"`, a cell that contains that text, or a result from COMPLEX. A real number is accepted and treated as having no imaginary part. |

### Return Value

A nonnegative number: the modulus of the complex number. Text that is not in x + yi or x + yj form returns an error.

## Examples

### Example 1: Classic 5-12-13 Triangle

```excel
=IMABS("5+12i")
```

**Result:** `13`

The square root of 5 squared plus 12 squared is the square root of 169, which is 13.

### Example 2: Negative Coefficients

```excel
=IMABS("-3-4i")
```

**Result:** `5`

The signs of the coefficients do not matter, because both are squared.

### Example 3: Built With COMPLEX

```excel
=IMABS(COMPLEX(3, 4, "j"))
```

**Result:** `5`

COMPLEX returns the text `3+4j`, and IMABS returns the modulus of that value.

### Example 4: Real Number Input

```excel
=IMABS(7)
```

**Result:** `7`

A real number is treated as a complex number with no imaginary part, so its modulus is its absolute value.

<!-- Image 2: Impedance Triangle Diagram. See Images/Engineering/IMABS.md -->

## Story Problems

### Problem 1: Impedance of Three Branches

An electrical technician records the impedance of three AC branches in ohms. Each value is entered as text in the form resistance plus reactance, written as `R+Xi`.

| Branch | Impedance |
| --- | --- |
| Lighting | 30+40i |
| Heater | 8+6i |
| Motor | 12+5i |

**Task:** Find the total opposition to current, in ohms, for the motor branch. Place the formula in `C4` and use the text in `B4`.

**Solution:**

```excel
=IMABS(B4)
```

**Answer:** `13` ohms. The motor branch has a resistance of 12 ohms and a reactance of 5 ohms, and the modulus is the square root of 144 plus 25.

### Problem 2: Phasor Amplitude

A signal analyzer reports a phasor as `0+6j`, meaning zero real part and an imaginary part of 6. The team wants the peak amplitude.

**Task:** Calculate the amplitude of the phasor in cell `B2`.

**Solution:**

```excel
=IMABS(B2)
```

**Answer:** `6`. A phasor with no real part is a pure imaginary value, so its modulus equals the imaginary coefficient.

## Use Cases

### AC Impedance Magnitude

**Scenario:** A plant engineer compares the total opposition of each motor circuit to choose the right cable size.

```excel
=IMABS(Circuits[Impedance])
```

**Why It Works:** The formula returns one magnitude per row. Sort the results to find the branch with the largest opposition. Note that IMABS over a range may need dynamic array support in older versions of Excel.

### Phasor Amplitude Check

**Scenario:** A test lab checks that each measured phasor stays under a rated amplitude.

```excel
=IF(IMABS(B2)>RatedAmplitude,"Over Rating","Within Rating")
```

**Why It Works:** IMABS converts the complex text to a size, which an IF test can compare against the rating.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error value | The text is not in x + yi or x + yj form, for example `"3+4k"`. | Correct the text so it uses `i` or `j` as the imaginary unit. |
| Error value | A cell holds a number with a stray space or a typo. | Clean the text with TRIM, then rewrite the value in standard form. |
| Unexpected size | Two numbers are entered as separate cells instead of one complex value. | Combine the parts with COMPLEX before calling IMABS. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel 2019, Excel 2021, Excel 2024, Excel for Microsoft 365 and Excel for the web | Accepts `i` or `j` as the imaginary unit. |
| Google Sheets | Available | Accepts the same text forms and returns the same modulus. |

## Tips and Best Practices

- Store complex values as text in one cell per value, so IMABS can read them without extra parsing.
- Use COMPLEX when the real and imaginary parts are in separate cells.
- Use IMARGUMENT with IMABS to recover both the size and the angle of a phasor.
- Use IFERROR around IMABS when a column may contain blank or invalid text.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds the complex text from real and imaginary coefficients. |
| [IMAGINARY](IMAGINARY.md) | Returns the imaginary coefficient, which is the reactance in an impedance. |
| [IMARGUMENT](IMARGUMENT.md) | Returns the angle of the same complex number in radians. |
| [IMCONJUGATE](IMCONJUGATE.md) | Returns the complex conjugate, which has the same modulus. |
| [IMREAL](IMREAL.md) | Returns the real coefficient, which is the resistance in an impedance. |

## Official Documentation

- [Microsoft Support: IMABS function](https://support.microsoft.com/en-us/excel/functions/imabs-function)
- [Google Docs Editors Help: IMABS](https://support.google.com/docs/answer/7411899)
