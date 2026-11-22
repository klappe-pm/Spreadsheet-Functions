---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Trigonometry
purpose:
  - Trigonometry
use-case:
  - Heading Calculations
  - Map Bearing Conversion
  - Vector Direction Analysis
related:
  - ATAN
  - COS
  - DEGREES
  - RADIANS
  - SIN
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/atan2-function
  - https://support.google.com/docs/answer/3093468
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Two Argument Arctangent
  - Quadrant Aware Arctangent
tags:
  - angle
  - coordinates
  - excel
  - sheets
  - trigonometry
---

# ATAN2

## Description

**ATAN2** returns the angle between the positive x-axis and a line drawn from the origin (0, 0) to a point with coordinates (x, y). The result is in radians, not degrees, and it falls between -pi and pi (the value -pi itself is never returned).

Use ATAN2 whenever you need a direction from coordinates, such as a heading from a GPS track, the slope of a vector, or the angle of a point on a chart. A positive result is a counterclockwise angle from the x-axis, and a negative result is clockwise.

ATAN2 is safer than the simpler ATAN(y/x) for two reasons. It accepts an x-coordinate of 0 without an error, and it tells apart points that share the same ratio but sit in opposite quadrants. For example, the point (3, 4) and the point (-3, -4) give ratios of 4/3 and 4/3 respectively, but their angles differ by pi.

Microsoft Excel and Google Sheets both take the x-coordinate first, then the y-coordinate. Both return the same radian value for the same point.

## Syntax

```excel
=ATAN2(x_num, y_num)
```

<!-- Image 1: ATAN2 Argument Order. See Images/Math & Trig/ATAN2.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x_num` | Yes | The x-coordinate of the point. Google Sheets calls this argument `x`. It can be 0 or negative. |
| `y_num` | Yes | The y-coordinate of the point. Google Sheets calls this argument `y`. It can be 0 or negative. |

### Return Value

A number of radians from -pi to pi, excluding -pi. Multiply by 180 and divide by `PI()`, or wrap the result in `DEGREES`, to get degrees. The function returns `#DIV/0!` when both `x_num` and `y_num` are 0, because the origin has no direction.

## Examples

### Example 1: Angle of a Point in the First Quadrant

```excel
=ATAN2(1, 1)
```

**Result:** `0.785398163`

The point (1, 1) sits on the diagonal, so the angle is pi/4 radians, which is 45 degrees.

### Example 2: Converting the Result to Degrees

```excel
=DEGREES(ATAN2(3, 4))
```

**Result:** `53.13010235`

The point (3, 4) is 53.13 degrees counterclockwise from the x-axis. `DEGREES` converts the radian result, so you do not need to multiply by 180/PI() yourself.

### Example 3: Comparing ATAN2 With ATAN

```excel
=ATAN2(-3, -4)
```

**Result:** `-2.214297436`

```excel
=ATAN(-4/-3)
```

**Result:** `0.927295218`

ATAN2 places the point (-3, -4) in the third quadrant and returns a negative angle. ATAN sees only the ratio 4/3 and returns the angle of the point (3, 4) instead. This is why ATAN2 is the right choice for headings and vectors.

<!-- Image 2: Quadrant Comparison of ATAN2 and ATAN. See Images/Math & Trig/ATAN2.md -->

### Example 4: A Point Directly Above the Origin

```excel
=ATAN2(0, 5)
```

**Result:** `1.570796327`

The point (0, 5) lies on the y-axis, so the angle is pi/2 radians. `ATAN(5/0)` would fail with `#DIV/0!` because it divides by zero, but ATAN2 handles an x-coordinate of 0 without a problem.

### Example 5: Combined With Other Functions

```excel
=IFERROR(DEGREES(ATAN2(B2, C2)), "At origin")
```

**Result:** `At origin` when B2 and C2 are both 0; otherwise the angle in degrees

The `IFERROR` wrapper turns the origin case into a readable label instead of an error code. Use the same pattern in any column that may contain points at the origin.

## Story Problems

### Problem 1: Delivery Robot Headings

A warehouse robot starts at the depot and drives three legs. Each row gives the distance east (x) and north (y) of the leg's end point, in meters.

| Leg | East (m) | North (m) | Heading (degrees) |
| --- | --- | --- | --- |
| A | 3 | 4 | |
| B | -2 | 5 | |
| C | -4 | -3 | |

**Task:** Fill column D with each leg's heading in degrees, measured counterclockwise from east.

**Solution:**

```excel
=DEGREES(ATAN2(B2, C2))
```

Copy the formula down to row 4.

**Answer:** Leg A is `53.13`, leg B is `111.80`, and leg C is `-143.13` degrees. Leg C points southwest, so its angle is negative.

<!-- Image 3: Robot Heading Results. See Images/Math & Trig/ATAN2.md -->

### Problem 2: Survey Benchmarks Around a Pier

A surveyor records two points relative to a benchmark, in meters. Each point needs its angle in radians for a drawing.

| Point | East (m) | North (m) | Angle (radians) |
| --- | --- | --- | --- |
| P1 | 0 | 9 | |
| P2 | 0 | -4 | |

**Task:** Find the angle in radians for each point. The x-coordinate is 0 for both points.

**Solution:**

```excel
=ATAN2(B2, C2)
```

Copy the formula down to row 3.

**Answer:** P1 is `1.570796327` radians (due north, 90 degrees) and P2 is `-1.570796327` radians (due south). `ATAN(C2/B2)` would fail for both points because the x-coordinate is 0.

## Use Cases

### Heading Calculations

**Scenario:** A logistics team logs GPS offsets from a depot as east and north distances and needs the heading of each leg in degrees.

```excel
=DEGREES(ATAN2(Track[East], Track[North]))
```

**Why It Works:** `ATAN2` takes the east distance as the x-coordinate and the north distance as the y-coordinate. `DEGREES` turns the radians into degrees that the team can compare to a compass chart. Check that the East column comes first, because swapping the two arguments rotates every heading by 90 degrees.

### Map Bearing Conversion

**Scenario:** A navigation sheet uses compass bearings, which start at north and run clockwise. Math angles start at east and run counterclockwise.

```excel
=MOD(90 - DEGREES(ATAN2(B2, C2)) + 360, 360)
```

**Why It Works:** Subtracting the math angle from 90 rotates the origin from east to north and reverses the direction. Adding 360 and taking `MOD` keeps the bearing between 0 and 359.99. For a point at east 3 and north 4, the bearing is 36.87 degrees.

### Vector Direction Analysis

**Scenario:** An engineer tracks a force vector given as horizontal and vertical components and needs its direction for a report.

```excel
=DEGREES(ATAN2(F2, E2))
```

**Why It Works:** The horizontal component is passed first because the x-coordinate comes first in the syntax. The sign of each component keeps the direction correct in every quadrant, which a plain ATAN(vertical/horizontal) would not do.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | Both `x_num` and `y_num` are 0. | Wrap the formula in `IFERROR` or `IF` to return a label for the origin. |
| Wrong quadrant | The formula uses ATAN(y/x) instead of ATAN2. | Replace the formula with ATAN2 and pass x first, then y. |
| Heading rotated 90 degrees | The x and y arguments are swapped. | Check that the east or x value is the first argument. |
| Unexpected small numbers | The result is in radians, not degrees. | Wrap the formula in `DEGREES`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions and Excel for the web | Arguments are named `x_num` and `y_num`. Returns `#DIV/0!` when both arguments are 0. |
| Google Sheets | Available | Arguments are named `x` and `y`. The argument order and radian output match Excel. |

## Tips and Best Practices

- Pass the x-coordinate first; swapping the arguments silently rotates every result.
- Use `DEGREES` for display and keep the raw radian value for further trigonometry.
- Use ATAN2 instead of ATAN(y/x) whenever the sign of either coordinate matters.
- Guard the origin case with `IFERROR` when the input table can contain (0, 0).
- Format the result as a number with the decimals you need; the function does not round.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ATAN](../Math%20%26%20Trig/ATAN.md) | Returns one angle from a single ratio; cannot tell opposite quadrants apart. |
| [COS](../Math%20%26%20Trig/COS.md) | Returns the horizontal component of a unit vector at a given angle. |
| [DEGREES](../Math%20%26%20Trig/DEGREES.md) | Converts the radian result of ATAN2 into degrees. |
| [RADIANS](../Math%20%26%20Trig/RADIANS.md) | Converts degrees into radians before passing an angle to trigonometric functions. |
| [SIN](../Math%20%26%20Trig/SIN.md) | Returns the vertical component of a unit vector at a given angle. |

## Official Documentation

- [Microsoft Support: ATAN2 function](https://support.microsoft.com/en-us/excel/functions/atan2-function)
- [Google Docs Editors Help: ATAN2](https://support.google.com/docs/answer/3093468)
