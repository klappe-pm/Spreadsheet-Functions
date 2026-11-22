---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Trigonometry
purpose:
  - Trigonometry
use-case:
  - Height from Elevation Angle
  - Ramp Slope Planning
  - Road Grade Rise
related:
  - ATAN
  - COS
  - DEGREES
  - PI
  - RADIANS
  - SIN
  - TANH
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/tan-function
  - https://support.google.com/docs/answer/3093586
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Tangent
  - Tangent of an Angle
tags:
  - excel
  - radians
  - sheets
  - trigonometry
---

# TAN

## Description

**TAN** returns the tangent of an angle. In a right triangle, the tangent of an angle is the length of the side opposite the angle divided by the length of the side next to it (the adjacent side). Use TAN when you know an angle and one side and need the other side, such as the height of an object seen at a known angle from a known distance.

TAN expects the angle in radians, not degrees. A formula such as `=TAN(45)` treats 45 as 45 radians and returns a meaningless value. Convert degrees with `RADIANS` or multiply by `PI()/180`. Google Sheets requires radians as well.

Because the tangent equals the sine divided by the cosine, TAN returns very large values near 90 degrees (PI()/2 radians). Excel returns a large number there rather than an error, so check the input when an angle can reach that point.

## Syntax

```excel
=TAN(number)
```

<!-- Image 1: Right Triangle Height. See Images/Math & Trig/TAN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The angle in radians. Google Sheets calls this argument `angle`. Use `RADIANS(degrees)` to convert degrees first. |

### Return Value

A number: the tangent of the angle. The result can be negative for angles between PI()/2 and PI() radians, or for negative angles. Text that cannot be read as a number returns `#VALUE!`.

## Examples

### Example 1: Angle in Radians

```excel
=TAN(0.785)
```

**Result:** `0.99920`

The angle 0.785 radians is about 45 degrees, so its tangent is just under 1.

### Example 2: Converting Degrees

With `45` in cell `A2`:

```excel
=TAN(RADIANS(A2))
```

**Result:** `1`

`RADIANS` converts 45 degrees to 0.785 radians before TAN runs. The formula `=TAN(45*PI()/180)` returns the same result.

<!-- Image 2: Radians Versus Degrees Input. See Images/Math & Trig/TAN.md -->

### Example 3: Degrees Entered Without Conversion

With `45` in cell `A2`:

```excel
=TAN(A2)
```

**Result:** `1.619775`

Excel reads 45 as 45 radians, which is not 45 degrees. The result is a valid number, so the error is easy to miss. Always convert degrees.

### Example 4: Rounded Results

```excel
=ROUND(TAN(RADIANS(30)),4)
```

**Result:** `0.5774`

ROUND limits the result to four decimal places for display or for comparison with a table value.

### Example 5: Angle Near a Right Angle

```excel
=TAN(RADIANS(90))
```

**Result:** about `1.63E+16`

At 90 degrees the tangent has no finite value, so the result is a very large number. Guard formulas that might reach this angle.

## Story Problems

### Problem 1: Radio Mast Height

A field crew stands 80 meters from the base of a radio mast and measures the angle from the ground to the top of the mast. The measurements are in the table below.

| Point | Distance (m) | Angle (degrees) |
| --- | --- | --- |
| Radio Mast | 80 | 35 |
| Water Tower | 120 | 22 |
| Clock Tower | 45 | 58 |

**Task:** Find the height of the radio mast in meters. The mast is in row 2.

**Solution:**

```excel
=B2*TAN(RADIANS(C2))
```

**Answer:** `56.02` meters. The distance is the adjacent side, so height equals distance times the tangent of the angle: 80 x TAN(35 degrees) = 56.02.

<!-- Image 3: Survey Table Layout. See Images/Math & Trig/TAN.md -->

### Problem 2: Rise on a Road Section

A road crew records the length and grade angle of two road sections. The run is the horizontal length, and the rise is the vertical change in height.

| Section | Run (m) | Angle (degrees) |
| --- | --- | --- |
| North Road | 250 | 4 |
| Hill Road | 400 | 2.5 |

**Task:** Find the rise of Hill Road in meters. Hill Road is in row 3.

**Solution:**

```excel
=B3*TAN(RADIANS(C3))
```

**Answer:** `17.46` meters, because 400 x TAN(2.5 degrees) = 17.46.

## Use Cases

### Height from Elevation Angle

**Scenario:** A survey crew measures the angle to the top of a structure from a known distance and needs the height above the ground.

```excel
=B2*TAN(RADIANS(C2))
```

**Why It Works:** The distance from the base is the adjacent side, and TAN converts the angle into the ratio between the two sides. Add the instrument height if the angle was read from eye level.

### Ramp Slope Planning

**Scenario:** A designer must keep a ramp at or below a maximum slope of one unit of rise for every twelve units of run.

```excel
=IF(TAN(RADIANS(C2))>1/12,"Too steep","Within limit")
```

**Why It Works:** The tangent of the slope angle is the ratio of rise to run, so it can be compared directly with the limit. The formula uses the same unit conversion as the other examples.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is text, or a cell with text is referenced. | Convert the value to a number. |
| Plausible but wrong result | The angle is in degrees but TAN expects radians. | Wrap the angle in `RADIANS` or multiply by `PI()/180`. |
| Very large result | The angle is 90 degrees (PI()/2 radians) or close to it. | Check the angle before using the result, or limit the angle range. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions, including Excel for the web | Argument named `number`. Expects radians. |
| Google Sheets | Available | Argument named `angle`. Expects radians. |

## Tips and Best Practices

- Keep angles in degrees in the sheet and convert them inside the formula with `RADIANS`, so the input matches what people measure.
- Test with 45 degrees first. `=TAN(RADIANS(45))` should return 1, which confirms the conversion works.
- For a right triangle, multiply the adjacent side by TAN to get the opposite side, and divide the opposite side by TAN to get the adjacent side.
- Use `ATAN` to find an angle from a known tangent, then `DEGREES` to show the answer in degrees.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ATAN](ATAN.md) | Returns the angle, in radians, whose tangent you know. The inverse of TAN. |
| [COS](COS.md) | Cosine, the denominator in the sine over cosine definition of TAN. |
| [DEGREES](DEGREES.md) | Converts a result in radians, such as from ATAN, to degrees. |
| [PI](PI.md) | Supplies pi for manual conversion with `PI()/180`. |
| [RADIANS](RADIANS.md) | Converts degrees to radians before TAN. |
| [SIN](SIN.md) | Sine, the numerator in the sine over cosine definition of TAN. |
| [TANH](TANH.md) | Hyperbolic tangent, which takes plain numbers and returns values between -1 and 1. |

## Official Documentation

- [Microsoft Support: TAN function](https://support.microsoft.com/en-us/excel/functions/tan-function)
- [Google Docs Editors Help: TAN](https://support.google.com/docs/answer/3093586)
