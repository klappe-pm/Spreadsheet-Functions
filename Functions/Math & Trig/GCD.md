---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Number Theory
purpose:
  - Arithmetic Operations
use-case:
  - Cutting Material Lengths
  - Tile Layout Planning
related:
  - FACTDOUBLE
  - LCM
  - MOD
  - QUOTIENT
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/gcd-function
  - https://support.google.com/docs/answer/3093489
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Greatest Common Divisor
tags:
  - divisors
  - excel
  - number-theory
  - sheets
---

# GCD

## Description

**GCD** returns the greatest common divisor of one or more integers: the largest whole number that divides every value with no remainder. For example, GCD(96,60) returns 12, because 12 divides both 96 and 60 exactly. Use GCD when a quantity must be split into equal pieces with nothing left over, or when the largest square tile that fits a rectangle without cutting is needed.

In Excel, GCD accepts up to 255 values. Decimal parts are removed before the calculation, so 12.7 is treated as 12. Zero is allowed, so GCD(5,0) returns 5. A negative value returns `#NUM!`, and a non-numeric value returns `#VALUE!`.

Google Sheets also provides GCD with a first value and optional additional values or ranges. The Sheets help page does not state argument limits, the treatment of negative numbers or error messages, so check those details on the page before relying on them.

## Syntax

```excel
=GCD(number1, [number2], ...)
```

<!-- Image 1: Shared Factors of Two Values. See Images/Math & Trig/GCD.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first integer. In Sheets, this argument is named `value1` and can also be a range. |
| `number2`, ... | No | Additional integers, up to 255 values in total in Excel. Each value's decimal part is removed before the calculation. |

### Return Value

A number: the largest integer that divides every supplied value with no remainder. The result is 1 when the values share no factor greater than 1.

## Examples

### Example 1: Two Values

```excel
=GCD(24,36)
```

**Result:** `12`

Both 24 and 36 are multiples of 12 (2 × 12 and 3 × 12), and no larger whole number divides both.

### Example 2: Decimal Value Is Truncated

```excel
=GCD(12.7,8)
```

**Result:** `4`

The value 12.7 is treated as 12. The greatest common divisor of 12 and 8 is 4.

### Example 3: Zero Is Allowed

```excel
=GCD(5,0)
```

**Result:** `5`

Every integer divides zero, so the greatest common divisor is the other value, 5.

<!-- Image 2: Range Input With Three Values. See Images/Math & Trig/GCD.md -->

### Example 4: A Range of Values

With the values 48, 180 and 66 in `A2:A4`:

```excel
=GCD(A2:A4)
```

**Result:** `6`

The greatest common divisor of 48 and 180 is 12, and the greatest common divisor of 12 and 66 is 6.

## Story Problems

### Problem 1: Tile Layout for a Kitchen

A contractor must cover a kitchen floor measuring 96 inches by 60 inches with square tiles that fit both dimensions exactly, so that no tile is cut.

| Room | Width (inches) | Length (inches) |
| --- | --- | --- |
| Kitchen | 96 | 60 |

**Task:** Find the largest square tile side, in whole inches, that fits both dimensions exactly.

**Solution:**

```excel
=GCD(B2,C2)
```

**Answer:** `12`. Twelve-inch tiles fit 8 across (96 ÷ 12) and 5 down (60 ÷ 12), which is 40 tiles with no cuts.

### Problem 2: Equal Lengths of Ribbon

A craft shop has two ribbons, 84 centimeters and 126 centimeters long, and wants to cut both into the longest possible equal pieces with no leftover.

| Ribbon | Length (cm) |
| --- | --- |
| Red | 84 |
| Blue | 126 |

**Task:** Find the longest piece length that divides both ribbons exactly.

**Solution:**

```excel
=GCD(B2:B3)
```

**Answer:** `42`. The red ribbon yields 2 pieces and the blue ribbon yields 3 pieces, with nothing left over.

## Use Cases

### Tile Layout Planning

**Scenario:** A flooring estimator checks whether a room's dimensions allow a single tile size with no cuts.

```excel
=GCD(B2,C2)
```

**Why It Works:** The result is the largest tile side that divides both the width and the length. If the result is 1, only single-inch tiles fit exactly, so the layout needs cuts or a different tile.

### Cutting Material Lengths

**Scenario:** A workshop receives three cut lengths of wood trim, 20 cm, 30 cm and 45 cm, and wants the longest piece that cuts each length into whole pieces.

```excel
=GCD(B2:B4)
```

**Why It Works:** Passing the range returns the greatest common divisor of all three values, which is 5 cm. Each length then cuts into whole pieces of 5 cm.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | A value is negative. | Use ABS on the inputs if the sign has no meaning for the problem. |
| `#VALUE!` | A value is text rather than a number. | Convert the value to a number or correct the cell reference. |
| `1` | The values share no common factor greater than 1. | Confirm the inputs are correct. A result of 1 is a valid answer. |
| Unexpected result | A decimal part was removed before the calculation. | Enter whole numbers in source cells, or round the inputs on purpose first. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Up to 255 values. Non-integers are truncated. Negative values return `#NUM!`. |
| Google Sheets | Available | Accepts values and ranges. The help page does not document argument limits or the result for negative numbers. |

## Tips and Best Practices

- Pass a range instead of listing each cell when the number of values changes.
- Enter whole numbers in source cells so no decimal part is dropped without notice.
- Use GCD with LCM when two repeating schedules must be compared.
- Check for a result of 1 before assuming the inputs are wrong, because it means the values share no factor.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FACTDOUBLE](FACTDOUBLE.md) | Computes a double factorial, another integer-based function. |
| [LCM](LCM.md) | Returns the least common multiple, the companion to GCD. |
| [MOD](MOD.md) | Returns the remainder, which tests whether one value divides another. |
| [QUOTIENT](QUOTIENT.md) | Returns the whole-number part of a division. |

## Official Documentation

- [Microsoft Support: GCD function](https://support.microsoft.com/en-us/excel/functions/gcd-function)
- [Google Docs Editors Help: GCD](https://support.google.com/docs/answer/3093489)
