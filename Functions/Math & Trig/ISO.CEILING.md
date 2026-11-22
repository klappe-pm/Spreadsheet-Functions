---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Rounding
purpose:
  - Rounding
use-case:
  - Pallet Fill Quantities
  - Shelf Length Planning
related:
  - CEILING
  - CEILING.MATH
  - CEILING.PRECISE
  - FLOOR.PRECISE
  - MROUND
  - ROUNDUP
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/iso-ceiling-function
  - https://support.google.com/docs/answer/9061294
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - ceiling
  - excel
  - rounding
  - sheets
---

# ISO.CEILING

## Description

**ISO.CEILING** rounds a number up to the nearest integer, or to the nearest multiple of a significance value. Rounding always goes up, whatever the sign of the number. For example, ISO.CEILING(4.3) returns 5, and ISO.CEILING(4.3,2) returns 6, the smallest multiple of 2 that is not below 4.3.

For a negative number, rounding up moves the value toward zero. ISO.CEILING(-4.3) returns -4. The sign of the significance is ignored, so ISO.CEILING(4.3,-2) returns the same result as ISO.CEILING(4.3,2). If the number or the significance is 0, the result is 0.

Use ISO.CEILING when a quantity must cover a requirement, such as filling a pallet or buying enough shelf length. For the opposite direction, use FLOOR.PRECISE. Microsoft lists ISO.CEILING for Microsoft 365, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016.

## Syntax

```excel
=ISO.CEILING(number, [significance])
```

<!-- Image 1: Number and Optional Significance. See Images/Math & Trig/ISO.CEILING.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value to round up. |
| `significance` | No | The multiple to round to. The default is 1. The sign of this argument is ignored. |

### Return Value

A number: `number` rounded up to the nearest integer or to the nearest multiple of `significance`. The result is 0 when either argument is 0.

## Examples

### Example 1: Round Up to an Integer

```excel
=ISO.CEILING(4.3)
```

**Result:** `5`

Significance defaults to 1, so 4.3 rounds up to the next integer, which is 5.

### Example 2: Round Up to a Multiple

```excel
=ISO.CEILING(4.3,2)
```

**Result:** `6`

The smallest multiple of 2 that is not below 4.3 is 6.

### Example 3: Negative Number

```excel
=ISO.CEILING(-4.3)
```

**Result:** `-4`

Rounding up moves -4.3 toward zero, which gives -4.

<!-- Image 2: Rounding Up to a Multiple of 8. See Images/Math & Trig/ISO.CEILING.md -->

### Example 4: Full Pallets of Eight Cartons

```excel
=ISO.CEILING(50,8)
```

**Result:** `56`

Seven full pallets hold 56 cartons, the smallest multiple of 8 that covers 50 cartons.

## Story Problems

### Problem 1: Pallets for Carton Orders

A distributor packs cartons onto pallets that hold exactly 8 cartons each. Three orders are listed in `B2:B4`, and each order must fill whole pallets.

| Order | Cartons |
| --- | --- |
| North | 50 |
| South | 61 |
| East | 16 |

**Task:** Round each order up to a multiple of 8, then total the cartons that must be loaded.

**Solution:**

```excel
=SUMPRODUCT(ISO.CEILING(B2:B4,8))
```

**Answer:** `136`. The rounded orders are 56, 64 and 16, which total 136 cartons.

### Problem 2: Shelf Lengths in Full Steps

A hardware store cuts shelf boards only in steps of 4 centimeters. The required lengths are in `B2:B4`.

| Shelf | Required Length (cm) |
| --- | --- |
| A | 13 |
| B | 22 |
| C | 30 |

**Task:** Round each length up to the next multiple of 4 centimeters, then total the board lengths to order.

**Solution:**

```excel
=SUMPRODUCT(ISO.CEILING(B2:B4,4))
```

**Answer:** `72`. The rounded lengths are 16, 24 and 32 centimeters, which total 72 centimeters.

## Use Cases

### Pallet Fill Quantities

**Scenario:** A warehouse supervisor needs to know how many cartons to load so that each pallet is complete.

```excel
=ISO.CEILING(B2,8)
```

**Why It Works:** The result is the smallest multiple of 8 that covers the order. The extra cartons are a deliberate buffer, so review the figure before it is used for purchasing.

### Shelf Length Planning

**Scenario:** A carpenter buys board in 4 cm steps and needs the length to cover each shelf.

```excel
=ISO.CEILING(B2,4)
```

**Why It Works:** Rounding up guarantees the board is at least as long as the requirement. A 22 cm shelf uses a 24 cm board, and the offcut is trimmed after cutting.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unexpected result | The value is rounded up when a lower value was expected. | Use FLOOR.PRECISE or ROUNDDOWN for the downward direction. |
| `0` | The number or the significance is 0. | Check the source cell and the significance value. |
| `#VALUE!` | An argument is text rather than a number. | Convert the value to a number or correct the cell reference. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Rounds up regardless of sign. The sign of significance is ignored. |
| Google Sheets | Available | The help page for this name points to the CEILING.PRECISE page, which has the same number and significance arguments and describes negative values rounding up toward zero, as ISO.CEILING does. |

## Tips and Best Practices

- Use ISO.CEILING when the quantity must meet or exceed a requirement.
- Remember that the sign of significance is ignored, so a negative significance gives the same result as a positive one.
- Store the significance in a labeled cell, such as pallet size or step length, so the rule is easy to change.
- Review rounded-up quantities before ordering, because the buffer can be large for big multiples.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CEILING](CEILING.md) | The older rounding-up function in the Math & Trig category. |
| [CEILING.MATH](CEILING.MATH.md) | Rounds up with a mode argument for negative numbers. |
| [CEILING.PRECISE](CEILING.PRECISE.md) | Rounds up with the sign of significance ignored, as ISO.CEILING does. |
| [FLOOR.PRECISE](FLOOR.PRECISE.md) | Rounds down, the opposite direction. |
| [MROUND](MROUND.md) | Rounds to the nearest multiple rather than always up. |
| [ROUNDUP](ROUNDUP.md) | Rounds away from zero to a set number of decimal places. |

## Official Documentation

- [Microsoft Support: ISO.CEILING function](https://support.microsoft.com/en-us/excel/functions/iso-ceiling-function)
- [Google Docs Editors Help: ISO.CEILING](https://support.google.com/docs/answer/9061294)
