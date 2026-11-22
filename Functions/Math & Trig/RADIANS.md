---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Trigonometry
purpose:
  - Trigonometry
  - Unit Conversion
use-case:
  - Angle Conversion for Engineering Sheets
  - Rotation Angle Inputs
  - Sine Calculation Prep
related:
  - COS
  - DEGREES
  - PI
  - SIN
  - TAN
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/radians-function
  - https://support.google.com/docs/answer/3093437
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Degrees to Radians
  - Radian Conversion
tags:
  - angles
  - conversion
  - excel
  - sheets
  - trigonometry
---

# RADIANS

## Description

**RADIANS** converts an angle from degrees to radians. A full circle is 360 degrees, or 2 times pi radians, so `=RADIANS(180)` returns pi, about 3.14159. The function takes one argument, the angle in degrees, and returns the same angle in radians.

Use RADIANS whenever an angle written in degrees feeds a trigonometric function. SIN, COS and TAN expect their input in radians. Passing degrees straight into them gives a different answer, so `=SIN(30)` returns -0.988, while `=SIN(RADIANS(30))` returns 0.5. Engineering sheets, surveying data and rotation formulas often store angles in degrees and convert them only inside the formula.

RADIANS does the reverse of DEGREES, which converts radians back to degrees. Use RADIANS only on values that are already in degrees. Converting a value that is already in radians multiplies it by about 0.01745 and produces a meaningless angle.

## Syntax

```excel
=RADIANS(angle)
```

<!-- Image 1: Degrees Into a Sine Formula. See Images/Math & Trig/RADIANS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `angle` | Yes | The angle in degrees to convert. Can be a number, a cell reference or a formula result. Negative angles and angles above 360 are accepted. |

### Return Value

A number: the angle in radians. For example, 90 degrees returns 1.5708, which is pi divided by 2. If `angle` is text that cannot be read as a number, the function returns `#VALUE!`.

<!-- Image 2: Conversion Table for Angles. See Images/Math & Trig/RADIANS.md -->

## Examples

### Example 1: Right Angle in Radians

```excel
=RADIANS(90)
```

**Result:** `1.5707963267948966`

A right angle is a quarter turn, which is pi divided by 2 radians.

### Example 2: Sixty Degrees

```excel
=ROUND(RADIANS(60), 4)
```

**Result:** `1.0472`

The rounded value is the radian measure of a 60 degree angle, which is pi divided by 3.

### Example 3: Sine of a Thirty Degree Angle

```excel
=ROUND(SIN(RADIANS(30)), 4)
```

**Result:** `0.5`

RADIANS converts 30 degrees first, and SIN then returns 0.5. Without the conversion, SIN would treat 30 as 30 radians.

### Example 4: Cosine of a Sixty Degree Angle

```excel
=ROUND(COS(RADIANS(60)), 4)
```

**Result:** `0.5`

The cosine of 60 degrees is 0.5. The formula converts the angle first, and ROUND hides the tiny floating-point difference in the stored value.

### Example 5: Tangent of a Forty Five Degree Angle in a Cell

The angle is in cell `B2` and holds `45`.

```excel
=ROUND(TAN(RADIANS(B2)), 4)
```

**Result:** `1`

The tangent of 45 degrees is 1. Keeping the angle in its own cell lets the formula update when the angle changes.

## Story Problems

### Problem 1: Horizontal Run and Rise of a Ramp

A loading ramp is 20 feet long and rises at an angle of 12 degrees from the ground. The crew needs the horizontal distance the ramp covers and the height it reaches.

| Item | Value |
| --- | --- |
| Ramp Length (feet) | 20 |
| Ramp Angle (degrees) | 12 |

**Task:** Calculate the horizontal run of the ramp, rounded to two decimal places.

**Solution:**

```excel
=ROUND(B2*COS(RADIANS(B3)), 2)
```

**Answer:** `19.56` feet. The run is the length times the cosine of 12 degrees. The height, from the sine, is 4.16 feet.

### Problem 2: Radian Value of a Dial Setting

A control dial is set to 135 degrees, and the software that reads the dial requires radians.

| Item | Value |
| --- | --- |
| Dial Setting (degrees) | 135 |

**Task:** Convert the dial setting to radians, rounded to four decimal places.

**Solution:**

```excel
=ROUND(RADIANS(B2), 4)
```

**Answer:** `2.3562` radians. The conversion multiplies 135 by pi and divides by 180, which equals 3 times pi divided by 4.

## Use Cases

### Angle Conversion for Engineering Sheets

**Scenario:** A structural engineer keeps beam slope angles in degrees, but a formula library expects radians.

```excel
=RADIANS(B2)
```

**Why It Works:** The formula converts the slope in `B2` on each row, so the engineer enters angles the way they appear on drawings. The converted value can then feed any trigonometric formula in the sheet.

### Rotation Angle Inputs

**Scenario:** A drafter moves a point around a circle by rotating it through a given angle from its starting position.

```excel
=D2*COS(RADIANS(E2))
```

**Why It Works:** The horizontal offset of a point at distance `D2` and angle `E2` equals the distance times the cosine of the angle. RADIANS makes the angle usable by COS.

### Sine Calculation Prep

**Scenario:** A surveyor computes the height of a sighting point from the distance and an angle of elevation recorded in degrees.

```excel
=F2*SIN(RADIANS(G2))
```

**Why It Works:** The vertical height equals the sloped distance times the sine of the elevation angle. Converting the angle in `G2` first prevents the sine from reading degrees as radians.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Wrong sine, cosine or tangent | The degree value was passed to a trigonometric function without RADIANS. | Wrap the angle in RADIANS before the trigonometric function. |
| Meaningless angle | The input was already in radians, so RADIANS converted it again. | Confirm the unit of the source data before converting. |
| `#VALUE!` | The angle is text, such as a label typed into the cell. | Convert the cell to a number, or re-enter the angle. |
| `#NAME?` | The function name is misspelled. | Check the spelling of RADIANS. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions | One argument. The official page gives no notes or version limits. |
| Google Sheets | Available | One argument. The official page gives the same definition and points to DEGREES for the reverse conversion. |

## Tips and Best Practices

- Convert once in a helper column when many formulas use the same angle.
- Use DEGREES to convert a radian result back to degrees for display.
- Check whether the trigonometric function expects degrees or radians before writing the formula, because Excel's SIN, COS and TAN expect radians.
- The equivalent formula `=B2*PI()/180` works when you need the conversion without the function.
- Round only the displayed result, so that the full angle is used in later calculations.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COS](COS.md) | Cosine of an angle in radians, often fed with RADIANS. |
| [DEGREES](DEGREES.md) | Converts radians back to degrees, the reverse of RADIANS. |
| [PI](PI.md) | Supplies the constant used in the conversion, 180 degrees equals pi radians. |
| [SIN](SIN.md) | Sine of an angle in radians. |
| [TAN](TAN.md) | Tangent of an angle in radians. |

## Official Documentation

- [Microsoft Support: RADIANS function](https://support.microsoft.com/en-us/excel/functions/radians-function)
- [Google Docs Editors Help: RADIANS](https://support.google.com/docs/answer/3093437)
