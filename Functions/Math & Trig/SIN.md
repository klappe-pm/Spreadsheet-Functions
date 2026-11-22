---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Trigonometry
purpose:
  - Trigonometry
use-case:
  - Ramp Height Estimates
  - Sine Wave Sampling
related:
  - ASIN
  - COS
  - DEGREES
  - PI
  - RADIANS
  - SINH
  - TAN
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/sin-function
  - https://support.google.com/docs/answer/3093447
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Sine
  - Sine of Angle
tags:
  - excel
  - radians
  - sheets
  - sine
  - trigonometry
---

# SIN

## Description

**SIN** returns the sine of an angle. The sine is the ratio of the side opposite an angle to the hypotenuse in a right triangle, and it always falls between -1 and 1. SIN is used for heights, offsets, waveforms, and any calculation where a length is multiplied by the sine of an angle.

The angle must be in radians. A formula such as SIN(30) treats 30 as 30 radians, not 30 degrees, and returns -0.9880. To work with degrees, convert the angle first with RADIANS(30), or multiply by PI()/180. Both methods return 0.5 for 30 degrees.

PI() returns the value of pi, so SIN(PI()/2) returns 1 and a quarter turn. Floating-point arithmetic can leave very small residues, such as the tiny positive result of SIN(PI()), so round the result when an exact display is needed.

Microsoft Excel and Google Sheets calculate SIN the same way. Both expect radians.

## Syntax

```excel
=SIN(number)
```

<!-- Image 1: Sine Triangle and Units. See Images/Math & Trig/SIN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The angle in radians for which you want the sine. Convert degrees with RADIANS before using them. |

### Return Value

Returns a number from -1 to 1 for the sine of the angle. The function returns #VALUE! when the argument is text that cannot be read as a number.

## Examples

### Example 1: Quarter Turn

```excel
=SIN(PI()/2)
```

**Result:** 1

A quarter turn is pi divided by 2 radians, and the sine at that angle is the maximum value, 1.

### Example 2: Thirty Degrees Converted to Radians

```excel
=SIN(RADIANS(30))
```

**Result:** 0.5

RADIANS converts 30 degrees to about 0.5236 radians. The sine at that angle is 0.5.

<!-- Image 2: Degrees Converted Before Sine. See Images/Math & Trig/SIN.md -->

### Example 3: A Single Radian

```excel
=SIN(1)
```

**Result:** 0.8415

The angle 1 is read as 1 radian, which is about 57.3 degrees. The sine is 0.8415.

### Example 4: Sine of a Full Half Turn

```excel
=SIN(PI())
```

**Result:** Approximately 1.22E-16, which is effectively zero

The exact value is zero, but floating-point arithmetic produces a very small number. Wrap the formula in ROUND, such as ROUND(SIN(PI()), 10), to display zero.

### Example 5: Negative Angle

```excel
=ROUND(SIN(RADIANS(-30)), 4)
```

**Result:** -0.5

The sine of a negative angle is the negative of the sine of the positive angle. ROUND removes the tiny floating-point error from the display.

## Story Problems

### Problem 1: Total Height of Three Ramps

A facilities team builds three access ramps. Each ramp has a length along the slope and an angle to the ground. The height of a ramp is its length multiplied by the sine of its angle.

| Ramp | Length (m) | Angle (degrees) |
| --- | --- | --- |
| North | 12 | 15 |
| East | 8 | 30 |
| South | 20 | 22 |

**Task:** Find the total height of the three ramps, rounded to two decimal places.

**Solution:**

```excel
=ROUND(SUMPRODUCT(B2:B4 * SIN(RADIANS(C2:C4))), 2)
```

**Answer:** `14.60` meters. The ramps are about 3.11, 4.00, and 7.49 meters high, and they total 14.598 before rounding.

### Problem 2: Height of a Clock Hand Tip

A clock-style gauge has a needle 10 centimeters long. The vertical height of the needle tip is the needle length multiplied by the sine of the needle angle, measured from the horizontal.

| Needle Length (cm) | Needle Angle (degrees) |
| --- | --- |
| 10 | 60 |

**Task:** Find the tip height for the 60 degree angle, rounded to two decimal places.

**Solution:**

```excel
=ROUND(10 * SIN(RADIANS(60)), 2)
```

**Answer:** `8.66` centimeters, because the sine of 60 degrees is about 0.8660.

## Use Cases

### Ramp Height Estimates

**Scenario:** A contractor knows the slope length of a ramp and the angle to the ground, and needs the height at the top to order support posts.

```excel
=B2 * SIN(RADIANS(C2))
```

**Why It Works:** The slope length in B2 multiplied by the sine of the angle gives the vertical rise. RADIANS converts the angle in C2 from degrees, so the formula returns a height in the same units as the length.

### Sine Wave Sampling

**Scenario:** A test engineer samples a vibration signal at set times and needs the expected displacement at each time.

```excel
=A2 * SIN(2 * PI() * B2 / C2)
```

**Why It Works:** A2 holds the amplitude, B2 holds the time, and C2 holds the period in the same time units. The angle 2 * PI() * B2 / C2 is in radians, so no conversion is needed.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unexpected value near -0.988 for 30 | The angle was entered in degrees, but SIN expects radians. | Wrap the angle in RADIANS, such as SIN(RADIANS(30)). |
| `#VALUE!` | An argument is text, not a number. | Convert the text with VALUE or correct the source cell. |
| Tiny nonzero result | Floating-point arithmetic at angles such as PI(). | Wrap the result in ROUND to display zero. |
| Result outside expected range | The formula multiplies by the sine but expects a cosine. | Check whether the geometry uses the side opposite the angle. |
| `#NAME?` | The function name is misspelled. | Check that the name is spelled SIN. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac, and web), Excel 2024, Excel 2021, Excel 2019, Excel 2016, and Microsoft Office | Angle is in radians. Use RADIANS or PI()/180 for degrees. |
| Google Sheets | Available | Angle is in radians, the same as Excel. |

## Tips and Best Practices

- Label angle columns with their unit, either radians or degrees, so readers know which one a value uses.
- Convert degrees once in a helper column, then reuse the radian value in every formula that needs it.
- Use ROUND for displayed results, and keep the unrounded value in calculations that follow.
- Use ASIN to find an angle from a sine value, the reverse operation.
- Check one known case, such as SIN(RADIANS(90)) equal to 1, before you trust a new formula.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ASIN](ASIN.md) | Returns the angle whose sine is a given value, the inverse of SIN. |
| [COS](COS.md) | Returns the cosine, used with SIN for the other side of a triangle. |
| [DEGREES](DEGREES.md) | Converts radians to degrees, the reverse of RADIANS. |
| [PI](PI.md) | Returns pi, which is used to express angles as fractions of a turn. |
| [RADIANS](RADIANS.md) | Converts degrees to radians before SIN is applied. |
| [SINH](SINH.md) | Returns the hyperbolic sine, which takes a plain number rather than an angle. |
| [TAN](TAN.md) | Returns the tangent, the ratio of SIN to COS. |

## Official Documentation

- [Microsoft Support: SIN function](https://support.microsoft.com/en-us/excel/functions/sin-function)
- [Google Docs Editors Help: SIN](https://support.google.com/docs/answer/3093447)
