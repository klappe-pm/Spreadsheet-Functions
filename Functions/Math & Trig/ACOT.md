---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Trigonometry
purpose:
  - Trigonometry
use-case:
  - Ramp Grade Reports
  - Roof Pitch Estimates
  - Sight Line Checks
related:
  - ACOTH
  - ATAN
  - COT
  - DEGREES
  - PI
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/acot-function
  - https://support.google.com/docs/answer/9084227
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Arccotangent
  - Inverse Cotangent
tags:
  - excel
  - inverse-trig
  - sheets
  - trigonometry
---

# ACOT

## Description

**ACOT** returns the inverse cotangent (arccotangent) of a number. It answers the question "which angle has this cotangent?" The cotangent is the reciprocal of the tangent, so for positive inputs `ACOT(x)` equals `ATAN(1/x)`. For negative inputs the two functions differ, because ACOT returns angles in the second half of its range.

Use ACOT when your ratio is adjacent over opposite, such as run over rise for a slope. Using ACOT avoids an extra division and keeps the formula readable. Any real number is a valid input, including zero and negative values.

ACOT returns radians in the range 0 to pi (about 3.14159). Negative inputs return angles in the second half of that range, and an input of 0 returns pi divided by 2. Wrap the result in `DEGREES` to read the angle in degrees. Use `ATAN` when you prefer the usual rise over run ratio.

## Syntax

```excel
=ACOT(number)
```

<!-- Image 1: Cotangent as Run Over Rise. See Images/Math & Trig/ACOT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The cotangent of the angle you want. It must be a real number. A cell reference or a formula result is allowed. |

### Return Value

The principal arccotangent in radians, between 0 and pi. Non-numeric input returns `#VALUE!`.

## Examples

### Example 1: Basic Angle

```excel
=ACOT(2)
```

**Result:** `0.463648`

The cotangent of about 0.4636 radians is 2.

### Example 2: Angle in Degrees

```excel
=DEGREES(ACOT(2))
```

**Result:** `26.56505`

`DEGREES` converts the radian result to degrees.

### Example 3: Zero Input

```excel
=ACOT(0)
```

**Result:** `1.570796`

A cotangent of 0 occurs at pi divided by 2, which is 90 degrees.

### Example 4: Negative Input

```excel
=ACOT(-1)
```

**Result:** `2.356194`

The result is 3 pi divided by 4, in the second half of the range. ACOT always returns a value between 0 and pi.

### Example 5: Ratio From a Cell

Run-to-rise ratio in `A2` is 4.8.

```excel
=DEGREES(ACOT(A2))
```

**Result:** `11.76829`

The angle from the horizontal is about 11.77 degrees.

## Story Problems

### Problem 1: Ramp Grades

Two ramps are built to the run and rise shown below, in feet.

| Ramp | Run (ft) | Rise (ft) |
| --- | --- | --- |
| R-1 | 12 | 2.5 |
| R-2 | 20 | 4 |

**Task:** Find the angle of each ramp from the horizontal, in degrees.

**Solution:**

```excel
=DEGREES(ACOT(B2/C2))
```

Fill the formula down from `D2`.

**Answer:** R-1 is `11.77` degrees and R-2 is `11.31` degrees. Dividing run by rise gives the cotangent, and ACOT turns that ratio into the angle.

<!-- Image 2: Ramp Run and Rise Triangle. See Images/Math & Trig/ACOT.md -->

### Problem 2: Vertical Surface Check

A surface sensor reports a run-to-rise ratio of 0 when the surface stands perfectly upright.

**Task:** Convert the sensor's ratio to degrees.

**Solution:**

```excel
=DEGREES(ACOT(0))
```

**Answer:** `90` degrees. A ratio of 0 means the surface is vertical, which is a right angle to the horizontal.

## Use Cases

### Ramp Grade Reports

**Scenario:** A facilities team compares ramp grades across a campus, and each design lists run and rise in separate columns.

```excel
=DEGREES(ACOT(Run/Rise))
```

**Why It Works:** The run and rise come straight from the drawing, so the formula does not need a separate division step.

### Roof Pitch Estimates

**Scenario:** An estimator records the horizontal run and vertical rise of each roof section and needs the pitch angle for material orders.

```excel
=ROUND(DEGREES(ACOT(Run/Rise)),1)
```

**Why It Works:** `ROUND` limits the angle to one decimal place for the order sheet.

### Sight Line Checks

**Scenario:** A safety team checks whether a sign remains visible from a given angle, using the horizontal offset and the height above the eye line.

```excel
=IF(DEGREES(ACOT(Offset/Height))>=MinimumAngle,"Visible","Obstructed")
```

**Why It Works:** The angle is compared with the minimum required angle, so the decision updates when the offset changes.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The input is text that cannot be read as a number. | Convert the cell to a number. |
| Angle looks like a radian value | The result is in radians, not degrees. | Wrap the call in `DEGREES`. |
| Angle is the complement of the expected value | The ratio was entered as rise over run instead of run over rise. | Divide run by rise, or use `ATAN` with rise over run. |
| `#NAME?` | The function name is misspelled. | Type `ACOT`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Returns radians between 0 and pi. Use `DEGREES` for degrees. |
| Google Sheets | Available | Same argument and radian result. The page describes the same 0 to pi range. |

## Tips and Best Practices

- Use ACOT when the ratio is adjacent over opposite, and use ATAN when it is opposite over adjacent.
- Keep the run and rise in labeled columns so anyone can check which value is the numerator.
- Use `DEGREES` in the same formula so the output unit is obvious to readers.
- Remember that inputs of 0 return pi divided by 2, which is a right angle, not an error.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ATAN](ATAN.md) | Inverse tangent. Use it when the ratio is rise over run. |
| [COT](COT.md) | Cotangent. The forward function that ACOT inverts. |
| [ACOTH](ACOTH.md) | Hyperbolic inverse cotangent. Use it for hyperbolic models. |
| [DEGREES](DEGREES.md) | Converts the radian result of ACOT to degrees. |
| [PI](PI.md) | Returns pi, useful when converting results by hand with `180/PI()`. |

## Official Documentation

- [Microsoft Support: ACOT function](https://support.microsoft.com/en-us/excel/functions/acot-function)
- [Google Docs Editors Help: ACOT](https://support.google.com/docs/answer/9084227)
