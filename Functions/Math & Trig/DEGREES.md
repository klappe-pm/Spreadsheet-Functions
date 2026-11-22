---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Trigonometry
purpose:
  - Unit Conversion
use-case:
  - Robotics Joint Reports
  - Sensor Angle Conversion
  - Turbine Blade Angles
related:
  - ATAN2
  - COS
  - PI
  - RADIANS
  - SIN
  - TAN
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/degrees-function
  - https://support.google.com/docs/answer/3093481
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Radians to Degrees
tags:
  - angles
  - excel
  - sheets
  - trigonometry
---

# DEGREES

## Description

**DEGREES** converts an angle measured in radians into degrees. Use it when a trig function such as ATAN or a formula that uses PI returns radians, and a report needs degrees. The result is a plain decimal number with no rounding applied.

DEGREES reads its input as radians. A value already in degrees is not converted again, so a number such as 90 entered by mistake is treated as 90 radians and returns about 5156.62. Check the source of every angle before converting it. The reverse conversion, from degrees to radians, uses RADIANS.

## Syntax

```excel
=DEGREES(angle)
```

<!-- Image 1: Syntax Anatomy. See Images/Math & Trig/DEGREES.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `angle` | Yes | The angle in radians to convert. PI() returns the value of pi, so `DEGREES(PI())` gives 180. |

### Return Value

A number: the angle expressed in degrees. A value that is not numeric returns `#VALUE!`.

## Examples

### Example 1: Half a Turn

```excel
=DEGREES(PI())
```

**Result:** `180`

Pi radians is half a full turn, which equals 180 degrees.

### Example 2: One Radian

```excel
=DEGREES(1)
```

**Result:** `57.29578`

One radian is about 57.3 degrees.

### Example 3: One Third of Pi

```excel
=DEGREES(PI()/3)
```

**Result:** `60`

Pi divided by three radians is a 60 degree angle.

### Example 4: Value From a Cell

Cell A2 holds `6`, an angle in radians.

```excel
=DEGREES(A2)
```

**Result:** `343.77468`

Six radians is just under one full turn, so the result is a little less than 360 degrees.

<!-- Image 2: Radians Converted to Degrees. See Images/Math & Trig/DEGREES.md -->

### Example 5: Negative Angle

```excel
=DEGREES(-PI()/4)
```

**Result:** `-45`

A negative angle converts to a negative number of degrees, which points the opposite way.

## Story Problems

### Problem 1: Turbine Blade Angles

A maintenance log records the pitch of three turbine blades in radians. The report needs the total pitch in degrees.

| Blade | Angle (radians) |
| --- | --- |
| Blade A | 0.5 |
| Blade B | 2 |
| Blade C | 3 |

**Task:** Convert all three blade angles to degrees and add them in one formula.

**Solution:**

```excel
=SUMPRODUCT(DEGREES(B2:B4))
```

**Answer:** `315.12679`. The three blades measure 28.64789, 114.59156 and 171.88734 degrees, which add to 315.12679.

### Problem 2: Sensor Joint Reading

A robot joint sensor reports 1.047198 radians. The controller needs the reading in whole degrees.

| Sensor | Angle (radians) |
| --- | --- |
| Joint sensor | 1.047198 |

**Task:** Convert the sensor reading to degrees and round the result to a whole number.

**Solution:**

```excel
=ROUND(DEGREES(B2),0)
```

**Answer:** `60`. The reading is one third of pi, which is 60 degrees.

## Use Cases

### Turbine Blade Angles

**Scenario:** A blade table stores pitch values in radians. A summary sheet needs the total pitch in degrees for each unit.

```excel
=SUMPRODUCT(DEGREES(Blades[Radians]))
```

**Why It Works:** SUMPRODUCT converts every blade angle and totals the results in one step. Keep the source values in radians so that the conversion is applied once.

### Sensor Angle Conversion

**Scenario:** A slope sensor reports the arctangent of a rise over a run as radians. A dashboard shows the slope in degrees.

```excel
=DEGREES(ATAN(B2))
```

**Why It Works:** ATAN returns radians, and DEGREES makes the result readable for people who think in degrees. Check that B2 holds the rise over run ratio, not a degree value.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unexpectedly large result | A value in degrees was passed to DEGREES. | Confirm that the input is in radians, or remove the conversion. |
| `#VALUE!` | The input is text or another non-numeric value. | Check the source cell, or convert the text to a number. |
| Wrong sign | The angle was entered with the wrong direction. | Check the sign of the source angle before converting. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in the Math and trigonometry group. | The argument is named `angle` and is read in radians. |
| Google Sheets | Available | The argument is named `angle` and is read in radians. Sample formulas match Excel. |

## Tips and Best Practices

- Keep angles in radians inside calculations, and convert to degrees only for the final report.
- Use PI() rather than typing 3.14159, so the conversion stays exact.
- Pair DEGREES with ATAN or ASIN when a formula returns radians that people want to read in degrees.
- Use RADIANS to reverse the conversion when a degree input is needed for a trig function.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ATAN2](ATAN2.md) | Returns an angle in radians that DEGREES can convert. |
| [COS](COS.md) | Takes an angle in radians, the input that DEGREES produces. |
| [PI](PI.md) | Supplies the value of pi used in common angle inputs. |
| [RADIANS](RADIANS.md) | The reverse conversion, from degrees to radians. |
| [SIN](SIN.md) | Takes an angle in radians, the input that DEGREES produces. |
| [TAN](TAN.md) | Takes an angle in radians, the input that DEGREES produces. |

## Official Documentation

- [Microsoft Support: DEGREES function](https://support.microsoft.com/en-us/excel/functions/degrees-function)
- [Google Docs Editors Help: DEGREES](https://support.google.com/docs/answer/3093481)
