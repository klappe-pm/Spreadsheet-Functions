---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Trigonometry
purpose:
  - Trigonometry
use-case:
  - Force Component Calculations
  - Ramp Horizontal Length
related:
  - ACOS
  - COSH
  - RADIANS
  - SIN
  - TAN
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/cos-function
  - https://support.google.com/docs/answer/3093476
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Cosine
tags:
  - excel
  - radians
  - sheets
  - trigonometry
---

# COS

## Description

**COS** returns the cosine of an angle, which is the ratio of the adjacent side to the hypotenuse in a right triangle. It gives the horizontal share of a length or force that points at an angle. For example, a 10 meter ramp set at 30 degrees covers a horizontal distance equal to 10 times COS of 30 degrees.

The angle must be in radians. Both Microsoft Excel and Google Sheets read the number as radians, so an angle in degrees must first be converted with `RADIANS`, or multiplied by `PI()/180`. Forgetting this step is the most common reason for a wrong result.

The result is always between -1 and 1. Use `ACOS` to go the other way and recover an angle from a cosine value, and use `COSH` for the hyperbolic version, which is a separate function with a different shape.

## Syntax

```excel
=COS(number)
```

<!-- Image 1: Angle in Radians. See Images/Math & Trig/COS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The angle in radians whose cosine you want. Google Sheets calls this argument `angle`. Convert degrees with `RADIANS` before you pass them in. |

### Return Value

A number between -1 and 1. The function returns `#VALUE!` when the argument is not numeric. Neither official page lists other error cases.

## Examples

### Example 1: Basic Usage With a Radian Value

```excel
=COS(1.047)
```

**Result:** `0.5001711`

The angle 1.047 radians, which is close to 60 degrees, has a cosine of about 0.5.

### Example 2: Converting Degrees by Hand

```excel
=COS(60 * PI() / 180)
```

**Result:** `0.5`

Multiplying degrees by PI() and dividing by 180 converts 60 degrees to radians before the cosine is taken.

### Example 3: Converting Degrees With RADIANS

```excel
=COS(RADIANS(60))
```

**Result:** `0.5`

`RADIANS` does the same conversion in one step and is easier to read.

### Example 4: The Cosine of Pi

```excel
=COS(PI())
```

**Result:** `-1`

Pi radians is a half turn, where the cosine reaches its minimum of -1.

### Example 5: A Right Angle Returns Almost Zero

```excel
=COS(RADIANS(90))
```

**Result:** `6.1E-17`

The cosine of 90 degrees is exactly 0 in mathematics. The tiny value comes from the limits of binary floating-point arithmetic, so wrap the result in `ROUND` when you need a clean zero.

## Story Problems

### Problem 1: Horizontal Length of Ramps

A facilities team measures three ramps by their slope length and angle. The horizontal distance each ramp covers determines how much floor space it needs.

| Ramp | Slope Length (m) | Angle (degrees) | Horizontal Length (m) |
| --- | --- | --- | --- |
| Dock | 12 | 15 | |
| Lobby | 8 | 30 | |
| Garage | 20 | 5 | |

**Task:** Find the horizontal length of each ramp, then total the three lengths.

**Solution:**

```excel
=B2 * COS(RADIANS(C2))
```

Copy the formula down to row 4, then total column D with `=SUM(D2:D4)`.

**Answer:** The horizontal lengths are 11.59, 6.93, and 19.92 meters, for a total of `38.44` meters.

<!-- Image 2: Ramp Horizontal Length Table. See Images/Math & Trig/COS.md -->

### Problem 2: Horizontal Share of Two Forces

Two cables pull on a sign post. Each cable's force acts at an angle from the horizontal, and the team needs the total horizontal force.

| Cable | Force (N) | Angle (degrees) | Horizontal Force (N) |
| --- | --- | --- | --- |
| Cable 1 | 50 | 40 | |
| Cable 2 | 80 | 75 | |

**Task:** Find each cable's horizontal force, then add the two values.

**Solution:**

```excel
=B2 * COS(RADIANS(C2))
```

Copy the formula down to row 3, then total column D with `=SUM(D2:D3)`.

**Answer:** Cable 1 gives 38.30 N and Cable 2 gives 20.71 N, for a total of `59.01` N.

<!-- Image 3: Horizontal Force Results. See Images/Math & Trig/COS.md -->

## Use Cases

### Ramp Horizontal Length

**Scenario:** A building manager must confirm that a ramp fits a fixed floor area before ordering it.

```excel
=SlopeLength * COS(RADIANS(Angle))
```

**Why It Works:** The horizontal length is the slope length times the cosine of the angle. Converting the angle with `RADIANS` makes the formula correct for angles entered in degrees.

### Force Component Calculations

**Scenario:** An engineer resolves a pulling force into the part that acts along a surface.

```excel
=Force * COS(RADIANS(Angle))
```

**Why It Works:** Only the component along the surface does useful work in this case, and the cosine gives that share. Check the angle reference before you copy the formula, because an angle measured from the vertical needs a different function.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Result far from expected | The angle is in degrees but was passed as radians. | Wrap the angle in `RADIANS` before the cosine is taken. |
| `#VALUE!` | The argument is text or a blank cell. | Convert the input to a number. |
| Value like `6.1E-17` | Floating-point rounding of an exact zero. | Wrap the result in `ROUND`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions and Excel for the web | Argument is named `number`. Expects radians only. |
| Google Sheets | Available | Argument is named `angle`. Expects radians only, and `RADIANS` converts degrees. |

## Tips and Best Practices

- Keep angles in degrees in the sheet and convert them with `RADIANS` inside the formula.
- Use `ROUND` on results that should be exact zero, such as the cosine of 90 degrees.
- Check one value by hand with a calculator before you fill a column.
- Use `ACOS` to recover an angle from a cosine value, and remember that it returns radians.
- Name the angle cell clearly, since a degree value passed by mistake is the most common error.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SIN](../Math%20%26%20Trig/SIN.md) | Returns the vertical share of the same angle. |
| [TAN](../Math%20%26%20Trig/TAN.md) | Returns the ratio of the vertical to the horizontal share. |
| [ACOS](../Math%20%26%20Trig/ACOS.md) | Recovers an angle in radians from a cosine value. |
| [COSH](../Math%20%26%20Trig/COSH.md) | Returns the hyperbolic cosine, which uses a different curve. |
| [RADIANS](../Math%20%26%20Trig/RADIANS.md) | Converts degrees into radians before the cosine is taken. |

## Official Documentation

- [Microsoft Support: COS function](https://support.microsoft.com/en-us/excel/functions/cos-function)
- [Google Docs Editors Help: COS](https://support.google.com/docs/answer/3093476)
