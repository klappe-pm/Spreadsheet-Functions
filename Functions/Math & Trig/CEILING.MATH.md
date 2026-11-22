---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Rounding
purpose:
  - Rounding
use-case:
  - Credit Note Rounding
  - Shipping Weight Rounding
related:
  - CEILING
  - CEILING.PRECISE
  - FLOOR.MATH
  - ISO.CEILING
  - ROUNDUP
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/ceiling-math-function
  - https://support.google.com/docs/answer/9061515
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Round Up With Mode
tags:
  - excel
  - negative-numbers
  - rounding
  - sheets
---

# CEILING.MATH

## Description

**CEILING.MATH** rounds a number up to the nearest integer or to the nearest multiple of a significance value. It is the modern version of `CEILING` and adds a third argument, `mode`, that controls which way negative numbers round.

Positive numbers always round up, and `mode` has no effect on them. For negative numbers, the default rounds toward zero, so -8.1 rounded to a multiple of 2 becomes -8. Set `mode` to any nonzero value to make negative numbers round away from zero, so -8.1 becomes -10. Use this when a credit, a refund, or a loss must grow in size instead of shrinking.

Both significance and mode are optional. Significance defaults to 1, so `CEILING.MATH(6.7)` returns 7. Microsoft lists the function in Excel 2016 and later, including Excel for the web. Google Sheets accepts the same arguments.

## Syntax

```excel
=CEILING.MATH(number, [significance], [mode])
```

<!-- Image 1: Mode Effect on Negative Numbers. See Images/Math & Trig/CEILING.MATH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value to round. Positive and negative values are accepted. |
| `significance` | No | The multiple to round to. Defaults to 1 when omitted. A value of 0 returns 0. |
| `mode` | No | Sets the direction for negative numbers. A zero or an omitted value rounds toward zero. Any nonzero value rounds away from zero. Mode does not change how positive numbers round. |

### Return Value

A number equal to `number` rounded up to the nearest integer or to the nearest multiple of `significance`, with the direction for negative values set by `mode`. The Microsoft page documents the valid range of `number` as roughly -2.229E-308 to 9.99E+307 and lists no other error cases.

## Examples

### Example 1: Rounding Up to a Multiple

```excel
=CEILING.MATH(24.3, 5)
```

**Result:** `25`

The value 24.3 rounds up to the next multiple of 5.

### Example 2: Rounding Up to the Next Integer

```excel
=CEILING.MATH(6.7)
```

**Result:** `7`

With no significance, the function rounds up to the next integer.

### Example 3: Negative Number Rounding Toward Zero

```excel
=CEILING.MATH(-8.1, 2)
```

**Result:** `-8`

The default mode moves -8.1 toward zero to the nearest multiple of 2, which is -8.

### Example 4: Negative Number Rounding Away From Zero

```excel
=CEILING.MATH(-8.1, 2, 1)
```

**Result:** `-10`

A nonzero mode moves -8.1 away from zero to the next multiple of 2 below it, which is -10.

### Example 5: Combined With Other Functions

```excel
=CEILING.MATH(-42, 10, -1)
```

**Result:** `-50`

A negative mode also rounds away from zero, so -42 becomes -50 at a significance of 10.

## Story Problems

### Problem 1: Shipping Weights in Half Kilograms

A courier charges by the half kilogram. Each parcel weight is rounded up to the next 0.5 kg before the charge is calculated.

| Parcel | Weight (kg) | Charged Weight (kg) |
| --- | --- | --- |
| P1 | 3.2 | |
| P2 | 7.9 | |
| P3 | 4.1 | |
| P4 | 10.0 | |

**Task:** Round each weight up to the next 0.5 kg and total the charged weights.

**Solution:**

```excel
=CEILING.MATH(B2, 0.5)
```

Copy the formula down to row 5, then total column C with `=SUM(C2:C5)`.

**Answer:** The charged weights are 3.5, 8.0, 4.5, and 10.0 kg, for a total of `26.0` kg. Parcel P4 is already on a step, so it does not change.

<!-- Image 2: Half Kilogram Rounding Table. See Images/Math & Trig/CEILING.MATH.md -->

### Problem 2: Rounding Credit Notes to Whole Dollars

A billing team issues credit notes in whole dollars. Credits are rounded away from zero, so a customer never receives less than the exact credit.

| Credit | Amount | Whole Dollar Credit |
| --- | --- | --- |
| Refund A | -12.40 | |
| Refund B | -7.25 | |

**Task:** Round each credit to a whole dollar away from zero, then total the credits.

**Solution:**

```excel
=CEILING.MATH(B2, 1, 1)
```

**Answer:** The whole dollar credits are -13 and -8, for a total of `-21`. A nonzero mode rounds both negative values away from zero.

<!-- Image 3: Credit Note Rounding Results. See Images/Math & Trig/CEILING.MATH.md -->

## Use Cases

### Shipping Weight Rounding

**Scenario:** A freight company bills each shipment by the next half kilogram, even when the scale shows a smaller weight.

```excel
=CEILING.MATH(Shipments[Weight], 0.5)
```

**Why It Works:** Positive weights always round up, so the mode argument is not needed. Every shipment is billed on a fixed step.

### Credit Note Rounding

**Scenario:** A finance team issues credit notes in whole dollars and wants refunds to round away from zero.

```excel
=CEILING.MATH(Credits[Amount], 1, 1)
```

**Why It Works:** The mode of 1 pushes negative amounts away from zero, so each credit is rounded in the customer's favor. Set the mode to 0 or leave it out for the default behavior.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Negative result smaller than expected | The mode is zero or omitted, so negatives round toward zero. | Set the mode to 1 or any nonzero value. |
| Unexpected whole number | The significance was omitted, so the default of 1 applies. | Pass the required significance explicitly. |
| `#VALUE!` | The number argument is text. | Convert the value to a number before rounding. |
| Confusion about significance | The argument description on the Microsoft page refers to decimal places, but the remarks describe a multiple. | Treat significance as the multiple to round to, as the examples show. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365, Excel 2024, Excel 2021, Excel 2019, Excel 2016, and Excel for the web | Mode 0 or omitted rounds negatives toward zero. Any nonzero mode rounds them away from zero. |
| Google Sheets | Available | Uses the same arguments. A blank or 0 mode rounds negatives toward zero, and any other value rounds them away. |

## Tips and Best Practices

- Leave mode out for positive-only data, since it has no effect there.
- Use mode 1 when negative amounts represent refunds or losses that must be rounded in the holder's favor.
- Keep significance in a separate cell so the rounding step can change without editing formulas.
- Test one negative input by hand before you apply the formula to a full column.
- Use `CEILING.PRECISE` when you want negatives to round toward zero with no mode setting.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CEILING](CEILING.md) | Older function that rounds up without a mode argument. |
| [CEILING.PRECISE](CEILING.PRECISE.md) | Always rounds up toward positive infinity and ignores the sign of significance. |
| [FLOOR.MATH](../Math%20%26%20Trig/FLOOR.MATH.md) | Rounds down to the nearest multiple, with its own mode argument. |
| [ISO.CEILING](../Math%20%26%20Trig/ISO.CEILING.md) | Rounds up to a multiple using ISO rules. |
| [ROUNDUP](../Math%20%26%20Trig/ROUNDUP.md) | Rounds away from zero to a number of decimal places. |

## Official Documentation

- [Microsoft Support: CEILING.MATH function](https://support.microsoft.com/en-us/excel/functions/ceiling-math-function)
- [Google Docs Editors Help: CEILING.MATH](https://support.google.com/docs/answer/9061515)
