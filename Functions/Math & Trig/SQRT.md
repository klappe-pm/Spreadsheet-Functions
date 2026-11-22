---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Logarithms and Powers
purpose:
  - Arithmetic Operations
use-case:
  - Distance Between Points
  - Square Tile Dimensions
related:
  - ABS
  - LN
  - POWER
  - SQRTPI
  - SUMPRODUCT
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/sqrt-function
  - https://support.google.com/docs/answer/3093577
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Square Root
  - Radical
tags:
  - excel
  - geometry
  - radicals
  - sheets
  - square-root
---

# SQRT

## Description

**SQRT** returns the positive square root of a number. The square root of a value is the number that, multiplied by itself, gives the original value. For example, SQRT(25) returns 5, because 5 times 5 equals 25.

The input must be zero or positive. A negative input returns the #NUM! error, because a real number multiplied by itself is never negative. To find the square root of a negative number as a complex number, use IMSQRT. To find the magnitude of a value that might be negative, wrap the input in ABS, such as SQRT(ABS(A2)).

SQRT is used for distances, standard deviations, areas, and any formula that undoes a squared term. The square root of a sum of squares is the basis of the Pythagorean theorem, which gives the length of the hypotenuse of a right triangle.

SQRT is the same as raising a number to the power 0.5. The formulas SQRT(x), POWER(x, 0.5), and x^0.5 return the same result. For other roots, such as a cube root, use POWER with a fractional exponent.

## Syntax

```excel
=SQRT(number)
```

<!-- Image 1: Square Root Argument Anatomy. See Images/Math & Trig/SQRT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | A zero or positive number for which you want the square root. Negative inputs return #NUM!. |

### Return Value

Returns the positive square root of the number. The result is never negative. Returns 0 when the input is 0, and returns #NUM! when the input is negative. Returns #VALUE! when the argument is text that cannot be read as a number.

## Examples

### Example 1: Square Root of a Perfect Square

```excel
=SQRT(25)
```

**Result:** 5

Five multiplied by itself is 25, so the square root is 5 with no decimal remainder.

### Example 2: Square Root of a Non-Perfect Square

```excel
=SQRT(2)
```

**Result:** 1.4142

Two has no exact square root in decimal form. The function returns the closest value its precision allows, shown here to four decimals.

<!-- Image 2: Negative Input and the ABS Fix. See Images/Math & Trig/SQRT.md -->

### Example 3: Square Root of a Fraction

```excel
=SQRT(0.25)
```

**Result:** 0.5

Half multiplied by itself is 0.25, so the square root of 0.25 is 0.5.

### Example 4: Pythagorean Distance

```excel
=SQRT(3^2 + 4^2)
```

**Result:** 5

The two legs of a right triangle are 3 and 4. The square root of the sum of their squares is the length of the hypotenuse, which is 5.

### Example 5: Negative Input

```excel
=SQRT(-16)
```

**Result:** #NUM!

A negative number has no real square root. To return the magnitude instead, use SQRT(ABS(-16)), which returns 4.

## Story Problems

### Problem 1: Farthest Sensor From the Base

A field crew records the position of four sensors as horizontal and vertical offsets, in meters, from a base station at the origin. The distance from the base to each sensor is the square root of the sum of the squared offsets.

| Sensor | X Offset | Y Offset |
| --- | --- | --- |
| S1 | 3 | 4 |
| S2 | 5 | 12 |
| S3 | 8 | 15 |
| S4 | 2 | 2 |

**Task:** Find the distance from the base to the sensor that is farthest away.

**Solution:**

```excel
=MAX(SQRT(B2:B5^2 + C2:C5^2))
```

**Answer:** `17` meters, for sensor S3. The other distances are 5, 13, and about 2.83 meters. In Excel versions without dynamic arrays, enter this formula as an array formula.

### Problem 2: Side Length of a Square Tile

A landscaper knows the area of each square patio tile in square feet. The side length of a square tile is the square root of its area, and the landscaper needs the side length for a 50 square foot tile.

| Tile | Area (sq ft) |
| --- | --- |
| Large | 144 |
| Medium | 50 |
| Small | 98 |

**Task:** Find the side length of the medium tile, rounded to two decimal places.

**Solution:**

```excel
=ROUND(SQRT(B3), 2)
```

**Answer:** `7.07` feet. The large and small tiles have side lengths of 12 and about 9.90 feet.

## Use Cases

### Distance Between Points

**Scenario:** A logistics planner calculates the straight-line distance between two warehouse locations, using their grid coordinates.

```excel
=SQRT((C2 - B2)^2 + (E2 - D2)^2)
```

**Why It Works:** The horizontal and vertical differences are squared, added, and square-rooted. The result is the straight-line distance between the points, in the same units as the coordinates. For latitude and longitude, use a great-circle formula instead.

### Square Tile Dimensions

**Scenario:** A flooring estimator converts the area of a square room into its side length, so the installer can measure each wall.

```excel
=SQRT(B2)
```

**Why It Works:** For a square, the area is the side length multiplied by itself. SQRT reverses that operation and returns the side length in the original unit.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input is negative. | Use ABS for the magnitude, or check the data for a sign error. |
| `#VALUE!` | The argument is text, not a number. | Convert the text with VALUE or correct the source cell. |
| `#NAME?` | The function name is misspelled. | Check that the name is spelled SQRT. |
| Unexpected decimals | A perfect square displays as a decimal in a general format. | Apply a number format with no decimals, or use ROUND for a whole number. |
| Wrong root | A cube root or other root was needed. | Use POWER(x, 1/3) for a cube root, or POWER(x, 1/n) for the nth root. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac, and web), Excel 2024, Excel 2021, Excel 2019, Excel 2016, Microsoft Office, and My Office for iPhone | Negative inputs return #NUM!. Use IMSQRT for complex results. |
| Google Sheets | Available | Negative inputs return #NUM!. For the negative root, multiply the SQRT result by -1. |

## Tips and Best Practices

- Check for negative inputs before the square root, or wrap the input in ABS when the magnitude is the goal.
- Use SQRT for readability, and POWER for other roots.
- Use SUMPRODUCT or dynamic arrays when SQRT must work across a range of values.
- Apply ROUND only to the displayed or reported result, not to intermediate values.
- Remember that a standard deviation is the square root of the variance, so SQRT converts it back to the original units.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ABS](ABS.md) | Returns the magnitude of a number, so SQRT(ABS(x)) never returns #NUM!. |
| [LN](LN.md) | Returns the natural logarithm, the inverse of EXP, used in other root and growth formulas. |
| [POWER](POWER.md) | Raises a number to any power, including the 0.5 power that equals SQRT. |
| [SQRTPI](SQRTPI.md) | Returns the square root of a number multiplied by pi, used in circle and area formulas. |
| [SUMPRODUCT](SUMPRODUCT.md) | Adds products across arrays, often combined with SQRT for sums of squares. |

## Official Documentation

- [Microsoft Support: SQRT function](https://support.microsoft.com/en-us/excel/functions/sqrt-function)
- [Google Docs Editors Help: SQRT](https://support.google.com/docs/answer/3093577)
