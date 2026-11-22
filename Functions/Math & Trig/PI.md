---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Trigonometry
purpose:
  - Trigonometry
use-case:
  - Circle Area Estimates
  - Circumference Calculations
  - Round Tank Volumes
related:
  - COS
  - DEGREES
  - RADIANS
  - SIN
  - SQRTPI
  - TAN
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/pi-function
  - https://support.google.com/docs/answer/3093432
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Circle Constant
  - Pi Constant
tags:
  - constants
  - excel
  - sheets
  - trigonometry
---

# PI

## Description

**PI** returns the mathematical constant pi, the ratio of a circle's circumference to its diameter. The value is approximately 3.14159. The function takes no arguments, so you type `=PI()` with empty parentheses. Excel documents the returned value as accurate to 15 digits, which is more precise than any decimal you would type by hand.

Use PI in any formula that works with circles: area, circumference, arc length, and the volume of cylinders. Because the formula calls the constant instead of a typed approximation, the results stay accurate when the radius or diameter in a cell changes.

PI also supports the trigonometric functions. SIN, COS and TAN expect angles in radians, and a half turn is `PI()` radians. PI does not calculate anything on its own. Its value appears only when you multiply, divide or pass it to another function. Formatting a cell to show fewer decimals changes only the display; the stored value keeps full precision.

## Syntax

```excel
=PI()
```

<!-- Image 1: Pi Constant in a Formula. See Images/Math & Trig/PI.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| None | Not applicable | PI takes no arguments. The empty parentheses are still required. |

### Return Value

A number: the value of pi, 3.14159265358979 at full precision. PI itself does not return an error. Any error comes from the formula that uses the result, such as a text value multiplied by PI.

## Examples

### Example 1: Return the Value of Pi

```excel
=PI()
```

**Result:** `3.14159265358979`

The function returns the constant with no input. The stored value keeps full precision even when the cell displays fewer decimals.

### Example 2: Area of a Circle

The radius is in cell `A2`, which holds `3`.

```excel
=ROUND(PI()*A2^2, 2)
```

**Result:** `28.27`

The formula squares the radius, multiplies by pi, and rounds to two decimal places. The exact area is 28.274333882308138.

<!-- Image 2: Circle Formula Layout. See Images/Math & Trig/PI.md -->

### Example 3: Circumference From a Diameter

The diameter is in cell `B2`, which holds `10`.

```excel
=ROUND(PI()*B2, 2)
```

**Result:** `31.42`

The circumference equals pi multiplied by the diameter. Rounding to two decimals gives a value suitable for a report.

### Example 4: Sine of a Quarter Turn

```excel
=SIN(PI()/2)
```

**Result:** `1`

A quarter turn is a quarter of 2 times pi, which is pi divided by 2 radians. The sine of that angle is 1, so the formula returns the maximum value of the sine function.

### Example 5: Arc Length for a Quarter Circle

The radius is in cell `A2`, which holds `3`, and the arc spans a quarter circle.

```excel
=ROUND(A2*PI()/2, 2)
```

**Result:** `4.71`

Arc length equals the radius multiplied by the angle in radians. A quarter circle spans pi divided by 2 radians, so the arc is 3 times pi divided by 2, or 4.712 before rounding.

## Story Problems

### Problem 1: Circular Garden Bed Edging

A landscaper builds round garden beds and sells edging by the foot. The diameters are listed in a sheet.

| Bed | Diameter (feet) |
| --- | --- |
| Herb Bed | 12 |
| Rose Bed | 8 |

**Task:** Calculate the edging length for the Herb Bed, rounded to two decimal places.

**Solution:**

```excel
=ROUND(PI()*B2, 2)
```

**Answer:** `37.70` feet. The circumference is pi times 12, which is 37.699, and it rounds to 37.70.

### Problem 2: Floor Area of a Round Table

A conference room includes a round table with a radius of 1.5 meters. The table surface area is needed for a flooring estimate.

| Item | Radius (meters) |
| --- | --- |
| Round Table | 1.5 |

**Task:** Calculate the area of the tabletop in square meters, rounded to two decimal places.

**Solution:**

```excel
=ROUND(PI()*B2^2, 2)
```

**Answer:** `7.07` square meters. The area is pi times 1.5 squared, which is 7.0686, and it rounds to 7.07.

## Use Cases

### Circle Area Estimates

**Scenario:** A sales team sizes round promotional displays by area so that each vendor quote uses the same measurements.

```excel
=ROUND(PI()*(B2/2)^2, 2)
```

**Why It Works:** The diameter in `B2` is halved to get the radius, because the area formula needs the radius. Keep the diameter in its own labeled column so that quotes update when a size changes.

### Circumference Calculations

**Scenario:** A fabricator orders steel band for pipe rings in several diameters.

```excel
=ROUND(PI()*C2, 1)
```

**Why It Works:** The formula multiplies the diameter in `C2` by pi and rounds to one decimal place. Order quantities are often in whole units, so wrap the result with ROUNDUP when the supplier only sells whole feet.

### Round Tank Volumes

**Scenario:** A facility manager estimates how much liquid a cylindrical tank holds.

```excel
=PI()*(D2/2)^2*E2
```

**Why It Works:** The base area is pi times the radius squared, and multiplying by the height in `E2` returns the volume in cubic units. Keep the units consistent across the diameter and height inputs.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | The function name is misspelled. | Type `PI`, check the spelling, and keep the empty parentheses. |
| `#VALUE!` | A number stored as text is multiplied by PI. | Convert the input to a number, or re-enter it in a cell formatted as a number. |
| Unexpected area | The diameter was used where the formula needs the radius. | Divide the diameter by 2 before squaring it. |
| Rounded total differs | The display was formatted to fewer decimals, but later steps used the full value. | Use ROUND in the formula when the rounded value must feed other calculations. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Microsoft 365, Excel 2021, Excel 2024 and Excel for the web | Returns pi accurate to 15 digits. |
| Google Sheets | Available | Same syntax with no arguments. Use ROUND or a number format when you need a fixed number of digits. |

## Tips and Best Practices

- Use `PI()` instead of typing 3.14, which loses precision in long formulas.
- Trigonometric functions expect radians, so convert degrees with RADIANS or multiply by `PI()/180`.
- Keep the radius or diameter in its own labeled cell so that every formula updates when the size changes.
- Round only the final result, not each step, to avoid cumulative rounding error.
- Check the units of the inputs, because a diameter used as a radius doubles the circumference and quadruples the area.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COS](COS.md) | Cosine of an angle in radians, often combined with PI. |
| [DEGREES](DEGREES.md) | Converts radians back to degrees. |
| [RADIANS](RADIANS.md) | Converts degrees to radians, the unit trigonometric functions expect. |
| [SIN](SIN.md) | Sine of an angle in radians. |
| [SQRTPI](SQRTPI.md) | Square root of a number multiplied by pi. |
| [TAN](TAN.md) | Tangent of an angle in radians. |

## Official Documentation

- [Microsoft Support: PI function](https://support.microsoft.com/en-us/excel/functions/pi-function)
- [Google Docs Editors Help: PI](https://support.google.com/docs/answer/3093432)
