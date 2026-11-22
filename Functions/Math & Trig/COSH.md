---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Hyperbolic
purpose:
  - Trigonometry
use-case:
  - Catenary Cable Heights
  - Hanging Line Sag
related:
  - ACOSH
  - COS
  - SINH
  - TANH
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/cosh-function
  - https://support.google.com/docs/answer/3093477
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Hyperbolic Cosine
tags:
  - catenary
  - excel
  - hyperbolic
  - sheets
  - trigonometry
---

# COSH

## Description

**COSH** returns the hyperbolic cosine of a real number. Unlike the circular cosine in `COS`, it takes any real number as input, not an angle, and its value is always 1 or more. The curve it draws is smooth and U-shaped, which is why it describes a hanging cable or chain.

The most common business use is the catenary, the curve a cable or wire takes under its own weight. The height of a catenary at position x is a times COSH(x / a), where a sets how tight the cable is. Engineers and surveyors use this shape to estimate sag and clearance.

COSH is an even function: COSH(-x) equals COSH(x). For large inputs the result grows quickly, so check the size of the input before you apply it to a long column. Microsoft Excel and Google Sheets both accept one argument with the same meaning.

## Syntax

```excel
=COSH(number)
```

<!-- Image 1: Catenary Curve Shape. See Images/Math & Trig/COSH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | Any real number. Google Sheets calls this argument `value`. The argument is not an angle, so no conversion is needed. |

### Return Value

A number that is 1 or more. `COSH(0)` returns 1, and the result increases as the absolute value of the input grows. Neither official page documents overflow behavior or error values for very large inputs, so check the output of extreme values before relying on it.

## Examples

### Example 1: Basic Usage

```excel
=COSH(4)
```

**Result:** `27.308233`

The hyperbolic cosine of 4 is about 27.31.

### Example 2: The Base of the Natural Logarithm

```excel
=COSH(EXP(1))
```

**Result:** `7.610125`

`EXP(1)` returns the constant e, about 2.718. The function then returns the hyperbolic cosine of that value.

### Example 3: Zero Returns One

```excel
=COSH(0)
```

**Result:** `1`

The hyperbolic cosine has its minimum value of 1 at zero. This makes it useful as a baseline in a catenary formula.

### Example 4: A Small Positive Value

```excel
=COSH(1)
```

**Result:** `1.543081`

The result is a little above 1, showing how slowly the curve rises near zero.

### Example 5: Negative Input

```excel
=COSH(-2)
```

**Result:** `3.762196`

The result equals COSH(2), because the function is symmetric around zero.

## Story Problems

### Problem 1: Height of a Power Line

A utility company hangs a cable between two poles. The cable follows a catenary with a = 10 meters. Heights are measured from the lowest point of the cable at x = 0.

| Position x (m) | Height (m) |
| --- | --- |
| 0 | |
| 5 | |
| 10 | |
| 20 | |

**Task:** Compute the height of the cable at each position using height = a times COSH(x / a).

**Solution:**

```excel
=10 * COSH(A2 / 10)
```

Copy the formula down to row 5.

**Answer:** The heights are 10.00, 11.28, 15.43, and 37.62 meters. The lowest point is 10 meters, the height at x = 0.

<!-- Image 2: Catenary Heights Table. See Images/Math & Trig/COSH.md -->

### Problem 2: Sag of a Hanging Line

A rope bridge uses a catenary with a = 25 meters. The sag is measured between the lowest point at x = 0 and the attachment point at x = 25.

| Point | Position x (m) | Height (m) |
| --- | --- | --- |
| Lowest point | 0 | |
| Attachment | 25 | |

**Task:** Find the height difference between the two points.

**Solution:**

```excel
=25 * COSH(B3 / 25) - 25 * COSH(B2 / 25)
```

**Answer:** The attachment point is `13.58` meters higher than the lowest point. The attachment height is 38.58 meters and the lowest point is 25 meters.

<!-- Image 3: Sag Calculation Diagram. See Images/Math & Trig/COSH.md -->

## Use Cases

### Catenary Cable Heights

**Scenario:** A utility planner needs the height of a cable at several points along a span to check ground clearance.

```excel
=CableA * COSH(Spans[Position] / CableA)
```

**Why It Works:** The formula follows the standard catenary equation. Setting the parameter `CableA` to the value that matches the tension in the cable makes the curve fit the real installation.

### Hanging Line Sag

**Scenario:** A rigger compares the sag of two lines with different tension settings.

```excel
=TensionA * COSH(Positions / TensionA) - TensionA
```

**Why It Works:** Subtracting the lowest point gives the sag relative to the bottom of the curve. The result is always zero or greater, which makes the comparison easy to read.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Very large result | The input is large, and the hyperbolic cosine grows quickly. | Check the scale of the input and the parameter `a`. |
| Unexpected height | The parameter `a` was not divided into the position. | Use `COSH(x / a)` and multiply by `a`. |
| `#VALUE!` | The argument is text or a blank cell. | Convert the value to a number before calling the function. |
| Confusion with cosine | `COS` was used on a length instead of an angle. | Use `COSH` for hyperbolic curves and `COS` for angles in radians. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions and Excel for the web | Argument is named `number`. Accepts any real number. |
| Google Sheets | Available | Argument is named `value`. Accepts any real number, and the page notes that complex results are not supported. |

## Tips and Best Practices

- Keep the parameter `a` in its own cell so the curve can be adjusted without editing formulas.
- Use the difference between two heights to measure sag, not a single height.
- Check one value by hand with a calculator before filling a column.
- Use `ACOSH` to recover the position on a catenary from a height ratio.
- Remember that COSH is not an angle function, so do not convert its input with `RADIANS`.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COS](../Math%20%26%20Trig/COS.md) | Circular cosine of an angle in radians. |
| [SINH](../Math%20%26%20Trig/SINH.md) | Hyperbolic sine, the companion function for hyperbolic curves. |
| [TANH](../Math%20%26%20Trig/TANH.md) | Hyperbolic tangent, the ratio of SINH to COSH. |
| [ACOSH](../Math%20%26%20Trig/ACOSH.md) | Inverse hyperbolic cosine, which recovers the input from a result of 1 or more. |

## Official Documentation

- [Microsoft Support: COSH function](https://support.microsoft.com/en-us/excel/functions/cosh-function)
- [Google Docs Editors Help: COSH](https://support.google.com/docs/answer/3093477)
