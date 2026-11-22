---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Number Theory
purpose:
  - Arithmetic Operations
use-case:
  - Shift Rotation Planning
  - Transit Schedule Alignment
related:
  - GCD
  - MOD
  - QUOTIENT
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/lcm-function
  - https://support.google.com/docs/answer/3093421
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Least Common Multiple
tags:
  - excel
  - multiples
  - number-theory
  - sheets
---

# LCM

## Description

**LCM** returns the least common multiple of one or more integers: the smallest positive whole number that is a multiple of every value. For example, LCM(4,6) returns 12, because 12 is the first number that both 4 and 6 divide evenly. Use LCM to find when repeating cycles line up again. Two events that repeat every 4 days and every 6 days coincide every 12 days.

In Excel, LCM accepts up to 255 values. Decimal parts are removed before the calculation, so 4.5 is treated as 4. A negative value returns `#NUM!`, and a non-numeric value returns `#VALUE!`. If the result would reach 2^53 or more, Excel also returns `#NUM!`, so very large inputs can fail even when each value is small.

Google Sheets provides LCM with a first value and optional additional values or ranges. Its help page truncates decimal parts in the same way, but it does not state argument limits or the treatment of negative numbers, so check the page before relying on those details.

## Syntax

```excel
=LCM(number1, [number2], ...)
```

<!-- Image 1: Repeating Cycles Lining Up. See Images/Math & Trig/LCM.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first integer. In Sheets, this argument is named `value1` and can also be a range. |
| `number2`, ... | No | Additional integers, up to 255 values in total in Excel. Decimal parts are removed before the calculation. |

### Return Value

A number: the smallest positive integer that is a multiple of every supplied value. Excel returns `#NUM!` for negative values and for results of 2^53 or more.

## Examples

### Example 1: Two Values

```excel
=LCM(4,6)
```

**Result:** `12`

The multiples of 4 are 4, 8, 12, and the multiples of 6 are 6, 12. The first common multiple is 12.

### Example 2: Three Values

```excel
=LCM(3,5,7)
```

**Result:** `105`

The three values share no factors, so the result is their product, 3 × 5 × 7 = 105.

### Example 3: Shared Factors Reduce the Result

```excel
=LCM(6,8,12)
```

**Result:** `24`

The value 12 already contains the factors of 6, and 8 contributes the extra factor of 2 needed for 24.

<!-- Image 2: Three Schedules and the Shared Day. See Images/Math & Trig/LCM.md -->

### Example 4: Values From a Range

With the intervals 15, 20 and 30 in `A2:A4`:

```excel
=LCM(A2:A4)
```

**Result:** `60`

The least common multiple of 15 and 20 is 60, and 60 is also a multiple of 30.

## Story Problems

### Problem 1: Maintenance Crew Rotations

Two maintenance crews repeat their rotations on fixed cycles. Crew A starts a rotation every 4 days, and Crew B starts one every 6 days. Both crews start on day 0.

| Crew | Cycle (days) |
| --- | --- |
| Crew A | 4 |
| Crew B | 6 |

**Task:** Find how many days pass until both crews start a rotation on the same day again.

**Solution:**

```excel
=LCM(B2:B3)
```

**Answer:** `12`. Both crews start a rotation on day 12, the first day that is a multiple of both 4 and 6.

### Problem 2: Bus Departures at a Shared Stop

Two bus routes leave the same stop at fixed intervals. Route 1 departs every 15 minutes and Route 2 every 20 minutes. Both buses leave at the same time at the start of service.

| Route | Interval (minutes) |
| --- | --- |
| Route 1 | 15 |
| Route 2 | 20 |

**Task:** Find how many minutes pass until both buses depart from the stop together again.

**Solution:**

```excel
=LCM(B2:B3)
```

**Answer:** `60`. Both buses depart together every 60 minutes.

## Use Cases

### Shift Rotation Planning

**Scenario:** A plant schedules two teams on different rotation lengths and needs to know when the teams work their first shift together again.

```excel
=LCM(B2,B3)
```

**Why It Works:** The result is the first day both cycles restart together. Use the result as the length of the full planning period, then repeat the pattern across it.

### Transit Schedule Alignment

**Scenario:** A transit planner checks when three routes with intervals of 10, 15 and 20 minutes all depart from a transfer point together.

```excel
=LCM(B2:B4)
```

**Why It Works:** The result of 60 minutes shows that a full alignment happens once an hour. Larger sets of intervals produce much larger results, so check the output for reasonable size.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | A value is negative. | Use ABS on the inputs if the sign has no meaning for the problem. |
| `#NUM!` | The result would reach 2^53 or more. | Split the values into smaller sets, or check whether the inputs are correct. |
| `#VALUE!` | A value is text rather than a number. | Convert the value to a number or correct the cell reference. |
| Unexpected result | A decimal part was removed, so 4.5 was treated as 4. | Enter whole numbers in source cells. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Up to 255 values. Non-integers are truncated. Negative values and results of 2^53 or more return `#NUM!`. |
| Google Sheets | Available | Accepts values and ranges. The help page truncates non-integers but does not document argument limits or negative values. |

## Tips and Best Practices

- Pass a range when the list of cycles changes, instead of editing the formula each time.
- Enter whole-number cycle lengths so that no decimal part is dropped without notice.
- Use GCD with LCM when comparing repeating schedules, because the two results describe the same shared structure.
- Check the size of the result when many values are combined, since the least common multiple grows quickly.

## Related Functions

| Function | Relationship |
| --- | --- |
| [GCD](GCD.md) | Returns the greatest common divisor, the companion to LCM. |
| [MOD](MOD.md) | Returns the remainder, which tests whether a value is a multiple of another. |
| [QUOTIENT](QUOTIENT.md) | Returns the whole-number part of a division, useful for counting full cycles. |

## Official Documentation

- [Microsoft Support: LCM function](https://support.microsoft.com/en-us/excel/functions/lcm-function)
- [Google Docs Editors Help: LCM](https://support.google.com/docs/answer/3093421)
