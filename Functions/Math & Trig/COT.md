---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Trigonometry
purpose:
  - Trigonometry
use-case:
  - Engineering Trig Checks
  - Slope Ratio Analysis
  - Surveying Angle Ratios
related:
  - ATAN
  - COTH
  - CSC
  - DEGREES
  - RADIANS
  - SEC
  - TAN
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/cot-function
  - https://support.google.com/docs/answer/9084169
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Cotangent
tags:
  - excel
  - reciprocal-trig
  - sheets
  - trigonometry
---

# COT

## Description

**COT** returns the cotangent of an angle that you supply in radians. The cotangent is the reciprocal of the tangent, so `COT(angle)` gives the same result as `1/TAN(angle)`. Use COT when a calculation is written in cotangent terms, such as a slope ratio where the adjacent side divided by the opposite side is the figure you need.

COT expects radians, not degrees. If your angles are stored in degrees, wrap them in RADIANS first, as shown in Example 3. An input of 0 returns `#DIV/0!`, and an input whose absolute value is 2^27 or greater returns `#NUM!`.

## Syntax

```excel
=COT(number)
```

<!-- Image 1: Syntax Anatomy. See Images/Math & Trig/COT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The angle in radians. A number that is not numeric returns `#VALUE!`. Convert degrees with RADIANS before using COT. |

### Return Value

A number: the cotangent of the angle. The function returns `#DIV/0!` when the input is 0, `#NUM!` when the absolute value of the input is 2^27 or greater, and `#VALUE!` when the input is not numeric.

## Examples

### Example 1: Cotangent of One Radian

```excel
=COT(1)
```

**Result:** `0.642093`

The angle is read as 1 radian, which gives 1 divided by tan(1).

### Example 2: Angle From a Cell

Cell A2 holds `45`, read as 45 radians.

```excel
=COT(A2)
```

**Result:** `0.61737`

The formula reads the value as radians, not degrees, so the result is the cotangent of 45 radians.

### Example 3: Radians Versus Degrees

Cell A3 holds `30`, an angle in degrees.

```excel
=COT(RADIANS(A3))
```

**Result:** `1.73205`

RADIANS converts 30 degrees to 0.5236 radians first. The cotangent of 30 degrees is the square root of 3.

<!-- Image 2: Radians Versus Degrees Input. See Images/Math & Trig/COT.md -->

### Example 4: Reciprocal of the Tangent

```excel
=1/TAN(1)
```

**Result:** `0.642093`

This matches Example 1. COT is a shorter way to write the same reciprocal relationship.

### Example 5: Zero Input

```excel
=COT(0)
```

**Result:** `#DIV/0!`

The cotangent of 0 is undefined. Guard against this case when a zero angle can appear in your data.

## Story Problems

### Problem 1: Slope Angle Readings

A civil crew logs four slope angles in radians, one per reading, in column B. The design team wants the total of their cotangents as a combined gradient index.

| Reading | Angle (radians) |
| --- | --- |
| R1 | 1 |
| R2 | 4 |
| R3 | 0.5 |
| R4 | 2 |

**Task:** Add the cotangents of the four angles in one formula.

**Solution:**

```excel
=SUMPRODUCT(COT(B2:B5))
```

**Answer:** `2.87861`. The four cotangents are 0.64209, 0.86369, 1.83049 and -0.45766. SUMPRODUCT is used because it evaluates the array of cotangents without needing array entry.

### Problem 2: Checking a Right Angle

A lab sheet checks whether the cotangent of a 45 degree angle is exactly 1. Because the angle is pi divided by four radians, the check uses PI.

| Check | Angle (radians) |
| --- | --- |
| Diagonal check | 0.785398 |

**Task:** Compute the cotangent of pi divided by four and confirm that the result is 1.

**Solution:**

```excel
=COT(PI()/4)
```

**Answer:** `1`. The cotangent of pi divided by four is exactly 1, which confirms that a 45 degree slope has equal rise and run.

## Use Cases

### Surveying Slope Ratios

**Scenario:** A survey team stores one slope angle per station in radians in a table named Survey. The report needs the total of the cotangents across all stations.

```excel
=SUMPRODUCT(COT(Survey[Angle]))
```

**Why It Works:** COT accepts a range inside SUMPRODUCT, so one formula totals every station. Keep the angles in radians, because a degree value will give a result that looks plausible but is wrong.

### Engineering Trig Checks

**Scenario:** An engineer reviews a worksheet that uses 1/TAN in some rows and COT in others, and needs proof that the two methods agree.

```excel
=ABS(COT(B2)-1/TAN(B2))
```

**Why It Works:** The difference should be zero or very close to zero. A value that is not near zero points to an input in degrees or a row that uses a different angle.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | The input is 0. | Use `=IF(A2=0,"",COT(A2))` to skip zero inputs. |
| `#NUM!` | The absolute value of the input is 2^27 or greater. | Check the source value for a unit or data entry mistake. |
| `#VALUE!` | The input is text or another non-numeric value. | Check the source cell, or convert the text to a number. |
| Unexpected result | The angle is in degrees, not radians. | Wrap the input in RADIANS, as in Example 3. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in the Math and trigonometry group. | The argument is named `number` and is read in radians. |
| Google Sheets | Available | The argument is named `angle` and is read in radians. Results match Excel for the same input. |

## Tips and Best Practices

- Convert degree values with RADIANS before calling COT, because COT never reads degrees.
- Guard against a zero input with IF when zero can appear in the data.
- Use COT only when the formula reads more clearly in cotangent terms. 1/TAN gives the same answer for any input where the tangent is not zero.
- Add a check column with `1/TAN` when a workbook must prove that two methods agree.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ATAN](ATAN.md) | Returns the angle for a tangent value, the inverse direction of this calculation. |
| [COTH](COTH.md) | The hyperbolic cotangent, for hyperbolic rather than circular angles. |
| [CSC](CSC.md) | The cosecant, the reciprocal of SIN, built the same way from a different ratio. |
| [DEGREES](DEGREES.md) | Converts a radian result to degrees for reporting. |
| [RADIANS](RADIANS.md) | Converts degrees to radians before COT is applied. |
| [SEC](SEC.md) | The secant, the reciprocal of COS. |
| [TAN](TAN.md) | The tangent, whose reciprocal COT returns. |

## Official Documentation

- [Microsoft Support: COT function](https://support.microsoft.com/en-us/excel/functions/cot-function)
- [Google Docs Editors Help: COT](https://support.google.com/docs/answer/9084169)
