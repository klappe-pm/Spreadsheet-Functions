---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Rounding
purpose:
  - Rounding
use-case:
  - Hourly Rate Rounding
  - Negative Adjustment Rounding
related:
  - CEILING.PRECISE
  - FLOOR
  - FLOOR.MATH
  - INT
  - MROUND
  - ROUNDDOWN
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/floor-precise-function
  - https://support.google.com/docs/answer/9116270
date-created: 2026-11-22
date-revised: 2026-11-22
aliases: []
tags:
  - excel
  - negative-numbers
  - rounding
  - sheets
---

# FLOOR.PRECISE

## Description

**FLOOR.PRECISE** rounds a number down to the nearest integer, or to the nearest multiple of a significance value. The direction is always down, whatever the sign of the number. A negative number rounds down, away from zero, so FLOOR.PRECISE(-10.5,1) returns -11. A positive number such as 96 rounds down to a multiple of 10 as 90 with FLOOR.PRECISE(96,10).

FLOOR.PRECISE has no mode argument, so its behavior for negative numbers never changes. That makes it the right choice when every negative value should round down in the same way. For a function that rounds negative numbers toward zero, use FLOOR.MATH with a nonzero mode.

The significance argument is optional and defaults to 1. Its sign is ignored, so a negative significance behaves like its absolute value. If the number or the significance is 0, the result is 0. Microsoft lists FLOOR.PRECISE for Microsoft 365, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016.

## Syntax

```excel
=FLOOR.PRECISE(number, [significance])
```

<!-- Image 1: Number and Optional Significance. See Images/Math & Trig/FLOOR.PRECISE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value to round down. |
| `significance` | No | The multiple to round to. The default is 1. The sign of this argument is ignored, so only its size matters. |

### Return Value

A number: `number` rounded down to the nearest integer or to the nearest multiple of `significance`. The result is 0 when either argument is 0.

## Examples

### Example 1: Positive Number

```excel
=FLOOR.PRECISE(3.2,1)
```

**Result:** `3`

The value 3.2 rounds down to the nearest integer, which is 3.

### Example 2: Negative Number

```excel
=FLOOR.PRECISE(-3.2,1)
```

**Result:** `-4`

The negative value rounds down, away from zero, to the nearest integer below it, which is -4.

### Example 3: Multiple of 10

```excel
=FLOOR.PRECISE(96,10)
```

**Result:** `90`

The largest multiple of 10 that does not exceed 96 is 90.

<!-- Image 2: Rounding Down on Both Sides of Zero. See Images/Math & Trig/FLOOR.PRECISE.md -->

### Example 4: Decimal Multiple With a Negative Value

```excel
=FLOOR.PRECISE(-23.25,0.1)
```

**Result:** `-23.3`

The value -23.25 rounds down to the nearest multiple of 0.1 below it, which is -23.3.

## Story Problems

### Problem 1: Hourly Rates Rounded to Half Dollars

A staffing agency publishes hourly rates rounded down to the nearest 0.50 so that its rate card uses only half-dollar steps. The rates are in `B2:B4`.

| Role | Rate |
| --- | --- |
| Designer | 23.75 |
| Writer | 31.20 |
| Editor | 18.60 |

**Task:** Round each rate down to the nearest 0.50, then total the rounded rates.

**Solution:**

```excel
=SUMPRODUCT(FLOOR.PRECISE(B2:B4,0.5))
```

**Answer:** `73`. The rounded rates are 23.50, 31.00 and 18.50, which total 73.00.

### Problem 2: Negative Adjustments Rounded Down to Whole Dollars

A customer account carries three negative adjustments. The finance team rounds each one down to whole dollars, so every adjustment moves further from zero.

| Adjustment | Amount |
| --- | --- |
| Late fee | -10.5 |
| Refund | -3.2 |
| Credit | -7.9 |

**Task:** Round each adjustment down to a whole dollar, then total the results.

**Solution:**

```excel
=SUMPRODUCT(FLOOR.PRECISE(B2:B4))
```

**Answer:** `-23`. The rounded adjustments are -11, -4 and -8, which total -23.

## Use Cases

### Hourly Rate Rounding

**Scenario:** A rate card must show only half-dollar steps, and no rate may be quoted above the true hourly cost.

```excel
=FLOOR.PRECISE(B2,0.5)
```

**Why It Works:** The formula rounds down to the nearest half dollar, so the quoted rate never exceeds the calculated rate. Check that B2 holds a rate in dollars, not cents.

### Negative Adjustment Rounding

**Scenario:** An accounting team rounds every adjustment down to whole dollars, positive or negative, so that the rule is the same for each line.

```excel
=FLOOR.PRECISE(B2)
```

**Why It Works:** The direction is always down, so a credit of -7.9 becomes -8 and a charge of 7.9 becomes 7. Use ROUND instead when the rule should be nearest-value rounding.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unexpected result | A negative number moves further from zero, such as -3.2 becoming -4. | Expect this behavior, or use FLOOR.MATH with a nonzero mode if negatives should move toward zero. |
| `0` | The number or the significance is 0. | Check the source cell and the significance value. |
| `#VALUE!` | An argument is text rather than a number. | Convert the value to a number or correct the cell reference. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | The sign of significance is ignored, and negative numbers round down. |
| Google Sheets | Available | The same arguments and results. The help page gives examples such as FLOOR.PRECISE(-10.5,1) returning -11. |

## Tips and Best Practices

- Choose FLOOR.PRECISE when every value should round down, whatever its sign.
- Remember that the sign of significance is ignored, so -1 behaves the same as 1.
- Use CEILING.PRECISE when the value should round up instead.
- Use ROUND when you need ordinary nearest-value rounding.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CEILING.PRECISE](CEILING.PRECISE.md) | Rounds up, the opposite direction. |
| [FLOOR](FLOOR.md) | The older Excel function that rounds down with a required significance. |
| [FLOOR.MATH](FLOOR.MATH.md) | Rounds down with a mode argument that can move negative numbers toward zero. |
| [INT](INT.md) | Rounds down to an integer with no significance argument. |
| [MROUND](MROUND.md) | Rounds to the nearest multiple rather than always down. |
| [ROUNDDOWN](ROUNDDOWN.md) | Rounds toward zero to a set number of decimal places. |

## Official Documentation

- [Microsoft Support: FLOOR.PRECISE function](https://support.microsoft.com/en-us/excel/functions/floor-precise-function)
- [Google Docs Editors Help: FLOOR.PRECISE](https://support.google.com/docs/answer/9116270)
