---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Trigonometry
purpose:
  - Trigonometry
use-case:
  - Cable Run Angles
  - Ramp Design
  - Sensor Mounting Angles
related:
  - ASIN
  - ATAN
  - COS
  - DEGREES
  - RADIANS
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/acos-function
  - https://support.google.com/docs/answer/3093461
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Arccosine
  - Inverse Cosine
tags:
  - excel
  - inverse-trig
  - sheets
  - trigonometry
---

# ACOS

## Description

**ACOS** returns the inverse cosine (arccosine) of a number. It answers the question "which angle has this cosine?" The input must be between -1 and 1, inclusive, and the result is an angle in radians from 0 to pi.

Use ACOS when you know the ratio of two sides of a right triangle and need the angle between them. In a right triangle, the cosine of an angle is the adjacent side divided by the hypotenuse, so the angle is `ACOS(adjacent / hypotenuse)`.

ACOS returns radians, not degrees. Wrap the result in `DEGREES` to read it as an angle in degrees. Use `ASIN` when the ratio is opposite over hypotenuse, and `ATAN` when the ratio is opposite over adjacent.

## Syntax

```excel
=ACOS(number)
```

<!-- Image 1: Right Triangle and the Cosine Ratio. See Images/Math & Trig/ACOS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The cosine of the angle you want. It must be between -1 and 1, inclusive. A cell reference or a formula result is allowed. |

### Return Value

The angle, in radians, whose cosine equals `number`. The result is between 0 and pi (about 3.14159). If `number` is less than -1 or greater than 1, Excel returns `#NUM!`. Non-numeric input returns `#VALUE!`.

## Examples

### Example 1: Angle in Radians

```excel
=ACOS(0.5)
```

**Result:** `1.047198`

This is pi divided by 3, which is the angle whose cosine is one half.

### Example 2: Angle in Degrees

```excel
=DEGREES(ACOS(0.5))
```

**Result:** `60`

`DEGREES` converts the radian result to degrees.

### Example 3: The Largest Possible Angle

```excel
=ACOS(-1)
```

**Result:** `3.141593`

A cosine of -1 occurs at 180 degrees, which is pi radians, the largest value ACOS returns.

### Example 4: Angle From a Ratio in a Cell

Adjacent-to-hypotenuse ratio is 0.8660254 in `A2`.

```excel
=DEGREES(ACOS(A2))
```

**Result:** `30`

The ratio is the cosine of 30 degrees, so the result is 30.

### Example 5: Guarding Against Out-of-Range Input

```excel
=IFERROR(DEGREES(ACOS(B2)),"Check ratio")
```

**Result:** `Check ratio` when `B2` contains 1.5

A cosine cannot be greater than 1, so the function returns an error. `IFERROR` replaces the error with a message that tells the user to check the input.

## Story Problems

### Problem 1: Cable Run Angle

A technician runs two cables from a wall box. Each cable is 4.0 meters long, and the horizontal distance each one covers is listed below.

| Cable | Horizontal (m) | Length (m) |
| --- | --- | --- |
| C-1 | 3.6 | 4.0 |
| C-2 | 2.4 | 4.0 |

**Task:** Find the angle of cable C-1 measured from the horizontal, in degrees.

**Solution:**

```excel
=DEGREES(ACOS(B2/C2))
```

**Answer:** `25.84` degrees. The cosine is 3.6 / 4.0 = 0.9, and the angle whose cosine is 0.9 is about 25.84 degrees.

<!-- Image 2: Cable Run Triangle. See Images/Math & Trig/ACOS.md -->

### Problem 2: Bracket Alignment

A bracket arm forms a right triangle. The table gives the adjacent side and the hypotenuse for two brackets, in centimeters.

| Bracket | Adjacent (cm) | Hypotenuse (cm) |
| --- | --- | --- |
| A | 25 | 100 |
| B | 60 | 80 |

**Task:** Find the angle at the base of each bracket, in degrees, filling the formula down the rows.

**Solution:**

```excel
=DEGREES(ACOS(B2/C2))
```

**Answer:** Bracket A is `75.52` degrees and bracket B is `41.41` degrees. A short adjacent side relative to the hypotenuse produces a steep angle, so bracket A is nearly upright.

## Use Cases

### Cable Run Angles

**Scenario:** An installer must confirm that each cable run leaves the wall box at a safe angle before ordering conduit.

```excel
=DEGREES(ACOS(Horizontal/Length))
```

**Why It Works:** The horizontal run and the cable length give the cosine of the angle. Check the ratio is between 0 and 1, because a horizontal run longer than the cable is physically impossible and returns `#NUM!`.

### Ramp Design

**Scenario:** A facilities team compares ramp designs by the angle each one makes with the ground.

```excel
=DEGREES(ACOS(RunLength/RampLength))
```

**Why It Works:** This form works when the ramp length is the hypotenuse and the horizontal run is the adjacent side. Use `ASIN` when the rise is known instead.

### Sensor Mounting Angles

**Scenario:** A plant engineer records the offset from a sensor mount to the target and needs the angle that keeps the sensor in view.

```excel
=ROUND(DEGREES(ACOS(Offset/Distance)),1)
```

**Why It Works:** `ROUND` limits the displayed decimals so the angle is easier to read in a report.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input is less than -1 or greater than 1. | Check the ratio. Adjacent sides cannot be longer than the hypotenuse. |
| `#VALUE!` | The input is text that cannot be read as a number. | Convert the cell to a number. |
| Angle looks like about 1 | The result is in radians, not degrees. | Wrap the call in `DEGREES`. |
| `#NAME?` | The function name is misspelled. | Type `ACOS`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions | Returns radians. Use `DEGREES` or multiply by `180/PI()` for degrees. |
| Google Sheets | Available | Same argument and radian result. The page describes the same range of -1 to 1. |

## Tips and Best Practices

- Check the ratio before calling ACOS. A small rounding error can push a value such as 1.0000001 out of range, so wrap the ratio in `MIN(1, MAX(-1, ratio))` when the source data is noisy.
- Convert to degrees with `DEGREES` in the same formula so the unit is clear to readers.
- Use `ACOS` for angles from the cosine, `ASIN` for angles from the sine, and `ATAN` for angles from the tangent.
- Use `ATAN2` when you have the opposite and adjacent sides and need the full range of directions.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ASIN](ASIN.md) | Inverse sine. Use it when the rise is known instead of the run. |
| [ATAN](ATAN.md) | Inverse tangent. Use it when the ratio is opposite over adjacent. |
| [COS](COS.md) | Cosine. The inverse of ACOS for angles in radians. |
| [DEGREES](DEGREES.md) | Converts the radian result of ACOS to degrees. |
| [RADIANS](RADIANS.md) | Converts a degree angle to radians before it is used as an input. |

## Official Documentation

- [Microsoft Support: ACOS function](https://support.microsoft.com/en-us/excel/functions/acos-function)
- [Google Docs Editors Help: ACOS](https://support.google.com/docs/answer/3093461)
