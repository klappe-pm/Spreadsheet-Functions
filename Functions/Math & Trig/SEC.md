---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Trigonometry
purpose:
  - Trigonometry
use-case:
  - Radian Angle Readings
  - Slope Length Estimates
related:
  - COS
  - COT
  - CSC
  - RADIANS
  - SECH
  - SIN
  - TAN
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/sec-function
  - https://support.google.com/docs/answer/9116395
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - excel
  - radians
  - secant
  - sheets
  - trigonometry
---

# SEC

## Description

**SEC** returns the secant of an angle. The secant is the reciprocal of the cosine, so SEC(x) equals 1 divided by COS(x). It is used in geometry and engineering where a slope length or a scale factor depends on the cosine of an angle.

The angle must be in radians, not degrees. Microsoft's example text describes angles in degrees, but the function treats the number as radians. To work with degrees, convert the value first with RADIANS, or multiply by PI()/180.

The secant is undefined where the cosine is zero, so SEC returns very large values near odd multiples of PI()/2. The Excel documentation says the absolute value of the angle must be less than 2^27, or the function returns #NUM!.

Use SEC when a formula already uses a secant, or when you want a single function call instead of 1/COS(x). For the hyperbolic version, use SECH.

## Syntax

```excel
=SEC(number)
```

<!-- Image 1: Secant Argument Anatomy. See Images/Math & Trig/SEC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The angle in radians for which you want the secant. Convert degrees with RADIANS first. The absolute value must be less than 2^27. |

### Return Value

Returns the secant of the angle as a number. The result is at least 1 in absolute value, because the cosine never exceeds 1. The function returns #NUM! when the angle is too large, and #VALUE! when the argument is text that cannot be read as a number.

## Examples

### Example 1: Secant of One Radian

```excel
=SEC(1)
```

**Result:** 1.8508

The cosine of 1 radian is about 0.5403. Dividing 1 by 0.5403 gives the secant, about 1.8508.

### Example 2: Secant of Zero

```excel
=SEC(0)
```

**Result:** 1

The cosine of 0 is 1, so the secant is also 1. This is the smallest value SEC can return.

<!-- Image 2: Degrees Converted to Radians. See Images/Math & Trig/SEC.md -->

### Example 3: Secant of a Negative Angle

```excel
=SEC(-1)
```

**Result:** 1.8508

The secant is an even function, so SEC(-1) equals SEC(1). The sign of the angle does not change the result.

### Example 4: Secant of a Degree Angle After Conversion

```excel
=SEC(RADIANS(60))
```

**Result:** 2

RADIANS converts 60 degrees to about 1.0472 radians. The cosine of 60 degrees is 0.5, so the secant is 2. Floating-point arithmetic can leave a tiny rounding difference, so wrap the result in ROUND when an exact display is needed.

### Example 5: Secant of a Larger Angle

```excel
=SEC(4)
```

**Result:** -1.5299

The angle 4 radians lies in the third quadrant, where the cosine is negative. The secant is therefore negative as well.

## Story Problems

### Problem 1: Slope Length From a Horizontal Run

A site engineer measures a horizontal run of 30 meters for a drainage ramp. The ramp angle is recorded in radians, and the slope length is the run multiplied by SEC of the angle.

| Reading | Angle (radians) |
| --- | --- |
| Gentle slope | 0.4 |
| Medium slope | 0.7 |
| Steep slope | 1.0 |

**Task:** Find the slope length of the steep ramp, in meters, to two decimal places.

**Solution:**

```excel
=ROUND(30 * SEC(1.0), 2)
```

**Answer:** `55.52` meters, because 30 divided by the cosine of 1.0 radian is about 55.52. The medium slope gives 39.22 meters and the gentle slope gives 32.57 meters.

### Problem 2: Converting a Degree Reading

A technician records the same ramp at 60 degrees. The technician must convert the reading to radians before using SEC, or the result will be wrong.

| Reading | Degrees | Radians |
| --- | --- | --- |
| Ramp check | 60 | 1.0472 |

**Task:** Find the secant of the ramp angle, and then the slope length for a 30 meter run.

**Solution:**

```excel
=ROUND(30 * SEC(RADIANS(60)), 2)
```

**Answer:** `60`, because SEC(RADIANS(60)) equals 2, and 30 multiplied by 2 is 60 meters.

## Use Cases

### Radian Angle Readings

**Scenario:** A sensor on a conveyor logs its tilt angle in radians, and the control system needs the secant to scale a measured distance.

```excel
=SEC(B2)
```

**Why It Works:** SEC reads the logged radian value directly. Keep the sensor in radians, because a degree reading in the same column will return a misleading secant.

### Slope Length Estimates

**Scenario:** A landscaping crew knows the horizontal run and the slope angle, and it needs the length of material to cut for each slope.

```excel
=B2 * SEC(B3)
```

**Why It Works:** The slope length is the horizontal run divided by the cosine of the angle, which is the same as multiplying by the secant. Round the result to the cutting precision the crew uses.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The absolute value of the angle is 2^27 or greater. | Reduce the angle to a smaller equivalent value within one full turn. |
| `#VALUE!` | The argument is text, not a number. | Convert the text with VALUE or correct the source cell. |
| Unexpectedly large result | The angle is close to an odd multiple of PI()/2. | Check the input angle, because the cosine is near zero there. |
| Wrong magnitude | A degree value was used without conversion. | Wrap the angle in RADIANS before calling SEC. |
| `#NAME?` | The function name is misspelled or unavailable in the version. | Check the spelling and the Excel version. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Excel for the web, Excel 2024, Excel 2021, Excel 2019, and Excel 2016 | Angle must be in radians. The absolute value must be less than 2^27. |
| Google Sheets | Available | Angle in radians, the same as Excel. Use RADIANS for degree values. |

## Tips and Best Practices

- Keep the input in radians, and label the column so the next reader knows the unit.
- Use RADIANS for degree values rather than a manual multiplication, which is easier to read in a formula.
- Use 1/COS(x) when the reader needs to see the cosine explicitly, because SEC is less familiar to most users.
- Check results near odd multiples of PI()/2, where the secant becomes very large.
- Round the displayed result, not the input, when a slope length must match a cutting tolerance.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COS](COS.md) | The reciprocal of SEC. SEC(x) equals 1 divided by COS(x). |
| [COT](COT.md) | The cotangent, the reciprocal of TAN. |
| [CSC](CSC.md) | The cosecant, the reciprocal of SIN. |
| [RADIANS](RADIANS.md) | Converts degrees to radians before SEC is used. |
| [SECH](SECH.md) | The hyperbolic secant, used for curves rather than circular angles. |
| [SIN](SIN.md) | Returns the sine, which is used with the other reciprocal functions. |
| [TAN](TAN.md) | Returns the tangent, the ratio of SIN to COS. |

## Official Documentation

- [Microsoft Support: SEC function](https://support.microsoft.com/en-us/excel/functions/sec-function)
- [Google Docs Editors Help: SEC](https://support.google.com/docs/answer/9116395)
