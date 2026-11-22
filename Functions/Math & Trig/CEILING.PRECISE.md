---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Rounding
purpose:
  - Rounding
use-case:
  - Lot Size Rounding
  - Negative Adjustment Rounding
related:
  - CEILING
  - CEILING.MATH
  - FLOOR.PRECISE
  - ISO.CEILING
  - MROUND
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/ceiling-precise-function
  - https://support.google.com/docs/answer/9061294
date-created: 2026-11-22
date-revised: 2026-11-22
aliases: []
tags:
  - excel
  - negative-numbers
  - rounding
  - sheets
---

# CEILING.PRECISE

## Description

**CEILING.PRECISE** rounds a number up to the nearest integer or to the nearest multiple of a significance value. Its direction does not depend on the sign of the number: the value always moves up toward a larger number. For a positive number, that means away from zero. For a negative number, it means toward zero, so -4.3 becomes -4.

The significance argument is optional and defaults to 1. Microsoft states that the sign of the significance is ignored and only its absolute value is used, so `CEILING.PRECISE(4.3, -2)` returns the same result as `CEILING.PRECISE(4.3, 2)`. If either argument is zero, the result is zero.

Use CEILING.PRECISE when you want predictable rounding that does not change when the input turns negative. For a choice between rounding directions, use `CEILING.MATH` instead. Microsoft lists the function in Excel 2010 and later versions, including Excel for the web. Google Sheets provides it with the same arguments.

## Syntax

```excel
=CEILING.PRECISE(number, [significance])
```

<!-- Image 1: Always Up Rounding Rule. See Images/Math & Trig/CEILING.PRECISE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value to round. Positive and negative values are accepted. |
| `significance` | No | The multiple to round to. Defaults to 1 when omitted. Only its absolute value is used, so a negative significance behaves like the same positive value. |

### Return Value

A number equal to `number` rounded up toward a larger value, to the nearest integer or to the nearest multiple of `significance`. The result is 0 when `number` or `significance` is 0. The Microsoft page does not document any error conditions.

## Examples

### Example 1: Rounding a Positive Number Up

```excel
=CEILING.PRECISE(4.3)
```

**Result:** `5`

The value 4.3 rounds up to the next integer.

### Example 2: Rounding a Negative Number Toward Zero

```excel
=CEILING.PRECISE(-4.3)
```

**Result:** `-4`

The value -4.3 rounds up toward a larger value, which is -4.

### Example 3: Ignoring the Sign of Significance

```excel
=CEILING.PRECISE(4.3, -2)
```

**Result:** `6`

The significance of -2 is treated as 2, so 4.3 rounds up to the next multiple of 2, which is 6.

### Example 4: Negative Number With a Multiple

```excel
=CEILING.PRECISE(-4.3, 2)
```

**Result:** `-4`

The value -4.3 rounds up to -4, which is the nearest multiple of 2 above it.

### Example 5: Combined With Other Functions

```excel
=CEILING.PRECISE(-23.25, 0.1)
```

**Result:** `-23.2`

The value -23.25 divided by 0.1 is -232.5, which rounds up to -232. Multiplying back gives -23.2.

## Story Problems

### Problem 1: Lot Sizes for a Bottling Run

A bottler packs drinks in lots of 8. Each order must be filled with complete lots, so each quantity is rounded up to the next multiple of 8.

| Order | Bottles Wanted | Bottles to Fill |
| --- | --- | --- |
| Order A | 47 | |
| Order B | 16 | |
| Order C | 30 | |

**Task:** Round each order up to a full lot of 8 and total the bottles to fill.

**Solution:**

```excel
=CEILING.PRECISE(B2, 8)
```

Copy the formula down to row 4, then total column C with `=SUM(C2:C4)`.

**Answer:** The bottles to fill are 48, 16, and 32, for a total of `96`. Order B is already a full lot, so it does not change.

<!-- Image 2: Lot Size Rounding Table. See Images/Math & Trig/CEILING.PRECISE.md -->

### Problem 2: Negative Adjustments in Half Dollar Steps

An accounting team records adjustments in half dollar steps. Each negative adjustment is rounded up toward zero so the ledger never overstates the reduction.

| Adjustment | Amount | Rounded Amount |
| --- | --- | --- |
| Adjustment 1 | -17.36 | |
| Adjustment 2 | -3.20 | |

**Task:** Round each adjustment up to the next 0.50 step, then total the rounded amounts.

**Solution:**

```excel
=CEILING.PRECISE(B2, 0.5)
```

**Answer:** The rounded adjustments are -17.0 and -3.0, for a total of `-20.0`. Both negative values move toward zero.

<!-- Image 3: Negative Adjustment Results. See Images/Math & Trig/CEILING.PRECISE.md -->

## Use Cases

### Lot Size Rounding

**Scenario:** A manufacturer produces parts in batches of a fixed size and needs each order rounded up to a full batch.

```excel
=CEILING.PRECISE(Orders[Quantity], 8)
```

**Why It Works:** Each quantity is rounded up to the next full batch, so the production schedule always covers the order.

### Negative Adjustment Rounding

**Scenario:** A ledger records small reductions in half dollar steps, and the reductions must round toward zero.

```excel
=CEILING.PRECISE(Adjustments[Amount], 0.5)
```

**Why It Works:** The rounding direction stays the same for negative amounts, so the function never pushes a reduction past its exact value.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Negative result smaller than expected | The number is negative, so it rounds toward zero. | Confirm that the upward direction is the one you need. Use `CEILING.MATH` with a mode when negatives must round away from zero. |
| Sign of significance ignored | The significance was entered as a negative number. | Enter a positive significance, since only its absolute value is used. |
| `#VALUE!` | One of the arguments is text. | Convert the value to a number before rounding. |
| Result is 0 | The significance is 0 or the number is 0. | Check that the significance cell holds the multiple you intend. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365, Excel for the web, Excel 2024, Excel 2021, Excel 2019, and Excel 2016 | Only the absolute value of significance is used. Negative numbers round toward zero. |
| Google Sheets | Available | Uses the same arguments, and the Google page also shows negative numbers rounding toward zero. |

## Tips and Best Practices

- Use CEILING.PRECISE when the rounding direction must not depend on the sign of the number.
- Enter the significance as a positive number so the intent is clear to readers.
- Keep the significance in its own cell so batch sizes or lot sizes can change without editing formulas.
- Test one negative input by hand before you apply the formula to a full column.
- Use `CEILING.MATH` when negative numbers must round away from zero.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CEILING](CEILING.md) | Older function with a required significance argument. |
| [CEILING.MATH](CEILING.MATH.md) | Adds a mode argument that controls how negative numbers round. |
| [FLOOR.PRECISE](../Math%20%26%20Trig/FLOOR.PRECISE.md) | Rounds down to the nearest multiple, the opposite direction. |
| [ISO.CEILING](../Math%20%26%20Trig/ISO.CEILING.md) | Rounds up to a multiple using ISO rules. |
| [MROUND](../Math%20%26%20Trig/MROUND.md) | Rounds to the nearest multiple in either direction. |

## Official Documentation

- [Microsoft Support: CEILING.PRECISE function](https://support.microsoft.com/en-us/excel/functions/ceiling-precise-function)
- [Google Docs Editors Help: CEILING.PRECISE](https://support.google.com/docs/answer/9061294)
