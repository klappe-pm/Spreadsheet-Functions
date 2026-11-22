---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
  - Trigonometry
use-case:
  - Phase Angle Reporting
  - Phasor Direction Checks
related:
  - ATAN2
  - COMPLEX
  - DEGREES
  - IMABS
  - IMAGINARY
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imargument-function
  - https://support.google.com/docs/answer/9116360
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Complex Argument
  - Phase Angle
tags:
  - complex-numbers
  - excel
  - sheets
  - trigonometry
---

# IMARGUMENT

## Description

**IMARGUMENT** returns the argument of a complex number, also called theta or the phase angle. The argument is the angle between the positive real axis and the line from zero to the point x + yi on the complex plane, measured in radians. For a value such as `3+4i`, the angle is the inverse tangent of 4 divided by 3.

The result is in radians and falls in the range from minus pi (exclusive) to pi (inclusive). Multiply a radian value by 180 and divide by pi, or wrap the result in DEGREES, to show the angle in degrees. Use IMABS for the size of the same number.

In AC analysis, the argument of an impedance or phasor gives the phase difference between voltage and current. IMARGUMENT is the direct method when the complex value is already stored as text. Use ATAN2 instead when the real and imaginary parts are in separate cells and you do not want to build a complex value first.

## Syntax

```excel
=IMARGUMENT(inumber)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/IMARGUMENT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The complex number, in text form such as `"3+4i"`, a cell that contains that text, or a result from COMPLEX. A real number is accepted and treated as having no imaginary part. |

### Return Value

A real number: the angle theta in radians, between minus pi (exclusive) and pi (inclusive). Text that is not a valid complex number returns an error.

## Examples

### Example 1: Basic Angle

```excel
=IMARGUMENT("3+4i")
```

**Result:** `0.92729522`

The angle is the inverse tangent of 4 divided by 3, which is about 0.9273 radians.

### Example 2: Pure Imaginary Value

```excel
=IMARGUMENT(COMPLEX(0, 1))
```

**Result:** `1.570796327`

A value on the positive imaginary axis has an angle of pi divided by 2, which is about 1.5708 radians.

### Example 3: Real Number Input

```excel
=IMARGUMENT(1)
```

**Result:** `0`

A positive real number lies on the positive real axis, so its angle is 0.

### Example 4: Angle in Degrees

Cell `B2` holds the text `3+4i`.

```excel
=DEGREES(IMARGUMENT(B2))
```

**Result:** `53.13`

The argument is about 0.9273 radians, which is about 53.13 degrees.

<!-- Image 2: Angle on the Complex Plane. See Images/Engineering/IMARGUMENT.md -->

## Story Problems

### Problem 1: Phase Angle of a Motor Load

A technician records the impedance of a motor as `4+3i` ohms. The team needs the phase angle between voltage and current, in degrees, for a report.

| Load | Impedance |
| --- | --- |
| Motor A | 4+3i |

**Task:** Calculate the phase angle of Motor A in degrees, using the text in `B2`.

**Solution:**

```excel
=DEGREES(IMARGUMENT(B2))
```

**Answer:** `36.87` degrees. The angle is the inverse tangent of 3 divided by 4, which is about 0.6435 radians.

### Problem 2: Direction of a Test Phasor

A signal analyzer reports a phasor as `1+1i`. The analyst wants the direction in radians to compare against a limit of 0.75 radians.

**Task:** Calculate the angle of the phasor in cell `B2`, then compare it with the limit in `C2`.

**Solution:**

```excel
=IMARGUMENT(B2)>C2
```

**Answer:** `TRUE`. The phasor's angle is 0.7854 radians, which is greater than the limit of 0.75 radians.

## Use Cases

### Phase Angle Reporting

**Scenario:** A power quality report lists the phase angle of each load in degrees for a table that management reviews each month.

```excel
=DEGREES(IMARGUMENT(Loads[Impedance]))
```

**Why It Works:** Wrapping the radian result in DEGREES makes the figures readable without a separate conversion column.

### Phasor Direction Checks

**Scenario:** A test engineer flags any measurement where the phase angle drifts beyond a tolerance.

```excel
=IF(ABS(IMARGUMENT(B2))>Tolerance,"Drift","OK")
```

**Why It Works:** The absolute value of the angle makes the test work for both leading and lagging phasors. Keep the tolerance in radians to match the function's output.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error value | The text is not a valid complex number. | Rewrite the value in x + yi or x + yj form. |
| Error value with zero | The input is 0, which has no defined angle in Google Sheets. | Test for zero with IF before calling IMARGUMENT. |
| Degrees off by a factor | The result is in radians but the report expects degrees. | Wrap the result in DEGREES. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel 2019, Excel 2021, Excel 2024, Excel for Microsoft 365 and Excel for the web | The help page does not describe the result for a zero input. |
| Google Sheets | Available | Returns an error when the input is 0. |

## Tips and Best Practices

- Keep the result in radians inside formulas and convert with DEGREES only for display.
- Use IF with a zero test before IMARGUMENT when a column may contain 0.
- Use IMABS with IMARGUMENT to recover both the size and the angle of the same value.
- Use ATAN2 when the real and imaginary parts are in separate cells.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ATAN2](../Math%20%26%20Trig/ATAN2.md) | Computes the angle from separate x and y values without building complex text. |
| [COMPLEX](COMPLEX.md) | Builds the complex number from real and imaginary coefficients. |
| [DEGREES](../Math%20%26%20Trig/DEGREES.md) | Converts the radian result to degrees. |
| [IMABS](IMABS.md) | Returns the size of the same complex number. |
| [IMAGINARY](IMAGINARY.md) | Returns the imaginary coefficient used in the angle calculation. |

## Official Documentation

- [Microsoft Support: IMARGUMENT function](https://support.microsoft.com/en-us/excel/functions/imargument-function)
- [Google Docs Editors Help: IMARGUMENT](https://support.google.com/docs/answer/9116360)
