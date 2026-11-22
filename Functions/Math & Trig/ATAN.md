---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Trigonometry
purpose:
  - Trigonometry
use-case:
  - Camera Tilt Angles
  - Road Grade Reports
  - Slope Comparisons
related:
  - ACOS
  - ASIN
  - ATAN2
  - DEGREES
  - RADIANS
  - TAN
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/atan-function
  - https://support.google.com/docs/answer/3093395
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Arctangent
  - Inverse Tangent
tags:
  - excel
  - inverse-trig
  - sheets
  - trigonometry
---

# ATAN

## Description

**ATAN** returns the inverse tangent (arctangent) of a number. It answers the question "which angle has this tangent?" The input can be any real number, and the result is an angle in radians between -pi/2 and pi/2 (about -1.5708 to 1.5708).

Use ATAN when you know the ratio of the opposite side to the adjacent side in a right triangle, such as rise over run for a road or a slope. The angle is `ATAN(opposite / adjacent)`. When you know the sine or cosine ratio instead, use `ASIN` or `ACOS`.

ATAN returns radians, so wrap the result in `DEGREES` for an angle in degrees. Because a tangent repeats its values, ATAN returns only the principal angle. When you have the two sides as separate values and need the angle in the correct quadrant, use `ATAN2` instead.

## Syntax

```excel
=ATAN(number)
```

<!-- Image 1: Right Triangle and the Tangent Ratio. See Images/Math & Trig/ATAN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The tangent of the angle you want. Any real number is allowed. A cell reference or a formula result is allowed. |

### Return Value

The angle, in radians, whose tangent equals `number`. The result is between -pi/2 and pi/2. Non-numeric input returns `#VALUE!`.

## Examples

### Example 1: Angle in Radians

```excel
=ATAN(1)
```

**Result:** `0.785398`

This is pi divided by 4, the angle whose tangent is 1.

### Example 2: Angle in Degrees

```excel
=DEGREES(ATAN(1))
```

**Result:** `45`

`DEGREES` converts the radian result to degrees.

### Example 3: Negative Input

```excel
=ATAN(-1)
```

**Result:** `-0.785398`

A negative tangent gives a negative angle with the same size.

### Example 4: Ratio From Two Cells

Rise is 6 in `A2` and run is 40 in `B2`.

```excel
=DEGREES(ATAN(A2/B2))
```

**Result:** `8.530766`

The angle is about 8.53 degrees.

### Example 5: Very Large Input

```excel
=ATAN(1000000)
```

**Result:** `1.570795`

As the input grows, the result approaches pi divided by 2 but never reaches it.

## Story Problems

### Problem 1: Road Grade Comparison

A county engineer records the rise and run of two road segments, in feet.

| Segment | Rise (ft) | Run (ft) |
| --- | --- | --- |
| S-1 | 6 | 40 |
| S-2 | 3 | 60 |

**Task:** Find the grade angle of each segment in degrees.

**Solution:**

```excel
=DEGREES(ATAN(B2/C2))
```

Fill the formula down from `D2` to `D3`.

**Answer:** S-1 is `8.53` degrees and S-2 is `2.86` degrees. The rise divided by the run gives the tangent of each grade.

<!-- Image 2: Two Road Segments Compared. See Images/Math & Trig/ATAN.md -->

### Problem 2: Finding the Steeper Segment

The engineer needs the name of the segment with the largest grade angle, using the results from Problem 1 in column `D`.

**Task:** Return the segment name with the largest angle.

**Solution:**

```excel
=INDEX(A2:A3,MATCH(MAX(D2:D3),D2:D3,0))
```

**Answer:** `S-1`, because 8.53 degrees is larger than 2.86 degrees.

## Use Cases

### Road Grade Reports

**Scenario:** A public works team lists each road segment's grade in degrees for a maintenance plan.

```excel
=ROUND(DEGREES(ATAN(Rise/Run)),2)
```

**Why It Works:** The grade is computed from the survey rise and run, and `ROUND` keeps the report to two decimal places.

### Camera Tilt Angles

**Scenario:** A security installer sets a camera tilt by measuring the height difference and the distance to the target.

```excel
=DEGREES(ATAN(HeightDifference/Distance))
```

**Why It Works:** The ratio of height to distance gives the tilt angle directly, so the installer can set it on the mount.

### Slope Comparisons

**Scenario:** A site planner compares several slopes and needs to know which one needs a retaining wall.

```excel
=IF(DEGREES(ATAN(Rise/Run))>MaximumAngle,"Retaining wall","Standard grading")
```

**Why It Works:** Each slope is converted to degrees and compared with the maximum allowed angle, so the decision is consistent across all rows.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | The run in the denominator is 0. | Check the run, or use `ATAN2` when one side can be zero. |
| `#VALUE!` | The input is text that cannot be read as a number. | Convert the cell to a number. |
| Angle looks like about 0.8 | The result is in radians, not degrees. | Wrap the call in `DEGREES`. |
| Wrong quadrant | The sides have opposite signs and ATAN returns only the principal angle. | Use `ATAN2` with the run and rise as separate arguments. |
| `#NAME?` | The function name is misspelled. | Type `ATAN`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Returns radians between -pi/2 and pi/2. Use `DEGREES` for degrees. |
| Google Sheets | Available | Same argument and radian result. The page gives the same principal range. |

## Tips and Best Practices

- Use ATAN when the ratio is opposite over adjacent. Use `ATAN2` when the direction of the angle matters across all four quadrants.
- Check that the denominator is not zero before dividing, or wrap the ratio in `IFERROR`.
- Convert to degrees in the same formula so the unit is clear to readers.
- Compare angles in the same unit. Mixing radian and degree values in one comparison is a common mistake.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ATAN2](ATAN2.md) | Returns the full-circle angle from separate x and y values. |
| [ASIN](ASIN.md) | Inverse sine. Use it when the opposite side and hypotenuse are known. |
| [ACOS](ACOS.md) | Inverse cosine. Use it when the adjacent side and hypotenuse are known. |
| [TAN](TAN.md) | Tangent. The forward function that ATAN inverts. |
| [DEGREES](DEGREES.md) | Converts the radian result of ATAN to degrees. |

## Official Documentation

- [Microsoft Support: ATAN function](https://support.microsoft.com/en-us/excel/functions/atan-function)
- [Google Docs Editors Help: ATAN](https://support.google.com/docs/answer/3093395)
