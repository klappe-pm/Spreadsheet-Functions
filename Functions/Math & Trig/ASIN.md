---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Trigonometry
purpose:
  - Trigonometry
use-case:
  - Conveyor Incline Checks
  - Ramp Rise Calculations
  - Slope Angle Reports
related:
  - ACOS
  - ATAN
  - DEGREES
  - RADIANS
  - SIN
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/asin-function
  - https://support.google.com/docs/answer/3093464
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Arcsine
  - Inverse Sine
tags:
  - excel
  - inverse-trig
  - sheets
  - trigonometry
---

# ASIN

## Description

**ASIN** returns the inverse sine (arcsine) of a number. It answers the question "which angle has this sine?" The input must be between -1 and 1, inclusive, and the result is an angle in radians between -pi/2 and pi/2 (about -1.5708 to 1.5708).

Use ASIN when you know the ratio of the opposite side to the hypotenuse in a right triangle, such as the rise of a ramp divided by its length. The angle is `ASIN(opposite / hypotenuse)`. When you know the adjacent side instead, use `ACOS`, and when you know the opposite and adjacent sides, use `ATAN`.

ASIN returns radians. Wrap the call in `DEGREES` to get an angle in degrees, or multiply by `180/PI()`. Because a sine value can match more than one angle, ASIN returns only the principal angle in the range above.

## Syntax

```excel
=ASIN(number)
```

<!-- Image 1: Right Triangle and the Sine Ratio. See Images/Math & Trig/ASIN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The sine of the angle you want. It must be between -1 and 1, inclusive. A cell reference or a formula result is allowed. |

### Return Value

The angle, in radians, whose sine equals `number`. The result is between -pi/2 and pi/2. An input outside the range from -1 to 1 returns `#NUM!`. Non-numeric input returns `#VALUE!`.

## Examples

### Example 1: Angle in Radians

```excel
=ASIN(0.5)
```

**Result:** `0.523599`

This is pi divided by 6, the angle whose sine is one half.

### Example 2: Negative Input in Degrees

```excel
=DEGREES(ASIN(-0.5))
```

**Result:** `-30`

A negative sine gives a negative angle, and `DEGREES` converts the result to degrees.

### Example 3: Largest Possible Result

```excel
=ASIN(1)
```

**Result:** `1.570796`

A sine of 1 corresponds to pi divided by 2, which is 90 degrees.

### Example 4: Ratio From a Cell

Opposite-over-hypotenuse ratio is 0.375 in `A2`.

```excel
=DEGREES(ASIN(A2))
```

**Result:** `22.02431`

The angle is about 22.02 degrees.

### Example 5: Guarding Against Out-of-Range Input

Ratio in `B2` is 1.2.

```excel
=IFERROR(DEGREES(ASIN(B2)),"Out of range")
```

**Result:** `Out of range`

A sine cannot be greater than 1, so `IFERROR` returns a label instead of an error.

## Story Problems

### Problem 1: Conveyor Incline

Two conveyors lift material between floors. Each belt length and its vertical rise are listed below, in meters.

| Conveyor | Rise (m) | Belt Length (m) |
| --- | --- | --- |
| C-1 | 1.5 | 4.0 |
| C-2 | 2.0 | 3.0 |

**Task:** Find the incline angle of each conveyor in degrees.

**Solution:**

```excel
=DEGREES(ASIN(B2/C2))
```

Fill the formula down from `D2` to `D3`.

**Answer:** C-1 is `22.02` degrees and C-2 is `41.81` degrees. The rise divided by the belt length gives the sine of the incline.

<!-- Image 2: Conveyor Belt Triangle. See Images/Math & Trig/ASIN.md -->

### Problem 2: Tilt Sensor Readings

A tilt sensor reports sine values for three measurements. Only values between -1 and 1 can be converted to angles.

| Measurement | Sine Value |
| --- | --- |
| T-1 | 0.8 |
| T-2 | 1.2 |
| T-3 | -0.3 |

**Task:** Count the measurements that ASIN can convert.

**Solution:**

```excel
=COUNTIFS(B2:B4,">=-1",B2:B4,"<=1")
```

**Answer:** `2`. T-1 and T-3 are valid. T-2 reads 1.2, which is outside the valid range, so the sensor must be recalibrated or the reading rechecked.

## Use Cases

### Conveyor Incline Checks

**Scenario:** A plant engineer confirms that each conveyor's incline stays below the manufacturer's maximum angle.

```excel
=DEGREES(ASIN(Rise/BeltLength))
```

**Why It Works:** The rise and belt length come from the layout drawing, so the angle updates when either measurement changes.

### Ramp Rise Calculations

**Scenario:** A facilities team designs a ramp with a fixed length and needs the angle that a given rise produces.

```excel
=ROUND(DEGREES(ASIN(Rise/Length)),1)
```

**Why It Works:** `ROUND` limits the angle to one decimal place for the design sheet.

### Slope Angle Reports

**Scenario:** A survey team records the elevation change and the distance along the slope for each site and reports the angle.

```excel
=IF(ABS(Rise/Length)<=1,DEGREES(ASIN(Rise/Length)),"Check survey")
```

**Why It Works:** The `IF` test stops out-of-range ratios from producing errors in the report.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input is less than -1 or greater than 1. | Check the ratio. The opposite side cannot be longer than the hypotenuse. |
| `#VALUE!` | The input is text that cannot be read as a number. | Convert the cell to a number. |
| Angle looks like about 0.5 | The result is in radians, not degrees. | Wrap the call in `DEGREES`. |
| `#NAME?` | The function name is misspelled. | Type `ASIN`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Returns radians. Use `DEGREES` or `180/PI()` for degrees. |
| Google Sheets | Available | Same argument and radian result. The page gives the same -1 to 1 input range. |

## Tips and Best Practices

- Use ASIN when the rise or opposite side is known, and use ACOS or ATAN for the other two common ratios.
- Check the ratio before calling ASIN. Rounding can push a value such as 1.0000001 out of range.
- Keep angles in radians inside long formulas and convert to degrees only at the output, so the unit stays consistent.
- Do not use ASIN to find an angle from the sine when the sine is a percentage. Divide the value by 100 first.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ACOS](ACOS.md) | Inverse cosine. Use it when the adjacent side is known. |
| [ATAN](ATAN.md) | Inverse tangent. Use it when the opposite and adjacent sides are known. |
| [SIN](SIN.md) | Sine. The forward function that ASIN inverts. |
| [DEGREES](DEGREES.md) | Converts the radian result of ASIN to degrees. |
| [RADIANS](RADIANS.md) | Converts a degree angle to radians before it is used as an input. |

## Official Documentation

- [Microsoft Support: ASIN function](https://support.microsoft.com/en-us/excel/functions/asin-function)
- [Google Docs Editors Help: ASIN](https://support.google.com/docs/answer/3093464)
